ASCX12

# CONSOLIDATED GUIDE

# Benefit Enrollment and Maintenance (834)

Consolidated Documents:

August 2006 005010X220

June 2010 005010X220A1

February 2011

ASC X12 Consolidated Guides aid in transaction implementation by combining official material into one user friendly document. Although the consolidated guides have not been explicitly mandated under HIPAA, they incorporate the individual guides that have been named into single documents. In the event that there is a conflict between the Consolidated Guides and the ASC X12 Type 3 Technical Reports or any subsequent errata, the underlying ASC X12 publications are the authoritative source.

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

Copyright © 2011, Data Interchange Standards Association (DISA) on behalf of the membership of ASC X12. Format © 2011 Washington Publishing Company (WPC). Exclusively published by WPC under license from DISA. All Rights Reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, recording or otherwise, without prior written permission.

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

# Table of Contents

## 1 Purpose and Business Information
1.1 Implementation Purpose and Scope 1
1.2 Version Information 1
1.3 Implementation Limitations 2
1.3.1 Batch and Real-time Usage 2
1.3.2 Other Usage Limitations 2
1.4 Business Usage 3
1.4.1 Information Flows 3
1.4.2 Location of Insurance Product Identifiers 3
1.4.3 Linking a Dependent to a Subscriber 4
1.4.4 Termination 5
1.4.5 Updates, Versus Full File Audits, Versus Full File Replacements 6
1.4.6 Coverage Levels and Dependents 7
1.5 Business Terminology 7
1.5.1 Date Terminology 9
1.6 Transaction Acknowledgments 9
1.6.1 997 Functional Acknowledgment 9
1.6.2 999 Implementation Acknowledgment 10
1.6.3 824 Application Advice 10
1.7 Related Transactions 10
1.8 Trading Partner Agreements 11
1.9 The HIPAA Role in Implementation Guides 11

## 2 Transaction Sets
2.1 Presentation Examples 13
2.2 Implementation Usage 18
2.2.1 Industry Usage 18
2.2.1.1 Transaction Compliance Related to Industry Usage 19
2.2.2 Loops 19
2.3 Transaction Set Listing 21
2.3.1 Implementation 21
2.3.2 Standard 25
2.4 834 Segment Detail 30
ST Transaction Set Header 31
BGN Beginning Segment 32
REF Transaction Set Policy Number 36
DTP File Effective Date 37
QTY Transaction Set Control Totals 38
N1 Sponsor Name 39
N1 Payer 41
N1 TPA/Broker Name 43

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

ACT TPA/Broker Account Information...45
INS Member Level Detail...47
REF Subscriber Identifier...55
REF Member Policy Number...56
REF Member Supplemental Identifier...57
DTP Member Level Dates...59
NM1 Member Name...62
PER Member Communications Numbers...65
N3 Member Residence Street Address...68
N4 Member City, State, ZIP Code...69
DMG Member Demographics...72
EC Employment Class...76
ICM Member Income...79
AMT Member Policy Amounts...81
HLH Member Health Information...82
LUI Member Language...84
NM1 Incorrect Member Name...86
DMG Incorrect Member Demographics...89
NM1 Member Mailing Address...93
N3 Member Mail Street Address...95
N4 Member Mail City, State, ZIP Code...96
NM1 Member Employer...98
PER Member Employer Communications Numbers...101
N3 Member Employer Street Address...104
N4 Member Employer City, State, ZIP Code...105
NM1 Member School...107
PER Member School Communications Numbers...109
N3 Member School Street Address...112
N4 Member School City, State, ZIP Code...113
NM1 Custodial Parent...115
PER Custodial Parent Communications Numbers...118
N3 Custodial Parent Street Address...121
N4 Custodial Parent City, State, ZIP Code...122
NM1 Responsible Person...124
PER Responsible Person Communications Numbers..127
N3 Responsible Person Street Address...130
N4 Responsible Person City, State, ZIP Code...131
NM1 Drop Off Location...133
N3 Drop Off Location Street Address...135
N4 Drop Off Location City, State, ZIP Code...136
DSB Disability Information...138
DTP Disability Eligibility Dates...140
HD Health Coverage...141
DTP Health Coverage Dates...145
AMT Health Coverage Policy...147
REF Health Coverage Policy Number...148
REF Prior Coverage Months...150
IDC Identification Card...152
LX Provider Information...154
NM1 Provider Name...155
N3 Provider Address...158
N4 Provider City, State, ZIP Code...159
PER Provider Communications Numbers...161

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

PLA Provider Change Reason ... 164
COB Coordination of Benefits ... 166
REF Additional Coordination of Benefits Identifiers ... 168
DTP Coordination of Benefits Eligibility Dates ... 170
NM1 Coordination of Benefits Related Entity ... 171
N3 Coordination of Benefits Related Entity Address .. 173
N4 Coordination of Benefits Other Insurance Company City, State, ZIP Code ... 174
PER Administrative Communications Contact ... 176
LS Additional Reporting Categories ... 178
LX Member Reporting Categories ... 179
N1 Reporting Category ... 180
REF Reporting Category Reference ... 181
DTP Reporting Category Date ... 183
LE Additional Reporting Categories Loop Termination ... 185
SE Transaction Set Trailer ... 186

## 3 Examples ... 187
3.1 Business Case Scenario 1 ... 187
3.2 Business Case Scenario 2 ... 188
3.3 Business Case Scenario 3 ... 189
3.4 Business Case Scenario 4 ... 190
3.5 Business Case Scenario 5 ... 191
3.6 Business Case Scenario 6 ... 192
3.7 Business Case Scenario 7 ... 193
3.8 Business Case Scenario 8 ... 194
3.9 Business Case Scenario 9 ... 195
3.10 Business Case Scenario 10 ... 195

## A External Code Sources ... A.1
5 Countries, Currencies and Funds ... A.1
22 States and Provinces ... A.2
51 ZIP Code ... A.2
94 International Organization for Standardization (Date and Time) ... A.3
102 Languages ... A.4
131 International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM) ... A.4
206 Government Bill of Lading Office Code ... A.5
307 National Council for Prescription Drug Programs Pharmacy Number ... A.5
457 NISO Z39.53 Language Code List ... A.6
537 Centers for Medicare and Medicaid Services National Provider Identifier ... A.6
540 Centers for Medicare and Medicaid Services PlanID ... A.7
859 Classification of Race or Ethnicity ... A.7
860 Race or Ethnicity Collection Code ... A.8
897 International Classification of Diseases, 10th Revision, Clinical Modification (ICD-10-CM) ... A.8
932 Universal Postal Codes ... A.9

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

## B Nomenclature 8.1

### B.1 ASC X12 Nomenclature 8.1

#### B.1.1 Interchange and Application Control Structures B.1

- B.1.1.1 Interchange Control Structure B.1
- B.1.1.2 Application Control Structure Definitions and Concepts B.2
- B.1.1.3 Business Transaction Structure Definitions and Concepts B.6
- B.1.1.4 Envelopes and Control Structures B.19
- B.1.1.5 Acknowledgments B.22

### B.2 Object Descriptors B.23

## C EDI Control Directory C.1

### C.1 Control Segments C.1

- ISA Interchange Control Header C.3
- GS Functional Group Header C.7
- GE Functional Group Trailer C.9
- IEA Interchange Control Trailer C.10

## D Change Summary D.1

## E Data Element Glossary E.1

### E.1 Data Element Name Index E.1

FEBRUARY 2011

CONSOLIDATED · 834

BENEFIT ENROLLMENT AND MAINTENANCE

005010X220 &amp; 005010X220A1

# 1 Purpose and Business Information

## 1.1 Implementation Purpose and Scope

For the health care industry to achieve the potential administrative cost savings with Electronic Data Interchange (EDI), standards have been developed and need to be implemented consistently by all organizations. To facilitate a smooth transition into the EDI environment, uniform implementation is critical.

The purpose of this implementation guide is to provide standardized data requirements and content to users of Version 005010 of ANSI ASC X12, Benefit Enrollment and Maintenance (834). The 834 is used to transfer enrollment information from the sponsor of the insurance coverage, benefits, or policy to a payer. The intent of this implementation guide is to meet the health care industry's specific need for the initial enrollment and subsequent maintenance of individuals who are enrolled in insurance products. This implementation guide specifically addresses the enrollment and maintenance of health care products only. One or more separate guides may be developed for life, flexible spending, and retirement products.

## 1.2 Version Information

This implementation guide is based on the October 2003 ASC X12 standards, referred to as Version 5, Release 1, Sub-release 0 (005010).

The unique Version/Release/Industry Identifier Code for transaction sets that are defined by this implementation guide is 005010X220A1.

The two-character Functional Identifier Code for the transaction set included in this implementation guide:

- BE Benefit Enrollment and Maintenance (834)

The Version/Release/Industry Identifier Code and the applicable Functional Identifier Code must be transmitted in the Functional Group Header (GS segment) that begins a functional group of these transaction sets. For more information, see the descriptions of GS01 and GS08 in Appendix C, EDI Control Directory.

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

# 1.3 Implementation Limitations

## 1.3.1 Batch and Real-time Usage

There are multiple methods available for sending and receiving business transactions electronically. Two common modes for EDI transactions are batch and real-time.

**Batch** - In a batch mode the sender does not remain connected while the receiver processes the transactions. Processing is usually completed according to a set schedule. If there is an associated business response transaction (such as a 271 Response to a 270 Request for Eligibility), the receiver creates the response transaction and stores it for future delivery. The sender of the original transmission reconnects at a later time and picks up the response transaction. This implementation guide does not set specific response time parameters for these activities.

**Real Time** - In real-time mode the sender remains connected while the receiver processes the transactions and returns a response transaction to the sender. This implementation guide does not set specific response time parameters for implementers.

This implementation guide is intended to support use in batch mode. This implementation guide is not intended to support use in real-time mode. A statement that the transaction is not intended to support a specific mode does not preclude its use in that mode between willing trading partners.

## 1.3.2 Other Usage Limitations

There are not other usage limitations.

Any response back to the Sponsor from the received transaction is outside the scope of the 834 and is the responsibility of the sponsor and payer.

FEBRUARY 2011

CONSOLIDATED · 834

BENEFIT ENROLLMENT AND MAINTENANCE

005010X220 &amp; 005010X220A1

# 1.4 Business Usage

## 1.4.1 Information Flows

![img-0.jpeg](img-0.jpeg)
Figure 1.1 - Health Care

Transaction sets included in the information flow diagram:

- 834: Benefit Enrollment and Maintenance
- 820: Payment Order/Remittance Advice
- 270: Health Care Eligibility/Benefit Inquiry
- 271: Health Care Eligibility/Benefit Information

## 1.4.2 Location of Insurance Product Identifiers

The 834 allows three locations for Insurance Product Identifiers, such as policy numbers and group numbers:

1. A situational REF segment at the Transaction level
2. A situational REF segment at the Member level (loop 2000)
3. A situational REF segment at the Health Coverage level (loop 2300)

The work group found that there was no consistent use for the Insurance Product Identifier at any level. For this reason, the consensus by the work group was to make the Insurance Product Identifier situational at all the levels. However, at least one REF segment containing the Insurance Product Identifier must be present for each Insurance Product either at the Transaction, Member, or Health Coverage level.

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

The work group selected code "38", Master Policy Number, at the Transaction level. This identifier is to be sent when the Insurance Product Identifier applies to all the Insurance Products in the Transaction.

The work group found that most of the time the Insurance Product Identifier is communicated at the Member level (loop 2000). The work group selected code "1L", Group or Policy Number, at this level. The Group or Policy Number applies to all the Health Coverage iterations (loop 2300) for the member named in loop 2000. Other iterations of the REF segment with other qualifiers are included to support business needs under the specific policy. The developers of this implementation guide were not able to limit the sender to a single code because of the variety of different insurance plans.

At the Health Coverage level (loop 2300), the sender also has the option of sending the Group or Policy Number. The work group selected code "1L", Group or Policy Number, at this level. This applies when different policy numbers exist for each Insurance Product specified in the HD segments.

## 1.4.3 Linking a Dependent to a Subscriber

Subscribers and dependents are sent as separate occurrences of Loop ID-2000. The initial enrollment for the subscriber must be sent before sending the initial enrollment for any of the subscriber's dependents. The enrollment of a dependent may follow the subscriber's enrollment in the same transmission, or it may be sent separately in a later transmission. Maintaining the existing enrollments of a subscriber and dependents can occur in any sequence.

Payers use various means to link dependents to the subscriber. The most common method is to use the subscriber's Social Security Number (SSN). To allow linking between subscribers and dependents without making assumptions about the receiving system, use the code "0F," Subscriber Number, in the REF segment, Loop ID-2000, position 0200. The subscriber's unique identifier is sent in this segment in both the subscriber's and the dependent's Loop ID-2000.

The individual's SSN is sent and identified as such in NM108, Loop ID-2000, position 0300. This applies to both subscribers and dependents. If the SSN is used for linking, then the subscriber's SSN is sent in both locations on the subscriber's Loop ID-2000.

FEBRUARY 2011

CONSOLIDATED · 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

## 1.4.4 Termination

The content of transactions intended to terminate coverage for subscribers and/or related members was the subject of extensive discussion during development of this implementation guide. The work group attempted to strike a balance between the systemic and operational benefits of highly detailed, rich data content and the reality of a current practice in which many plan sponsors and other originators of this transaction may have less than complete data on hand.

To accommodate the greatest possible number of users, the work group adopted a guiding principle that only the minimum necessary data would be required for a given type of termination, but that additional data could be sent at the sender's discretion. Trading partners should agree on their approach to communicating terminations in their trading partner agreement. Regardless of additional data and trading partner agreements, transactions of certain format and content must cause very specific outcomes in receiver systems.

A termination date passed at the INS level for an individual who is the subscriber (That is, a termination date passed in the DTP segment in position 0250 in the 2000 loop for an INS segment with INS01 = 'Y') indicates that all coverages for that subscriber and any associated dependants are to be terminated in the receiver's system on the indicated date. Said another way, if a subscriber, spouse and two children are all enrolled in medical, prescription and vision coverages in the receiver's system, an "Eligibility End" date passed in that DTP segment for the subscriber must cause the termination of all three coverages for all four individuals in the receiver's system on the date provided in DTP03.

A termination date passed at the INS level for an individual who is not the subscriber (That is, a termination date passed in the DTP segment in position 0250 in the 2000 loop for an INS segment with INS01 = 'N') indicates that all coverages for that individual are to be terminated in the receiver's system on the indicated date. If a subscriber, spouse and two children are all enrolled in medical, prescription and vision coverages in the receiver's system, an "Eligibility End" date passed in that DTP segment for the spouse must cause the termination of all three coverages for one individual (the spouse).

A termination date passed at the HD level (that is, a termination date passed in the DTP segment in position 2700 in the 2300 loop for an HD loop of any coverage type) applies singly to an individual and a coverage. If a subscriber, spouse and two children are all enrolled in medical, prescription and vision coverages in the receiver's system, a "Benefit End" date passed in the DTP segment subordinate to the vision coverage for the spouse indicates that the last day of the spouse's vision coverage is the date provided in that

FEBRUARY 2011
5

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

segment's DTP03. Coverage for other lines of coverage for the member will not be affected, nor will any coverage for any other member linked to the same subscriber.

Termination dates are not to be sent at both the HD and INS levels for a particular occurrence of loop 2000.

For an individual who is not the subscriber, terminating all lines of coverage at the HD level is the equivalent of terminating that dependent at the INS level. For a subscriber, terminating all insurance products at the HD level is not equivalent to passing the termination at the INS level. Passing terminations at the INS level for a subscriber causes all coverages for all linked dependants to be terminated. Passing terminations at the HD level for a subscriber does not affect the coverages of other individuals linked to that subscriber - dependants may continue to be covered in dependant-only coverage.

A change of coverage or an addition of coverage may not automatically result in the termination of existing coverage unless this is clearly agreed upon in the Trading Partner Agreement.

Member records that were previously reported as covered and subsequently omitted from the full file replacement can be terminated by the receiver if the process is clearly agreed upon in the Trading Partner Agreement.

# 1.4.5 Updates, Versus Full File Audits, Versus Full File Replacements

The 834 transaction can be used to provide either updates to the enrollment database, full file audits of the 834 enrollment process, or full file replacements.

An update is either an "add", "terminate" or "change" request. The transaction only contains information about the changed members. This is identified in BGN08 by a code value of '2', Change (Update).

A full file audit lists all current members, whether involved in a change or not. This facilitates keeping the sponsor's and payer's systems in sync. This is not intended to contain a history of all previous enrollments. The full file audit is intended to identify all active members, at a given point in time and may or may not include terminated members based on your Trading Partner Agreement. The full file audit is not intended to be used to make any changes to the enrollment database. This type of transaction is identified by a BGN08 code value of '4', Verify. Any response back to the sponsor from the received transactions are outside the scope of the 834 and are the responsibility of the sponsor

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

and payer. In addition, INS03 in Loop 2000 and HD01 in Loop 2300 must be set to a value of '030', Audit or Compare.

A full file identified in BGN08 by a code value of 'RX', Replace, is intended to identify all active members, at a given point in time and may or may not include terminated members based on your Trading Partner Agreement. This transaction allows a payer to identify additions, terminations, and changes that need to be applied to the payer's system.

## 1.4.6 Coverage Levels and Dependents

Differences exist in how Payers handle dependents. Some Payers identify a coverage level (HD05) for the subscriber which defines the coverage for eligible dependents as well. Other Payers need detailed information on each dependent in order to maintain their databases. Still other Payers require both types of information.

The trading partner agreement between the Payer and the Sponsor must identify the member reporting requirements for the Enrollment transaction.

When the insurance contract requires the Coverage Level code and no dependent information, HD05 is Required for all initial enrollment or changes to the Coverage Level Code.

When Dependent information is required without the Coverage Level Codes, separate INS loops are Required for enrollment or change for each dependent. See the Termination section for more information. HD05 is NOT USED for any dependent.

When the dependent information and Coverage Level Code are Required, the Coverage Level Code (HD05) must be used for all subscriber initial enrollment or when the Subscriber's Coverage Level Code changes. This change applies to all covered dependents of the subscriber. The Coverage Level Code is NOT USED with dependent enrollment, changes or terminations. Note: If a dependent addition or termination effectively changes the Coverage Level Code of a subscriber, the subscriber must be changed directly if the insurance contract requires use of the Coverage Level Code.

## 1.5 Business Terminology

**Dependent**

A dependent is an individual who is eligible for coverage because of his or her association with a subscriber. Typically, a dependent is a member of the subscriber's family.

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

## Health Care Providers

Health care providers are individuals and organizations that provide health care services. Health care providers can include physicians, hospitals, clinics, pharmacies, and long-term care facilities. The legal definition of health care provider is included in section 262, Administrative Simplification, of the Health Insurance Portability and Accountability Act of 1996.

## Insured or Member

An insured individual or member is a subscriber or dependent who has been enrolled for coverage under an insurance plan. Dependents of a Subscriber who have not been individually enrolled for coverage are not included in Insured or Member.

## Payer/Insurer

The payer is the party that pays claims and/or administers the insurance coverage, benefit, or product. A payer can be an insurance company; Health Maintenance Organization (HMO); Preferred Provider Organization (PPO); a government agency, such as Medicare or CHAMPUS/TRICARE; or another organization contracted by one of these groups.

## Plan Administrator

The plan administrator is the entity that administers a benefit plan and determines the amount to be paid on a claim but does not actually make the payment.

## Sponsor

A sponsor is the party that ultimately pays for the coverage, benefit, or product. A sponsor can be an employer, union, government agency, association, or insurance agency.

## Subscriber

The subscriber is an individual eligible for coverage because of his or her association with a sponsor. Examples of subscribers include the following: employees; union members; and individuals covered under government programs, such as Medicare and Medicaid

## Third Party Administrator (TPA)

A sponsor may elect to contract with a Third Party Administrator (TPA) or other vendor to handle collecting insured member data if the sponsor chooses not to perform this function.

## Vendors/Intermediaries

Vendors and intermediaries are organizations that distribute information about eligibility for specific benefits, but they do not actually administer the plan or make payments.

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

## 1.5.1 Date Terminology

Users of past 834 implementation guides encountered considerable confusion about what codes should be used for dates related to the insured in Loop ID-2000 and to the insurance coverage in Loop ID-2300. This confusion resulted because several codes with very similar uses were available. These codes include the following: effective date, eligibility date, enrollment date, plan date, coverage date, and benefit date.

The tendency has been to try to use the same terminology as that used in the application systems. Lengthy discussion was required to reach a resolution because the application systems' terminology often differed among different systems. To facilitate communications between different systems, the developers of this implementation guide have limited the codes in Loop ID-2300 DTP, with the term "benefit" being used for actual dates of coverage. The developers of this implementation guide recommend that the term "Eligibility" is used from the point of view of the plan sponsor. That is, an individual's "eligibility" dates are those during which he or she may choose to be covered by the sponsor's benefits. The developers further recommend that the term "enrollment" be used from the point of view of the payor. In this case, an individual's "enrollment" dates are those dates during which he or she is covered by a particular benefit.

Many more codes are listed in the DTP segment in Loop ID-2000. The developers of this implementation guide recommend that the term "eligibility" be used to refer to the dates on which an insured individual may choose to be covered.

## 1.6 Transaction Acknowledgments

There are several acknowledgment implementation transactions available for use. The IG developers have noted acknowledgment requirements in this section. Other recommendations of acknowledgment transactions may be used at the discretion of the trading partners. A statement that the acknowledgment is not required does not preclude its use between willing trading partners.

## 1.6.1 997 Functional Acknowledgment

The 997 informs the submitter that the functional group arrived at the destination. It may include information about the syntactical quality of the functional group.

The Functional Acknowledgment (997) transaction is not required as a response to receipt of a batch transaction compliant with this implementation guide.

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

The Functional Acknowledgment (997) transaction is not required as a response to receipt of a real-time transaction compliant with this implementation guide.

A 997 Implementation Guide is being developed for use by the insurance industry and is expected to be available for use with this version of this Implementation Guide.

## 1.6.2 999 Implementation Acknowledgment

The 999 informs the submitter that the functional group arrived at the destination. It may include information about the syntactical quality of the functional group and the implementation guide compliance.

The Implementation Acknowledgment (999) transaction is not required as a response to receipt of a batch transaction compliant with this implementation guide.

The Implementation Acknowledgment (999) transaction is not required as a response to receipt of a real-time transaction compliant with this implementation guide.

A 999 Implementation Guide is being developed for use by the insurance industry and is expected to be available for use with this version of this Implementation Guide.

## 1.6.3 824 Application Advice

The 824 informs the submitter of the results of the receiving application system's data content edits of transaction sets.

The Application Advice (824) transaction is not required as a response to receipt of a batch transaction compliant with this implementation guide.

The Application Advice (824) transaction is not required as a response to receipt of a real-time transaction compliant with this implementation guide.

An 824 Implementation Guide is being developed for use by the insurance industry and is expected to be available for use with this version of this Implementation Guide.

## 1.7 Related Transactions

There are no transactions related to the transactions described in this implementation guide.

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

## 1.8 Trading Partner Agreements

Trading partner agreements are used to establish and document the relationship between trading partners. A trading partner agreement must not override the specifications in this implementation guide if a transmission is reported in GS08 to be a product of this implementation guide.

## 1.9 HIPAA Role in Implementation Guides

Administrative Simplification provisions of the Health Insurance Portability and Accountability Act of 1996 (PL 104-191 - known as HIPAA) direct the Secretary of Health and Human Services to adopt standards for transactions to enable health information to be exchanged electronically and to adopt specifications for implementing each standard.

This implementation guide has been developed for use as an insurance industry implementation guide. At the time of publication it has not been adopted as a HIPAA standard. Should the Secretary adopt this implementation guide as a standard, the Secretary will establish compliance dates for its use by HIPAA covered entities.

FEBRUARY 2011
11

__________

__________

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

# 2 Transaction Set

NOTE
See Appendix B, Nomenclature, to review the transaction set structure, including descriptions of segments, data elements, levels, and loops.

## 2.1 Presentation Examples

The ASC X12 standards are generic. For example, multiple trading communities use the same PER segment to specify administrative communication contacts. Each community decides which elements to use and which code values in those elements are applicable.

This implementation guide uses a format that depicts both the generalized standard and the insurance industry-specific implementation. In this implementation guide, IMPLEMENTATION specifies the requirements for this implementation. X12 STANDARD is included as a reference only.

The transaction set presentation is comprised of two main sections with subsections within the main sections:

### 2.3 Transaction Set Listing

There are two sub-sections under this general title. The first sub-section concerns this implementation of a generic X12 transaction set. The second sub-section concerns the generic X12 standard itself.

**IMPLEMENTATION**
This section lists the levels, loops, and segments contained in this implementation. It also serves as an index to the segment detail.

**STANDARD**
This section is included as a reference.

### 2.4 Segment Detail

There are three sub-sections under this general title. This section repeats once for each segment used in this implementation providing segment specific detail and X12 standard detail.

**SEGMENT DETAIL**
This section is included as a reference.

**DIAGRAM**
This section is included as a reference. It provides a pictorial view of the standard and shows which elements are used in this implementation.

**ELEMENT DETAIL**
This section specifies the implementation details of each data element.

FEBRUARY 2011
13

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

These illustrations (Figures 2.1 through 2.5) are examples and are not extracted from the Section 2 detail in this implementation guide. Annotated illustrations, presented below in the same order they appear in this implementation guide, describe the format of the transaction set that follows.

FEBRUARY 2011

CONSOLIDATED • 834

BENEFIT ENROLLMENT AND MAINTENANCE

005010X220 &amp; 005010X220A1

# IMPLEMENTATION

Indicates that this section is the implementation and not the standard

# 8XX Insurance Transaction Set

Table 1 - Header

|  PAGE # | POS. # | SEG. ID | NAME | USAGE | REPEAT | LOOP REPEAT  |
| --- | --- | --- | --- | --- | --- | --- |
|  53 | 0100 | ST | Transaction Set Header | Each segment is assigned an industry specific name. Not used segments do not appear | R | 1  |
|  54 | 0200 | BPR | Financial Information |  | R | 1  |
|  60 | 0400 | TRN | Reassociation Key |  | R | 1  |
|  62 | 0500 | CUR | Non-US Dollars Currency |  | S | 1  |
|  65 | 0600 | REF | Receiver ID | Each loop is assigned an industry specific name | S | 1  |
|  66 | 0600 | REF | Version Number |  | S | 1  |
|  68 | 0700 | DTM | Production Date |  | S | 1  |
|   |  |  | PAYER NAME |  |  | 1  |
|  70 | 0800 | N1 | Payer Name |  | R | 1  |
|  72 | 1000 | N3 | Payer Address | R=Required | S | 1  |
|  75 | 1100 | N4 | Payer City, State, Zip | S=Situational | S | 1  |
|  76 | 1200 | REF | Additional Payer Reference Number |  | S | 1  |
|  78 | 1300 | PER | Payer Contact |  | S | 1  |
|   |  |  | PAYEE NAME |  |  | 1  |
|  79 | 0800 | N1 | Payee Name |  | R | 1  |
|  81 | 1000 | N3 | Payee Address |  | S | 1  |
|  82 | 1100 | N4 | Payee City, State, Zip |  | S | 1  |
|  84 | 1200 | REF | Payee Additional Reference Number |  | S | >1  |
|  Position Numbers and Segment IDs retain their X12 values Individual segments and entire loops are repeated  |   |   |   |   |   |   |

Figure 2.1. Transaction Set Key — Implementation

# STANDARD

# 8XX Insurance Transaction Set

Indicates that this section is identical to the ASC X12 standard

Functional Group ID: XX

See Appendix B.1, ASC X12 Nomenclature for a complete description of the standard

This Draft Standard for Trial Use contains the format and establishes the data contents of the Insurance Transaction Set (8XX) within the context of the Electronic Data Interchange (EDI) environment.

Table 1 - Header

|  POS. # | SEG. ID | NAME | REQ. DES. | MAX USE | LOOP REPEAT  |
| --- | --- | --- | --- | --- | --- |
|  0100 | ST | Transaction Set Header | M | 1 |   |
|  0200 | BPR | Beginning Segment | M | 1 |   |
|  0300 | NTE | Note/Special Instruction | O | >1 |   |
|  0400 | TRN | Trace | O | 1 |   |

Figure 2.2. Transaction Set Key — Standard

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE

005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

# SEGMENT DETAIL

Industry assigned
Segment Name
**NM1 - PATIENT NAME**

X12 Segment Name: Individual or Organizational Name

X12 Purpose: To supply the full name of an individual or organizational entity

X12 Syntax:
1. P0809
If either NM108 or NM109 is present, then the other is required.

2. C1110
If NM111 is present, then NM110 is required.

Industry assigned
Loop ID and Loop Name

Industry Segment
Repeat
Loop: 2100B — PATIENT NAME  Loop Repeat: 1

Segment: 1

Industry
usage
→ Usage: SITUATIONAL

Situational Rule: Required when the patient is different from the insured. If not required by this implementation guide, do not send.

TR3 Notes: 1. Any necessary identification number must be provided in NM109.

Industry
Notes
TR3 Example: NM1*QC*1*Shepard*Sam*A***34*452114586~

Example

![img-1.jpeg](img-1.jpeg)
Figure 2.3. Segment Key — Implementation
DIAGRAM
Figure 2.4. Segment Key — Diagram

FEBRUARY 2011

CONSOLIDATED • 834

BENEFIT ENROLLMENT AND MAINTENANCE

005010X220 &amp; 005010X220A1

![img-2.jpeg](img-2.jpeg)

Figure 2.5. Segment Key — Element Summary

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

## 2.2 Implementation Usage

### 2.2.1 Industry Usage

Industry Usage describes when loops, segments, and elements are to be sent when complying with this implementation guide. The three choices for Usage are required, not used, and situational. To avoid confusion, these are named differently than the X12 standard Condition Designators (mandatory, optional, and relational).

**Required** This loop/segment/element must always be sent.

Required segments in Situational loops only occur when the loop is used.

Required elements in Situational segments only occur when the segment is used.

Required component elements in Situational composite elements only occur when the composite element is used.

**Not Used** This element must never be sent.

**Situational** Use of this loop/segment/element varies, depending on data content and business context as described in the defining rule. The defining rule is documented in a Situational Rule attached to the item.

There are two forms of Situational Rules.

The first form is “Required when <explicit condition="" statement="">. If not required by this implementation guide, may be provided at the sender’s discretion, but cannot be required by the receiver.” The data qualified by such a situational rule cannot be required or requested by the receiver, transmission of this data is solely at the sender’s discretion.

The alternative form is “Required when <explicit condition="" statement="">. If not required by this implementation guide, do not send.” The data qualified by such a situational rule cannot be sent except as described in the explicit condition statement.

FEBRUARY 2011</explicit></explicit>

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

## 2.2.1.1 Transaction Compliance Related to Industry Usage

A transmitted transaction complies with an implementation guide when it satisfies the requirements as defined within the implementation guide. The presence or absence of an item (loop, segment, or element) complies with the industry usage specified by this implementation guide according to the following table.

|  Industry Usage | Business Condition is | Item is | Transaction Complies with Implementation Guide?  |
| --- | --- | --- | --- |
|  Required | N/A | Sent | Yes  |
|   |   |  Not Sent | No  |
|  Not Used | N/A | Sent | No  |
|   |   |  Not Sent | Yes  |
|  Situational (Required when <explicit condition statement>. If not required by this implementation guide, may be provided at the sender’s discretion, but cannot be required by the receiver.) | True | Sent | Yes  |
|   |   |  Not Sent | No  |
|   |  Not True | Sent | Yes  |
|   |   |  Not Sent | Yes  |
|  Situational (Required when <explicit condition statement>. If not required by this implementation guide, do not send.) | True | Sent | Yes  |
|   |   |  Not Sent | No  |
|   |  Not True | Sent | No  |
|   |   |  Not Sent | Yes  |

This table specifies how an entity is to evaluate a transmitted transaction for compliance with industry usage. It is not intended to require or imply that the receiver must reject non-compliant transactions. The receiver will handle non-compliant transactions based on its business process and any applicable regulations.

## 2.2.2 Loops

Loop requirements depend on the context or location of the loop within the transaction. See Appendix B for more information on loops.

- A nested loop can be used only when the associated higher level loop is used.
- The usage of a loop is the same as the usage of its beginning segment.
- If a loop’s beginning segment is Required, the loop is Required and must occur at least once unless it is nested in a loop that is not being used.
- If a loop’s beginning segment is Situational, the loop is Situational.
- Subsequent segments within a loop can be sent only when the beginning segment is used.
- Required segments in Situational loops occur only when the loop is used.

FEBRUARY 2011
19

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1
CONSOLIDATED • 834

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834

## 2.3 Transaction Set Listing

### 2.3.1 Implementation

This section lists the levels, loops, and segments contained in this implementation. It also serves as an index to the segment detail. Refer to section 2.1 Presentation Examples for detailed information on the components of the Implementation section.

FEBRUARY 2011
21

005010X220 &amp; 005010X220A1 • 834

CONSOLIDATED • 834

IMPLEMENTATION

# 834 Benefit Enrollment and Maintenance

Table 1 - Header

|  PAGE # | POS. # | SEG. ID | NAME | USAGE | REPEAT | LOOP REPEAT  |
| --- | --- | --- | --- | --- | --- | --- |
|  31 | 0100 | ST | Transaction Set Header | R | 1 |   |
|  32 | 0200 | BGN | Beginning Segment | R | 1 |   |
|  36 | 0300 | REF | Transaction Set Policy Number | S | 1 |   |
|  37 | 0400 | DTP | File Effective Date | S | >1 |   |
|  38 | 0600 | QTY | Transaction Set Control Totals | S | 3 |   |
|   |  |  | LOOP ID - 1000A SPONSOR NAME |  |  | 1  |
|  39 | 0700 | N1 | Sponsor Name | R | 1 |   |
|   |  |  | LOOP ID - 1000B PAYER |  |  | 1  |
|  41 | 0700 | N1 | Payer | R | 1 |   |
|   |  |  | LOOP ID - 1000C TPA/BROKER NAME |  |  | 2  |
|  43 | 0700 | N1 | TPA/Broker Name | S | 1 |   |
|   |  |  | LOOP ID - 1100C TPA/BROKER ACCOUNT INFORMATION |  |  | 1  |
|  45 | 1200 | ACT | TPA/Broker Account Information | S | 1 |   |

Table 2 - Detail

|  PAGE # | POS. # | SEG. ID | NAME | USAGE | REPEAT | LOOP REPEAT  |
| --- | --- | --- | --- | --- | --- | --- |
|   |  |  | LOOP ID - 2000 MEMBER LEVEL DETAIL |  |  | >1  |
|  47 | 0100 | INS | Member Level Detail | R | 1 |   |
|  55 | 0200 | REF | Subscriber Identifier | R | 1 |   |
|  56 | 0200 | REF | Member Policy Number | S | 1 |   |
|  57 | 0200 | REF | Member Supplemental Identifier | S | 13 |   |
|  59 | 0250 | DTP | Member Level Dates | S | 24 |   |
|   |  |  | LOOP ID - 2100A MEMBER NAME |  |  | 1  |
|  62 | 0300 | NM1 | Member Name | R | 1 |   |
|  65 | 0400 | PER | Member Communications Numbers | S | 1 |   |
|  68 | 0500 | N3 | Member Residence Street Address | S | 1 |   |
|  69 | 0600 | N4 | Member City, State, ZIP Code | S | 1 |   |
|  72 | 0800 | DMG | Member Demographics | S | 1 |   |
|  76 | 1000 | EC | Employment Class | S | >1 |   |
|  79 | 1100 | ICM | Member Income | S | 1 |   |
|  81 | 1200 | AMT | Member Policy Amounts | S | 7 |   |
|  82 | 1300 | HLH | Member Health Information | S | 1 |   |
|  84 | 1500 | LUI | Member Language | S | >1 |   |
|   |  |  | LOOP ID - 2100B INCORRECT MEMBER NAME |  |  | 1  |
|  86 | 0300 | NM1 | Incorrect Member Name | S | 1 |   |
|  89 | 0800 | DMG | Incorrect Member Demographics | S | 1 |   |
|   |  |  | LOOP ID - 2100C MEMBER MAILING ADDRESS |  |  | 1  |
|  93 | 0300 | NM1 | Member Mailing Address | S | 1 |   |
|  95 | 0500 | N3 | Member Mail Street Address | R | 1 |   |
|  96 | 0600 | N4 | Member Mail City, State, ZIP Code | R | 1 |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834

|   |  | LOOP ID - 2100D MEMBER EMPLOYER |   |   | 3  |
| --- | --- | --- | --- | --- | --- |
|  98 | 0300 | NM1 | Member Employer | S | 1  |
|  101 | 0400 | PER | Member Employer Communications Numbers | S | 1  |
|  104 | 0500 | N3 | Member Employer Street Address | S | 1  |
|  105 | 0600 | N4 | Member Employer City, State, ZIP Code | S | 1  |
|   |  |  | LOOP ID - 2100E MEMBER SCHOOL |  | 3  |
|  107 | 0300 | NM1 | Member School | S | 1  |
|  109 | 0400 | PER | Member School Communications Numbers | S | 1  |
|  112 | 0500 | N3 | Member School Street Address | S | 1  |
|  113 | 0600 | N4 | Member School City, State, ZIP Code | S | 1  |
|   |  |  | LOOP ID - 2100F CUSTODIAL PARENT |  | 1  |
|  115 | 0300 | NM1 | Custodial Parent | S | 1  |
|  118 | 0400 | PER | Custodial Parent Communications Numbers | S | 1  |
|  121 | 0500 | N3 | Custodial Parent Street Address | S | 1  |
|  122 | 0600 | N4 | Custodial Parent City, State, ZIP Code | S | 1  |
|   |  |  | LOOP ID - 2100G RESPONSIBLE PERSON |  | 13  |
|  124 | 0300 | NM1 | Responsible Person | S | 1  |
|  127 | 0400 | PER | Responsible Person Communications Numbers | S | 1  |
|  130 | 0500 | N3 | Responsible Person Street Address | S | 1  |
|  131 | 0600 | N4 | Responsible Person City, State, ZIP Code | S | 1  |
|   |  |  | LOOP ID - 2100H DROP OFF LOCATION |  | 1  |
|  133 | 0300 | NM1 | Drop Off Location | S | 1  |
|  135 | 0500 | N3 | Drop Off Location Street Address | S | 1  |
|  136 | 0600 | N4 | Drop Off Location City, State, ZIP Code | S | 1  |
|   |  |  | LOOP ID - 2200 DISABILITY INFORMATION |  | >1  |
|  138 | 2000 | DSB | Disability Information | S | 1  |
|  140 | 2100 | DTP | Disability Eligibility Dates | S | 2  |
|   |  |  | LOOP ID - 2300 HEALTH COVERAGE |  | 99  |
|  141 | 2600 | HD | Health Coverage | S | 1  |
|  145 | 2700 | DTP | Health Coverage Dates | R | 6  |
|  147 | 2800 | AMT | Health Coverage Policy | S | 9  |
|  148 | 2900 | REF | Health Coverage Policy Number | S | 14  |
|  150 | 2900 | REF | Prior Coverage Months | S | 1  |
|  152 | 3000 | IDC | Identification Card | S | 3  |
|   |  |  | LOOP ID - 2310 PROVIDER INFORMATION |  | 30  |
|  154 | 3100 | LX | Provider Information | S | 1  |
|  155 | 3200 | NM1 | Provider Name | R | 1  |
|  158 | 3500 | N3 | Provider Address | S | 2  |
|  159 | 3600 | N4 | Provider City, State, ZIP Code | S | 1  |
|  161 | 3700 | PER | Provider Communications Numbers | S | 2  |
|  164 | 3950 | PLA | Provider Change Reason | S | 1  |
|   |  |  | LOOP ID - 2320 COORDINATION OF BENEFITS |  | 5  |
|  166 | 4000 | COB | Coordination of Benefits | S | 1  |
|  168 | 4050 | REF | Additional Coordination of Benefits Identifiers | S | 4  |
|  170 | 4070 | DTP | Coordination of Benefits Eligibility Dates | S | 2  |
|   |  |  | LOOP ID - 2330 COORDINATION OF BENEFITS RELATED ENTITY |  | 3  |
|  171 | 4100 | NM1 | Coordination of Benefits Related Entity | S | 1  |
|  173 | 4300 | N3 | Coordination of Benefits Related Entity Address | S | 1  |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834
CONSOLIDATED • 834

|  174 | 4400 | N4 | Coordination of Benefits Other Insurance Company City, State, ZIP Code | S | 1  |
| --- | --- | --- | --- | --- | --- |
|  176 | 4500 | PER | Administrative Communications Contact | S | 1  |
|  178 | 6880 | LS | Additional Reporting Categories | S | 1  |
|   |  |  | LOOP ID - 2700 MEMBER REPORTING CATEGORIES |  | >1  |
|  179 | 6881 | LX | Member Reporting Categories | S | 1  |
|   |  |  | LOOP ID - 2750 REPORTING CATEGORY |  | 1  |
|  180 | 6882 | N1 | Reporting Category | S | 1  |
|  181 | 6883 | REF | Reporting Category Reference | S | 1  |
|  183 | 6884 | DTP | Reporting Category Date | S | 1  |
|  185 | 6885 | LE | Additional Reporting Categories Loop Termination | S | 1  |
|  186 | 6900 | SE | Transaction Set Trailer | R | 1  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834

## 2.3.2 X12 Standard

This section is included as a reference. The implementation guide reference clarifies actual usage. Refer to section 2.1 Presentation Examples for detailed information on the components of the X12 Standard section.

FEBRUARY 2011
25

005010X220 &amp; 005010X220A1 • 834

CONSOLIDATED • 834

STANDARD

# 834 Benefit Enrollment and Maintenance

Functional Group ID: BE

This X12 Transaction Set contains the format and establishes the data contents of the Benefit Enrollment and Maintenance Transaction Set (834) for use within the context of an Electronic Data Interchange (EDI) environment. This transaction set can be used to establish communication between the sponsor of the insurance product and the payer. Such transaction(s) may or may not take place through a third party administrator (TPA).

For the purpose of this standard, the sponsor is the party or entity that ultimately pays for the coverage, benefit or product. A sponsor can be an employer, union, government agency, association, or insurance agency.

The payer refers to an entity that pays claims, administers the insurance product or benefit, or both. A payer can be an insurance company, health maintenance organization (HMO), preferred provider organization (PPO), government agency (Medicare, Medicaid, Champus, etc.), or an entity that may be contracted by one of these former groups.

For the purpose of the 834 transaction set, a third party administrator (TPA) can be contracted by a sponsor to handle data gathering from those covered by the sponsor if the sponsor does not elect to perform this function itself.

Table 1 - Header

|  POS. # | SEG. ID | NAME | REQ. DES. | MAX USE | LOOP REPEAT  |
| --- | --- | --- | --- | --- | --- |
|  0100 | ST | Transaction Set Header | M | 1 |   |
|  0200 | BGN | Beginning Segment | M | 1 |   |
|  0300 | REF | Reference Information | O | >1 |   |
|  0400 | DTP | Date or Time or Period | O | >1 |   |
|  0500 | AMT | Monetary Amount Information | O | >1 |   |
|  0600 | QTY | Quantity Information | O | >1 |   |
|   |  | LOOP ID - 1000 |  |  | >1  |
|  0700 | N1 | Party Identification | M | 1 |   |
|  0800 | N2 | Additional Name Information | O | 2 |   |
|  0900 | N3 | Party Location | O | 2 |   |
|  1000 | N4 | Geographic Location | O | 1 |   |
|  1100 | PER | Administrative Communications Contact | O | 3 |   |
|   |  | LOOP ID - 1100 |  |  | 10  |
|  1200 | ACT | Account Identification | O | 1 |   |
|  1300 | REF | Reference Information | O | 5 |   |
|  1400 | N3 | Party Location | O | 1 |   |
|  1500 | N4 | Geographic Location | O | 1 |   |
|  1600 | PER | Administrative Communications Contact | O | 5 |   |
|  1700 | DTP | Date or Time or Period | O | 1 |   |
|  1800 | AMT | Monetary Amount Information | O | 1 |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834

# Table 2 - Detail

|  POS. # | SEG. ID | NAME | REQ. DES. | MAX USE | LOOP REPEAT  |
| --- | --- | --- | --- | --- | --- |
|   |  | LOOP ID - 2000 |  |  | >1  |
|  0100 | INS | Insured Benefit | O | 1 |   |
|  0200 | REF | Reference Information | M | >1 |   |
|  0250 | DTP | Date or Time or Period | O | >1 |   |
|   |  | LOOP ID - 2100 |  |  | >1  |
|  0300 | NM1 | Individual or Organizational Name | O | 1 |   |
|  0400 | PER | Administrative Communications Contact | O | 1 |   |
|  0500 | N3 | Party Location | O | 1 |   |
|  0600 | N4 | Geographic Location | O | 1 |   |
|  0800 | DMG | Demographic Information | O | 1 |   |
|  0900 | PM | Electronic Funds Transfer Information | O | 1 |   |
|  1000 | EC | Employment Class | O | >1 |   |
|  1100 | ICM | Individual Income | O | 1 |   |
|  1200 | AMT | Monetary Amount Information | O | 10 |   |
|  1300 | HLH | Health Information | O | 1 |   |
|  1400 | HI | Health Care Information Codes | O | 10 |   |
|  1500 | LUI | Language Use | O | >1 |   |
|   |  | LOOP ID - 2200 |  |  | 4  |
|  2000 | DSB | Disability Information | O | 1 |   |
|  2100 | DTP | Date or Time or Period | O | 10 |   |
|  2200 | AD1 | Adjustment Amount | O | 10 |   |
|   |  | LOOP ID - 2300 |  |  | 99  |
|  2600 | HD | Health Coverage | O | 1 |   |
|  2700 | DTP | Date or Time or Period | O | 10 |   |
|  2800 | AMT | Monetary Amount Information | O | 3 |   |
|  2900 | REF | Reference Information | O | 5 |   |
|  3000 | IDC | Identification Card | O | >1 |   |
|   |  | LOOP ID - 2310 |  |  | 30  |
|  3100 | LX | Transaction Set Line Number | O | 1 |   |
|  3200 | NM1 | Individual or Organizational Name | O | 1 |   |
|  3300 | N1 | Party Identification | O | 3 |   |
|  3400 | N2 | Additional Name Information | O | 1 |   |
|  3500 | N3 | Party Location | O | 2 |   |
|  3600 | N4 | Geographic Location | O | 2 |   |
|  3700 | PER | Administrative Communications Contact | O | 2 |   |
|  3800 | PRV | Provider Information | O | 1 |   |
|  3900 | DTP | Date or Time or Period | O | 6 |   |
|  3950 | PLA | Place or Location | O | 1 |   |
|   |  | LOOP ID - 2320 |  |  | 5  |
|  4000 | COB | Coordination of Benefits | O | 1 |   |
|  4050 | REF | Reference Information | O | >1 |   |
|  4070 | DTP | Date or Time or Period | O | 2 |   |
|   |  | LOOP ID - 2330 |  |  | 3  |
|  4100 | NM1 | Individual or Organizational Name | O | 1 |   |
|  4200 | N2 | Additional Name Information | O | 1 |   |
|  4300 | N3 | Party Location | O | 2 |   |
|  4400 | N4 | Geographic Location | O | 1 |   |
|  4500 | PER | Administrative Communications Contact | O | 1 |   |
|   |  | LOOP ID - 2400 |  |  | 10  |
|  4600 | LC | Life Coverage | O | 1 |   |

FEBRUARY 2011
27

005010X220 &amp; 005010X220A1 • 834

CONSOLIDATED • 834

|  4700 AMT | Monetary Amount Information | O | 5  |
| --- | --- | --- | --- |
|  4800 DTP | Date or Time or Period | O | 2  |
|  4850 REF | Reference Information | O | >1  |
|  LOOP ID - 2410 |   |   | 20  |
|  4900 BEN | Beneficiary or Owner Information | O | 1  |
|  5000 NM1 | Individual or Organizational Name | O | 1  |
|  5100 N1 | Party Identification | O | 1  |
|  5200 N2 | Additional Name Information | O | 1  |
|  5300 N3 | Party Location | O | 1  |
|  5400 N4 | Geographic Location | O | 1  |
|  5420 DMG | Demographic Information | O | 1  |
|  LOOP ID - 2500 |   |   | 5  |
|  5500 FSA | Flexible Spending Account | O | 1  |
|  5600 AMT | Monetary Amount Information | O | 10  |
|  5700 DTP | Date or Time or Period | O | 10  |
|  5750 REF | Reference Information | O | >1  |
|  LOOP ID - 2600 |   |   | >1  |
|  5800 RP | Retirement Product | O | 1  |
|  5900 DTP | Date or Time or Period | O | >1  |
|  5920 REF | Reference Information | O | >1  |
|  5940 INV | Investment Vehicle Selection | O | >1  |
|  5960 AMT | Monetary Amount Information | O | 20  |
|  5970 QTY | Quantity Information | O | 20  |
|  5980 K3 | File Information | O | 3  |
|  6000 REL | Relationship | O | 1  |
|  LOOP ID - 2610 |   |   | >1  |
|  6100 NM1 | Individual or Organizational Name | O | 1  |
|  6300 N2 | Additional Name Information | O | 1  |
|  6510 DMG | Demographic Information | O | 1  |
|  6520 BEN | Beneficiary or Owner Information | O | 1  |
|  6530 REF | Reference Information | O | >1  |
|  LOOP ID - 2620 |   |   | >1  |
|  6540 NX1 | Property or Entity Identification | O | 1  |
|  6550 N3 | Party Location | O | 1  |
|  6560 N4 | Geographic Location | O | 1  |
|  6570 DTP | Date or Time or Period | O | >1  |
|  LOOP ID - 2630 |   |   | >1  |
|  6600 FC | Financial Contribution | O | 1  |
|  6700 DTP | Date or Time or Period | O | >1  |
|  LOOP ID - 2640 |   |   | >1  |
|  6780 INV | Investment Vehicle Selection | O | 1  |
|  6790 DTP | Date or Time or Period | O | >1  |
|  6800 QTY | Quantity Information | O | >1  |
|  6810 ENT | Entity | O | >1  |
|  6820 REF | Reference Information | O | >1  |
|  6830 AMT | Monetary Amount Information | O | 20  |
|  6840 K3 | File Information | O | 3  |
|  LOOP ID - 2650 |   |   | >1  |
|  6850 AIN | Income | O | 1  |
|  6860 QTY | Quantity Information | O | >1  |
|  6870 DTP | Date or Time or Period | O | >1  |

28

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834

|  6880 | LS | Loop Header | O | 1  |
| --- | --- | --- | --- | --- |
|   |  | LOOP ID - 2700 |  | >1  |
|  6881 | LX | Transaction Set Line Number | O | 1  |
|   |  | LOOP ID - 2750 |  | >1  |
|  6882 | N1 | Party Identification | M | 1  |
|  6883 | REF | Reference Information | M | 1  |
|  6884 | DTP | Date or Time or Period | O | 1  |
|  6885 | LE | Loop Trailer | O | 1  |
|  6900 | SE | Transaction Set Trailer | M | 1  |

NOTES:

1/0500 The AMT segment is used to record the total Flexible Spending Account contributions in the transaction set.

1/0600 The QTY segment is used to record the total number of subscribers and dependents in the transaction set.

1/0700 At least one iteration of loop 1000 is required to identify the sender or receiver.

2/0100 A Subscriber is a person who elects the benefits and is affiliated with the employer or the insurer. A Dependent is a person who is affiliated with the subscriber, such as a spouse, child, etc., and is therefore entitled to benefits. Subscriber information must come before dependent information. The INS segment is used to note if information being submitted is subscriber information or dependent information.

2/0200 The REF segment is required to link the dependent(s) to the subscriber.

2/3100 Loop 2310 contains information about the primary care providers for the subscriber or the dependent, and about the beneficiaries of any employer-sponsored life insurance for the subscriber.

2/3200 Either NM1 or N1 will be included depending on whether an individual or organization is being specified.

2/5500 Loop 2500 may only appear for the Subscriber.

FEBRUARY 2011
29

005010X220 &amp; 005010X220A1 • 834
CONSOLIDATED • 834

## 2.4 834 Segment Detail

This section specifies the segments, data elements, and codes for this implementation. Refer to section 2.1 Presentation Examples for detailed information on the components of the Segment Detail section.

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • ST
TRANSACTION SET HEADER

## SEGMENT DETAIL

### ST - TRANSACTION SET HEADER

X12 Segment Name: Transaction Set Header

X12 Purpose: To indicate the start of a transaction set and to assign a control number

Segment Repeat: 1

Usage: REQUIRED

TR3 Example: ST*834*0001*005010X220A1~

## DIAGRAM

### ST *

|  ST01 | 143  |
| --- | --- |
|  TS ID
Code  |   |
|  M 1 | ID 3/3  |

* ST02 329
TS Control Number
M 1 AN 4/9

* ST03 1705
Imple Conv Reference
O 1 AN 1/35

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | ST01 | 143 | Transaction Set Identifier Code
Code uniquely identifying a Transaction Set | M 1 ID 3/3  |
|   |  |  | SEMANTIC: The transaction set identifier (ST01) is used by the translation routines of the interchange partners to select the appropriate transaction set definition (e.g., 810 selects the Invoice Transaction Set). |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 834 Benefit Enrollment and Maintenance |   |
|  REQUIRED | ST02 | 329 | Transaction Set Control Number
Identifying control number that must be unique within the transaction set functional group assigned by the originator for a transaction set | M 1 AN 4/9  |
|   |  |  | The Transaction Set Control Number in ST02 and SE02 must be identical. The number must be unique within a specific interchange (ISA-IEA), but can repeat in other interchanges. |   |
|  REQUIRED | ST03 | 1705 | Implementation Convention Reference
Reference assigned to identify Implementation Convention | O 1 AN 1/35  |
|   |  |  | SEMANTIC: The implementation convention reference (ST03) is used by the translation routines of the interchange partners to select the appropriate implementation convention to match the transaction set definition. When used, this implementation convention reference takes precedence over the implementation reference specified in the GS08. |   |
|   |  |  | This element must be populated with the guide identifier named in Section 1.2. |   |
|   |  |  | This field contains the same value as GS08. Some translator products strip off the ISA and GS segments prior to application (STSE) processing. Providing the information from the GS08 at this level will ensure that the appropriate application mapping is utilized at translation time. |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • BGN
BEGINNING SEGMENT
CONSOLIDATED • 834

# SEGMENT DETAIL

# BGN - BEGINNING SEGMENT

X12 Segment Name: Beginning Segment
X12 Purpose: To indicate the beginning of a transaction set
X12 Syntax: 1. C0504
If BGN05 is present, then BGN04 is required.

Segment Repeat: 1

Usage: REQUIRED

TR3 Example: BGN*00*11227*19970920*1200*ES***2~

# DIAGRAM

BGN
BGN01 353
TS Purpose Code
M 1 ID 2/2
BGN02 127
Reference Ident
M 1 AN 1/50
BGN03 373
Date
M 1 DT 8/8
BGN04 337
Time
X 1 TM 4/8
BGN05 623
Time Code
O 1 ID 2/2
BGN06 127
Reference Ident
O 1 AN 1/50

BGN07 640
Transaction Type-Code
O 1 ID 2/2
BGN08 306
Action Code
O 1 ID 1/2
BGN09 786
Security Level-Code
O 1 ID 2/2

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | BGN01 | 353 | Transaction Set Purpose Code
Code identifying purpose of transaction set | M 1 ID 2/2  |
|   |  |  | CODE | DEFINITION  |
|   |  |  | 00 | Original  |
|   |  |  |  | If the original transaction has already been processed, an incoming transaction using this code may be rejected by the receiver. The rejection will be identified to the sender by telephone or other direct contact.  |
|   |  |  |  | The “00” indicates the first time the transaction is sent.  |
|   |  |  | 15 | Re-Submission  |
|   |  |  |  | Send the “15” when the original transmission was incorrect, has yet to be processed by the receiver, and a new corrected transmission is being sent. This transmission can then be pended by the receiver’s translator for further review.  |
|   |  |  | 22 | Information Copy  |
|   |  |  |  | Send the “22” when the original transmission was lost or not processed, and the sender is passing another transmission that is the same as the original.  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • BGN
BEGINNING SEGMENT

REQUIRED BGN02 127
Reference Identification M 1 AN 1/50
Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier
SEMANTIC: BGN02 is the transaction set reference number.
IMPLEMENTATION NAME: Transaction Set Reference Number
This element is the transaction set reference number assigned by the sender's application. It uniquely identifies this occurrence of the transaction for future reference.

REQUIRED BGN03 373
Date M 1 DT 8/8
Date expressed as CCYYMMDD where CC represents the first two digits of the calendar year
SEMANTIC: BGN03 is the transaction set date.
IMPLEMENTATION NAME: Transaction Set Creation Date
This element identifies the date that the submitter created the file.

REQUIRED BGN04 337
Time X 1 TM 4/8
Time expressed in 24-hour clock time as follows: HHMM, or HHMMSS, or HHMMSSD, or HHMMSSDD, where H = hours (00-23), M = minutes (00-59), S = integer seconds (00-59) and DD = decimal seconds; decimal seconds are expressed as follows: D = tenths (0-9) and DD = hundredths (00-99)
SYNTAX: C0504
SEMANTIC: BGN04 is the transaction set time.
IMPLEMENTATION NAME: Transaction Set Creation Time
This element is used as a time stamp to uniquely identify the transmission.

SITUATIONAL BGN05 623
Time Code O 1 ID 2/2
Code identifying the time. In accordance with International Standards Organization standard 8601, time can be specified by a + or - and an indication in hours in relation to Universal Time Coordinate (UTC) time; since + is a restricted character, + and - are substituted by P and M in the codes that follow
SYNTAX: C0504
SEMANTIC: BGN05 is the transaction set time qualifier.
SITUATIONAL RULE: Required when the sender and receiver are not in the same time zone. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Time Zone Code
CODE SOURCE 94: International Organization for Standardization (Date and Time)

|  CODE | DEFINITION  |
| --- | --- |
|  01 | Equivalent to ISO P01  |
|  02 | Equivalent to ISO P02  |
|  03 | Equivalent to ISO P03  |
|  04 | Equivalent to ISO P04  |
|  05 | Equivalent to ISO P05  |
|  06 | Equivalent to ISO P06  |
|  07 | Equivalent to ISO P07  |
|  08 | Equivalent to ISO P08  |
|  09 | Equivalent to ISO P09  |

FEBRUARY 2011
33

005010X220 &amp; 005010X220A1 • 834 • BGN
BEGINNING SEGMENT
CONSOLIDATED • 834

|  10 | Equivalent to ISO P10  |
| --- | --- |
|  11 | Equivalent to ISO P11  |
|  12 | Equivalent to ISO P12  |
|  13 | Equivalent to ISO M12  |
|  14 | Equivalent to ISO M11  |
|  15 | Equivalent to ISO M10  |
|  16 | Equivalent to ISO M09  |
|  17 | Equivalent to ISO M08  |
|  18 | Equivalent to ISO M07  |
|  19 | Equivalent to ISO M06  |
|  20 | Equivalent to ISO M05  |
|  21 | Equivalent to ISO M04  |
|  22 | Equivalent to ISO M03  |
|  23 | Equivalent to ISO M02  |
|  24 | Equivalent to ISO M01  |
|  AD | Alaska Daylight Time  |
|  AS | Alaska Standard Time  |
|  AT | Alaska Time  |
|  CD | Central Daylight Time  |
|  CS | Central Standard Time  |
|  CT | Central Time  |
|  ED | Eastern Daylight Time  |
|  ES | Eastern Standard Time  |
|  ET | Eastern Time  |
|  GM | Greenwich Mean Time  |
|  HD | Hawaii-Aleutian Daylight Time  |
|  HS | Hawaii-Aleutian Standard Time  |
|  HT | Hawaii-Aleutian Time  |
|  LT | Local Time  |
|  MD | Mountain Daylight Time  |
|  MS | Mountain Standard Time  |
|  MT | Mountain Time  |
|  ND | Newfoundland Daylight Time  |
|  NS | Newfoundland Standard Time  |
|  NT | Newfoundland Time  |
|  PD | Pacific Daylight Time  |
|  PS | Pacific Standard Time  |
|  PT | Pacific Time  |
|  TD | Atlantic Daylight Time  |
|  TS | Atlantic Standard Time  |
|  TT | Atlantic Time  |
|  UT | Universal Time Coordinate  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • BGN
BEGINNING SEGMENT

|  SITUATIONAL | BGN06 | 127 | Reference Identification
O 1 AN 1/50
Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier
SEMANTIC: BGN06 is the transaction set reference number of a previously sent transaction affected by the current transaction.
SITUATIONAL RULE: Required when there is a previously sent transaction to cross-reference. If not required by this implementation guide, do not send.  |
| --- | --- | --- | --- |
|  IMPLEMENTATION NAME: Original Transaction Set Reference Number  |   |   |   |
|  NOT USED | BGN07 | 640 | Transaction Type Code
O 1 ID 2/2  |
|  REQUIRED | BGN08 | 306 | Action Code
O 1 ID 1/2
Code indicating type of action  |
|   |  |  | CODE DEFINITION  |
|   |  |  | 2 Change (Update)  |
|   |  |  | Used to identify a transaction of additions, terminations and changes to the current enrollment.  |
|   |  |  | 4 Verify  |
|   |  |  | Used to identify a full enrollment transaction to verify that the sponsor's and payer's systems are synchronized.  |
|   |  |  | RX Replace  |
|   |  |  | Used to identify a full enrollment transmission to be used to identify additions, terminations and changes that need to be applied to the payer's enrollment system.  |
|  NOT USED | BGN09 | 786 | Security Level Code
O 1 ID 2/2  |

FEBRUARY 2011
35

005010X220 &amp; 005010X220A1 • 834 • REF
TRANSACTION SET POLICY NUMBER
CONSOLIDATED • 834

# SEGMENT DETAIL

## REF - TRANSACTION SET POLICY NUMBER

X12 Segment Name: Reference Information

X12 Purpose: To specify identifying information

X12 Syntax: 1. R0203
At least one of REF02 or REF03 is required.

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the insurance contract or trading partner agreement identifies a Master Policy Number for use with electronic enrollment. If not required may be provided at the sender’s discretion if a unique ID Number for a group applies to the entire transaction set.

TR3 Notes: 1. The definition of the Master Policy Number is determined by the issuer of the policy, the Payer/Plan Administrator. The Master Policy Number may be used to meet various business needs such as indicating the line of business under which the policy is defined.

TR3 Example: REF*38*123456~

# DIAGRAM

REF * REF01 128
Reference Ident Qual
M 1 ID 2/3 * REF02 127
Reference Ident
X 1 AN 1/50 * REF03 352
Description
X 1 AN 1/80 * REF04 C040
Reference Identifier
O 1

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | REF01 | 128 | Reference Identification Qualifier
Code qualifying the Reference Identification | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 38 Master Policy Number |   |
|  REQUIRED | REF02 | 127 | Reference Identification
X 1 AN 1/50
Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier
SYNTAX: R0203 |   |
|   |  |  | IMPLEMENTATION NAME: Master Policy Number |   |
|  NOT USED | REF03 | 352 | Description | X 1 AN 1/80  |
|  NOT USED | REF04 | C040 | REFERENCE IDENTIFIER | O 1  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • DTP
FILE EFFECTIVE DATE

## SEGMENT DETAIL

**DTP - FILE EFFECTIVE DATE**

X12 Segment Name: Date or Time or Period
X12 Purpose: To specify any or all of a date, a time, or a time period
Segment Repeat: &gt;1
Usage: SITUATIONAL
Situational Rule: Required when specified in the contract. If not required by this implementation guide, do not send.
TR3 Example: DTP®007®D8®19961001~

## DIAGRAM

**DTP** *

DTP01 374
Date/Time Qualifier
M 1 ID 3/3

DTP02 1250
Date Time Format Qual
M 1 ID 2/3

DTP03 1251
Date Time Period
M 1 AN 1/35

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | DTP01 | 374 | Date/Time Qualifier
Code specifying type of date or time, or both date and time | M 1 ID 3/3  |
|   |  |  | IMPLEMENTATION NAME: Date Time Qualifier |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 007 Effective |   |
|   |  |  | 090 Report Start |   |
|   |  |  | 091 Report End |   |
|   |  |  | 303 Maintenance Effective |   |
|   |  |  | 382 Enrollment |   |
|   |  |  | 388 Payment Commencement |   |
|  REQUIRED | DTP02 | 1250 | Date Time Period Format Qualifier
Code indicating the date format, time format, or date and time format | M 1 ID 2/3  |
|   |  |  | SEMANTIC: DTP02 is the date or time or period format that will appear in DTP03. |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | D8 Date Expressed in Format CCYYMMDD |   |
|  REQUIRED | DTP03 | 1251 | Date Time Period
Expression of a date, a time, or range of dates, times or dates and times | M 1 AN 1/35  |

FEBRUARY 2011
37

005010X220 &amp; 005010X220A1 • 834 • QTY
TRANSACTION SET CONTROL TOTALS
CONSOLIDATED • 834

## SEGMENT DETAIL

### QTY - TRANSACTION SET CONTROL TOTALS

**X12 Segment Name:** Quantity Information

**X12 Purpose:** To specify quantity information

**X12 Set Notes:** 1. The QTY segment is used to record the total number of subscribers and dependents in the transaction set.

**X12 Syntax:**
1. R0204
At least one of QTY02 or QTY04 is required.
2. E0204
Only one of QTY02 or QTY04 may be present.

**Segment Repeat:** 3

**Usage:** SITUATIONAL

**Situational Rule:** Required when the contract or trading partner agreement specifies that this information be included in the transaction set. If not required by this implementation guide, do not send.

**TR3 Example:** QTY*TO*10000~

## DIAGRAM

![img-3.jpeg](img-3.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | QTY01 | 673 | Quantity Qualifier
Code specifying the type of quantity |   |   | M 1 | ID | 2/2  |
|   |  |  | CODE | DEFINITION |  |  |  |   |
|   |  |  | DT | Dependent Total |  |  |  |   |
|   |  |  | ET | Employee Total |  |  |  |   |
|   |  |  | TO | Total |  |  |  |   |
|  REQUIRED | QTY02 | 380 | Quantity
Numeric value of quantity |   |   | X 1 | R | 1/15  |
|   |  |  | SYNTAX: R0204, E0204 |   |   |  |  |   |
|   |  |  | IMPLEMENTATION NAME: Record Totals |   |   |  |  |   |
|  NOT USED | QTY03 | C001 | COMPOSITE UNIT OF MEASURE |   |   | O 1 |  |   |
|  NOT USED | QTY04 | 61 | Free-form Information |   |   | X 1 | AN | 1/30  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 1000A • N1
SPONSOR NAME

## SEGMENT DETAIL

### N1 - SPONSOR NAME

X12 Segment Name: Party Identification

X12 Purpose: To identify a party by type of organization, name, and code

X12 Set Notes: 1. At least one iteration of loop 1000 is required to identify the sender or receiver.

X12 Syntax: 1. R0203
At least one of N102 or N103 is required.
2. P0304
If either N103 or N104 is present, then the other is required.

Loop: 1000A — SPONSOR NAME  Loop Repeat: 1

Segment Repeat: 1

Usage: REQUIRED

TR3 Notes: 1. This loop identifies the sponsor. See section 1.5 for the definition of Sponsor.

TR3 Example: N1*P5**FI*12356799~

## DIAGRAM

![img-4.jpeg](img-4.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | N101 | 98 | Entity Identifier Code |   |   | M 1 | ID | 2/3  |
|   |  |  | Code identifying an organizational entity, a physical location, property or an individual |   |   |  |  |   |
|   |  |  | CODE | DEFINITION |   |  |  |   |
|   |  |  | P5 | Plan Sponsor |   |  |  |   |
|  SITUATIONAL | N102 | 93 | Name |  |  | X 1 | AN | 1/60  |
|   |  |  | Free-form name |  |  |  |  |   |
|   |  |  | SYNTAX: R0203 |  |  |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when the receiver needs the sponsor name. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|   |  |  | IMPLEMENTATION NAME: Plan Sponsor Name  |   |   |   |   |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 1000A • N1
SPONSOR NAME
CONSOLIDATED • 834

|  REQUIRED | N103 | 66 | Identification Code Qualifier | X 1 ID | 1/2  |
| --- | --- | --- | --- | --- | --- |
|   |  |  | Code designating the system/method of code structure used for Identification Code (67)  |   |   |
|   |  |  | SYNTAX: R0203, P0304  |   |   |
|   |  |  | CODE | DEFINITION  |   |
|   |  |  | 24 | Employer's Identification Number  |   |
|   |  |  |  | The identifier is the Employer Identification Number (EIN) issued by the IRS. The EIN has been adopted as the HIPAA Standard Unique Employer Identifier.  |   |
|   |  |  | 94 | Code assigned by the organization that is the ultimate destination of the transaction set  |   |
|   |  |  | FI | Federal Taxpayer's Identification Number  |   |
|  REQUIRED | N104 | 67 | Identification Code | X 1 AN | 2/80  |
|   |  |  | Code identifying a party or other code  |   |   |
|   |  |  | SYNTAX: P0304  |   |   |
|   |  |  | COMMENT: This segment, used alone, provides the most efficient method of providing organizational identification. To obtain this efficiency the "ID Code" (N104) must provide a key to the table maintained by the transaction processing party.  |   |   |
|   |  |  | IMPLEMENTATION NAME: Sponsor Identifier  |   |   |
|  NOT USED | N105 | 706 | Entity Relationship Code | O 1 ID | 2/2  |
|  NOT USED | N106 | 98 | Entity Identifier Code | O 1 ID | 2/3  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 1000B • N1
PAYER

## SEGMENT DETAIL

### N1 - PAYER

**X12 Segment Name:** Party Identification

**X12 Purpose:** To identify a party by type of organization, name, and code

**X12 Set Notes:** 1. At least one iteration of loop 1000 is required to identify the sender or receiver.

**X12 Syntax:** 1. R0203
At least one of N102 or N103 is required.
2. P0304
If either N103 or N104 is present, then the other is required.

**Loop:** 1000B — PAYER
**Loop Repeat:** 1

**Segment Repeat:** 1

**Usage:** REQUIRED

**TR3 Notes:** 1. This loop identifies the payer. See section 1.5 for the definition of payer.

**TR3 Example:** N1*IN**FI*12356799-

## DIAGRAM

|  N1 * | N101 98
Entity ID Code
M 1 ID 2/3 | * | N102 93
Name
X 1 AN 1/60 | * | N103 66
ID Code
Qualifier
X 1 ID 1/2 | * | N104 67
ID Code
X 1 AN 2/80 | * | N105 706
Entity
Relat Code
O 1 ID 2/2 | * | N106 98
Entity ID Code
O 1 ID 2/3  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N101 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | IN Insurer |   |
|  SITUATIONAL | N102 | 93 | Name
Free-form name | X 1 AN 1/60  |
|   |  |  | SYNTAX: R0203 |   |
|   |  |  | SITUATIONAL RULE: Required when the receiver needs the payer name. If not required by this implementation guide, do not send. |   |
|   |  |  | IMPLEMENTATION NAME: Insurer Name |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 1000B • N1
PAYER
CONSOLIDATED • 834

|  REQUIRED | N103 | 66 | Identification Code Qualifier | X 1 ID | 1/2  |
| --- | --- | --- | --- | --- | --- |
|   |  |  | Code designating the system/method of code structure used for Identification Code (67)  |   |   |
|   |  |  | SYNTAX: R0203, P0304  |   |   |
|   |  |  | CODE | DEFINITION  |   |
|   |  |  | 94 | Code assigned by the organization that is the ultimate destination of the transaction set  |   |
|   |  |  | FI | Federal Taxpayer's Identification Number  |   |
|   |  |  | XV | Centers for Medicare and Medicaid Services PlanID  |   |
|   |  |  |  | Use when reporting Health Plan ID (HPID) or Other Entity Identifier (OEID).  |   |
|   |  |  |  | CODE SOURCE 540: Centers for Medicare and Medicaid Services PlanID  |   |
|  REQUIRED | N104 | 67 | Identification Code | X 1 AN | 2/80  |
|   |  |  | Code identifying a party or other code  |   |   |
|   |  |  | SYNTAX: P0304  |   |   |
|   |  |  | COMMENT: This segment, used alone, provides the most efficient method of providing organizational identification. To obtain this efficiency the "ID Code" (N104) must provide a key to the table maintained by the transaction processing party.  |   |   |
|   |  |  | IMPLEMENTATION NAME: Insurer Identification Code  |   |   |
|  NOT USED | N105 | 706 | Entity Relationship Code | O 1 ID | 2/2  |
|  NOT USED | N106 | 98 | Entity Identifier Code | O 1 ID | 2/3  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 1000C • N1
TPA/BROKER NAME

## SEGMENT DETAIL

### N1 - TPA/BROKER NAME

X12 Segment Name: Party Identification

X12 Purpose: To identify a party by type of organization, name, and code

X12 Set Notes: 1. At least one iteration of loop 1000 is required to identify the sender or receiver.

X12 Syntax: 1. R0203
At least one of N102 or N103 is required.
2. P0304
If either N103 or N104 is present, then the other is required.

Loop: 1000C — TPA/BROKER NAME  Loop Repeat: 2

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when a TPA or a Broker is involved in this enrollment. See section 1.5 for definitions. If not required by this implementation guide, do not send.

TR3 Example: N1*TV*MONEY TALKS BROKERAGE*FI*123356799~

## DIAGRAM

|  N1 * | N101 98
Entity ID
Code
M 1 ID 2/3 | * | N102 93
Name
X 1 AN 1/60 | * | N103 66
ID Code
Qualifier
X 1 ID 1/2 | * | N104 67
ID Code
X 1 AN 2/80 | * | N105 706
Entity
Relat Code
O 1 ID 2/2 | * | N106 98
Entity ID
Code
O 1 ID 2/3  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | N101 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual |   |   | M 1 | ID | 2/3  |
|   |  |  | CODE | DEFINITION |   |  |  |   |
|   |  |  | BO | Broker or Sales Office |   |  |  |   |
|   |  |  | TV | Third Party Administrator (TPA) |   |  |  |   |
|  REQUIRED | N102 | 93 | Name
Free-form name |   |   | X 1 | AN | 1/60  |
|   |  |  | SYNTAX: R0203 |   |   |  |  |   |
|   |  |  | IMPLEMENTATION NAME: TPA or Broker Name |   |   |  |  |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 1000C • N1
TPA/BROKER NAME
CONSOLIDATED • 834

|  REQUIRED | N103 | 66 | Identification Code Qualifier | X 1 ID | 1/2  |
| --- | --- | --- | --- | --- | --- |
|   |  |  | Code designating the system/method of code structure used for Identification Code (67)  |   |   |
|   |  |  | SYNTAX: R0203, P0304  |   |   |
|   |  |  | CODE | DEFINITION  |   |
|   |  |  | 94 | Code assigned by the organization that is the ultimate destination of the transaction set  |   |
|   |  |  | FI | Federal Taxpayer's Identification Number  |   |
|   |  |  | XV | Centers for Medicare and Medicaid Services PlanID  |   |
|   |  |  |  | Use when reporting Health Plan ID (HPID) or Other Entity Identifier (OEID).  |   |
|   |  |  |  | CODE SOURCE 540: Centers for Medicare and Medicaid Services PlanID  |   |
|  REQUIRED | N104 | 67 | Identification Code | X 1 AN | 2/80  |
|   |  |  | Code identifying a party or other code  |   |   |
|   |  |  | SYNTAX: P0304  |   |   |
|   |  |  | COMMENT: This segment, used alone, provides the most efficient method of providing organizational identification. To obtain this efficiency the "ID Code" (N104) must provide a key to the table maintained by the transaction processing party.  |   |   |
|   |  |  | IMPLEMENTATION NAME: TPA or Broker Identification Code  |   |   |
|  NOT USED | N105 | 706 | Entity Relationship Code | O 1 ID | 2/2  |
|  NOT USED | N106 | 98 | Entity Identifier Code | O 1 ID | 2/3  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 1100C • ACT
TPA/BROKER ACCOUNT INFORMATION

## SEGMENT DETAIL

### ACT - TPA/BROKER ACCOUNT INFORMATION

X12 Segment Name: Account Identification

X12 Purpose: To specify account information

X12 Syntax:
1. P0304
If either ACT03 or ACT04 is present, then the other is required.
2. C0506
If ACT05 is present, then ACT06 is required.
3. C0705
If ACT07 is present, then ACT05 is required.

Loop: 1100C — TPA/BROKER ACCOUNT INFORMATION  Loop Repeat: 1

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the account number of the TPA or Broker is different than the account number for the sponsor. If not required by this implementation guide, do not send.

TR3 Example: ACT*1234***23498765~

## DIAGRAM

|  ACT | ACT01 508
Account Number
M 1 AN 1/35 | ACT02 93
Name
O 1 AN 1/60 | ACT03 66
ID Code
Qualifier
X 1 ID 1/2 | ACT04 67
ID Code
X 1 AN 2/80 | ACT05 569
Acct Number
Qualifier
X 1 ID 1/3 | ACT06 508
Account Number
X 1 AN 1/35  |
| --- | --- | --- | --- | --- | --- | --- |
|   | ACT07 352
Description
O 1 AN 1/80 | ACT08 107
Payment
Method Code
O 1 ID 1/2 | ACT09 1216
Benefit
Status Code
O 1 ID 1/1 |  |  |   |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | ACT01 | 508 | Account Number | M 1 | AN | 1/35  |
|   |  |  | Account number assigned |  |  |   |
|   |  |  | IMPLEMENTATION NAME: TPA or Broker Account Number  |   |   |   |
|  NOT USED | ACT02 | 93 | Name | O 1 | AN | 1/60  |
|  NOT USED | ACT03 | 66 | Identification Code Qualifier | X 1 | ID | 1/2  |
|  NOT USED | ACT04 | 67 | Identification Code | X 1 | AN | 2/80  |
|  NOT USED | ACT05 | 569 | Account Number Qualifier | X 1 | ID | 1/3  |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 1100C • ACT
TPA/BROKER ACCOUNT INFORMATION
CONSOLIDATED • 834

|  SITUATIONAL | ACT06 | 508 | Account Number | X 1 | AN | 1/35  |
| --- | --- | --- | --- | --- | --- | --- |
|   |  |  | Account number assigned |  |  |   |
|   |  |  | SYNTAX: C0506 |  |  |   |
|   |  |  | COMMENT: ACT06 is an account associated with the account in ACT01. |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when more than 1 TPA or Broker Account Number applies to this transaction. If not required by this implementation guide, do not send. |  |  |   |
|   |  |  | IMPLEMENTATION NAME: TPA or Broker Account Number |  |  |   |
|  NOT USED | ACT07 | 352 | Description | O 1 | AN | 1/80  |
|  NOT USED | ACT08 | 107 | Payment Method Type Code | O 1 | ID | 1/2  |
|  NOT USED | ACT09 | 1216 | Benefit Status Code | O 1 | ID | 1/1  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2000 • INS
MEMBER LEVEL DETAIL

# SEGMENT DETAIL

## INS - MEMBER LEVEL DETAIL

X12 Segment Name: Insured Benefit

X12 Purpose: To provide benefit information on insured entities

X12 Set Notes: 1. A Subscriber is a person who elects the benefits and is affiliated with the employer or the insurer. A Dependent is a person who is affiliated with the subscriber, such as a spouse, child, etc., and is therefore entitled to benefits. Subscriber information must come before dependent information. The INS segment is used to note if information being submitted is subscriber information or dependent information.

X12 Syntax: 1. P1112
If either INS11 or INS12 is present, then the other is required.

Loop: 2000 — MEMBER LEVEL DETAIL Loop Repeat: &gt;1

Segment Repeat: 1

Usage: REQUIRED

TR3 Notes: 1. Subscriber information must precede dependent information in a transmission, or the subscriber information must have been submitted to the receiver in a previous transmission.

TR3 Example: INS*Y*18*021*28*A***FT~

# DIAGRAM

![img-5.jpeg](img-5.jpeg)

FEBRUARY 2011
47

005010X220 &amp; 005010X220A1 • 834 • 2000 • INS MEMBER LEVEL DETAIL

CONSOLIDATED • 834

ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | INS01 | 1073 | Yes/No Condition or Response Code
Code indicating a Yes or No condition or response |   |   | M 1 | ID 1/1  |
|   |  |  | SEMANTIC: INS01 indicates status of the insured. A “Y” value indicates the insured is a subscriber: an “N” value indicates the insured is a dependent.  |   |   |   |   |
|   |  |  | IMPLEMENTATION NAME: Member Indicator  |   |   |   |   |
|   |  |  | ALIAS: Subscriber Indicator  |   |   |   |   |
|   |  |  | CODE | DEFINITION  |   |   |   |
|   |  |  | N | No  |   |   |   |
|   |  |  | Y | Yes  |   |   |   |
|  REQUIRED | INS02 | 1069 | Individual Relationship Code
Code indicating the relationship between two individuals or entities |   |   | M 1 | ID 2/2  |
|   |  |  | The value 18 must be used for the subscriber.  |   |   |   |   |
|   |  |  | For dependents, this value identifies their relationship to the subscriber. For example, a daughter would be value 19.  |   |   |   |   |
|   |  |  | CODE | DEFINITION  |   |   |   |
|   |  |  | 01 | Spouse  |   |   |   |
|   |  |  | 03 | Father or Mother  |   |   |   |
|   |  |  | 04 | Grandfather or Grandmother  |   |   |   |
|   |  |  | 05 | Grandson or Granddaughter  |   |   |   |
|   |  |  | 06 | Uncle or Aunt  |   |   |   |
|   |  |  | 07 | Nephew or Niece  |   |   |   |
|   |  |  | 08 | Cousin  |   |   |   |
|   |  |  | 09 | Adopted Child  |   |   |   |
|   |  |  | 10 | Foster Child  |   |   |   |
|   |  |  | 11 | Son-in-law or Daughter-in-law  |   |   |   |
|   |  |  | 12 | Brother-in-law or Sister-in-law  |   |   |   |
|   |  |  | 13 | Mother-in-law or Father-in-law  |   |   |   |
|   |  |  | 14 | Brother or Sister  |   |   |   |
|   |  |  | 15 | Ward  |   |   |   |
|   |  |  | 16 | Stepparent  |   |   |   |
|   |  |  | 17 | Stepson or Stepdaughter  |   |   |   |
|   |  |  | 18 | Self  |   |   |   |
|   |  |  | 19 | Child  |   |   |   |
|   |  |  | 23 | Sponsored Dependent  |   |   |   |
|   |  |  |  | Dependents between the ages of 19 and 25 not attending school; age qualifications may vary depending on policy.  |   |   |   |
|   |  |  | 24 | Dependent of a Minor Dependent  |   |   |   |
|   |  |  | 25 | Ex-spouse  |   |   |   |
|   |  |  | 26 | Guardian  |   |   |   |
|   |  |  | 31 | Court Appointed Guardian  |   |   |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2000 • INS
MEMBER LEVEL DETAIL

|  REQUIRED | INS03 | 875 | 38 | Collateral Dependent  |
| --- | --- | --- | --- | --- |
|   |   |   |   | Relative related by blood or marriage who resides in the home and is dependent on the insured for a major portion of their support.  |
|   |   |   |  53 | Life Partner  |
|   |   |   |   | This is a partner that acts like a spouse without a legal marriage commitment.  |
|   |   |   |  60 | Annuitant  |
|   |   |   |  D2 | Trustee  |
|   |   |   |  G8 | Other Relationship  |
|   |   |   |  G9 | Other Relative  |
|  SITUATIONAL | INS04 | 1203 | Maintenance Type Code
Code identifying the specific type of item maintenance | O 1 ID 3/3  |
|   |   |   |  CODE | DEFINITION  |
|   |   |   |  001 | Change  |
|   |   |   |   | Use this code to indicate a change to an existing subscriber/dependent record.  |
|   |   |   |  021 | Addition  |
|   |   |   |   | Use this code to add a subscriber or dependent.  |
|   |   |   |  024 | Cancellation or Termination  |
|   |   |   |   | Use this code for cancellation, termination, or deletion of a subscriber or dependent.  |
|   |   |   |  025 | Reinstatement  |
|   |   |   |   | Use this code for reinstatement of a cancelled subscriber/dependent record.  |
|   |   |   |  030 | Audit or Compare  |
|   |   |   |   | Use this code when sending a full file (BGN08 = ‘4’ or ‘RX’) to verify that the sponsor and payer databases are synchronized. See section 1.4.5, Update, Versus Full File Audits, Versus Full File Replacements, for additional information.  |
|   |   |   |  Maintenance Reason Code
Code identifying the reason for the maintenance change | O 1 ID 2/3  |
|  SITUATIONAL RULE: Required when the payer needs to know the reason for the change. If not required by this implementation guide, do not send.  |   |   |   |   |
|  CODE | DEFINITION  |   |   |   |

FEBRUARY 2011
49

005010X220 &amp; 005010X220A1 • 834 • 2000 • INS MEMBER LEVEL DETAIL
CONSOLIDATED • 834

|  10 | Consolidation Omnibus Budget Reconciliation Act (COBRA) Premium Paid  |
| --- | --- |
|  11 | Surviving Spouse  |
|  14 | Voluntary Withdrawal  |
|  15 | Primary Care Provider (PCP) Change  |
|  16 | Quit  |
|  17 | Fired  |
|  18 | Suspended  |
|  20 | Active  |
|  21 | Disability  |
|  22 | Plan Change  |
|   | Use this code when a member changes from one Plan to a different Plan. This is not intended to identify changes to a Plan.  |
|  25 | Change in Identifying Data Elements  |
|   | Use this code when a change has been made to the primary elements that identify a member. Such primary elements include the following: first name, last name, Social Security Number, date of birth, and employee identification number.  |
|  26 | Declined Coverage  |
|   | Use this code when a member declined a previously active coverage.  |
|  27 | Pre-Enrollment  |
|   | Use this code to enroll newborns prior to receiving the newborn's application.  |
|  28 | Initial Enrollment  |
|   | Use this code the first time the member selected coverage with the Plan Sponsor.  |
|  29 | Benefit Selection  |
|   | Use this code when a member changes benefits within a Plan.  |
|  31 | Legal Separation  |
|  32 | Marriage  |
|  33 | Personnel Data  |
|   | Use this code for any data change that is not included in any of the other allowed codes. An example would be change in Coordination of Benefits information.  |
|  37 | Leave of Absence with Benefits  |
|  38 | Leave of Absence without Benefits  |
|  39 | Lay Off with Benefits  |
|  40 | Lay Off without Benefits  |
|  41 | Re-enrollment  |
|  43 | Change of Location  |
|   | Use this code to indicate a change of address.  |
|  59 | Non Payment  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2000 • INS
MEMBER LEVEL DETAIL

|  REQUIRED | INS05 | 1216 | AA | Dissatisfaction with Office Staff  |
| --- | --- | --- | --- | --- |
|   |   |   |  AB | Dissatisfaction with Medical Care/Services Rendered  |
|   |   |   |  AC | Inconvenient Office Location  |
|   |   |   |  AD | Dissatisfaction with Office Hours  |
|   |   |   |  AE | Unable to Schedule Appointments in a Timely Manner  |
|   |   |   |  AF | Dissatisfaction with Physician’s Referral Policy  |
|   |   |   |  AG | Less Respect and Attention Time Given than to Other Patients  |
|   |   |   |  AH | Patient Moved to a New Location  |
|   |   |   |  AI | No Reason Given  |
|   |   |   |  AJ | Appointment Times not Met in a Timely Manner  |
|   |   |   |  AL | Algorithm Assigned Benefit Selection  |
|  EC | Member Benefit Selection  |   |   |   |
|  SITUATIONAL | INS06 | C052 | AB | Dissatisfaction with Medical Care/Services Rendered  |
|   |   |   |  AC | Inconvenient Office Location  |
|   |   |   |  AD | Dissatisfaction with Office Hours  |
|   |   |   |  AE | Unable to Schedule Appointments in a Timely Manner  |
|  REQUIRED | INS05 | 1216 | AD | Dissatisfaction with Physician’s Referral Policy  |
|   |   |   |  AE | Less Respect and Attention Time Given than to Other Patients  |
|   |   |   |  AH | Patient Moved to a New Location  |
|   |   |   |  AI | No Reason Given  |

FEBRUARY 2011
51

005010X220 &amp; 005010X220A1 • 834 • 2000 • INS MEMBER LEVEL DETAIL

CONSOLIDATED • 834

SITUATIONAL INS06 - 2 1701 Eligibility Reason Code O ID 1/1
Code specifying reason for eligibility
SITUATIONAL RULE: Required if the reason for Medicare is provided to the sponsor by the member. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Medicare Eligibility Reason Code

|  CODE | DEFINITION  |
| --- | --- |
|  0 | Age  |
|  1 | Disability  |
|  2 | End Stage Renal Disease (ESRD)  |
|  1701 | Eligibility Reason Code O ID 1/1  |
|  1701 | Eligibility Reason Code O ID 1/1  |

NOT USED INS06 - 3
NOT USED INS06 - 4
SITUATIONAL INS07 1219
Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying
A Qualifying Event is any of the following which results in loss of coverage for a Qualified Beneficiary

SITUATIONAL RULE: Required when a member is being enrolled in or is enrolled for a benefit covered by COBRA. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying Event Code

|  CODE | DEFINITION  |
| --- | --- |
|  1 | Termination of Employment  |
|  2 | Reduction of work hours  |
|  3 | Medicare  |
|  4 | Death  |
|  5 | Divorce  |
|  6 | Separation  |
|  7 | Ineligible Child  |
|  8 | Bankruptcy of Retiree’s Former Employer (26 U.S.C. 4980B(f)(3)(F))  |
|  9 | Layoff  |
|  10 | Leave of Absence  |
|  ZZ | Mutually Defined  |

SITUATIONAL INS08 584
Employment Status Code O 1 ID 2/2
Code showing the general employment status of an employee/claimant
SITUATIONAL RULE: Required for subscriber. If not required by this implementation guide, do not send.

If this insurance enrollment is through a non-employment based program such as Medicare or Medicaid then this data element will contain the status of the subscriber in that program, rather than their employment status. Codes for non-employment based programs will be limited to “AC”, Active and “TE”, Terminated.

|  CODE | DEFINITION  |
| --- | --- |
|  AC | Active  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2000 • INS
MEMBER LEVEL DETAIL

|   |  |  | AO | Active Military - Overseas |   |
| --- | --- | --- | --- | --- | --- |
|   |  |  | AU | Active Military - USA |   |
|   |  |  | FT | Full-time |   |
|   |  |  |  | Full time active employee |   |
|   |  |  | L1 | Leave of Absence |   |
|   |  |  | PT | Part-time |   |
|   |  |  |  | Part time Active Employee |   |
|   |  |  | RT | Retired |   |
|   |  |  | TE | Terminated |   |
|  SITUATIONAL | INS09 | 1220 | Student Status Code O 1 ID 1/1
Code indicating the student status of the patient if 19 years of age or older, not handicapped and not the insured |   |   |
|   |  |  | SITUATIONAL RULE: Required when describing a non-spouse dependent whose age requires a qualifying condition for enrollment (e.g., being an active student). See the Plan contract for details of the age requirements for student status usage. If not required by this implementation guide, do not send. |   |   |
|   |  |  | CODE | DEFINITION |   |
|   |  |  | F | Full-time |   |
|   |  |  | N | Not a Student |   |
|   |  |  | P | Part-time |   |
|  SITUATIONAL | INS10 | 1073 | Yes/No Condition or Response Code O 1 ID 1/1
Code indicating a Yes or No condition or response |   |   |
|   |  |  | SEMANTIC: INS10 is the handicapped status indicator. A "Y" value indicates an individual is handicapped; an "N" value indicates an individual is not handicapped. |   |   |
|   |  |  | SITUATIONAL RULE: Required when the member is handicapped or to correct a previous report of handicapped status. If not required by this implementation guide, do not send. |   |   |
|   |  |  | IMPLEMENTATION NAME: Handicap Indicator |   |   |
|   |  |  | CODE | DEFINITION |   |
|   |  |  | N | No |   |
|   |  |  | Y | Yes |   |
|  SITUATIONAL | INS11 | 1250 | Date Time Period Format Qualifier X 1 ID 2/3
Code indicating the date format, time format, or date and time format |   |   |
|   |  |  | SYNTAX: P1112 |   |   |
|   |  |  | SITUATIONAL RULE: Required when the Insured Individual Death Date is sent in INS12. If not required by this implementation guide, do not send. |   |   |
|   |  |  | CODE | DEFINITION |   |
|   |  |  | D8 | Date Expressed in Format CCYYMMDD |   |

FEBRUARY 2011
53

005010X220 &amp; 005010X220A1 • 834 • 2000 • INS
MEMBER LEVEL DETAIL
CONSOLIDATED • 834

SITUATIONAL INS12 1251
Date Time Period
X 1 AN 1/35
Expression of a date, a time, or range of dates, times or dates and times

SYNTAX: P1112

SEMANTIC: INS12 is the date of death.

SITUATIONAL RULE: Required if the subscriber/dependent is deceased. If not required by this implementation guide, do not send. This is the date of death for the subscriber/dependent and does not replace the use of the termination date within the 2300 loop.

IMPLEMENTATION NAME: Member Individual Death Date

SITUATIONAL INS13 1165
Confidentiality Code
O 1 ID 1/1
Code indicating the access to insured information

SITUATIONAL RULE: Required when the member has specified the access to their information. If not required by this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  R | Restricted Access  |
|  U | Unrestricted Access  |

NOT USED INS14 19
City Name
O 1 AN 2/30

NOT USED INS15 156
State or Province Code
O 1 ID 2/2

NOT USED INS16 26
Country Code
O 1 ID 2/3

SITUATIONAL INS17 1470
Number
O 1 N0 1/9
A generic number

SEMANTIC: INS17 is the number assigned to each family member born with the same birth date. This number identifies birth sequence for multiple births allowing proper tracking and response of benefits for each dependent (i.e., twins, triplets, etc.).

SITUATIONAL RULE: Required when reporting family members with the same birth date if a birth sequence number is needed for proper reporting, tracking or response to benefits. If not required by this implementation guide, do not send.

IMPLEMENTATION NAME: Birth Sequence Number

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2000 • REF
SUBSCRIBER IDENTIFIER

## SEGMENT DETAIL

### REF - SUBSCRIBER IDENTIFIER

X12 Segment Name: Reference Information

X12 Purpose: To specify identifying information

X12 Set Notes: 1. The REF segment is required to link the dependent(s) to the subscriber.

X12 Syntax: 1. R0203
At least one of REF02 or REF03 is required.

Loop: 2000 — MEMBER LEVEL DETAIL

Segment Repeat: 1

Usage: REQUIRED

TR3 Notes: 1. This segment must contain a unique SUBSCRIBER identification number (SSN or other). This occurrence is identified by the 0F qualifier (REF01). This identifier is used for linking the subscriber with dependents as required under many policies.

2. The developers recommend using the identifier developed under the HIPAA legislation, when that becomes available.

TR3 Example: REF*0F*920399398~

## DIAGRAM

REF
REF01 128
Reference Ident Qual
M 1 ID 2/3
REF02 127
Reference Ident
X 1 AN 1/50
REF03 352
Description
X 1 AN 1/80
REF04 C040
Reference Identifier
O 1

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | REF01 | 128 | Reference Identification Qualifier
Code qualifying the Reference Identification |   |   | M 1 | ID 2/3  |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | 0F | Subscriber Number |   |  |   |
|   |  |  |  | The assignment of the Subscriber Number is designated within the Insurance Contract. |   |  |   |
|  REQUIRED | REF02 | 127 | Reference Identification
Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier |   |   | X 1 | AN 1/50  |
|   |  |  | SYNTAX: R0203 |   |   |  |   |
|   |  |  | IMPLEMENTATION NAME: Subscriber Identifier |   |   |  |   |
|  NOT USED | REF03 | 352 | Description |   |   | X 1 | AN 1/80  |
|  NOT USED | REF04 | C040 | REFERENCE IDENTIFIER |   |   | O 1 |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 2000 • REF
MEMBER POLICY NUMBER
CONSOLIDATED • 834

# SEGMENT DETAIL

# REF - MEMBER POLICY NUMBER

X12 Segment Name: Reference Information

X12 Purpose: To specify identifying information

X12 Set Notes: 1. The REF segment is required to link the dependent(s) to the subscriber.

X12 Syntax: 1. R0203

At least one of REF02 or REF03 is required.

Loop: 2000 — MEMBER LEVEL DETAIL

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the policy or group number applies to all coverage data (all 2300 loops for this member). If not required by this implementation guide, do not send.

TR3 Notes: 1. The policy number passed in this segment is an attribute of the contract relationship between the plan sponsor (sender) and the payer (receiver) and not an attribute of an individual's participation in any coverage passed in an HD loop.

TR3 Example: REF*1L*9CC4123~

# DIAGRAM

![img-6.jpeg](img-6.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | REF01 | 128 | Reference Identification Qualifier
Code qualifying the Reference Identification | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 1L Group or Policy Number |   |
|   |  |  | The submitter sends the payer's pre-assigned Group or Policy Number. |   |
|  REQUIRED | REF02 | 127 | Reference Identification
X 1 AN 1/50
Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier | X 1 AN 1/50  |
|   |  |  | SYNTAX: R0203 |   |
|   |  |  | IMPLEMENTATION NAME: Member Group or Policy Number |   |
|  NOT USED | REF03 | 352 | Description | X 1 AN 1/80  |
|  NOT USED | REF04 | C040 | REFERENCE IDENTIFIER | O 1  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2000 • REF
MEMBER SUPPLEMENTAL IDENTIFIER

## SEGMENT DETAIL

**REF - MEMBER SUPPLEMENTAL IDENTIFIER**

X12 Segment Name: Reference Information

X12 Purpose: To specify identifying information

X12 Set Notes: 1. The REF segment is required to link the dependent(s) to the subscriber.

X12 Syntax: 1. R0203
At least one of REF02 or REF03 is required.

Loop: 2000 — MEMBER LEVEL DETAIL

Segment Repeat: 13

Usage: SITUATIONAL

Situational Rule: Required when sending additional identifying information on the member. If not required by this implementation guide, do not send.

TR3 Example: REF*17*920399398~

## DIAGRAM

**REF**

|  REF01 | 128 | Reference Ident Qual | M 1 | ID | 2/3  |
| --- | --- | --- | --- | --- | --- |
|  REF02 | 127 | Reference Ident | X 1 | AN | 1/50  |
|  REF03 | 352 | Description | X 1 | AN | 1/80  |
|  REF04 | C040 | Reference Identifier | O 1 | ~  |   |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | REF01 | 128 | Reference Identification Qualifier
Code qualifying the Reference Identification | M 1 ID 2/3  |
|  CODE | DEFINITION |  |  |   |
|  17 | Client Reporting Category |  |  |   |
|   | Used when further identification of a member is required under the insurance contract between the sponsor and the payer and allowed by federal and state regulations. |  |  |   |
|  23 | Client Number |  |  |   |
|   | To be used to pass a payer specific identifier for a member. Not to be used after the HIPAA standard National Identifier for Individuals is implemented. |  |  |   |
|  3H | Case Number |  |  |   |
|  4A | Personal Identification Number (PIN) |  |  |   |
|   | Use this code to transmit a password that is associated with the member’s record. |  |  |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 2000 • REF
MEMBER SUPPLEMENTAL IDENTIFIER
CONSOLIDATED • 834

|  6O | Cross Reference Number  |
| --- | --- |
|   | Used when further identification of a member is required for reporting, indexing, or other purpose as mutually agreed upon between the sender and receiver of the transaction set.  |
|  ABB | Personal ID Number  |
|  D3 | National Council for Prescription Drug Programs Pharmacy Number  |
|   | CODE SOURCE 307: National Council for Prescription Drug Programs Pharmacy Number  |
|  DX | Department/Agency Number  |
|   | Use when members in a coverage group are set up as different departments or divisions under the terms of the insurance policy.  |
|  F6 | Health Insurance Claim (HIC) Number  |
|   | Use when reporting Medicare eligibility for a member until the National Identifier is mandated for use.  |
|  P5 | Position Code  |
|   | Use this code to transmit the title of the member's employment position.  |
|  Q4 | Prior Identifier Number  |
|   | Use to pass the Identifier Number under which the member had previous coverage with the payer. This could be the result of a change in employment or coverage that resulted in a new ID number being assigned but left the member covered by the same payer.  |
|  QQ | Unit Number  |
|   | Use when members in a coverage group are set up as different units under the terms of the insurance policy. Units may exist within another grouping such as division or department.  |
|  ZZ | Mutually Defined  |

REQUIRED REF02 127
Reference Identification X 1 AN 1/50
Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier
SYNTAX: R0203
IMPLEMENTATION NAME: Member Supplemental Identifier

NOT USED REF03 352
Description X 1 AN 1/80
NOT USED REF04 C040
REFERENCE IDENTIFIER O 1

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2000 • DTP
MEMBER LEVEL DATES

## SEGMENT DETAIL

### DTP - MEMBER LEVEL DATES

X12 Segment Name: Date or Time or Period

X12 Purpose: To specify any or all of a date, a time, or a time period

Loop: 2000 — MEMBER LEVEL DETAIL

Segment Repeat: 24

Usage: SITUATIONAL

Situational Rule: Required when enrolling a member or when the sponsor is informed of a change to any applicable date listed in DTP01. Only those dates that apply to the particular insurance contract need to be sent. If not required by this implementation guide, do not send.

TR3 Notes: 1. While many of the dates listed for DTP01 are related to termination, the only code that is used to actually terminate a Member is 357 (Eligibility End). Similarly, the Eligibility Begin Date (code 356) is the date the individual is eligible for coverage, not the date coverage is effective.

TR3 Example: DTP*356*D8*19960705~

## DIAGRAM

DTP *

|  DTP01 | 374  |
| --- | --- |
|  Date/Time Qualifier  |   |
|  M 1 | ID 3/3  |
|  DTP02 | 1250  |
| --- | --- |
|  Date Time Format Qual  |   |
|  M 1 | ID 2/3  |
|  DTP03 | 1251  |
| --- | --- |
|  Date Time Period  |   |
|  M 1 | AN 1/35  |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | DTP01 | 374 | Date/Time Qualifier | M 1 ID 3/3  |
|   |  |  | Code specifying type of date or time, or both date and time |   |
|   |  |  | IMPLEMENTATION NAME: Date Time Qualifier |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 050 Received |   |
|   |  |  | Used to identify the date an enrollment application is received. |   |
|   |  |  | 286 Retirement |   |
|   |  |  | 296 Initial Disability Period Return To Work |   |
|   |  |  | 297 Initial Disability Period Last Day Worked |   |
|   |  |  | 300 Enrollment Signature Date |   |
|   |  |  | 301 Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying Event |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 2000 • DTP MEMBER LEVEL DATES

CONSOLIDATED • 834

|  303 | Maintenance Effective  |
| --- | --- |
|   | This code is used to send the effective date of a change to an existing member’s information, excluding changes made in Loop 2300.  |
|  336 | Employment Begin  |
|  337 | Employment End  |
|  338 | Medicare Begin  |
|  339 | Medicare End  |
|  340 | Consolidated Omnibus Budget Reconciliation Act (COBRA) Begin  |
|  341 | Consolidated Omnibus Budget Reconciliation Act (COBRA) End  |
|  350 | Education Begin  |
|   | This is the start date for the student at the current educational institution.  |
|  351 | Education End  |
|   | This is the expected graduation date the student at the current educational institution.  |
|  356 | Eligibility Begin  |
|   | The date when a member could elect to enroll or begin benefits in any health care plan through the employer. This is not the actual begin date of coverage, which is conveyed in the DTP segment at position 2700.  |
|  357 | Eligibility End  |
|   | The eligibility end date represents the last date of coverage for which claims will be paid for the individual being terminated. For example, if a date of 02/28/2001 is passed then claims for this individual will be paid through 11:59 p.m. on 02/28/2001.  |
|  383 | Adjusted Hire  |
|  385 | Credited Service Begin  |
|   | The start date from which an employee’s length of service, as defined in the plan document, will be calculated.  |
|  386 | Credited Service End  |
|   | The end date to be used in the calculation of an employee’s length of service, as defined in the plan document.  |
|  393 | Plan Participation Suspension  |
|  394 | Rehire  |
|  473 | Medicaid Begin  |
|  474 | Medicaid End  |

REQUIRED DTP02 1250
Date Time Period Format Qualifier M 1 ID 2/3
Code indicating the date format, time format, or date and time format

SEMANTIC: DTP02 is the date or time or period format that will appear in DTP03.

|  CODE | DEFINITION  |
| --- | --- |
|  D8 | Date Expressed in Format CCYYMMDD  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2000 • DTP
MEMBER LEVEL DATES

REQUIRED DTP03 1251 Date Time Period M 1 AN 1/35
Expression of a date, a time, or range of dates, times or dates and times
IMPLEMENTATION NAME: Status Information Effective Date

FEBRUARY 2011
61

005010X220 &amp; 005010X220A1 • 834 • 2100A • NM1
MEMBER NAME
CONSOLIDATED • 834

# SEGMENT DETAIL

# NM1 - MEMBER NAME

X12 Segment Name: Individual or Organizational Name

X12 Purpose: To supply the full name of an individual or organizational entity

X12 Syntax: 1. P0809
If either NM108 or NM109 is present, then the other is required.

2. C1110
If NM111 is present, then NM110 is required.

3. C1203
If NM112 is present, then NM103 is required.

Loop: 2100A — MEMBER NAME  Loop Repeat: 1

Segment Repeat: 1

Usage: REQUIRED

TR3 Example: NM1*IL*1*SMITH*JOHN*M**SR~

# DIAGRAM

# NM1

|  NM101 | 98 | NM102 | 1065 | NM103 | 1035 | NM104 | 1036 | NM105 | 1037 | NM106 | 1038  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Entity ID Code | M 1 | ID | 1/1 | Name Last/ Org Name | X 1 | AN | 1/60 | Name First | O 1 | AN | 1/25  |
|  X 1 | AN | 1/10 |  |  |  |  |  |  |  |  |   |
|  NM107 | 1039 | NM108 | 66 | NM109 | 67 | NM110 | 706 | NM111 | 98 | NM112 | 1035  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Name Suffix | O 1 | AN | 1/10 | ID Code Qualifier | X 1 | ID | 2/2 | Entity Relat Code | X 1 | ID | 2/3  |
|  X 1 | ID | 1/2 |  |  |  |  |  |  |  |  |   |

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | NM101 | 98 | Entity Identifier Code | M 1 ID 2/3  |
|   |  |  | Code identifying an organizational entity, a physical location, property or an individual |   |

This code identifies if this is a correction to a previous enrollment or if it is a new, or update, enrollment transaction.

|  CODE | DEFINITION  |
| --- | --- |
|  74 | Corrected Insured  |
|   | Use this code if this transmission is correcting the identifier information on a member already enrolled. Usage of this code requires the sending of an NM1 with code '70' in loop 2100B.  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • NM1
MEMBER NAME

|  REQUIRED | NM102 | 1065 | IL | Insured or Subscriber  |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |  Use this code for enrolling a new member or updating a member with no change in identifying information. The identifying information for a member is specified under the insurance contract between the sponsor and payer.  |   |   |
|  REQUIRED | NM103 | 1035 | Entity Type Qualifier |   | M 1 | ID 1/1  |
|   |   |   |  Code qualifying the type of entity
SEMANTIC: NM102 qualifies NM103.
CODE DEFINITION |   |  |   |
|  REQUIRED | NM104 | 1036 | 1 Person |   |  |   |
|   |   |   |  Name Last or Organization Name
Individual last name or organizational name
SYNTAX: C1203 |   | X 1 | AN 1/60  |
|  SITUATIONAL | NM104 | 1036 | IMPLEMENTATION NAME: Member Last Name |   |  |   |
|   |   |   |  Name First
Individual first name |   | O 1 | AN 1/35  |
|  SITUATIONAL | NM105 | 1037 | SITUATIONAL RULE: Required when NM102 is equal to “1” (person) and the person has a first name. If not required by this implementation guide, do not send. |   |  |   |
|   |   |   |  IMPLEMENTATION NAME: Member First Name |   |  |   |
|  SITUATIONAL | NM105 | 1037 | SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send. |   |  |   |
|   |   |   |  IMPLEMENTATION NAME: Member First Name |   |  |   |
|  SITUATIONAL | NM106 | 1038 | SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send. |   |  |   |
|   |   |   |  IMPLEMENTATION NAME: Member Middle Name |   |  |   |
|  SITUATIONAL | NM106 | 1038 | SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send. |   |  |   |
|   |   |   |  IMPLEMENTATION NAME: Member Name Prefix |   |  |   |
|  SITUATIONAL | NM107 | 1039 | SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send. |   |  |   |
|   |   |   |  IMPLEMENTATION NAME: Member Name Prefix |   |  |   |

FEBRUARY 2011
63

005010X220 &amp; 005010X220A1 • 834 • 2100A • NM1
MEMBER NAME
CONSOLIDATED • 834

|  SITUATIONAL | NM108 | 66 | Identification Code Qualifier | X 1 ID | 1/2  |
| --- | --- | --- | --- | --- | --- |
|   |  |  | Code designating the system/method of code structure used for Identification Code (67)  |   |   |
|   |  |  | SYNTAX: P0809  |   |   |
|   |  |  | SITUATIONAL RULE: Required when a value is being reported in the NM109 element. If not required by this implementation guide, do not send.  |   |   |
|   |  |  | CODE | DEFINITION  |   |
|   |  |  | 34 | Social Security Number  |   |
|   |  |  |  | The social security number may not be used for any Federally administered programs such as Medicare or CHAMPUS/TRICARE.  |   |
|   |  |  | ZZ | Mutually Defined  |   |
|   |  |  |  | Value is required if National Individual Identifier is mandated for use. Otherwise, one of the other listed codes may be used.  |   |
|  SITUATIONAL | NM109 | 67 | Identification Code | X 1 AN | 2/80  |
|   |  |  | Code identifying a party or other code  |   |   |
|   |  |  | SYNTAX: P0809  |   |   |
|   |  |  | SITUATIONAL RULE: Required when a Member Identifier is known and allowed under confidentiality regulations. If not required by this implementation guide, do not send.  |   |   |
|   |  |  | IMPLEMENTATION NAME: Member Identifier  |   |   |
|  NOT USED | NM110 | 706 | Entity Relationship Code | X 1 ID | 2/2  |
|  NOT USED | NM111 | 98 | Entity Identifier Code | O 1 ID | 2/3  |
|  NOT USED | NM112 | 1035 | Name Last or Organization Name | O 1 AN | 1/60  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • PER
MEMBER COMMUNICATIONS NUMBERS

# SEGMENT DETAIL

# PER - MEMBER COMMUNICATIONS NUMBERS

X12 Segment Name: Administrative Communications Contact

X12 Purpose: To identify a person or office to whom administrative communications should be directed

X12 Syntax:
1. P0304
If either PER03 or PER04 is present, then the other is required.
2. P0506
If either PER05 or PER06 is present, then the other is required.
3. P0708
If either PER07 or PER08 is present, then the other is required.

Loop: 2100A — MEMBER NAME

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when enrolling subscribers, dependents with different contact information, or when changing a member's contact information and the information is provided to the sponsor for the member. If not required by this implementation guide, do not send.

TR3 Notes: 1. When the communication number represents a telephone number in the United States and other countries using the North American Dialing Plan (for voice, data, fax, etc.), the communication number always includes the area code and phone number using the format AAABBBCCCC, where AAA is the area code, BBB is the telephone number prefix, and CCCC is the telephone number (e.g. (534)224-2525 would be represented as 5342242525).

TR3 Example: PER®IP®HP®8015554321~

# DIAGRAM

PER
|  PER01 | 366 | Contact | Funct Code | M 1 | ID | 2/2  |
| --- | --- | --- | --- | --- | --- | --- |
|  PER02 | 93 | Name | O 1 | AN | 1/60 |   |
|  PER03 | 365 | Comm | Number Qual | X 1 | ID | 2/2  |
|  PER04 | 364 | Comm | Number Qual | X 1 | AN 1/256 |   |
|  PER05 | 365 | Comm | Number Qual | X 1 | ID | 2/2  |
|  PER06 | 364 | Comm | Number Qual | X 1 | AN 1/256 |   |
|  PER07 | 365 | Comm | Number Qual | X 1 | ID | 2/2  |
| --- | --- | --- | --- | --- | --- | --- |
|  PER08 | 364 | Comm | Number | X 1 | AN 1/256 |   |
|  PER09 | 443 | Contact-Inq | Reference | O 1 | AN | 1/20  |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 2100A • PER

MEMBER COMMUNICATIONS NUMBERS

CONSOLIDATED • 834

ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | PER01 | 366 | Contact Function Code |   |   | M 1 | ID 2/2  |
|   |  |  | Code identifying the major duty or responsibility of the person or group named |   |   |  |   |
|   |  |  | CODE | DEFINITION |  |  |   |
|   |  |  | IP | Insured Party |  |  |   |
|  NOT USED | PER02 | 93 | Name |   | O 1 | AN | 1/60  |
|  REQUIRED | PER03 | 365 | Communication Number Qualifier |   | X 1 | ID | 2/2  |
|   |  |  | Code identifying the type of communication number |   |  |  |   |
|   |  |  | SYNTAX: P0304 |   |  |  |   |
|   |  |  | CODE | DEFINITION |  |  |   |
|   |  |  | AP | Alternate Telephone |  |  |   |
|   |  |  | BN | Beeper Number |  |  |   |
|   |  |  | CP | Cellular Phone |  |  |   |
|   |  |  | EM | Electronic Mail |  |  |   |
|   |  |  | EX | Telephone Extension |  |  |   |
|   |  |  | FX | Facsimile |  |  |   |
|   |  |  | HP | Home Phone Number |  |  |   |
|   |  |  | TE | Telephone |  |  |   |
|   |  |  | WP | Work Phone Number |  |  |   |
|  REQUIRED | PER04 | 364 | Communication Number |   | X 1 | AN | 1/256  |
|   |  |  | Complete communications number including country or area code when applicable |   |  |  |   |
|   |  |  | SYNTAX: P0304 |   |  |  |   |
|  SITUATIONAL | PER05 | 365 | Communication Number Qualifier |   | X 1 | ID | 2/2  |
|   |  |  | Code identifying the type of communication number |   |  |  |   |
|   |  |  | SYNTAX: P0506 |   |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when a value is being reported in the PER06 element. If not required by this implementation guide, do not send. |   |  |  |   |
|   |  |  | CODE | DEFINITION |  |  |   |
|   |  |  | AP | Alternate Telephone |  |  |   |
|   |  |  | BN | Beeper Number |  |  |   |
|   |  |  | CP | Cellular Phone |  |  |   |
|   |  |  | EM | Electronic Mail |  |  |   |
|   |  |  | EX | Telephone Extension |  |  |   |
|   |  |  | FX | Facsimile |  |  |   |
|   |  |  | HP | Home Phone Number |  |  |   |
|   |  |  | TE | Telephone |  |  |   |
|   |  |  | WP | Work Phone Number |  |  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • PER
MEMBER COMMUNICATIONS NUMBERS

SITUATIONAL PER06 364
Communication Number X 1 AN 1/256
Complete communications number including country or area code when applicable
SYNTAX: P0506

SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.

SITUATIONAL PER07 365
Communication Number Qualifier X 1 ID 2/2
Code identifying the type of communication number
SYNTAX: P0708

SITUATIONAL RULE: Required when a value is being reported in the PER08 element. If not required by this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  AP | Alternate Telephone  |
|  BN | Beeper Number  |
|  CP | Cellular Phone  |
|  EM | Electronic Mail  |
|  EX | Telephone Extension  |
|  FX | Facsimile  |
|  HP | Home Phone Number  |
|  TE | Telephone  |
|  WP | Work Phone Number  |

SITUATIONAL PER08 364
Communication Number X 1 AN 1/256
Complete communications number including country or area code when applicable
SYNTAX: P0708

SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.

NOT USED PER09 443
Contact Inquiry Reference O 1 AN 1/20

FEBRUARY 2011
67

005010X220 &amp; 005010X220A1 • 834 • 2100A • N3
MEMBER RESIDENCE STREET ADDRESS
CONSOLIDATED • 834

# SEGMENT DETAIL

# N3 - MEMBER RESIDENCE STREET ADDRESS

X12 Segment Name: Party Location

X12 Purpose: To specify the location of the named party

Loop: 2100A — MEMBER NAME

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when enrolling subscribers, dependents with different address information, or when changing a member's address. If not required by this implementation guide, do not send.

TR3 Example: N3*50 ORCHARD STREET~

# DIAGRAM

![img-7.jpeg](img-7.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N301 | 166 | Address Information
Address information | M 1 AN 1/55  |
|   |  |  | IMPLEMENTATION NAME: Member Address Line |   |
|  SITUATIONAL | N302 | 166 | Address Information
Address information | O 1 AN 1/55  |
|   |  |  | SITUATIONAL RULE: Required if a second address line exists. If not required by this implementation guide, do not send. |   |
|   |  |  | IMPLEMENTATION NAME: Member Address Line |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • N4
MEMBER CITY, STATE, ZIP CODE

## SEGMENT DETAIL

### N4 - MEMBER CITY, STATE, ZIP CODE

**X12 Segment Name:** Geographic Location

**X12 Purpose:** To specify the geographic place of the named party

**X12 Syntax:**

1. E0207
Only one of N402 or N407 may be present.

2. C0605
If N406 is present, then N405 is required.

3. C0704
If N407 is present, then N404 is required.

**Loop:** 2100A — MEMBER NAME

**Segment Repeat:** 1

**Usage:** SITUATIONAL

**Situational Rule:** Required when enrolling subscribers, dependents with different address information, or when changing a member’s address. If not required by this implementation guide, do not send.

**TR3 Example:** N4*KANSAS CITY*MO*64108~

## DIAGRAM

### N4 *

|  N401 | 19 | N402 | 156 | N403 | 116 | N404 | 26 | N405 | 309 | N406 | 310  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  City Name | O 1 | State or Prov Code | X 1 | ID | 2/2 | Country Code | X 1 | ID | 2/3 | Location Qualifier | X 1 ID 1/2  |
|  O 1 | AN | 2/30 |  |  |  |  |  |  |  |  |   |

* N407 1715
Country Sub Code
X 1 ID 1/3

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N401 | 19 | City Name | O 1 AN 2/30  |
|   |  |  | Free-form text for city name |   |
|   |  |  | COMMENT: A combination of either N401 through N404, or N405 and N406 may be adequate to specify a location. |   |
|   |  |  | IMPLEMENTATION NAME: Member City Name |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 2100A • N4
MEMBER CITY, STATE, ZIP CODE
CONSOLIDATED • 834

|  SITUATIONAL | N402 | 156 | State or Province Code | X 1 ID | 2/2  |
| --- | --- | --- | --- | --- | --- |
|  Code (Standard State/Province) as defined by appropriate government agency  |   |   |   |   |   |
|  SYNTAX: E0207  |   |   |   |   |   |
|  COMMENT: N402 is required only if city name (N401) is in the U.S. or Canada.  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  IMPLEMENTATION NAME: Member State Code  |   |   |   |   |   |
|  CODE SOURCE 22: States and Provinces  |   |   |   |   |   |
|  SITUATIONAL | N403 | 116 | Postal Code | O 1 ID | 3/15  |
|  Code defining international postal zone code excluding punctuation and blanks (zip code for United States)  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada, or when a postal code exists for the country in N404. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  IMPLEMENTATION NAME: Member Postal Zone or Zip Code  |   |   |   |   |   |
|  CODE SOURCE 51: ZIP Code  |   |   |   |   |   |
|  CODE SOURCE 932: Universal Postal Codes  |   |   |   |   |   |
|  SITUATIONAL | N404 | 26 | Country Code | X 1 ID | 2/3  |
|  Code identifying the country  |   |   |   |   |   |
|  SYNTAX: C0704  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is outside the United States of America. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  CODE SOURCE 5: Countries, Currencies and Funds  |   |   |   |   |   |
|  Use the alpha-2 country codes from Part 1 of ISO 3166.  |   |   |   |   |   |
|  SITUATIONAL | N405 | 309 | Location Qualifier | X 1 ID | 1/2  |
|  Code identifying type of location  |   |   |   |   |   |
|  SYNTAX: C0605  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when such transmission is required under the insurance contract between the sponsor and payer and allowed by federal and state regulations. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  CODE SOURCE 206: Government Bill of Lading Office Code  |   |   |   |   |   |
|  CODE DEFINITION  |   |   |   |   |   |
|  60 | Area  |   |   |   |   |
|  CY | County/Parish  |   |   |   |   |
|  SITUATIONAL | N406 | 310 | Location Identifier | O 1 AN | 1/30  |
|  Code which identifies a specific location  |   |   |   |   |   |
|  SYNTAX: C0605  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when such transmission is required under the insurance contract between the sponsor and payer and allowed by federal and state regulations. If not required by this implementation guide, do not send.  |   |   |   |   |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • N4
MEMBER CITY, STATE, ZIP CODE

SITUATIONAL N407 1715 Country Subdivision Code X 1 ID 1/3
Code identifying the country subdivision
SYNTAX: E0207, C0704

SITUATIONAL RULE: Required when the address is not in the United States of America, including its territories, or Canada, and the country in N404 has administrative subdivisions such as but not limited to states, provinces, cantons, etc. If not required by this implementation guide, do not send.

CODE SOURCE 5: Countries, Currencies and Funds

Use the country subdivision codes from Part 2 of ISO 3166.

FEBRUARY 2011
71

005010X220 &amp; 005010X220A1 • 834 • 2100A • DMG
MEMBER DEMOGRAPHICS
CONSOLIDATED • 834

# SEGMENT DETAIL

# DMG - MEMBER DEMOGRAPHICS

X12 Segment Name: Demographic Information

X12 Purpose: To supply demographic information

X12 Syntax: 1. P0102
If either DMG01 or DMG02 is present, then the other is required.

2. P1011
If either DMG10 or DMG11 is present, then the other is required.

3. C1105
If DMG11 is present, then DMG05 is required.

Loop: 2100A — MEMBER NAME

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when enrolling a new member, changing a member's demographic information, or terminating a member. If not required by this implementation guide, do not send.

TR3 Example: DMG*D8*19450915*F*M~

# DIAGRAM

# DMG

![img-8.jpeg](img-8.jpeg)

DMG01 1250
Date Time Format Qual
X 1 ID 2/3

![img-9.jpeg](img-9.jpeg)

DMG02 1251
Date Time Period
X 1 AN 1/35

![img-10.jpeg](img-10.jpeg)

DMG03 1068
Gender Code
O 1 ID 1/1

![img-11.jpeg](img-11.jpeg)

DMG04 1067
Marital Status Code
O 1 ID 1/1

![img-12.jpeg](img-12.jpeg)

DMG05 C056
Comp Race or Ethn Inf
X 10

![img-13.jpeg](img-13.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | DMG01 | 1250 | Date Time Period Format Qualifier
Code indicating the date format, time format, or date and time format | X 1 ID 2/3  |
|   |  |  | SYNTAX: P0102 |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | D8 Date Expressed in Format CCYYMMDD |   |
|  REQUIRED | DMG02 | 1251 | Date Time Period
Expression of a date, a time, or range of dates, times or dates and times | X 1 AN 1/35  |
|   |  |  | SYNTAX: P0102 |   |
|   |  |  | SEMANTIC: DMG02 is the date of birth. |   |
|   |  |  | IMPLEMENTATION NAME: Member Birth Date |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • DMG
MEMBER DEMOGRAPHICS

|  REQUIRED | DMG03 | 1068 | Gender Code | O 1 ID | 1/1  |
| --- | --- | --- | --- | --- | --- |
|   |  |  | Code indicating the sex of the individual |  |   |
|   |  |  | CODE | DEFINITION |   |
|   |  |  | F | Female |   |
|   |  |  | M | Male |   |
|   |  |  | U | Unknown |   |
|   |  |  |  | This code is to be used only when the gender is unknown or when it can not be sent due to reporting restrictions.  |   |
|  SITUATIONAL | DMG04 | 1067 | Marital Status Code | O 1 ID | 1/1  |
|   |  |  | Code defining the marital status of a person |  |   |
|   |  |  | SITUATIONAL RULE: Required when such transmission is required under the insurance contract between the sponsor and payer and allowed by federal and state regulations. This element is NOT USED when the member identified in the related INS segment is not the subscriber. If not required by this implementation guide, do not send. |  |   |
|   |  |  | CODE | DEFINITION |   |
|   |  |  | B | Registered Domestic Partner |   |
|   |  |  | D | Divorced |   |
|   |  |  | I | Single |   |
|   |  |  | M | Married |   |
|   |  |  | R | Unreported |   |
|   |  |  | S | Separated |   |
|   |  |  | U | Unmarried (Single or Divorced or Widowed) |   |
|   |  |  |  | This code should be used if the previous status is unknown. |   |
|   |  |  | W | Widowed |   |
|   |  |  | X | Legally Separated |   |
|  SITUATIONAL | DMG05 | C056 | COMPOSITE RACE OR ETHNICITY | X |   |
|   |  |  | INFORMATION | 10 |   |
|   |  |  | To send general and detailed information on race or ethnicity |  |   |
|   |  |  | SYNTAX: |  |   |
|   |  |  | P0203 |  |   |
|   |  |  | If either C05602 or C05603 is present, then the other is required. |  |   |
|   |  |  | SITUATIONAL RULE: Required when such transmission is required under the insurance contract between the sponsor and payer and allowed by federal and state regulations. If not required by this implementation guide, do not send. |  |   |
|   |  |  | Race or Ethnicity information is reported in either DMG05-1 or DMG05-2 and DMG05-3. |  |   |

FEBRUARY 2011
73

005010X220 &amp; 005010X220A1 • 834 • 2100A • DMG
MEMBER DEMOGRAPHICS
CONSOLIDATED • 834

|  SITUATIONAL | DMG05 - 1 | 1109 | Race or Ethnicity Code | O | ID | 1/1  |
| --- | --- | --- | --- | --- | --- | --- |
|   |  |  | Code indicating the racial or ethnic background of a person; it is normally self-reported; Under certain circumstances this information is collected for United States Government statistical purposes  |   |   |   |
|   |  |  | SITUATIONAL RULE: Required when reporting the Race or Ethnicity code from the DMG05-1 list of code values. If not required by this implementation guide, do not send.  |   |   |   |
|   |  | CODE | DEFINITION |  |  |   |
|   |  | 7 | Not Provided |  |  |   |
|   |  | 8 | Not Applicable |  |  |   |
|   |  | A | Asian or Pacific Islander |  |  |   |
|   |  | B | Black |  |  |   |
|   |  | C | Caucasian |  |  |   |
|   |  | D | Subcontinent Asian American |  |  |   |
|   |  | E | Other Race or Ethnicity |  |  |   |
|   |  | F | Asian Pacific American |  |  |   |
|   |  | G | Native American |  |  |   |
|   |  | H | Hispanic |  |  |   |
|   |  | I | American Indian or Alaskan Native |  |  |   |
|   |  | J | Native Hawaiian |  |  |   |
|   |  | N | Black (Non-Hispanic) |  |  |   |
|   |  | O | White (Non-Hispanic) |  |  |   |
|   |  | P | Pacific Islander |  |  |   |
|   |  | Z | Mutually Defined |  |  |   |
|  SITUATIONAL | DMG05 - 2 | 1270 | Code List Qualifier Code | X | ID | 1/3  |
|   |  |  | Code identifying a specific industry code list  |   |   |   |
|   |  |  | SYNTAX: |  |  |   |
|   |  |  | P0203 |  |  |   |
|   |  |  | SEMANTIC: |  |  |   |
|   |  |  | C056-02 and C056-03 are used to specify detailed information about race or ethnicity.  |   |   |   |
|   |  |  | SITUATIONAL RULE: Required when the Classification of Race or Ethnicity code set is being used to report Race or Ethnicity data. If not required by this implementation guide, do not send.  |   |   |   |
|   |  | CODE | DEFINITION |  |  |   |
|   |  | RET | Classification of Race or Ethnicity |  |  |   |
|   |  |  | CODE SOURCE 859: Classification of Race or Ethnicity  |   |   |   |
|  SITUATIONAL | DMG05 - 3 | 1271 | Industry Code | X | AN | 1/30  |
|   |  |  | Code indicating a code from a specific industry code list  |   |   |   |
|   |  |  | SYNTAX: |  |  |   |
|   |  |  | P0203 |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when reporting the Race or Ethnicity code obtained from the Classification of Race or Ethnicity code. If not required by this implementation guide, do not send. |  |  |   |
|   |  |  | IMPLEMENTATION NAME: Race or Ethnicity Code |  |  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • DMG
MEMBER DEMOGRAPHICS

# CODE SOURCE 859: Classification of Race or Ethnicity

|  SITUATIONAL | DMG06 | 1066 | Citizenship Status Code | O 1 | ID | 1/2  |
| --- | --- | --- | --- | --- | --- | --- |
|  Code indicating citizenship status  |   |   |   |   |   |   |
|  SITUATIONAL RULE: Required when such transmission is required under the insurance contract between the sponsor and payer and allowed by federal and state regulations. This element is NOT USED when the member identified in the related INS segment is not the subscriber. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  CODE | DEFINITION  |   |   |   |   |   |
|  1 | U.S. Citizen  |   |   |   |   |   |
|  2 | Non-Resident Alien  |   |   |   |   |   |
|  3 | Resident Alien  |   |   |   |   |   |
|  4 | Illegal Alien  |   |   |   |   |   |
|  5 | Alien  |   |   |   |   |   |
|  6 | U.S. Citizen - Non-Resident  |   |   |   |   |   |
|  7 | U.S. Citizen - Resident  |   |   |   |   |   |
|  NOT USED | DMG07 | 26 | Country Code | O 1 | ID | 2/3  |
|  NOT USED | DMG08 | 659 | Basis of Verification Code | O 1 | ID | 1/2  |
|  NOT USED | DMG09 | 380 | Quantity | O 1 | R | 1/15  |
|  SITUATIONAL | DMG10 | 1270 | Code List Qualifier Code | X 1 | ID | 1/3  |
|  Code identifying a specific industry code list  |   |   |   |   |   |   |
|  SYNTAX: P1011  |   |   |   |   |   |   |
|  SITUATIONAL RULE: Required when such transmission is required under the insurance contract between the sponsor and payer and allowed by federal and state regulations. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  CODE | DEFINITION  |   |   |   |   |   |
|  REC | Race or Ethnicity Collection Code  |   |   |   |   |   |
|  CODE SOURCE 860: Race or Ethnicity Collection Code  |   |   |   |   |   |   |
|  SITUATIONAL | DMG11 | 1271 | Industry Code | X 1 | AN | 1/30  |
|  Code indicating a code from a specific industry code list  |   |   |   |   |   |   |
|  SYNTAX: P1011, C1105  |   |   |   |   |   |   |
|  SEMANTIC: DMG11 is used to specify how the information in DMG05, including repeats of C056, was collected.  |   |   |   |   |   |   |
|  SITUATIONAL RULE: Required when there is a need to specify how the information in DMG05, including any repeats, was collected. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  IMPLEMENTATION NAME: Race or Ethnicity Collection Code  |   |   |   |   |   |   |

FEBRUARY 2011
75

005010X220 &amp; 005010X220A1 • 834 • 2100A • EC
EMPLOYMENT CLASS
CONSOLIDATED • 834

## SEGMENT DETAIL

### EC - EMPLOYMENT CLASS

X12 Segment Name: Employment Class

X12 Purpose: To provide class of employment information

Loop: 2100A — MEMBER NAME

Segment Repeat: &gt;1

Usage: SITUATIONAL

Situational Rule: Required when sending additional employment class information on the member. If not required by this implementation guide, do not send.

TR3 Example: EC*04*06*07~

## DIAGRAM

|  EC * | EC01 1176
Employment Class Code
O 1 ID 2/3 | EC02 1176
Employment Class Code
O 1 ID 2/3 | EC03 1176
Employment Class Code
O 1 ID 2/3 | EC04 954
Percent
O 1 R 1/10 | EC05 1201
Information Status Code
O 1 ID 1/1 | EC06 1149
Occupation Code
O 1 ID 4/6  |
| --- | --- | --- | --- | --- | --- | --- |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | EC01 | 1176 | Employment Class Code
Code indicating category of employee | O 1 ID 2/3  |
|   |  |  | CODE
DEFINITION |   |
|   |  |  | 01 | Union  |
|   |  |  | 02 | Non-Union  |
|   |  |  | 03 | Executive  |
|   |  |  | 04 | Non-Executive  |
|   |  |  | 05 | Management  |
|   |  |  | 06 | Non-Management  |
|   |  |  | 07 | Hourly  |
|   |  |  | 08 | Salaried  |
|   |  |  | 09 | Administrative  |
|   |  |  | 10 | Non-Administrative  |
|   |  |  | 11 | Exempt  |
|   |  |  | 12 | Non-Exempt  |
|   |  |  | 17 | Highly Compensated  |
|   |  |  | 18 | Key-Employee  |
|   |  |  | 19 | Bargaining  |
|   |  |  | 20 | Non-Bargaining  |
|   |  |  | 21 | Owner  |
|   |  |  | 22 | President  |
|   |  |  | 23 | Vice President  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • EC
EMPLOYMENT CLASS

SITUATIONAL EC02 1176 Employment Class Code O 1 ID 2/3
Code indicating category of employee

SITUATIONAL RULE: Required if further classification information is needed. If not required by this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  01 | Union  |
|  02 | Non-Union  |
|  03 | Executive  |
|  04 | Non-Executive  |
|  05 | Management  |
|  06 | Non-Management  |
|  07 | Hourly  |
|  08 | Salaried  |
|  09 | Administrative  |
|  10 | Non-Administrative  |
|  11 | Exempt  |
|  12 | Non-Exempt  |
|  17 | Highly Compensated  |
|  18 | Key-Employee  |
|  19 | Bargaining  |
|  20 | Non-Bargaining  |
|  21 | Owner  |
|  22 | President  |
|  23 | Vice President  |

SITUATIONAL EC03 1176 Employment Class Code O 1 ID 2/3
Code indicating category of employee

SITUATIONAL RULE: Required if further classification information is needed. If not required by this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  01 | Union  |
|  02 | Non-Union  |
|  03 | Executive  |
|  04 | Non-Executive  |
|  05 | Management  |
|  06 | Non-Management  |
|  07 | Hourly  |
|  08 | Salaried  |
|  09 | Administrative  |
|  10 | Non-Administrative  |
|  11 | Exempt  |
|  12 | Non-Exempt  |
|  17 | Highly Compensated  |
|  18 | Key-Employee  |
|  19 | Bargaining  |

FEBRUARY 2011
77

005010X220 &amp; 005010X220A1 • 834 • 2100A • EC
EMPLOYMENT CLASS
CONSOLIDATED • 834

|   |  |  | 20 | Non-Bargaining |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|   |  |  | 21 | Owner |  |  |   |
|   |  |  | 22 | President |  |  |   |
|   |  |  | 23 | Vice President |  |  |   |
|  NOT USED | EC04 | 954 | Percentage as Decimal |   | O 1 | R | 1/10  |
|  NOT USED | EC05 | 1201 | Information Status Code |   | O 1 | ID | 1/1  |
|  NOT USED | EC06 | 1149 | Occupation Code |   | O 1 | ID | 4/6  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • ICM
MEMBER INCOME

## SEGMENT DETAIL

### ICM - MEMBER INCOME

X12 Segment Name: Individual Income

X12 Purpose: To supply information to determine benefit eligibility, deductibles, and retirement and investment contributions

Loop: 2100A — MEMBER NAME

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when such transmission is required under the insurance contract between the sponsor and payer. If not required by this implementation guide, do not send.

TR3 Example: ICM*1*425.25*40~

## DIAGRAM

ICM * ICM01 594 Frequency Code M 1 ID 1/1 * ICM02 782 Monetary Amount M 1 R 1/18 * ICM03 380 Quantity O 1 R 1/15 * ICM04 310 Location Identifier O 1 AN 1/30 * ICM05 1214 Salary Grade O 1 AN 1/5 * ICM06 100 Currency Code O 1 ID 3/3

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | ICM01 | 594 | Frequency Code | M 1 ID 1/1
Code indicating frequency or type of activities or actions being reported  |

SEMA NTIC: ICM01 is the frequency at which an individual's wages are paid.

|  CODE | DEFINITION  |
| --- | --- |
|  1 | Weekly  |
|  2 | Biweekly  |
|  3 | Semimonthly  |
|  4 | Monthly  |
|  6 | Daily  |
|  7 | Annual  |
|  8 | Two Calendar Months  |
|  9 | Lump-Sum Separation Allowance  |
|  B | Year-to-Date  |
|  C | Single  |
|  H | Hourly  |
|  Q | Quarterly  |
|  S | Semiannual  |
|  U | Unknown  |

FEBRUARY 2011
79

005010X220 &amp; 005010X220A1 • 834 • 2100A • ICM
MEMBER INCOME
CONSOLIDATED • 834

|  REQUIRED | ICM02 | 782 | Monetary Amount
Monetary amount | M 1 | R | 1/18  |
| --- | --- | --- | --- | --- | --- | --- |
|   |  |  | SEMANTIC: ICM02 is the yearly wages amount. |  |  |   |
|   |  |  | IMPLEMENTATION NAME: Wage Amount |  |  |   |
|  SITUATIONAL | ICM03 | 380 | Quantity
Numeric value of quantity | O 1 | R | 1/15  |
|   |  |  | SEMANTIC: ICM03 is the weekly hours. |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when such transmission is required under the insurance contract between the sponsor and payer. If not required by this implementation guide, do not send. |  |  |   |
|   |  |  | IMPLEMENTATION NAME: Work Hours Count |  |  |   |
|  SITUATIONAL | ICM04 | 310 | Location Identifier
Code which identifies a specific location | O 1 | AN | 1/30  |
|   |  |  | SEMANTIC: ICM04 is the employer location qualifier such as a department number. |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when such transmission is required under the insurance contract between the sponsor and payer. If not required by this implementation guide, do not send. |  |  |   |
|   |  |  | IMPLEMENTATION NAME: Location Identification Code |  |  |   |
|  SITUATIONAL | ICM05 | 1214 | Salary Grade
The salary grade code assigned by the employer | O 1 | AN | 1/5  |
|   |  |  | SITUATIONAL RULE: Required when such transmission is required under the insurance contract between the sponsor and payer. If not required by this implementation guide, do not send. |  |  |   |
|   |  |  | IMPLEMENTATION NAME: Salary Grade Code |  |  |   |
|  NOT USED | ICM06 | 100 | Currency Code | O 1 | ID | 3/3  |

80
FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • AMT
MEMBER POLICY AMOUNTS

## SEGMENT DETAIL

### AMT - MEMBER POLICY AMOUNTS

X12 Segment Name: Monetary Amount Information
X12 Purpose: To indicate the total monetary amount
Loop: 2100A — MEMBER NAME
Segment Repeat: 7
Usage: SITUATIONAL
Situational Rule: Required when such transmission is required under the insurance contract between the sponsor and payer. If not required by this implementation guide, do not send.
TR3 Example: AMT®D2®100~

## DIAGRAM

AMT®
AMT01 522
Amount Qual Code
M 1 ID 1/3
AMT02 782
Monetary Amount
M 1 R 1/18
AMT03 478
Credit/Debit Flag Code
O 1 ID 1/1

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | AMT01 | 522 | Amount Qualifier Code
Code to qualify amount |   |   | M 1 | ID 1/3  |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | B9 | Co-insurance - Actual |   |  |   |
|   |  |  |  | This will contain any co-insurance selection amount.
The option of adjusting this amount to produce the actual co-insurance can be defined in the insurance contract. |   |  |   |
|   |  |  | C1 | Co-Payment Amount |   |  |   |
|   |  |  | D2 | Deductible Amount |   |  |   |
|   |  |  | EBA | Expected Expenditure Amount |   |  |   |
|   |  |  | FK | Other Unlisted Amount |   |  |   |
|   |  |  | P3 | Premium Amount |   |  |   |
|   |  |  | R | Spend Down |   |  |   |
|  REQUIRED | AMT02 | 782 | Monetary Amount
Monetary amount |   | M 1 | R | 1/18  |
|   |  |  | IMPLEMENTATION NAME: Contract Amount  |   |   |   |   |
|  NOT USED | AMT03 | 478 | Credit/Debit Flag Code |   | O 1 | ID | 1/1  |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 2100A • HLH
MEMBER HEALTH INFORMATION
CONSOLIDATED • 834

# SEGMENT DETAIL

## HLH - MEMBER HEALTH INFORMATION

X12 Segment Name: Health Information
X12 Purpose: To provide health information
Loop: 2100A — MEMBER NAME
Segment Repeat: 1
Usage: SITUATIONAL
Situational Rule: Required on initial enrollment of a member when appropriate medical information about the member is available. If not required by this implementation guide, do not send.
TR3 Example: HLH®X®74®210~

# DIAGRAM

HLH
HLH01 1212
Health Relate Code
O 1 ID 1/1
HLH02 65
Height
O 1 R 1/8
HLH03 81
Weight
O 1 R 1/10
HLH04 81
Weight
O 1 R 1/10
HLH05 352
Description
O 1 AN 1/80
HLH06 1213
Current Health Code
O 1 ID 1/1

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | HLH01 | 1212 | Health-Related Code
Code indicating a specific health situation | O 1 ID 1/1  |
|   |  |  | IMPLEMENTATION NAME: Health Related Code |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | N None |   |
|   |  |  | S Substance Abuse |   |
|   |  |  | T Tobacco Use |   |
|   |  |  | U Unknown |   |
|   |  |  | X Tobacco Use and Substance Abuse |   |
|  SITUATIONAL | HLH02 | 65 | Height
Vertical dimension of an object measured when the object is in the upright position | O 1 R 1/8  |
|   |  |  | SITUATIONAL RULE: Required when available. If not required by this implementation guide, do not send. |   |
|   |  |  | IMPLEMENTATION NAME: Member Height |   |
|   |  |  | The height must be reported in inches. |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • HLH
MEMBER HEALTH INFORMATION

|  SITUATIONAL | HLH03 | 81 | Weight | O 1 | R | 1/10  |
| --- | --- | --- | --- | --- | --- | --- |
|   |  |  | Numeric value of weight |  |  |   |
|   |  |  | SEMANTIC: HLH03 is the current weight in pounds. |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when available. If not required by this implementation guide, do not send. |  |  |   |
|   |  |  | IMPLEMENTATION NAME: Member Weight |  |  |   |
|  NOT USED | HLH04 | 81 | Weight | O 1 | R | 1/10  |
|  NOT USED | HLH05 | 352 | Description | O 1 | AN | 1/80  |
|  NOT USED | HLH06 | 1213 | Current Health Condition Code | O 1 | ID | 1/1  |
|  NOT USED | HLH07 | 352 | Description | O 1 | AN | 1/80  |

FEBRUARY 2011
83

005010X220 &amp; 005010X220A1 • 834 • 2100A • LUI
MEMBER LANGUAGE
CONSOLIDATED • 834

# SEGMENT DETAIL

# LUI - MEMBER LANGUAGE

X12 Segment Name: Language Use

X12 Purpose: To specify language, type of usage, and proficiency or fluency

X12 Syntax: 1. P0102
If either LUI01 or LUI02 is present, then the other is required.

2. L040203
If LUI04 is present, then at least one of LUI02 or LUI03 are required.

Loop: 2100A — MEMBER NAME

Segment Repeat: &gt;1

Usage: SITUATIONAL

Situational Rule: Required if the sponsor knows that the member's primary language is not English, and such transmission is required under the insurance contract between the sponsor and payer and allowed by federal and state regulations. If not required by this implementation guide do not send.

TR3 Notes: 1. Any need to send/collect this information will need to be contained in the trading partner agreement.

TR3 Example: LUI*LD*123**8~

# DIAGRAM

|  LUI * | LUI01 66
ID Code
Qualifier
X 1 ID 1/2 | LUI02 67
ID
Code
X 1 AN 2/80 | LUI03 352
Description
X 1 AN 1/80 | LUI04 1303
Use of
Lang Indica
O 1 ID 1/2 | LUI05 1476
Language
Prof Indica
O 1 ID 1/1  |
| --- | --- | --- | --- | --- | --- |

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  SITUATIONAL | LUI01 | 66 | Identification Code Qualifier
Code designating the system/method of code structure used for Identification Code (67)
SYNTAX: P0102 | X 1 ID 1/2  |

SITUATIONAL RULE: Required when a value is being reported in the LUI02 element. If not required by this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  LD | NISO Z39.53 Language Codes  |
|  LE | CODE SOURCE 457: NISO Z39.53 Language Code List
ISO 639 Language Codes
CODE SOURCE 102: Languages  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100A • LUI
MEMBER LANGUAGE

|  SITUATIONAL | LUI02 | 67 | Identification Code
Code identifying a party or other code
SYNTAX: P0102, L040203
SEMANTIC: LUI02 is the language code.
SITUATIONAL RULE: Required if the sponsor is able to code the language identification. If not required by this implementation guide, do not send. | X 1 | AN | 2/80  |
| --- | --- | --- | --- | --- | --- | --- |
|   |  |  | IMPLEMENTATION NAME: Language Code |  |  |   |
|  SITUATIONAL | LUI03 | 352 | Description
A free-form description to clarify the related data elements and their content
SYNTAX: L040203
SEMANTIC: LUI03 is the name of the language.
SITUATIONAL RULE: Required if the sender is unable to code the necessary language identification in LUI01 and LUI02. If not required by this implementation guide, do not send. | X 1 | AN | 1/80  |
|   |  |  | IMPLEMENTATION NAME: Language Description |  |  |   |
|  SITUATIONAL | LUI04 | 1303 | Use of Language Indicator
Code indicating the use of a language
SYNTAX: L040203
SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send. | O 1 | ID | 1/2  |
|   |  |  | IMPLEMENTATION NAME: Language Use Indicator |  |  |   |
|   |  |  | CODE | DEFINITION |  |   |
|   |  |  | 5 | Language Reading |  |   |
|   |  |  | 6 | Language Writing |  |   |
|   |  |  | 7 | Language Speaking |  |   |
|   |  |  | 8 | Native Language |  |   |
|  NOT USED | LUI05 | 1476 | Language Proficiency Indicator | O 1 | ID | 1/1  |

FEBRUARY 2011
85

005010X220 &amp; 005010X220A1 • 834 • 2100B • NM1
INCORRECT MEMBER NAME
CONSOLIDATED • 834

# SEGMENT DETAIL

# NM1 - INCORRECT MEMBER NAME

X12 Segment Name: Individual or Organizational Name

X12 Purpose: To supply the full name of an individual or organizational entity

X12 Syntax:
1. P0809
If either NM108 or NM109 is present, then the other is required.
2. C1110
If NM111 is present, then NM110 is required.
3. C1203
If NM112 is present, then NM103 is required.

Loop: 2100B — INCORRECT MEMBER NAME  Loop Repeat: 1

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required if a corrected name is being sent in loop 2100A or if previously supplied demographics are being changed. If only the demographics are being changed, the code in NM101 in loop 2100A will be IL, and the code in NM101 in this loop will be 70. If not required by this implementation guide, do not send.

TR3 Notes: 1. If only the demographics are being changed, the code in NM101 in loop 2100A will be IL, and the code in NM101 in this loop will be 70.

TR3 Example: NM1*70*1*SMYTH*JON~

# DIAGRAM

![img-14.jpeg](img-14.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | NM101 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual | M 1 ID 2/3  |
|   |  |  | This code identifies that the information that follows is previously reported enrollment information that is being corrected. |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 70 Prior Incorrect Insured |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100B • NM1
INCORRECT MEMBER NAME

|  REQUIRED | NM102 | 1065 | Entity Type Qualifier
Code qualifying the type of entity
SEMANTIC: NM102 qualifies NM103.
CODE DEFINITION | M 1 | ID | 1/1  |
| --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | NM103 | 1035 | 1 Person
Name Last or Organization Name
Individual last name or organizational name
SYNTAX: C1203
IMPLEMENTATION NAME: Prior Incorrect Member Last Name | X 1 | AN | 1/60  |
|  SITUATIONAL | NM104 | 1036 | Name First
Individual first name | O 1 | AN | 1/35  |
|   |   |   |  SITUATIONAL RULE: Required when NM102 is equal to “1” (person) and the person has a first name. If not required by this implementation guide, do not send. |  |  |   |
|   |   |   |  IMPLEMENTATION NAME: Prior Incorrect Member First Name |  |  |   |
|  SITUATIONAL | NM105 | 1037 | Name Middle
Individual middle name or initial | O 1 | AN | 1/25  |
|   |   |   |  SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send. |  |  |   |
|   |   |   |  IMPLEMENTATION NAME: Prior Incorrect Member Middle Name |  |  |   |
|  SITUATIONAL | NM106 | 1038 | Name Prefix
Prefix to individual name | O 1 | AN | 1/10  |
|   |   |   |  SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send. |  |  |   |
|   |   |   |  IMPLEMENTATION NAME: Prior Incorrect Member Name Prefix |  |  |   |
|  SITUATIONAL | NM107 | 1039 | Name Suffix
Suffix to individual name | O 1 | AN | 1/10  |
|   |   |   |  SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send. |  |  |   |
|   |   |   |  IMPLEMENTATION NAME: Prior Incorrect Member Name Suffix |  |  |   |
|  SITUATIONAL | NM108 | 66 | Identification Code Qualifier
Code designating the system/method of code structure used for Identification Code (67)
SYNTAX: P0809
SITUATIONAL RULE: Required when a corrected value is being reported in the NM109 element. If not required by this implementation guide, do not send. | X 1 | ID | 1/2  |
|   |   |   |  CODE DEFINITION |  |  |   |
|   |   |   |  34 | Social Security Number |  |   |
|   |   |   |   | The social security number may not be used for any Federally administered programs such as Medicare or CHAMPUS/TRICARE. |  |   |

FEBRUARY 2011
87

005010X220 &amp; 005010X220A1 • 834 • 2100B • NM1
INCORRECT MEMBER NAME
CONSOLIDATED • 834

|   |  |  | ZZ | Mutually Defined  |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|   |  |  |  | Value is required if National Individual Identifier is mandated for use. Otherwise, one of the other listed codes may be used.  |   |   |   |
|  SITUATIONAL | NM109 | 67 | Identification Code |   | X 1 | AN | 2/80  |
|   |   |   |  Code identifying a party or other code |   |  |  |   |
|   |   |   |  SYNTAX: P0809 |   |  |  |   |
|   |   |   |  SITUATIONAL RULE: Required when there was a previous error. If not required by this implementation guide, do not send. |   |  |  |   |
|   |   |   |  IMPLEMENTATION NAME: Prior Incorrect Insured Identifier |   |  |  |   |
|   |   |   |  NM109 is the identifier that was previously sent in error. This allows matching with data on receiver's system. |   |  |  |   |
|  NOT USED | NM110 | 706 | Entity Relationship Code |   | X 1 | ID | 2/2  |
|  NOT USED | NM111 | 98 | Entity Identifier Code |   | O 1 | ID | 2/3  |
|  NOT USED | NM112 | 1035 | Name Last or Organization Name |   | O 1 | AN | 1/60  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100B • DMG
INCORRECT MEMBER DEMOGRAPHICS

# SEGMENT DETAIL

## DMG - INCORRECT MEMBER DEMOGRAPHICS

X12 Segment Name: Demographic Information

X12 Purpose: To supply demographic information

X12 Syntax:
1. P0102
If either DMG01 or DMG02 is present, then the other is required.
2. P1011
If either DMG10 or DMG11 is present, then the other is required.
3. C1105
If DMG11 is present, then DMG05 is required.

Loop: 2100B — INCORRECT MEMBER NAME

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when there is a change to the previously supplied demographic information. If not required by this implementation guide, do not send.

TR3 Example: DMG*D8*19450915*M~

# DIAGRAM

![img-15.jpeg](img-15.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  SITUATIONAL | DMG01 | 1250 | Date Time Period Format Qualifier
X 1 ID 2/3
Code indicating the date format, time format, or date and time format | X 1 ID 2/3  |
|   |  |  | SYNTAX: P0102 |   |
|   |  |  | SITUATIONAL RULE: Required when the members birth date is being corrected. If not required by this implementation guide, do not send. |   |
|   |  | CODE | DEFINITION |   |
|   |  | D8 | Date Expressed in Format CCYYMMDD |   |

FEBRUARY 2011
89

005010X220 &amp; 005010X220A1 • 834 • 2100B • DMG
INCORRECT MEMBER DEMOGRAPHICS
CONSOLIDATED • 834

|  SITUATIONAL | DMG02 | 1251 | Date Time Period | X 1 | AN | 1/35  |
| --- | --- | --- | --- | --- | --- | --- |
|  Expression of a date, a time, or range of dates, times or dates and times  |   |   |   |   |   |   |
|  SYNTAX: P0102  |   |   |   |   |   |   |
|  SEMANTIC: DMG02 is the date of birth.  |   |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the members birth date is being corrected. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  IMPLEMENTATION NAME: Prior Incorrect Insured Birth Date  |   |   |   |   |   |   |
|  SITUATIONAL | DMG03 | 1068 | Gender Code | O 1 | ID | 1/1  |
|  Code indicating the sex of the individual  |   |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the members gender is being corrected. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  IMPLEMENTATION NAME: Prior Incorrect Insured Gender Code  |   |   |   |   |   |   |
|   |  |  | CODE | DEFINITION  |   |   |
|   |  |  | F | Female  |   |   |
|   |  |  | M | Male  |   |   |
|   |  |  | U | Unknown  |   |   |
|  SITUATIONAL | DMG04 | 1067 | Marital Status Code | O 1 | ID | 1/1  |
|  Code defining the marital status of a person  |   |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the members Marital Status Code is being corrected. If not required this implementation guide, do not send.  |   |   |   |   |   |   |
|   |  |  | CODE | DEFINITION  |   |   |
|   |  |  | B | Registered Domestic Partner  |   |   |
|   |  |  | D | Divorced  |   |   |
|   |  |  | I | Single  |   |   |
|   |  |  | M | Married  |   |   |
|   |  |  | R | Unreported  |   |   |
|   |  |  | S | Separated  |   |   |
|   |  |  | U | Unmarried (Single or Divorced or Widowed)  |   |   |
|   |  |  |  | This code should be used if the previous status is unknown.  |   |   |
|   |  |  | W | Widowed  |   |   |
|   |  |  | X | Legally Separated  |   |   |
|  SITUATIONAL | DMG05 | C056 | COMPOSITE RACE OR ETHNICITY | X  |   |   |
|   |  |  | INFORMATION | 10  |   |   |
|  To send general and detailed information on race or ethnicity  |   |   |   |   |   |   |
|  SYNTAX:  |   |   |   |   |   |   |
|  P0203  |   |   |   |   |   |   |
|  If either C05602 or C05603 is present, then the other is required.  |   |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the members Race or Ethnicity is being corrected. If not required this implementation guide, do not send.  |   |   |   |   |   |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100B • DMG
INCORRECT MEMBER DEMOGRAPHICS

SITUATIONAL DMG05 - 1

1109 Race or Ethnicity Code O ID 1/1
Code indicating the racial or ethnic background of a person; it is normally self-reported; Under certain circumstances this information is collected for United States Government statistical purposes

SITUATIONAL RULE: Required when the members Race or Ethnicity is being corrected. If not required this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  7 | Not Provided  |
|  8 | Not Applicable  |
|  A | Asian or Pacific Islander  |
|  B | Black  |
|  C | Caucasian  |
|  D | Subcontinent Asian American  |
|  E | Other Race or Ethnicity  |
|  F | Asian Pacific American  |
|  G | Native American  |
|  H | Hispanic  |
|  I | American Indian or Alaskan Native  |
|  J | Native Hawaiian  |
|  N | Black (Non-Hispanic)  |
|  O | White (Non-Hispanic)  |
|  P | Pacific Islander  |
|  Z | Mutually Defined  |

SITUATIONAL DMG05 - 2

1270 Code List Qualifier Code X ID 1/3
Code identifying a specific industry code list

SYNTAX: P0203

SEMANTIC: C056-02 and C056-03 are used to specify detailed information about race or ethnicity.

SITUATIONAL RULE: Required when the members Race or Ethnicity is being corrected. If not required this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  RET | Classification of Race or Ethnicity  |
|  1271 | Code source 859: Classification of Race or Ethnicity
Industry Code X AN 1/30
Code indicating a code from a specific industry code list  |

SYNTAX: P0203

SITUATIONAL RULE: Required when the members Race or Ethnicity is being corrected. If not required this implementation guide, do not send.

IMPLEMENTATION NAME: Race or Ethnicity Code

FEBRUARY 2011
91

005010X220 &amp; 005010X220A1 • 834 • 2100B • DMG
INCORRECT MEMBER DEMOGRAPHICS
CONSOLIDATED • 834

|  SITUATIONAL | DMG06 | 1066 | Citizenship Status Code |   | O 1 | ID | 1/2  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|   |   |   |  Code indicating citizenship status |   |  |  |   |
|   |   |   |  SITUATIONAL RULE: Required when the members Race or Ethnicity is being corrected. If not required this implementation guide, do not send. |   |  |  |   |
|   |   |   |  CODE | DEFINITION |  |  |   |
|   |   |   |  1 | U.S. Citizen |  |  |   |
|   |   |   |  2 | Non-Resident Alien |  |  |   |
|   |   |   |  3 | Resident Alien |  |  |   |
|   |   |   |  4 | Illegal Alien |  |  |   |
|   |   |   |  5 | Alien |  |  |   |
|   |   |   |  6 | U.S. Citizen - Non-Resident |  |  |   |
|   |   |   |  7 | U.S. Citizen - Resident |  |  |   |
|  NOT USED | DMG07 | 26 | Country Code |   | O 1 | ID | 2/3  |
|  NOT USED | DMG08 | 659 | Basis of Verification Code |   | O 1 | ID | 1/2  |
|  NOT USED | DMG09 | 380 | Quantity |   | O 1 | R | 1/15  |
|  SITUATIONAL | DMG10 | 1270 | Code List Qualifier Code |   | X 1 | ID | 1/3  |
|   |   |   |  Code identifying a specific industry code list |   |  |  |   |
|   |   |   |  SYNTAX: P1011 |   |  |  |   |
|   |   |   |  SITUATIONAL RULE: Required when the members Race or Ethnicity is being corrected. If not required this implementation guide, do not send. |   |  |  |   |
|   |   |   |  CODE | DEFINITION |  |  |   |
|  SITUATIONAL | DMG11 | 1271 | REC |   | Race or Ethnicity Collection Code  |   |   |
|   |   |   |  Industry Code |   | X 1 | AN | 1/30  |
|   |   |   |  Code indicating a code from a specific industry code list |   |  |  |   |
|   |   |   |  SYNTAX: P1011, C1105 |   |  |  |   |
|   |   |   |  SEMANTIC: DMG11 is used to specify how the information in DMG05, including repeats of C056, was collected. |   |  |  |   |
|   |   |   |  SITUATIONAL RULE: Required when the members Race or Ethnicity is being corrected. If not required this implementation guide, do not send. |   |  |  |   |
|   |   |   |  IMPLEMENTATION NAME: Race or Ethnicity Collection Code |   |  |  |   |
|   |   |   |  |   |   |   |   |
|   |   |   |  |   |   |   |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100C • NM1
MEMBER MAILING ADDRESS

## SEGMENT DETAIL

### NM1 - MEMBER MAILING ADDRESS

**X12 Segment Name:** Individual or Organizational Name
**X12 Purpose:** To supply the full name of an individual or organizational entity
**X12 Syntax:**
1. P0809
If either NM108 or NM109 is present, then the other is required.
2. C1110
If NM111 is present, then NM110 is required.
3. C1203
If NM112 is present, then NM103 is required.

**Loop:** 2100C — MEMBER MAILING ADDRESS
**Loop Repeat:** 1

**Segment Repeat:** 1

**Usage:** SITUATIONAL

**Situational Rule:** Required when the member mailing address is different from the residence address sent in loop 2100A or when the dependent’s address is different from the subscriber. If not required by this implementation guide, do not send.

**TR3 Example:** NM1*31*1~

## DIAGRAM

|  NM1 * | NM101 98
Entity ID Code
M 1 ID 2/3 | * | NM102 1065
Entity Type Qualifier
M 1 ID 1/1 | * | NM103 1035
Name Last/Org Name
X 1 AN 1/60 | * | NM104 1036
Name First
O 1 AN 1/35 | * | NM105 1037
Name Middle
O 1 AN 1/25 | * | NM106 1038
Name Prefix
O 1 AN 1/10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  * | NM107 1039
Name Suffix
O 1 AN 1/10 | * | NM108 66
ID Code Qualifier
X 1 ID 1/2 | * | NM109 67
ID Code
X 1 AN 2/80 | * | NM110 706
Entity Relat Code
X 1 ID 2/2 | * | NM111 98
Entity ID Code
O 1 ID 2/3 | * | NM112 1035
Name Last/Org Name
O 1 AN 1/60  |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | NM101 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 31 Postal Mailing Address |   |
|  REQUIRED | NM102 | 1065 | Entity Type Qualifier
Code qualifying the type of entity | M 1 ID 1/1  |
|   |  |  | SEMANTIC: NM102 qualifies NM103. |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 1 Person |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 2100C • NM1
MEMBER MAILING ADDRESS
CONSOLIDATED • 834

|  NOT USED | NM103 | 1035 | Name Last or Organization Name | X 1 | AN | 1/60  |
| --- | --- | --- | --- | --- | --- | --- |
|  NOT USED | NM104 | 1036 | Name First | O 1 | AN | 1/35  |
|  NOT USED | NM105 | 1037 | Name Middle | O 1 | AN | 1/25  |
|  NOT USED | NM106 | 1038 | Name Prefix | O 1 | AN | 1/10  |
|  NOT USED | NM107 | 1039 | Name Suffix | O 1 | AN | 1/10  |
|  NOT USED | NM108 | 66 | Identification Code Qualifier | X 1 | ID | 1/2  |
|  NOT USED | NM109 | 67 | Identification Code | X 1 | AN | 2/80  |
|  NOT USED | NM110 | 706 | Entity Relationship Code | X 1 | ID | 2/2  |
|  NOT USED | NM111 | 98 | Entity Identifier Code | O 1 | ID | 2/3  |
|  NOT USED | NM112 | 1035 | Name Last or Organization Name | O 1 | AN | 1/60  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100C • N3
MEMBER MAIL STREET ADDRESS

## SEGMENT DETAIL

### N3 - MEMBER MAIL STREET ADDRESS

X12 Segment Name: Party Location

X12 Purpose: To specify the location of the named party

Loop: 2100C — MEMBER MAILING ADDRESS

Segment Repeat: 1

Usage: REQUIRED

TR3 Example: N3®P.O. Box 1234~

## DIAGRAM

### N3

N301 166
Address Information
M 1 AN 1/55

N302 166
Address Information
O 1 AN 1/55

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | N301 | 166 | Address Information
Address information | M 1 | AN | 1/55  |
|   |  |  | IMPLEMENTATION NAME: Member Address Line |  |  |   |
|  SITUATIONAL | N302 | 166 | Address Information
Address information | O 1 | AN | 1/55  |
|   |  |  | SITUATIONAL RULE: Required if a second address line exists. If not required by this implementation guide, do not send. |  |  |   |
|   |  |  | IMPLEMENTATION NAME: Member Address Line |  |  |   |

FEBRUARY 2011
95

005010X220 &amp; 005010X220A1 • 834 • 2100C • N4
MEMBER MAIL CITY, STATE, ZIP CODE
CONSOLIDATED • 834

# SEGMENT DETAIL

# N4 - MEMBER MAIL CITY, STATE, ZIP CODE

X12 Segment Name: Geographic Location

X12 Purpose: To specify the geographic place of the named party

X12 Syntax: 1. E0207
Only one of N402 or N407 may be present.

2. C0605
If N406 is present, then N405 is required.

3. C0704
If N407 is present, then N404 is required.

Loop: 2100C — MEMBER MAILING ADDRESS

Segment Repeat: 1

Usage: REQUIRED

TR3 Example: N4*KANSAS CITY*MO*64108~

# DIAGRAM

N4
![img-16.jpeg](img-16.jpeg)

N407 1715
Country Sub Code
X 1 ID 1/3

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N401 | 19 | City Name
Free-form text for city name | O 1 AN 2/30  |
|   |  |  | COMMENT: A combination of either N401 through N404, or N405 and N406 may be adequate to specify a location.  |   |
|   |  |  | IMPLEMENTATION NAME: Member Mail City Name  |   |
|  SITUATIONAL | N402 | 156 | State or Province Code
Code (Standard State/Province) as defined by appropriate government agency
SYNTAX: E0207 | X 1 ID 2/2  |
|   |  |  | COMMENT: N402 is required only if city name (N401) is in the U.S. or Canada.  |   |
|   |  |  | SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada. If not required by this implementation guide, do not send.  |   |
|   |  |  | IMPLEMENTATION NAME: Member Mail State Code  |   |
|   |  |  | CODE SOURCE 22: States and Provinces  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100C • N4
MEMBER MAIL CITY, STATE, ZIP CODE

|  SITUATIONAL | N403 | 116 | Postal Code | O 1 | ID | 3/15  |
| --- | --- | --- | --- | --- | --- | --- |
|  Code defining international postal zone code excluding punctuation and blanks (zip code for United States)  |   |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada, or when a postal code exists for the country in N404. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  IMPLEMENTATION NAME: Member Mail Postal Zone or ZIP Code  |   |   |   |   |   |   |
|  CODE SOURCE 51: ZIP Code  |   |   |   |   |   |   |
|  CODE SOURCE 932: Universal Postal Codes  |   |   |   |   |   |   |
|  SITUATIONAL | N404 | 26 | Country Code | X 1 | ID | 2/3  |
|  Code identifying the country  |   |   |   |   |   |   |
|  SYNTAX: C0704  |   |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is outside the United States of America. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  CODE SOURCE 5: Countries, Currencies and Funds  |   |   |   |   |   |   |
|  Use the alpha-2 country codes from Part 1 of ISO 3166.  |   |   |   |   |   |   |
|  NOT USED | N405 | 309 | Location Qualifier | X 1 | ID | 1/2  |
|  NOT USED | N406 | 310 | Location Identifier | O 1 | AN | 1/30  |
|  SITUATIONAL | N407 | 1715 | Country Subdivision Code | X 1 | ID | 1/3  |
|  Code identifying the country subdivision  |   |   |   |   |   |   |
|  SYNTAX: E0207, C0704  |   |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is not in the United States of America, including its territories, or Canada, and the country in N404 has administrative subdivisions such as but not limited to states, provinces, cantons, etc. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  CODE SOURCE 5: Countries, Currencies and Funds  |   |   |   |   |   |   |
|  Use the country subdivision codes from Part 2 of ISO 3166.  |   |   |   |   |   |   |

FEBRUARY 2011
97

005010X220 &amp; 005010X220A1 • 834 • 2100D • NM1
MEMBER EMPLOYER
CONSOLIDATED • 834

# SEGMENT DETAIL

# NM1 - MEMBER EMPLOYER

X12 Segment Name: Individual or Organizational Name

X12 Purpose: To supply the full name of an individual or organizational entity

X12 Syntax:
1. P0809
If either NM108 or NM109 is present, then the other is required.
2. C1110
If NM111 is present, then NM110 is required.
3. C1203
If NM112 is present, then NM103 is required.

Loop: 2100D — MEMBER EMPLOYER  Loop Repeat: 3

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the member is employed by someone other than the sponsor and the insurance contract requires the payer to be notified of such employment. If not required by this implementation guide, do not send.

TR3 Notes: 1. This segment is not used to collect Coordination of Benefits (COB) information. COB information must be passed in the 2320 loop.

TR3 Example: NM1*36*2*ABC CORP.~

# DIAGRAM

![img-17.jpeg](img-17.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | NM101 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 36 Employer |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100D • NM1
MEMBER EMPLOYER

|  REQUIRED | NM102 | 1065 | Entity Type Qualifier
Code qualifying the type of entity
SEMANTIC: NM102 qualifies NM103.
CODE DEFINITION
1 Person
2 Non-Person Entity | M 1 ID | 1/1  |
| --- | --- | --- | --- | --- | --- |
|  SITUATIONAL | NM103 | 1035 | Name Last or Organization Name
Individual last name or organizational name
SYNTAX: C1203
SITUATIONAL RULE: Required until the National Identifier for employer is implemented. If not required by this implementation guide, do not send. | X 1 AN | 1/60  |
|  SITUATIONAL | NM104 | 1036 | IMPLEMENTATION NAME: Member Employer Name
Name First
Individual first name
SITUATIONAL RULE: Required when NM102 is equal to “1” (person) and the person has a first name. If not required by this implementation guide, do not send. | O 1 AN | 1/35  |
|  SITUATIONAL | NM105 | 1037 | IMPLEMENTATION NAME: Member Employer First Name
Name Middle
Individual middle name or initial
SITUATIONAL RULE: Required if supplied by the member and NM102 equals ‘1’. If not required by this implementation guide, do not send. | O 1 AN | 1/25  |
|  SITUATIONAL | NM106 | 1038 | IMPLEMENTATION NAME: Member Employer Middle Name
Name Prefix
Prefix to individual name
SITUATIONAL RULE: Required if supplied by the member and NM102 equals ‘1’. If not required by this implementation guide, do not send. | O 1 AN | 1/10  |
|  SITUATIONAL | NM107 | 1039 | IMPLEMENTATION NAME: Member Employer Name Prefix
Name Suffix
Suffix to individual name
SITUATIONAL RULE: Required if supplied by the member and NM102 equals ‘1’. If not required by this implementation guide, do not send. | O 1 AN | 1/10  |

FEBRUARY 2011
99

005010X220 &amp; 005010X220A1 • 834 • 2100D • NM1
MEMBER EMPLOYER
CONSOLIDATED • 834

|  SITUATIONAL | NM108 | 66 | Identification Code Qualifier | X 1 ID | 1/2  |
| --- | --- | --- | --- | --- | --- |
|   |  |  | Code designating the system/method of code structure used for Identification Code (67)  |   |   |
|   |  |  | SYNTAX: P0809  |   |   |
|   |  |  | SITUATIONAL RULE: Required when a value is being reported in the NM109 element. If not required by this implementation guide, do not send.  |   |   |
|   |  |  | CODE | DEFINITION  |   |
|   |  |  | 24 | Employer's Identification Number  |   |
|   |  |  |  | This is the "HIPAA Employer Identifier".  |   |
|   |  |  | 34 | Social Security Number  |   |
|  SITUATIONAL | NM109 | 67 | Identification Code | X 1 AN | 2/80  |
|   |  |  | Code identifying a party or other code  |   |   |
|   |  |  | SYNTAX: P0809  |   |   |
|   |  |  | SITUATIONAL RULE: Required when available, and allowed under confidentiality regulations. If not required by this implementation guide, do not send.  |   |   |
|   |  |  | IMPLEMENTATION NAME: Member Employer Identifier  |   |   |
|  NOT USED | NM110 | 706 | Entity Relationship Code | X 1 ID | 2/2  |
|  NOT USED | NM111 | 98 | Entity Identifier Code | O 1 ID | 2/3  |
|  NOT USED | NM112 | 1035 | Name Last or Organization Name | O 1 AN | 1/60  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100D • PER MEMBER EMPLOYER COMMUNICATIONS NUMBERS

## SEGMENT DETAIL

# PER - MEMBER EMPLOYER COMMUNICATIONS NUMBERS

X12 Segment Name: Administrative Communications Contact

X12 Purpose: To identify a person or office to whom administrative communications should be directed

X12 Syntax:
1. P0304
If either PER03 or PER04 is present, then the other is required.
2. P0506
If either PER05 or PER06 is present, then the other is required.
3. P0708
If either PER07 or PER08 is present, then the other is required.

Loop: 2100D — MEMBER EMPLOYER

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the Member Employers contact information is provided to the sponsor. If not required by this implementation guide, do not send.

TR3 Notes:
1. When the communication number represents a telephone number in the United States and other countries using the North American Dialing Plan (for voice, data, fax, etc.), the communication number always includes the area code and phone number using the format AAABBBCCCC, where AAA is the area code, BBB is the telephone number prefix, and CCCC is the telephone number (e.g. (534)224-2525 would be represented as 5342242525).

TR3 Example: PER*EP**TE*8001234567~

## DIAGRAM

PER
![img-18.jpeg](img-18.jpeg)
![img-19.jpeg](img-19.jpeg)

FEBRUARY 2011
101

005010X220 &amp; 005010X220A1 • 834 • 2100D • PER

MEMBER EMPLOYER COMMUNICATIONS NUMBERS

CONSOLIDATED • 834

ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | PER01 | 366 | Contact Function Code |   |   | M 1 | ID 2/2  |
|   |  |  | Code identifying the major duty or responsibility of the person or group named |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | EP | Employer Contact |   |  |   |
|  SITUATIONAL | PER02 | 93 | Name |  |  | O 1 | AN 1/60  |
|   |  |  | Free-form name |  |  |  |   |
|   |  |  | SITUATIONAL RULE: Required if member employer communication contact name is supplied by the member. If not required by this implementation guide, do not send.  |   |   |   |   |
|   |  |  | IMPLEMENTATION NAME: Member Employer Communications Contact Name  |   |   |   |   |
|  REQUIRED | PER03 | 365 | Communication Number Qualifier |   |   | X 1 | ID 2/2  |
|   |  |  | Code identifying the type of communication number |   |   |  |   |
|   |  |  | SYNTAX: P0304 |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | AP | Alternate Telephone |   |  |   |
|   |  |  | BN | Beeper Number |   |  |   |
|   |  |  | CP | Cellular Phone |   |  |   |
|   |  |  | EM | Electronic Mail |   |  |   |
|   |  |  | EX | Telephone Extension |   |  |   |
|   |  |  | FX | Facsimile |   |  |   |
|   |  |  | TE | Telephone |   |  |   |
|  REQUIRED | PER04 | 364 | Communication Number |   |   | X 1 | AN 1/256  |
|   |  |  | Complete communications number including country or area code when applicable |   |   |  |   |
|   |  |  | SYNTAX: P0304 |   |   |  |   |
|  SITUATIONAL | PER05 | 365 | Communication Number Qualifier |   |   | X 1 | ID 2/2  |
|   |  |  | Code identifying the type of communication number |   |   |  |   |
|   |  |  | SYNTAX: P0506 |   |   |  |   |
|   |  |  | SITUATIONAL RULE: Required when a value is being reported in the PER06 element. If not required by this implementation guide, do not send.  |   |   |   |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | AP | Alternate Telephone |   |  |   |
|   |  |  | BN | Beeper Number |   |  |   |
|   |  |  | CP | Cellular Phone |   |  |   |
|   |  |  | EM | Electronic Mail |   |  |   |
|   |  |  | EX | Telephone Extension |   |  |   |
|   |  |  | FX | Facsimile |   |  |   |
|   |  |  | TE | Telephone |   |  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100D • PER
MEMBER EMPLOYER COMMUNICATIONS NUMBERS

SITUATIONAL PER06 364 Communication Number X 1 AN 1/256
Complete communications number including country or area code when applicable
SYNTAX: P0506

SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.

SITUATIONAL PER07 365 Communication Number Qualifier X 1 ID 2/2
Code identifying the type of communication number
SYNTAX: P0708

SITUATIONAL RULE: Required when a value is being reported in the PER08 element. If not required by this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  AP | Alternate Telephone  |
|  BN | Beeper Number  |
|  CP | Cellular Phone  |
|  EM | Electronic Mail  |
|  EX | Telephone Extension  |
|  FX | Facsimile  |
|  TE | Telephone  |

SITUATIONAL PER08 364 Communication Number X 1 AN 1/256
Complete communications number including country or area code when applicable
SYNTAX: P0708

SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.

NOT USED PER09 443 Contact Inquiry Reference O 1 AN 1/20

FEBRUARY 2011 103

005010X220 &amp; 005010X220A1 • 834 • 2100D • N3
MEMBER EMPLOYER STREET ADDRESS
CONSOLIDATED • 834

# SEGMENT DETAIL

# N3 - MEMBER EMPLOYER STREET ADDRESS

X12 Segment Name: Party Location

X12 Purpose: To specify the location of the named party

Loop: 2100D — MEMBER EMPLOYER

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the member's employer is not the sponsor and the employer address is provided to the sponsor by the member. If not required by this implementation guide, do not send.

TR3 Example: N3*50 ORCHARD STREET~

# DIAGRAM

![img-20.jpeg](img-20.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N301 | 166 | Address Information
Address information | M 1 AN 1/55  |
|   |  |  | IMPLEMENTATION NAME: Member Employer Address Line  |   |
|  SITUATIONAL | N302 | 166 | Address Information
Address information | O 1 AN 1/55  |
|   |  |  | SITUATIONAL RULE: Required if a second address line exists. If not required by this implementation guide, do not send.  |   |
|   |  |  | IMPLEMENTATION NAME: Member Employer Address Line  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100D • N4
MEMBER EMPLOYER CITY, STATE, ZIP CODE

## SEGMENT DETAIL

**N4 - MEMBER EMPLOYER CITY, STATE, ZIP CODE**

**X12 Segment Name:** Geographic Location

**X12 Purpose:** To specify the geographic place of the named party

**X12 Syntax:**

1. E0207
Only one of N402 or N407 may be present.

2. C0605
If N406 is present, then N405 is required.

3. C0704
If N407 is present, then N404 is required.

**Loop:** 2100D — MEMBER EMPLOYER

**Segment Repeat:** 1

**Usage:** SITUATIONAL

**Situational Rule:** Required when the member’s employer is not the sponsor and the employer address is provided to the sponsor by the member. If not required by this implementation guide, do not send.

**TR3 Example:** N4*KANSAS CITY*MO*64108~

## DIAGRAM

![img-21.jpeg](img-21.jpeg)

![img-22.jpeg](img-22.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N401 | 19 | City Name | O 1 AN 2/30  |
|   |  |  | Free-form text for city name |   |
|   |  |  | COMMENT: A combination of either N401 through N404, or N405 and N406 may be adequate to specify a location. |   |
|   |  |  | IMPLEMENTATION NAME: Member Employer City Name |   |

FEBRUARY 2011
105

005010X220 &amp; 005010X220A1 • 834 • 2100D • N4
MEMBER EMPLOYER CITY, STATE, ZIP CODE
CONSOLIDATED • 834

SITUATIONAL N402 156
State or Province Code X 1 ID 2/2
Code (Standard State/Province) as defined by appropriate government agency
SYNTAX: E0207
COMMENT: N402 is required only if city name (N401) is in the U.S. or Canada.

SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Member Employer State Code
CODE SOURCE 22: States and Provinces

SITUATIONAL N403 116
Postal Code O 1 ID 3/15
Code defining international postal zone code excluding punctuation and blanks (zip code for United States)

SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada, or when a postal code exists for the country in N404. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Member Employer Postal Zone or ZIP Code
CODE SOURCE 51: ZIP Code
CODE SOURCE 932: Universal Postal Codes

SITUATIONAL N404 26
Country Code X 1 ID 2/3
Code identifying the country
SYNTAX: C0704

SITUATIONAL RULE: Required when the address is outside the United States of America. If not required by this implementation guide, do not send.
CODE SOURCE 5: Countries, Currencies and Funds
Use the alpha-2 country codes from Part 1 of ISO 3166.

NOT USED N405 309
Location Qualifier X 1 ID 1/2

NOT USED N406 310
Location Identifier O 1 AN 1/30

SITUATIONAL N407 1715
Country Subdivision Code X 1 ID 1/3
Code identifying the country subdivision
SYNTAX: E0207, C0704

SITUATIONAL RULE: Required when the address is not in the United States of America, including its territories, or Canada, and the country in N404 has administrative subdivisions such as but not limited to states, provinces, cantons, etc. If not required by this implementation guide, do not send.
CODE SOURCE 5: Countries, Currencies and Funds
Use the country subdivision codes from Part 2 of ISO 3166.

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100E • NM1
MEMBER SCHOOL

## SEGMENT DETAIL

### NM1 - MEMBER SCHOOL

**X12 Segment Name:** Individual or Organizational Name
**X12 Purpose:** To supply the full name of an individual or organizational entity
**X12 Syntax:**
1. P0809
If either NM108 or NM109 is present, then the other is required.
2. C1110
If NM111 is present, then NM110 is required.
3. C1203
If NM112 is present, then NM103 is required.

**Loop:** 2100E — MEMBER SCHOOL
**Loop Repeat:** 3

**Segment Repeat:** 1

**Usage:** SITUATIONAL

**Situational Rule:** Required when the member is enrolled in school and the payer is required to be notified under the insurance contract between the sponsor and the payer. If not required by this implementation guide, do not send.

**TR3 Example:** NM1®M8®2®University of Utah~

## DIAGRAM

|  NM1 * | NM101 98
Entity ID Code
M 1 ID 2/3 | * | NM102 1065
Entity Type Qualifier
M 1 ID 1/1 | * | NM103 1035
Name Last/Org Name
X 1 AN 1/60 | * | NM104 1036
Name First
O 1 AN 1/35 | * | NM105 1037
Name Middle
O 1 AN 1/25 | * | NM106 1038
Name Prefix
O 1 AN 1/10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  * | NM107 1039
Name Suffix
O 1 AN 1/10 | * | NM108 66
ID Code Qualifier
X 1 ID 1/2 | * | NM109 67
ID Code
X 1 AN 2/80 | * | NM110 706
Entity Relat Code
X 1 ID 2/2 | * | NM111 98
Entity ID Code
O 1 ID 2/3 | * | NM112 1035
Name Last/Org Name
O 1 AN 1/60  |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | NM101 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | M8 Educational Institution |   |
|  REQUIRED | NM102 | 1065 | Entity Type Qualifier
Code qualifying the type of entity | M 1 ID 1/1  |
|   |  |  | SEMANTIC: NM102 qualifies NM103. |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 2 Non-Person Entity |   |

FEBRUARY 2011
107

005010X220 &amp; 005010X220A1 • 834 • 2100E • NM1
MEMBER SCHOOL
CONSOLIDATED • 834

|  REQUIRED | NM103 | 1035 | Name Last or Organization Name
Individual last name or organizational name
SYNTAX: C1203 | X 1 | AN | 1/60  |
| --- | --- | --- | --- | --- | --- | --- |
|  IMPLEMENTATION NAME: School Name  |   |   |   |   |   |   |
|  NOT USED | NM104 | 1036 | Name First | O 1 | AN | 1/35  |
|  NOT USED | NM105 | 1037 | Name Middle | O 1 | AN | 1/25  |
|  NOT USED | NM106 | 1038 | Name Prefix | O 1 | AN | 1/10  |
|  NOT USED | NM107 | 1039 | Name Suffix | O 1 | AN | 1/10  |
|  NOT USED | NM108 | 66 | Identification Code Qualifier | X 1 | ID | 1/2  |
|  NOT USED | NM109 | 67 | Identification Code | X 1 | AN | 2/80  |
|  NOT USED | NM110 | 706 | Entity Relationship Code | X 1 | ID | 2/2  |
|  NOT USED | NM111 | 98 | Entity Identifier Code | O 1 | ID | 2/3  |
|  NOT USED | NM112 | 1035 | Name Last or Organization Name | O 1 | AN | 1/60  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100E • PER
MEMBER SCHOOL COMMUNICATIONS NUMBERS

# SEGMENT DETAIL

## PER - MEMBER SCHOOL COMMUNICATIONS NUMBERS

**X12 Segment Name:** Administrative Communications Contact

**X12 Purpose:** To identify a person or office to whom administrative communications should be directed

**X12 Syntax:**

1. P0304
If either PER03 or PER04 is present, then the other is required.

2. P0506
If either PER05 or PER06 is present, then the other is required.

3. P0708
If either PER07 or PER08 is present, then the other is required.

**Loop:** 2100E — MEMBER SCHOOL

**Segment Repeat:** 1

**Usage:** SITUATIONAL

**Situational Rule:** Required when the Member School contact information is provided to the sponsor. If not required by this implementation guide, do not send.

**TR3 Notes:**

1. When the communication number represents a telephone number in the United States and other countries using the North American Dialing Plan (for voice, data, fax, etc.), the communication number always includes the area code and phone number using the format AAABBBCCCC, where AAA is the area code, BBB is the telephone number prefix, and CCCC is the telephone number (e.g. (534)224-2525 would be represented as 5342242525).

**TR3 Example:** PER*SK**TE*8001234567~

## DIAGRAM

![img-23.jpeg](img-23.jpeg)

FEBRUARY 2011
109

005010X220 &amp; 005010X220A1 • 834 • 2100E • PER

MEMBER SCHOOL COMMUNICATIONS NUMBERS

CONSOLIDATED • 834

ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | PER01 | 366 | Contact Function Code |   |   | M 1 | ID 2/2  |
|   |  |  | Code identifying the major duty or responsibility of the person or group named |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | SK | School Clerk |   |  |   |
|  SITUATIONAL | PER02 | 93 | Name |   |   | O 1 | AN 1/60  |
|   |  |  | Free-form name |   |   |  |   |
|   |  |  | SITUATIONAL RULE: Required if member school communication contact name is supplied by the member. If not required by this implementation guide, do not send. |   |   |  |   |
|   |  |  | IMPLEMENTATION NAME: Member School Communications Contact Name |   |   |  |   |
|  REQUIRED | PER03 | 365 | Communication Number Qualifier |   |   | X 1 | ID 2/2  |
|   |  |  | Code identifying the type of communication number |   |   |  |   |
|   |  |  | SYNTAX: P0304 |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | EM | Electronic Mail |   |  |   |
|   |  |  | EX | Telephone Extension |   |  |   |
|   |  |  | FX | Facsimile |   |  |   |
|   |  |  | TE | Telephone |   |  |   |
|  REQUIRED | PER04 | 364 | Communication Number |   |   | X 1 | AN 1/256  |
|   |  |  | Complete communications number including country or area code when applicable |   |   |  |   |
|   |  |  | SYNTAX: P0304 |   |   |  |   |
|  SITUATIONAL | PER05 | 365 | Communication Number Qualifier |   |   | X 1 | ID 2/2  |
|   |  |  | Code identifying the type of communication number |   |   |  |   |
|   |  |  | SYNTAX: P0506 |   |   |  |   |
|   |  |  | SITUATIONAL RULE: Required when a value is being reported in the PER06 element. If not required by this implementation guide, do not send. |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | EM | Electronic Mail |   |  |   |
|   |  |  | EX | Telephone Extension |   |  |   |
|   |  |  | FX | Facsimile |   |  |   |
|   |  |  | TE | Telephone |   |  |   |
|  SITUATIONAL | PER06 | 364 | Communication Number |   |   | X 1 | AN 1/256  |
|   |  |  | Complete communications number including country or area code when applicable |   |   |  |   |
|   |  |  | SYNTAX: P0506 |   |   |  |   |
|   |  |  | SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send. |   |   |  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100E • PER MEMBER SCHOOL COMMUNICATIONS NUMBERS

SITUATIONAL PER07 365 Communication Number Qualifier X 1 ID 2/2
Code identifying the type of communication number
SYNTAX: P0708
SITUATIONAL RULE: Required when a value is being reported in the PER08 element. If not required by this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  EM | Electronic Mail  |
|  EX | Telephone Extension  |
|  FX | Facsimile  |
|  TE | Telephone  |

SITUATIONAL PER08 364 Communication Number X 1 AN 1/256
Complete communications number including country or area code when applicable
SYNTAX: P0708
SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.

NOT USED PER09 443 Contact Inquiry Reference O 1 AN 1/20

FEBRUARY 2011
111

005010X220 &amp; 005010X220A1 • 834 • 2100E • N3
MEMBER SCHOOL STREET ADDRESS
CONSOLIDATED • 834

# SEGMENT DETAIL

# N3 - MEMBER SCHOOL STREET ADDRESS

X12 Segment Name: Party Location

X12 Purpose: To specify the location of the named party

Loop: 2100E — MEMBER SCHOOL

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the member is enrolled in school and the school address is provided to the sponsor by the member. If not required by this implementation guide, do not send.

TR3 Example: N3®P.O. Box 1234~

# DIAGRAM

![img-24.jpeg](img-24.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N301 | 166 | Address Information
Address information | M 1 AN 1/55  |
|   |  |  | IMPLEMENTATION NAME: School Address Line |   |
|  SITUATIONAL | N302 | 166 | Address Information
Address information | O 1 AN 1/55  |
|   |  |  | SITUATIONAL RULE: Required if a second address line exists. If not required by this implementation guide, do not send. |   |
|   |  |  | IMPLEMENTATION NAME: School Address Line |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100E • N4
MEMBER SCHOOL CITY, STATE, ZIP CODE

## SEGMENT DETAIL

**N4 - MEMBER SCHOOL CITY, STATE, ZIP CODE**

**X12 Segment Name:** Geographic Location

**X12 Purpose:** To specify the geographic place of the named party

**X12 Syntax:**

1. E0207
Only one of N402 or N407 may be present.

2. C0605
If N406 is present, then N405 is required.

3. C0704
If N407 is present, then N404 is required.

**Loop:** 2100E — MEMBER SCHOOL

**Segment Repeat:** 1

**Usage:** SITUATIONAL

**Situational Rule:** Required when the member is enrolled in school and the school address is provided to the sponsor by the member. If not required by this implementation guide, do not send.

**TR3 Example:** N4*KANSAS CITY*MO*64108~

## DIAGRAM

![img-25.jpeg](img-25.jpeg)

![img-26.jpeg](img-26.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N401 | 19 | City Name | O 1 AN 2/30  |
|   |  |  | Free-form text for city name |   |
|   |  |  | COMMENT: A combination of either N401 through N404, or N405 and N406 may be adequate to specify a location. |   |
|   |  |  | IMPLEMENTATION NAME: Member School City Name |   |

FEBRUARY 2011
113

005010X220 &amp; 005010X220A1 • 834 • 2100E • N4
MEMBER SCHOOL CITY, STATE, ZIP CODE
CONSOLIDATED • 834

|  SITUATIONAL | N402 | 156 | State or Province Code | X 1 ID | 2/2  |
| --- | --- | --- | --- | --- | --- |
|  Code (Standard State/Province) as defined by appropriate government agency  |   |   |   |   |   |
|  SYNTAX: E0207  |   |   |   |   |   |
|  COMMENT: N402 is required only if city name (N401) is in the U.S. or Canada.  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  IMPLEMENTATION NAME: Member School State Code  |   |   |   |   |   |
|  CODE SOURCE 22: States and Provinces  |   |   |   |   |   |
|  SITUATIONAL | N403 | 116 | Postal Code | O 1 ID | 3/15  |
|  Code defining international postal zone code excluding punctuation and blanks (zip code for United States)  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada, or when a postal code exists for the country in N404. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  IMPLEMENTATION NAME: Member School Postal Zone or ZIP Code  |   |   |   |   |   |
|  CODE SOURCE 51: ZIP Code  |   |   |   |   |   |
|  CODE SOURCE 932: Universal Postal Codes  |   |   |   |   |   |
|  SITUATIONAL | N404 | 26 | Country Code | X 1 ID | 2/3  |
|  Code identifying the country  |   |   |   |   |   |
|  SYNTAX: C0704  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is outside the United States of America. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  CODE SOURCE 5: Countries, Currencies and Funds  |   |   |   |   |   |
|  Use the alpha-2 country codes from Part 1 of ISO 3166.  |   |   |   |   |   |
|  NOT USED | N405 | 309 | Location Qualifier | X 1 ID | 1/2  |
|  NOT USED | N406 | 310 | Location Identifier | O 1 AN | 1/30  |
|  SITUATIONAL | N407 | 1715 | Country Subdivision Code | X 1 ID | 1/3  |
|  Code identifying the country subdivision  |   |   |   |   |   |
|  SYNTAX: E0207, C0704  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is not in the United States of America, including its territories, or Canada, and the country in N404 has administrative subdivisions such as but not limited to states, provinces, cantons, etc. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  CODE SOURCE 5: Countries, Currencies and Funds  |   |   |   |   |   |
|  Use the country subdivision codes from Part 2 of ISO 3166.  |   |   |   |   |   |

114
FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100F • NM1
CUSTODIAL PARENT

## SEGMENT DETAIL

### NM1 - CUSTODIAL PARENT

X12 Segment Name: Individual or Organizational Name

X12 Purpose: To supply the full name of an individual or organizational entity

X12 Syntax:
1. P0809
If either NM108 or NM109 is present, then the other is required.
2. C1110
If NM111 is present, then NM110 is required.
3. C1203
If NM112 is present, then NM103 is required.

Loop: 2100F — CUSTODIAL PARENT  Loop Repeat: 1

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the custodial parent of a minor dependent is someone other than the subscriber. If not required by this implementation guide, do not send.

TR3 Notes: 1. Any other situation, (examples: Guardianship, Legal Indemnity, Power of Attorney, and/or Separation Agreements) would be handled under the Responsible Party NM1 segment.

TR3 Example: NM1*S3*1*JONES*MARY~

## DIAGRAM

![img-27.jpeg](img-27.jpeg)

* NM1 *
NM101 98
Entity ID Code
M 1 ID 2/3

* NM102 1065
Entity Type Qualifier
M 1 ID 1/1

* NM103 1035
Name Last/ Org Name
X 1 AN 1/60

* NM104 1036
Name First
O 1 AN 1/35

* NM105 1037
Name Middle
O 1 AN 1/25

* NM106 1038
Name Prefix
O 1 AN 1/10

* NM107 1039
Name Suffix
O 1 AN 1/10

* NM108 66
ID Code Qualifier
X 1 ID 1/2

* NM109 67
ID Code
X 1 AN 2/80

* NM110 706
Entity Relat Code
X 1 ID 2/2

* NM111 98
Entity ID Code
O 1 ID 2/3

* NM112 1035
Name Last/ Org Name
O 1 AN 1/60

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | NM101 | 98 | Entity Identifier Code | M 1 ID 2/3  |
|   |  |  | Code identifying an organizational entity, a physical location, property or an individual |   |
|   |  | CODE | DEFINITION |   |
|   |  | S3 | Custodial Parent |   |

FEBRUARY 2011
115

005010X220 &amp; 005010X220A1 • 834 • 2100F • NM1
CONSOLIDATED • 834
CUSTODIAL PARENT

|  REQUIRED | NM102 | 1065 | Entity Type Qualifier
Code qualifying the type of entity
SEMANTIC: NM102 qualifies NM103.
CODE DEFINITION | M 1 ID | 1/1  |
| --- | --- | --- | --- | --- | --- |
|  REQUIRED | NM103 | 1035 | 1 Person
Name Last or Organization Name
Individual last name or organizational name
SYNTAX: C1203
IMPLEMENTATION NAME: Custodial Parent Last Name | X 1 AN | 1/60  |
|  REQUIRED | NM104 | 1036 | Name First
Individual first name
IMPLEMENTATION NAME: Custodial Parent First Name | O 1 AN | 1/35  |
|  SITUATIONAL | NM105 | 1037 | Name Middle
Individual middle name or initial
SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Custodial Parent Middle Name | O 1 AN | 1/25  |
|  SITUATIONAL | NM106 | 1038 | Name Prefix
Prefix to individual name
SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Custodial Parent Name Prefix | O 1 AN | 1/10  |
|  SITUATIONAL | NM107 | 1039 | Name Suffix
Suffix to individual name
SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Custodial Parent Name Suffix | O 1 AN | 1/10  |
|  SITUATIONAL | NM108 | 66 | Identification Code Qualifier
Code designating the system/method of code structure used for Identification Code (67)
SYNTAX: P0809
SITUATIONAL RULE: Required when a value is being reported in the NM109 element. If not required by this implementation guide, do not send.
CODE DEFINITION | X 1 ID | 1/2  |
|   |  |  | 34 Social Security Number
The social security number may not be used for any Federally administered programs such as Medicare or CHAMPUS/TRICARE. |  |   |
|   |  |  | ZZ Mutually Defined
Value is required if National Individual Identifier is mandated for use. Otherwise, one of the other listed codes may be used. |  |   |

116
FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100F • NM1
CUSTODIAL PARENT

SITUATIONAL NM109 67 Identification Code X 1 AN 2/80
Code identifying a party or other code
SYNTAX: P0809
SITUATIONAL RULE: Required when available, and allowed under confidentiality regulations. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Custodial Parent Identifier

|  NOT USED | NM110 | 706 | Entity Relationship Code | X 1 | ID | 2/2  |
| --- | --- | --- | --- | --- | --- | --- |
|  NOT USED | NM111 | 98 | Entity Identifier Code | O 1 | ID | 2/3  |
|  NOT USED | NM112 | 1035 | Name Last or Organization Name | O 1 | AN | 1/60  |

FEBRUARY 2011
117

005010X220 &amp; 005010X220A1 • 834 • 2100F • PER

CUSTODIAL PARENT COMMUNICATIONS NUMBERS

CONSOLIDATED • 834

# SEGMENT DETAIL

## PER - CUSTODIAL PARENT COMMUNICATIONS NUMBERS

X12 Segment Name: Administrative Communications Contact

X12 Purpose: To identify a person or office to whom administrative communications should be directed

X12 Syntax:
1. P0304
If either PER03 or PER04 is present, then the other is required.
2. P0506
If either PER05 or PER06 is present, then the other is required.
3. P0708
If either PER07 or PER08 is present, then the other is required.

Loop: 2100F — CUSTODIAL PARENT

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the Custodial Parent contact information is provided to the sponsor. If not required by this implementation guide, do not send.

TR3 Notes:
1. When the communication number represents a telephone number in the United States and other countries using the North American Dialing Plan (for voice, data, fax, etc.), the communication number always includes the area code and phone number using the format AAABBBCCCC, where AAA is the area code, BBB is the telephone number prefix, and CCCC is the telephone number (e.g. (534)224-2525 would be represented as 5342242525).

TR3 Example: PER*PQ**TE*8001234567~

# DIAGRAM

PER

|  PER01 | 366 | Contact | Funct Code | M 1 | ID | 2/2  |
| --- | --- | --- | --- | --- | --- | --- |
|  PER02 | 93 | Name | O 1 | AN | 1/60 |   |
|  PER03 | 365 | Comm | Number Qual | X 1 | ID | 2/2  |
|  PER04 | 364 | Comm | Number | X 1 | AN 1/256 |   |
|  PER05 | 365 | Comm | Number Qual | X 1 | ID | 2/2  |
|  PER06 | 364 | Comm | Number | X 1 | AN 1/256 |   |
|  PER07 | 365 | Comm | Number Qual | X 1 | ID | 2/2  |
| --- | --- | --- | --- | --- | --- | --- |
|  PER08 | 364 | Comm | Number | X 1 | AN 1/256 |   |
|  PER09 | 443 | Contact-Inq | Reference | O 1 | AN | 1/20  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100F • PER
CUSTODIAL PARENT COMMUNICATIONS NUMBERS

ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | PER01 | 366 | Contact Function Code |   |   | M 1 | ID 2/2  |
|   |  |  | Code identifying the major duty or responsibility of the person or group named |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | PQ | Parent or Guardian |   |  |   |
|  NOT USED | PER02 | 93 | Name |   |   | O 1 | AN 1/60  |
|  REQUIRED | PER03 | 365 | Communication Number Qualifier |   |   | X 1 | ID 2/2  |
|   |  |  | Code identifying the type of communication number |   |   |  |   |
|   |  |  | SYNTAX: P0304 |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | AP | Alternate Telephone |   |  |   |
|   |  |  | BN | Beeper Number |   |  |   |
|   |  |  | CP | Cellular Phone |   |  |   |
|   |  |  | EM | Electronic Mail |   |  |   |
|   |  |  | EX | Telephone Extension |   |  |   |
|   |  |  | FX | Facsimile |   |  |   |
|   |  |  | HP | Home Phone Number |   |  |   |
|   |  |  | TE | Telephone |   |  |   |
|   |  |  | WP | Work Phone Number |   |  |   |
|  REQUIRED | PER04 | 364 | Communication Number |   |   | X 1 | AN 1/256  |
|   |  |  | Complete communications number including country or area code when applicable |   |   |  |   |
|   |  |  | SYNTAX: P0304 |   |   |  |   |
|  SITUATIONAL | PER05 | 365 | Communication Number Qualifier |   |   | X 1 | ID 2/2  |
|   |  |  | Code identifying the type of communication number |   |   |  |   |
|   |  |  | SYNTAX: P0506 |   |   |  |   |
|   |  |  | SITUATIONAL RULE: Required when a value is being reported in the PER06 element. If not required by this implementation guide, do not send. |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | AP | Alternate Telephone |   |  |   |
|   |  |  | BN | Beeper Number |   |  |   |
|   |  |  | CP | Cellular Phone |   |  |   |
|   |  |  | EM | Electronic Mail |   |  |   |
|   |  |  | EX | Telephone Extension |   |  |   |
|   |  |  | FX | Facsimile |   |  |   |
|   |  |  | HP | Home Phone Number |   |  |   |
|   |  |  | TE | Telephone |   |  |   |
|   |  |  | WP | Work Phone Number |   |  |   |

FEBRUARY 2011
119

005010X220 &amp; 005010X220A1 • 834 • 2100F • PER

CUSTODIAL PARENT COMMUNICATIONS NUMBERS

CONSOLIDATED • 834

|  SITUATIONAL | PER06 | 364 | Communication Number | X 1 | AN | 1/256  |
| --- | --- | --- | --- | --- | --- | --- |
|   |  |  | Complete communications number including country or area code when applicable  |   |   |   |
|   |  |  | SYNTAX: P0506 |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.  |   |   |   |
|  SITUATIONAL | PER07 | 365 | Communication Number Qualifier | X 1 | ID | 2/2  |
|   |  |  | Code identifying the type of communication number  |   |   |   |
|   |  |  | SYNTAX: P0708 |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when a value is being reported in the PER08 element. If not required by this implementation guide, do not send.  |   |   |   |
|   |  |  | CODE | DEFINITION |  |   |
|   |  |  | AP | Alternate Telephone |  |   |
|   |  |  | BN | Beeper Number |  |   |
|   |  |  | CP | Cellular Phone |  |   |
|   |  |  | EM | Electronic Mail |  |   |
|   |  |  | EX | Telephone Extension |  |   |
|   |  |  | HP | Home Phone Number |  |   |
|   |  |  | TE | Telephone |  |   |
|   |  |  | WP | Work Phone Number |  |   |
|  SITUATIONAL | PER08 | 364 | Communication Number | X 1 | AN | 1/256  |
|   |  |  | Complete communications number including country or area code when applicable  |   |   |   |
|   |  |  | SYNTAX: P0708 |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.  |   |   |   |
|  NOT USED | PER09 | 443 | Contact Inquiry Reference | O 1 | AN | 1/20  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100F • N3
CUSTODIAL PARENT STREET ADDRESS

## SEGMENT DETAIL

### N3 - CUSTODIAL PARENT STREET ADDRESS

X12 Segment Name: Party Location

X12 Purpose: To specify the location of the named party

Loop: 2100F — CUSTODIAL PARENT

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the custodial parent of a minor dependent is someone other than the subscriber and the information is provided to the sponsor. If not required by this implementation guide, do not send.

TR3 Example: N3*50 ORCHARD STREET~

## DIAGRAM

N3 * N301 166
Address Information
M 1 AN 1/55

* N302 166
Address Information
O 1 AN 1/55

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | N301 | 166 | Address Information
Address information | M 1 | AN | 1/55  |
|   |  |  | IMPLEMENTATION NAME: Custodial Parent Address Line  |   |   |   |
|  SITUATIONAL | N302 | 166 | Address Information
Address information | O 1 | AN | 1/55  |
|   |  |  | SITUATIONAL RULE: Required if a second address line exists. If not required by this implementation guide, do not send.  |   |   |   |
|   |  |  | IMPLEMENTATION NAME: Custodial Parent Address Line  |   |   |   |

FEBRUARY 2011
121

005010X220 &amp; 005010X220A1 • 834 • 2100F • N4

CUSTODIAL PARENT CITY, STATE, ZIP CODE

CONSOLIDATED • 834

## SEGMENT DETAIL

### N4 - CUSTODIAL PARENT CITY, STATE, ZIP CODE

X12 Segment Name: Geographic Location

X12 Purpose: To specify the geographic place of the named party

X12 Syntax:

1. E0207
Only one of N402 or N407 may be present.

2. C0605
If N406 is present, then N405 is required.

3. C0704
If N407 is present, then N404 is required.

Loop: 2100F — CUSTODIAL PARENT

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the custodial parent of a minor dependent is someone other than the subscriber and the information is provided to the sponsor. If not required by this implementation guide, do not send.

TR3 Example: N4*KANSAS CITY*MO*64108~

## DIAGRAM

![img-28.jpeg](img-28.jpeg)

N4

N401 19
City Name
O 1 AN 2/30

N402 156
State or Prov Code
X 1 ID 2/2

N403 116
Postal Code
O 1 ID 3/15

N404 26
Country Code
X 1 ID 2/3

N405 309
Location Qualifier
X 1 ID 1/2

N406 310
Location Identifier
O 1 AN 1/30

N407 1715
Country Sub Code
X 1 ID 1/3

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N401 | 19 | City Name | O 1 AN 2/30  |
|   |  |  | Free-form text for city name |   |
|   |  |  | COMMENT: A combination of either N401 through N404, or N405 and N406 may be adequate to specify a location. |   |
|   |  |  | IMPLEMENTATION NAME: Custodial Parent City Name |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100F • N4
CUSTODIAL PARENT CITY, STATE, ZIP CODE

SITUATIONAL N402 156
State or Province Code X 1 ID 2/2
Code (Standard State/Province) as defined by appropriate government agency
SYNTAX: E0207
COMMENT: N402 is required only if city name (N401) is in the U.S. or Canada.

SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Custodial Parent State Code
CODE SOURCE 22: States and Provinces

SITUATIONAL N403 116
Postal Code O 1 ID 3/15
Code defining international postal zone code excluding punctuation and blanks (zip code for United States)

SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada, or when a postal code exists for the country in N404. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Custodial Parent Postal Zone or ZIP Code
CODE SOURCE 51: ZIP Code
CODE SOURCE 932: Universal Postal Codes

SITUATIONAL N404 26
Country Code X 1 ID 2/3
Code identifying the country
SYNTAX: C0704

SITUATIONAL RULE: Required when the address is outside the United States of America. If not required by this implementation guide, do not send.
CODE SOURCE 5: Countries, Currencies and Funds
Use the alpha-2 country codes from Part 1 of ISO 3166.

NOT USED N405 309
Location Qualifier X 1 ID 1/2

NOT USED N406 310
Location Identifier O 1 AN 1/30

SITUATIONAL N407 1715
Country Subdivision Code X 1 ID 1/3
Code identifying the country subdivision
SYNTAX: E0207, C0704

SITUATIONAL RULE: Required when the address is not in the United States of America, including its territories, or Canada, and the country in N404 has administrative subdivisions such as but not limited to states, provinces, cantons, etc. If not required by this implementation guide, do not send.
CODE SOURCE 5: Countries, Currencies and Funds
Use the country subdivision codes from Part 2 of ISO 3166.

FEBRUARY 2011
123

005010X220 &amp; 005010X220A1 • 834 • 2100G • NM1
RESPONSIBLE PERSON
CONSOLIDATED • 834

# SEGMENT DETAIL

# NM1 - RESPONSIBLE PERSON

X12 Segment Name: Individual or Organizational Name

X12 Purpose: To supply the full name of an individual or organizational entity

X12 Syntax: 1. P0809
If either NM108 or NM109 is present, then the other is required.

2. C1110
If NM111 is present, then NM110 is required.

3. C1203
If NM112 is present, then NM103 is required.

Loop: 2100G — RESPONSIBLE PERSON Loop Repeat: 13

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required to identify the person(s), other than the subscriber, who are responsible for the member. If not required by this implementation guide, do not send.

TR3 Example: NM1*QD*1*CASE*JOHN~

# DIAGRAM

# NM1

|  NM101 | 98 | NM102 | 1065 | NM103 | 1035 | NM104 | 1036 | NM105 | 1037 | NM106 | 1038  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Entity ID Code | M 1 | ID | 1/1 | Name Last/ Org Name | X 1 | AN | 1/60 | Name First | O 1 | AN | 1/25  |
|  M 107 | 1039 | NM108 | 66 | NM109 | 67 | NM110 | 706 | NM111 | 98 | NM112 | 1035  |
|  Name Suffix | O 1 | AN | 1/10 | ID Code Qualifier | X 1 | ID | 1/2 | Entity Relative Code | X 1 | ID | 2/2  |
|  M 110 | 102 | 103 | 104 | Entity Relative Code | X 1 | ID | 2/2 | Entity ID Code | O 1 | ID | 2/3  |

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | NM101 | 98 | Entity Identifier Code | M 1 ID 2/3  |
|   |  |  | Code identifying an organizational entity, a physical location, property or an individual |   |
|  CODE | DEFINITION  |
| --- | --- |
|  6Y | Case Manager  |
|  9K | Key Person  |
|  E1 | Person or Other Entity Legally Responsible for a Child  |
|   | Used to identify a legal indemnity situation.  |
|   | This code is used when a Qualified Medical Child Support Order (QMSCO) is present.  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100G • NM1
RESPONSIBLE PERSON

|  REQUIRED | NM102 | 1065 | EI | Executor of Estate  |
| --- | --- | --- | --- | --- |
|   |   |   |   |  This is used when the subscriber is deceased and the executor/responsible party is other than a surviving spouse.  |
|   |   |   |  EXS | Ex-spouse  |
|   |   |   |   |  This is used to identify a separated spouse under a separation agreement, or that the member is the divorced spouse and self responsible. This is NOT USED to identify the custodial parent for dependent children after a divorce.  |
|   |   |   |  GB | Other Insured  |
|   |   |   |  GD | Guardian  |
|   |   |   |  J6 | Power of Attorney  |
|   |   |   |  LR | Legal Representative  |
|   |   |   |  QD | Responsible Party  |
|   |   |   |  S1 | Parent  |
|   |   |   |  TZ | Significant Other  |
|   |   |   |  X4 | Spouse  |
|   |   |   |  Entity Type Qualifier | M 1 ID 1/1  |
|  Code qualifying the type of entity
SEMANTIC: NM102 qualifies NM103.
CODE DEFINITION  |   |   |   |   |
|  REQUIRED | NM103 | 1035 | 1 | Person  |
|   |   |   |  Name Last or Organization Name | X 1 AN 1/60  |
|   |   |   |  Individual last name or organizational name
SYNTAX: C1203 |   |
|  SITUATIONAL | NM104 | 1036 | IMPLEMENTATION NAME: Responsible Party Last or Organization Name  |   |
|   |   |   |  Name First | O 1 AN 1/35  |
|   |   |   |  Individual first name |   |
|   |   |   |  SITUATIONAL RULE: Required when NM102 is equal to “1” (person) and the person has a first name. If not required by this implementation guide, do not send. |   |
|  SITUATIONAL | NM105 | 1037 | IMPLEMENTATION NAME: Responsible Party First Name  |   |
|   |   |   |  Name Middle | O 1 AN 1/25  |
|   |   |   |  Individual middle name or initial |   |
|   |   |   |  SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send. |   |
|  SITUATIONAL | NM106 | 1038 | IMPLEMENTATION NAME: Responsible Party Middle Name  |   |
|   |   |   |  Name Prefix | O 1 AN 1/10  |
|   |   |   |  Prefix to individual name |   |
|   |   |   |  SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send. |   |

FEBRUARY 2011
125

005010X220 &amp; 005010X220A1 • 834 • 2100G • NM1
RESPONSIBLE PERSON
CONSOLIDATED • 834

|  SITUATIONAL | NM107 | 1039 | Name Suffix
Suffix to individual name | O 1 | AN | 1/10  |
| --- | --- | --- | --- | --- | --- | --- |
|  SITUATIONAL | NM108 | 66 | SITUATIONAL RULE: Required if supplied by member. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Responsible Party Suffix Name  |   |   |   |
|   |   |   |  Identification Code Qualifier
Code designating the system/method of code structure used for Identification Code (67)
SYNTAX: P0809 | X 1 | ID | 1/2  |
|  SITUATIONAL | NM109 | 67 | SITUATIONAL RULE: Required when a value is being reported in the NM109 element. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Responsible Party Identifier  |   |   |   |
|   |   |   |  Identification Code
Code identifying a party or other code | X 1 | AN | 2/80  |
|   |   |   |  SYNTAX: P0809 |  |  |   |
|  NOT USED | NM110 | 706 | Entity Relationship Code | X 1 | ID | 2/2  |
|  NOT USED | NM111 | 98 | Entity Identifier Code | O 1 | ID | 2/3  |
|  NOT USED | NM112 | 1035 | Name Last or Organization Name | O 1 | AN | 1/60  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100G • PER
RESPONSIBLE PERSON COMMUNICATIONS NUMBERS

# SEGMENT DETAIL

## PER - RESPONSIBLE PERSON COMMUNICATIONS NUMBERS

**X12 Segment Name:** Administrative Communications Contact

**X12 Purpose:** To identify a person or office to whom administrative communications should be directed

**X12 Syntax:**
1. P0304
If either PER03 or PER04 is present, then the other is required.
2. P0506
If either PER05 or PER06 is present, then the other is required.
3. P0708
If either PER07 or PER08 is present, then the other is required.

**Loop:** 2100G — RESPONSIBLE PERSON

**Segment Repeat:** 1

**Usage:** SITUATIONAL

**Situational Rule:** Required when the Responsible Person contact information is provided to the sponsor. If not required by this implementation guide, do not send.

**TR3 Notes:**
1. When the communication number represents a telephone number in the United States and other countries using the North American Dialing Plan (for voice, data, fax, etc.), the communication number always includes the area code and phone number using the format AAABBBCCCC, where AAA is the area code, BBB is the telephone number prefix, and CCCC is the telephone number (e.g. (534)224-2525 would be represented as 5342242525).

**TR3 Example:** PER*RP**HP*8015554321~

# DIAGRAM

![img-29.jpeg](img-29.jpeg)

FEBRUARY 2011
127

005010X220 &amp; 005010X220A1 • 834 • 2100G • PER
RESPONSIBLE PERSON COMMUNICATIONS NUMBERS
CONSOLIDATED • 834

ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | PER01 | 366 | Contact Function Code |   |   | M 1 | ID 2/2  |
|   |  |  | Code identifying the major duty or responsibility of the person or group named |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | RP | Responsible Person |   |  |   |
|  NOT USED | PER02 | 93 | Name |   |   | O 1 | AN 1/60  |
|  REQUIRED | PER03 | 365 | Communication Number Qualifier |   |   | X 1 | ID 2/2  |
|   |  |  | Code identifying the type of communication number |   |   |  |   |
|   |  |  | SYNTAX: P0304 |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | AP | Alternate Telephone |   |  |   |
|   |  |  | BN | Beeper Number |   |  |   |
|   |  |  | CP | Cellular Phone |   |  |   |
|   |  |  | EM | Electronic Mail |   |  |   |
|   |  |  | EX | Telephone Extension |   |  |   |
|   |  |  | FX | Facsimile |   |  |   |
|   |  |  | HP | Home Phone Number |   |  |   |
|   |  |  | TE | Telephone |   |  |   |
|   |  |  | WP | Work Phone Number |   |  |   |
|  REQUIRED | PER04 | 364 | Communication Number |   |   | X 1 | AN 1/256  |
|   |  |  | Complete communications number including country or area code when applicable |   |   |  |   |
|   |  |  | SYNTAX: P0304 |   |   |  |   |
|  SITUATIONAL | PER05 | 365 | Communication Number Qualifier |   |   | X 1 | ID 2/2  |
|   |  |  | Code identifying the type of communication number |   |   |  |   |
|   |  |  | SYNTAX: P0506 |   |   |  |   |
|   |  |  | SITUATIONAL RULE: Required when a value is being reported in the PER06 element. If not required by this implementation guide, do not send. |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | AP | Alternate Telephone |   |  |   |
|   |  |  | BN | Beeper Number |   |  |   |
|   |  |  | CP | Cellular Phone |   |  |   |
|   |  |  | EM | Electronic Mail |   |  |   |
|   |  |  | EX | Telephone Extension |   |  |   |
|   |  |  | FX | Facsimile |   |  |   |
|   |  |  | HP | Home Phone Number |   |  |   |
|   |  |  | TE | Telephone |   |  |   |
|   |  |  | WP | Work Phone Number |   |  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100G • PER
RESPONSIBLE PERSON COMMUNICATIONS NUMBERS

SITUATIONAL PER06 364 Communication Number X 1 AN 1/256
Complete communications number including country or area code when applicable
SYNTAX: P0506

SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.

SITUATIONAL PER07 365 Communication Number Qualifier X 1 ID 2/2
Code identifying the type of communication number
SYNTAX: P0708

SITUATIONAL RULE: Required when a value is being reported in the PER08 element. If not required by this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  AP | Alternate Telephone  |
|  BN | Beeper Number  |
|  CP | Cellular Phone  |
|  EM | Electronic Mail  |
|  EX | Telephone Extension  |
|  FX | Facsimile  |
|  HP | Home Phone Number  |
|  TE | Telephone  |
|  WP | Work Phone Number  |

SITUATIONAL PER08 364 Communication Number X 1 AN 1/256
Complete communications number including country or area code when applicable
SYNTAX: P0708

SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.

NOT USED PER09 443 Contact Inquiry Reference O 1 AN 1/20

FEBRUARY 2011
129

005010X220 &amp; 005010X220A1 • 834 • 2100G • N3
RESPONSIBLE PERSON STREET ADDRESS
CONSOLIDATED • 834

# SEGMENT DETAIL

# N3 - RESPONSIBLE PERSON STREET ADDRESS

X12 Segment Name: Party Location

X12 Purpose: To specify the location of the named party

Loop: 2100G — RESPONSIBLE PERSON

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when there is a person other than the subscriber who is responsible for the member and the responsible person's address is provided to the sponsor. If not required by this implementation guide, do not send.

TR3 Example: N3®50 ORCHARD STREET~

# DIAGRAM

![img-30.jpeg](img-30.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N301 | 166 | Address Information
Address information | M 1 AN 1/55  |
|   |  |  | IMPLEMENTATION NAME: Responsible Party Address Line  |   |
|  SITUATIONAL | N302 | 166 | Address Information
Address information | O 1 AN 1/55  |
|   |  |  | SITUATIONAL RULE: Required if a second address line exists. If not required by this implementation guide, do not send.  |   |
|   |  |  | IMPLEMENTATION NAME: Responsible Party Address Line  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100G • N4
RESPONSIBLE PERSON CITY, STATE, ZIP CODE

## SEGMENT DETAIL

### N4 - RESPONSIBLE PERSON CITY, STATE, ZIP CODE

**X12 Segment Name:** Geographic Location

**X12 Purpose:** To specify the geographic place of the named party

**X12 Syntax:**

1. E0207
Only one of N402 or N407 may be present.

2. C0605
If N406 is present, then N405 is required.

3. C0704
If N407 is present, then N404 is required.

**Loop:** 2100G — RESPONSIBLE PERSON

**Segment Repeat:** 1

**Usage:** SITUATIONAL

**Situational Rule:** Required when there is a person other than the subscriber who is responsible for the member and the responsible person’s address is provided to the sponsor. If not required by this implementation guide, do not send.

**TR3 Example:** N4*KANSAS CITY*MO*64108~

## DIAGRAM

![img-31.jpeg](img-31.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N401 | 19 | City Name
Free-form text for city name | O 1 AN 2/30  |
|   |  |  | COMMENT: A combination of either N401 through N404, or N405 and N406 may be adequate to specify a location.  |   |
|   |  |  | IMPLEMENTATION NAME: Responsible Person City Name  |   |

FEBRUARY 2011
131

005010X220 &amp; 005010X220A1 • 834 • 2100G • N4
RESPONSIBLE PERSON CITY, STATE, ZIP CODE
CONSOLIDATED • 834

|  SITUATIONAL | N402 | 156 | State or Province Code | X 1 ID | 2/2  |
| --- | --- | --- | --- | --- | --- |
|  Code (Standard State/Province) as defined by appropriate government agency  |   |   |   |   |   |
|  SYNTAX: E0207  |   |   |   |   |   |
|  COMMENT: N402 is required only if city name (N401) is in the U.S. or Canada.  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  IMPLEMENTATION NAME: Responsible Person State Code  |   |   |   |   |   |
|  CODE SOURCE 22: States and Provinces  |   |   |   |   |   |
|  SITUATIONAL | N403 | 116 | Postal Code | O 1 ID | 3/15  |
|  Code defining international postal zone code excluding punctuation and blanks (zip code for United States)  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada, or when a postal code exists for the country in N404. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  IMPLEMENTATION NAME: Responsible Person Postal Zone or ZIP Code  |   |   |   |   |   |
|  CODE SOURCE 51: ZIP Code  |   |   |   |   |   |
|  CODE SOURCE 932: Universal Postal Codes  |   |   |   |   |   |
|  SITUATIONAL | N404 | 26 | Country Code | X 1 ID | 2/3  |
|  Code identifying the country  |   |   |   |   |   |
|  SYNTAX: C0704  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is outside the United States of America. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  CODE SOURCE 5: Countries, Currencies and Funds  |   |   |   |   |   |
|  Use the alpha-2 country codes from Part 1 of ISO 3166.  |   |   |   |   |   |
|  NOT USED | N405 | 309 | Location Qualifier | X 1 ID | 1/2  |
|  NOT USED | N406 | 310 | Location Identifier | O 1 AN | 1/30  |
|  SITUATIONAL | N407 | 1715 | Country Subdivision Code | X 1 ID | 1/3  |
|  Code identifying the country subdivision  |   |   |   |   |   |
|  SYNTAX: E0207, C0704  |   |   |   |   |   |
|  SITUATIONAL RULE: Required when the address is not in the United States of America, including its territories, or Canada, and the country in N404 has administrative subdivisions such as but not limited to states, provinces, cantons, etc. If not required by this implementation guide, do not send.  |   |   |   |   |   |
|  CODE SOURCE 5: Countries, Currencies and Funds  |   |   |   |   |   |
|  Use the country subdivision codes from Part 2 of ISO 3166.  |   |   |   |   |   |

132
FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100H • NM1
DROP OFF LOCATION

## SEGMENT DETAIL

### NM1 - DROP OFF LOCATION

X12 Segment Name: Individual or Organizational Name

X12 Purpose: To supply the full name of an individual or organizational entity

X12 Syntax:
1. P0809
If either NM108 or NM109 is present, then the other is required.
2. C1110
If NM111 is present, then NM110 is required.
3. C1203
If NM112 is present, then NM103 is required.

Loop: 2100H — DROP OFF LOCATION  Loop Repeat: 1

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when member has requested shipments to be sent to an address other than their residence or mailing. If not required by this implementation guide, do not send.

TR3 Example: NM1*45*1*CASE*JOHN~

## DIAGRAM

|  NM1 * | NM101 98
Entity ID
Code
M 1 ID 2/3 | * | NM102 1065
Entity Type
Qualifier
M 1 ID 1/1 | * | NM103 1035
Name Last/
Org Name
X 1 AN 1/60 | * | NM104 1036
Name
First
O 1 AN 1/35 | * | NM105 1037
Name
Middle
O 1 AN 1/25 | * | NM106 1038
Name
Prefix
O 1 AN 1/10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  * | NM107 1039
Name
Suffix
O 1 AN 1/10 | * | NM108 66
ID Code
Qualifier
X 1 ID 1/2 | * | NM109 67
ID
Code
X 1 AN 2/80 | * | NM110 706
Entity
Relat Code
X 1 ID 2/2 | * | NM111 98
Entity ID
Code
O 1 ID 2/3 | * | NM112 1035
Name Last/
Org Name
O 1 AN 1/60  |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | NM101 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 45 Drop-off Location |   |
|  REQUIRED | NM102 | 1065 | Entity Type Qualifier
Code qualifying the type of entity | M 1 ID 1/1  |
|   |  |  | SEMANTIC: NM102 qualifies NM103. |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 1 Person |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 2100H • NM1
DROP OFF LOCATION
CONSOLIDATED • 834

|  SITUATIONAL | NM103 | 1035 | Name Last or Organization Name
Individual last name or organizational name
SYNTAX: C1203 | X 1 | AN | 1/60  |
| --- | --- | --- | --- | --- | --- | --- |
|  SITUATIONAL RULE: Required if supplied by the member. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  SITUATIONAL | NM104 | 1036 | Name First
Individual first name | O 1 | AN | 1/35  |
|  SITUATIONAL RULE: Required if supplied by the member. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  SITUATIONAL | NM105 | 1037 | Name Middle
Individual middle name or initial | O 1 | AN | 1/25  |
|  SITUATIONAL RULE: Required if supplied by the member. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  SITUATIONAL | NM106 | 1038 | Name Prefix
Prefix to individual name | O 1 | AN | 1/10  |
|  SITUATIONAL RULE: Required if supplied by the member. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  SITUATIONAL | NM107 | 1039 | Name Suffix
Suffix to individual name | O 1 | AN | 1/10  |
|  SITUATIONAL RULE: Required if supplied by the member. If not required by this implementation guide, do not send.  |   |   |   |   |   |   |
|  NOT USED | NM108 | 66 | Identification Code Qualifier | X 1 | ID | 1/2  |
|  NOT USED | NM109 | 67 | Identification Code | X 1 | AN | 2/80  |
|  NOT USED | NM110 | 706 | Entity Relationship Code | X 1 | ID | 2/2  |
|  NOT USED | NM111 | 98 | Entity Identifier Code | O 1 | ID | 2/3  |
|  NOT USED | NM112 | 1035 | Name Last or Organization Name | O 1 | AN | 1/60  |

134
FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100H • N3
DROP OFF LOCATION STREET ADDRESS

## SEGMENT DETAIL

### N3 - DROP OFF LOCATION STREET ADDRESS

X12 Segment Name: Party Location

X12 Purpose: To specify the location of the named party

Loop: 2100H — DROP OFF LOCATION

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when member has requested shipments to be sent to an address other than their residence or mailing. If not required by this implementation guide, do not send.

TR3 Example: N3®50 ORCHARD STREET~

## DIAGRAM

![img-32.jpeg](img-32.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N301 | 166 | Address Information
Address information | M 1 AN 1/55  |
|   |  |  | IMPLEMENTATION NAME: Drop Off Location Address Line  |   |
|  SITUATIONAL | N302 | 166 | Address Information
Address information | O 1 AN 1/55  |
|   |  |  | SITUATIONAL RULE: Required if a second address line exists. If not required by this implementation guide, do not send.  |   |
|   |  |  | IMPLEMENTATION NAME: Drop Off Location Address Line  |   |

FEBRUARY 2011
135

005010X220 &amp; 005010X220A1 • 834 • 2100H • N4 DROP OFF LOCATION CITY, STATE, ZIP CODE

CONSOLIDATED • 834

## SEGMENT DETAIL

### N4 - DROP OFF LOCATION CITY, STATE, ZIP CODE

X12 Segment Name: Geographic Location

X12 Purpose: To specify the geographic place of the named party

X12 Syntax:
1. E0207
Only one of N402 or N407 may be present.
2. C0605
If N406 is present, then N405 is required.
3. C0704
If N407 is present, then N404 is required.

Loop: 2100H — DROP OFF LOCATION

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when member has requested shipments to be sent to an address other than their residence or mailing. If not required by this implementation guide, do not send.

TR3 Example: N4*KANSAS CITY*MO*64108~

## DIAGRAM

![img-33.jpeg](img-33.jpeg)

![img-34.jpeg](img-34.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N401 | 19 | City Name
Free-form text for city name | O 1 AN 2/30  |
|   |  |  | COMMENT: A combination of either N401 through N404, or N405 and N406 may be adequate to specify a location.  |   |
|   |  |  | IMPLEMENTATION NAME: Drop Off Location City Name  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2100H • N4 DROP OFF LOCATION CITY, STATE, ZIP CODE

SITUATIONAL N402 156
State or Province Code X 1 ID 2/2
Code (Standard State/Province) as defined by appropriate government agency
SYNTAX: E0207
COMMENT: N402 is required only if city name (N401) is in the U.S. or Canada.

SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Drop Off Location State Code
CODE SOURCE 22: States and Provinces

SITUATIONAL N403 116
Postal Code O 1 ID 3/15
Code defining international postal zone code excluding punctuation and blanks (zip code for United States)

SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada, or when a postal code exists for the country in N404. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Drop Off Location Postal Zone or ZIP Code
CODE SOURCE 51: ZIP Code
CODE SOURCE 932: Universal Postal Codes

SITUATIONAL N404 26
Country Code X 1 ID 2/3
Code identifying the country
SYNTAX: C0704

SITUATIONAL RULE: Required when the address is outside the United States of America. If not required by this implementation guide, do not send.
CODE SOURCE 5: Countries, Currencies and Funds
Use the alpha-2 country codes from Part 1 of ISO 3166.

NOT USED N405 309
Location Qualifier X 1 ID 1/2

NOT USED N406 310
Location Identifier O 1 AN 1/30

SITUATIONAL N407 1715
Country Subdivision Code X 1 ID 1/3
Code identifying the country subdivision
SYNTAX: E0207, C0704

SITUATIONAL RULE: Required when the address is not in the United States of America, including its territories, or Canada, and the country in N404 has administrative subdivisions such as but not limited to states, provinces, cantons, etc. If not required by this implementation guide, do not send.
CODE SOURCE 5: Countries, Currencies and Funds
Use the country subdivision codes from Part 2 of ISO 3166.

FEBRUARY 2011
137

005010X220 &amp; 005010X220A1 • 834 • 2200 • DSB
DISABILITY INFORMATION
CONSOLIDATED • 834

# SEGMENT DETAIL

# DSB - DISABILITY INFORMATION

X12 Segment Name: Disability Information

X12 Purpose: To supply disability information

X12 Syntax: 1. P0708

If either DSB07 or DSB08 is present, then the other is required.

Loop: 2200 — DISABILITY INFORMATION Loop Repeat: &gt;1

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when enrolling a disabled member or when disability information about an existing member is added or changed. If not required by this implementation guide, do not send.

TR3 Example: DSB*2***DX*585~

# DIAGRAM

DSB
* DSB01 1146
* Disability Type Code
* M 1 ID 1/1
* DSB02 380
* Quantity
* O 1 R 1/15
* DSB03 1149
* Occupation Code
* O 1 ID 4/6
* DSB04 1154
* Work-Inty Code
* O 1 ID 1/1
* DSB05 1161
* Product Option-Code
* O 1 ID 1/2
* DSB06 782
* Monetary Amount
* O 1 R 1/18

* DSB07 235
* Prod/Serv ID Qual
* X 1 ID 2/2
* DSB08 1137
* Medical Code Value
* X 1 AN 1/15

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   | ATTRIBUTES  |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | DSB01 | 1146 | Disability Type Code |   | M 1 | ID | 1/1  |
|   |   |   |  Code identifying the disability status of the individual |   |  |  |   |
|   |   |   |  CODE | DEFINITION |  |  |   |
|   |   |   |  1 | Short Term Disability |  |  |   |
|   |   |   |  2 | Long Term Disability |  |  |   |
|   |   |   |  3 | Permanent or Total Disability |  |  |   |
|   |   |   |  4 | No Disability |  |  |   |
|  NOT USED | DSB02 | 380 | Quantity |   | O 1 | R | 1/15  |
|  NOT USED | DSB03 | 1149 | Occupation Code |   | O 1 | ID | 4/6  |
|  NOT USED | DSB04 | 1154 | Work Intensity Code |   | O 1 | ID | 1/1  |
|  NOT USED | DSB05 | 1161 | Product Option Code |   | O 1 | ID | 1/2  |
|  NOT USED | DSB06 | 782 | Monetary Amount |   | O 1 | R | 1/18  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2200 • DSB
DISABILITY INFORMATION

SITUATIONAL DSB07 235
Product/Service ID Qualifier X 1 ID 2/2
Code identifying the type/source of the descriptive number used in Product/Service ID (234)
SYNTAX: P0708
SITUATIONAL RULE: Required when a value is being reported in the DSB08 element. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Product or Service ID Qualifier

|  CODE | DEFINITION  |
| --- | --- |
|  DX | International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM) - Diagnosis  |
|  ZZ | CODE SOURCE 131: International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM)
Mutually Defined  |
|   | To be used for the International Classification of Diseases, 10th Revision, Clinical Modification (ICD-10-CM) - Diagnosis.  |
|   | CODE SOURCE: 897 International Classification of Diseases, 10th Revision, Clinical Modification (ICD-10-CM)  |

SITUATIONAL DSB08 1137
Medical Code Value X 1 AN 1/15
Code value for describing a medical condition or procedure
SYNTAX: P0708
SEMANTIC: DSB08 is the functional status code for the disability.
SITUATIONAL RULE: Required when called for in the insurance contract between the sponsor and payer and allowed by federal and state regulations. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Diagnosis Code

FEBRUARY 2011
139

005010X220 &amp; 005010X220A1 • 834 • 2200 • DTP
DISABILITY ELIGIBILITY DATES
CONSOLIDATED • 834

# SEGMENT DETAIL

## DTP - DISABILITY ELIGIBILITY DATES

X12 Segment Name: Date or Time or Period

X12 Purpose: To specify any or all of a date, a time, or a time period

Loop: 2200 — DISABILITY INFORMATION

Segment Repeat: 2

Usage: SITUATIONAL

Situational Rule: Required when enrolling a disabled member or when disability dates change for an existing member, and the disability dates are known by the sponsor. If not required by this implementation guide, do not send.

TR3 Notes: 1. This segment is used to send the first and last date of disability.

TR3 Example: DTP*360*D8*19961001~

# DIAGRAM

DTP * DTP01 374
Date/Time Qualifier
M 1 ID 3/3

* DTP02 1250
Date Time Format Qual
M 1 ID 2/3

* DTP03 1251
Date Time Period
M 1 AN 1/35

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | DTP01 | 374 | Date/Time Qualifier
Code specifying type of date or time, or both date and time | M 1 ID 3/3  |
|   |  |  | IMPLEMENTATION NAME: Date Time Qualifier |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 360 Initial Disability Period Start |   |
|   |  |  | 361 Initial Disability Period End |   |
|  REQUIRED | DTP02 | 1250 | Date Time Period Format Qualifier
Code indicating the date format, time format, or date and time format | M 1 ID 2/3  |
|   |  |  | SEMANTIC: DTP02 is the date or time or period format that will appear in DTP03. |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | D8 Date Expressed in Format CCYYMMDD |   |
|  REQUIRED | DTP03 | 1251 | Date Time Period
Expression of a date, a time, or range of dates, times or dates and times | M 1 AN 1/35  |
|   |  |  | IMPLEMENTATION NAME: Disability Eligibility Date |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2300 • HD
HEALTH COVERAGE

## SEGMENT DETAIL

### HD - HEALTH COVERAGE

X12 Segment Name: Health Coverage
X12 Purpose: To provide information on health coverage
Loop: 2300 — HEALTH COVERAGE  Loop Repeat: 99
Segment Repeat: 1
Usage: SITUATIONAL
Situational Rule: Required when enrolling a new member or when adding, updating, removing coverage or auditing an existing member. If not required by this implementation guide, do not send.
TR3 Notes: 1. Refer to section 1.4.4 “Termination” for additional information relative to removing a member’s coverage.
TR3 Example: HD*021**HLT*PLAN A BCD*FAM~

## DIAGRAM

![img-35.jpeg](img-35.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | HD01 | 875 | Maintenance Type Code
Code identifying the specific type of item maintenance | M 1 ID 3/3  |
|  Required to identify the specific type of item maintenance.  |   |   |   |   |
|  CODE DEFINITION  |   |   |   |   |
|  001 | Change  |   |   |   |
|  002 | Delete  |   |   |   |
|  Use this code for deleting an incorrect coverage record.  |   |   |   |   |
|  021 | Addition  |   |   |   |
|  024 | Cancellation or Termination  |   |   |   |
|  Use this code for cancelling/terminating a coverage.  |   |   |   |   |
|  025 | Reinstatement  |   |   |   |
|  026 | Correction  |   |   |   |
|  This code is used to correct an incorrect record.  |   |   |   |   |

FEBRUARY 2011
141

005010X220 &amp; 005010X220A1 • 834 • 2300 • HD
HEALTH COVERAGE
CONSOLIDATED • 834

|   |  |  | 030 | Audit or Compare |  |   |
| --- | --- | --- | --- | --- | --- | --- |
|   |  |  | 032 | Employee Information Not Applicable |  |   |
|   |  |  |  | Certain situations, such as military duty and CHAMPUS/TRICARE, classify the subscriber as ineligible for coverage or benefits. However, dependents of the subscribers are still eligible for coverage or benefits under the subscriber. Subscriber identifying elements are needed to accurately identify dependents. |  |   |
|  NOT USED | HD02 | 1203 | Maintenance Reason Code | O 1 | ID | 2/3  |
|  REQUIRED | HD03 | 1205 | Insurance Line Code | O 1 | ID | 2/3  |
|   |  |  | Code identifying a group of insurance products |  |  |   |
|   |  |  | CODE | DEFINITION |  |   |
|   |  |  | AG | Preventative Care/Wellness |  |   |
|   |  |  | AH | 24 Hour Care |  |   |
|   |  |  | AJ | Medicare Risk |  |   |
|   |  |  | AK | Mental Health |  |   |
|   |  |  | DCP | Dental Capitation |  |   |
|   |  |  |  | This identifies a dental managed care organization (DMO). |  |   |
|   |  |  | DEN | Dental |  |   |
|   |  |  | EPO | Exclusive Provider Organization |  |   |
|   |  |  | FAC | Facility |  |   |
|   |  |  | HE | Hearing |  |   |
|   |  |  | HLT | Health |  |   |
|   |  |  |  | Includes both hospital and professional coverage. |  |   |
|   |  |  | HMO | Health Maintenance Organization |  |   |
|   |  |  | LTC | Long-Term Care |  |   |
|   |  |  | LTD | Long-Term Disability |  |   |
|   |  |  | MM | Major Medical |  |   |
|   |  |  | MOD | Mail Order Drug |  |   |
|   |  |  | PDG | Prescription Drug |  |   |
|   |  |  | POS | Point of Service |  |   |
|   |  |  | PPO | Preferred Provider Organization |  |   |
|   |  |  | PRA | Practitioners |  |   |
|   |  |  | STD | Short-Term Disability |  |   |
|   |  |  | UR | Utilization Review |  |   |
|   |  |  | VIS | Vision |  |   |
|  SITUATIONAL | HD04 | 1204 | Plan Coverage Description | O 1 | AN | 1/50  |
|   |  |  | A description or number that identifies the plan or coverage |  |  |   |
|   |  |  | SITUATIONAL RULE: Required when additional information is needed to describe the exact type of coverage being provided. If not required by this implementation guide, do not send. |  |  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2300 • HD
HEALTH COVERAGE

SITUATIONAL HD05 1207
Coverage Level Code
O 1 ID 3/3
Code indicating the level of coverage being provided for this insured

SITUATIONAL RULE: Required when called for in the insurance contract between the sponsor and payer and allowed by federal and state regulations. If not required by this implementation guide, do not send.

See section 1.4.6, Coverage Levels and Dependents, for additional information.

|  CODE | DEFINITION  |
| --- | --- |
|  CHD | Children Only  |
|  DEP | Dependents Only  |
|  E1D | Employee and One Dependent  |
|  For this code, the dependent is a non-spouse dependent. This code is not used for identification of Employee and Spouse. See code ESP.  |   |
|  E2D | Employee and Two Dependents  |
|  E3D | Employee and Three Dependents  |
|  E5D | Employee and One or More Dependents  |
|  E6D | Employee and Two or More Dependents  |
|  E7D | Employee and Three or More Dependents  |
|  E8D | Employee and Four or More Dependents  |
|  E9D | Employee and Five or More Dependents  |
|  ECH | Employee and Children  |
|  EMP | Employee Only  |
|  ESP | Employee and Spouse  |
|  FAM | Family  |
|  IND | Individual  |
|  SPC | Spouse and Children  |
|  SPO | Spouse Only  |
|  TWO | Two Party  |

NOT USED HD06 609
NOT USED HD07 609
NOT USED HD08 1209
SITUATIONAL HD09 1073

Count O 1 N0 1/9
Count O 1 N0 1/9
Underwriting Decision Code O 1 ID 1/1
Yes/No Condition or Response Code O 1 ID 1/1

Code indicating a Yes or No condition or response

SEMANTIC: HD09 is a late enrollee indicator. A "Y" value indicates the insured is a late enrollee, which can result in a reduction of benefits; an "N" value indicates the insured is a regular enrollee.

SITUATIONAL RULE: Required when there is a need to designate a member as a late enrollee. If not required by this implementation guide, do not send.

IMPLEMENTATION NAME: Late Enrollment Indicator

|  CODE | DEFINITION  |
| --- | --- |
|  N | No  |
|  Y | Yes  |

FEBRUARY 2011
143

005010X220 &amp; 005010X220A1 • 834 • 2300 • HD
HEALTH COVERAGE
CONSOLIDATED • 834

|  NOT USED | HD10 | 1211 | Drug House Code | O 1 | ID | 2/3  |
| --- | --- | --- | --- | --- | --- | --- |
|  NOT USED | HD11 | 1073 | Yes/No Condition or Response Code | O 1 | ID | 1/1  |

144
FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2300 • DTP
HEALTH COVERAGE DATES

## SEGMENT DETAIL

### DTP - HEALTH COVERAGE DATES

X12 Segment Name: Date or Time or Period

X12 Purpose: To specify any or all of a date, a time, or a time period

Loop: 2300 — HEALTH COVERAGE

Segment Repeat: 6

Usage: REQUIRED

TR3 Example: DTP※348※D8※19961001~

## DIAGRAM

![img-36.jpeg](img-36.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | DTP01 | 374 | Date/Time Qualifier
Code specifying type of date or time, or both date and time | M 1 ID 3/3  |
|   |  |  | IMPLEMENTATION NAME: Date Time Qualifier |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 300 Enrollment Signature Date |   |
|   |  |  | 303 Maintenance Effective |   |
|   |  |  | This is the effective date of a change where a member’s coverage is not being added or removed. |   |
|   |  |  | 343 Premium Paid to Date End |   |
|   |  |  | 348 Benefit Begin |   |
|   |  |  | This is the effective date of coverage. This code must always be sent when adding or reinstating coverage. |   |
|   |  |  | 349 Benefit End |   |
|   |  |  | The termination date represents the last date of coverage in which claims will be paid for the individual being terminated. For example, if a date of 02/28/2001 is passed then claims for this individual will be paid through 11:59 p.m. on 2/28/01. |   |
|   |  |  | 543 Last Premium Paid Date |   |
|   |  |  | 695 Previous Period |   |
|   |  |  | This value is only to be used when reporting Previous Coverage Months. |   |

FEBRUARY 2011
145

005010X220 &amp; 005010X220A1 • 834 • 2300 • DTP
HEALTH COVERAGE DATES
CONSOLIDATED • 834

|  REQUIRED | DTP02 | 1250 | Date Time Period Format Qualifier | M 1 ID | 2/3  |
| --- | --- | --- | --- | --- | --- |
|   |  |  | Code indicating the date format, time format, or date and time format  |   |   |
|   |  |  | SEMANTIC: DTP02 is the date or time or period format that will appear in DTP03.  |   |   |
|   |  |  | CODE | DEFINITION |   |
|   |  |  | D8 | Date Expressed in Format CCYYMMDD |   |
|   |  |  | RD8 | Range of Dates Expressed in Format CCYYMMDD-CCYYMMDD |   |
|   |  |  |  | This value is only to be used when reporting Previous Coverage Months. |   |
|  REQUIRED | DTP03 | 1251 | Date Time Period | M 1 AN | 1/35  |
|   |  |  | Expression of a date, a time, or range of dates, times or dates and times  |   |   |
|   |  |  | IMPLEMENTATION NAME: Coverage Period  |   |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2300 • AMT
HEALTH COVERAGE POLICY

## SEGMENT DETAIL

### AMT - HEALTH COVERAGE POLICY

X12 Segment Name: Monetary Amount Information

X12 Purpose: To indicate the total monetary amount

Loop: 2300 — HEALTH COVERAGE

Segment Repeat: 9

Usage: SITUATIONAL

Situational Rule: Required when such transmission is required under the insurance contract between the sponsor and the payer. If not required by this implementation guide, do not send.

TR3 Example: AMT%C1%20~

## DIAGRAM

AMT * AMT01 522 Amount Qual Code M 1 ID 1/3 * AMT02 782 Monetary Amount M 1 R 1/18 * AMT03 478 Cred/Debit Flag Code O 1 ID 1/1

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | AMT01 | 522 | Amount Qualifier Code
Code to qualify amount |   |   | M 1 | ID 1/3  |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | B9 | Co-insurance - Actual |   |  |   |
|   |  |  |  | This will contain any co-insurance selection amount.
The option of adjusting this amount to produce the actual co-insurance can be defined in the insurance contract. |   |  |   |
|   |  |  | C1 | Co-Payment Amount |   |  |   |
|   |  |  | D2 | Deductible Amount |   |  |   |
|   |  |  | EBA | Expected Expenditure Amount |   |  |   |
|   |  |  | FK | Other Unlisted Amount |   |  |   |
|   |  |  | P3 | Premium Amount |   |  |   |
|   |  |  | R | Spend Down |   |  |   |
|  REQUIRED | AMT02 | 782 | Monetary Amount
Monetary amount |   | M 1 | R | 1/18  |
|   |  |  | IMPLEMENTATION NAME: Contract Amount  |   |   |   |   |
|  NOT USED | AMT03 | 478 | Credit/Debit Flag Code |   | O 1 | ID | 1/1  |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 2300 • REF
HEALTH COVERAGE POLICY NUMBER
CONSOLIDATED • 834

# SEGMENT DETAIL

# REF - HEALTH COVERAGE POLICY NUMBER

X12 Segment Name: Reference Information

X12 Purpose: To specify identifying information

X12 Syntax: 1. R0203

At least one of REF02 or REF03 is required.

Loop: 2300 — HEALTH COVERAGE

Segment Repeat: 14

Usage: SITUATIONAL

Situational Rule: Required when such transmission is required under the Trading Partner Agreement between the sponsor and the payer. If not required by this implementation guide, do not send.

TR3 Example: REF*1L*123456~

# DIAGRAM

REF * REF01 128 Reference Ident Qual M 1 ID 2/3 * REF02 127 Reference Ident X 1 AN 1/50 * REF03 352 Description X 1 AN 1/80 * REF04 C040 Reference Identifier O 1

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | REF01 | 128 | Reference Identification Qualifier Code qualifying the Reference Identification | M 1 ID 2/3  |
|  CODE | DEFINITION  |
| --- | --- |
|  17 | Client Reporting Category  |
|  1L | Group or Policy Number  |
|   | Required when a group number that applies to this individual's participation in the coverage passed in this HD loop is required by the terms of the contract between the sponsor (sender) and payer (receiver); if not required may be sent at the sender's discretion.  |
|  9V | Payment Category  |
|  CE | Class of Contract Code  |
|  E8 | Service Contract (Coverage) Number  |
|  M7 | Medical Assistance Category  |
|  PID | Program Identification Number  |
|  RB | Rate code number  |
|  X9 | Internal Control Number  |
|  XM | Issuer Number  |
|  XX1 | Special Program Code  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2300 • REF
HEALTH COVERAGE POLICY NUMBER

|   |  |  | XX2 | Service Area Code |   |
| --- | --- | --- | --- | --- | --- |
|   |  |  | ZX | County Code |   |
|   |  |  | ZZ | Mutually Defined |   |
|   |  |  |  | Use this code for the Payment Plan Type Code
(Annual or Quarterly) until a standard code is assigned. |   |
|  REQUIRED | REF02 | 127 | Reference Identification | X 1 AN 1/50 |   |
|   |  |  | Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier |   |   |
|   |  |  | SYNTAX: R0203 |   |   |
|   |  |  | IMPLEMENTATION NAME: Member Group or Policy Number |   |   |
|  NOT USED | REF03 | 352 | Description | X 1 AN 1/80 |   |
|  NOT USED | REF04 | C040 | REFERENCE IDENTIFIER | O 1 |   |

FEBRUARY 2011
149

005010X220 &amp; 005010X220A1 • 834 • 2300 • REF PRIOR COVERAGE MONTHS

CONSOLIDATED • 834

## SEGMENT DETAIL

# REF - PRIOR COVERAGE MONTHS

X12 Segment Name: Reference Information

X12 Purpose: To specify identifying information

X12 Syntax: 1. R0203

At least one of REF02 or REF03 is required.

Loop: 2300 — HEALTH COVERAGE

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the portability provisions of the Health Insurance Portability and Accountability Act require reporting of the number of months of prior health coverage that meet the certification requirements of the Act.

TR3 Example: REF*QQ*0~

## DIAGRAM

REF *

|  REF01 | 128 | Reference Ident Qual | M 1 | ID | 2/3  |
| --- | --- | --- | --- | --- | --- |
|  REF02 | 127 | Reference Ident | X 1 | AN | 1/50  |
|  REF03 | 352 | Description | X 1 | AN | 1/80  |
|  REF04 | C040 | Reference Identifier | O 1 | -  |   |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | REF01 | 128 | Reference Identification Qualifier
Code qualifying the Reference Identification | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | QQ Unit Number |   |
|   |  |  | This code is used in this implementation guide to indicate that the value in REF02 is the response required under the portability provisions of HIPAA.  |   |
|  REQUIRED | REF02 | 127 | Reference Identification X 1 AN 1/50
Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier
SYNTAX: R0203  |   |
|   |  |  | IMPLEMENTATION NAME: Prior Coverage Month Count  |   |
|   |  |  | Indicator identifying the number of prior months insurance coverage that may apply under the portability provisions of the Health Insurance Portability and Accountability Act.  |   |
|   |  |  | This field will contain the number of months of prior health insurance coverage that meets the portability requirements of the HIPAA certification requirements. To be sent on new enrollments when available.  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2300 • REF
PRIOR COVERAGE MONTHS

|  NOT USED | REF03 | 352 | Description | X 1 | AN | 1/80  |
| --- | --- | --- | --- | --- | --- | --- |
|  NOT USED | REF04 | C040 | REFERENCE IDENTIFIER | O 1 |  |   |

FEBRUARY 2011
151

005010X220 &amp; 005010X220A1 • 834 • 2300 • IDC
IDENTIFICATION CARD
CONSOLIDATED • 834

## SEGMENT DETAIL

# IDC - IDENTIFICATION CARD

X12 Segment Name: Identification Card

X12 Purpose: To provide notification to produce replacement identification card(s)

Loop: 2300 — HEALTH COVERAGE

Segment Repeat: 3

Usage: SITUATIONAL

Situational Rule: Required when requesting the production of an identification card as the result of an enrollment add, change, or statement. If not required by this implementation guide, do not send.

TR3 Notes: 1. An enrollment statement refers to a situation where no change is being made to the enrollment except to request a replacement ID card.

TR3 Example: IDC®12345®H~

## DIAGRAM

![img-37.jpeg](img-37.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | IDC01 | 1204 | Plan Coverage Description
A description or number that identifies the plan or coverage | M 1 AN 1/50  |
|   |  |  | If no additional information is needed, this element will be sent as a single zero. |   |
|  REQUIRED | IDC02 | 1215 | Identification Card Type Code
Code identifying the type of identification card | M 1 ID 1/1  |
|   |  |  | This code is used to identify that the card issued will be specific to the coverage identified in the related HD segment. |   |
|   |  |  | CODE | DEFINITION  |
|   |  |  | D | Dental Insurance  |
|   |  |  | H | Health Insurance  |
|   |  |  | P | Prescription Drug Service Drug Insurance  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2300 • IDC
IDENTIFICATION CARD

|  SITUATIONAL | IDC03 | 380 | Quantity
Numeric value of quantity | O 1 R 1/15  |
| --- | --- | --- | --- | --- |
|  SEMANTIC: IDC03 is the number of cards being requested.  |   |   |   |   |
|  SITUATIONAL RULE: Required if the number of card requests is greater than 1. If not required by this implementation guide, do not send.  |   |   |   |   |
|  IMPLEMENTATION NAME: Identification Card Count  |   |   |   |   |
|  Only non-negative integer values are to be sent.  |   |   |   |   |
|  SITUATIONAL | IDC04 | 306 | Action Code
Code indicating type of action | O 1 ID 1/2  |
|  SEMANTIC: IDC04 is the reason for the card being requested, i.e., add or a change.  |   |   |   |   |
|  SITUATIONAL RULE: Required if the sender knows the reason for the card request. If not required by this implementation guide, do not send.  |   |   |   |   |
|  CODE |   |   | DEFINITION  |   |
|  1 |   |   | Add  |   |
|  2 |   |   | Change (Update)  |   |
|  RX |   |   | Replace  |   |
|  Use when requesting replacement cards with no change to data.  |   |   |   |   |

FEBRUARY 2011
153

005010X220 &amp; 005010X220A1 • 834 • 2310 • LX
PROVIDER INFORMATION
CONSOLIDATED • 834

# SEGMENT DETAIL

## LX - PROVIDER INFORMATION

X12 Segment Name: Transaction Set Line Number

X12 Purpose: To reference a line number in a transaction set

X12 Set Notes: 1. Loop 2310 contains information about the primary care providers for the subscriber or the dependent, and about the beneficiaries of any employer-sponsored life insurance for the subscriber.

Loop: 2310 — PROVIDER INFORMATION Loop Repeat: 30

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required to provide information about the primary care or capitated physicians and pharmacies chosen by the enrollee in a managed care plan when that selection is made through the sponsor. If not required by this implementation guide, do not send.

TR3 Notes: 1. Use one iteration of the loop to identify each applicable health care service provider.

2. The primary care provider effective date is defaulted to the effective date of the product identified in the DTP segment of the 2300 loop. When an enrollee switches from one primary care provider to another through the sponsor, the new provider must be listed with the effective date of change.

TR3 Example: LX*1~

# DIAGRAM

LX *

|  LX01 | 554  |
| --- | --- |
|  Assigned Number  |   |
|  M 1 | N0 1/6  |

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | LX01 | 554 | Assigned Number | M 1 N0 1/6  |
|   |  |  | Number assigned for differentiation within a transaction set |   |
|   |  |  | This is a sequential number representing the number of loops for this insured person. Begin with 1 for each insured person.  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2310 • NM1
PROVIDER NAME

## SEGMENT DETAIL

### NM1 - PROVIDER NAME

**X12 Segment Name:** Individual or Organizational Name

**X12 Purpose:** To supply the full name of an individual or organizational entity

**X12 Set Notes:**
1. Either NM1 or N1 will be included depending on whether an individual or organization is being specified.

**X12 Syntax:**
1. P0809
If either NM108 or NM109 is present, then the other is required.
2. C1110
If NM111 is present, then NM110 is required.
3. C1203
If NM112 is present, then NM103 is required.

**Loop:** 2310 — PROVIDER INFORMATION

**Segment Repeat:** 1

**Usage:** REQUIRED

**TR3 Notes:**
1. The National Provider ID must be passed in NM109. Until that ID is available, the Federal Taxpayer’s Identification Number or another identification number that is necessary to identify the entity must be sent if available. If the identification number is not available then the Provider’s Name must be passed using elements NM103 through NM107 as outlined in segment note 2.

**TR3 Example:** NM1*P3*1***SV*25341234567*25~

## DIAGRAM

![img-38.jpeg](img-38.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | NM101 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual | M 1 ID 2/3  |
|   |  | CODE | DEFINITION |   |
|   |  | 1X | Laboratory |   |
|   |  | 3D | Obstetrics and Gynecology Facility |   |

FEBRUARY 2011
155

005010X220 &amp; 005010X220A1 • 834 • 2310 • NM1
PROVIDER NAME
CONSOLIDATED • 834

|   |  | 80 | Hospital |  |   |
| --- | --- | --- | --- | --- | --- |
|   |  | FA | Facility |  |   |
|   |  | OD | Doctor of Optometry |  |   |
|   |  | P3 | Primary Care Provider |  |   |
|   |  | QA | Pharmacy |  |   |
|   |  | QN | Dentist |  |   |
|   |  | Y2 | Managed Care Organization |  |   |
|  REQUIRED | NM102 | 1065 | Entity Type Qualifier | M 1 | ID  |
|   |  |  | Code qualifying the type of entity |  |   |
|   |  |  | SEMANTIC: NM102 qualifies NM103. |  |   |
|   |  |  | CODE | DEFINITION |   |
|   |  |  | 1 | Person |   |
|   |  |  | 2 | Non-Person Entity |   |
|  SITUATIONAL | NM103 | 1035 | Name Last or Organization Name | X 1 | AN  |
|   |  |  | Individual last name or organizational name |  | 1/60  |
|   |  |  | SYNTAX: C1203 |  |   |
|   |  |  | SITUATIONAL RULE: Required when NM102 is equal to ‘1’ or ‘2’ and the sponsor is not able to provide the standard ID in element NM109. If not required by this implementation guide, do not send. |  |   |
|   |  |  | IMPLEMENTATION NAME: Provider Last or Organization Name |  |   |
|  SITUATIONAL | NM104 | 1036 | Name First | O 1 | AN  |
|   |  |  | Individual first name |  | 1/35  |
|   |  |  | SITUATIONAL RULE: Required when NM102 is equal to ‘1’ and the sponsor is not able to provide the standard ID in element NM109. If not required by this implementation guide, do not send. |  |   |
|   |  |  | IMPLEMENTATION NAME: Provider First Name |  |   |
|  SITUATIONAL | NM105 | 1037 | Name Middle | O 1 | AN  |
|   |  |  | Individual middle name or initial |  | 1/25  |
|   |  |  | SITUATIONAL RULE: Required when NM102 is equal to ‘1’ and the sponsor is not able to provide the standard ID in element NM109 and has this information. If not required by this implementation guide, do not send. |  |   |
|   |  |  | IMPLEMENTATION NAME: Provider Middle Name |  |   |
|  SITUATIONAL | NM106 | 1038 | Name Prefix | O 1 | AN  |
|   |  |  | Prefix to individual name |  | 1/10  |
|   |  |  | SITUATIONAL RULE: Required when NM102 is equal to ‘1’ and the sponsor is not able to provide the standard ID in element NM109 and has this information. If not required by this implementation guide, do not send. |  |   |
|   |  |  | IMPLEMENTATION NAME: Provider Name Prefix |  |   |

156
FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2310 • NM1
PROVIDER NAME

SITUATIONAL NM107 1039 Name Suffix O 1 AN 1/10
Suffix to individual name

SITUATIONAL RULE: Required when NM102 is equal to ‘1’ and the sponsor is not able to provide the standard ID in element NM109 and has this information. If not required by this implementation guide, do not send.

IMPLEMENTATION NAME: Provider Name Suffix

SITUATIONAL NM108 66 Identification Code Qualifier X 1 ID 1/2
Code designating the system/method of code structure used for Identification Code (67)
SYNTAX: P0809

SITUATIONAL RULE: Required for providers in the United States or its territories when the provider has received an NPI. If not required by this implementation guide, do not send.

SITUATIONAL NM109 67 Code Definition
34 Social Security Number
The social security number may not be used for any Federally administered programs such as Medicare or CHAMPUS/TRICARE.
FI Federal Taxpayer’s Identification Number
SV Service Provider Number
This is a number assigned by the payer used to identify a provider.
XX Centers for Medicare and Medicaid Services National Provider Identifier
CODE SOURCE 537: Centers for Medicare &amp; Medicaid Services National Provider Identifier
Identification Code X 1 AN 2/80
Code identifying a party or other code

REQUIRED NM110 706 Entity Relationship Code X 1 ID 2/2
Code describing entity relationship
SYNTAX: C1110
COMMENT: NM110 and NM111 further define the type of entity in NM101.

This element indicates whether or not the member is an existing patient of the provider.

NOTE DEFINITION
25 Established Patient
26 Not Established Patient
72 Unknown

NOT USED NM111 98 Entity Identifier Code O 1 ID 2/3
NOT USED NM112 1035 Name Last or Organization Name O 1 AN 1/60

FEBRUARY 2011 157

005010X220 &amp; 005010X220A1 • 834 • 2310 • N3
PROVIDER ADDRESS
CONSOLIDATED • 834

# SEGMENT DETAIL

# N3 - PROVIDER ADDRESS

X12 Segment Name: Party Location

X12 Purpose: To specify the location of the named party

Loop: 2310 — PROVIDER INFORMATION

Segment Repeat: 2

Usage: SITUATIONAL

Situational Rule: Required when the location of the named provider needs to be reported. If not required by this implementation guide, do not send.

TR3 Example: N3®50 ORCHARD STREET~

# DIAGRAM

N3 * N301 166
Address Information
M 1 AN 1/55

* N302 166
Address Information
O 1 AN 1/55

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N301 | 166 | Address Information
Address information | M 1 AN 1/55  |
|   |  |  | IMPLEMENTATION NAME: Provider Address Line |   |
|  SITUATIONAL | N302 | 166 | Address Information
Address information | O 1 AN 1/55  |
|   |  |  | SITUATIONAL RULE: Required if a second address line exists. If not required by this implementation guide, do not send. |   |
|   |  |  | IMPLEMENTATION NAME: Provider Address Line |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2310 • N4
PROVIDER CITY, STATE, ZIP CODE

## SEGMENT DETAIL

### N4 - PROVIDER CITY, STATE, ZIP CODE

**X12 Segment Name:** Geographic Location

**X12 Purpose:** To specify the geographic place of the named party

**X12 Syntax:**

1. E0207
Only one of N402 or N407 may be present.

2. C0605
If N406 is present, then N405 is required.

3. C0704
If N407 is present, then N404 is required.

**Loop:** 2310 — PROVIDER INFORMATION

**Segment Repeat:** 1

**Usage:** SITUATIONAL

**Situational Rule:** Required when the location of the named provider needs to be reported. If not required by this implementation guide, do not send.

**TR3 Example:** N4*KANSAS CITY*MO*64108~

## DIAGRAM

### N4 *

|  N401 | 19 | City Name | O 1 | AN | 2/30 | *  |
| --- | --- | --- | --- | --- | --- | --- |
|  N402 | 156 | State or Prov Code | X 1 | ID | 2/2 | *  |
|  N403 | 116 | Postal Code | O 1 | ID | 3/15 | *  |
|  N404 | 26 | Country Code | X 1 | ID | 2/3 | *  |
|  N405 | 309 | Location Qualifier | X 1 | ID | 1/2 | *  |
|  N406 | 310 | Location Identifier | O 1 | AN | 1/30 |   |

* N407 1715
Country Sub Code
X 1 ID 1/3

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N401 | 19 | City Name
Free-form text for city name | O 1 AN 2/30  |
|  COMMENT: A combination of either N401 through N404, or N405 and N406 may be adequate to specify a location.  |   |   |   |   |
|  IMPLEMENTATION NAME: Provider City Name  |   |   |   |   |

FEBRUARY 2011
159

005010X220 &amp; 005010X220A1 • 834 • 2310 • N4
PROVIDER CITY, STATE, ZIP CODE
CONSOLIDATED • 834

SITUATIONAL N402 156
State or Province Code X 1 ID 2/2
Code (Standard State/Province) as defined by appropriate government agency
SYNTAX: E0207
COMMENT: N402 is required only if city name (N401) is in the U.S. or Canada.

SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Provider State Code
CODE SOURCE 22: States and Provinces

SITUATIONAL N403 116
Postal Code O 1 ID 3/15
Code defining international postal zone code excluding punctuation and blanks (zip code for United States)

SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada, or when a postal code exists for the country in N404. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Provider Postal Zone or ZIP Code
CODE SOURCE 51: ZIP Code
CODE SOURCE 932: Universal Postal Codes

SITUATIONAL N404 26
Country Code X 1 ID 2/3
Code identifying the country
SYNTAX: C0704

SITUATIONAL RULE: Required when the address is outside the United States of America. If not required by this implementation guide, do not send.
CODE SOURCE 5: Countries, Currencies and Funds
Use the alpha-2 country codes from Part 1 of ISO 3166.

NOT USED N405 309
Location Qualifier X 1 ID 1/2

NOT USED N406 310
Location Identifier O 1 AN 1/30

SITUATIONAL N407 1715
Country Subdivision Code X 1 ID 1/3
Code identifying the country subdivision
SYNTAX: E0207, C0704

SITUATIONAL RULE: Required when the address is not in the United States of America, including its territories, or Canada, and the country in N404 has administrative subdivisions such as but not limited to states, provinces, cantons, etc. If not required by this implementation guide, do not send.
CODE SOURCE 5: Countries, Currencies and Funds
Use the country subdivision codes from Part 2 of ISO 3166.

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2310 • PER
PROVIDER COMMUNICATIONS NUMBERS

# SEGMENT DETAIL

# PER - PROVIDER COMMUNICATIONS NUMBERS

X12 Segment Name: Administrative Communications Contact

X12 Purpose: To identify a person or office to whom administrative communications should be directed

X12 Syntax:
1. P0304
If either PER03 or PER04 is present, then the other is required.
2. P0506
If either PER05 or PER06 is present, then the other is required.
3. P0708
If either PER07 or PER08 is present, then the other is required.

Loop: 2310 — PROVIDER INFORMATION

Segment Repeat: 2

Usage: SITUATIONAL

Situational Rule: Required when the Provider contact information is provided to the sponsor. If not required by this implementation guide, do not send.

TR3 Notes:
1. When the communication number represents a telephone number in the United States and other countries using the North American Dialing Plan (for voice, data, fax, etc.), the communication number always includes the area code and phone number using the format AAABBBCCCC, where AAA is the area code, BBB is the telephone number prefix, and CCCC is the telephone number (e.g. (534)224-2525 would be represented as 5342242525).

TR3 Example: PER®IC®HP®8015554321~

# DIAGRAM

PER
|  PER01 | 366 | Contact | Funct Code | M 1 | ID | 2/2  |
| --- | --- | --- | --- | --- | --- | --- |
|  PER02 | 93 | Name | O 1 | AN | 1/60 |   |
|  PER03 | 365 | Comm | Number Qual | X 1 | ID | 2/2  |
|  PER04 | 364 | Comm | Number | X 1 | AN 1/256 |   |
|  PER05 | 365 | Comm | Number Qual | X 1 | ID | 2/2  |
|  PER06 | 364 | Comm | Number | X 1 | AN 1/256 |   |
|  PER07 | 365 | Comm | Number Qual | X 1 | ID | 2/2  |
| --- | --- | --- | --- | --- | --- | --- |
|  PER08 | 364 | Comm | Number | X 1 | AN 1/256 |   |
|  PER09 | 443 | Contact-Inq | Reference | O 1 | AN | 1/20  |

FEBRUARY 2011
161

005010X220 &amp; 005010X220A1 • 834 • 2310 • PER
PROVIDER COMMUNICATIONS NUMBERS
CONSOLIDATED • 834

ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | PER01 | 366 | Contact Function Code |   |   | M 1 | ID 2/2  |
|   |  |  | Code identifying the major duty or responsibility of the person or group named |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | IC | Information Contact |   |  |   |
|  NOT USED | PER02 | 93 | Name |   |   | O 1 | AN 1/60  |
|  REQUIRED | PER03 | 365 | Communication Number Qualifier |   |   | X 1 | ID 2/2  |
|   |  |  | Code identifying the type of communication number |   |   |  |   |
|   |  |  | SYNTAX: P0304 |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | AP | Alternate Telephone |   |  |   |
|   |  |  | BN | Beeper Number |   |  |   |
|   |  |  | CP | Cellular Phone |   |  |   |
|   |  |  | EM | Electronic Mail |   |  |   |
|   |  |  | EX | Telephone Extension |   |  |   |
|   |  |  | FX | Facsimile |   |  |   |
|   |  |  | HP | Home Phone Number |   |  |   |
|   |  |  | TE | Telephone |   |  |   |
|   |  |  | WP | Work Phone Number |   |  |   |
|  REQUIRED | PER04 | 364 | Communication Number |   |   | X 1 | AN 1/256  |
|   |  |  | Complete communications number including country or area code when applicable |   |   |  |   |
|   |  |  | SYNTAX: P0304 |   |   |  |   |
|  SITUATIONAL | PER05 | 365 | Communication Number Qualifier |   |   | X 1 | ID 2/2  |
|   |  |  | Code identifying the type of communication number |   |   |  |   |
|   |  |  | SYNTAX: P0506 |   |   |  |   |
|   |  |  | SITUATIONAL RULE: Required when a value is being reported in the PER06 element. If not required by this implementation guide, do not send. |   |   |  |   |
|   |  |  | CODE | DEFINITION |   |  |   |
|   |  |  | AP | Alternate Telephone |   |  |   |
|   |  |  | BN | Beeper Number |   |  |   |
|   |  |  | CP | Cellular Phone |   |  |   |
|   |  |  | EM | Electronic Mail |   |  |   |
|   |  |  | EX | Telephone Extension |   |  |   |
|   |  |  | FX | Facsimile |   |  |   |
|   |  |  | HP | Home Phone Number |   |  |   |
|   |  |  | TE | Telephone |   |  |   |
|   |  |  | WP | Work Phone Number |   |  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2310 • PER
PROVIDER COMMUNICATIONS NUMBERS

SITUATIONAL PER06 364 Communication Number X 1 AN 1/256
Complete communications number including country or area code when applicable
SYNTAX: P0506

SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.

SITUATIONAL PER07 365 Communication Number Qualifier X 1 ID 2/2
Code identifying the type of communication number
SYNTAX: P0708

SITUATIONAL RULE: Required when a value is being reported in the PER08 element. If not required by this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  AP | Alternate Telephone  |
|  BN | Beeper Number  |
|  CP | Cellular Phone  |
|  EM | Electronic Mail  |
|  EX | Telephone Extension  |
|  FX | Facsimile  |
|  HP | Home Phone Number  |
|  TE | Telephone  |
|  WP | Work Phone Number  |

SITUATIONAL PER08 364 Communication Number X 1 AN 1/256
Complete communications number including country or area code when applicable
SYNTAX: P0708

SITUATIONAL RULE: Required when additional communication numbers are available. If not required by this implementation guide, do not send.

NOT USED PER09 443 Contact Inquiry Reference O 1 AN 1/20

FEBRUARY 2011
163

005010X220 &amp; 005010X220A1 • 834 • 2310 • PLA
PROVIDER CHANGE REASON
CONSOLIDATED • 834

## SEGMENT DETAIL

### PLA - PROVIDER CHANGE REASON

X12 Segment Name: Place or Location

X12 Purpose: To indicate action to be taken for the location specified and to qualify the location specified

Loop: 2310 — PROVIDER INFORMATION

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required to report the reason and the effective date that a member changes providers as described by the NM1 segment in Loop 2310. If not required by this implementation guide, do not send.

TR3 Example: PLA*2*1P*19970628**AI~

## DIAGRAM

![img-39.jpeg](img-39.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | PLA01 | 306 | Action Code
Code indicating type of action | M 1 ID 1/2  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 2 Change (Update) |   |
|  REQUIRED | PLA02 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 1P Provider |   |
|  REQUIRED | PLA03 | 373 | Date
Date expressed as CCYYMMDD where CC represents the first two digits of the calendar year | M 1 DT 8/8  |
|   |  |  | SEMANTIC: PLA03 is the effective date for the action identified in PLA01. |   |
|   |  |  | IMPLEMENTATION NAME: Provider Effective Date |   |
|   |  |  | This is the effective date of the change of PCP. |   |
|  NOT USED | PLA04 | 337 | Time
O 1 TM 4/8 |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2310 • PLA
PROVIDER CHANGE REASON

REQUIRED PLA05 1203
Maintenance Reason Code O 1 ID 2/3
Code identifying the reason for the maintenance change

If none of the specific Maintenance Reasons apply, send 'AI', No Reason Given.

|  CODE | DEFINITION  |
| --- | --- |
|  14 | Voluntary Withdrawal  |
|  22 | Plan Change  |
|  46 | Current Customer Information File in Error  |
|  AA | Dissatisfaction with Office Staff  |
|  AB | Dissatisfaction with Medical Care/Services Rendered  |
|  AC | Inconvenient Office Location  |
|  AD | Dissatisfaction with Office Hours  |
|  AE | Unable to Schedule Appointments in a Timely Manner  |
|  AF | Dissatisfaction with Physician's Referral Policy  |
|  AG | Less Respect and Attention Time Given than to Other Patients  |
|  AH | Patient Moved to a New Location  |
|  AI | No Reason Given  |
|  AJ | Appointment Times not Met in a Timely Manner  |

FEBRUARY 2011
165

005010X220 &amp; 005010X220A1 • 834 • 2320 • COB
COORDINATION OF BENEFITS
CONSOLIDATED • 834

# SEGMENT DETAIL

# COB - COORDINATION OF BENEFITS

X12 Segment Name: Coordination of Benefits

X12 Purpose: To supply information on coordination of benefits

Loop: 2320 — COORDINATION OF BENEFITS Loop Repeat: 5

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required whenever an individual has another insurance plan with benefits similar to those covered by the insurance product specified in the HD segment for this occurrence of Loop ID-2300. If not required by this implementation guide, do not send.

TR3 Example: COB®P®XYZ123®1~

# DIAGRAM

|  COB | COB01 1138
Payer Resp
Seq No Code
O 1 ID 1/1 | COB02 127
Reference
Ident
O 1 AN 1/50 | COB03 1143
Benefits
Coord Code
O 1 ID 1/1 | COB04 1365
Service
Type Code
O 9 ID 1/2  |
| --- | --- | --- | --- | --- |

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | COB01 | 1138 | Payer Responsibility Sequence Number Code
O 1 ID 1/1
Code identifying the insurance carrier's level of responsibility for a payment of a claim | O 1 ID 1/1  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | P Primary |   |
|   |  |  | S Secondary |   |
|   |  |  | T Tertiary |   |
|   |  |  | U Unknown |   |
|  SITUATIONAL | COB02 | 127 | Reference Identification
O 1 AN 1/50
Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier | O 1 AN 1/50  |
|   |  |  | SEMANTIC: COB02 is the policy number. |   |
|   |  |  | SITUATIONAL RULE: Required when the policy number is available. If not required by this implementation guide, do not send. |   |
|   |  |  | IMPLEMENTATION NAME: Member Group or Policy Number |   |
|  REQUIRED | COB03 | 1143 | Coordination of Benefits Code
O 1 ID 1/1
Code identifying whether there is a coordination of benefits | O 1 ID 1/1  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 1 Coordination of Benefits |   |
|   |  |  | 5 Unknown |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2320 • COB
COORDINATION OF BENEFITS

6 No Coordination of Benefits
This code is sent when it has been determined that there is no COB.

Service Type Code
O 9 ID 1/2
Code identifying the classification of service

SITUATIONAL RULE: Required when detailed COB coverage information is agreed to be exchanged. If not required by this implementation guide, do not send.

|  CODE | DEFINITION  |
| --- | --- |
|  1 | Medical Care  |
|  35 | Dental Care  |
|  48 | Hospital - Inpatient  |
|  50 | Hospital - Outpatient  |
|  54 | Long Term Care  |
|  89 | Free Standing Prescription Drug  |
|  90 | Mail Order Prescription Drug  |
|  A4 | Psychiatric  |
|  AG | Skilled Nursing Care  |
|  AL | Vision (Optometry)  |
|  BB | Partial Hospitalization (Psychiatric)  |

FEBRUARY 2011
167

005010X220 &amp; 005010X220A1 • 834 • 2320 • REF
ADDITIONAL COORDINATION OF BENEFITS IDENTIFIERS
CONSOLIDATED • 834

# SEGMENT DETAIL

# REF - ADDITIONAL COORDINATION OF BENEFITS IDENTIFIERS

X12 Segment Name: Reference Information
X12 Purpose: To specify identifying information
X12 Syntax: 1. R0203
At least one of REF02 or REF03 is required.
Loop: 2320 — COORDINATION OF BENEFITS
Segment Repeat: 4
Usage: SITUATIONAL
Situational Rule: Required if additional COB identifiers are supplied by the subscriber. If not required by this implementation guide, do not send.
TR3 Notes: 1. Use the Social Security Number until the National ID Number for individuals is available.
TR3 Example: REF*6P*AZ12345~

# DIAGRAM

REF
REF01 128
Reference Ident Qual
M 1 ID 2/3
REF02 127
Reference Ident
X 1 AN 1/50
REF03 352
Description
X 1 AN 1/80
REF04 C040
Reference Identifier
O 1

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | REF01 | 128 | Reference Identification Qualifier
Code qualifying the Reference Identification | M 1 ID 2/3  |
|   |  |  | CODE | DEFINITION  |
|   |  |  | 60 | Account Suffix Code  |
|   |  |  | 6P | Group Number  |
|   |  |  | SY | Social Security Number  |
|   |  |  |  | The social security number may not be used for any Federally administered programs such as Medicare or CHAMPUS/TRICARE.  |
|   |  |  | ZZ | Mutually Defined  |
|   |  |  |  | Mutually Defined, will be used in this REF01 for National Individual Identifier until a standard code is defined.  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2320 • REF
ADDITIONAL COORDINATION OF BENEFITS IDENTIFIERS

|  REQUIRED | REF02 | 127 | Reference Identification | X 1 | AN | 1/50  |
| --- | --- | --- | --- | --- | --- | --- |
|  Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier  |   |   |   |   |   |   |
|  SYNTAX: R0203  |   |   |   |   |   |   |
|  IMPLEMENTATION NAME: Member Group or Policy Number  |   |   |   |   |   |   |
|  NOT USED | REF03 | 352 | Description | X 1 | AN | 1/80  |
|  NOT USED | REF04 | C040 | REFERENCE IDENTIFIER | O 1 |  |   |

FEBRUARY 2011
169

005010X220 &amp; 005010X220A1 • 834 • 2320 • DTP
COORDINATION OF BENEFITS ELIGIBILITY DATES
CONSOLIDATED • 834

## SEGMENT DETAIL

# DTP - COORDINATION OF BENEFITS ELIGIBILITY DATES

X12 Segment Name: Date or Time or Period
X12 Purpose: To specify any or all of a date, a time, or a time period
Loop: 2320 — COORDINATION OF BENEFITS
Segment Repeat: 2
Usage: SITUATIONAL
Situational Rule: Required when the submitter needs to send effective dates for coordination of benefits. If not required by this implementation guide, do not send.
TR3 Example: DTP®344®D8®19960401~

## DIAGRAM

![img-40.jpeg](img-40.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | DTP01 | 374 | Date/Time Qualifier
Code specifying type of date or time, or both date and time | M 1 ID 3/3  |
|   |  |  | IMPLEMENTATION NAME: Date Time Qualifier |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 344 Coordination of Benefits Begin |   |
|   |  |  | 345 Coordination of Benefits End |   |
|  REQUIRED | DTP02 | 1250 | Date Time Period Format Qualifier
Code indicating the date format, time format, or date and time format | M 1 ID 2/3  |
|   |  |  | SEMANTIC: DTP02 is the date or time or period format that will appear in DTP03. |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | D8 Date Expressed in Format CCYYMMDD |   |
|  REQUIRED | DTP03 | 1251 | Date Time Period
Expression of a date, a time, or range of dates, times or dates and times | M 1 AN 1/35  |
|   |  |  | IMPLEMENTATION NAME: Coordination of Benefits Date |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2330 • NM1
COORDINATION OF BENEFITS RELATED ENTITY

## SEGMENT DETAIL

### NM1 - COORDINATION OF BENEFITS RELATED ENTITY

**X12 Segment Name:** Individual or Organizational Name
**X12 Purpose:** To supply the full name of an individual or organizational entity
**X12 Syntax:**

1. P0809
If either NM108 or NM109 is present, then the other is required.

2. C1110
If NM111 is present, then NM110 is required.

3. C1203
If NM112 is present, then NM103 is required.

**Loop:** 2330 — COORDINATION OF BENEFITS RELATED ENTITY
**Loop Repeat:** 3

**Segment Repeat:** 1

**Usage:** SITUATIONAL

**Situational Rule:** Required to send the name of the insurance company when provided to the sponsor. If not required by this implementation guide, do not send.

**TR3 Example:** NM1*IN*2*ABC INSURANCE CO~

## DIAGRAM

![img-41.jpeg](img-41.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | NM101 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 36 Employer |   |
|   |  |  | GW Group |   |
|   |  |  | IN Insurer |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • 2330 • NM1
COORDINATION OF BENEFITS RELATED ENTITY
CONSOLIDATED • 834

|  REQUIRED | NM102 | 1065 | Entity Type Qualifier
Code qualifying the type of entity
SEMANTIC: NM102 qualifies NM103.
CODE DEFINITION | M 1 | ID | 1/1  |
| --- | --- | --- | --- | --- | --- | --- |
|  SITUATIONAL | NM103 | 1035 | 2 Non-Person Entity
Name Last or Organization Name
Individual last name or organizational name
SYNTAX: C1203 | X 1 | AN | 1/60  |
|   |   |   |  SITUATIONAL RULE: Required to send the insurance company name if no standard identifier is available to pass in NM109. If not required by this implementation guide, do not send.  |   |   |   |
|  IMPLEMENTATION NAME: Coordination of Benefits Insurer Name  |   |   |   |   |   |   |
|  NOT USED | NM104 | 1036 | Name First | O 1 | AN | 1/35  |
|  NOT USED | NM105 | 1037 | Name Middle | O 1 | AN | 1/25  |
|  NOT USED | NM106 | 1038 | Name Prefix | O 1 | AN | 1/10  |
|  NOT USED | NM107 | 1039 | Name Suffix | O 1 | AN | 1/10  |
|  SITUATIONAL | NM108 | 66 | Identification Code Qualifier
Code designating the system/method of code structure used for Identification Code (67)
SYNTAX: P0809 | X 1 | ID | 1/2  |
|   |   |   |  SITUATIONAL RULE: Required when a value is being reported in the NM109 element. If not required by this implementation guide, do not send.  |   |   |   |
|   |   |   | CODE DEFINITION |   |   |   |
|   |   |   | FI Federal Taxpayer’s Identification Number |   |   |   |
|   |   |   | NI National Association of Insurance Commissioners (NAIC) Identification |   |   |   |
|   |   |   | XV Centers for Medicare and Medicaid Services PlanID |   |   |   |
|   |   |   | Use when reporting Health Plan ID (HPID) or Other Entity Identifier (OEID). |   |   |   |
|  SITUATIONAL | NM109 | 67 | Identification Code
Code identifying a party or other code
SYNTAX: P0809 | X 1 | AN | 2/80  |
|   |   |   |  SITUATIONAL RULE: Required when supplied by the employee to the sponsor. If not required by this implementation guide, do not send.  |   |   |   |
|   |   |   | IMPLEMENTATION NAME: Coordination of Benefits Insurer Identification Code  |   |   |   |
|  NOT USED | NM110 | 706 | Entity Relationship Code | X 1 | ID | 2/2  |
|  NOT USED | NM111 | 98 | Entity Identifier Code | O 1 | ID | 2/3  |
|  NOT USED | NM112 | 1035 | Name Last or Organization Name | O 1 | AN | 1/60  |

172
FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2330 • N3
COORDINATION OF BENEFITS RELATED ENTITY ADDRESS

## SEGMENT DETAIL

### N3 - COORDINATION OF BENEFITS RELATED ENTITY ADDRESS

X12 Segment Name: Party Location

X12 Purpose: To specify the location of the named party

Loop: 2330 — COORDINATION OF BENEFITS RELATED ENTITY

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when detailed COB coverage information is agreed to be exchanged. If not required by this implementation guide, do not send.

TR3 Example: N3®50 ORCHARD STREET~

## DIAGRAM

![img-42.jpeg](img-42.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N301 | 166 | Address Information
Address information | M 1 AN 1/55  |
|  SITUATIONAL | N302 | 166 | Address Information
Address information | O 1 AN 1/55  |
|   |  |  | SITUATIONAL RULE: Required if a second address line exists. If not required by this implementation guide, do not send.  |   |

FEBRUARY 2011
173

005010X220 &amp; 005010X220A1 • 834 • 2330 • N4

COORDINATION OF BENEFITS OTHER INSURANCE COMPANY CITY, STATE, ZIP CODE

CONSOLIDATED • 834

## SEGMENT DETAIL

### N4 - COORDINATION OF BENEFITS OTHER INSURANCE COMPANY CITY, STATE, ZIP CODE

X12 Segment Name: Geographic Location

X12 Purpose: To specify the geographic place of the named party

X12 Syntax:
1. E0207
Only one of N402 or N407 may be present.
2. C0605
If N406 is present, then N405 is required.
3. C0704
If N407 is present, then N404 is required.

Loop: 2330 — COORDINATION OF BENEFITS RELATED ENTITY

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when detailed COB coverage information is agreed to be exchanged. If not required by this implementation guide, do not send.

TR3 Example: N4*KANSAS CITY*MO*64108~

## DIAGRAM

![img-43.jpeg](img-43.jpeg)

* N407 1715
Country Sub Code
X 1 ID 1/3

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | N401 | 19 | City Name
Free-form text for city name | O 1 AN 2/30  |
|   |  |  | COMMENT: A combination of either N401 through N404, or N405 and N406 may be adequate to specify a location.  |   |
|   |  |  | IMPLEMENTATION NAME: Coordination of Benefits Other Insurance Company City Name  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2330 • N4
COORDINATION OF BENEFITS OTHER INSURANCE COMPANY CITY, STATE, ZIP CODE

SITUATIONAL N402 156
State or Province Code X 1 ID 2/2
Code (Standard State/Province) as defined by appropriate government agency
SYNTAX: E0207
COMMENT: N402 is required only if city name (N401) is in the U.S. or Canada.

SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Coordination of Benefits Other Insurance Company State Code
CODE SOURCE 22: States and Provinces

SITUATIONAL N403 116
Postal Code O 1 ID 3/15
Code defining international postal zone code excluding punctuation and blanks (zip code for United States)

SITUATIONAL RULE: Required when the address is in the United States of America, including its territories, or Canada, or when a postal code exists for the country in N404. If not required by this implementation guide, do not send.
IMPLEMENTATION NAME: Coordination of Benefits Other Insurance Company Postal Zone or ZIP Code
CODE SOURCE 51: ZIP Code
CODE SOURCE 932: Universal Postal Codes

SITUATIONAL N404 26
Country Code X 1 ID 2/3
Code identifying the country
SYNTAX: C0704

SITUATIONAL RULE: Required when the address is outside the United States of America. If not required by this implementation guide, do not send.
CODE SOURCE 5: Countries, Currencies and Funds
Use the alpha-2 country codes from Part 1 of ISO 3166.

NOT USED N405 309
Location Qualifier X 1 ID 1/2

NOT USED N406 310
Location Identifier O 1 AN 1/30

SITUATIONAL N407 1715
Country Subdivision Code X 1 ID 1/3
Code identifying the country subdivision
SYNTAX: E0207, C0704

SITUATIONAL RULE: Required when the address is not in the United States of America, including its territories, or Canada, and the country in N404 has administrative subdivisions such as but not limited to states, provinces, cantons, etc. If not required by this implementation guide, do not send.
CODE SOURCE 5: Countries, Currencies and Funds
Use the country subdivision codes from Part 2 of ISO 3166.

FEBRUARY 2011
175

005010X220 &amp; 005010X220A1 • 834 • 2330 • PER
ADMINISTRATIVE COMMUNICATIONS CONTACT
CONSOLIDATED • 834

## SEGMENT DETAIL

# PER - ADMINISTRATIVE COMMUNICATIONS CONTACT

X12 Segment Name: Administrative Communications Contact

X12 Purpose: To identify a person or office to whom administrative communications should be directed

X12 Syntax:
1. P0304
If either PER03 or PER04 is present, then the other is required.
2. P0506
If either PER05 or PER06 is present, then the other is required.
3. P0708
If either PER07 or PER08 is present, then the other is required.

Loop: 2330 — COORDINATION OF BENEFITS RELATED ENTITY

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when detailed COB coverage information is agreed to be exchanged. If not required by this implementation guide, do not send.

TR3 Example: PER*CN**TE*8015554321~

## DIAGRAM

PER
![img-44.jpeg](img-44.jpeg)
PER01 366
Contact
Funct Code
M 1 ID 2/2
PER02 93
Name
O 1 AN 1/60
PER03 365
Comm
Number Qual
X 1 ID 2/2
PER04 364
Comm
Number
X 1 AN 1/256
PER05 365
Comm
Number Qual
X 1 ID 2/2
PER06 364
Comm
Number
X 1 AN 1/256

PER07 365
Comm
Number Qual
X 1 ID 2/2
PER08 364
Comm
Number
X 1 AN 1/256
PER09 443
Contact Inq
Reference
O 1 AN 1/20

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | PER01 | 366 | Contact Function Code | M 1 ID 2/2  |
|   |  |  | Code identifying the major duty or responsibility of the person or group named |   |
|   |  |  | CODE | DEFINITION  |
|   |  |  | CN | General Contact  |
|  NOT USED | PER02 | 93 | Name | O 1 AN 1/60  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2330 • PER ADMINISTRATIVE COMMUNICATIONS CONTACT

|  REQUIRED | PER03 | 365 | Communication Number Qualifier | X 1 | ID | 2/2  |
| --- | --- | --- | --- | --- | --- | --- |
|   |  |  | Code identifying the type of communication number |  |  |   |
|   |  |  | SYNTAX: P0304 |  |  |   |
|   |  |  | CODE | DEFINITION |  |   |
|   |  |  | TE | Telephone |  |   |
|  REQUIRED | PER04 | 364 | Communication Number | X 1 | AN | 1/256  |
|   |  |  | Complete communications number including country or area code when applicable |  |  |   |
|   |  |  | SYNTAX: P0304 |  |  |   |
|  NOT USED | PER05 | 365 | Communication Number Qualifier | X 1 | ID | 2/2  |
|  NOT USED | PER06 | 364 | Communication Number | X 1 | AN | 1/256  |
|  NOT USED | PER07 | 365 | Communication Number Qualifier | X 1 | ID | 2/2  |
|  NOT USED | PER08 | 364 | Communication Number | X 1 | AN | 1/256  |
|  NOT USED | PER09 | 443 | Contact Inquiry Reference | O 1 | AN | 1/20  |

FEBRUARY 2011
177

005010X220 &amp; 005010X220A1 • 834 • 2000 • LS
ADDITIONAL REPORTING CATEGORIES
CONSOLIDATED • 834

# SEGMENT DETAIL

# LS - ADDITIONAL REPORTING CATEGORIES

X12 Segment Name: Loop Header

X12 Purpose: To indicate that the next segment begins a loop

X12 Semantic: 1. One loop may be nested contained within another loop, provided the inner nested loop terminates before the outer loop. When specified by the standard setting body as mandatory, this segment in combination with "LE", must be used. It is not to be used if not specifically set forth for use. The loop identifier in the loop header and trailer must be identical. The value for the identifier is the loop ID of the required loop segment. The loop ID number is given on the transaction set diagram in the appropriate ASC X12 version/release.

X12 Comments: 1. See Figures Appendix for an explanation of the use of the LS and LE segments.

Loop: 2000 — MEMBER LEVEL DETAIL

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when needed to provide additional reporting categories about the member. If not required by this implementation guide, do not send.

TR3 Example: LS*2700~

# DIAGRAM

LS * LS01 447
Loop ID Code
M 1 AN 1/4

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | LS01 | 447 | Loop Identifier Code | M 1 AN 1/4  |
|   |  |  | The loop ID number given on the transaction set diagram is the value for this data element in segments LS and LE  |   |
|   |  |  | Use the value 2700.  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2700 • LX
MEMBER REPORTING CATEGORIES

## SEGMENT DETAIL

### LX - MEMBER REPORTING CATEGORIES

X12 Segment Name: Transaction Set Line Number
X12 Purpose: To reference a line number in a transaction set
Loop: 2700 — MEMBER REPORTING CATEGORIES  Loop Repeat: &gt;1
Segment Repeat: 1
Usage: SITUATIONAL
Situational Rule: Required when needed to provide additional reporting categories about the member. If not required by this implementation guide, do not send.
TR3 Example: LX*1~

## DIAGRAM

LX *

|  LX01 | 554  |
| --- | --- |
|  Assigned Number  |   |
|  M 1 | N0 1/6  |

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | LX01 | 554 | Assigned Number | M 1 | N0 | 1/6  |
|   |  |  | Number assigned for differentiation within a transaction set |  |  |   |
|   |  |  | Use this sequential non-negative integer for LX loops for this member’s additional reporting categories. |  |  |   |

FEBRUARY 2011
179

005010X220 &amp; 005010X220A1 • 834 • 2750 • N1
REPORTING CATEGORY
CONSOLIDATED • 834

# SEGMENT DETAIL

# N1 - REPORTING CATEGORY

X12 Segment Name: Party Identification

X12 Purpose: To identify a party by type of organization, name, and code

X12 Syntax: 1. R0203
At least one of N102 or N103 is required.

2. P0304
If either N103 or N104 is present, then the other is required.

Loop: 2750 — REPORTING CATEGORY  Loop Repeat: 1

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required to specify the name of the reporting category of the member's participating entity.

TR3 Example: N1*75*SOUTHEASTERN UNION~

# DIAGRAM

![img-45.jpeg](img-45.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | N101 | 98 | Entity Identifier Code
Code identifying an organizational entity, a physical location, property or an individual |   |   | M 1 | ID | 2/3  |
|   |  |  | CODE | DEFINITION |  |  |  |   |
|   |  |  | 75 | Participant |  |  |  |   |
|  REQUIRED | N102 | 93 | Name
Free-form name |   |   | X 1 | AN | 1/60  |
|   |  |  | SYNTAX: R0203 |   |   |  |  |   |
|   |  |  | IMPLEMENTATION NAME: Member Reporting Category Name |   |   |  |  |   |
|  NOT USED | N103 | 66 | Identification Code Qualifier |   |   | X 1 | ID | 1/2  |
|  NOT USED | N104 | 67 | Identification Code |   |   | X 1 | AN | 2/80  |
|  NOT USED | N105 | 706 | Entity Relationship Code |   |   | O 1 | ID | 2/2  |
|  NOT USED | N106 | 98 | Entity Identifier Code |   |   | O 1 | ID | 2/3  |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2750 • REF
REPORTING CATEGORY REFERENCE

## SEGMENT DETAIL

**REF - REPORTING CATEGORY REFERENCE**

X12 Segment Name: Reference Information

X12 Purpose: To specify identifying information

X12 Syntax: 1. R0203
At least one of REF02 or REF03 is required.

Loop: 2750 — REPORTING CATEGORY

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required to specify the reference identifier associated with the reporting category of the member’s participating entity.

TR3 Example: REF*26*442~

## DIAGRAM

**REF** * REF01 128
Reference Ident Qual
M 1 ID 2/3

* REF02 127
Reference Ident
X 1 AN 1/50

* REF03 352
Description
X 1 AN 1/80

* REF04 C040
Reference Identifier
O 1

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | REF01 | 128 | Reference Identification Qualifier
Code qualifying the Reference Identification | M 1 ID 2/3  |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 00 Contracting District Number |   |
|   |  |  | 17 Client Reporting Category |   |
|   |  |  | 18 Plan Number |   |
|   |  |  | 19 Division Identifier |   |
|   |  |  | 26 Union Number |   |
|   |  |  | 3L Branch Identifier |   |
|   |  |  | 6M Application Number |   |
|   |  |  | 9V Payment Category |   |
|   |  |  | 9X Account Category |   |
|   |  |  | GE Geographic Number |   |
|   |  |  | LU Location Number |   |
|   |  |  | PID Program Identification Number |   |
|   |  |  | XX1 Special Program Code |   |
|   |  |  | XX2 Service Area Code |   |
|   |  |  | YY Geographic Key |   |
|   |  |  | ZZ Mutually Defined |   |

FEBRUARY 2011
181

005010X220 &amp; 005010X220A1 • 834 • 2750 • REF
REPORTING CATEGORY REFERENCE
CONSOLIDATED • 834

|  REQUIRED | REF02 | 127 | Reference Identification | X 1 | AN | 1/50  |
| --- | --- | --- | --- | --- | --- | --- |
|  Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier  |   |   |   |   |   |   |
|  SYNTAX: R0203  |   |   |   |   |   |   |
|  IMPLEMENTATION NAME: Member Reporting Category Reference ID  |   |   |   |   |   |   |
|  NOT USED | REF03 | 352 | Description | X 1 | AN | 1/80  |
|  NOT USED | REF04 | C040 | REFERENCE IDENTIFIER | O 1 |  |   |

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2750 • DTP
REPORTING CATEGORY DATE

## SEGMENT DETAIL

### DTP - REPORTING CATEGORY DATE

X12 Segment Name: Date or Time or Period

X12 Purpose: To specify any or all of a date, a time, or a time period

Loop: 2750 — REPORTING CATEGORY

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when called for in the insurance contract between the sponsor and payer. If not required by this implementation guide, do not send.

TR3 Notes: 1. Use this segment to associate a date or date range with a reporting category.

TR3 Example: DTP*007*RD8*20040101-20040531~

## DIAGRAM

DTP * DTP01 374
Date/Time Qualifier M 1 ID 3/3 * DTP02 1250
Date Time Format Qual M 1 ID 2/3 * DTP03 1251
Date Time Period M 1 AN 1/35

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | DTP01 | 374 | Date/Time Qualifier
Code specifying type of date or time, or both date and time | M 1 ID 3/3  |
|   |  |  | IMPLEMENTATION NAME: Date Time Qualifier |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | 007 Effective |   |
|  REQUIRED | DTP02 | 1250 | Date Time Period Format Qualifier
Code indicating the date format, time format, or date and time format | M 1 ID 2/3  |
|   |  |  | SEMANTIC: DTP02 is the date or time or period format that will appear in DTP03. |   |
|   |  |  | CODE DEFINITION |   |
|   |  |  | D8 Date Expressed in Format CCYYMMDD |   |
|   |  |  | RD8 Range of Dates Expressed in Format CCYYMMDD-CCYYMMDD |   |
|   |  |  | A range of dates expressed in the format CCYYMMDD-CCYYMMDD where CCYY is the numerical expression of the century CC and year YY. MM is the numerical expression of the month within the year, and DD is the numerical expression of the day within the year; the first occurrence of CCYYMMDD is the beginning date and the second occurrence is the ending date. |   |

FEBRUARY 2011
183

005010X220 &amp; 005010X220A1 • 834 • 2750 • DTP
REPORTING CATEGORY DATE
CONSOLIDATED • 834

REQUIRED DTP03 1251
Date Time Period M 1 AN 1/35
Expression of a date, a time, or range of dates, times or dates and times

IMPLEMENTATION NAME: Member Reporting Category Effective Date(s)

FEBRUARY 2011

CONSOLIDATED • 834
005010X220 &amp; 005010X220A1 • 834 • 2000 • LE
ADDITIONAL REPORTING CATEGORIES LOOP TERMINATION

## SEGMENT DETAIL

# LE - ADDITIONAL REPORTING CATEGORIES LOOP TERMINATION

X12 Segment Name: Loop Trailer

X12 Purpose: To indicate that the loop immediately preceding this segment is complete

X12 Semantic: 1. One loop may be nested contained within another loop, provided the inner nested loop terminates before the other loop. When specified by the standards setting body as mandatory, this segment in combination with "LS", must be used. It is not to be used if not specifically set forth for use. The loop identifier in the loop header and trailer must be identical. The value for the identifier is the loop ID of the required loop beginning segment. The loop ID number is given on the transaction set diagram in the appropriate ASC X12 version/release.

X12 Comments: 1. See Figures Appendix for an explanation of the use of the LE and LS segments.

Loop: 2000 — MEMBER LEVEL DETAIL

Segment Repeat: 1

Usage: SITUATIONAL

Situational Rule: Required when the LS segment in position 6880 is sent. If not required by this implementation guide, do not send.

TR3 Example: LE®2700~

## DIAGRAM

![img-46.jpeg](img-46.jpeg)

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | LE01 | 447 | Loop Identifier Code | M 1 AN 1/4  |
|   |  |  | The loop ID number given on the transaction set diagram is the value for this data element in segments LS and LE  |   |
|   |  |  | Use the value 2700.  |   |

FEBRUARY 2011

005010X220 &amp; 005010X220A1 • 834 • SE
TRANSACTION SET TRAILER
CONSOLIDATED • 834

## SEGMENT DETAIL

## SE - TRANSACTION SET TRAILER

X12 Segment Name: Transaction Set Trailer

X12 Purpose: To indicate the end of the transaction set and provide the count of the transmitted segments (including the beginning (ST) and ending (SE) segments)

X12 Comments: 1. SE is the last segment of each transaction set.

Segment Repeat: 1

Usage: REQUIRED

TR3 Example: SE*39*0001~

## DIAGRAM

SE * SE01 96
Number of
Inc Segs
M 1 N0 1/10 * SE02 329
TS Control
Number
M 1 AN 4/9

## ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | SE01 | 96 | Number of Included Segments | M 1 N0 1/10
Total number of segments included in a transaction set including ST and SE segments  |
|   |  |  | IMPLEMENTATION NAME: Transaction Segment Count |   |
|  REQUIRED | SE02 | 329 | Transaction Set Control Number | M 1 AN 4/9
Identifying control number that must be unique within the transaction set functional group assigned by the originator for a transaction set  |
|   |  |  | The transaction set control numbers in ST02 and SE02 must be identical. This unique number also aids in error resolution research. For example, start with the number 0001 and increment from there. This number must be unique within a specific group and interchange, but the number can repeat in other groups and interchanges.  |   |

FEBRUARY 2011

CONSOLIDATED · 834

BENEFIT ENROLLMENT AND MAINTENANCE

005010X220 &amp; 005010X220A1

# 3 Examples

# 3.1 Business Case Scenario 1 -- Enroll an Employee in Multiple Health Care Insurance Products

John Doe is enrolling in three health care products -- health, dental, and vision. He also has Coordination of Benefits (COB) with another insurance company.

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  ST*834*0001*005010X220A1~ | Used to indicate the start of a transaction set and to specify a transaction set control number.  |
|  BGN*00*12456*19980520*1200***2~ | This is an original transaction uniquely identified by the sender with reference #12456. The transaction was created on 5/20/1998 at 12:00 Noon.  |
|  N1*P5**FI*999888777~ | Specifies the sponsor/sender's tax ID number.  |
|  N1*IN**FI*654456654~ | Specifies the insurance company/receiver's tax ID number.  |
|  INS*Y*18*021*20*A***FT~ | Beginning of Table 2. Indicates that the subscriber (John Doe) is adding coverage as an active employee.  |
|  REF*0F*123456789~ | John's subscriber ID number.  |
|  REF*1L*123456001~ | This is the group number assigned by the carrier.  |
|  DTP*356*D8*19960523~ | The eligibility date for this transaction is 5/23/1996.  |
|  NM1*IL*1*DOE*JOHN*P***34*123456789~ | Subscriber's name.  |
|  PER*IP**HP*7172343334*WP*7172341240~ | John's home phone number is (717)234-3334 and his work number is (717)234-1240  |
|  N3*100 MARKET ST*APT 3G~ | This is John's street address.  |
|  N4*CAMP
HILL*PA*17011**CY*CUMBERLAND~ | This is John's city, state zip code and county.  |
|  DMG*D8*19400816*M~ | This is John's date of birth and gender  |

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  HD*021**HLT~ | John is enrolling in a health benefit.  |
|  DTP*348*D8*19960601~ | The benefits under this plan begin 6/01/1996  |
|  COB*P*890111*5~ | This lets the carrier know that John has COB with another company.  |
|  HD*021**DEN~ | John is enrolling in the Dental benefit.  |
|  DTP*348*D8*19960601~ | The benefits under this plan begin 6/01/1996  |
|  HD*021**VIS~ | John is enrolling in the Vision benefit.  |
|  DTP*348*D8*19960601~ | The benefits under this plan begin 6/01/1996  |
|  SE*21*12345~ | End of transaction set. 21 segments were sent and the control number in the ST segment is 12345.  |

# 3.2 Business Case Scenario 2 -- Add a Dependent (Full-time Student) to an Existing Enrollment

James E. Doe, the son of John Doe, is being enrolled under John Doe's medical coverage. James is enrolled at Penn State and expects to graduate on 5/15/1998. His Social Security Number is 103229876. The enrollment for the subscriber, John Doe, had to be submitted before his dependents can be enrolled.

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  ST*834*0001*005010X220A1~ | Used to indicate the start of a transaction set and to specify a transaction set control number.  |
|  BGN*00*12456*19980520*1200***2~ | This is an original transaction uniquely identified by the sender with reference #12456. The transaction was created on 5/20/1998 at 12:00 Noon.  |
|  REF*38*ABCD012354~ | Master policy number (group ID).  |
|  N1*P5**FI*999888777~ | Specifies the sponsor/sender's tax ID number.  |
|  N1*IN**FI*654456654~ | Specifies the insurance company/receiver's tax ID number.  |

FEBRUARY 2011

CONSOLIDATED · 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  INS*N*19*021*28*A***F~ | Beginning of Table 2. Indicates that the dependent (James Doe) is adding coverage as a full time student.  |
|  REF*0F*123456789~ | John's subscriber ID number.  |
|  REF*1L*123456001~ | This is the group number assigned by the carrier.  |
|  DTP*351*D8*19980515~ | The expected graduation date from Penn State is 5/15/1998  |
|  NM1*IL*1*DOE*JAMES*E***34*103229876~ | Dependents name and ssn.  |
|  DMG*D8*19770816*M~ | This is James date of birth and gender  |
|  NM1*M8*2*PENN STATE UNIVERSITY~ | This is the school that James attends.  |
|  HD*021*HLT~ | James is enrolling in a health benefit.  |
|  DTP*348*D8*19960601~ | The benefits under this plan begin 6/01/1996  |
|  SE*15*12345~ | End of transaction set. 15 segments were sent and the control number in the ST segment is 12345.  |

# 3.3 Business Case Scenario 3 -- Enroll an Employee in a Managed Care Product

William Smith is enrolling in the HMO product effective 6/1/1996. He has selected Dr. Bernard Brown as his primary care physician for the program. Mr. Smith is already Dr. Brown's patient. Dr. Brown's provider number is 143766.

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  ST*834*0001*005010X220A1~ | Used to indicate the start of a transaction set and to specify a transaction set control number.  |
|  BGN*00*12456*19980520*1200***2~ | This is an original transaction uniquely identified by the sender with reference #12456. The transaction was created on 5/20/1998 at 12:00 Noon.  |
|  N1*P5**FI*999888777~ | Specifies the sponsor/sender's tax ID number.  |
|  N1*IN**FI*654456654~ | Specifies the insurance company/receiver's tax ID number.  |

FEBRUARY 2011
189

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  INS*Y*18*021*20*A***FT~ | Beginning of Table 2.Indicates that the subscriber (William Smith) is receiving benefits as an active fulltime employee.  |
|  REF*0F*202443307~ | William's subscriber ID number.  |
|  REF*1L*123456001~ | This is the group number assigned by the carrier.  |
|  DTP*356*D8*19960112~ | William first became eligible for coverage on 1/12/96.  |
|  NM1*IL*1*SMITH*WILLIAM***34*202443307~ | Subscriber's name and SSN.  |
|  PER*IP**HP*7172343334*WP*7172341240~ | William's home phone number is (717)234-3334 and his work number is (717)234-1240  |
|  N3*1715 SOUTHWIND AVENUE~ | This is William's street address.  |
|  N4*ANYTOWN*PA*171110000~ | This is Williams's city, state zip code and county.  |
|  DMG*D8*19700614*M~ | This is William's date of birth and gender  |
|  HD*021**HMO~ | William is enrolling in a HMO benefit.  |
|  DTP*348*D8*19960601~ | The benefits under this plan begin 6/01/1996  |
|  LX*01~ | This starts the provider information.  |
|  NM1*P3*1*BROWN*BERNARD**DR**SV*143766*25~ | This gives the provider name, ID number and indicates William is a previous patient of Dr. Brown.  |
|  SE*18*12345~ | End of transaction set. 18 segments were sent and the control number in the ST segment is 12345.  |

# 3.4 Business Case Scenario 4 -- Add Subscriber Coverage

William Smith is adding dental coverage as a benefit, which will be effective on 7/1/2002.

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  ST*834*0001*005010X220A1~ | Used to indicate the start of a transaction set and to specify a transaction set control number.  |

FEBRUARY 2011

CONSOLIDATED · 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  BGN*00*12456*20020601*1200***2~ | This is an original transaction uniquely identified by the sender with reference #12456. The transaction was created on 6/1/2002 at 12:00 Noon.  |
|  REF*38*ABCD012354~ | Master policy number (group ID).  |
|  N1*P5**FI*999888777~ | Specifies the sponsor/sender's tax ID number.  |
|  N1*IN**FI*654456654~ | Specifies the insurance company/receiver's tax ID number.  |
|  INS*Y*18*001*22*A***FT~ | Beginning of Table 2. Indicates that the subscriber (William Smith) is updating coverage as an active employee.  |
|  REF*0F*202443307~ | Williams subscriber ID number.  |
|  REF*1L*123456001~ | This is the group number assigned by the carrier.  |
|  NM1*IL*1*SMITH*WILLIAM***ZZ*2024433307~ | Subscriber's name.  |
|  HD*021**DEN~ | William is enrolling in the Dental benefit.  |
|  DTP*348*D8*20020701~ | The benefits under this plan begin 7/1/2002.  |
|  SE*12*12345~ | End of transaction set. 12 segments were sent and the control number in the ST segment is 12345.  |

**NOTE**

In the previous example, to remove coverage do the following: change the maintenance type code (HD01) from 021 (addition) to 024 (cancellation/termination), and change the date/time qualifier (DTP01) from 348 (benefit begin) to 349 (benefit end).

## 3.5 Business Case Scenario 5 -- Change subscriber information

John Doe is correcting his date of birth.

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  ST*834*0001*005010X220A1~ | Used to indicate the start of a transaction set and to specify a transaction set control number.  |

FEBRUARY 2011
191

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  BGN*00*12456*19980520*1200***2~ | This is an original transaction uniquely identified by the sender with reference #12456. The transaction was created on 5/20/1998 at 12:00 Noon.  |
|  N1*P5*GENERIC INC~ | Specifies the sponsor/sender's tax ID number.  |
|  N1*IN*ABC
INSURANCE*FI*654456654~ | Specifies the insurance company/receiver's tax ID number.  |
|  INS*Y*18*001*25*A***FT~ | Beginning of Table 2. Indicates that the subscriber (John Doe) is updating coverage as an active employee.  |
|  REF*0F*123456789~ | John's subscriber ID number.  |
|  REF*1L*123456001~ | This is the group number assigned by the carrier.  |
|  NMI*IL*1*DOE*JAMES*E***34*103229876~ | Members name and ssn.  |
|  DMG*D8*19500415*M~ | This is John's date of birth and gender  |
|  NM1*70*1*DOE*JAMES*E~ | Subscriber's name. The NM101 = 70 indicates that this is a change to information previously sent.  |
|  DMG*D8*19500416*M~ | This is John's incorrect date of birth.  |
|  SE*12*12345~ | End of transaction set. 12 segments were sent and the control number in the ST segment is 12345.  |

# 3.6 Business Case Scenario 6 -- Cancel a dependent

John Doe is canceling coverage for his over-age dependent, James, to be effective 8/1/1996.

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  ST*834*0001*005010X220A1~ | Used to indicate the start of a transaction set and to specify a transaction set control number.  |
|  BGN*00*12456*19980520*1200***2~ | This is an original transaction uniquely identified by the sender with reference #12456. The transaction was created on 5/20/1998 at 12:00 Noon.  |
|  REF*38*ABCD012354~ | Master policy number (group ID).  |

FEBRUARY 2011

CONSOLIDATED · 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  N1*P5**FI*999888777~ | Specifies the sponsor/sender's tax ID number.  |
|  N1*IN**FI*654456654~ | Specifies the insurance company/receiver's tax ID number.  |
|  INS*N*19*024*07*A~ | Beginning of Table 2. Indicates that the dependent (James Doe) is terminating all coverage's.  |
|  REF*0F*123456789~ | John's subscriber ID number.  |
|  REF*1L*123456001~ | This is the group number assigned by the carrier.  |
|  DTP*357*D8*19960801~ | The benefits under this plan are terminating 8/01/1996.  |
|  NM1*IL*1*DOE*JAMES*E***34*103229876~ | Dependent's name and SSN.  |
|  DMG*D8*19770816*M~ | This is James' date of birth and gender.  |
|  SE*12*12345~ | End of transaction set. 12 segments were sent and the control number in the ST segment is 12345.  |

# 3.7 Business Case Scenario 7 -- Terminate Eligibility for a Subscriber

The eligibility for John Doe is being canceled because he terminated employment on 10/1/1996.

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  ST*834*0001*005010X220A1~ | Used to indicate the start of a transaction set and to specify a transaction set control number.  |
|  BGN*00*12456*19980520*1200***2~ | This is an original transaction uniquely identified by the sender with reference #12456. The transaction was created on 5/20/1998 at 12:00 Noon.  |
|  N1*P5**FI*999888777~ | Specifies the sponsor/sender's tax ID number.  |
|  N1*IN**FI*654456654~ | Specifies the insurance company/receiver's tax ID number.  |
|  INS*Y*18*024*08*A***TE~ | Beginning of Table 2. Indicates that the subscriber (John Doe) is terminating all coverage.  |
|  REF*0F*123456789~ | John's subscriber ID number.  |

FEBRUARY 2011
193

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  REF*1L*123456001~ | This is the group number assigned by the carrier.  |
|  DTP*357*D8*19961001~ | The benefits under this plan are terminating 10/01/1996.  |
|  NM1*IL*1*DOE*JOHN*E***34*103229876~ | Subscriber's name.  |
|  SE*10*12345~ | End of transaction set. 10 segments were sent and the control number in the ST segment is 12345.  |

# 3.8 Business Case Scenario 8 -- Reinstate an Employee

John Doe's contract was incorrectly canceled and is being reinstated.

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  ST*834*0001*005010X220A1~ | Used to indicate the start of a transaction set and to specify a transaction set control number.  |
|  BGN*00*12456*19980520*1200***2~ | This is an original transaction uniquely identified by the sender with reference #12456. The transaction was created on 5/20/1998 at 12:00 Noon.  |
|  REF*38*ABCD012354~ | Master policy number (group ID).  |
|  N1*P5**FI*999888777~ | Specifies the sponsor/sender's tax ID number.  |
|  N1*IN**FI*654456654~ | Specifies the insurance company/receiver's tax ID number.  |
|  INS*Y*18*025*20*A***FT~ | Beginning of Table 2. Indicates that the subscriber (John Doe) is reinstating all coverages.  |
|  REF*0F*123456789~ | John's subscriber ID number.  |
|  REF*1L*123456001~ | This is the group number assigned by the carrier.  |
|  DTP*303*D8*19961001~ | The benefits under this plan are reinstated as of 6/01/1996.  |
|  NM1*IL*1*DOE*JAMES*E***34*103229876~ | Subscriber's name.  |
|  SE*11*12345~ | End of transaction set. 11 segments were sent and the control number in the ST segment is 12345.  |

FEBRUARY 2011

CONSOLIDATED · 834

BENEFIT ENROLLMENT AND MAINTENANCE

005010X220 &amp; 005010X220A1

# 3.9 Business Case Scenario 9 -- Reinstate the Employee at the Coverage (HD) Level

William Smith is reinstating his dental coverage.

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  ST*834*0001*005010X220A1~ | Used to indicate the start of a transaction set and to specify a transaction set control number.  |
|  BGN*00*12456*20020601*1200***2~ | This is an original transaction uniquely identified by the sender with reference #12456. The transaction was created on 6/01/2002 at 12:00 Noon.  |
|  REF*38*ABCD012354~ | Master policy number (group ID).  |
|  N1*P5**FI*999888777~ | Specifies the sponsor/sender's tax ID number.  |
|  N1*IN**FI*654456654~ | Specifies the insurance company/receiver's tax ID number.  |
|  INS*Y*18*025**A***FT~ | Beginning of Table 2. Indicates that the subscriber (William Smith) is submitting a reinstate to an his existing record.  |
|  REF*0F*202443307~ | William's subscriber ID number.  |
|  REF*1L*123456001~ | This is the group number assigned by the carrier.  |
|  NM1*IL*1*SMITH*WILLIAM***ZZ*202443307~ | William's subscriber ID number.  |
|  HD*025**DEN~ | William is reinstating in the Dental benefit.  |
|  DTP*348*D8*20020701~ | The reinstate of coverage begins 7/1/2002.  |
|  SE*12*12345~ | End of transaction set. 12 segments were sent and the control number in the ST segment is 12345.  |

# 3.10 Business Case Scenario 10 -- Reinstate member eligibility (INS)

This example illustrates the reinstatement of the person as eligible without reinstatement of coverage in a particular benefit.

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

|  X12 SYNTAX | COMMENTS  |
| --- | --- |
|  ST*834*0001*005010X220A1~ | Used to indicate the start of a transaction set and to specify a transaction set control number.  |
|  BGN*00*12456*20020601*1200***2~ | This is an original transaction uniquely identified by the sender with reference #12456. The transaction was created on 6/01/2002 at 12:00 Noon.  |
|  REF*38*ABCD012354~ | Master policy number (group ID).  |
|  N1*P5**FI*999888777~ | Specifies the sponsor/sender's tax ID number.  |
|  N1*IN**FI*654456654~ | Specifies the insurance company/receiver's tax ID number.  |
|  INS*Y*18*025**A***FT~ | Beginning of Table 2. Indicates that the subscriber (William Smith) is submitting a change to his existing record.  |
|  REF*0F*202443307~ | William's subscriber ID number.  |
|  REF*1L*123456001~ | This is the group number assigned by the carrier.  |
|  NM1*IL*1*SMITH*WILLIAM***ZZ*2024433307~ | Subscriber's name.  |
|  SE*10*12345~ | End of transaction set. 10 segments were sent and the control number in the ST segment is 12345.  |

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

# A External Code Sources

## A.1 External Code Sources

### 5 Countries, Currencies and Funds

#### SIMPLE DATA ELEMENT/CODE REFERENCES
26, 100, 1715, 66/38, 235/CH, 955/SP

#### SOURCE
Codes for Representation of Names of Countries, ISO 3166-(Latest Release)

Codes for Representation of Currencies and Funds, ISO 4217-(Latest Release)

#### AVAILABLE FROM
American National Standards Institute
25 West 43rd Street, 4th Floor
New York, NY 10036

#### ABSTRACT
Part 1 (Country codes) of the ISO 3166 international standard establishes codes that represent the current names of countries, dependencies, and other areas of special geopolitical interest, on the basis of lists of country names obtained from the United Nations. Part 2 (Country subdivision codes) establishes a code that represents the names of the principal administrative divisions, or similar areas, of the countries, etc. included in Part 1. Part 3 (Codes for formerly used names of countries) establishes a code that represents non-current country names, i.e., the country names deleted from ISO 3166 since its first publication in 1974. Most currencies are those of the geopolitical entities that are listed in ISO 3166 Part 1, Codes for the Representation of Names of Countries. The code may be a three-character alphabetic or three-digit numeric. The two leftmost characters of the alphabetic code identify the currency authority to which the code is assigned (using the two character alphabetic code from ISO 3166 Part 1, if applicable). The rightmost character is a mnemonic derived from the name of the major currency unit or fund. For currencies not associated with a single geographic entity, a specially-allocated two-character alphabetic code, in the range XA to XZ identifies the currency authority. The rightmost character is derived from the name of the geographic area concerned, and is mnemonic to the extent possible. The numeric codes are identical to those assigned to the geographic entities listed in ISO 3166 Part 1. The range 950-998

FEBRUARY 2011
A.1

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

is reserved for identification of funds and currencies not associated with a single entity listed in ISO 3166 Part 1.

## 22 States and Provinces

### SIMPLE DATA ELEMENT/CODE REFERENCES

156, 66/SJ, 235/A5, 771/009

### SOURCE

U.S. Postal Service or

Canada Post or

Bureau of Transportation Statistics

### AVAILABLE FROM

The U.S. state codes may be obtained from:

U.S. Postal Service

National Information Data Center

P.O. Box 2977

Washington, DC 20013

www.usps.gov

The Canadian province codes may be obtained from:

http://www.canadapost.ca

The Mexican state codes may be obtained from:

www.bts.gov/ntda/tbscd/mex-states.html

### ABSTRACT

Provides names, abbreviations, and two character codes for the states, provinces and sub-country divisions as defined by the appropriate government agency of the United States, Canada, and Mexico.

## 51 ZIP Code

### SIMPLE DATA ELEMENT/CODE REFERENCES

116, 66/16, 309/PQ, 309/PR, 309/PS, 771/010

### SOURCE

National ZIP Code and Post Office Directory, Publication 65

The USPS Domestic Mail Manual

A.2

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

# AVAILABLE FROM
U.S Postal Service
Washington, DC 20260
New Orders
Superintendent of Documents
P.O. Box 371954
Pittsburgh, PA 15250-7954

# ABSTRACT
The ZIP Code is a geographic identifier of areas within the United States and its territories for purposes of expediting mail distribution by the U.S. Postal Service. It is five or nine numeric digits. The ZIP Code structure divides the U.S. into ten large groups of states. The leftmost digit identifies one of these groups. The next two digits identify a smaller geographic area within the large group. The two rightmost digits identify a local delivery area. In the nine-digit ZIP Code, the four digits that follow the hyphen further subdivide the delivery area. The two leftmost digits identify a sector which may consist of several large buildings, blocks or groups of streets. The rightmost digits divide the sector into segments such as a street, a block, a floor of a building, or a cluster of mailboxes. The USPS Domestics Mail Manual includes information on the use of the new 11-digit zip code.

# 94 International Organization for Standardization (Date and Time)

SIMPLE DATA ELEMENT/CODE REFERENCES
623

SOURCE
ISO 8601

AVAILABLE FROM
American National Standards Institute
25 West 43rd Street, 4th Floor
New York, NY 10036

# ABSTRACT
ISO Standards code list for representation of date and time.

FEBRUARY 2011
A.3

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

## 102 Languages

### SIMPLE DATA ELEMENT/CODE REFERENCES
819, 66/LE

### SOURCE
Code for the representation of names of languages (ISO 639)

### AVAILABLE FROM
American National Standards Institute
25 West 43rd Street, 4th Floor
New York, NY 10036

### ABSTRACT
A set of symbols used to designate languages.

## 131 International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM)

### SIMPLE DATA ELEMENT/CODE REFERENCES
128/ICD, 235/DX, 235/ID, 1270/BF, 1270/BJ, 1270/BK, 1270/BN, 1270/BQ, 1270/BR, 1270/DD, 1270/PR, 1270/SD, 1270/TD, 1270/AAU, 1270/AAV, 1270/AAX

### SOURCE
International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM), Volumes I, II and III

### AVAILABLE FROM
Superintendent of Documents
U.S. Government Printing Office
P.O. Box 371954
Pittsburgh, PA 15250

### ABSTRACT
The International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM), Volumes I, II (diagnoses) and III (procedures) describes the classification of morbidity and mortality information for statistical purposes and for the indexing of healthcare records by diseases and procedures.

A.4

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

# 206 Government Bill of Lading Office Code

## SIMPLE DATA ELEMENT/CODE REFERENCES
309

## SOURCE
Defense Traffic Management Regulation (DTMR), Appendix I - Government Bill of Lading Codes

## AVAILABLE FROM
Military Traffic Management Command (MTMC)
Attn: Programs and Systems Support (MTIN-P)
5611 Columbia Pike
Falls Church, VA 22041-5050

## ABSTRACT
Defines the regulations for managing the transportation of goods owned or purchased by the Department of Defense.

# 307 National Council for Prescription Drug Programs Pharmacy Number

## SIMPLE DATA ELEMENT/CODE REFERENCES
128/D3

## SOURCE
National Council for Prescription Drug Programs (NCPDP) Provider Number Database and Listing

## AVAILABLE FROM
National Council for Prescription Drug Programs (NCPDP)
9240 East Raintree Drive
Scottsdale, AZ 85260

## ABSTRACT
A unique number assigned in the U.S. and its territories to individual clinic, hospital, chain, and independent pharmacy and dispensing physician locations that conduct business by billing third-party and dispensing physician locations that conduct business by billing third-party drug benefit payers. The National Council for Prescription Drug Programs (NCPDP) maintains this database. The NCPDP Provider Number is a

FEBRUARY 2011
A.5

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

seven-digit number with the following format SSNNNNC, where SS=NCPDP assigned state code number, NNNN=sequential numbering scheme assigned to pharmacy locations, and C=check digit caluculate by algorithm from previous six digits.

# 457 NISO Z39.53 Language Code List

## SIMPLE DATA ELEMENT/CODE REFERENCES
66/LD

## SOURCE
Code list for the representation of names of written languages (NISO Z39.53)

## AVAILABLE FROM
National Information Standards Organization Press
P.O. 338
Oxon Hill, MD 20750-0338

## ABSTRACT
A set of codes to designate written languages.

# 537 Centers for Medicare and Medicaid Services National Provider Identifier

## SIMPLE DATA ELEMENT/CODE REFERENCES
66/XX, 128/HPI

## SOURCE
National Provider System

## AVAILABLE FROM
Centers for Medicare and Medicaid Services
Office of Financial Management
Division of Provider/Supplier Enrollment
C4-10-07
7500 Security Boulevard
Baltimore, MD 21244-1850

## ABSTRACT
The Centers for Medicare and Medicaid Services is developing the National Provider Identifier (NPI), which has been proposed as the standard unique identifier for each

A.6

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

health care provider under the Health Insurance Portability and Accountability Act of 1996.

# 540 Centers for Medicare and Medicaid Services PlanID

SIMPLE DATA ELEMENT/CODE REFERENCES
66/XV, 128/ABY

SOURCE
PlanID Database

AVAILABLE FROM
Centers for Medicare and Medicaid Services
Center of Beneficiary Services, Membership Operations Group
Division of Benefit Coordination
S1-05-06
7500 Security Boulevard
Baltimore, MD 21244-1850

ABSTRACT
The Centers for Medicare and Medicaid Services has joined with other payers to develop a unique national payer identification number. The Centers for Medicare and Medicaid Services is the authorizing agent for enumerating payers through the services of a PlanID Registrar. It may also be used by other payers on a voluntary basis.

# 859 Classification of Race or Ethnicity

SIMPLE DATA ELEMENT/CODE REFERENCES
1270/RET

SOURCE
Classification of Race or Ethnicity

AVAILABLE FROM
Health Information and Surveillance Systems Board
Centers for Disease Control and Prevention
Mailstop C08
1600 Clifton Road, NE
Atlanta, Georgia 30333

FEBRUARY 2011
A.7

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

## ABSTRACT

The Classification of Race or Ethnicity provides a detailed, hierarchical classification of race and ethnicity that complies with the U.S. Office of Management and Budget's 1997 Revisions to the Standards for the Classification of Federal Data on Race and Ethnicity and is consistent with the classification of race and ethnicity used by the U.S. Bureau of the Census.

## 860 Race or Ethnicity Collection Code

### SIMPLE DATA ELEMENT/CODE REFERENCES

1270/REC

### SOURCE

Race or Ethnicity Collection Code

### AVAILABLE FROM

Health Information and Surveillance Systems Board

Centers for Disease Control and Prevention

Mailstop C08

1600 Clifton Road, NE

Atlanta, Georgia 30333

### ABSTRACT

The Race or Ethnicity Collection code provides a method of describing how information on race or ethnicity is collected in various data gathering systems.

## 897 International Classification of Diseases, 10th Revision, Clinical Modification (ICD-10-CM)

### SIMPLE DATA ELEMENT/CODE REFERENCES

128/I10, 235/DC, 1270/ABF, 1270/ABJ, 1270/ABK, 1270/ABN, 1270/ABU, 1270/ABV, 1270/ADD, 1270/APR, 1270/ASD, 1270/ATD

### SOURCE

International Classification of Diseases, 10th Revision, Clinical Modification (ICD-10-CM)

### AVAILABLE FROM

OCD/Classifications and Public Health Data Standards

National Center for Health Statistics

3311 Toledo Road

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

Hyattsville, MD 20782

## ABSTRACT
The International Classicication of Diseases, 10th Revision, Clinical Modification (ICD-10-CM), describes the classification of morbidity and mortality information for statistical purposes and for the indexing of healthcare records by diseases.

## 932 Universal Postal Codes

### SIMPLE DATA ELEMENT/CODE REFERENCES
116

### SOURCE
Universal Postal Union website

### AVAILABLE FROM
International Bureau of the Universal Postal Union
POST*CODE
Case postale 13
3000 BERNE 15 Switzerland

## ABSTRACT
The postcode is the fundamental, essential element of an address. A unique, universal identifier, it unambiguously identifies the addressee's locality and assists in the transmission and sorting of mail items. At present, 105 UPU member countries use postcodes as part of their addressing systems.

FEBRUARY 2011
A.9

__________

__________

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

# B Nomenclature

## B.1 ASC X12 Nomenclature

### B.1.1 Interchange and Application Control Structures

Appendix B is provided as a reference to the X12 syntax, usage, and related information. It is not a full statement of Interchange and Control Structure rules. The full X12 Interchange and Control Structures and other rules (X12.5, X12.6, X12.59, X12 dictionaries, other X12 standards and official documents) apply unless specifically modified in the detailed instructions of this implementation guide (see Section B.1.1.3.1.2 - *Decimal* for an example of such a modification).

### B.1.1.1 Interchange Control Structure

The transmission of data proceeds according to very strict format rules to ensure the integrity and maintain the efficiency of the interchange. Each business grouping of data is called a transaction set. For instance, a group of benefit enrollments sent from a sponsor to a payer is considered a transaction set.

Each transaction set contains groups of logically related data in units called segments. For instance, the N4 segment used in the transaction set conveys the city, state, ZIP Code, and other geographic information. A transaction set contains multiple segments, so the addresses of the different parties, for example, can be conveyed from one computer to the other. An analogy would be that the transaction set is like a freight train; the segments are like the train's cars; and each segment can contain several data elements the same as a train car can hold multiple crates.

The sequence of the elements within one segment is specified by the ASC X12 standard as well as the sequence of segments in the transaction set. In a more conventional computing environment, the segments would be equivalent to records, and the elements equivalent to fields.

Similar transaction sets, called "functional groups," can be sent together within a transmission. Each functional group is prefaced by a group start segment; and a functional group is terminated by a group end segment. One or more functional groups are prefaced by an interchange header and followed by an interchange trailer.

Figure B.1 - *Transmission Control Schematic*, illustrates this interchange control.

FEBRUARY 2011
B.1

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

![img-47.jpeg](img-47.jpeg)
Figure B.1 - Transmission Control Schematic

The interchange header and trailer segments envelop one or more functional groups or interchange-related control segments and perform the following functions:

1. Define the data element separators and the data segment terminator.
2. Identify the sender and receiver.
3. Provide control information for the interchange.
4. Allow for authorization and security information.

## B.1.1.2 Application Control Structure Definitions and Concepts

## B.1.1.2.1 Basic Structure

A data element corresponds to a data field in data processing terminology. A data segment corresponds to a record in data processing terminology. The data segment

B.2

FEBRUARY 2011

CONSOLIDATED · 834

BENEFIT ENROLLMENT AND MAINTENANCE

005010X220 &amp; 005010X220A1

begins with a segment ID and contains related data elements. A control segment has the same structure as a data segment; the distinction is in the use. The data segment is used primarily to convey user information, but the control segment is used primarily to convey control information and to group data segments.

## B.1.1.2.2 Basic Character Set

The section that follows is designed to have representation in the common character code schemes of EBCDIC, ASCII, and CCITT International Alphabet 5. The ASC X12 standards are graphic-character-oriented; therefore, common character encoding schemes other than those specified herein may be used as long as a common mapping is available. Because the graphic characters have an implied mapping across character code schemes, those bit patterns are not provided here.

The basic character set of this standard, shown in Table B.1 - Basic Character Set, includes those selected from the uppercase letters, digits, space, and special characters as specified below.

Table B.1 - Basic Character Set

|  A...Z | 0...9 | ! | " | & | ' | ( | ) | + | *  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  , | - | . | / | : | ; | ? | = | "!" (space) |   |

## B.1.1.2.3 Extended Character Set

An extended character set may be used by negotiation between the two parties and includes the lowercase letters and other special characters as specified in Table B.2 - Extended Character Set.

Table B.2 - Extended Character Set

|  a...z | % | ~ | @ | [ | ] | _ | { | }  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  \ | | | < | > | ^ | ` | # | $ |   |

Note that the extended characters include several character codes that have multiple graphical representations for a specific bit pattern. The complete list appears in other standards such as CCITT S.5. Use of the USA graphics for these codes presents no problem unless data is exchanged with an international partner. Other problems, such as the translation of item descriptions from English to French, arise when exchanging data with an international partner, but minimizing the use of codes with multiple graphics eliminates one of the more obvious problems.

FEBRUARY 2011

B.3

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

For implementations compliant with this guide, either the entire extended character set must be acceptable, or the entire extended character set must not be used. In the absence of a specific trading partner agreement to the contrary, trading partners will assume that the extended character set is acceptable. Use of the extended character set allows the use of the "@" character in email addresses within the PER segment. Users should note that characters in the extended character set, as well as the basic character set, may be used as delimiters only when they do not occur in the data as stated in Section B.1.1.2.4.1 - Base Control Set.

## B.1.1.2.4 Control Characters

Two control character groups are specified; they have restricted usage. The common notation for these groups is also provided, together with the character coding in three common alphabets. In Table B.3 - Base Control Set, the column IA5 represents CCITT V.3 International Alphabet 5.

## B.1.1.2.4.1 Base Control Set

The base control set includes those characters that will not have a disruptive effect on most communication protocols. These are represented by:

Table B.3 - Base Control Set

|  NOTATION | NAME | EBCDIC | ASCII | IA5  |
| --- | --- | --- | --- | --- |
|  BEL | bell | 2F | 07 | 07  |
|  HT | horizontal tab | 05 | 09 | 09  |
|  LF | line feed | 25 | 0A | 0A  |
|  VT | vertical tab | 0B | 0B | 0B  |
|  FF | form feed | 0C | 0C | 0C  |
|  CR | carriage return | 0D | 0D | 0D  |
|  FS | file separator | 1C | 1C | 1C  |
|  GS | group separator | 1D | 1D | 1D  |
|  RS | record separator | 1E | 1E | 1E  |
|  US | unit separator | 1F | 1F | 1F  |
|  NL | new line | 15 |  |   |

FEBRUARY 2011

CONSOLIDATED · 834

BENEFIT ENROLLMENT AND MAINTENANCE

005010X220 &amp; 005010X220A1

The Group Separator (GS) may be an exception in this set because it is used in the 3780 communications protocol to indicate blank space compression.

## B.1.1.2.4.2 Extended Control Set

The extended control set includes those that may have an effect on a transmission system. These are shown in Table B.4 - Extended Control Set.

Table B.4 - Extended Control Set

|  NOTATION | NAME | EBCDIC | ASCII | IA5  |
| --- | --- | --- | --- | --- |
|  SOH | start of header | 01 | 01 | 01  |
|  STX | start of text | 02 | 02 | 02  |
|  ETX | end of text | 03 | 03 | 03  |
|  EOT | end of transmission | 37 | 04 | 04  |
|  ENQ | enquiry | 2D | 05 | 05  |
|  ACK | acknowledge | 2E | 06 | 06  |
|  DC1 | device control 1 | 11 | 11 | 11  |
|  DC2 | device control 2 | 12 | 12 | 12  |
|  DC3 | device control 3 | 13 | 13 | 13  |
|  DC4 | device control 4 | 3C | 14 | 14  |
|  NAK | negative acknowledge | 3D | 15 | 15  |
|  SYN | synchronous idle | 32 | 16 | 16  |
|  ETB | end of block | 26 | 17 | 17  |

## B.1.1.2.5 Delimiters

A delimiter is a character used to separate two data elements or component elements or to terminate a segment. The delimiters are an integral part of the data.

Delimiters are specified in the interchange header segment, ISA. The ISA segment can be considered in implementations compliant with this guide (see Appendix C, ISA Segment Note 1) to be a 105 byte fixed length record, followed by a segment terminator. The data element separator is byte number 4; the repetition separator is byte number

FEBRUARY 2011

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

83; the component element separator is byte number 105; and the segment terminator is the byte that immediately follows the component element separator.

Once specified in the interchange header, the delimiters are not to be used in a data element value elsewhere in the interchange. For consistency, this implementation guide uses the delimiters shown in Table B.5 - Delimiters, in all examples of EDI transmissions.

Table B.5 - Delimiters
|  CHARACTER | NAME | DELIMITER  |
| --- | --- | --- |
|  * | Asterisk | Data Element Separator  |
|  ^ | Carat | Repetition Separator  |
|  : | Colon | Component Element Separator  |
|  ~ | Tilde | Segment Terminator  |

The delimiters above are for illustration purposes only and are not specific recommendations or requirements. Users of this implementation guide should be aware that an application system may use some valid delimiter characters within the application data. Occurrences of delimiter characters in transmitted data within a data element will result in errors in translation. The existence of asterisks (*) within transmitted application data is a known issue that can affect translation software.

## B.1.1.3 Business Transaction Structure Definitions and Concepts

The ASC X12 standards define commonly used business transactions (such as a health care claim) in a formal structure called "transaction sets." A transaction set is composed of a transaction set header control segment, one or more data segments, and a transaction set trailer control segment. Each segment is composed of the following:

- A unique segment ID
- One or more logically related data elements each preceded by a data element separator
- A segment terminator

## B.1.1.3.1 Data Element

The data element is the smallest named unit of information in the ASC X12 standard. Data elements are identified as either simple or component. A data element that occurs as an ordinally positioned member of a composite data structure is identified as a component data element. A data element that occurs in a segment outside the defined boundaries of a composite data structure is identified as a simple data element. The

FEBRUARY 2011

CONSOLIDATED · 834

BENEFIT ENROLLMENT AND MAINTENANCE

005010X220 &amp; 005010X220A1

distinction between simple and component data elements is strictly a matter of context because a data element can be used in either capacity.

Data elements are assigned a unique reference number. Each data element has a name, description, type, minimum length, and maximum length. For ID type data elements, this guide provides the applicable ASC X12 code values and their descriptions or references where the valid code list can be obtained.

A simple data element within a segment may have an attribute indicating that it may occur once or a specific number of times more than once. The number of permitted repeats are defined as an attribute in the individual segment where the repeated data element occurs.

Each data element is assigned a minimum and maximum length. The length of the data element value is the number of character positions used except as noted for numeric, decimal, and binary elements.

The data element types shown in Table B.6 - Data Element Types, appear in this implementation guide.

Table B.6 - Data Element Types

|  SYMBOL | TYPE  |
| --- | --- |
|  Nn | Numeric  |
|  R | Decimal  |
|  ID | Identifier  |
|  AN | String  |
|  DT | Date  |
|  TM | Time  |
|  B | Binary  |

The data element minimum and maximum lengths may be restricted in this implementation guide for a compliant implementation. Such restrictions may occur by virtue of the allowed qualifier for the data element or by specific instructions regarding length or format as stated in this implementation guide.

FEBRUARY 2011

B.7

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

## B.1.1.3.1.1 Numeric

A numeric data element is represented by one or more digits with an optional leading sign representing a value in the normal base of 10. The value of a numeric data element includes an implied decimal point. It is used when the position of the decimal point within the data is permanently fixed and is not to be transmitted with the data.

This set of guides denotes the number of implied decimal positions. The representation for this data element type is "Nn" where N indicates that it is numeric and n indicates the number of decimal positions to the right of the implied decimal point.

If n is 0, it need not appear in the specification; N is equivalent to N0. For negative values, the leading minus sign (-) is used. Absence of a sign indicates a positive value. The plus sign (+) must not be transmitted.

## EXAMPLE

A transmitted value of 1234, when specified as numeric type N2, represents a value of 12.34.

Leading zeros must be suppressed unless necessary to satisfy a minimum length requirement. The length of a numeric type data element does not include the optional sign.

## B.1.1.3.1.2 Decimal

A decimal data element may contain an explicit decimal point and is used for numeric values that have a varying number of decimal positions. This data element type is represented as "R."

The decimal point always appears in the character stream if the decimal point is at any place other than the right end. If the value is an integer (decimal point at the right end) the decimal point must be omitted. For negative values, the leading minus sign (-) is used. Absence of a sign indicates a positive value. The plus sign (+) must not be transmitted.

Leading zeros must be suppressed unless necessary to satisfy a minimum length requirement. Trailing zeros following the decimal point must be suppressed unless necessary to indicate precision. The use of triad separators (for example, the commas in 1,000,000) is expressly prohibited. The length of a decimal type data element does not include the optional leading sign or decimal point.

## EXAMPLE

A transmitted value of 12.34 represents a decimal value of 12.34.

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

While the ASC X12 standard supports usage of exponential notation, this guide prohibits that usage.

For implementation of this guide under the rules promulgated under the Health Insurance Portability and Accountability Act (HIPAA), decimal data elements in Data Element 782 (Monetary Amount) will be limited to a maximum length of 10 characters including reported or implied places for cents (implied value of 00 after the decimal point). Note the statement in the preceding paragraph that the decimal point and leading sign, if sent, are not part of the character count.

## EXAMPLE

For implementations mandated under HIPAA rules:

- The following transmitted value represents the largest positive dollar amount that can be sent: 99999999.99
- The following transmitted value is the longest string of characters that can be sent representing whole dollars: 99999999
- The following transmitted value is the longest string of characters that can be sent representing negative dollars and cents: -99999999.99
- The following transmitted value is the longest string of characters that can be sent representing negative whole dollars: -99999999

## B.1.1.3.1.3 Identifier

An identifier data element always contains a value from a predefined list of codes that is maintained by the ASC X12 Committee or some other body recognized by the Committee. Trailing spaces must be suppressed unless they are necessary to satisfy a minimum length. An identifier is always left justified. The representation for this data element type is "ID."

## B.1.1.3.1.4 String

A string data element is a sequence of any characters from the basic or extended character sets. The string data element must contain at least one non-space character. The significant characters shall be left justified. Leading spaces, when they occur, are presumed to be significant characters. Trailing spaces must be suppressed unless they are necessary to satisfy a minimum length. The representation for this data element type is "AN."

## B.1.1.3.1.5 Date

A date data element is used to express the standard date in either YYMMDD or CCYYMMDD format in which CC is the first two digits of the calendar year, YY is the last two digits of the calendar year, MM is the month (01 to 12), and DD is the day in the

FEBRUARY 2011
B.9

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

month (01 to 31). The representation for this data element type is "DT." Users of this guide should note that all dates within transactions are 8-character dates (millennium compliant) in the format CCYYMMDD. The only date data element that is in format YYMMDD is the Interchange Date data element in the ISA segment and the TA1 segment where the century is easily determined because of the nature of an interchange header.

## B.1.1.3.1.6 Time

A time data element is used to express the ISO standard time HHMMSSd..d format in which HH is the hour for a 24 hour clock (00 to 23), MM is the minute (00 to 59), SS is the second (00 to 59) and d..d is decimal seconds. The representation for this data element type is "TM." The length of the data element determines the format of the transmitted time.

### EXAMPLE

Transmitted data elements of four characters denote HHMM. Transmitted data elements of six characters denote HHMMSS.

## B.1.1.3.1.7 Binary

The binary data element is any sequence of octets ranging in value from binary 00000000 to binary 11111111. This data element type has no defined maximum length. Actual length is specified by the immediately preceding data element. Within the body of a transaction set (from ST to SE) implemented according to this technical report, the binary data element type is only used in the segments Binary Data Segment BIN, and Binary Data Structure BDS. Within those segments, Data Element 785 Binary Data is a string of octets which can assume any binary pattern from hexadecimal 00 to FF, and can be used to send text as well as coded data, including data from another application in its native format. The binary data type is also used in some control and security structures.

Not all transaction sets use the Binary Data Segment BIN or Binary Data Structure BDS.

## B.1.1.3.2 Repeating Data Elements

Simple or composite data elements within a segment can be designated as repeating data elements. Repeating data elements are adjacent data elements that occur up to a number of times specified in the standard as number of repeats. The implementation guide may also specify the number of repeats of a repeating data element in a specific location in the transaction that are permitted in a compliant implementation. Adjacent occurrences of the same repeating simple data element or composite data structure in a segment shall be separated by a repetition separator.

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

## B.1.1.3.3 Composite Data Structure

The composite data structure is an intermediate unit of information in a segment. Composite data structures are composed of one or more logically related simple data elements, each, except the last, followed by a sub-element separator. The final data element is followed by the next data element separator or the segment terminator. Each simple data element within a composite is called a component.

Each composite data structure has a unique four-character identifier, a name, and a purpose. The identifier serves as a label for the composite. A composite data structure can be further defined through the use of syntax notes, semantic notes, and comments. Each component within the composite is further characterized by a reference designator and a condition designator. The reference designators and the condition designators are described in Section B.1.1.3.8 - Reference Designator and Section B.1.1.3.9 - Condition Designator.

A composite data structure within a segment may have an attribute indicating that it may occur once or a specific number of times more than once. The number of permitted repeats are defined as an attribute in the individual segment where the repeated composite data structure occurs.

## B.1.1.3.4 Data Segment

The data segment is an intermediate unit of information in a transaction set. In the data stream, a data segment consists of a segment identifier, one or more composite data structures or simple data elements each preceded by a data element separator and succeeded by a segment terminator.

Each data segment has a unique two- or three-character identifier, a name, and a purpose. The identifier serves as a label for the data segment. A segment can be further defined through the use of syntax notes, semantic notes, and comments. Each simple data element or composite data structure within the segment is further characterized by a reference designator and a condition designator.

## B.1.1.3.5 Syntax Notes

Syntax notes describe relational conditions among two or more data segment units within the same segment, or among two or more component data elements within the same composite data structure. For a complete description of the relational conditions, See Section B.1.1.3.9 - Condition Designator.

FEBRUARY 2011
B.11

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

## B.1.1.3.6 Semantic Notes

Simple data elements or composite data structures may be referenced by a semantic note within a particular segment. A semantic note provides important additional information regarding the intended meaning of a designated data element, particularly a generic type, in the context of its use within a specific data segment. Semantic notes may also define a relational condition among data elements in a segment based on the presence of a specific value (or one of a set of values) in one of the data elements.

## B.1.1.3.7 Comments

A segment comment provides additional information regarding the intended use of the segment.

## B.1.1.3.8 Reference Designator

Each simple data element or composite data structure in a segment is provided a structured code that indicates the segment in which it is used and the sequential position within the segment. The code is composed of the segment identifier followed by a two-digit number that defines the position of the simple data element or composite data structure in that segment.

For purposes of creating reference designators, the composite data structure is viewed as the hierarchical equal of the simple data element. Each component data element in a composite data structure is identified by a suffix appended to the reference designator for the composite data structure of which it is a member. This suffix is prefixed with a hyphen and defines the position of the component data element in the composite data structure.

### EXAMPLE

- The first simple element of the CLP segment would be identified as CLP01.
- The first position in the SVC segment is occupied by a composite data structure that contains seven component data elements, the reference designator for the second component data element would be SVC01-02.

## B.1.1.3.9 Condition Designator

This section provides information about X12 standard conditions designators. It is provided so that users will have information about the general standard. Implementation guides may impose other conditions designators. See implementation guide section 2.1 Presentation Examples for detailed information about the implementation guide Industry Usage requirements for compliant implementation.

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

Data element conditions are of three types: mandatory, optional, and relational. They define the circumstances under which a data element may be required to be present or not present in a particular segment.

FEBRUARY 2011
B.13

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

Table B.7 - Condition Designator

|  DESIGNATOR | DESCRIPTION  |   |
| --- | --- | --- |
|  M- Mandatory | The designation of mandatory is absolute in the sense that there is no dependency on other data elements. This designation may apply to either simple data elements or composite data structures. If the designation applies to a composite data structure, then at least one value of a component data element in that composite data structure shall be included in the data segment.  |   |
|  O- Optional | The designation of optional means that there is no requirement for a simple data element or composite data structure to be present in the segment. The presence of a value for a simple data element or the presence of value for any of the component data elements of a composite data structure is at the option of the sender.  |   |
|  X- Relational | Relational conditions may exist among two or more simple data elements within the same data segment based on the presence or absence of one of those data elements (presence means a data element must not be empty). Relational conditions are specified by a condition code (see table below) and the reference designators of the affected data elements. A data element may be subject to more than one relational condition.  |   |
|   | The definitions for each of the condition codes used within syntax notes are detailed below:  |   |
|   | CONDITION CODE | DEFINITION  |
|   | P- Paired or Multiple | If any element specified in the relational condition is present, then all of the elements specified must be present.  |
|   | R- Required | At least one of the elements specified in the condition must be present.  |
|   | E- Exclusion | Not more than one of the elements specified in the condition may be present.  |

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

|  DESIGNATOR | DESCRIPTION  |   |
| --- | --- | --- |
|   | C- Conditional | If the first element specified in the condition is present, then all other elements must be present. However, any or all of the elements not specified as the first element in the condition may appear without requiring that the first element be present. The order of the elements in the condition does not have to be the same as the order of the data elements in the data segment.  |
|   | L- List Conditional | If the first element specified in the condition is present, then at least one of the remaining elements must be present. However, any or all of the elements not specified as the first element in the condition may appear without requiring that the first element be present. The order of the elements in the condition does not have to be the same as the order of the data elements in the data segment.  |

## B.1.1.3.10 Absence of Data

Any simple data element that is indicated as mandatory must not be empty if the segment is used. At least one component data element of a composite data structure that is indicated as mandatory must not be empty if the segment is used. Optional simple data elements and/or composite data structures and their preceding data element separators that are not needed must be omitted if they occur at the end of a segment. If they do not occur at the end of the segment, the simple data element values and/or composite data structure values may be omitted. Their absence is indicated by the occurrence of their preceding data element separators, in order to maintain the element's or structure's position as defined in the data segment.

Likewise, when additional information is not necessary within a composite, the composite may be terminated by providing the appropriate data element separator or segment terminator.

If a segment has no data in any data element within the segment (an "empty" segment), that segment must not be sent.

FEBRUARY 2011
B.15

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

## B.1.1.3.11 Control Segments

A control segment has the same structure as a data segment, but it is used for transferring control information rather than application information.

## B.1.1.3.11.1 Loop Control Segments

Loop control segments are used only to delineate bounded loops. Delineation of the loop shall consist of the loop header (LS segment) and the loop trailer (LE segment). The loop header defines the start of a structure that must contain one or more iterations of a loop of data segments and provides the loop identifier for this loop. The loop trailer defines the end of the structure. The LS segment appears only before the first occurrence of the loop, and the LE segment appears only after the last occurrence of the loop. Unbounded looping structures do not use loop control segments.

## B.1.1.3.11.2 Transaction Set Control Segments

The transaction set is delineated by the transaction set header (ST segment) and the transaction set trailer (SE segment). The transaction set header identifies the start and identifier of the transaction set. The transaction set trailer identifies the end of the transaction set and provides a count of the data segments, which includes the ST and SE segments.

## B.1.1.3.11.3 Functional Group Control Segments

The functional group is delineated by the functional group header (GS segment) and the functional group trailer (GE segment). The functional group header starts and identifies one or more related transaction sets and provides a control number and application identification information. The functional group trailer defines the end of the functional group of related transaction sets and provides a count of contained transaction sets.

## B.1.1.3.11.4 Relations among Control Segments

The control segment of this standard must have a nested relationship as is shown and annotated in this subsection. The letters preceding the control segment name are the segment identifier for that control segment. The indentation of segment identifiers shown below indicates the subordination among control segments.

- GS Functional Group Header, starts a group of related transaction sets.
- ST Transaction Set Header, starts a transaction set.
- LS Loop Header, starts a bounded loop of data segments but is not part of the loop.
- LS Loop Header, starts an inner, nested, bounded loop.
- LE Loop Trailer, ends an inner, nested bounded loop.

B.16

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

LE Loop Trailer, ends a bounded loop of data segments but is not part of the loop.

SE Transaction Set Trailer, ends a transaction set.

GE Functional Group Trailer, ends a group of related transaction sets.

More than one ST/SE pair, each representing a transaction set, may be used within one functional group. Also more than one LS/LE pair, each representing a bounded loop, may be used within one transaction set.

## B.1.1.3.12 Transaction Set

The transaction set is the smallest meaningful set of information exchanged between trading partners. The transaction set consists of a transaction set header segment, one or more data segments in a specified order, and a transaction set trailer segment. See Figure B.1 - Transmission Control Schematic.

## B.1.1.3.12.1 Transaction Set Header and Trailer

A transaction set identifier uniquely identifies a transaction set. This identifier is the first data element of the Transaction Set Header Segment (ST). A user assigned transaction set control number in the header must match the control number in the Trailer Segment (SE) for any given transaction set. The value for the number of included segments in the SE segment is the total number of segments in the transaction set, including the ST and SE segments.

## B.1.1.3.12.2 Data Segment Groups

The data segments in a transaction set may be repeated as individual data segments or as unbounded or bounded loops.

## B.1.1.3.12.3 Repeated Occurrences of Single Data Segments

When a single data segment is allowed to be repeated, it may have a specified maximum number of occurrences defined at each specified position within a given transaction set standard. Alternatively, a segment may be allowed to repeat an unlimited number of times. The notation for an unlimited number of repetitions is "&gt;1."

## B.1.1.3.12.4 Loops of Data Segments

Loops are groups of semantically related segments. Data segment loops may be unbounded or bounded.

### Unbounded Loops

To establish the iteration of a loop, the first data segment in the loop must appear once and only once in each iteration. Loops may have a specified maximum number of

FEBRUARY 2011
B.17

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

repetitions. Alternatively, the loop may be specified as having an unlimited number of iterations. The notation for an unlimited number of repetitions is "&gt;1."

A specified sequence of segments is in the loop. Loops themselves are optional or mandatory. The requirement designator of the beginning segment of a loop indicates whether at least one occurrence of the loop is required. Each appearance of the beginning segment defines an occurrence of the loop.

The requirement designator of any segment within the loop after the beginning segment applies to that segment for each occurrence of the loop. If there is a mandatory requirement designator for any data segment within the loop after the beginning segment, that data segment is mandatory for each occurrence of the loop. If the loop is optional, the mandatory segment only occurs if the loop occurs.

# Bounded Loops

The characteristics of unbounded loops described previously also apply to bounded loops. In addition, bounded loops require a Loop Start Segment (LS) to appear before the first occurrence and a Loop End Segment (LE) to appear after the last consecutive occurrence of the loop. If the loop does not occur, the LS and LE segments are suppressed.

# B.1.1.3.12.5 Data Segments in a Transaction Set

When data segments are combined to form a transaction set, three characteristics are applied to each data segment: a requirement designator, a position in the transaction set, and a maximum occurrence.

# B.1.1.3.12.6 Data Segment Requirement Designators

A data segment, or loop, has one of the following requirement designators for health care and insurance transaction sets, indicating its appearance in the data stream of a transmission. These requirement designators are represented by a single character code.

Table B.8 - Data Segment Requirement Designators

|  DESIGNATOR | DESCRIPTION  |
| --- | --- |
|  M- Mandatory | This data segment must be included in the transaction set. (Note that a data segment may be mandatory in a loop of data segments, but the loop itself is optional if the beginning segment of the loop is designated as optional.)  |
|  O- Optional | The presence of this data segment is the option of the sending party.  |

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

## B.1.1.3.12.7 Data Segment Position

The ordinal positions of the segments in a transaction set are explicitly specified for that transaction. Subject to the flexibility provided by the optional requirement designators of the segments, this positioning must be maintained.

## B.1.1.3.12.8 Data Segment Occurrence

A data segment may have a maximum occurrence of one, a finite number greater than one, or an unlimited number indicated by "&gt;1."

## B.1.1.3.13 Functional Group

A functional group is a group of similar transaction sets that is bounded by a functional group header segment and a functional group trailer segment. The functional identifier defines the group of transactions that may be included within the functional group. The value for the functional group control number in the header and trailer control segments must be identical for any given group. The value for the number of included transaction sets is the total number of transaction sets in the group. See Figure B.1 - Transmission Control Schematic.

## B.1.1.4 Envelopes and Control Structures

### B.1.1.4.1 Interchange Control Structures

Typically, the term "interchange" connotes the ISA/IEA envelope that is transmitted between trading/business partners. Interchange control is achieved through several "control" components. The interchange control number is contained in data element ISA13 of the ISA segment. The identical control number must also occur in data element 02 of the IEA segment. Most commercial translation software products will verify that these two elements are identical. In most translation software products, if these elements are different the interchange will be "suspended" in error.

There are many other features of the ISA segment that are used for control measures. For instance, the ISA segment contains data elements such as authorization information, security information, sender identification, and receiver identification that can be used for control purposes. These data elements are agreed upon by the trading partners prior to transmission. The interchange date and time data elements as well as the interchange control number within the ISA segment are used for debugging purposes when there is a problem with the transmission or the interchange.

Data Element ISA12, Interchange Control Version Number, indicates the version of the ISA/IEA envelope. GS08 indicates the version of the transaction sets contained within the ISA/IEA envelope. The versions are not required to be the same. An Interchange

FEBRUARY 2011
B.19

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

Acknowledgment can be requested through data element ISA14. The interchange acknowledgment is the TA1 segment. Data element ISA15, Test Indicator, is used between trading partners to indicate that the transmission is in a "test" or "production" mode. Data element ISA16, Subelement Separator, is used by the translator for interpretation of composite data elements.

The ending component of the interchange or ISA/IEA envelope is the IEA segment. Data element IEA01 indicates the number of functional groups that are included within the interchange. In most commercial translation software products, an aggregate count of functional groups is kept while interpreting the interchange. This count is then verified with data element IEA01. If there is a discrepancy, in most commercial products, the interchange is suspended. The other data element in the IEA segment is IEA02 which is referenced above.

See Appendix C, EDI Control Directory, for a complete detailing of the inter-change control header and trailer. The authors recommend that when two transactions with different X12 versions numbers are sent in one interchange control structure (multiple functional groups within one ISA/IEA envelope), the Interchange Control version used should be that of the most recent transaction version included in the envelope. For the transmission of HIPAA transactions with mixed versions, this would be a compliant enveloping structure.

## B.1.1.4.2 Functional Groups

Control structures within the functional group envelope include the functional identifier code in GS01. The Functional Identifier Code is used by the commercial translation software during interpretation of the interchange to determine the different transaction sets that may be included within the functional group. If an inappropriate transaction set is contained within the functional group, most commercial translation software will suspend the functional group within the interchange. The Application Sender's Code in GS02 can be used to identify the sending unit of the transmission. The Application Receiver's Code in GS03 can be used to identify the receiving unit of the transmission. The functional group contains a creation date (GS04) and creation time (GS05) for the functional group. The Group Control Number is contained in GS06. These data elements (GS04, GS05, and GS06) can be used for debugging purposes. GS08, Version/Release/Industry Identifier Code is the version/release/sub-release of the transaction sets being transmitted in this functional group.

The Functional Group Control Number in GS06 must be identical to data element 02 of the GE segment. Data element GE01 indicates the number of transaction sets within the functional group. In most commercial translation software products, an aggregate

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

count of the transaction sets is kept while interpreting the functional group. This count is then verified with data element GE01.

See Appendix C, EDI Control Directory, for a complete detailing of the functional group header and trailer.

## B.1.1.4.3 HL Structures

The HL segment is used in several X12 transaction sets to identify levels of detail information using a hierarchical structure, such as relating dependents to a subscriber. Hierarchical levels may differ from guide to guide.

For example, each provider can bill for one or more subscribers, each subscriber can have one or more dependents and the subscriber and the dependents can make one or more claims.

Each guide states what levels are available, the level's usage, number of repeats, and whether that level has subordinate levels within a transaction set.

For implementations compliant with this guide, the repeats of the loops identified by the HL structure shall appear in the hierarchical order specified in BHT01, when those particular hierarchical levels exist. That is, an HL parent loop must be followed by the subordinate child loops, if any, prior to commencing a new HL parent loop at the same hierarchical level.

The following diagram, from transaction set 837, illustrates a typical hierarchy.

|  Dependents | Subscribers | Provider  |
| --- | --- | --- |

The two examples below illustrate this requirement:

## Example 1 based on Implementation Guide 811X201: INSURER

- First STATE in transaction (child of INSURER)
- First POLICY in transaction (child of first STATE)
- First VEHICLE in transaction (child of first POLICY)
- Second POLICY in transaction (child of first STATE)
- Second VEHICLE in transaction (child of second POLICY)
- Third VEHICLE in transaction (child of second POLICY)

FEBRUARY 2011
B.21

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

Second STATE in transaction (child of INSURER)
Third POLICY in transaction (child of second STATE)
Fourth VEHICLE in transaction (child of third POLICY)

## Example 2 based on Implementation Guide 837X141

First PROVIDER in transaction
First SUBSCRIBER in transaction (child of first PROVIDER)

Second PROVIDER in transaction
Second SUBSCRIBER in transaction (child of second PROVIDER)
First DEPENDENT in transaction (child of second SUBSCRIBER)
Second DEPENDENT in transaction (child of second SUBSCRIBER)
Third SUBSCRIBER in transaction (child of second PROVIDER)

Third PROVIDER in transaction
Fourth SUBSCRIBER in transaction (child of third PROVIDER)
Fifth SUBSCRIBER in transaction (child of third PROVIDER)
Third DEPENDENT in transaction (child of fifth SUBSCRIBER)

## B.1.1.5 Acknowledgments

## B.1.1.5.1 Interchange Acknowledgment, TA1

The TA1 segment provides the capability for the interchange receiver to notify the sender that a valid envelope was received or that problems were encountered with the interchange control structure. The TA1 verifies the envelopes only. Transaction set-specific verification is accomplished through use of the Functional Acknowledgment Transaction Set, 997. See Section B.1.1.5.2 - Functional Acknowledgment, 997, for more details. The TA1 is unique in that it is a single segment transmitted without the GS/GE envelope structure. A TA1 can be included in an interchange with other functional groups and transactions.

Encompassed in the TA1 are the interchange control number, interchange date and time, interchange acknowledgment code, and the interchange note code. The interchange control number, interchange date and time are identical to those that were present in the transmitted interchange from the trading partner. This provides the capability to associate the TA1 with the transmitted interchange. TA104, Interchange Acknowledgment Code, indicates the status of the interchange control structure. This data element stipulates whether the transmitted interchange was accepted with no errors, accepted with errors, or rejected because of errors. TA105, Interchange Note Code, is a numerical code that indicates the error found while processing the interchange control structure. Values for this data element indicate whether the error occurred at the interchange or functional group envelope.

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

## B.1.1.5.2 Functional Acknowledgment, 997

The Functional Acknowledgment Transaction Set, 997, has been designed to allow trading partners to establish a comprehensive control function as a part of their business exchange process. This acknowledgment process facilitates control of EDI. There is a one-to-one correspondence between a 997 and a functional group. Segments within the 997 can identify the acceptance or rejection of the functional group, transaction sets or segments. Data elements in error can also be identified. There are many EDI implementations that have incorporated the acknowledgment process in all of their electronic communications. The 997 is used as a functional acknowledgment to a previously transmitted functional group.

The 997 is a transaction set and thus is encapsulated within the interchange control structure (envelopes) for transmission.

## B.2 Object Descriptors

Object Descriptors (OD) provide a method to uniquely identify specific locations within an implementation guide. There is an OD assigned at every level of the X12N implementation:

1. Transaction Set
2. Loop
3. Segment
4. Composite Data Element
5. Component Data Element
6. Simple Data Element

ODs at the first four levels are coded using X12 identifiers separated by underbars:

|  Entity | Example  |
| --- | --- |
|  1. Transaction Set Identifier plus a unique 2 character value | 837Q1  |
|  2. Above plus under bar plus Loop Identifier as assigned within an implementation guide | 837Q1_2330C  |
|  3. Above plus under bar plus Segment Identifier | 837Q1_2330C_NM1  |

FEBRUARY 2011
B.23

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED · 834

|  Entity | Example  |
| --- | --- |
|  4. Above plus Reference Designator plus under bar plus Composite Identifier | 837Q1_2400_SV101_C003  |

The fifth and sixth levels add a name derived from the "Industry Term" defined in the X12N Data Dictionary. The name is derived by removing the spaces.

|  Entity | Example  |
| --- | --- |
|  5. Number 4 above plus composite sequence plus under bar plus name | 837Q1_2400_SV101_C00302_ProcedureCode  |
|  6. Number 3 above plus Reference Designator plus two under bars plus name | 837Q1_2330C_NM109__OtherPayerPatientPrimaryIdentifier  |

Said in another way, ODs contain a coded component specifying a location in an implementation guide, a separator, and a name portion. For example:

![img-48.jpeg](img-48.jpeg)

Since ODs are unique across all X12N implementation guides, they can be used for a variety of purposes. For example, as a cross reference to older data transmission systems, like the National Standard Format for health care claims, or to form XML tags for newer data transmission systems.

B.24

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

## C EDI Control Directory

### C.1 Control Segments

- ISA
Interchange Control Header Segment
- GS
Functional Group Header Segment
- GE
Functional Group Trailer Segment
- IEA
Interchange Control Trailer Segment

FEBRUARY 2011
C.1

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1
CONSOLIDATED • 834

C.2

FEBRUARY 2011

CONSOLIDATED • 834
CONTROL SEGMENTS

# SEGMENT DETAIL

## ISA - INTERCHANGE CONTROL HEADER

X12 Segment Name: Interchange Control Header

X12 Purpose: To start and identify an interchange of zero or more functional groups and interchange-related control segments

Usage: REQUIRED

TR3 Notes:
1. All positions within each of the data elements must be filled.
2. For compliant implementations under this implementation guide, ISA13, the interchange Control Number, must be a positive unsigned number. Therefore, the ISA segment can be considered a fixed record length segment.
3. The first element separator defines the element separator to be used through the entire interchange.
4. The ISA segment terminator defines the segment terminator used throughout the entire interchange.
5. Spaces in the example interchanges are represented by “.” for clarity.

TR3 Example: ISA*00*...*01*SECRET...*ZZ*SUBMITTERS.ID..*ZZ* RECEIVERS.ID...*030101*1253*^*00501*000000905*1*T*:~

# DIAGRAM

![img-49.jpeg](img-49.jpeg)

FEBRUARY 2011
C.3

CONTROL SEGMENTS

CONSOLIDATED • 834

ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME |   |   | ATTRIBUTES  |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  REQUIRED | ISA01 | I01 | Authorization Information Qualifier |   |   | M 1 | ID 2/2  |
|   |   |   |  Code identifying the type of information in the Authorization Information |   |   |  |   |
|   |   |   |  CODE | DEFINITION |   |  |   |
|   |   |   |  00 | No Authorization Information Present (No Meaningful Information in I02) |   |  |   |
|  REQUIRED | ISA02 | I02 | 03 | Additional Data Identification |   |  |   |
|   |   |   |  Authorization Information |   | M 1 | AN 10/10 |   |
|  Information used for additional identification or authorization of the interchange sender or the data in the interchange; the type of information is set by the Authorization Information Qualifier (I01)  |   |   |   |   |   |   |   |
|  REQUIRED | ISA03 | I03 | Security Information Qualifier |   | M 1 | ID 2/2 |   |
|   |   |   |  Code identifying the type of information in the Security Information |   |  |  |   |
|   |   |   |  CODE | DEFINITION |   |  |   |
|   |   |   |  00 | No Security Information Present (No Meaningful Information in I04) |   |  |   |
|  REQUIRED | ISA04 | I04 | 01 | Password |   |  |   |
|   |   |   |  Security Information |   | M 1 | AN 10/10 |   |
|  This is used for identifying the security information about the interchange sender or the data in the interchange; the type of information is set by the Security Information Qualifier (I03)  |   |   |   |   |   |   |   |
|  REQUIRED | ISA05 | I05 | Interchange ID Qualifier |   | M 1 | ID 2/2 |   |
|   |   |   |  Code indicating the system/method of code structure used to designate the sender or receiver ID element being qualified |   |  |  |   |
|   |   |   |  This ID qualifies the Sender in ISA06. |   |  |  |   |
|   |   |   |  CODE | DEFINITION |   |  |   |
|   |   |   |  01 | Duns (Dun & Bradstreet) |   |  |   |
|   |   |   |  14 | Duns Plus Suffix |   |  |   |
|   |   |   |  20 | Health Industry Number (HIN) |   |  |   |
|   |   |   |  27 | CODE SOURCE 121: Health Industry Number |   |  |   |
|   |   |   |  28 | Carrier Identification Number as assigned by Health Care Financing Administration (HCFA) |   |  |   |
|   |   |   |  29 | Fiscal Intermediary Identification Number as assigned by Health Care Financing Administration (HCFA) |   |  |   |
|   |   |   |  30 | Medicare Provider and Supplier Identification Number as assigned by Health Care Financing Administration (HCFA) |   |  |   |
|   |   |   |  33 | U.S. Federal Tax Identification Number |   |  |   |
|  REQUIRED | ISA06 | I06 | ZZ Mutually Defined |   |  |  |   |
|   |   |   | Interchange Sender ID |   | M 1 | AN 15/15 |   |

FEBRUARY 2011

CONSOLIDATED • 834
CONTROL SEGMENTS

|  REQUIRED | ISA07 | I05 | Interchange ID Qualifier | M 1 | ID | 2/2  |
| --- | --- | --- | --- | --- | --- | --- |
|   |  |  | Code indicating the system/method of code structure used to designate the sender or receiver ID element being qualified  |   |   |   |
|   |  |  | This ID qualifies the Receiver in ISA08.  |   |   |   |
|   |  |  | CODE | DEFINITION  |   |   |
|   |  |  | 01 | Duns (Dun & Bradstreet)  |   |   |
|   |  |  | 14 | Duns Plus Suffix  |   |   |
|   |  |  | 20 | Health Industry Number (HIN)  |   |   |
|   |  |  |  | CODE SOURCE 121: Health Industry Number  |   |   |
|   |  |  | 27 | Carrier Identification Number as assigned by Health Care Financing Administration (HCFA)  |   |   |
|   |  |  | 28 | Fiscal Intermediary Identification Number as assigned by Health Care Financing Administration (HCFA)  |   |   |
|   |  |  | 29 | Medicare Provider and Supplier Identification Number as assigned by Health Care Financing Administration (HCFA)  |   |   |
|   |  |  | 30 | U.S. Federal Tax Identification Number  |   |   |
|   |  |  | 33 | National Association of Insurance Commissioners Company Code (NAIC)  |   |   |
|   |  |  | ZZ | Mutually Defined  |   |   |
|  REQUIRED | ISA08 | I07 | Interchange Receiver ID | M 1 | AN | 15/15  |
|   |  |  | Identification code published by the receiver of the data; When sending, it is used by the sender as their sending ID, thus other parties sending to them will use this as a receiving ID to route data to them  |   |   |   |
|  REQUIRED | ISA09 | I08 | Interchange Date | M 1 | DT | 6/6  |
|   |  |  | Date of the interchange  |   |   |   |
|   |  |  | The date format is YYMMDD.  |   |   |   |
|  REQUIRED | ISA10 | I09 | Interchange Time | M 1 | TM | 4/4  |
|   |  |  | Time of the interchange  |   |   |   |
|   |  |  | The time format is HHMM.  |   |   |   |
|  REQUIRED | ISA11 | I65 | Repetition Separator | M 1 |  | 1/1  |
|   |  |  | Type is not applicable; the repetition separator is a delimiter and not a data element; this field provides the delimiter used to separate repeated occurrences of a simple data element or a composite data structure; this value must be different than the data element separator, component element separator, and the segment terminator  |   |   |   |
|  REQUIRED | ISA12 | I11 | Interchange Control Version Number | M 1 | ID | 5/5  |
|   |  |  | Code specifying the version number of the interchange control segments  |   |   |   |
|   |  |  | CODE | DEFINITION  |   |   |
|   |  |  | 00501 | Standards Approved for Publication by ASC X12 Procedures Review Board through October 2003  |   |   |
|  REQUIRED | ISA13 | I12 | Interchange Control Number | M 1 | N0 | 9/9  |
|   |  |  | A control number assigned by the interchange sender  |   |   |   |
|   |  |  | The Interchange Control Number, ISA13, must be identical to the associated Interchange Trailer IEA02.  |   |   |   |
|   |  |  | Must be a positive unsigned number and must be identical to the value in IEA02.  |   |   |   |

FEBRUARY 2011
C.5

CONTROL SEGMENTS
CONSOLIDATED • 834

|  REQUIRED | ISA14 | I13 | Acknowledgment Requested | M 1 ID | 1/1  |
| --- | --- | --- | --- | --- | --- |
|   |  |  | Code indicating sender's request for an interchange acknowledgment  |   |   |
|   |  |  | See Section B.1.1.5.1 for interchange acknowledgment information.  |   |   |
|   |  |  | CODE | DEFINITION |   |
|   |  |  | 0 | No Interchange Acknowledgment Requested |   |
|   |  |  | 1 | Interchange Acknowledgment Requested (TA1) |   |
|  REQUIRED | ISA15 | I14 | Interchange Usage Indicator | M 1 ID | 1/1  |
|   |  |  | Code indicating whether data enclosed by this interchange envelope is test, production or information  |   |   |
|   |  |  | CODE | DEFINITION |   |
|   |  |  | P | Production Data |   |
|   |  |  | T | Test Data |   |
|  REQUIRED | ISA16 | I15 | Component Element Separator | M 1 | 1/1  |
|   |  |  | Type is not applicable; the component element separator is a delimiter and not a data element; this field provides the delimiter used to separate component data elements within a composite data structure; this value must be different than the data element separator and the segment terminator  |   |   |

FEBRUARY 2011

CONSOLIDATED • 834
CONTROL SEGMENTS

# SEGMENT DETAIL

## GS - FUNCTIONAL GROUP HEADER

X12 Segment Name: Functional Group Header

X12 Purpose: To indicate the beginning of a functional group and to provide control information

X12 Comments: 1. A functional group of related transaction sets, within the scope of X12 standards, consists of a collection of similar transaction sets enclosed by a functional group header and a functional group trailer.

Usage: REQUIRED

TR3 Example: GS*BE*SENDER CODE*RECEIVER CODE*19991231*0802* 1*X*005010X220A1~

# DIAGRAM

![img-50.jpeg](img-50.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | GS01 | 479 | Functional Identifier Code
Code identifying a group of application related transaction sets | M 1 ID 2/2  |
|   |  |  | This is the 2-character Functional Identifier Code assigned to each transaction set by X12. The specific code for a transaction set defined by this implementation guide is presented in section 1.2, Version Information.  |   |
|  REQUIRED | GS02 | 142 | Application Sender's Code
Code identifying party sending transmission; codes agreed to by trading partners | M 1 AN 2/15  |
|   |  |  | Use this code to identify the unit sending the information.  |   |
|  REQUIRED | GS03 | 124 | Application Receiver's Code
Code identifying party receiving transmission; codes agreed to by trading partners | M 1 AN 2/15  |
|   |  |  | Use this code to identify the unit receiving the information.  |   |
|  REQUIRED | GS04 | 373 | Date
Date expressed as CCYYMMDD where CC represents the first two digits of the calendar year
SEMANTIC: GS04 is the group date.
Use this date for the functional group creation date. | M 1 DT 8/8  |

FEBRUARY 2011
C.7

CONTROL SEGMENTS
CONSOLIDATED • 834

|  REQUIRED | GS05 | 337 | Time | M 1 | TM | 4/8  |
| --- | --- | --- | --- | --- | --- | --- |
|  Time expressed in 24-hour clock time as follows: HHMM, or HHMMSS, or HHMMSSD, or HHMMSSDD, where H = hours (00-23), M = minutes (00-59), S = integer seconds (00-59) and DD = decimal seconds; decimal seconds are expressed as follows: D = tenths (0-9) and DD = hundredths (00-99)  |   |   |   |   |   |   |
|  SEMANTIC: GS05 is the group time.  |   |   |   |   |   |   |
|  Use this time for the creation time. The recommended format is HHMM.  |   |   |   |   |   |   |
|  REQUIRED | GS06 | 28 | Group Control Number | M 1 | N0 | 1/9  |
|  Assigned number originated and maintained by the sender  |   |   |   |   |   |   |
|  SEMANTIC: The data interchange control number GS06 in this header must be identical to the same data element in the associated functional group trailer, GE02.  |   |   |   |   |   |   |
|  For implementations compliant with this guide, GS06 must be unique within a single transmission (that is, within a single ISA to IEA enveloping structure). The authors recommend that GS06 be unique within all transmissions over a period of time to be determined by the sender.  |   |   |   |   |   |   |
|  REQUIRED | GS07 | 455 | Responsible Agency Code | M 1 | ID | 1/2  |
|  Code identifying the issuer of the standard; this code is used in conjunction with Data Element 480  |   |   |   |   |   |   |
|   |   |   | CODE | DEFINITION  |   |   |
|   |   |   | X | Accredited Standards Committee X12  |   |   |
|  REQUIRED | GS08 | 480 | Version / Release / Industry Identifier Code | M 1 | AN | 1/12  |
|  Code indicating the version, release, subrelease, and industry identifier of the EDI standard being used, including the GS and GE segments; if code in DE455 in GS segment is X, then in DE 480 positions 1-3 are the version number; positions 4-6 are the release and subrelease, level of the version; and positions 7-12 are the industry or trade association identifiers (optionally assigned by user); if code in DE455 in GS segment is T, then other formats are allowed  |   |   |   |   |   |   |
|  CODE SOURCE 881: Version / Release / Industry Identifier Code  |   |   |   |   |   |   |
|  This is the unique Version/Release/Industry Identifier Code assigned to an implementation by X12N. The specific code for a transaction set defined by this implementation guide is presented in section 1.2, Version Information.  |   |   |   |   |   |   |
|   |   |   | CODE | DEFINITION  |   |   |
|  005010X220A1 Standards Approved for Publication by ASC X12 Procedures Review Board through October 2003  |   |   |   |   |   |   |

FEBRUARY 2011

CONSOLIDATED • 834
CONTROL SEGMENTS

# SEGMENT DETAIL

## GE - FUNCTIONAL GROUP TRAILER

X12 Segment Name: Functional Group Trailer

X12 Purpose: To indicate the end of a functional group and to provide control information

X12 Comments: 1. The use of identical data interchange control numbers in the associated functional group header and trailer is designed to maximize functional group integrity. The control number is the same as that used in the corresponding header.

Usage: REQUIRED

TR3 Example: GE®1®1~

# DIAGRAM

GE
GE01 97
Number of TS Included
M 1 N0 1/6
GE02 28
Group Ctrl Number
M 1 N0 1/9

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | GE01 | 97 | Number of Transaction Sets Included | M 1 N0 1/6
Total number of transaction sets included in the functional group or interchange (transmission) group terminated by the trailer containing this data element  |
|  REQUIRED | GE02 | 28 | Group Control Number | M 1 N0 1/9
Assigned number originated and maintained by the sender  |

SEMANTIC: The data interchange control number GE02 in this trailer must be identical to the same data element in the associated functional group header, GS06.

FEBRUARY 2011
C.9

CONTROL SEGMENTS
CONSOLIDATED • 834

# SEGMENT DETAIL

## IEA - INTERCHANGE CONTROL TRAILER

X12 Segment Name: Interchange Control Trailer

X12 Purpose: To define the end of an interchange of zero or more functional groups and interchange-related control segments

Usage: REQUIRED

TR3 Example: IEA®1®000000905~

# DIAGRAM

![img-51.jpeg](img-51.jpeg)

# ELEMENT DETAIL

|  USAGE | REF. DES. | DATA ELEMENT | NAME | ATTRIBUTES  |
| --- | --- | --- | --- | --- |
|  REQUIRED | IEA01 | I16 | Number of Included Functional Groups | M 1 N0 1/5  |
|   |  |  | A count of the number of functional groups included in an interchange |   |
|  REQUIRED | IEA02 | I12 | Interchange Control Number | M 1 N0 9/9  |
|   |  |  | A control number assigned by the interchange sender |   |

C.10
FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

# D Change Summary

This Implementation Guide defines X12N implementation 005010X220 of the Benefit Enrollment and Maintenance. It is based on version/release/subrelease 005010 of the ASC X12 standards.

The previous X12N implementation of the Benefit Enrollment and Maintenance was 004050X125. It was based on the version/release/subrelease 004050 of the ASC X12 standards.

Implementation of 005010X220 contains significant changes and clarifications. It can only be used with other trading partners who have also implemented 005010X220. Below is a high-level description of the changes in the implementation of 005010X220.

# Changes to the Section 1

1. Section 1.1 changed version to 5010.
2. Section 1.2 changed version to 5010.
3. Section 1.3.1 updated last paragraph.
4. Section 1.3.2 new paragraph added.
5. Section 1.4.1 wording changed
6. Section 1.4.5 new paragraph added.
7. Section 1.5 new section added.
8. Section 1.6.1 new section added.
9. Section 1.6.2 new section added.
10. Section 1.6.3 new section added.
11. Section 1.4 new section added.

# Changes to the Section 2

## 834 Changes

1. ST03 and ST03 wording changed to match the 837 TR3's.
2. BGN08 added code RX
3. Header QTY segment added. Valid codes are ET, DT, TO.
4. 1000B Header N103 'advised' removed from code value XV.
5. 2000 INS02 note changed.
6. 2000 INS03 note changed for code value 30.
7. 2000 INS13 note changed.
8. 2000 INS04 note changed
9. 2000 INS04 new codes added AA, AB, AC, AD, AE, AF, AG, AH, AJ, AL and EC.
10. 2000 INS04 note changed for codes 22, 26, 27, 28, 29, XN, XT.

FEBRUARY 2011
D.1

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

10. 2000 INS13 changed the usage from 'Not Used' to 'Situational' and added a usage note.
11. 2000 INS17 note changed.
12. 2000 REF increased the repeat to 10.
13. 2000 REF TR3 note corrected.
14. 2000 REF note changed.
15. 2000 REF01 added codes 4A and P5.
16. 2000 DTP increased the repeat to 24 from 22.
17. 2000 DTP note changed.
18. 2000 DTP01 note changed for code 357.
19. 2100A NM104 changed usage from 'Required' to Situational' and added a usage note.
20. 2100A NM108 note changed.
21. 2100A NM109 note changed.
22. 2100A PER note changed.
23. 2100A PER05 note changed.
24. 2100A PER07 note changed.
25. 2100A N3 note changed.
26. 2100A N406 note changed.
27. 2100A DMG03 note changed.
28. 2100A DMG06 note changed.
29. 2100A AMT increase repeat to 7 from 4.
30. 2100A AMT01 added codes R, FK and EBA.
31. 2100A HLH02 note changed.
32. 2100A LUI note changed.
33. 2100A LUI01 note changed.
34. 2100B NM1 note changed.
35. 2100B NM101 note removed.
36. 2100B NM108 note changed.
37. 2100B NM109 note changed.
38. 2100B DMG01 changed usage from 'Required' to 'Situational' and added a usage note.
39. 2100B DMG02 changed usage from 'Required' to 'Situational' and added a usage note.
40. 2100B DMG03 changed usage from 'Required' to 'Situational' and added a usage note.
41. 2100D NM1 note changed.

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

42. 2100D NM105 note changed.
43. 2100D NM106 note changed.
44. 2100D NM107 note changed.
45. 2100D NM108 note changed.
46. 2100D NM109 note changed.
47. 2100D PER note changed.
48. 2100D PER05 note changed.
49. 2100D PER07 note changed.
50. 2100E PER note changed.
51. 2100E PER05 note changed.
52. 2100E PER07 note changed.
53. 2100F NM108 note changed.
54. 2100F NM109 note changed
55. 2100F PER note changed.
56. 2100F PER05 note changed.
57. 2100F PER07 note changed.
58. 2100G NM1 note changed.
59. 2100G NM1 increased repeat from 1 to 13.
60. 2100G NM101 added codes 6Y, 9K, LR, GB, TZ, X4.
61. 2100G NM101 note changed for code EI.
62. 2100G NM104-NM107 - usage changed to situational
63. 2100G NM108 note changed.
64. 2100G NM109 note changed
65. 2100G PER note changed.
66. 2100G PER05 note changed.
67. 2100G PER07 note changed.
68. 2100H new 'Drop-Off Location' loop.
69. 2200 DSB07 note changed and added code ZZ.
70. 2200 DSB08 note changed.
71. 2200 DTP note changed.
72. 2300 REF01 added codes CE, E8, M7, RB, ZX, PID, XX1 and XX2.
73. 2300 REF01 removed notes from codes 17, 9V.
74. 2300 HD03 added codes AC, ADD, AF, AP, AR, LL, and UL.
75. 2300 HD04 note changed.
76. 2300 HD05 note changed.
77. 2300 HD06 usage changed.

FEBRUARY 2011
D.3

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

78. 2300 HD09 changed usage from 'Not Used' to 'Situational' and added a usage note.
79. 2300 DTP01 increased usage to 6.
80. 2300 DTP01 note changed for code 348.
81. 2300 DTP01 note changed for code 349.
82. 2300 DTP01 added codes 300 and 695.
83. 2300 DTP02 added code RD8.
84. 2300 AMT increased repeat to 9.
85. 2300 AMT01 added codes R, FK, EBA and I0.
86. 2300 REF increased repeat to 12 from 4.
87. 2300 REF note added.
88. 2300 IDC01 note changed.
89. 2300 IDC02 note changed.
90. 2310 LX note changed.
91. 2310 NM108 and NM109 note changed.
92. 2310 N3 note changed.
93. 2310 N3 segment added.
94. 2310 N4 note changed.
95. 2310 N405 usage changed.
96. 2310 PER note changed.
97. 2310 PER05 note changed.
98. 2310 PER07 note changed.
99. 2310 PLA segment name changed.
100. 2320 COB04 usage changed to situational.
101. 2320 COB04 code values 1, 48, 50, 35, BB, A4, 54, AG, 90, AL added.
102. 2320 REF note changed.
103. 2330 NM1 loop renamed to Coordination of Benefits Other Insurance Company.
104. 2330 NM1 segment repeat increased to 3.
105. 2330 NM101 code values GW,36 added.
106. 2330 NM103 implementation name changed to Coordination of Benefits In-surer Name.
107. 2330 NM109 implementation name changed to Coordination of Benefits In-surer Identification Code.
108. 2330 NM108 note changed.
109. 2330 NM109 note changed
110. 2330 N3 segment added

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

111. 2330 N4 segment added
112. 2330 PER segment added
113. 2700 new 'Additional Reporting Categories' loop added.
114. 2710 LX new segment added.
115. 2750 N1 new segment added.
116. 2750 REF new segment added
117. 2750 DTP new segment added.

## Changes to Section 3

1. Business Case Scenario 9 added.
2. Business Case Scenario 10 added.

## Changes to Section E

1. Data element definition supplied for Late Enrollment Indicator.
2. Data element definition supplied for Member Reporting Category Effective Date
3. Data element definition supplied for Member Reporting Category Reference ID.
4. Data element definition supplied for Member Reporting Category Name.

FEBRUARY 2011
D.5

BENEFIT ENROLLMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1
CONSOLIDATED • 834

D.6

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLEMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

# E Data Element Glossary

## E.1 Data Element Name Index

This section contains an alphabetic listing of data elements used in this implementation guide. Consult the X12N Data Element Dictionary for a complete list of all X12N Data Elements. Data element names in normal type are generic ASC X12 names. Italic type indicates a health care industry defined name.

![img-52.jpeg](img-52.jpeg)

## Action Code

Code indicating type of action

H | BGN08 | - | 306 ...35
D | 2300 | IDC04 | - | 306 ...153
D | 2310 | PLA01 | - | 306 ...164

## Address Information

Address information.

D | 2330 | N301 | - | 166 ...173
D | 2330 | N302 | - | 166 ...173

## Amount Qualifier Code

Code to qualify amount.

D | 2100A | AMT01 | - | 522 ...81
D | 2300 | AMT01 | - | 522 ...147

## Assigned Number

Number assigned for differentiation within a transaction set.

D | 2310 | LX01 | - | 554 ...154
D | 2700 | LX01 | - | 554 ...179

## Benefit Status Code

The type of coverage under which benefits are paid.

D | 2000 | INS05 | - | 1216 ...51

## Birth Sequence Number

A number indicating the order of birth for the identified person in relationship to family members with the same date of birth.

D | 2000 | INS17 | - | 1470 ...54

## Citizenship Status Code

Code indicating citizenship status

D | 2100A | DMG06 | - | 1066 ...75
D | 2100B | DMG06 | - | 1066 ...92

## Code List Qualifier Code

Code identifying a specific industry code list.

D | 2100A | DMG05 | C056-2 | 1270 ...74
D | 2100A | DMG10 | - | 1270 ...75
D | 2100B | DMG05 | C056-2 | 1270 ...91
D | 2100B | DMG10 | - | 1270 ...92

## Communication Number

Complete communications number including country or area code when applicable

D | 2100A | PER04 | - | 364 ...66
D | 2100A | PER06 | - | 364 ...67
D | 2100A | PER08 | - | 364 ...102
D | 2100D | PER04 | - | 364 ...103
D | 2100D | PER08 | - | 364 ...103
D | 2100E | PER04 | - | 364 ...110
D | 2100E | PER06 | - | 364 ...111
D | 2100F | PER04 | - | 364 ...119
D | 2100F | PER06 | - | 364 ...120
D | 2100F | PER08 | - | 364 ...120
D | 2100G | PER04 | - | 364 ...128
D | 2100G | PER06 | - | 364 ...129
D | 2100G | PER08 | - | 364 ...129
D | 2310 | PER04 | - | 364 ...162
D | 2310 | PER06 | - | 364 ...163
D | 2310 | PER08 | - | 364 ...163
D | 2330 | PER04 | - | 364 ...177

FEBRUARY 2011
E.1

BENEFIT ENROLLEMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

## Communication Number Qualifier

Code identifying the type of communication number.

D | 2100A | PER03 | - | 365 ... 66
D | 2100A | PER05 | - | 365 ... 66
D | 2100A | PER07 | - | 365 ... 67
D | 2100D | PER03 | - | 365 ... 102
D | 2100D | PER05 | - | 365 ... 102
D | 2100D | PER07 | - | 365 ... 103
D | 2100E | PER03 | - | 365 ... 110
D | 2100E | PER05 | - | 365 ... 110
D | 2100E | PER07 | - | 365 ... 111
D | 2100F | PER03 | - | 365 ... 119
D | 2100F | PER05 | - | 365 ... 119
D | 2100F | PER07 | - | 365 ... 120
D | 2100G | PER03 | - | 365 ... 128
D | 2100G | PER05 | - | 365 ... 128
D | 2100G | PER07 | - | 365 ... 129
D | 2310 | PER03 | - | 365 ... 162
D | 2310 | PER05 | - | 365 ... 162
D | 2310 | PER07 | - | 365 ... 163
D | 2330 | PER03 | - | 365 ... 177

## Confidentiality Code

Code indicating the access to insured information.

D | 2000 | INS13 | - | 1165 ... 54

## Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying Event Code

A Qualifying Event is an event under the law which results in loss of coverage for a Qualified Beneficiary.

D | 2000 | INS07 | - | 1219 ... 52

## Contact Function Code

Code identifying the major duty or responsibility of the person or group named.

D | 2100A | PER01 | - | 366 ... 66
D | 2100D | PER01 | - | 366 ... 102
D | 2100E | PER01 | - | 366 ... 110
D | 2100F | PER01 | - | 366 ... 119
D | 2100G | PER01 | - | 366 ... 128
D | 2310 | PER01 | - | 366 ... 162
D | 2330 | PER01 | - | 366 ... 176

## Contract Amount

Fixed monetary amount pertaining to the contract

D | 2100A | AMT02 | - | 782 ... 81
D | 2300 | AMT02 | - | 782 ... 147

## Coordination of Benefits Code

Code identifying whether there is a coordination of benefits

D | 2320 | COB03 | - | 1143 ... 166

## Coordination of Benefits Date

The dates of eligibility for coordination of benefits

D | 2320 | DTP03 | - | 1251 ... 170

## Coordination of Benefits Insurer Identification Code

Code identifying the insurer for coordination of benefits.

D | 2330 | NM109 | - | 67 ... 172

## Coordination of Benefits Insurer Name

Name of the insurer for coordination of benefits.

D | 2330 | NM103 | - | 1035 ... 172

## Coordination of Benefits Other Insurance Company City Name

Name of the city in which the Other Insurance Company exists.

D | 2330 | N401 | - | 19 ... 174

## Coordination of Benefits Other Insurance Company Postal Zone or ZIP Code

Zip code in which the Other Insurance Company exists.

D | 2330 | N403 | - | 116 ... 175

## Coordination of Benefits Other Insurance Company State Code

State in which the Other Insurance Company exists.

D | 2330 | N402 | - | 156 ... 175

## Country Code

Code indicating the geographic location.

D | 2100A | N404 | - | 26 ... 70
D | 2100C | N404 | - | 26 ... 97
D | 2100D | N404 | - | 26 ... 106
D | 2100E | N404 | - | 26 ... 114
D | 2100F | N404 | - | 26 ... 123
D | 2100G | N404 | - | 26 ... 132
D | 2100H | N404 | - | 26 ... 137
D | 2310 | N404 | - | 26 ... 160
D | 2330 | N404 | - | 26 ... 175

## Country Subdivision Code

Code identifying the country subdivision.

D | 2100A | N407 | - | 1715 ... 71
D | 2100C | N407 | - | 1715 ... 97
D | 2100D | N407 | - | 1715 ... 106
D | 2100E | N407 | - | 1715 ... 114
D | 2100F | N407 | - | 1715 ... 123
D | 2100G | N407 | - | 1715 ... 132
D | 2100H | N407 | - | 1715 ... 137
D | 2310 | N407 | - | 1715 ... 160
D | 2330 | N407 | - | 1715 ... 175

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLEMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

## Coverage Level Code
Code indicating the level of coverage being provided for this insured
D | 2300 | HD05 | - | 1207 ... 143

## Coverage Period
The coverage period associated with this premium payment.
D | 2300 | DTP03 | - | 1251 ... 146

## Custodial Parent Address Line
The first line of the address of the individual's parent who has legal custody of the individual.
D | 2100F | N301 | - | 166 ... 121
D | 2100F | N302 | - | 166 ... 121

## Custodial Parent City Name
The city of the individual's parent who has legal custody of the individual.
D | 2100F | N401 | - | 19 ... 122

## Custodial Parent First Name
The first name of the individual's parent who has legal custody of the individual.
D | 2100F | NM104 | - | 1036 ... 116

## Custodial Parent Identifier
The identification number of the individual's parent who has legal custody of the individual.
D | 2100F | NM109 | - | 67 ... 117

## Custodial Parent Last Name
The last name of the individual's parent who has legal custody of the individual.
D | 2100F | NM103 | - | 1035 ... 116

## Custodial Parent Middle Name
The middle name of the individual's parent who has legal custody of the individual.
D | 2100F | NM105 | - | 1037 ... 116

## Custodial Parent Name Prefix
The prefix to the name of the individual's parent who has legal custody of the individual.
D | 2100F | NM106 | - | 1038 ... 116

## Custodial Parent Postal Zone or ZIP Code
The postal ZIP code of the individual's parent who has legal custody of the individual.
D | 2100F | N403 | - | 116 ... 123

## Custodial Parent State Code
The code for the state of the individual's parent who has legal custody of the individual.
D | 2100F | N402 | - | 156 ... 123

## Date Time Period
Expression of a date, a time, or a range of dates, times, or dates and times.
H | | DTP03 | - | 1251 ... 37

## Date Time Period Format
### Qualifier
Code indicating the date format, time format, or date and time format.
H | | DTP02 | - | 1250 ... 37
D | 2000 | INS11 | - | 1250 ... 53
D | 2000 | DTP02 | - | 1250 ... 60
D | 2100A | DMG01 | - | 1250 ... 72
D | 2100B | DMG01 | - | 1250 ... 89
D | 2200 | DTP02 | - | 1250 ... 140
D | 2300 | DTP02 | - | 1250 ... 146
D | 2320 | DTP02 | - | 1250 ... 170
D | 2750 | DTP02 | - | 1250 ... 183

## Date Time Qualifier
Code specifying the type of date or time or both date and time.
H | | DTP01 | - | 374 ... 37
D | 2000 | DTP01 | - | 374 ... 59
D | 2200 | DTP01 | - | 374 ... 140
D | 2300 | DTP01 | - | 374 ... 145
D | 2320 | DTP01 | - | 374 ... 170
D | 2750 | DTP01 | - | 374 ... 183

## Diagnosis Code
An ICD-9-CM Diagnosis Code identifying a diagnosed medical condition.
D | 2200 | DSB08 | - | 1137 ... 139

## Disability Eligibility Date
Date when individual became eligible for disability benefits.
D | 2200 | DTP03 | - | 1251 ... 140

## Disability Type Code
An indicator to describe type of disability.
D | 2200 | DSB01 | - | 1146 ... 138

## Drop Off Location Address Line
The address line of the drop off location.
D | 2100H | N301 | - | 166 ... 135
D | 2100H | N302 | - | 166 ... 135

## Drop Off Location City Name
The city name of the drop off location address.
D | 2100H | N401 | - | 19 ... 136

FEBRUARY 2011
E.3

BENEFIT ENROLLEMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

# Drop Off Location Postal Zone or ZIP Code

The postal ZIP code of the drop off location address.

D | 2100H | N403 | - | 116... 137

# Drop Off Location State Code

The state code of the drop off location address.

D | 2100H | N402 | - | 156... 137

# Employment Class Code

Code indicating category of employee.

D | 2100A | EC01 | - | 1176... 76
D | 2100A | EC02 | - | 1176... 77
D | 2100A | EC03 | - | 1176... 77

# Employment Status Code

A code used to define the employment status of the individual covered by this insurance payer.

D | 2000 | INS08 | - | 584... 52

# Entity Identifier Code

Code identifying an organizational entity, a physical location, property or an individual.

H | 1000A | N101 | - | 98... 39
H | 1000B | N101 | - | 98... 41
H | 1000C | N101 | - | 98... 43
D | 2100A | NM101 | - | 98... 62
D | 2100B | NM101 | - | 98... 86
D | 2100C | NM101 | - | 98... 93
D | 2100D | NM101 | - | 98... 98
D | 2100E | NM101 | - | 98... 107
D | 2100F | NM101 | - | 98... 115
D | 2100G | NM101 | - | 98... 124
D | 2100H | NM101 | - | 98... 133
D | 2310 | NM101 | - | 98... 155
D | 2310 | PLA02 | - | 98... 164
D | 2330 | NM101 | - | 98... 171
D | 2750 | N101 | - | 98... 180

# Entity Relationship Code

Code describing the relationship of one identified person to another.

D | 2310 | NM110 | - | 706... 157

# Entity Type Qualifier

Code qualifying the type of entity.

D | 2100A | NM102 | - | 1065... 63
D | 2100B | NM102 | - | 1065... 87
D | 2100C | NM102 | - | 1065... 93
D | 2100D | NM102 | - | 1065... 99
D | 2100E | NM102 | - | 1065... 107
D | 2100F | NM102 | - | 1065... 116
D | 2100G | NM102 | - | 1065... 125
D | 2100H | NM102 | - | 1065... 133
D | 2310 | NM102 | - | 1065... 156
D | 2330 | NM102 | - | 1065... 172

# Frequency Code

Code indicating frequency or type of payment.

D | 2100A | ICM01 | - | 594... 79

# Gender Code

A code indicating the gender of the patient or insured.

D | 2100A | DMG03 | - | 1068... 73

# Handicap Indicator

Code indicating if individual is handicapped or not.

D | 2000 | INS10 | - | 1073... 53

# Health Related Code

Code indicating a specific health situation.

D | 2100A | HLH01 | - | 1212... 82

# Identification Card Count

The number of cards being requested.

D | 2300 | IDC03 | - | 380... 153

# Identification Card Type Code

Code identifying the type of identification card

D | 2300 | IDC02 | - | 1215... 152

# Identification Code Qualifier

Code designating the system/method of code structure used for Identification Code (67).

H | 1000A | N103 | - | 66... 40
H | 1000B | N103 | - | 66... 42
H | 1000C | N103 | - | 66... 44
D | 2100A | NM108 | - | 66... 64
D | 2100A | LUI01 | - | 66... 84
D | 2100B | NM108 | - | 66... 87
D | 2100D | NM108 | - | 66... 100
D | 2100F | NM108 | - | 66... 116
D | 2100G | NM108 | - | 66... 126
D | 2310 | NM108 | - | 66... 157
D | 2330 | NM108 | - | 66... 172

# Implementation Convention Reference

Reference assigned to identify Implementation Convention.

H | ST03 | - | 1705... 31

# Individual Relationship Code

Code indicating the relationship between two individuals or entities.

D | 2000 | INS02 | - | 1069... 48

# Insurance Line Code

Code identifying a group of insurance products

D | 2300 | HD03 | - | 1205... 142

# Insurer Identification Code

Code identifying the insurer providing coverage.

H | 1000B | N104 | - | 67... 42

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLEMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

## Insurer Name
Name of the insurer providing coverage.
H | 1000B | N102 | - | 93 | 41

## Language Code
Code indicating the language spoken by an individual.
D | 2100A | LUI02 | - | 67 | 85

## Language Description
Narrative text indicating the language spoken by an individual.
D | 2100A | LUI03 | - | 352 | 85

## Language Use Indicator
Code indicating the way a language is used by an individual, such as speaking or reading.
D | 2100A | LUI04 | - | 1303 | 85

## Late Enrollment Indicator
Code identifying if the insured is a late enrollee.
D | 2300 | HD09 | - | 1073 | 143

## Location Identification Code
Code which identifies a specific location.
D | 2100A | ICM04 | - | 310 | 80

## Location Identifier
Code which identifies a specific location.
D | 2100A | N406 | - | 310 | 70

## Location Qualifier
Code identifying type of location.
D | 2100A | N405 | - | 309 | 70

## Loop Identifier Code
The loop ID number given on the transaction set diagram is the value for this data element in segments LS and LE.
D | 2000 | LS01 | - | 447 | 178
D | 2000 | LE01 | - | 447 | 185

## Maintenance Reason Code
Code identifying reason for the maintenance change
D | 2000 | INS04 | - | 1203 | 49
D | 2310 | PLA05 | - | 1203 | 165

## Maintenance Type Code
Code identifying a specific type of item maintenance
D | 2000 | INS03 | - | 875 | 49
D | 2300 | HD01 | - | 875 | 141

## Marital Status Code
Code defining the marital status of a person.
D | 2100A | DMG04 | - | 1067 | 73
D | 2100B | DMG04 | - | 1067 | 90

## Master Policy Number
The identification of the master policy providing coverage for the entities identified in the transaction.
H | REF02 | - | 127 | 36

## Medicare Eligibility Reason Code
Code specifying reason for Medicare eligibility.
D | 2000 | INS06 | C052-2 | 1701 | 52

## Medicare Plan Code
Code identifying the Medicare Plan.
D | 2000 | INS06 | C052-1 | 1218 | 51

## Member Address Line
Address line of the current mailing address of the insured member.
D | 2100A | N301 | - | 166 | 68
D | 2100A | N302 | - | 166 | 68
D | 2100C | N301 | - | 166 | 95
D | 2100C | N302 | - | 166 | 95

## Member Birth Date
The date of birth of the member to the indicated coverage or policy.
D | 2100A | DMG02 | - | 1251 | 72

## Member City Name
City name of the member's mailing address.
D | 2100A | N401 | - | 19 | 69

## Member Employer Address Line
First line of the current mailing address of the member's employer.
D | 2100D | N301 | - | 166 | 104
D | 2100D | N302 | - | 166 | 104

## Member Employer City Name
The city name of the member's employer.
D | 2100D | N401 | - | 19 | 105

## Member Employer Communications Contact Name
The name of the member's employer.
D | 2100D | PER02 | - | 93 | 102

## Member Employer First Name
First name of the member's employer.
D | 2100D | NM104 | - | 1036 | 99

FEBRUARY 2011
E.5

BENEFIT ENROLLEMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

| Member Employer Identifier
Identification number or reference for the member's employer.
D | 2100D | NM109 | - | 67 | 100 | Member Identifier
Member's unique identification number assigned by a payer.
D | 2100A | NM109 | - | 67 | 64 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Member Employer Middle Name
Middle name of the member's employer.
D | 2100D | NM105 | - | 1037 | 99 | Member Indicator
Indicates whether the member is the subscriber or a dependent.
D | 2000 | INS01 | - | 1073 | 48 |
| Member Employer Name
The name of the member's individual's employer.
D | 2100D | NM103 | - | 1035 | 99 | Member Individual Death Date
Date of death for subscriber or dependent.
D | 2000 | INS12 | - | 1251 | 54 |
| Member Employer Name Prefix
Prefix to the name of the member's employer.
D | 2100D | NM106 | - | 1038 | 99 | Member Last Name
The last name of the insured individual to the coverage.
D | 2100A | NM103 | - | 1035 | 63 |
| Member Employer Name Suffix
Name suffix, including generation, of the member's employer.
D | 2100D | NM107 | - | 1039 | 99 | Member Mail City Name
Name of the city of the members mailing address.
D | 2100C | N401 | - | 19 | 96 |
| Member Employer Postal Zone or ZIP Code
The zip code of the member's employer.
D | 2100D | N403 | - | 116 | 106 | Member Mail Postal Zone or ZIP Code
Zip code of the members mailing address.
D | 2100C | N403 | - | 116 | 97 |
| Member Employer State Code
The state postal code of the member's employer.
D | 2100D | N402 | - | 156 | 106 | Member Mail State Code
State of the members mailing address.
D | 2100C | N402 | - | 156 | 96 |
| Member First Name
The first name of the insured individual to the coverage.
D | 2100A | NM104 | - | 1036 | 63 | Member Middle Name
The middle name of the insured individual to the coverage.
D | 2100A | NM105 | - | 1037 | 63 |
| Member Group or Policy Number
The identification number, control number, or code assigned by the carrier or administrator to identify the group under which the individual is covered.
D | 2000 | REF02 | - | 127 | 56
D | 2300 | REF02 | - | 127 | 149
D | 2320 | COB02 | - | 127 | 166
D | 2320 | REF02 | - | 127 | 169 | Member Name Prefix
The name prefix of the insured individual to the coverage.
D | 2100A | NM106 | - | 1038 | 63 |
| Member Height
Height of member.
D | 2100A | HLH02 | - | 65 | 82 | Member Name Suffix
The name suffix of the insured individual to the coverage.
D | 2100A | NM107 | - | 1039 | 63 |
|  | Member Postal Zone or Zip Code
The postal zip code of the member's mailing address.
D | 2100A | N403 | - | 116 | 70 |

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLEMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

| **Member Reporting Category Effective Date(s)**
The date the reporting category is effective or terminated.
D | 2750 | DTP03 | - | 1251 ... 184 | **Name Last or Organization Name**
Individual last name or organization name.
D | 2100H | NM103 | - | 1035 ... 134 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Member Reporting Category Name**
The name of the reporting category.
D | 2750 | N102 | - | 93 ... 180 | **Name Middle**
Individual middle name or initial.
D | 2100H | NM105 | - | 1037 ... 134 |
| **Member Reporting Category Reference ID**
Identifier associated with the reporting category.
D | 2750 | REF02 | - | 127 ... 182 | **Name Prefix**
The prefix to an individual's name.
D | 2100H | NM106 | - | 1038 ... 134 |
| **Member School City Name**
Name of the city of the members school address.
D | 2100E | N401 | - | 19 ... 113 | **Name Suffix**
This suffix to an individual's name.
D | 2100H | NM107 | - | 1039 ... 134 |
| **Member School Communications Contact Name**
Name of school attended by referenced member.
D | 2100E | PER02 | - | 93 ... 110 | **Original Transaction Set Reference Number**
Number that identified the original transaction set.
H | | BGN06 | - | 127 ... 35 |
| **Member School Postal Zone or ZIP Code**
Zip code of the members school address.
D | 2100E | N403 | - | 116 ... 114 | **Payer Responsibility Sequence Number Code**
Code identifying the insurance carrier's level of responsibility for a payment of a claim
D | 2320 | COB01 | - | 1138 ... 166 |
| **Member School State Code**
State of the members school address.
D | 2100E | N402 | - | 156 ... 114 | **Plan Coverage Description**
A description or number that identifies the plan or coverage
D | 2300 | HD04 | - | 1204 ... 142
D | 2300 | IDC01 | - | 1204 ... 152 |
| **Member State Code**
Member State Code.
D | 2100A | N402 | - | 156 ... 70 | **Plan Sponsor Name**
The name of the entity providing coverage to the subscriber.
H | 1000A | N102 | - | 93 ... 39 |
| **Member Supplemental Identifier**
Identifies another or additional distinguishing code number associated with the member.
D | 2000 | REF02 | - | 127 ... 58 | **Prior Coverage Month Count**
Number of months of prior health insurance coverage.
D | 2300 | REF02 | - | 127 ... 150 |
| **Member Weight**
Weight of member.
D | 2100A | HLH03 | - | 81 ... 83 | **Prior Incorrect Insured Birth Date**
The birth date previously reported or used for an individual when corrected data is reported.
D | 2100B | DMG02 | - | 1251 ... 90 |
| **Name First**
Individual first name.
D | 2100H | NM104 | - | 1036 ... 134 |  |

FEBRUARY 2011
E.7

BENEFIT ENROLLEMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

## Prior Incorrect Insured Gender Code

The gender previously reported or used for an individual when corrected data is reported.

D | 2100B | DMG03 | - | 1068 ... 90

## Prior Incorrect Insured Identifier

The identification number previously reported or used for an individual when a corrected name is reported.

D | 2100B | NM109 | - | 67 ... 88

## Prior Incorrect Member First Name

The first name previously reported or used for an individual when a corrected name is reported.

D | 2100B | NM104 | - | 1036 ... 87

## Prior Incorrect Member Last Name

The last name previously reported or used for an individual when a corrected name is reported.

D | 2100B | NM103 | - | 1035 ... 87

## Prior Incorrect Member Middle Name

The middle name previously reported or used for an individual when a corrected name is reported.

D | 2100B | NM105 | - | 1037 ... 87

## Prior Incorrect Member Name Prefix

The prefix to the name previously reported or used for an individual when a corrected name is reported.

D | 2100B | NM106 | - | 1038 ... 87

## Prior Incorrect Member Name Suffix

The suffix to the name previously reported or used for an individual when a corrected name is reported.

D | 2100B | NM107 | - | 1039 ... 87

## Product or Service ID Qualifier

Code identifying the type/source of the descriptive number used in Product/Service ID (234).

D | 2200 | DSB07 | - | 235 ... 139

## Provider Address Line

The street address of the provider.

D | 2310 | N301 | - | 166 ... 158

D | 2310 | N302 | - | 166 ... 158

## Provider City Name

The city name of the provider.

D | 2310 | N401 | - | 119 ... 159

## Provider Effective Date

The date the change of the primary care provider is effective.

D | 2310 | PLA03 | - | 373 ... 164

## Provider First Name

The first name of the provider of care submitting a transaction or related to the information provided in or request by the transaction.

D | 2310 | NM104 | - | 1036 ... 156

## Provider Identifier

Number assigned by the payer, regulatory authority, or other authorized body or agency to identify the provider.

D | 2310 | NM109 | - | 67 ... 157

## Provider Last or Organization Name

The last name of the provider of care or name of the provider organization submitting a transaction or related to the information provided in or request by the transaction.

D | 2310 | NM103 | - | 1035 ... 156

## Provider Middle Name

The middle name of the provider of care submitting a transaction or related to the information provided in or request by the transaction.

D | 2310 | NM105 | - | 1037 ... 156

## Provider Name Prefix

The name prefix of the provider of care submitting a transaction or related to the information provided in or request by the transaction.

D | 2310 | NM106 | - | 1038 ... 156

## Provider Name Suffix

The name suffix of the provider of care submitting a transaction or related to the information provided in or request by the transaction.

D | 2310 | NM107 | - | 1039 ... 157

## Provider Postal Zone or ZIP Code

The zip code of the provider.

D | 2310 | N403 | - | 116 ... 160

FEBRUARY 2011

CONSOLIDATED • 834
BENEFIT ENROLLMENT AND MAINTENANCE
005010X220 &amp; 005010X220A1

# Provider State Code
The State Postal Code of the provider
D | 2310 | N402 | - | 156 | 160

# Quantity Qualifier
Code specifying the type of quantity.
H | | QTY01 | - | 673 | 38

# Race or Ethnicity Code
Code indicating the racial or ethnic background of a person.
D | 2100A | DMG05 | C056-1 | 1109 | 74
D | 2100A | DMG05 | C056-3 | 1271 | 74
D | 2100B | DMG05 | C056-1 | 1109 | 91
D | 2100B | DMG05 | C056-3 | 1271 | 91

# Race or Ethnicity Collection Code
Code identifying how the Race or Ethnicity information was collected.
D | 2100A | DMG11 | - | 1271 | 75
D | 2100B | DMG11 | - | 1271 | 92

# Record Totals
Total number of records in this transaction.
H | | QTY02 | - | 380 | 38

# Reference Identification Qualifier
Code qualifying the reference identification.
H | | | REF01 | - | 128 | 36
D | 2000 | REF01 | - | 128 | 55
D | 2000 | REF01 | - | 128 | 56
D | 2000 | REF01 | - | 128 | 57
D | 2300 | REF01 | - | 128 | 148
D | 2300 | REF01 | - | 128 | 150
D | 2320 | REF01 | - | 128 | 168
D | 2750 | REF01 | - | 128 | 181

# Responsible Party Address Line
Address line of the person or entity responsible for payment of balance of bill after applicable processing by other parties, insurers, or organizations.
D | 2100G | N301 | - | 166 | 130
D | 2100G | N302 | - | 166 | 130

# Responsible Party First Name
First name of the person or entity responsible for payment of balance of bill after applicable processing by other parties, insurers, or organizations.
D | 2100G | NM104 | - | 1036 | 125

# Responsible Party Identifier
The identification number of the individual responsible for payment of balance of bill after applicable processing by other parties, insurers, or organizations.
D | 2100G | NM109 | - | 67 | 126

# Responsible Party Last or Organization Name
Last name or organization name of the person or entity responsible for payment of balance of bill after applicable processing by other parties, insurers, or organizations.
D | 2100G | NM103 | - | 1035 | 125

# Responsible Party Middle Name
Middle name of the person or entity responsible for payment of balance of bill after applicable processing by other parties, insurers, or organizations.
D | 2100G | NM105 | - | 1037 | 125

# Responsible Party Name Prefix
The prefix to the name of the individual responsible for payment of balance of bill after applicable processing by other parties, insurers, or organizations.
D | 2100G | NM106 | - | 1038 | 125

# Responsible Party Suffix Name
Suffix for name of the person or entity responsible for payment of balance of bill after applicable processing by other parties, insurers, or organizations.
D | 2100G | NM107 | - | 1039 | 126

# Responsible Person City Name
Name of the city of the Responsible Person.
D | 2100G | N401 | - | 19 | 131

# Responsible Person Postal Zone or ZIP Code
Zip code of the Responsible Person.
D | 2100G | N403 | - | 116 | 132

# Responsible Person State Code
State of the Responsible Person.
D | 2100G | N402 | - | 156 | 132

# Salary Grade Code
A code that identifies the salary or wage level of an employee.
D | 2100A | ICM05 | - | 1214 | 80

FEBRUARY 2011
E.9

BENEFIT ENROLLEMENT AND MAINTENANCE 005010X220 &amp; 005010X220A1

CONSOLIDATED • 834

# School Address Line

Address line of address for school of referenced individual

D | 2100E | N301 | - | 166 ... 112
D | 2100E | N302 | - | 166 ... 112

# School Name

Name of school attended by referenced person.

D | 2100E | NM103 | - | 1035 ... 108

# Service Type Code

Code identifying the classification of service.

D | 2320 | COB04 | - | 1365 ... 167

# Sponsor Identifier

Identification of the party paying for the coverage.

H | 1000A | N104 | - | 67 ... 40

# Status Information Effective Date

The date that the status information provided is effective.

D | 2000 | DTP03 | - | 1251 ... 61

# Student Status Code

Code indicating the student status of the patient if 19 years of age or older, not handicapped and not the insured

D | 2000 | INS09 | - | 1220 ... 53

# Subscriber Identifier

Insured's or subscriber's unique identification number assigned by a payer.

D | 2000 | REF02 | - | 127 ... 55

# TPA or Broker Account Number

Account number assigned to the Third Party Administrator or broker

H | 1100C | ACT01 | - | 508 ... 45
H | 1100C | ACT06 | - | 508 ... 46

# TPA or Broker Identification Code

Code identifying the Third Party Administrator or broker

H | 1000C | N104 | - | 67 ... 44

# TPA or Broker Name

Name of the Third Party Administrator or Broker.

H | 1000C | N102 | - | 93 ... 43

# Time Zone Code

Code identifying the time zone used in specifying a time.

H | | BGN05 | - | 623 ... 33

# Transaction Segment Count

A tally of all segments between the ST and the SE segments including the ST and SE segments.

D | | SE01 | - | 96 ... 186

# Transaction Set Control Number

The unique identification number within a transaction set.

H | | ST02 | - | 329 ... 31
D | | SE02 | - | 329 ... 186

# Transaction Set Creation Date

Identifies the date the submitter created the transaction.

H | | BGN03 | - | 373 ... 33

# Transaction Set Creation Time

Time file is created for transmission.

H | | BGN04 | - | 337 ... 33

# Transaction Set Identifier Code

Code uniquely identifying a Transaction Set.

H | | ST01 | - | 143 ... 31

# Transaction Set Purpose Code

Code identifying purpose of transaction set.

H | | BGN01 | - | 353 ... 32

# Transaction Set Reference Number

Number uniquely identifying a transaction set.

H | | BGN02 | - | 127 ... 33

# Wage Amount

Amount of wages or income for the specified period.

D | 2100A | ICM02 | - | 782 ... 80

# Work Hours Count

Number of hours of employment for a specified period.

D | 2100A | ICM03 | - | 380 ... 80

FEBRUARY 2011