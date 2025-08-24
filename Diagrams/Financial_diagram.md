# Financial Functions Relationship Diagram

This diagram shows the relationships between functions in the Financial category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Financial fill:#54A0FF,stroke:#333,stroke-width:2px,color:#000
    EUROCONVERT["EUROCONVERT<br/>EUROCONVERT calculates financial metrics including payments,..."]
    TBILLYIELD["TBILLYIELD<br/>TBILLYIELD calculates financial metrics including payments, ..."]
    COUPNUM["COUPNUM<br/>COUPNUM calculates financial metrics including payments, ret..."]
    CUMIPMT["CUMIPMT<br/>CUMIPMT calculates financial metrics including payments, ret..."]
    PRICEMAT["PRICEMAT<br/>PRICEMAT calculates financial metrics including payments, re..."]
    MIRR["MIRR<br/>MIRR calculates financial metrics including payments, return..."]
    DOLLARFR["DOLLARFR<br/>DOLLARFR calculates financial metrics including payments, re..."]
    PV["PV<br/>PV calculates the present value of an investment based on co..."]
    FV["FV<br/>FV calculates financial metrics including payments, returns,..."]
    PPMT["PPMT<br/>PPMT calculates financial metrics including payments, return..."]
    MDURATION["MDURATION<br/>MDURATION calculates financial metrics including payments, r..."]
    DISC["DISC<br/>DISC calculates financial metrics including payments, return..."]
    SYD["SYD<br/>SYD calculates financial metrics including payments, returns..."]
    IPMT["IPMT<br/>IPMT calculates financial metrics including payments, return..."]
    COUPDAYS["COUPDAYS<br/>COUPDAYS calculates financial metrics including payments, re..."]
    TBILLPRICE["TBILLPRICE<br/>TBILLPRICE calculates financial metrics including payments, ..."]
    COUPDAYSNC["COUPDAYSNC<br/>COUPDAYSNC calculates financial metrics including payments, ..."]
    NPV["NPV<br/>NPV calculates financial metrics including payments, returns..."]
    FVSCHEDULE["FVSCHEDULE<br/>FVSCHEDULE calculates financial metrics including payments, ..."]
    EFFECT["EFFECT<br/>EFFECT calculates financial metrics including payments, retu..."]
    PMT["PMT<br/>PMT calculates the payment for a loan based on constant paym..."]
    NPER["NPER<br/>NPER calculates financial metrics including payments, return..."]
    AMORDEGRC["AMORDEGRC<br/>AMORDEGRC calculates financial metrics including payments, r..."]
    AMORLINC["AMORLINC<br/>AMORLINC calculates financial metrics including payments, re..."]
    NOMINAL["NOMINAL<br/>NOMINAL calculates financial metrics including payments, ret..."]
    PRICE["PRICE<br/>PRICE calculates financial metrics including payments, retur..."]
    YIELDMAT["YIELDMAT<br/>YIELDMAT calculates financial metrics including payments, re..."]
    IRR["IRR<br/>IRR calculates financial metrics including payments, returns..."]
    SLN["SLN<br/>SLN calculates financial metrics including payments, returns..."]
    DOLLARDE["DOLLARDE<br/>DOLLARDE calculates financial metrics including payments, re..."]
    YIELD["YIELD<br/>YIELD calculates financial metrics including payments, retur..."]
    VDB["VDB<br/>VDB calculates financial metrics including payments, returns..."]
    ODDLYIELD["ODDLYIELD<br/>ODDLYIELD calculates financial metrics including payments, r..."]
    RECEIVED["RECEIVED<br/>RECEIVED calculates financial metrics including payments, re..."]
    XNPV["XNPV<br/>XNPV calculates financial metrics including payments, return..."]
    ODDLPRICE["ODDLPRICE<br/>ODDLPRICE calculates financial metrics including payments, r..."]
    CUMPRINC["CUMPRINC<br/>CUMPRINC calculates financial metrics including payments, re..."]
    COUPNCD["COUPNCD<br/>COUPNCD calculates financial metrics including payments, ret..."]
    DB["DB<br/>DB calculates financial metrics including payments, returns,..."]
    TBILLEQ["TBILLEQ<br/>TBILLEQ calculates financial metrics including payments, ret..."]
    ODDFYIELD["ODDFYIELD<br/>ODDFYIELD calculates financial metrics including payments, r..."]
    YIELDDISC["YIELDDISC<br/>YIELDDISC calculates financial metrics including payments, r..."]
    ISPMT["ISPMT<br/>ISPMT calculates financial metrics including payments, retur..."]
    PRICEDISC["PRICEDISC<br/>PRICEDISC calculates financial metrics including payments, r..."]
    COUPPCD["COUPPCD<br/>COUPPCD calculates financial metrics including payments, ret..."]
    INTRATE["INTRATE<br/>INTRATE calculates financial metrics including payments, ret..."]
    ACCRINT["ACCRINT<br/>ACCRINT calculates financial metrics including payments, ret..."]
    ACCRINTM["ACCRINTM<br/>ACCRINTM calculates financial metrics including payments, re..."]
    DDB["DDB<br/>DDB calculates financial metrics including payments, returns..."]
    COUPDAYBS["COUPDAYBS<br/>COUPDAYBS calculates financial metrics including payments, r..."]
    RATE["RATE<br/>RATE calculates financial metrics including payments, return..."]
    DURATION["DURATION<br/>DURATION calculates financial metrics including payments, re..."]
    ODDFPRICE["ODDFPRICE<br/>ODDFPRICE calculates financial metrics including payments, r..."]
    XIRR["XIRR<br/>XIRR calculates financial metrics including payments, return..."]
    IF["IF<br/>External Function"]
    EUROCONVERT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    EUROCONVERT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    EUROCONVERT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    EUROCONVERT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    TBILLYIELD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    COUPNUM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    CUMIPMT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    PRICEMAT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    MIRR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    DOLLARFR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    FV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    PPMT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    MDURATION -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    DISC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    SYD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    IPMT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    COUPDAYS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    TBILLPRICE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    COUPDAYSNC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    NPV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    FVSCHEDULE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    EFFECT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    NPER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    AMORDEGRC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    AMORLINC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    NOMINAL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    PRICE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    YIELDMAT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    IRR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    SLN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    DOLLARDE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    YIELD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    VDB -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    ODDLYIELD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    RECEIVED -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    XNPV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    ODDLPRICE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    CUMPRINC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    COUPNCD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    DB -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    TBILLEQ -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    ODDFYIELD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    YIELDDISC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    ISPMT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    PRICEDISC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    COUPPCD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    INTRATE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    ACCRINT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    ACCRINTM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    DDB -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    COUPDAYBS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    RATE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    DURATION -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    ODDFPRICE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
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
    IF["IF<br/>Related Function"]
    XIRR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    XIRR -.-> IFERROR
    class IFERROR external
    class EUROCONVERT Financial
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
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 54
