---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Financial
purpose:
  - Function Relationships
use-case:
  - Calculating Depreciation
  - Valuing Investments
  - Estimating Loan Payments
related:
  - AMORDEGRC
  - AMORLINC
  - AVERAGE
  - COUPDAYS
  - COUPDAYSNC
  - COUPNUM
  - CUMIPMT
  - DISC
  - DOLLARDE
  - DOLLARFR
  - EFFECT
  - EUROCONVERT
  - FV
  - FVSCHEDULE
  - IF
  - IFERROR
  - IPMT
  - IRR
  - MDURATION
  - MIRR
  - NOMINAL
  - NPER
  - NPV
  - ODDLYIELD
  - PMT
  - PPMT
  - PRICE
  - PRICEMAT
  - PV
  - RATE
  - RECEIVED
  - SLN
  - SUM
  - SYD
  - TBILLPRICE
  - TBILLYIELD
  - VDB
  - XNPV
  - YIELD
  - YIELDMAT
level: 3
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - depreciation
  - financial
  - investments
---

# Financial Functions Relationship Diagram

This diagram shows the relationships between functions in the Financial category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Financial fill:#54A0FF,stroke:#333,stroke-width:2px,color:#000
    EUROCONVERT["EUROCONVERT<br/>Converts euro currencies (Add-in and Automation category)"]
    TBILLYIELD["TBILLYIELD<br/>Returns the yield of a Treasury bill"]
    COUPNUM["COUPNUM<br/>Returns the number of coupons between settlement and maturity"]
    CUMIPMT["CUMIPMT<br/>Returns cumulative interest paid between two periods"]
    PRICEMAT["PRICEMAT<br/>Returns the price per $100 face value at maturity"]
    MIRR["MIRR<br/>Returns the modified internal rate of return"]
    DOLLARFR["DOLLARFR<br/>Converts a decimal dollar price to a fractional price"]
    PV["PV<br/>Returns the present value of an investment"]
    FV["FV<br/>Returns the future value of an investment"]
    PPMT["PPMT<br/>Returns the principal payment for an investment in a period"]
    MDURATION["MDURATION<br/>Returns the modified Macaulay duration of a security"]
    DISC["DISC<br/>Returns the discount rate for a security"]
    SYD["SYD<br/>Returns sum-of-years digits depreciation for a period"]
    IPMT["IPMT<br/>Returns the interest payment for an investment in a period"]
    COUPDAYS["COUPDAYS<br/>Returns days in the coupon period that contains settlement"]
    TBILLPRICE["TBILLPRICE<br/>Returns the price per $100 face value of a Treasury bill"]
    COUPDAYSNC["COUPDAYSNC<br/>Returns days from settlement to the next coupon date"]
    NPV["NPV<br/>Returns the net present value of periodic cash flows"]
    FVSCHEDULE["FVSCHEDULE<br/>Returns future value after a series of interest rates"]
    EFFECT["EFFECT<br/>Returns the effective annual interest rate"]
    PMT["PMT<br/>Returns the periodic payment for a loan or annuity"]
    NPER["NPER<br/>Returns the number of periods for an investment or loan"]
    AMORDEGRC["AMORDEGRC<br/>Returns depreciation per period using a depreciation coefficient"]
    AMORLINC["AMORLINC<br/>Returns depreciation for each accounting period"]
    NOMINAL["NOMINAL<br/>Returns the annual nominal interest rate"]
    PRICE["PRICE<br/>Returns the price per $100 face value of a periodic security"]
    YIELDMAT["YIELDMAT<br/>Returns the annual yield of a security paid at maturity"]
    IRR["IRR<br/>Returns the internal rate of return for periodic cash flows"]
    SLN["SLN<br/>Returns straight-line depreciation of an asset for one period"]
    DOLLARDE["DOLLARDE<br/>Converts a fractional dollar price to a decimal price"]
    YIELD["YIELD<br/>Returns the yield of a security that pays periodic interest"]
    VDB["VDB<br/>Returns depreciation for a specified or partial period"]
    ODDLYIELD["ODDLYIELD<br/>Returns the yield of a security with an odd last period"]
    RECEIVED["RECEIVED<br/>Returns the amount received at maturity for a security"]
    XNPV["XNPV<br/>Returns the net present value for irregular cash flows"]
    ODDLPRICE["ODDLPRICE<br/>Returns the price per $100 face value with an odd last period"]
    CUMPRINC["CUMPRINC<br/>Returns cumulative principal paid between two periods"]
    COUPNCD["COUPNCD<br/>Returns the next coupon date after settlement"]
    DB["DB<br/>Returns depreciation for a period using fixed-declining balance"]
    TBILLEQ["TBILLEQ<br/>Returns the bond-equivalent yield for a Treasury bill"]
    ODDFYIELD["ODDFYIELD<br/>Returns the yield of a security with an odd first period"]
    YIELDDISC["YIELDDISC<br/>Returns the annual yield of a discounted security"]
    ISPMT["ISPMT<br/>Returns interest paid during a specific period of a loan"]
    PRICEDISC["PRICEDISC<br/>Returns the price per $100 face value of a discounted security"]
    COUPPCD["COUPPCD<br/>Returns the previous coupon date before settlement"]
    INTRATE["INTRATE<br/>Returns the interest rate for a fully invested security"]
    ACCRINT["ACCRINT<br/>Returns accrued interest for a security with periodic interest"]
    ACCRINTM["ACCRINTM<br/>Returns accrued interest for a security paid at maturity"]
    DDB["DDB<br/>Returns depreciation using the double-declining balance method"]
    COUPDAYBS["COUPDAYBS<br/>Returns days from the coupon period start to settlement"]
    RATE["RATE<br/>Returns the interest rate per period of an annuity"]
    DURATION["DURATION<br/>Returns the annual duration of a security with periodic interest"]
    ODDFPRICE["ODDFPRICE<br/>Returns the price per $100 face value with an odd first period"]
    XIRR["XIRR<br/>Returns the internal rate of return for irregular cash flows"]
    PDURATION["PDURATION<br/>Returns the periods needed for an investment to reach a value"]
    RRI["RRI<br/>Returns an equivalent interest rate for investment growth"]
    IF["IF<br/>External Function"]
    EUROCONVERT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    EUROCONVERT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    EUROCONVERT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    EUROCONVERT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    EUROCONVERT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TBILLYIELD --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TBILLYIELD --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TBILLYIELD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    TBILLYIELD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    TBILLYIELD -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUPNUM --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUPNUM --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COUPNUM --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    COUPNUM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    COUPNUM -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUMIPMT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUMIPMT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUMIPMT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUMIPMT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUMIPMT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PRICEMAT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PRICEMAT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    PRICEMAT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    PRICEMAT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    PRICEMAT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MIRR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MIRR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    MIRR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    MIRR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    MIRR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DOLLARFR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DOLLARFR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DOLLARFR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DOLLARFR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DOLLARFR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PV --> IF
    class IF external
    PV --> PMT
    PV --> RATE
    PV -.-> FV
    PV -.-> PMT
    IF["IF<br/>External Function"]
    FV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FV --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FV --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    FV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    FV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PPMT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PPMT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    PPMT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    PPMT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    PPMT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MDURATION --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MDURATION --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    MDURATION --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    MDURATION -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    MDURATION -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DISC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DISC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DISC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DISC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DISC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SYD --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SYD --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SYD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    SYD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    SYD -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IPMT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IPMT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IPMT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IPMT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IPMT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUPDAYS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUPDAYS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COUPDAYS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    COUPDAYS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    COUPDAYS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TBILLPRICE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TBILLPRICE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TBILLPRICE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    TBILLPRICE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    TBILLPRICE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUPDAYSNC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUPDAYSNC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COUPDAYSNC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    COUPDAYSNC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    COUPDAYSNC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    NPV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    NPV --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    NPV --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    NPV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    NPV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FVSCHEDULE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FVSCHEDULE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FVSCHEDULE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    FVSCHEDULE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    FVSCHEDULE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    EFFECT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    EFFECT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    EFFECT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    EFFECT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    EFFECT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PMT --> IF
    class IF external
    PMT --> PV
    PMT --> RATE
    PMT -.-> PV
    PMT -.-> FV
    IF["IF<br/>External Function"]
    NPER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    NPER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    NPER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    NPER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    NPER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    AMORDEGRC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    AMORDEGRC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    AMORDEGRC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    AMORDEGRC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    AMORDEGRC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    AMORLINC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    AMORLINC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    AMORLINC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    AMORLINC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    AMORLINC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    NOMINAL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    NOMINAL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    NOMINAL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    NOMINAL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    NOMINAL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PRICE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PRICE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    PRICE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    PRICE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    PRICE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    YIELDMAT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    YIELDMAT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    YIELDMAT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    YIELDMAT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    YIELDMAT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IRR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IRR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IRR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IRR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IRR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SLN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SLN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SLN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    SLN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    SLN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DOLLARDE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DOLLARDE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DOLLARDE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DOLLARDE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DOLLARDE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    YIELD --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    YIELD --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    YIELD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    YIELD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    YIELD -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    VDB --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VDB --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    VDB --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    VDB -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    VDB -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ODDLYIELD --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ODDLYIELD --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ODDLYIELD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ODDLYIELD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ODDLYIELD -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RECEIVED --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    RECEIVED --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    RECEIVED --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    RECEIVED -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    RECEIVED -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    XNPV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    XNPV --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    XNPV --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    XNPV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    XNPV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ODDLPRICE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ODDLPRICE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ODDLPRICE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ODDLPRICE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ODDLPRICE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUMPRINC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUMPRINC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUMPRINC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUMPRINC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUMPRINC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUPNCD --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUPNCD --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COUPNCD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    COUPNCD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    COUPNCD -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DB --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DB --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DB --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DB -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DB -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TBILLEQ --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TBILLEQ --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TBILLEQ --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    TBILLEQ -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    TBILLEQ -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ODDFYIELD --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ODDFYIELD --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ODDFYIELD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ODDFYIELD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ODDFYIELD -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    YIELDDISC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    YIELDDISC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    YIELDDISC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    YIELDDISC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    YIELDDISC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISPMT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISPMT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISPMT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ISPMT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ISPMT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PRICEDISC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PRICEDISC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    PRICEDISC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    PRICEDISC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    PRICEDISC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUPPCD --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUPPCD --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COUPPCD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    COUPPCD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    COUPPCD -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    INTRATE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    INTRATE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    INTRATE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    INTRATE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    INTRATE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ACCRINT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ACCRINT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ACCRINT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ACCRINT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ACCRINT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ACCRINTM --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ACCRINTM --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ACCRINTM --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ACCRINTM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ACCRINTM -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DDB --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DDB --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DDB --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DDB -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DDB -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUPDAYBS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUPDAYBS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COUPDAYBS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    COUPDAYBS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    COUPDAYBS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RATE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    RATE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    RATE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    RATE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    RATE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DURATION --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DURATION --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DURATION --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DURATION -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DURATION -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ODDFPRICE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ODDFPRICE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ODDFPRICE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ODDFPRICE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ODDFPRICE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    XIRR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    XIRR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    XIRR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    XIRR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    XIRR -.-> IFERROR
    class IFERROR external
    class EUROCONVERT external
    IF["IF<br/>External Function"]
    PDURATION --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PDURATION --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    PDURATION --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    PDURATION -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    PDURATION -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RRI --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    RRI --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    RRI --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    RRI -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    RRI -.-> IFERROR
    class IFERROR external
    class TBILLYIELD Financial
    class COUPNUM Financial
    class CUMIPMT Financial
    class PRICEMAT Financial
    class MIRR Financial
    class DOLLARFR Financial
    class PV Financial
    class FV Financial
    class PPMT Financial
    class MDURATION Financial
    class DISC Financial
    class SYD Financial
    class IPMT Financial
    class COUPDAYS Financial
    class TBILLPRICE Financial
    class COUPDAYSNC Financial
    class NPV Financial
    class FVSCHEDULE Financial
    class EFFECT Financial
    class PMT Financial
    class NPER Financial
    class AMORDEGRC Financial
    class AMORLINC Financial
    class NOMINAL Financial
    class PRICE Financial
    class YIELDMAT Financial
    class IRR Financial
    class SLN Financial
    class DOLLARDE Financial
    class YIELD Financial
    class VDB Financial
    class ODDLYIELD Financial
    class RECEIVED Financial
    class XNPV Financial
    class ODDLPRICE Financial
    class CUMPRINC Financial
    class COUPNCD Financial
    class DB Financial
    class TBILLEQ Financial
    class ODDFYIELD Financial
    class YIELDDISC Financial
    class ISPMT Financial
    class PRICEDISC Financial
    class COUPPCD Financial
    class INTRATE Financial
    class ACCRINT Financial
    class ACCRINTM Financial
    class DDB Financial
    class COUPDAYBS Financial
    class RATE Financial
    class DURATION Financial
    class ODDFPRICE Financial
    class XIRR Financial
    class PDURATION Financial
    class RRI Financial
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```

## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (`-.->`)**: "Similar functions" relationships
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in This Category: 55
