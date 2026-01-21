# COMMONWEALTH OF VIRGINIA

![img-0.jpeg](img-0.jpeg)

# Medicaid Enterprise System (MES) MMIS Companion Guide

# Benefit Enrollment and Maintenance (834)

ASC X12N 834

VERSION 005010X220A1

September 14, 2022

Document Version 2.8

Department of Medical Assistance Services (DMAS)

Page 1

VIRGINIA'S WEDICAID PROGRAM
DMAS
INNOVATION · QUALITY · VALUE
Benefit Enrollment and Maintenance (834)
ASC X12N 834
VERSION 005010 X220A1
14 September 2022

VERSION CHANGE SUMMARY

|  VERSION NO. | DESCRIPTION | DATE  |
| --- | --- | --- |
|  |   |   |
|  Version 1.0 – 1.1 | Xerox VAMMIS FA 5010 Original Implementation | 08/19/2011  |
|  Version 1.2 | Updated with Dental Specific Data Elements | 09/09/2011  |
|  Version 1.3 | Updated with Transportation Specific Data Elements | 09/26/2011  |
|  Version 1.4 | Added INS04 in 2000 Loop for Transportation. Removed the PER05 in 2100A Loop for Transportation. | 11/04/2011  |
|  Version 1.5 | Xerox Rebranding | 06/04/2012  |
|  Version 1.6 | Updated for Behavioral Health | 02/03/2014  |
|  Version 1.7 | Updated for All Level of Care (Dental and Behavioral Health) | 09/12/2014  |
|  Version 1.8 | Updated For Release 67/68 SSN | 10/16/2014  |
|  Version 1.9 | Updated to include CCC MMP Information | 07/08/2015  |
|  Version 2.0 | Updated for Release 73 – COB Carrier ID and Behavioral Health Replacement ID Card | 9/16/2015  |
|  Version 2.1 | Conduent Rebranding | 05/19/2017  |
|  Version 2.2 | Updated for Medicare Administrative Contractors for CCC Plus – 2700 Loop; Removed paragraphs in Special Notes | 06/05/2018  |
|  Version 2.3 | Updated Special Notes regarding 834 file generation | 06/11/2018  |
|  Version 2.4 | Updated for Medicaid Expansion – Added 2300 REF XX1 and 2310 NM110 value 72 - Unknown | 08/29/2018  |
|  Version 2.5 | Updated XA and XG description on Page 9 for CCC Plus and Medallion 4 MCOs | 12/02/2020  |
|  Version 2.6 | Updated the Page Numbers, Added Citizenship Status, Case Review Date and Expected Delivery Date, New Change Source Values, Citizenship Status Values. Reference EWO 2020-350-001-M | 10/08/2021  |
|  Version 2.7 | Effective February 14, 2022 in preparation for MMIS Rebranding to MES April 4, 2022
Updated front matter including:
Introduction – updated links, Purpose – reworded section, and Special Notes –reworded the section and on page 5 information added – DMAS MES EDI web portal access | 01/31/2022  |
|  Version 2.8 | Updated Change Code Source Value for MSR 2018-345-002-M | 09/14/2022  |

Page 2

Benefit Enrollment and Maintenance (834)
ASC X12N 834
VERSION 005010 X220A1
14 September 2022

# INTRODUCTION

The Health Insurance Portability and Accountability Act (HIPAA) requires that Medicaid, and all other health insurance payers in the United States, comply with the EDI standards for health care as established by the Secretary of Health and Human Services. The ANSI X12N implementation guides have been established as the standards of compliance for claim transactions.

The following information is intended to serve only as a companion document to the HIPAA ANSI X12N implementation guides. The use of this document is solely for the purpose of clarification. The information describes specific requirements to be used for processing data. This companion document supplements, but does not contradict any requirements in the X12N implementation guide.

Additional information on the Final Rule for Standards for Electronic Transactions can be found at http://aspe.hhs.gov/admnsimp/final/txfin00.htm. The HIPAA Implementation Guides can be accessed at http://store.x12.org/store

# PURPOSE

This guide provides assistance in the development and use of electronic transfer of benefit enrollment and maintenance data. Conduent adheres to all HIPAA standards and this guide contains clarifications and requirements that are specific to transactions and data elements contained in various segments.

This guide is used for various Vendors (includes Transportation, Behavioral Health and Dental) and any differences will be noted in the comments section specific to the Vendors.

# SPECIAL NOTES

An MCO may request and obtain an NPI. If an NPI is assigned it will be used. MCOs that do not obtain an NPI will be given a new 10-digit DMAS assigned Atypical Provider ID (API). The 834 is generated using the MCO's API or NPI.

Multiple 2300 loops may be written out as necessary to reflect member enrollment segments. These segments are only present for Add (type 021) and Audit (type 030) records and sent out only when additional enrollment information is available on database. These segments can be easily ignored if not needed.

DMMM

Benefit Enrollment and Maintenance (834)

ASC X12N 834

VERSION 005010 X220A1

14 September 2022

The Patient Pay amount (applies only for MCOs, MMPs and Behavioral Health Service Provider) will be sent in AMT segment with AMT01= 'C1'. The Patient Pay begin and end dates are sent in the DTP segment with qualifiers '348' and '349' in DTP01. These segments can be easily ignored if not needed.

The 834 transaction is used to provide member rosters. The Managed Care subsystem of VAMMIS generates an 834 file mid-month for each MCO after assignment runs. CCCPlusand Medallion 4.0 plans also receive two weekly files containing changes on the 6th and 13th of the month. The month end file contains the prospective capitation payment per member, and the remittance date that payment to the provider will occur in the next month. The Behavioral Health and Dental Service vendors receive a daily 834 benefit enrollment file in addition to a monthly 834 file. The NEMT broker receives a weekly and monthly 834 file.

Conduent uses the MOVEit® DMZ application to transmit batch EDI data into the Virginia Medicaid system. All Service Centers must have applied and been authorized by the Virginia EDI Coordinators office before using MOVEit® DMZ.

EDI Submitters can upload and retrieve batch files via the MOVEit® DMZ application using either of two methods:

a. Point a web browser to http://vammis-filetransfer.com and follow the web interface prompts to perform the desire task
b. Use an SFTP Client application that references the vammis-filetransfer.com domain to perform the desired task

MOVEit® DMZ is a secure file transfer and secure message server. It is a vital component of the MOVEit® family of secure file processing, storage, and transfer products developed by Ipswitch, Inc.

These products provide comprehensive, integrated, standards-based solutions for secure handling of sensitive information, including financial files, medical records, legal documents, and personal data.

More information or additional help regarding MOVEit® DMZ can be located on this webpage: https://vamedicaid.dmas.virginia.gov/sites/default/files/2022-01/VAMMIS_File_Transfer_FAQ.pdf

Page 4

Benefit Enrollment and Maintenance (834)

ASC X12N 834

VERSION 005010 X220A1

14 September 2022

EMPORIUM'S MEDICAID PROGRAM

DMAS

DEMONSTRATION - BIBLIOTHEATRIC

The DMAS MES EDI web portal can be accessed from this web page: https://login.vamedicaid.dmas.virginia.gov/SecureISS/landingpage

For initial EDI Enrollment as a Trading partner, complete the Electronic Trading Partner Agreement online. The initial online enrollment can be accessed from this web page: https://vamedicaid.dmas.virginia.gov/form/edi-enrollment. After completing the enrollment, you will receive your credentials along with a unique Service Center ID assigned by Virginia Medicaid via email from no-reply@va.healthinteractive.net. The Virginia EDI test coordinator at Conduent will reach out with testing instructions after the Trading Partner Agreement is signed and approved.

The MES EDI web portal allows Service Centers or Trading Partners to:

- Enroll to submit healthcare transactions electronically
- Authorize trading partners or service centers to retrieve and/or modify electronic X12 transactions
- Self-service for password updates

Use the following link to access the MES EDI Portal FAQs:

https://login.vamedicaid.dmas.virginia.gov/SecureISS/faqLoginPage

VIRGINIA'S MEDICAID PROGRAM
DMAS
INNOVATION · QUALITY · VALUE
Benefit Enrollment and Maintenance (834)
ASC X12N 834
VERSION 005010 X220A1
14 September 2022

DATA ELEMENT DESCRIPTION

|  Page | Loop | Segment | Data Element | Comments  |
| --- | --- | --- | --- | --- |
|  C.4 |  | ISA | ISA01 - Authorization Information Qualifier | 00 – No authorization information present  |
|  C.4 |  | ISA | ISA03 - Security Information Qualifier | 00 – No security information present  |
|  C.4 |  | ISA | ISA05 - Interchange ID Qualifier | ZZ – mutually defined  |
|  C.4 |  | ISA | ISA06 - Interchange Sender ID | VAMMIS FA  |
|  C.5 |  | ISA | ISA07 - Interchange ID Qualifier | ZZ – Mutually defined  |
|  C.5 |  | ISA | ISA08 - Interchange Receiver ID | Medicaid Service Center  |
|  C.5 |  | ISA | ISA12 - Interchange Control Version Number | 00501 - Version Number  |
|  C.6 |  | ISA | ISA14 – Acknowledgment Requested | 0 = No Interchange Acknowledgment Requested  |
|  C.6 |  | ISA | ISA15 - Usage Indicator | P = Production or T = Test  |
|  C.6 |  | ISA | ISA16 - Component Element Separator | ‘>’  |
|  |   |   |   |   |
|  C.7 |  | GS | GS02 - Application Sender's Code | VAMMIS FA  |
|  C.7 |  | GS | GS03 - Application Receiver's Code | 4 digit Service Center ID assigned by Virginia Medicaid  |
|  C.8 |  | GS | GS08 - Version/Release/Industry Identifier Code | 005010X220A1  |
|  |   |   |   |   |
|  36 |  | REF | REF01- Ref ID Qualifier | 38 - Master Policy Number  |
|  36 |  | REF | REF02- Reference ID | Provider NPI
or
DMAS assigned API  |
|  |   |   |   |   |
|  37 |  | DTP | DTP01 – Date/Time Qualifier | 007 - Effective – File Effective Date  |
|  |   |   |   |   |
|  39 | 1000A | N1 | N102 - Plan Sponsor Name (P5) | Department of Medical Assistance Services  |
|  40 | 1000A | N1 | N104 - ID Code | DMAS Federal Tax ID 546116277  |
|  |   |   |   |   |
|  41 | 1000B | N1 | N102 - Insurer Name (IN) | Provider name  |
|  42 | 1000B | N1 | N104 - ID Code | Provider federal tax id  |
|  |   |   |   |   |
|  49 | 2000 | INS | INS03 - Maintenance Type Code | For MCOs and Behavioral Health:
021 - Add
024 - Cancel
030 - Audit
For Dental, MMPs, and Behavioral Health Daily:
030 - Audit
For MMPs mid-month and end of month files:
021 – Add
024 – Cancel
030 – Audit  |

Page 6

Benefit Enrollment and Maintenance (834)

ASC X12N 834

VERSION 005010 X220A1

D

14 September 2022

|  Page | Loop | Segment | Data Element | Comments  |
| --- | --- | --- | --- | --- |
|  49 - 51 | 2000 | INS | INS04 – Maintenance Reason Code | For Transportation Service Provider: XN – Notification Only  |
|  55 | 2000 | REF | REF01 – Ref ID Qualifier | 0F – Subscriber number  |
|  55 | 2000 | REF | REF02 - Reference ID | Member number  |
|  |   |   |   |   |
|  57 | 2000 | REF | REF01 – Ref ID Qualifier | 17 – Client reporting category  |
|  58 | 2000 | REF | REF02 - Reference ID | Program designation code  |
|  |   |   |   |   |
|  57 | 2000 | REF | REF01 – Ref ID Qualifier | 3H – Case Number  |
|  58 | 2000 | REF | REF02 - Reference ID | Case Number  |
|  |   |   |   |   |
|  57 | 2000 | REF | REF01 – Ref ID Qualifier | ZZ – Mutually Defined  |
|  58 | 2000 | REF | REF02 – Reference ID | For Transportation Service Provider: Capitation Rate
For MCOs, MMPs, Behavioral Health, Transportation Service Provider, and Dental Service Providers: CZ-X CR-CCYYMMDD ED-CCYYMMDD
The following are three values that are sent situationally based on data availability.
(Concatenated Field with space between each)
For instance: only one value will be sent if the other two are not available. (REF*ZZ*CZ-A)
CZ- Citizenship Status
CR- Case Review Date
ED- Expected Delivery
Citizenship Status Values for X:
A – Undocumented/Illegal Alien or Legal Alien eligible only for emergency services
C – US Citizen
D – Undocumented/Illegal Alien or Legal Alien eligible only for dialysis srvcs
E – Entrant
I – Immigrant Children
N – Naturalized US Citizen
P – Full-benefit Qualified Alien
R – Refugee
V – Visitor, Temporary Visa  |
|  |   |   |   |   |
|  59-60 | 2000 | DTP | DTP01 – Date/Time Qualifier | For MCOs, MMPs, Behavioral Health, and Dental Service Providers: 356 – Eligibility Begin Date
357 – Eligibility End Date
For Transportation Service Provider: 300 – Enrollment Signature Date – Benefit Plan Date  |

Page 7

VIRGINIA'S WEDICAHS PROGRAM
DMAS
INNOVATION · QUALITY · VALUE
Benefit Enrollment and Maintenance (834)
ASC X12N 834
VERSION 005010 X220A1
14 September 2022

|  64 | 2100A | NM1 | NM108 - Identification Code Qualifier | For Transportation, Behavioral Health, Dental Service Providers: "34" Social Security Number  |
| --- | --- | --- | --- | --- |
|  64 | 2100A | NM1 | NM109 - Identification Code | Social Security Number  |
|  66 | 2100A | PER | PER03 – Communication Number Qualifier | For MCOs and Behavioral Health: TE – Telephone Number
For Transportation and Dental Service Providers: HP – Home Phone Number  |
|  66 | 2100A | PER | PER05 – Communication Number Qualifier | For Dental Service Providers: WP – Work Phone Number  |
|  |   |   |   |   |
|  70 | 2100A | N4 | N405 – Location Qualifier | 60 – Area  |
|  70 | 2100A | N4 | N406 – Location Identifier | FIPS Code  |
|  |   |   |   |   |
|  84 | 2100A | LUI | LUI01- Identification Code Qualifier | LE - ISO 639 Language Codes  |
|  85 | 2100A | LUI | LUI02- Identification Code | Language Code  |
|  |   |   |   |   |
|  142 | 2300 | HD | HD03 – Insurance Line Code | For MCOs, MMPs, Behavioral Health, and Dental Service Providers: HMO - Health Maintenance Organization
For Transportation Service Provider: HLT – Health  |

Page 8

Benefit Enrollment and Maintenance (834)

ASC X12N 834

VERSION 005010 X220A1

DMI

14 September 2022

|  Page | Loop | Segment | Data Element | Comments  |
| --- | --- | --- | --- | --- |
|  142 | 2300 | HD | HD04 – Plan Coverage Description | For MCOs, MMPs Behavioral Health, and Dental Service Providers: Benefit plan package code For Transportation Service Provider: Benefit plan package code (Concatenated field with a short name at the end)  |
|  |   |   |   |   |
|  147 | 2300 | AMT | AMT01 – Amount Qualifier Code | For MCOs and MMPs: P3 – Premium amount  |
|  147 | 2300 | AMT | AMT02 - Monetary Amount | For MCOs and MMPs: Capitation amount - Payments only appear with the end of the month processing.  |
|  |   |   |   |   |
|  148 | 2300 | REF | REF01 – Ref ID Qualifier | For MCOs, MMPs, Behavioral Health, and Dental Service Providers: 17 – Client reporting category (Indicates Managed Care Benefit) For Transportation Service Provider: ZZ –Mutually Defined  |
|  149 | 2300 | REF | REF02 – Reference ID | For MCOs, MMPs, Behavioral Health, and Dental Service Providers: AID Category For Transportation Service Provider: M –Medicaid , O- Other  |
|  |   |   |   |   |
|  The following IDC Segment Occurs for the Replacement ID Card if applicable  |   |   |   |   |
|  |   |   |   |   |
|  150 | 2300 | IDC | IDC01 – Plan Coverage Description | 0 – Indicating no Additional Information  |
|  150 | 2300 | IDC | IDC02 – Identification Card Type Code | H – Indicating Health Insurance  |
|  151 | 2300 | IDC | IDC04 – Action code | RX – Indicating Replacement  |
|  |   |   |   |   |
|  154 | 2310 | NM1 | NM101 – Entity Identifier Code | P3 – Primary Care Provider Code  |
|  154 | 2310 | NM1 | NM102 – Entity Type Qualifier | 2 – Non person Entity  |
|  154 | 2310 | NM1 | NM103 – Provider Last or Organization Name | Full name of the Provider  |
|  |   |   |   |   |
|  160 | 2310 | PER | PER03 – Communication Number Qualifier | For Transportation Service Provider: TE – Telephone  |
|  160 | 2310 | PER | PER04 – Communication Number | For Transportation Service Provider: Provider’s Telephone Number  |
|  |   |   |   |   |
|  The following loop can occur 5 times and provides information to a Third Party Administrator  |   |   |   |   |
|  |   |   |   |   |
|  164 | 2320 | COB | COB01 - Payer Responsibility Sequence Number Code | For MCOs, MMPs, Behavioral Health, and Transportation Service Provider: ‘P’ for PRIMARY ‘S’ for Secondary For Dental Service Provider:  |

Page 9

VIRGINIA'S WEDICAHS PROGRAM
DMAS
INNOVATION · QUALITY · VALUE
Benefit Enrollment and Maintenance (834)
ASC X12N 834
VERSION 005010 X220A1
14 September 2022

|  Page | Loop | Segment | Data Element | Comments  |
| --- | --- | --- | --- | --- |
|   |  |  |  | ‘U’ for Unknown  |
|  164 | 2320 | COB | COB02 - Reference ID | TPL policy number  |
|  164 | 2320 | COB | COB03 - COB Code | 1 – Coordination of benefits  |
|  164 | 2320 | COB | COB04 – Service Type Code | For MCOs, MMPs, and Transportation Service
Provider:
1 - Medical Care
35 - Dental Care
48 - Hospital Inpatient
89 - Free Standing Prescription Drug
A4 - Psychiatric
AG - Skilled Nursing Care
AL - Vision (Optometry)
For Transportation Service Provider:
50 - Hospital Outpatient
54 - Long Term Care Outpatient
For Dental Service Provider:
1 - Medical Care
35 - Dental Care
For Behavioral Health Service Provider:
1 - Medical Care
48 - Hospital Inpatient
A4 - Psychiatric  |
|  |   |   |   |   |
|  166 | 2320 | REF | REF01 - Reference ID Qualifier | 60 - Account Suffix Code  |
|  167 | 2320 | REF | REF02 - Reference ID | TPL coverage type  |
|  |   |   |   |   |
|  166 | 2320 | REF | REF01 - Reference ID Qualifier | ZZ- Mutually Defined  |
|  167 | 2320 | REF | REF02 - Reference ID | TPL Carrier ID  |
|  |   |   |   |   |
|  168 | 2320 | DTP | DTP01 - Date/Time Qualifier | 344 – COB Begin Date  |
|  168 | 2320 | DTP | DTP03 - Date Time Period | TPL Begin Date  |
|  |   |   |   |   |
|  168 | 2320 | DTP | DTP01 - Date/Time Qualifier | 345 – COB End Date  |
|  168 | 2320 | DTP | DTP03 - Date Time Period | TPL End Date  |
|  The following loop can occur 3 times and provides information to a Third Party Administrator  |   |   |   |   |
|  |   |   |   |   |
|  169 | 2330 | NM1 | NM101 - Entity ID Code | IN – Insurer  |
|  170 | 2330 | NM1 | NM103 – Name Last or Organization Name | TPL carrier name  |
|  |   |   |   |   |
|  171 | 2330 | N3 | N301 – Address Information | TPL Carrier Address Line 1  |
|  |   |   |   |   |
|  172 | 2330 | N4 | N401 – City Name | TPL Carrier City Name  |
|  173 | 2330 | N4 | N402 – State or Province Code | TPL Carrier State  |
|  173 | 2330 | N4 | N403 – Postal Code | TPL Carrier Zipcode  |
|  |   |   |   |   |

Page 10

Benefit Enrollment and Maintenance (834)

ASC X12N 834

VERSION 005010 X220A1

D

14 September 2022

|  Page | Loop | Segment | Data Element | Comments  |
| --- | --- | --- | --- | --- |
|  This additional 2300 loop will carry additional benefit segments; it can occur up to 40 times.  |   |   |   |   |
|  140 | 2300 | HD | HD01 – Maintenance type code | For Behavioral Health and the Dental Vendor:
021 - Adds
024 - Cancel
030 - Audits
For Transportation Service Provider:
021 for Adds
030 for Audits  |
|  141 | 2300 | HD | HD03 – Insurance Line Code | For MCOs, Behavioral Health and the Dental Vendor:
HMO - Health Maintenance Organization
For Transportation Service Provider:
HLT – Health  |
|  141 | 2300 | HD | HD04 – Plan Coverage Description | Benefit plan package code (does not apply to the Behavioral Health and the Dental Vendor.)  |
|  143 | 2300 | DTP | DTP01 - Date/Time Qualifier | 348 for Enrollment begin date  |
|  144 | 2300 | DTP | DTP03 - Date Time Period | Enrollment begin date  |
|  143 | 2300 | DTP | DTP01 – Date/Time Qualifier | 349 for Enrollment end date  |
|  144 | 2300 | DTP | DTP03 – Date/Time Period | Enrollment end date  |
|  146 | 2300 | REF | REF01 – Reference ID Qualifier | 1L for Group or Policy Number  |
|  147 | 2300 | REF | REF02 – Reference ID | First two characters of Benefit Plan
For MCOs and Transportation Vendor:
(Default to 00)
For Behavioral Health and the Dental Vendor:
(Default to 01)  |
|  The following segment applies to CCC Plus and Medallion 4.0 MCOs for the Medically Complex benefit:  |   |   |   |   |
|  146 | 2300 | REF | REF01 – Reference ID Qualifier | XX1 for Special Program Code  |
|  147 | 2300 | REF | REF02 – Reference ID | ‘Change Source’ value:
‘X’ - Indicates a screening has been completed, and is not required for this member.
(Loop 2310, NM109 identifies the MCO ID that supplied the most recent screening.)
‘XP’ – Indicates a screening is required for this member. (Member attestation to DSS.)
‘XA’ – Indicates screening was ‘auto-assigned’
‘XG’ – Indicates member is former GAP
‘86’ – Ventilator
‘89’ – Medically Complex
‘92’ - Rehabilitation  |
|  153 | 2310 | NM1 | NM101 – Entity Identifier Code | P3 – Primary Care Provider Code (Only occurs  |
|  154 | 2310 | NM1 | NM102 – Entity Type Qualifier | 2 – Non person Entity  |

|  Page | Loop | Segment | Data Element | Comments  |
| --- | --- | --- | --- | --- |
|  155 | 2310 | NM1 | NM108 – Identification Code Qualifier | SV – Service Provider Number  |
|  155 | 2310 | NM1 | NM109 – Identification Code | Provider ID associated with the benefit in the 2300 loop  |
|  155 | 2310 | NM1 | NM110 – Entity Relationship Code | 25 – Established Patient – default value for benefits (Managed Care, Waivers, EI, etc.); 72 – Unknown – value for Medically Complex benefit (HD04 is ‘01010100X’)  |
|  The following loop will be populated for CCC Plus NPIs to identify a Member's Medicare Administrative Contract ID when available  |   |   |   |   |
|  176 | 2700 | LS | LS01 – Loop Identifier Code | 2700 – Loop Header  |
|  177 | 2710 | LX | LX01 – Assigned Number | A sequential number beginning with 1. If you are only expecting one, this will always be 1.  |
|  178 | 2750 | N1 | N101 – Entity Identifier Code | 75 – Participant  |
|  178 | 2750 | N1 | N102 – Name | Member Reporting Category Name. For example, Member Associated DSNP  |
|  179 | 2750 | REF | REF01 – Reference ID Qualifier | ZZ – Mutually Defined  |
|  180 | 2750 | REF | REF02 – Reference ID | Alphanumeric MAC ID (DE 9064)  |
|  181 | 2750 | DTP | DTP01 – Date/Time Qualifier | 007 – Effective Date  |
|  181 | 2750 | DTP | DTP02 – Date/Time Period Qualifier Format | D8 – CCYYMMDD format  |
|  182 | 2750 | DTP | DTP03 – Date/Time Period | Effective date of the month – For example, if we are running in October for November, date would be “20171101”  |
|  183 | 2700 | LE | LE01 – Loop Identifier Code | 2700 – Loop Trailer  |

Page 12