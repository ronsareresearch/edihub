"""
[TREO] - Member-Level Storage Models
Date: 2026-01-20
Purpose: SQLAlchemy models for scalable member-level storage

These models enable storing each member (Loop 2000) as a separate database row
instead of storing all members in a single JSONB column, allowing for:
- Scalable storage (no JSONB size limits)
- Queryable members (SQL queries per member)
- Indexed member fields
- Faster queries and updates
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Index
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database_treo import BaseTreo as Base


class EnrollmentFileMember(Base):
    """
    Member-level storage model.
    Stores each member (Loop 2000) as a separate row for scalable processing.
    """
    __tablename__ = 'enrollment_file_members'
    __table_args__ = {'schema': 'public'}
    
    member_id = Column(Integer, primary_key=True, autoincrement=True)
    enrollment_file_id = Column(Integer, ForeignKey('public.enrollment_files.enrollment_file_id', ondelete='CASCADE'), nullable=False, index=True)
    member_index = Column(Integer, nullable=False)  # Order in file (0-based or 1-based)
    member_data = Column(JSONB, nullable=False)  # Complete member JSON (Loop 2000 + nested loops)
    ins_segment = Column(JSONB, nullable=True)  # INS segment data for quick queries
    parsed_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    # Relationships
    enrollment_file = relationship("EnrollmentFile", back_populates="members")
    segments = relationship("EnrollmentFileSegment", back_populates="member", cascade="all, delete-orphan")
    
    # Unique constraint: one member per index per file
    __table_args__ = (
        Index('ix_enrollment_file_members_member_index', 'enrollment_file_id', 'member_index', unique=True),
        {'schema': 'public'}
    )
    
    def __repr__(self):
        return f"<EnrollmentFileMember(member_id={self.member_id}, enrollment_file_id={self.enrollment_file_id}, member_index={self.member_index})>"


class EnrollmentFileSegment(Base):
    """
    Segment-level storage model.
    Stores individual segments for advanced querying (optional).
    """
    __tablename__ = 'enrollment_file_segments'
    __table_args__ = {'schema': 'public'}
    
    segment_id = Column(Integer, primary_key=True, autoincrement=True)
    enrollment_file_id = Column(Integer, ForeignKey('public.enrollment_files.enrollment_file_id', ondelete='CASCADE'), nullable=False, index=True)
    member_id = Column(Integer, ForeignKey('public.enrollment_file_members.member_id', ondelete='CASCADE'), nullable=True, index=True)
    segment_code = Column(String(10), nullable=False, index=True)  # INS, REF, DTP, etc.
    segment_order = Column(Integer, nullable=False)  # Order in file
    segment_data = Column(JSONB, nullable=False)  # Segment element data
    parsed_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    # Relationships
    enrollment_file = relationship("EnrollmentFile", back_populates="file_segments")
    member = relationship("EnrollmentFileMember", back_populates="segments")
    
    def __repr__(self):
        return f"<EnrollmentFileSegment(segment_id={self.segment_id}, segment_code='{self.segment_code}', member_id={self.member_id})>"


class EnrollmentFileProcessingStatus(Base):
    """
    Processing status tracking model.
    Tracks parsing progress for resumable processing of large files.
    """
    __tablename__ = 'enrollment_file_processing_status'
    __table_args__ = {'schema': 'public'}
    
    status_id = Column(Integer, primary_key=True, autoincrement=True)
    enrollment_file_id = Column(Integer, ForeignKey('public.enrollment_files.enrollment_file_id', ondelete='CASCADE'), nullable=False, unique=True, index=True)
    total_segments = Column(Integer, nullable=True)
    segments_parsed = Column(Integer, nullable=False, server_default='0')
    members_parsed = Column(Integer, nullable=False, server_default='0')
    current_segment_index = Column(Integer, nullable=True)
    last_checkpoint_at = Column(DateTime(timezone=True), nullable=True)
    processing_status = Column(String(50), nullable=False, server_default='pending', index=True)
    # Status values: pending, processing, completed, failed, paused
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    enrollment_file = relationship("EnrollmentFile", back_populates="processing_status_rel")
    
    def __repr__(self):
        return f"<EnrollmentFileProcessingStatus(status_id={self.status_id}, enrollment_file_id={self.enrollment_file_id}, processing_status='{self.processing_status}', members_parsed={self.members_parsed})>"
