"""
[TREO] - Treo Enrollment Architecture Models
Date: 2026-01-16
Purpose: SQLAlchemy models for TREO Application enroll Database
"""
from sqlalchemy import Column, Integer, String, Boolean, BigInteger, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database_treo import BaseTreo as Base


class Client(Base):
    """
    Client/Tenant model for Treo enrollment architecture.
    """
    __tablename__ = 'clients'
    __table_args__ = {'schema': 'public'}
    
    client_id = Column(Integer, primary_key=True, autoincrement=True)
    client_code = Column(String(50), unique=True, nullable=False, index=True)
    client_name = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default='true')
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    lobs = relationship("LOB", back_populates="client", cascade="all, delete-orphan")
    enrollment_files = relationship("EnrollmentFile", back_populates="client", cascade="all, delete-orphan")
    process_logs = relationship("ProcessLog", back_populates="client")
    
    def __repr__(self):
        return f"<Client(client_id={self.client_id}, client_code='{self.client_code}', client_name='{self.client_name}')>"


class LOB(Base):
    """
    Line of Business model for Treo enrollment architecture.
    """
    __tablename__ = 'lobs'
    __table_args__ = {'schema': 'public'}
    
    lob_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('public.clients.client_id', ondelete='CASCADE'), nullable=False, index=True)
    lob_code = Column(String(50), nullable=False)
    lob_name = Column(String(255), nullable=False)
    program_type = Column(String(50), nullable=True)  # MEDICAID, MEDICARE, CHIP, etc.
    is_active = Column(Boolean, nullable=False, server_default='true')
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    client = relationship("Client", back_populates="lobs")
    enrollment_files = relationship("EnrollmentFile", back_populates="lob", cascade="all, delete-orphan")
    process_logs = relationship("ProcessLog", back_populates="lob")
    
    def __repr__(self):
        return f"<LOB(lob_id={self.lob_id}, client_id={self.client_id}, lob_code='{self.lob_code}', lob_name='{self.lob_name}')>"


class EnrollmentFile(Base):
    """
    Enrollment File model for Treo enrollment architecture.
    Stores parsed EDI 834 files as JSON documents.
    """
    __tablename__ = 'enrollment_files'
    __table_args__ = {'schema': 'public'}
    
    enrollment_file_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('public.clients.client_id', ondelete='CASCADE'), nullable=False, index=True)
    lob_id = Column(Integer, ForeignKey('public.lobs.lob_id', ondelete='CASCADE'), nullable=False, index=True)
    file_name = Column(String(500), nullable=False)
    file_size_bytes = Column(BigInteger, nullable=True)
    file_hash = Column(String(64), nullable=True, index=True)  # SHA-256 hash for duplicate detection
    original_file_path = Column(String(1000), nullable=True)  # Relative path: data/json_files/{file_name}
    processing_status = Column(String(50), nullable=True, server_default='pending', index=True)  # 'pending', 'processing', 'completed', 'failed'
    error_message = Column(Text, nullable=True)  # Error message if processing failed
    processed_at = Column(DateTime(timezone=True), nullable=True)  # When file was successfully processed
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    created_by = Column(String(255), nullable=True)  # User who uploaded the file
    
    # Relationships
    client = relationship("Client", back_populates="enrollment_files")
    lob = relationship("LOB", back_populates="enrollment_files")
    process_logs = relationship("ProcessLog", back_populates="enrollment_file", cascade="all, delete-orphan")
    edi_header = relationship("EDIHeader", back_populates="enrollment_file", uselist=False, cascade="all, delete-orphan")  # Legacy - will be removed
    edi_control_seg = relationship("EDIControlSeg", back_populates="enrollment_file", uselist=False, cascade="all, delete-orphan")
    edi_trans_seg_records = relationship("EDITransSeg", back_populates="enrollment_file", cascade="all, delete-orphan")
    edi_data_members = relationship("EDIData", back_populates="enrollment_file", cascade="all, delete-orphan")
    edi_addt_data_records = relationship("EDIAddtData", back_populates="enrollment_file", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<EnrollmentFile(enrollment_file_id={self.enrollment_file_id}, file_name='{self.file_name}', processing_status='{self.processing_status}')>"


class ProcessLog(Base):
    """
    Process Log model for Treo enrollment architecture.
    Stores detailed processing logs, errors, and warnings for each file processing attempt.
    """
    __tablename__ = 'process_log'
    __table_args__ = {'schema': 'public'}
    
    process_log_id = Column(Integer, primary_key=True, autoincrement=True)
    enrollment_file_id = Column(Integer, ForeignKey('public.enrollment_files.enrollment_file_id', ondelete='SET NULL'), nullable=True, index=True)
    client_id = Column(Integer, ForeignKey('public.clients.client_id', ondelete='CASCADE'), nullable=False, index=True)
    lob_id = Column(Integer, ForeignKey('public.lobs.lob_id', ondelete='CASCADE'), nullable=False, index=True)
    file_name = Column(String(500), nullable=False)  # Stored even if file record doesn't exist (rollback scenario)
    file_hash = Column(String(64), nullable=True, index=True)  # For tracking even if rollback occurred
    log_type = Column(String(50), nullable=False, index=True)  # 'error', 'warning', 'info', 'debug'
    log_level = Column(String(20), nullable=False, index=True)  # 'ERROR', 'WARN', 'INFO', 'DEBUG'
    message = Column(Text, nullable=False)  # Log message
    error_code = Column(String(50), nullable=True)  # Error code if applicable
    segment_code = Column(String(10), nullable=True)  # Segment code if error is segment-specific
    element_ref = Column(String(20), nullable=True)  # Element reference if error is element-specific
    line_number = Column(Integer, nullable=True)  # Line number in original EDI file
    loop_id = Column(String(50), nullable=True)  # Loop identifier if error is loop-specific
    log_metadata = Column('metadata', JSONB, nullable=True)  # Additional context/metadata as JSON (column name is 'metadata' in DB)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    
    # Relationships
    enrollment_file = relationship("EnrollmentFile", back_populates="process_logs")
    client = relationship("Client", back_populates="process_logs")
    lob = relationship("LOB", back_populates="process_logs")
    
    def __repr__(self):
        return f"<ProcessLog(process_log_id={self.process_log_id}, log_type='{self.log_type}', log_level='{self.log_level}')>"


class EDIControlSeg(Base):
    """
    EDI Control Segments model for Treo enrollment architecture.
    Stores file-level control segments (ISA, GS, GE, IEA).
    One row per enrollment file.
    """
    __tablename__ = 'edi_control_seg'
    __table_args__ = {'schema': 'public'}
    
    enrollment_file_id = Column(Integer, ForeignKey('public.enrollment_files.enrollment_file_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    
    # ISA Segment (Interchange Control Header) - 16 elements
    isa01 = Column(String(2), nullable=True)
    isa02 = Column(String(10), nullable=True)
    isa03 = Column(String(2), nullable=True)
    isa04 = Column(String(10), nullable=True)
    isa05 = Column(String(2), nullable=True)
    isa06 = Column(String(15), nullable=True)
    isa07 = Column(String(2), nullable=True)
    isa08 = Column(String(15), nullable=True)
    isa09 = Column(String(6), nullable=True)
    isa10 = Column(String(4), nullable=True)
    isa11 = Column(String(1), nullable=True)
    isa12 = Column(String(5), nullable=True)
    isa13 = Column(String(9), nullable=True)
    isa14 = Column(String(1), nullable=True)
    isa15 = Column(String(1), nullable=True)
    isa16 = Column(String(1), nullable=True)
    
    # GS Segment (Functional Group Header) - 8 elements
    gs01 = Column(String(2), nullable=True)
    gs02 = Column(String(15), nullable=True)
    gs03 = Column(String(15), nullable=True)
    gs04 = Column(String(8), nullable=True)
    gs05 = Column(String(4), nullable=True)
    gs06 = Column(String(2), nullable=True)
    gs07 = Column(String(1), nullable=True)
    gs08 = Column(String(12), nullable=True)
    
    # GE Segment (Functional Group Trailer) - 2 elements
    ge01 = Column(String(6), nullable=True)
    ge02 = Column(String(9), nullable=True)
    
    # IEA Segment (Interchange Control Trailer) - 2 elements
    iea01 = Column(String(5), nullable=True)
    iea02 = Column(String(9), nullable=True)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    # Relationships
    enrollment_file = relationship("EnrollmentFile", back_populates="edi_control_seg")
    
    def __repr__(self):
        return f"<EDIControlSeg(enrollment_file_id={self.enrollment_file_id})>"


class EDITransSeg(Base):
    """
    EDI Transaction Segments model for Treo enrollment architecture.
    Stores transaction-level segments (ST, BGN, REF, DTP, N1, SE).
    One row per transaction set (ST/SE pair) within an enrollment file.
    """
    __tablename__ = 'edi_trans_seg'
    __table_args__ = {'schema': 'public'}
    
    # Primary Key (composite)
    enrollment_file_id = Column(Integer, ForeignKey('public.enrollment_files.enrollment_file_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    trans_index = Column(Integer, primary_key=True, nullable=False)  # Sequential position of transaction set in file (1-based)
    
    # ST Segment (Transaction Set Header) - 3 elements
    st01 = Column(String(3), nullable=True)
    st02 = Column(String(9), nullable=True)
    st03 = Column(String(12), nullable=True)
    
    # BGN Segment (Beginning Segment) - 8 elements
    bgn01 = Column(String(2), nullable=True)
    bgn02 = Column(String(30), nullable=True)
    bgn03 = Column(String(8), nullable=True)
    bgn04 = Column(String(4), nullable=True)
    bgn05 = Column(String(30), nullable=True)
    bgn06 = Column(String(30), nullable=True)
    bgn07 = Column(String(30), nullable=True)
    bgn08 = Column(String(2), nullable=True)
    
    # REF Segment (Reference Information) - Up to 5 instances (2 elements per instance)
    ref01_1 = Column(String(3), nullable=True)
    ref02_1 = Column(String(30), nullable=True)
    ref01_2 = Column(String(3), nullable=True)
    ref02_2 = Column(String(30), nullable=True)
    ref01_3 = Column(String(3), nullable=True)
    ref02_3 = Column(String(30), nullable=True)
    ref01_4 = Column(String(3), nullable=True)
    ref02_4 = Column(String(30), nullable=True)
    ref01_5 = Column(String(3), nullable=True)
    ref02_5 = Column(String(30), nullable=True)
    
    # DTP Segment (Date/Time/Period) - Up to 5 instances (3 elements per instance)
    dtp01_1 = Column(String(3), nullable=True)
    dtp02_1 = Column(String(3), nullable=True)
    dtp03_1 = Column(String(35), nullable=True)
    dtp01_2 = Column(String(3), nullable=True)
    dtp02_2 = Column(String(3), nullable=True)
    dtp03_2 = Column(String(35), nullable=True)
    dtp01_3 = Column(String(3), nullable=True)
    dtp02_3 = Column(String(3), nullable=True)
    dtp03_3 = Column(String(35), nullable=True)
    dtp01_4 = Column(String(3), nullable=True)
    dtp02_4 = Column(String(3), nullable=True)
    dtp03_4 = Column(String(35), nullable=True)
    dtp01_5 = Column(String(3), nullable=True)
    dtp02_5 = Column(String(3), nullable=True)
    dtp03_5 = Column(String(35), nullable=True)
    
    # N1 Segment (Name/Entity Information) - Up to 3 instances (2 elements per instance, for Loops 1000A, 1000B, 1000C)
    n101_1 = Column(String(3), nullable=True)
    n102_1 = Column(String(60), nullable=True)
    n101_2 = Column(String(3), nullable=True)
    n102_2 = Column(String(60), nullable=True)
    n101_3 = Column(String(3), nullable=True)
    n102_3 = Column(String(60), nullable=True)
    
    # SE Segment (Transaction Set Trailer) - 2 elements
    se01 = Column(String(10), nullable=True)
    se02 = Column(String(9), nullable=True)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    # Relationships
    enrollment_file = relationship("EnrollmentFile", back_populates="edi_trans_seg_records")
    
    def __repr__(self):
        return f"<EDITransSeg(enrollment_file_id={self.enrollment_file_id}, trans_index={self.trans_index})>"


# Legacy EDIHeader model - will be removed after migration
class EDIHeader(Base):
    """
    EDI Header model for Treo enrollment architecture.
    DEPRECATED: This model will be removed after migration to edi_control_seg and edi_trans_seg.
    Stores flattened EDI header segments (ISA, GS, ST, BGN, REF, DTP, QTY, SE, GE, IEA) in sequence order.
    Each repeating segment instance gets its own numbered columns (e.g., dtp01_1, dtp02_1, dtp03_1, dtp01_2, ...).
    """
    __tablename__ = 'edi_header'
    __table_args__ = {'schema': 'public'}
    
    enrollment_file_id = Column(Integer, ForeignKey('public.enrollment_files.enrollment_file_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    
    # ISA Segment (Interchange Control Header) - 16 elements
    isa01 = Column(String(2), nullable=True)
    isa02 = Column(String(10), nullable=True)
    isa03 = Column(String(2), nullable=True)
    isa04 = Column(String(10), nullable=True)
    isa05 = Column(String(2), nullable=True)
    isa06 = Column(String(15), nullable=True)
    isa07 = Column(String(2), nullable=True)
    isa08 = Column(String(15), nullable=True)
    isa09 = Column(String(6), nullable=True)
    isa10 = Column(String(4), nullable=True)
    isa11 = Column(String(1), nullable=True)
    isa12 = Column(String(5), nullable=True)
    isa13 = Column(String(9), nullable=True)
    isa14 = Column(String(1), nullable=True)
    isa15 = Column(String(1), nullable=True)
    isa16 = Column(String(1), nullable=True)
    
    # GS Segment (Functional Group Header) - 8 elements
    gs01 = Column(String(2), nullable=True)
    gs02 = Column(String(15), nullable=True)
    gs03 = Column(String(15), nullable=True)
    gs04 = Column(String(8), nullable=True)
    gs05 = Column(String(4), nullable=True)
    gs06 = Column(String(2), nullable=True)
    gs07 = Column(String(1), nullable=True)
    gs08 = Column(String(12), nullable=True)
    
    # ST Segment (Transaction Set Header) - 3 elements
    st01 = Column(String(3), nullable=True)
    st02 = Column(String(9), nullable=True)
    st03 = Column(String(12), nullable=True)
    
    # BGN Segment (Beginning Segment) - 8 elements
    bgn01 = Column(String(2), nullable=True)
    bgn02 = Column(String(30), nullable=True)
    bgn03 = Column(String(8), nullable=True)
    bgn04 = Column(String(4), nullable=True)
    bgn05 = Column(String(30), nullable=True)
    bgn06 = Column(String(30), nullable=True)
    bgn07 = Column(String(30), nullable=True)
    bgn08 = Column(String(2), nullable=True)
    
    # REF Segment (Reference Information) - 1 instance (2 elements per instance)
    ref01 = Column(String(3), nullable=True)
    ref02 = Column(String(30), nullable=True)
    
    # DTP Segment (Date/Time/Period) - 2 instances (3 elements per instance)
    dtp01_1 = Column(String(3), nullable=True)
    dtp02_1 = Column(String(3), nullable=True)
    dtp03_1 = Column(String(35), nullable=True)
    dtp01_2 = Column(String(3), nullable=True)
    dtp02_2 = Column(String(3), nullable=True)
    dtp03_2 = Column(String(35), nullable=True)
    
    # SE Segment (Transaction Set Trailer) - 2 elements
    se01 = Column(String(10), nullable=True)
    se02 = Column(String(9), nullable=True)
    
    # GE Segment (Functional Group Trailer) - 2 elements
    ge01 = Column(String(6), nullable=True)
    ge02 = Column(String(9), nullable=True)
    
    # IEA Segment (Interchange Control Trailer) - 2 elements
    iea01 = Column(String(5), nullable=True)
    iea02 = Column(String(9), nullable=True)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    # Relationships
    enrollment_file = relationship("EnrollmentFile", back_populates="edi_header")
    
    def __repr__(self):
        return f"<EDIHeader(enrollment_file_id={self.enrollment_file_id})>"


class EDIData(Base):
    """
    EDI Data model for Treo enrollment architecture.
    Stores flattened EDI member-level data (Loop 2000) in sequence order.
    Each row represents one member (from INS01 to next INS segment).
    
    Complete structure based on parsed JSON:
    - INS Segment: 1 instance, 8 elements
    - REF Segment: Up to 12 instances, 2 elements each (max 11 found in data, +1 safety margin)
    - DTP Segment: Up to 10 instances, 3 elements each (max 9 found in data, +1 safety margin)
    - NM1 Segment: 1 instance, 4 elements
    - N3 Segment: 1 instance, 2 elements
    - N4 Segment: 1 instance, 6 elements
    - DMG Segment: 1 instance, 5 elements
    - LUI Segment: 1 instance, 2 elements
    - HD Segment: Up to 2 instances, 4 elements each
    - AMT Segment: 1 instance, 2 elements
    - LS Segment: 1 instance, 1 element (Additional Reporting Categories)
    - LE Segment: 1 instance, 1 element (Additional Reporting Categories Loop Termination)
    """
    __tablename__ = 'edi_data'
    __table_args__ = {'schema': 'public'}
    
    # Primary Key (composite)
    enrollment_file_id = Column(Integer, ForeignKey('public.enrollment_files.enrollment_file_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    member_index = Column(Integer, primary_key=True, nullable=False)  # Sequential position in file (1-based)
    
    # INS Segment (Member Level Detail) - 1 instance, 8 elements
    ins01 = Column(String(1), nullable=True)
    ins02 = Column(String(2), nullable=True)
    ins03 = Column(String(3), nullable=True)
    ins04 = Column(String(2), nullable=True)
    ins05 = Column(String(1), nullable=True)
    ins06 = Column(String(1), nullable=True)
    ins07 = Column(String(1), nullable=True)
    ins08 = Column(String(2), nullable=True)
    
    # REF Segment (Reference Information) - Up to 12 instances (2 elements per instance)
    # Based on actual data: max 11 instances found, +1 for safety margin
    # Currently only 3 instances in JSON, but reserved for future expansion
    ref01_1 = Column(String(3), nullable=True)
    ref02_1 = Column(String(30), nullable=True)
    ref01_2 = Column(String(3), nullable=True)
    ref02_2 = Column(String(30), nullable=True)
    ref01_3 = Column(String(3), nullable=True)
    ref02_3 = Column(String(30), nullable=True)
    ref01_4 = Column(String(3), nullable=True)
    ref02_4 = Column(String(30), nullable=True)
    ref01_5 = Column(String(3), nullable=True)
    ref02_5 = Column(String(30), nullable=True)
    ref01_6 = Column(String(3), nullable=True)
    ref02_6 = Column(String(30), nullable=True)
    ref01_7 = Column(String(3), nullable=True)
    ref02_7 = Column(String(30), nullable=True)
    ref01_8 = Column(String(3), nullable=True)
    ref02_8 = Column(String(30), nullable=True)
    ref01_9 = Column(String(3), nullable=True)
    ref02_9 = Column(String(30), nullable=True)
    ref01_10 = Column(String(3), nullable=True)
    ref02_10 = Column(String(30), nullable=True)
    ref01_11 = Column(String(3), nullable=True)
    ref02_11 = Column(String(30), nullable=True)
    ref01_12 = Column(String(3), nullable=True)
    ref02_12 = Column(String(30), nullable=True)
    ref01_12 = Column(String(3), nullable=True)
    ref02_12 = Column(String(30), nullable=True)
    
    # DTP Segment (Date/Time/Period) - Up to 10 instances (3 elements per instance)
    # Based on actual data: max 9 instances found, +1 for safety margin
    # Currently only 1 instance in JSON, but reserved for future expansion
    dtp01_1 = Column(String(3), nullable=True)
    dtp02_1 = Column(String(3), nullable=True)
    dtp03_1 = Column(String(35), nullable=True)
    dtp01_2 = Column(String(3), nullable=True)
    dtp02_2 = Column(String(3), nullable=True)
    dtp03_2 = Column(String(35), nullable=True)
    dtp01_3 = Column(String(3), nullable=True)
    dtp02_3 = Column(String(3), nullable=True)
    dtp03_3 = Column(String(35), nullable=True)
    dtp01_4 = Column(String(3), nullable=True)
    dtp02_4 = Column(String(3), nullable=True)
    dtp03_4 = Column(String(35), nullable=True)
    dtp01_5 = Column(String(3), nullable=True)
    dtp02_5 = Column(String(3), nullable=True)
    dtp03_5 = Column(String(35), nullable=True)
    dtp01_6 = Column(String(3), nullable=True)
    dtp02_6 = Column(String(3), nullable=True)
    dtp03_6 = Column(String(35), nullable=True)
    dtp01_7 = Column(String(3), nullable=True)
    dtp02_7 = Column(String(3), nullable=True)
    dtp03_7 = Column(String(35), nullable=True)
    dtp01_8 = Column(String(3), nullable=True)
    dtp02_8 = Column(String(3), nullable=True)
    dtp03_8 = Column(String(35), nullable=True)
    dtp01_9 = Column(String(3), nullable=True)
    dtp02_9 = Column(String(3), nullable=True)
    dtp03_9 = Column(String(35), nullable=True)
    dtp01_10 = Column(String(3), nullable=True)
    dtp02_10 = Column(String(3), nullable=True)
    dtp03_10 = Column(String(35), nullable=True)
    
    # NM1 Segment (Name/Entity Information) - 1 instance, 4 elements
    nm101 = Column(String(3), nullable=True)
    nm102 = Column(String(1), nullable=True)
    nm103 = Column(String(60), nullable=True)
    nm104 = Column(String(35), nullable=True)
    
    # N3 Segment (Address Information) - 1 instance, 2 elements
    n301 = Column(String(55), nullable=True)
    n302 = Column(String(55), nullable=True)
    
    # N4 Segment (Geographic Location) - 1 instance, 6 elements
    n401 = Column(String(30), nullable=True)
    n402 = Column(String(2), nullable=True)
    n403 = Column(String(15), nullable=True)
    n404 = Column(String(15), nullable=True)
    n405 = Column(String(2), nullable=True)
    n406 = Column(String(3), nullable=True)
    
    # DMG Segment (Demographic Information) - 1 instance, 5 elements
    dmg01 = Column(String(3), nullable=True)
    dmg02 = Column(String(8), nullable=True)
    dmg03 = Column(String(1), nullable=True)
    dmg04 = Column(String(1), nullable=True)
    dmg05 = Column(String(2), nullable=True)
    
    # LUI Segment (Language) - 1 instance, 2 elements
    lui01 = Column(String(2), nullable=True)
    lui02 = Column(String(2), nullable=True)
    
    # HD Segment (Health Coverage) - Up to 2 instances, 4 elements per instance
    hd01_1 = Column(String(3), nullable=True)
    hd02_1 = Column(String(1), nullable=True)
    hd03_1 = Column(String(3), nullable=True)
    hd04_1 = Column(String(50), nullable=True)
    hd01_2 = Column(String(3), nullable=True)
    hd02_2 = Column(String(1), nullable=True)
    hd03_2 = Column(String(3), nullable=True)
    hd04_2 = Column(String(50), nullable=True)
    
    # AMT Segment (Monetary Amount) - 1 instance, 2 elements
    amt01 = Column(String(3), nullable=True)
    amt02 = Column(String(18), nullable=True)
    
    # LS Segment (Additional Reporting Categories) - 1 instance, 1 element
    ls01 = Column(String(4), nullable=True)
    
    # LE Segment (Additional Reporting Categories Loop Termination) - 1 instance, 1 element
    le01 = Column(String(4), nullable=True)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    # Relationships
    enrollment_file = relationship("EnrollmentFile", back_populates="edi_data_members")
    
    def __repr__(self):
        return f"<EDIData(enrollment_file_id={self.enrollment_file_id}, member_index={self.member_index})>"


class EDIAddtData(Base):
    """
    Additional Reporting Categories Data (LS/LE Loop 2700)
    
    Stores data from Additional Reporting Categories loops (LS/LE) within member records.
    Linked to edi_data via ref02_1 (subscriber identifier).
    
    Segments in LS/LE loop:
    - LS Segment: 1 instance, 1 element (Loop Start)
    - LX Segment: 1 instance, 1 element (Transaction Set Line Number)
    - N1 Segment: 1 instance, 2 elements (Name/Entity Information)
    - REF Segment: 1 instance, 2 elements (Reference Information)
    - DTP Segment: 1 instance, 3 elements (Date/Time/Period)
    - LE Segment: 1 instance, 1 element (Loop End)
    """
    __tablename__ = 'edi_addt_data'
    __table_args__ = {'schema': 'public'}
    
    # Primary Key (composite)
    enrollment_file_id = Column(Integer, ForeignKey('public.enrollment_files.enrollment_file_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    ref02_1 = Column(String(30), primary_key=True, nullable=False)  # Links to edi_data.ref02_1 (subscriber identifier)
    ls_le_index = Column(Integer, primary_key=True, nullable=False)  # Sequential position of LS/LE loop within member (1-based)
    
    # LS Segment (Loop Start) - 1 instance, 1 element
    ls01 = Column(String(4), nullable=True)
    
    # LX Segment (Transaction Set Line Number) - 1 instance, 1 element
    lx01 = Column(String(6), nullable=True)
    
    # N1 Segment (Name/Entity Information) - 1 instance, 2 elements
    n101 = Column(String(3), nullable=True)
    n102 = Column(String(60), nullable=True)
    
    # REF Segment (Reference Information) - 1 instance, 2 elements
    ref01 = Column(String(3), nullable=True)
    ref02 = Column(String(30), nullable=True)
    
    # DTP Segment (Date/Time/Period) - 1 instance, 3 elements
    dtp01 = Column(String(3), nullable=True)
    dtp02 = Column(String(3), nullable=True)
    dtp03 = Column(String(35), nullable=True)
    
    # LE Segment (Loop End) - 1 instance, 1 element
    le01 = Column(String(4), nullable=True)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    # Relationships
    enrollment_file = relationship("EnrollmentFile", back_populates="edi_addt_data_records")
    
    def __repr__(self):
        return f"<EDIAddtData(enrollment_file_id={self.enrollment_file_id}, ref02_1={self.ref02_1}, ls_le_index={self.ls_le_index})>"
