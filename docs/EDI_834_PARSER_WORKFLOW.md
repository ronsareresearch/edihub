# EDI 834 Parser Workflow Explanation

## Overview
This document explains how the EDI 834 parser works with base config files and client-specific config files.

## 1. Configuration File Hierarchy

```
configs/
├── base_edi834_config.yaml          # Base EDI 834 standard (ASC X12N 834)
├── loops/
│   ├── loop_transactional.yaml      # ST, BGN, REF, DTP, QTY, SE
│   ├── loop_1000A.yaml              # SPONSOR NAME (N1)
│   ├── loop_1000B.yaml              # PAYER (N1)
│   ├── loop_2000.yaml               # MEMBER LEVEL (INS, REF, DTP)
│   ├── loop_2100A.yaml              # MEMBER NAME (NM1, DMG, PER, etc.)
│   ├── loop_2300.yaml               # HEALTH COVERAGE (HD, DTP, AMT, REF)
│   └── ... (all other loops)
├── validation/
│   ├── file_level.yaml              # File-level validation rules
│   ├── field_level.yaml             # Field-level validation rules (data types, formats)
│   └── syntax_rules.yaml            # Syntax validation rules (P, C, R, E rules)
└── clients/
    ├── virginia_medicaid_834_config.yaml        # Client customizations (structure)
    └── virginia_medicaid_business_rules.yaml    # Client business rules (validations)
```

## 2. Initialization Phase (When Parser Starts)

### Step 1: Load Base Configuration
```python
# YamlConfigAdapter834 loads:
1. base_edi834_config.yaml → Control segments (ISA, GS, GE, IEA, ST, SE)
2. loops/*.yaml → All loop definitions with segments and elements
```

**What's in base config:**
- Segment definitions (INS, NM1, HD, REF, DTP, etc.)
- Element definitions (INS01, INS02, etc.)
- Usage codes: `['R']` = Required, `['S']` = Situational
- Data types: `AN`, `ID`, `DT`, `N`, etc.
- Length constraints: `min_length`, `max_length`
- Qualifier values: Allowed values for ID-type elements
- Syntax rules: `P0102`, `R0203`, `C0504`, etc.

### Step 2: Load Client-Specific Configuration
```python
# For client_id=1 (Virginia Medicaid):
1. clients/virginia_medicaid_834_config.yaml → Customizations
2. clients/virginia_medicaid_business_rules.yaml → Business rules
```

**What client configs override:**
- Additional qualifier values (e.g., DTP01: "356", "357" for Virginia Medicaid)
- Custom segments in specific loops
- Element mappings for data transformation
- Loop structure customizations (e.g., LS/LE boundaries for Loop 2700)

**What business rules add:**
- Required values (e.g., ISA06 must be "VAMMIS FA")
- Allowed values per client (e.g., INS03: ["021", "024", "030"])
- Format validations (e.g., GS03 must be 4-digit numeric)
- Client-specific validation messages

### Step 3: Merge Configurations
```python
# YamlConfigAdapter834.transform_to_parser_format():
1. Start with base config (all loops from loops/*.yaml)
2. Apply client customizations (override/add qualifiers, segments)
3. Result: Merged config with base + client overrides
```

## 3. Parsing Flow (Processing EDI File Line by Line)

### Phase 1: File-Level Validation
```
EDI File → Parse ISA → Parse GS → Parse ST
         ↓
    FileLevelValidator834
    - Checks: ISA/GS/GE/IEA control numbers match
    - Checks: Required segments present (usage: ['R'])
    - Checks: Segment counts match
```

### Phase 2: Segment-by-Segment Parsing

For each segment in the EDI file:

```
Segment Line (e.g., "INS*Y*18*021*XN*A...")
    ↓
1. Detect Loop Context
   YamlLoopDetector834.detect_loop()
   - Determines: Is this segment starting a new loop? (2000, 2100A, etc.)
   - Uses: Loop order from config
   
    ↓
2. Parse Segment Elements
   Parser extracts elements using delimiters (*, :, ~)
   
    ↓
3. Validate Each Element (Multi-Layer Validation)
   
   a) Syntax Validator (SyntaxValidator834)
      - Checks: Element is required (usage: ['M'])
      - Checks: Element length (min/max)
      - Checks: Syntax rules (P, C, R, E) - WARNING if violated
   
   b) Field-Level Validator (FieldLevelValidator834)
      - Checks: Data type format (AN, ID, DT, etc.) - WARNING if mismatch
      - Checks: Required segments (usage: ['R']) - ERROR if missing
      - Uses: field_level.yaml rules
   
   c) Business Rules Validator (BusinessRulesValidator834)
      - Checks: Client-specific required values (e.g., ISA06="VAMMIS FA")
      - Checks: Client-specific allowed values (e.g., INS03=["021","024","030"])
      - Checks: Format validations (e.g., GS03=4-digit numeric)
      - Uses: clients/*_business_rules.yaml rules
   
    ↓
4. Apply Syntax Rules (After All Elements in Segment)
   SyntaxValidator834.validate_segment_syntax_rules()
   - Validates: P rules (Paired), C rules (Conditional), R rules (Required), E rules (Exclusive)
   - Example: P0102 means "If INS01 or INS02 present, then the other is required"
   - Severity: WARNING (not error)
   
    ↓
5. Store Parsed Data
   - Add to JSON structure in memory
   - Track loop context (current_loop_id)
```

## 4. Validation Hierarchy

### Validation Order (from most generic to most specific):

```
1. FILE-LEVEL VALIDATIONS (FileLevelValidator834)
   ├── Source: validation/file_level.yaml
   ├── Checks: Control segments, segment counts, envelope integrity
   └── Severity: ERROR

2. SYNTAX VALIDATIONS (SyntaxValidator834)
   ├── Source: loops/*.yaml (syntax codes) + validation/syntax_rules.yaml
   ├── Checks: Element presence, length, syntax rules (P/C/R/E)
   └── Severity: ERROR (missing required) / WARNING (syntax violations)

3. FIELD-LEVEL VALIDATIONS (FieldLevelValidator834)
   ├── Source: validation/field_level.yaml + loops/*.yaml (metadata)
   ├── Checks: Data types, formats, required segments
   └── Severity: WARNING (data type mismatch) / ERROR (required segment missing)

4. BUSINESS RULES VALIDATIONS (BusinessRulesValidator834)
   ├── Source: clients/*_business_rules.yaml
   ├── Checks: Client-specific required/allowed values, formats
   └── Severity: ERROR / WARNING / INFO (per rule)
```

## 5. Example: Parsing INS Segment in Loop 2000

### EDI Line:
```
INS*Y*18*021*XN*A*FT*N*AI*00123456789**M*C*N...
```

### Parsing Steps:

**Step 1: Detect Loop**
- Previous segment ended Loop 1000B
- INS segment detected → Starts Loop 2000
- `current_loop_id = "2000"`

**Step 2: Parse Elements**
```
INS01 = "Y"
INS02 = "18"
INS03 = "021"
INS04 = "XN"
...
```

**Step 3: Validate Each Element**

For INS01:
- **Syntax Validator**: ✅ Required element present, length OK
- **Field Validator**: ✅ Data type ID is valid, value "Y" is in qualifier list
- **Business Rules**: ✅ (No client-specific rule for INS01)

For INS03:
- **Syntax Validator**: ✅ Element present, length OK
- **Field Validator**: ✅ Data type ID, length OK
- **Business Rules**: ✅ Value "021" in allowed list ["021","024","030"] for Virginia Medicaid

**Step 4: Validate Segment Syntax**
- Check syntax rules for INS segment in Loop 2000
- Example: P1112 (If INS11 or INS12 present, then the other is required)
- If violated → WARNING (not error)

**Step 5: Store Data**
```json
{
  "loop_2000": {
    "ins01_yes_no_indicator": "Y",
    "ins02_individual_relationship_code": "18",
    "ins03_maintenance_type_code": "021",
    "ins04_maintenance_reason_code": "XN",
    ...
  }
}
```

## 6. How Client Configs Override Base Configs

### Example 1: DTP Segment in Loop 2000

**Base Config (loop_2000.yaml):**
```yaml
- segment_code: DTP
  elements:
    - ref_designator: DTP01
      qualifier: [336, 337, 348, 349, ...]  # Standard qualifiers
```

**Client Config (virginia_medicaid_834_config.yaml):**
```yaml
segments:
  - segment_code: "DTP"
    loop_context: "2000"
    custom_elements:
      - ref_designator: "DTP01"
        qualifier_values: ["356", "357"]  # Virginia-specific qualifiers
```

**Result**: Parser accepts base qualifiers AND client-specific qualifiers ["356", "357"]

### Example 2: REF Segment Required Value

**Base Config**: REF*38 is situational (usage: ['S'])

**Client Business Rules (virginia_medicaid_business_rules.yaml):**
```yaml
- rule_id: "BIZ_VM_008"
  segment: "REF"
  loop: "header"
  element: "REF01"
  required_value: "38"
  severity: "error"
```

**Result**: For Virginia Medicaid, REF*38 in header is REQUIRED (error if missing)

## 7. Complete Workflow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    INITIALIZATION                            │
├─────────────────────────────────────────────────────────────┤
│ 1. Load Base Config (base_edi834_config.yaml)               │
│ 2. Load All Loop Configs (loops/*.yaml)                     │
│ 3. Load Validation Rules (validation/*.yaml)                │
│ 4. Load Client Config (clients/*_834_config.yaml)           │
│ 5. Load Client Business Rules (clients/*_business_rules.yaml)│
│ 6. Merge: Base + Client Overrides = Final Config            │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                    FILE PARSING                              │
├─────────────────────────────────────────────────────────────┤
│  For each line in EDI file:                                 │
│                                                              │
│  Line → Detect Segment → Detect Loop Context                │
│    ↓                                                         │
│  Parse Elements (split by delimiters)                       │
│    ↓                                                         │
│  ┌──────────────────────────────────────────┐              │
│  │     MULTI-LAYER VALIDATION                │              │
│  ├──────────────────────────────────────────┤              │
│  │ 1. Syntax Validator                       │              │
│  │    - Required? Length?                    │              │
│  │ 2. Field-Level Validator                  │              │
│  │    - Data type? Format?                   │              │
│  │ 3. Business Rules Validator               │              │
│  │    - Client-specific rules?               │              │
│  └──────────────────────────────────────────┘              │
│    ↓                                                         │
│  Apply Syntax Rules (P/C/R/E)                               │
│    ↓                                                         │
│  Store Parsed Data (JSON structure)                         │
│    ↓                                                         │
│  Collect Errors/Warnings                                     │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                    FINALIZATION                              │
├─────────────────────────────────────────────────────────────┤
│ 1. File-Level Validation (control numbers, counts)          │
│ 2. Generate Validation Report                               │
│    - Errors: Blocking issues (required missing, etc.)       │
│    - Warnings: Non-blocking issues (format, syntax)         │
│ 3. Return Parsed JSON + Validation Results                  │
└─────────────────────────────────────────────────────────────┘
```

## 8. Key Points

1. **Base Config = EDI Standard**: Defines standard EDI 834 structure per ASC X12N
2. **Client Config = Customizations**: Overrides/adds to base for client-specific needs
3. **Validation is Layered**: Multiple validators check the same data with different rules
4. **Errors vs Warnings**: 
   - **ERROR**: Blocks processing (required segment/element missing, invalid required value)
   - **WARNING**: Non-blocking (data type mismatch, syntax violation, format issue)
5. **All in Memory**: No database writes during parsing - builds JSON structure
6. **Config Caching**: Configs are loaded once and cached for performance

## 9. Example: Full Flow for Virginia Medicaid File

```
1. Parser initialized with client_id=1
   → Loads base_edi834_config.yaml
   → Loads all loops/*.yaml
   → Loads virginia_medicaid_834_config.yaml
   → Loads virginia_medicaid_business_rules.yaml
   → Merges configs

2. File arrives: "ISA*00*...*VAMMIS FA*..."
   → Parse ISA segment
   → Validate ISA06 = "VAMMIS FA" (Business Rule BIZ_VM_003) ✅
   → Validate ISA16 = ">" (Business Rule BIZ_VM_004) ✅

3. Segment: "INS*Y*18*021*XN*..."
   → Detect: Loop 2000
   → Parse elements
   → Validate INS03 = "021" in ["021","024","030"] (Business Rule BIZ_VM_012) ✅
   → Validate INS04 = "XN" for Transportation (Business Rule BIZ_VM_013) ✅

4. Segment: "REF*0F*123456789"
   → Still in Loop 2000
   → Validate REF01 = "0F" required (Business Rule BIZ_VM_014) ✅

5. Segment: "DTP*356*D8*20240101"
   → Still in Loop 2000
   → Validate DTP01 = "356" in allowed qualifiers (Client Config) ✅

6. Continue parsing all segments...

7. Final validation report shows:
   - 0 Errors (all required elements present, all business rules passed)
   - 2 Warnings (syntax rule P0102 violated, data type format issue)
```

This architecture allows the parser to:
- Support standard EDI 834 files (using base config)
- Support client-specific customizations (using client configs)
- Provide comprehensive validation (multiple layers)
- Remain flexible and maintainable (YAML-based, no database dependencies)

---

## 10. Complete Services Architecture

The EDI 834 parser uses multiple service files, each with a specific responsibility. Here's how they all work together:

### Service Files Overview

```
edibackend/app/services/
├── CORE PARSER SERVICES (2 files)
│   ├── treo_base_parser_834.py         ✅ Main parser (consolidated: base + hybrid + JSON building)
│   └── treo_parser_834.py              ✅ Complete Treo workflow orchestrator
│
├── CONFIGURATION SERVICES (3 files)
│   ├── config_loader_834.py            ✅ Loads/caches client configs (includes yaml_config_adapter functionality)
│   ├── yaml_metadata_adapter_834.py    ✅ Provides element/segment metadata
│   └── yaml_validation_loader_834.py   ✅ Loads validation rules from YAML
│
├── VALIDATION SERVICES (5 files)
│   ├── validation_pipeline_834.py      ✅ NEW: 3-stage validation orchestrator (file → field → syntax/business)
│   ├── validation_cache_834.py         ✅ NEW: Validation result caching for performance
│   ├── file_level_validator_834.py     ✅ File-level validations (ISA/GS/ST/SE) with early exit
│   ├── field_level_validator_834.py    ✅ Unified validator (field-level + syntax rules P/C/R/E)
│   └── json_schema_validator_834.py    ✅ JSON schema validation (after parsing)
│
├── BUSINESS RULES SERVICES (2 files)
│   ├── business_rule_plugin_base_834.py ✅ NEW: Plugin system for client-specific business rules
│   └── business_rules_validator_834.py ⚠️ DEPRECATED: Use plugin system instead
│
├── PARSING SUPPORT SERVICES (2 files)
│   ├── yaml_loop_detector_834.py       ✅ Config-driven loop detection
│   └── plugin_base_834.py              ✅ Plugin system for custom parsing logic
│
├── DATA TRANSFORMATION SERVICES (2 files)
│   ├── edi_json_builder_834.py         ✅ Builds JSON structure from parsed data
│   └── treo_edi_file_header_mapper_834.py  ✅ Maps JSON to relational tables
│
│   [DEPRECATED - Can be deleted:]
│   └── jsonb_query_helper_834.py       ❌ Eliminated - queries moved to api_treo.py
│
└── UTILITY SERVICES (1 file)
    └── duplicate_detector_834.py       ✅ Duplicate file detection

[DEPRECATED - Can be deleted:]
├── yaml_base_parser_834.py             ❌ Consolidated into treo_base_parser_834.py
├── hybrid_parser_834.py                ❌ Consolidated into treo_base_parser_834.py
├── treo_json_parser_834.py             ❌ Consolidated into treo_base_parser_834.py
├── syntax_validator_834.py             ❌ Merged into field_level_validator_834.py
├── yaml_config_adapter_834.py          ❌ Merged into config_loader_834.py
└── business_rules_validator_834.py     ⚠️ Replaced by business_rule_plugin_base_834.py

Total: 18 active files (reduced from 23 files)
```

### Service Relationships and Flow

#### 1. CORE PARSER SERVICES (Parsing Engine)

**treo_base_parser_834.py** - Consolidated Base Parser (NEW)
- **Purpose**: Consolidated parser that combines base parsing, plugin support, and JSON building
- **Responsibilities**:
  - Initializes all validators and config loaders
  - Parses control segments (ISA, GS, ST, SE, GE, IEA)
  - Parses transaction segments (BGN, INS, NM1, HD, etc.)
  - Orchestrates validation during parsing
  - Tracks parsing state (current loops, segments, elements)
  - Integrates plugin system for custom parsing logic (10% of cases)
  - Builds JSON structure during parsing (not after)
  - Handles complex client-specific parsing scenarios
- **Consolidates**: 
  - `yaml_base_parser_834.py` (base parsing logic)
  - `hybrid_parser_834.py` (plugin support)
  - `treo_json_parser_834.py` (JSON building)
- **Uses**: All configuration, validation, and plugin services
- **Returns**: Parsed data structures + validation results + JSON structure
- **Rationale**: The inheritance chain (YamlBaseParser834 → HybridEDIParser834 → TreoJSONParser834) was only used by Treo, so consolidation eliminates unnecessary abstraction layers while maintaining all functionality.

**treo_parser_834.py** - Complete Treo Workflow Orchestrator
- **Purpose**: End-to-end workflow for Treo enrollment file processing
- **Responsibilities**:
  - Orchestrates complete workflow: duplicate check → parse → validate → build JSON → store
  - Calculates file hash for duplicate detection
  - Calls all services in correct order
  - Handles database transactions
  - Returns final processing results
- **Uses**: 
  - `duplicate_detector_834` - Check for duplicates
  - `treo_base_parser_834` - Parse EDI file (returns JSON + validation results)
  - `json_schema_validator_834` - Validate JSON schema
- **Workflow**:
  ```
  1. Calculate file hash → duplicate_detector
  2. Check duplicates → duplicate_detector
  3. Parse file → treo_base_parser (returns JSON + validation)
  4. Validate JSON → json_schema_validator
  5. Store in database → EnrollmentFile model
  ```
- **Note**: JSON is built during parsing (not after) by `treo_base_parser_834`

#### 2. CONFIGURATION SERVICES (Config Management)

**config_loader_834.py** - Configuration Loader (Enhanced)
- **Purpose**: Loads and caches client configurations
- **Responsibilities**:
  - Loads base config + client configs (includes yaml_config_adapter functionality)
  - Transforms YAML config structure to parser-compatible format
  - Caches configs for performance
  - Provides methods: `get_loop_order()`, `get_loop_segments()`, `get_config_dir()`, etc.
  - Merges base + client configs (client overrides base)
- **Updated**: 2026-01-16 - Merged `yaml_config_adapter_834.py` functionality into this file
- **Used by**: `treo_base_parser_834`, `yaml_loop_detector_834`
- **Note**: `yaml_config_adapter_834.py` is deprecated - functionality merged here

**yaml_metadata_adapter_834.py** - Metadata Provider
- **Purpose**: Provides element and segment metadata from YAML configs
- **Responsibilities**:
  - Loads all element definitions from loop configs
  - Provides metadata: `get_element()`, `get_loop_element_info()`, `get_segment_syntax()`
  - Caches metadata for fast lookups
  - Maps YAML usage codes (M/O/S/X) to database codes (R/S/N)
- **Used by**: 
  - `syntax_validator_834` - For element metadata
  - `field_level_validator_834` - For element definitions

**yaml_validation_loader_834.py** - Validation Rules Loader
- **Purpose**: Loads validation rules from YAML files
- **Responsibilities**:
  - Loads `validation/file_level.yaml`
  - Loads `validation/field_level.yaml`
  - Loads `validation/syntax_rules.yaml`
  - Loads `clients/*_business_rules.yaml`
  - Provides methods: `get_file_level_rules()`, `get_field_level_rules()`, `get_business_rules()`
- **Used by**: 
  - `file_level_validator_834`
  - `field_level_validator_834`
  - `business_rules_validator_834`
  - `syntax_validator_834`

#### 3. VALIDATION SERVICES (Efficient 3-Stage Pipeline)

**validation_pipeline_834.py** - Validation Pipeline Orchestrator (NEW)
- **Purpose**: Orchestrates 3-stage validation pipeline with early exit
- **Responsibilities**:
  - Stage 1: File-level validation (early exit on critical errors)
  - Stage 2 & 3: Combined element validation (field + syntax + business rules)
  - Coordinates all validators
  - Manages validation caching
  - Integrates business rule plugins
- **Features**:
  - Early exit on critical file-level errors (saves 30-50% time for invalid files)
  - Validation result caching
  - Single validation call per element
  - Business rules via plugin system
- **Uses**: `file_level_validator_834`, `field_level_validator_834`, `business_rule_plugin_base_834`
- **Used by**: `treo_base_parser_834`

**validation_cache_834.py** - Validation Cache (NEW)
- **Purpose**: Caches validation results for performance
- **Responsibilities**:
  - Element metadata caching
  - Validation rules caching
  - Validation result caching (LRU eviction)
  - Business rule plugin caching per client
- **Benefits**: Reduces redundant validation checks (10-20% performance improvement)

**file_level_validator_834.py** - File-Level Validator (Enhanced)
- **Purpose**: Validates file-level structure and integrity
- **Responsibilities**:
  - Validates control segments (ISA/GS/GE/IEA match)
  - Validates required segments (usage: ['R'])
  - Validates segment counts (SE01 matches actual count)
  - Validates envelope integrity
  - **Early exit**: Returns `should_exit` flag for critical errors
- **Uses**: `yaml_validation_loader_834`
- **Updated**: 2026-01-16 - Added early exit support with severity levels
- **Called by**: `validation_pipeline_834` (Stage 1)

**field_level_validator_834.py** - Unified Field-Level Validator (Enhanced)
- **Purpose**: Unified element/field validation (field-level + syntax rules)
- **Responsibilities**:
  - Validates data types (AN, ID, DT, N, R, etc.) → **WARNING if mismatch**
  - Validates required segments (usage: ['R']) → **ERROR if missing**
  - Validates format patterns and qualifier values
  - **Validates syntax rules (P/C/R/E)** → **WARNING if violated** (merged from syntax_validator)
  - Validates element length from metadata
- **Updated**: 2026-01-16 - Merged `syntax_validator_834.py` functionality into this file
- **Uses**: 
  - `yaml_validation_loader_834` - For field-level and syntax rules
  - `yaml_metadata_adapter_834` - For element definitions and syntax codes
- **Called by**: `validation_pipeline_834` (Stage 2 & 3)
- **Note**: `syntax_validator_834.py` is deprecated - functionality merged here

**business_rule_plugin_base_834.py** - Business Rule Plugin System (NEW)
- **Purpose**: Plugin system for client-specific business rules
- **Responsibilities**:
  - Base class for business rule plugins
  - Plugin registry for managing client-specific rules
  - Dynamic plugin loading per client
  - Easy to extend without code changes
- **Replaces**: `business_rules_validator_834.py` (YAML-based approach)
- **Benefits**: More flexible, testable, and extensible than YAML-only approach

**business_rules_validator_834.py** - Business Rules Validator (DEPRECATED)
- **Status**: ⚠️ DEPRECATED - Use `business_rule_plugin_base_834.py` plugin system instead
- **Purpose**: YAML-based client-specific business rules validation
- **Note**: Replaced by more flexible plugin system for better extensibility

**json_schema_validator_834.py** - JSON Schema Validator
- **Purpose**: Validates final JSON structure against JSON schema
- **Responsibilities**:
  - Loads JSON schema from `configs/edi834_json_schema.json`
  - Validates complete JSON structure after parsing
  - Reports schema validation errors
- **Used by**: `treo_parser_834` (after JSON is built)
- **Called after**: `edi_json_builder_834` completes

#### 4. PARSING SUPPORT SERVICES (Loop Detection & Plugins)

**yaml_loop_detector_834.py** - Loop Detector
- **Purpose**: Detects loop transitions during parsing
- **Responsibilities**:
  - Determines when a new loop starts (e.g., INS → Loop 2000, HD → Loop 2300)
  - Uses config-driven loop detection (from YAML)
  - Handles special loop detection rules (qualifier-based)
  - Tracks loop hierarchy and context
- **Uses**: `config_loader_834`
- **Used by**: `treo_base_parser_834` (during segment parsing)

**plugin_base_834.py** - Parser Plugin System
- **Purpose**: Extensible plugin system for custom parsing logic
- **Responsibilities**:
  - Base class `ParserPlugin` for custom parsing plugins
  - `PluginRegistry` manages plugin loading and registration
  - Handles complex client-specific parsing (10% of cases)
  - Allows custom segment parsing logic
- **Used by**: `treo_base_parser_834` (for custom parsing scenarios)
- **Note**: Separate from `business_rule_plugin_base_834.py` (for business rules)

#### 5. DATA TRANSFORMATION SERVICES (JSON & Storage)

**edi_json_builder_834.py** - JSON Builder
- **Purpose**: Builds structured JSON from parsed segment data
- **Responsibilities**:
  - Converts parsed segments to JSON structure
  - Organizes data into: `interchange`, `functional_group`, `transaction_set`
  - Builds loop structures (2000, 2100A, 2300, etc.)
  - Tracks metadata (segment counts, member counts, etc.)
- **Uses**: Parsed data from parser
- **Used by**: `treo_parser_834` (after parsing completes)

**treo_edi_file_header_mapper_834.py** - Header Mapper
- **Purpose**: Maps JSON data to relational database tables
- **Responsibilities**:
  - Extracts header data from JSON (`interchange`, `functional_group`, `transaction_set`)
  - Populates `edi_file_headers` table
  - Populates `edi_file_header_n1_loops` table
  - Handles N1 loop data (1000A, 1000B, 1000C)
- **Uses**: `EnrollmentFile.edi_data` (JSONB column)
- **Used by**: Treo workflow (after JSON is stored)

**jsonb_query_helper_834.py** - JSONB Query Helper (DEPRECATED)
- **Status**: ❌ ELIMINATED - Queries moved to API layer
- **Rationale**: If all data mappings are done from JSON, no separate helper needed
- **Migration**: 
  - Database query methods moved to `api_treo.py` endpoints
  - Static methods removed (access JSON directly)
- **Note**: Queries are now inline in API endpoints where they're used

#### 6. UTILITY SERVICES (File Management)

**duplicate_detector_834.py** - Duplicate Detector
- **Purpose**: Detects duplicate files using SHA-256 hash
- **Responsibilities**:
  - Calculates file hash (SHA-256)
  - Checks if file already exists in database
  - Supports duplicate handling modes: 'reject', 'warn', 'allow'
  - Prevents processing duplicate files
- **Used by**: `treo_parser_834` (before parsing starts)

---

## 11. Complete Service Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                     INITIALIZATION PHASE                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  treo_parser_834 (TreoParser834)                                     │
│    ↓                                                                 │
│  ├─→ config_loader_834 (ConfigLoader834)                            │
│  │     ├─→ Loads base_edi834_config.yaml (internal)                │
│  │     ├─→ Loads loops/*.yaml (internal)                           │
│  │     └─→ Loads clients/*_834_config.yaml (internal)              │
│  │                                                                   │
│  ├─→ yaml_metadata_adapter_834 (YamlMetadataAdapter834)            │
│  │     └─→ Loads all element/segment metadata                      │
│  │                                                                   │
│  ├─→ yaml_validation_loader_834 (YamlValidationLoader834)          │
│  │     ├─→ Loads validation/file_level.yaml                        │
│  │     ├─→ Loads validation/field_level.yaml                       │
│  │     ├─→ Loads validation/syntax_rules.yaml                      │
│  │     └─→ Loads clients/*_business_rules.yaml                     │
│  │                                                                   │
│  ├─→ treo_base_parser_834 (TreoBaseParser834)                      │
│  │     ├─→ Initializes validation_pipeline_834                     │
│  │     ├─→ Initializes yaml_loop_detector_834                      │
│  │     └─→ Initializes edi_json_builder_834 (internal)             │
│  │                                                                   │
│  ├─→ duplicate_detector_834 (DuplicateDetector834)                 │
│  └─→ json_schema_validator_834 (JSONSchemaValidator834)            │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                     PARSING PHASE                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  For each line in EDI file:                                          │
│                                                                       │
│  1. Segment Detection                                                │
│     treo_base_parser_834                                             │
│       └─→ yaml_loop_detector_834 (YamlLoopDetector834)              │
│             └─→ config_loader_834                                    │
│                   └─→ Determines loop context                       │
│                                                                       │
│  2. Element Parsing                                                  │
│     treo_base_parser_834                                             │
│       └─→ Splits segment by delimiters (*, :, ~)                   │
│                                                                       │
│  3. Validation Pipeline (3-Stage)                                    │
│     validation_pipeline_834 (ValidationPipeline834)                  │
│       │                                                                   │
│       ├─→ STAGE 1: File-Level Validation (Early Exit)              │
│       │     file_level_validator_834                                 │
│       │       ├─→ Validates control segments                        │
│       │       └─→ Returns should_exit if critical errors            │
│       │                                                                   │
│       ├─→ STAGE 2: Field-Level Validation                           │
│       │     field_level_validator_834                                │
│       │       ├─→ Checks required (usage: ['M']) → ERROR             │
│       │       ├─→ Checks length (min/max) → ERROR                   │
│       │       ├─→ Checks data type format → WARNING                 │
│       │       └─→ Uses: yaml_metadata_adapter_834                   │
│       │                                                                   │
│       └─→ STAGE 3: Syntax + Business Rules                          │
│             ├─→ field_level_validator_834                            │
│             │     └─→ Validates P/C/R/E rules → WARNING            │
│             └─→ business_rule_plugin_base_834 (plugins)             │
│                   └─→ Client-specific rules → ERROR/WARNING         │
│                                                                       │
│  4. Data Storage (In-Memory + JSON Building)                         │
│     treo_base_parser_834                                             │
│       ├─→ Stores parsed data in memory structures                   │
│       └─→ Updates JSON builder during parsing                       │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│              STAGE 1: FILE-LEVEL VALIDATION (Early Exit)             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  validation_pipeline_834.validate_file_structure()                   │
│    └─→ file_level_validator_834 (FileLevelValidator834)             │
│          ├─→ Validates ISA/GS/GE/IEA control numbers                │
│          ├─→ Validates ST/SE control numbers                        │
│          ├─→ Validates segment counts                               │
│          ├─→ Validates required segments (usage: ['R'])             │
│          └─→ Returns should_exit=True if critical errors            │
│                                                                       │
│  ⚠️ EARLY EXIT: If should_exit=True, stop parsing immediately       │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
                              ↓ (Continue if no critical errors)
┌─────────────────────────────────────────────────────────────────────┐
│          STAGES 2 & 3: ELEMENT VALIDATION (During Parsing)           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  validation_pipeline_834.validate_element()                          │
│    ├─→ field_level_validator_834 (FieldLevelValidator834)           │
│    │     ├─→ Field-level validation (data types, formats)           │
│    │     └─→ Syntax validation (P/C/R/E rules)                     │
│    └─→ business_rule_plugin_base_834 (plugins)                      │
│          └─→ Client-specific business rules                         │
│                                                                       │
│  JSON building happens simultaneously during parsing                 │
│    └─→ edi_json_builder_834 (built incrementally)                   │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                  JSON SCHEMA VALIDATION PHASE                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  json_schema_validator_834 (JSONSchemaValidator834)                 │
│    ├─→ Loads schema from configs/edi834_json_schema.json            │
│    ├─→ Validates complete JSON structure                            │
│    └─→ Reports schema validation errors                             │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    STORAGE PHASE                                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  treo_parser_834                                                     │
│    ├─→ Stores JSON in enrollment_files.edi_data (JSONB)            │
│    ├─→ Logs processing results                                       │
│    └─→ Returns processing results                                    │
│                                                                       │
│  (Optional) treo_edi_file_header_mapper_834                         │
│    ├─→ Maps JSON to edi_file_headers table                          │
│    └─→ Maps JSON to edi_file_header_n1_loops table                  │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 12. Service Dependency Graph

```
┌─────────────────────────────────────────────────────────────┐
│                    TOP-LEVEL ORCHESTRATOR                     │
│                  treo_parser_834.py                           │
└─────────────────────────────────────────────────────────────┘
                              ↓
        ┌─────────────────────┼─────────────────────┐
        ↓                     ↓                     ↓
┌──────────────┐    ┌──────────────────┐   ┌──────────────┐
│ Duplicate    │    │   Parser Chain   │   │   JSON       │
│ Detector     │    │                  │   │   Builder    │
└──────────────┘    └──────────────────┘   └──────────────┘
                            ↓                     ↓
              ┌─────────────┼─────────────┐      ↓
              ↓             ↓             ↓      ↓
      ┌──────────┐  ┌──────────────┐  ┌─────────────┐
      │ Hybrid   │  │ Loop         │  │ JSON Schema │
      │ Parser   │  │ Detector     │  │ Validator   │
      └──────────┘  └──────────────┘  └─────────────┘
              ↓             ↓
      ┌──────────┐  ┌──────────────┐
      │  Base    │  │   Config     │
      │  Parser  │  │   Loader     │
      └──────────┘  └──────────────┘
              ↓             ↓
      ┌─────────────────────────────────┐
      │   VALIDATION LAYER               │
      ├─────────────────────────────────┤
      │ • Syntax Validator               │
      │ • Field-Level Validator          │
      │ • Business Rules Validator       │
      │ • File-Level Validator           │
      └─────────────────────────────────┘
              ↓             ↓
      ┌─────────────────────────────────┐
      │   CONFIGURATION LAYER            │
      ├─────────────────────────────────┤
      │ • Config Adapter                 │
      │ • Metadata Adapter               │
      │ • Validation Loader              │
      └─────────────────────────────────┘
```

---

## 13. Data Flow Through Services

### Example: Parsing INS Segment in Loop 2000

```
1. EDI Line: "INS*Y*18*021*XN*A..."
   ↓
2. treo_parser_834.parse_and_store()
   ↓
3. treo_base_parser_834.parse_x12_file()
   ↓
4. treo_base_parser_834._parse_transaction_segments()
   ↓
5. treo_base_parser_834._parse_segment_config_driven()
   ↓
6. yaml_loop_detector_834.detect_loop_transition()
   → Uses: config_loader_834.get_loop_order()
   → Detects: Loop 2000
   ↓
7. treo_base_parser_834 parses elements:
   INS01="Y", INS02="18", INS03="021", ...
   ↓
8. For each element, validators called:
   
   a) syntax_validator_834.validate_element(INS01, "Y", "INS", "2000")
      → Uses: yaml_metadata_adapter_834.get_element("INS01")
      → Checks: Required? Length?
   
   b) field_level_validator_834.validate_element(INS01, "Y", "INS", "2000")
      → Uses: yaml_metadata_adapter_834.get_loop_element_info("INS01", "2000")
      → Uses: yaml_validation_loader_834.get_field_level_rules()
      → Checks: Data type? Qualifier valid?
   
   c) business_rules_validator_834.validate_element(INS03, "021", "INS", "2000")
      → Uses: yaml_validation_loader_834.get_business_rules("INS", "INS03", "2000")
      → Checks: Value "021" in ["021","024","030"]? ✅
   ↓
9. After all elements parsed:
   syntax_validator_834.validate_segment_syntax_rules("INS", "2000")
   → Validates: P1112 rule (if INS11 or INS12 present, both required)
   → If violated → WARNING
   ↓
10. treo_base_parser_834 stores parsed data in memory AND updates JSON builder
    → JSON is built incrementally during parsing (not after)
    ↓
11. After file parsing completes:
    treo_base_parser_834.get_json()
    → Returns already-built JSON structure
    ↓
12. json_schema_validator_834.validate(json_data)
    → Validates JSON structure against schema
    ↓
13. treo_parser_834 stores JSON in database
    → enrollment_files.edi_data (JSONB column)
```

---

## 14. Key Service Responsibilities Summary

| Service | Primary Responsibility | Key Methods |
|---------|----------------------|-------------|
| **treo_parser_834** | Complete workflow orchestration | `parse_and_store()` |
| **treo_base_parser_834** | Consolidated base parser (parsing + plugins + JSON) | `parse_x12_file()`, `_parse_isa_segment()`, plugin integration, JSON building |
| **treo_parser_834** | Complete workflow orchestrator | `parse_and_store()` |
| **validation_pipeline_834** | 3-stage validation orchestrator | `validate_file_structure()`, `validate_element()`, `validate_segment_syntax()` |
| **validation_cache_834** | Validation result caching | `get_validation_result()`, `set_validation_result()` |
| **config_loader_834** | Config loading & caching (includes adapter functionality) | `load_config()`, `get_loop_order()`, `get_config_dir()` |
| **yaml_metadata_adapter_834** | Element/segment metadata | `get_element()`, `get_loop_element_info()`, `get_segment_syntax()` |
| **yaml_validation_loader_834** | Validation rules loading | `get_field_level_rules()`, `get_syntax_rules()`, `get_business_rules()` |
| **yaml_loop_detector_834** | Loop detection | `detect_loop_transition()` |
| **field_level_validator_834** | Unified field + syntax validation | `validate_element()`, `validate_segment_syntax_rules()` |
| **file_level_validator_834** | File-level validation with early exit | `validate_file_data()` |
| **business_rule_plugin_base_834** | Business rule plugin system | `BusinessRulePluginBase`, `BusinessRulePluginRegistry` |
| **edi_json_builder_834** | JSON structure building (during parsing) | `start_ins_loop()`, `add_ins_segment()`, `get_json()` |
| **json_schema_validator_834** | JSON schema validation | `validate()` |
| **duplicate_detector_834** | Duplicate detection | `check_duplicate()` |
| **plugin_base_834** | Parser plugin system | `ParserPlugin`, `PluginRegistry` |
| **treo_edi_file_header_mapper_834** | JSON → Relational mapping | `map_enrollment_file()` |
| **api_treo.py** | API endpoints with inline JSONB queries | `query_by_bgn_reference()`, `query_by_member()` |

---

## 15. Service Interaction Patterns

### Pattern 1: Initialization Chain
```
treo_parser_834.__init__()
  → Creates all validators
  → Creates config_loader_834
    → Creates yaml_config_adapter_834
      → Loads base + client configs
  → Creates yaml_metadata_adapter_834
    → Loads all element metadata
  → Creates yaml_validation_loader_834
    → Loads all validation rules
```

### Pattern 2: Parsing Chain
```
        treo_parser_834.parse_and_store()
          → treo_base_parser_834.parse_x12_file()
            → treo_base_parser_834._parse_transaction_segments()
              → treo_base_parser_834._parse_segment_config_driven()
                → yaml_loop_detector_834.detect_loop_transition()
                → Validators called for each element
                → Syntax rules validated after segment
                → JSON builder updated during parsing
```

### Pattern 3: Validation Pipeline (3-Stage)
```
treo_base_parser_834._parse_segment_config_driven()
  → For each element:
    → validation_pipeline_834.validate_element()
      ├─→ field_level_validator_834.validate_element() (Stage 2)
      │     ├─→ Field-level validation (data types, formats)
      │     └─→ Element length validation (from metadata)
      └─→ business_rule_plugin_base_834 (Stage 3)
            └─→ Client-specific business rules
  → After all elements in segment:
    → validation_pipeline_834.validate_segment_syntax()
      └─→ field_level_validator_834.validate_segment_syntax_rules() (P/C/R/E)
  → During parsing:
    → JSON builder updated with parsed data
```

### Pattern 4: JSON Building Chain
```
treo_parser_834.parse_and_store()
  → edi_json_builder_834.build_from_parser_data()
    → Builds JSON structure from parsed data
  → json_schema_validator_834.validate()
    → Validates JSON structure
```

This architecture provides:
- **Separation of Concerns**: Each service has a single, well-defined responsibility
- **Modularity**: Services can be used independently or together
- **Extensibility**: Easy to add new validators, parsers, or plugins
- **Testability**: Each service can be tested independently
- **Maintainability**: Changes to one service don't affect others

---

## 16. Deprecated Files - Can Be Deleted

The following files are deprecated and can be safely deleted after verification:

### ❌ Deprecated Parser Files (Consolidated into `treo_base_parser_834.py`)
1. **`yaml_base_parser_834.py`** - Base parser logic
   - **Status**: Consolidated into `treo_base_parser_834.py`
   - **Reason**: Inheritance chain eliminated for Treo-only use case
   - **Verification**: Check if imported anywhere (should only be in deprecated files)

2. **`hybrid_parser_834.py`** - Plugin support parser
   - **Status**: Consolidated into `treo_base_parser_834.py`
   - **Reason**: Plugin support now directly in consolidated parser
   - **Verification**: Only imported by `treo_json_parser_834.py` (also deprecated)

3. **`treo_json_parser_834.py`** - JSON building parser
   - **Status**: Consolidated into `treo_base_parser_834.py`
   - **Reason**: JSON building now happens during parsing in consolidated parser
   - **Verification**: Only imports `hybrid_parser_834.py` (also deprecated)

### ❌ Deprecated Validator Files
4. **`syntax_validator_834.py`** - Syntax rule validator
   - **Status**: Merged into `field_level_validator_834.py`
   - **Reason**: Syntax validation now part of unified field validator
   - **Verification**: Only imported by deprecated `yaml_base_parser_834.py`

### ❌ Deprecated Config Files
5. **`yaml_config_adapter_834.py`** - YAML config transformer
   - **Status**: Merged into `config_loader_834.py`
   - **Reason**: Adapter was only used internally by config loader
   - **Verification**: Only imported by `config_loader_834.py` (should be removed)

### ⚠️ Deprecated Business Rules Validator
6. **`business_rules_validator_834.py`** - YAML-based business rules validator
   - **Status**: Replaced by `business_rule_plugin_base_834.py` plugin system
   - **Reason**: Plugin system is more flexible and extensible
   - **Verification**: Only imported by deprecated `yaml_base_parser_834.py`
   - **Note**: If you have existing YAML business rules, they can be converted to plugins

### ❌ Eliminated Query Helper
7. **`jsonb_query_helper_834.py`** - JSONB query helper
   - **Status**: ELIMINATED - Queries moved to API layer
   - **Reason**: If all data mappings are done from JSON, no separate helper needed
   - **Migration**: Query methods moved directly to `api_treo.py` endpoints
   - **Static methods**: Removed (access JSON directly)

### Summary
- **Before consolidation**: 23 service files
- **After consolidation**: 17 active service files (reduced from 18)
- **Can be deleted**: 7 deprecated/eliminated files
- **Reduction**: ~26% fewer files, simpler architecture

### Deletion Checklist
Before deleting, verify:
1. ✅ No active imports of these files (except in deprecated files)
2. ✅ All functionality is preserved in consolidated files
3. ✅ Tests pass with consolidated files
4. ✅ Any references in documentation updated
