"""
[TREO] - Metadata Schema Models
Date: 2026-01-20
Purpose: SQLAlchemy models for metadata schema in enroll database
Contains EDI 834 metadata tables: loops, segments, elements, etc.
"""
from sqlalchemy import Column, Integer, String, SmallInteger, DateTime, ForeignKey, PrimaryKeyConstraint, Boolean
from sqlalchemy.orm import relationship
from app.database_treo import BaseTreo as Base


# ============================================================================
# Core Metadata Tables
# ============================================================================

class Loop(Base):
    """
    Loop metadata table - defines EDI 834 loops.
    """
    __tablename__ = 'loops'
    __table_args__ = {'schema': 'metadata'}
    
    loop_id = Column(Integer, primary_key=True, autoincrement=True)
    loopid = Column(String(15), nullable=False, unique=True, index=True)
    name = Column(String(200), nullable=False)
    repeat_min = Column(SmallInteger, nullable=False)
    repeat_max = Column(SmallInteger, nullable=True)
    loop_desc = Column(String(200), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True)
    updated_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    loop_segments = relationship("LoopSegment", back_populates="loop")
    loop_elements = relationship("LoopElement", back_populates="loop")
    code_values = relationship("CodeValue", back_populates="loop")
    loop_element_additional_syntax = relationship("LoopElementAdditionalSyntax", back_populates="loop")
    
    def __repr__(self):
        return f"<Loop(loop_id={self.loop_id}, loopid='{self.loopid}', name='{self.name}')>"


class Segment(Base):
    """
    Segment metadata table - defines EDI 834 segments.
    """
    __tablename__ = 'segments'
    __table_args__ = {'schema': 'metadata'}
    
    segment_id = Column(Integer, primary_key=True, autoincrement=True)
    segmentid = Column(String(50), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    elements = relationship("Element", back_populates="segment")
    loop_segments = relationship("LoopSegment", back_populates="segment")
    
    def __repr__(self):
        return f"<Segment(segment_id={self.segment_id}, segmentid='{self.segmentid}')>"


class Element(Base):
    """
    Element metadata table - defines EDI 834 elements.
    """
    __tablename__ = 'elements'
    __table_args__ = {'schema': 'metadata'}
    
    element_id = Column(Integer, primary_key=True, autoincrement=True)
    segment_id = Column(Integer, ForeignKey('metadata.segments.segment_id'), nullable=False)
    name = Column(String(500), nullable=True)
    min_length = Column(SmallInteger, nullable=False)
    max_length = Column(SmallInteger, nullable=False)
    ref_designator = Column(String(10), nullable=False, index=True)
    elementdatatype_id = Column(Integer, ForeignKey('metadata.element_data_types.elementdatatype_id'), nullable=False)
    parent_element_id = Column(Integer, ForeignKey('metadata.elements.element_id'), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    segment = relationship("Segment", back_populates="elements")
    element_data_type = relationship("ElementDataType", back_populates="elements")
    parent_element = relationship("Element", remote_side=[element_id], backref="child_elements")
    loop_elements = relationship("LoopElement", back_populates="element")
    code_values = relationship("CodeValue", back_populates="element")
    loop_element_additional_syntax = relationship("LoopElementAdditionalSyntax", back_populates="element")
    
    def __repr__(self):
        return f"<Element(element_id={self.element_id}, ref_designator='{self.ref_designator}', name='{self.name}')>"


# ============================================================================
# Reference/Lookup Tables
# ============================================================================

class ElementDataType(Base):
    """
    Element data type reference table.
    """
    __tablename__ = 'element_data_types'
    __table_args__ = {'schema': 'metadata'}
    
    elementdatatype_id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(10), nullable=False)
    type = Column(String(50), nullable=False)
    
    # Relationships
    elements = relationship("Element", back_populates="element_data_type")
    
    def __repr__(self):
        return f"<ElementDataType(elementdatatype_id={self.elementdatatype_id}, symbol='{self.symbol}', type='{self.type}')>"


class IndustryUsage(Base):
    """
    Industry usage reference table (R, S, P, C, E usage codes).
    """
    __tablename__ = 'industry_usage'
    __table_args__ = {'schema': 'metadata'}
    
    usage_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    usage_type = Column(String(1), nullable=False)  # R, S, P, C, E
    usage_type_desc = Column(String(200), nullable=False)
    
    # Relationships
    loop_segments = relationship("LoopSegment", back_populates="usage")
    loop_elements = relationship("LoopElement", back_populates="usage")
    
    def __repr__(self):
        return f"<IndustryUsage(usage_id={self.usage_id}, usage_type='{self.usage_type}', usage_type_desc='{self.usage_type_desc}')>"


class SyntaxRule(Base):
    """
    Syntax rules reference table.
    """
    __tablename__ = 'syntax_rules'
    __table_args__ = {'schema': 'metadata'}
    
    syntaxrule_id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(200), nullable=True)
    
    # Relationships
    syntaxes = relationship("Syntax", back_populates="syntax_rule")
    
    def __repr__(self):
        return f"<SyntaxRule(syntaxrule_id={self.syntaxrule_id}, description='{self.description}')>"


class Syntax(Base):
    """
    Syntax table - links syntax rules to syntax IDs.
    """
    __tablename__ = 'syntax'
    __table_args__ = {'schema': 'metadata'}
    
    syntax_id = Column(Integer, primary_key=True, autoincrement=True)
    syntaxid = Column(String(20), nullable=False)
    syntaxrule_id = Column(Integer, ForeignKey('metadata.syntax_rules.syntaxrule_id'), nullable=False)
    
    # Relationships
    syntax_rule = relationship("SyntaxRule", back_populates="syntaxes")
    loop_elements = relationship("LoopElement", back_populates="syntax")
    loop_element_additional_syntax = relationship("LoopElementAdditionalSyntax", back_populates="syntax")
    
    def __repr__(self):
        return f"<Syntax(syntax_id={self.syntax_id}, syntaxid='{self.syntaxid}')>"


# ============================================================================
# Junction/Relationship Tables
# ============================================================================

class LoopSegment(Base):
    """
    Loop-Segment relationship table - defines which segments belong to which loops.
    """
    __tablename__ = 'loop_segments'
    __table_args__ = (
        PrimaryKeyConstraint('segment_id', 'loop_id'),
        {'schema': 'metadata'}
    )
    
    segment_id = Column(Integer, ForeignKey('metadata.segments.segment_id'), nullable=False)
    loop_id = Column(Integer, ForeignKey('metadata.loops.loop_id'), nullable=False)
    order_no = Column(SmallInteger, nullable=False)
    usage_id = Column(Integer, ForeignKey('metadata.industry_usage.usage_id'), nullable=False)
    segment_repeat_min = Column(SmallInteger, nullable=False)
    segment_repeat_max = Column(SmallInteger, nullable=True)
    segment_name = Column(String(500), nullable=False)
    
    # Relationships
    segment = relationship("Segment", back_populates="loop_segments")
    loop = relationship("Loop", back_populates="loop_segments")
    usage = relationship("IndustryUsage", back_populates="loop_segments")
    
    def __repr__(self):
        return f"<LoopSegment(loop_id={self.loop_id}, segment_id={self.segment_id}, order_no={self.order_no})>"


class LoopElement(Base):
    """
    Loop-Element relationship table - defines which elements belong to which loops.
    """
    __tablename__ = 'loop_elements'
    __table_args__ = (
        PrimaryKeyConstraint('loop_id', 'element_id'),
        {'schema': 'metadata'}
    )
    
    loop_id = Column(Integer, ForeignKey('metadata.loops.loop_id'), nullable=False)
    element_id = Column(Integer, ForeignKey('metadata.elements.element_id'), nullable=False)
    order_no = Column(SmallInteger, nullable=False)
    usage_id = Column(Integer, ForeignKey('metadata.industry_usage.usage_id'), nullable=False)
    syntax_id = Column(Integer, ForeignKey('metadata.syntax.syntax_id'), nullable=True)
    note = Column(String(500), nullable=True)
    
    # Relationships
    loop = relationship("Loop", back_populates="loop_elements")
    element = relationship("Element", back_populates="loop_elements")
    usage = relationship("IndustryUsage", back_populates="loop_elements")
    syntax = relationship("Syntax", back_populates="loop_elements")
    
    def __repr__(self):
        return f"<LoopElement(loop_id={self.loop_id}, element_id={self.element_id}, order_no={self.order_no})>"


class CodeValue(Base):
    """
    Code values table - defines valid code values for elements within loops.
    """
    __tablename__ = 'code_values'
    __table_args__ = (
        PrimaryKeyConstraint('loop_id', 'element_id', 'codevalue_id'),
        {'schema': 'metadata'}
    )
    
    loop_id = Column(Integer, ForeignKey('metadata.loops.loop_id'), nullable=False)
    element_id = Column(Integer, ForeignKey('metadata.elements.element_id'), nullable=False)
    codevalue_id = Column(Integer, nullable=False)
    value = Column(String(255), nullable=True)
    definition = Column(String(1000), nullable=True)
    
    # Relationships
    loop = relationship("Loop", back_populates="code_values")
    element = relationship("Element", back_populates="code_values")
    
    def __repr__(self):
        return f"<CodeValue(loop_id={self.loop_id}, element_id={self.element_id}, codevalue_id={self.codevalue_id}, value='{self.value}')>"


class LoopElementAdditionalSyntax(Base):
    """
    Additional syntax rules for loop elements.
    """
    __tablename__ = 'loop_element_additional_syntax'
    __table_args__ = {'schema': 'metadata'}
    
    loop_id = Column(Integer, ForeignKey('metadata.loops.loop_id'), nullable=False, primary_key=True)
    element_id = Column(Integer, ForeignKey('metadata.elements.element_id'), nullable=False, primary_key=True)
    syntax_id = Column(Integer, ForeignKey('metadata.syntax.syntax_id'), nullable=False, primary_key=True)
    
    # Relationships
    loop = relationship("Loop", back_populates="loop_element_additional_syntax")
    element = relationship("Element", back_populates="loop_element_additional_syntax")
    syntax = relationship("Syntax", back_populates="loop_element_additional_syntax")
    
    def __repr__(self):
        return f"<LoopElementAdditionalSyntax(loop_id={self.loop_id}, element_id={self.element_id}, syntax_id={self.syntax_id})>"


# ============================================================================
# Control Segment Tables
# ============================================================================

class ControlSegment(Base):
    """
    Control segment metadata (ISA, GS, GE, IEA, ST, SE).
    """
    __tablename__ = 'control_segments'
    __table_args__ = {'schema': 'metadata'}
    
    controlsegment_id = Column(Integer, primary_key=True, autoincrement=True)
    segmentid = Column(String(10), nullable=False)
    name = Column(String(500), nullable=False)
    
    # Relationships
    control_segment_elements = relationship("ControlSegmentElement", back_populates="control_segment")
    
    def __repr__(self):
        return f"<ControlSegment(controlsegment_id={self.controlsegment_id}, segmentid='{self.segmentid}', name='{self.name}')>"


class ControlSegmentElement(Base):
    """
    Control segment elements metadata.
    """
    __tablename__ = 'control_segment_elements'
    __table_args__ = {'schema': 'metadata'}
    
    controlsegmentelement_id = Column(Integer, primary_key=True, autoincrement=True)
    controlsegment_id = Column(Integer, ForeignKey('metadata.control_segments.controlsegment_id'), nullable=False)
    name = Column(String(500), nullable=False)
    min_length = Column(SmallInteger, nullable=False)
    max_length = Column(SmallInteger, nullable=False)
    order_no = Column(SmallInteger, nullable=False)
    usage_id = Column(Integer, ForeignKey('metadata.industry_usage.usage_id'), nullable=False)
    elementdatatype_id = Column(Integer, ForeignKey('metadata.element_data_types.elementdatatype_id'), nullable=True)
    
    # Relationships
    control_segment = relationship("ControlSegment", back_populates="control_segment_elements")
    element_data_type = relationship("ElementDataType")
    usage = relationship("IndustryUsage")
    control_segment_code_values = relationship("ControlSegmentCodeValue", back_populates="control_segment_element")
    control_segment_element_data = relationship("ControlSegmentElementData", back_populates="control_segment_element")
    
    def __repr__(self):
        return f"<ControlSegmentElement(controlsegmentelement_id={self.controlsegmentelement_id}, name='{self.name}')>"


class ControlSegmentCodeValue(Base):
    """
    Code values for control segment elements.
    """
    __tablename__ = 'control_segment_code_values'
    __table_args__ = {'schema': 'metadata'}
    
    codevalue_id = Column(Integer, primary_key=True, autoincrement=True)
    controlsegmentelement_id = Column(Integer, ForeignKey('metadata.control_segment_elements.controlsegmentelement_id'), nullable=False)
    value = Column(String(255), nullable=True)
    definition = Column(String(1000), nullable=True)
    
    # Relationships
    control_segment_element = relationship("ControlSegmentElement", back_populates="control_segment_code_values")
    
    def __repr__(self):
        return f"<ControlSegmentCodeValue(codevalue_id={self.codevalue_id}, value='{self.value}')>"


class ControlSegmentElementData(Base):
    """
    Additional data for control segment elements.
    """
    __tablename__ = 'control_segment_element_data'
    __table_args__ = {'schema': 'metadata'}
    
    cselementdata_id = Column(Integer, primary_key=True, autoincrement=True)
    controlsegmentelement_id = Column(Integer, ForeignKey('metadata.control_segment_elements.controlsegmentelement_id'), nullable=False)
    data_value = Column(String(100), nullable=True)
    is_active = Column(Boolean, nullable=False, server_default='true')
    
    # Relationships
    control_segment_element = relationship("ControlSegmentElement", back_populates="control_segment_element_data")
    
    def __repr__(self):
        return f"<ControlSegmentElementData(cselementdata_id={self.cselementdata_id}, data_value='{self.data_value}')>"


class ElementDataTypeExpression(Base):
    """
    Regular expressions for element data types.
    """
    __tablename__ = 'element_data_type_expressions'
    __table_args__ = {'schema': 'metadata'}
    
    elementdatatypeexp_id = Column(Integer, primary_key=True, autoincrement=True)
    elementdatatype_id = Column(Integer, ForeignKey('metadata.element_data_types.elementdatatype_id'), nullable=False)
    regular_expression = Column(String(1000), nullable=False)
    description = Column(String(500), nullable=False)
    
    # Relationships
    element_data_type = relationship("ElementDataType")
    
    def __repr__(self):
        return f"<ElementDataTypeExpression(elementdatatypeexp_id={self.elementdatatypeexp_id}, description='{self.description}')>"


class ElementComment(Base):
    """
    Comments for elements.
    """
    __tablename__ = 'element_comments'
    __table_args__ = {'schema': 'metadata'}
    
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    loop_id = Column(Integer, nullable=True)
    loopid = Column(String(10), nullable=True)
    loop = Column(String(50), nullable=True)
    element_id = Column(Integer, nullable=True)
    element = Column(String(100), nullable=True)
    comments = Column(String(1000), nullable=True)
    
    def __repr__(self):
        return f"<ElementComment(comment_id={self.comment_id}, element='{self.element}')>"
