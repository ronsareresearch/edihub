"""
[YAML/JSON] - Models Package
[UPDATED] - 2026-01-20: Added metadata models for enroll database
Purpose: Models package initialization - YAML/JSON architecture
"""
# Treo Models (enroll database - JSON-based)
from app.models.treo_models import (
    Client, LOB, EnrollmentFile, ProcessLog, EDIHeader, EDIControlSeg, EDITransSeg, EDIData, EDIAddtData
)

# Member-Level Storage Models removed - no longer storing member data in database

# Metadata Models (enroll database - metadata schema)
from app.models.treo_metadata import (
    Loop, Segment, Element, ElementDataType, IndustryUsage,
    SyntaxRule, Syntax, LoopSegment, LoopElement, CodeValue,
    LoopElementAdditionalSyntax, ControlSegment, ControlSegmentElement,
    ControlSegmentCodeValue, ControlSegmentElementData,
    ElementDataTypeExpression, ElementComment
)

__all__ = [
    # Treo Models (enroll database - public schema)
    'Client', 'LOB', 'EnrollmentFile', 'ProcessLog', 'EDIHeader', 'EDIControlSeg', 'EDITransSeg', 'EDIData', 'EDIAddtData',
    # Metadata Models (enroll database - metadata schema)
    'Loop', 'Segment', 'Element', 'ElementDataType', 'IndustryUsage',
    'SyntaxRule', 'Syntax', 'LoopSegment', 'LoopElement', 'CodeValue',
    'LoopElementAdditionalSyntax', 'ControlSegment', 'ControlSegmentElement',
    'ControlSegmentCodeValue', 'ControlSegmentElementData',
    'ElementDataTypeExpression', 'ElementComment',
]
