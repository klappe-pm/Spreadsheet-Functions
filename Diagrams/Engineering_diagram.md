# Engineering Functions Relationship Diagram

This diagram shows the relationships between functions in the Engineering category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Engineering fill:#FF9F43,stroke:#333,stroke-width:2px,color:#000
    DEC2BIN["DEC2BIN<br/>DEC2BIN performs specialized calculations for analytical app..."]
    IMLOG10["IMLOG10<br/>IMLOG10 performs specialized calculations for analytical app..."]
    BIN2DEC["BIN2DEC<br/>BIN2DEC performs specialized calculations for analytical app..."]
    OCT2DEC["OCT2DEC<br/>OCT2DEC performs specialized calculations for analytical app..."]
    BESSELK["BESSELK<br/>BESSELK performs specialized calculations for analytical app..."]
    BITOR["BITOR<br/>BITOR performs specialized calculations for analytical appli..."]
    BITAND["BITAND<br/>BITAND performs specialized calculations for analytical appl..."]
    IMCOS["IMCOS<br/>IMCOS performs specialized calculations for analytical appli..."]
    IMCONJUGATE["IMCONJUGATE<br/>IMCONJUGATE performs specialized calculations for analytical..."]
    IMTAN["IMTAN<br/>IMTAN performs specialized calculations for analytical appli..."]
    DELTA["DELTA<br/>DELTA performs specialized calculations for analytical appli..."]
    OCT2BIN["OCT2BIN<br/>OCT2BIN performs specialized calculations for analytical app..."]
    BESSELJ["BESSELJ<br/>BESSELJ performs specialized calculations for analytical app..."]
    DEC2OCT["DEC2OCT<br/>DEC2OCT performs specialized calculations for analytical app..."]
    BITLSHIFT["BITLSHIFT<br/>BITLSHIFT performs specialized calculations for analytical a..."]
    IMABS["IMABS<br/>IMABS performs specialized calculations for analytical appli..."]
    IMAGINARY["IMAGINARY<br/>IMAGINARY performs specialized calculations for analytical a..."]
    BIN2OCT["BIN2OCT<br/>BIN2OCT performs specialized calculations for analytical app..."]
    COMPLEX["COMPLEX<br/>COMPLEX performs specialized calculations for analytical app..."]
    BITXOR["BITXOR<br/>BITXOR performs specialized calculations for analytical appl..."]
    BESSELY["BESSELY<br/>BESSELY performs specialized calculations for analytical app..."]
    IMCSC["IMCSC<br/>IMCSC performs specialized calculations for analytical appli..."]
    BITRSHIFT["BITRSHIFT<br/>BITRSHIFT performs specialized calculations for analytical a..."]
    IMPOWER["IMPOWER<br/>IMPOWER performs specialized calculations for analytical app..."]
    IMLN["IMLN<br/>IMLN performs specialized calculations for analytical applic..."]
    IMLOG2["IMLOG2<br/>IMLOG2 performs specialized calculations for analytical appl..."]
    IMCOSH["IMCOSH<br/>IMCOSH performs specialized calculations for analytical appl..."]
    IMDIV["IMDIV<br/>IMDIV performs specialized calculations for analytical appli..."]
    IMSINH["IMSINH<br/>IMSINH performs specialized calculations for analytical appl..."]
    IMSUM["IMSUM<br/>IMSUM performs specialized calculations for analytical appli..."]
    ERFC_PRECISE["ERFC.PRECISE<br/>ERFC.PRECISE performs specialized calculations for analytica..."]
    IMSECH["IMSECH<br/>IMSECH performs specialized calculations for analytical appl..."]
    IMARGUMENT["IMARGUMENT<br/>IMARGUMENT performs specialized calculations for analytical ..."]
    ERF_PRECISE["ERF.PRECISE<br/>ERF.PRECISE performs specialized calculations for analytical..."]
    IMSQRT["IMSQRT<br/>IMSQRT performs specialized calculations for analytical appl..."]
    IMEXP["IMEXP<br/>IMEXP performs specialized calculations for analytical appli..."]
    ERFC["ERFC<br/>ERFC performs specialized calculations for analytical applic..."]
    IMSIN["IMSIN<br/>IMSIN performs specialized calculations for analytical appli..."]
    ERF["ERF<br/>ERF performs specialized calculations for analytical applica..."]
    BESSELI["BESSELI<br/>BESSELI performs specialized calculations for analytical app..."]
    HEX2DEC["HEX2DEC<br/>HEX2DEC performs specialized calculations for analytical app..."]
    IMREAL["IMREAL<br/>IMREAL performs specialized calculations for analytical appl..."]
    GESTEP["GESTEP<br/>GESTEP performs specialized calculations for analytical appl..."]
    HEX2BIN["HEX2BIN<br/>HEX2BIN performs specialized calculations for analytical app..."]
    IMCSCH["IMCSCH<br/>IMCSCH performs specialized calculations for analytical appl..."]
    IMSUB["IMSUB<br/>IMSUB performs specialized calculations for analytical appli..."]
    DEC2HEX["DEC2HEX<br/>DEC2HEX performs specialized calculations for analytical app..."]
    IMCOT["IMCOT<br/>IMCOT performs specialized calculations for analytical appli..."]
    IMPRODUCT["IMPRODUCT<br/>IMPRODUCT performs specialized calculations for analytical a..."]
    OCT2HEX["OCT2HEX<br/>OCT2HEX performs specialized calculations for analytical app..."]
    HEX2OCT["HEX2OCT<br/>HEX2OCT performs specialized calculations for analytical app..."]
    BIN2HEX["BIN2HEX<br/>BIN2HEX performs specialized calculations for analytical app..."]
    IMSEC["IMSEC<br/>IMSEC performs specialized calculations for analytical appli..."]
    CONVERT["CONVERT<br/>CONVERT performs specialized calculations for analytical app..."]
    IF["IF<br/>External Function"]
    DEC2BIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DEC2BIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DEC2BIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DEC2BIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DEC2BIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMLOG10 --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMLOG10 --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMLOG10 --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMLOG10 -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMLOG10 -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BIN2DEC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BIN2DEC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BIN2DEC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BIN2DEC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BIN2DEC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    OCT2DEC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    OCT2DEC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    OCT2DEC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    OCT2DEC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    OCT2DEC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BESSELK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BESSELK --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BESSELK --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BESSELK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BESSELK -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BITOR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BITOR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BITOR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BITOR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BITOR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BITAND --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BITAND --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BITAND --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BITAND -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BITAND -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCOS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCOS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCOS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMCOS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMCOS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCONJUGATE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCONJUGATE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCONJUGATE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMCONJUGATE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMCONJUGATE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMTAN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMTAN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMTAN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMTAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMTAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DELTA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DELTA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DELTA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DELTA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DELTA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    OCT2BIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    OCT2BIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    OCT2BIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    OCT2BIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    OCT2BIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BESSELJ --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BESSELJ --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BESSELJ --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BESSELJ -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BESSELJ -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DEC2OCT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DEC2OCT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DEC2OCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DEC2OCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DEC2OCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BITLSHIFT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BITLSHIFT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BITLSHIFT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BITLSHIFT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BITLSHIFT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMABS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMABS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMABS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMABS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMABS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMAGINARY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMAGINARY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMAGINARY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMAGINARY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMAGINARY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BIN2OCT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BIN2OCT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BIN2OCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BIN2OCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BIN2OCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COMPLEX --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COMPLEX --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COMPLEX --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    COMPLEX -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COMPLEX -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BITXOR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BITXOR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BITXOR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BITXOR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BITXOR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BESSELY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BESSELY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BESSELY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BESSELY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BESSELY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCSC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCSC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCSC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMCSC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMCSC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BITRSHIFT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BITRSHIFT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BITRSHIFT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BITRSHIFT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BITRSHIFT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMPOWER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPOWER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPOWER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMPOWER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMPOWER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMLN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMLN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMLN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMLN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMLN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMLOG2 --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMLOG2 --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMLOG2 --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMLOG2 -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMLOG2 -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCOSH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCOSH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCOSH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMCOSH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMCOSH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMDIV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMDIV --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMDIV --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMDIV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMDIV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSINH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSINH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSINH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMSINH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMSINH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSUM --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSUM --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSUM --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMSUM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMSUM -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ERFC_PRECISE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ERFC_PRECISE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ERFC_PRECISE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ERFC_PRECISE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ERFC_PRECISE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSECH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSECH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSECH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMSECH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMSECH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMARGUMENT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMARGUMENT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMARGUMENT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMARGUMENT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMARGUMENT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ERF_PRECISE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ERF_PRECISE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ERF_PRECISE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ERF_PRECISE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ERF_PRECISE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSQRT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSQRT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSQRT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMSQRT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMSQRT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMEXP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMEXP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMEXP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMEXP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMEXP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ERFC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ERFC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ERFC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ERFC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ERFC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMSIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMSIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ERF --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ERF --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ERF --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ERF -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ERF -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BESSELI --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BESSELI --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BESSELI --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BESSELI -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BESSELI -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HEX2DEC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HEX2DEC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    HEX2DEC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    HEX2DEC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    HEX2DEC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMREAL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMREAL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMREAL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMREAL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMREAL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GESTEP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GESTEP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    GESTEP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    GESTEP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GESTEP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HEX2BIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HEX2BIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    HEX2BIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    HEX2BIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    HEX2BIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCSCH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCSCH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCSCH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMCSCH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMCSCH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSUB --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSUB --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSUB --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMSUB -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMSUB -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DEC2HEX --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DEC2HEX --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DEC2HEX --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DEC2HEX -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DEC2HEX -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCOT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCOT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCOT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMCOT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMCOT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMPRODUCT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPRODUCT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPRODUCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMPRODUCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMPRODUCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    OCT2HEX --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    OCT2HEX --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    OCT2HEX --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    OCT2HEX -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    OCT2HEX -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HEX2OCT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HEX2OCT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    HEX2OCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    HEX2OCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    HEX2OCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BIN2HEX --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BIN2HEX --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BIN2HEX --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BIN2HEX -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BIN2HEX -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSEC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSEC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSEC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMSEC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMSEC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CONVERT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CONVERT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CONVERT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CONVERT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CONVERT -.-> IFERROR
    class IFERROR external
    class DEC2BIN Engineering
    class IMLOG10 Engineering
    class BIN2DEC Engineering
    class OCT2DEC Engineering
    class BESSELK Engineering
    class BITOR Engineering
    class BITAND Engineering
    class IMCOS Engineering
    class IMCONJUGATE Engineering
    class IMTAN Engineering
    class DELTA Engineering
    class OCT2BIN Engineering
    class BESSELJ Engineering
    class DEC2OCT Engineering
    class BITLSHIFT Engineering
    class IMABS Engineering
    class IMAGINARY Engineering
    class BIN2OCT Engineering
    class COMPLEX Engineering
    class BITXOR Engineering
    class BESSELY Engineering
    class IMCSC Engineering
    class BITRSHIFT Engineering
    class IMPOWER Engineering
    class IMLN Engineering
    class IMLOG2 Engineering
    class IMCOSH Engineering
    class IMDIV Engineering
    class IMSINH Engineering
    class IMSUM Engineering
    class ERFC_PRECISE Engineering
    class IMSECH Engineering
    class IMARGUMENT Engineering
    class ERF_PRECISE Engineering
    class IMSQRT Engineering
    class IMEXP Engineering
    class ERFC Engineering
    class IMSIN Engineering
    class ERF Engineering
    class BESSELI Engineering
    class HEX2DEC Engineering
    class IMREAL Engineering
    class GESTEP Engineering
    class HEX2BIN Engineering
    class IMCSCH Engineering
    class IMSUB Engineering
    class DEC2HEX Engineering
    class IMCOT Engineering
    class IMPRODUCT Engineering
    class OCT2HEX Engineering
    class HEX2OCT Engineering
    class BIN2HEX Engineering
    class IMSEC Engineering
    class CONVERT Engineering
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 54
