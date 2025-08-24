# Excel-specific Functions Relationship Diagram

This diagram shows the relationships between functions in the Excel-specific category and their connections to commonly used functions.

```mermaid
graph LR
    classDef Excel-specific fill:#6C5CE7,stroke:#333,stroke-width:2px,color:#000
    TOCOL["TOCOL<br/>TOCOL performs specialized calculations for analytical appli..."]
    CUMIPMT["CUMIPMT<br/>CUMIPMT performs specialized calculations for analytical app..."]
    FILTERXML["FILTERXML<br/>FILTERXML performs specialized calculations for analytical a..."]
    SCAN["SCAN<br/>SCAN performs specialized calculations for analytical applic..."]
    TEXTAFTER["TEXTAFTER<br/>TEXTAFTER performs specialized calculations for analytical a..."]
    MAP["MAP<br/>MAP performs specialized calculations for analytical applica..."]
    TEXTJOIN["TEXTJOIN<br/>TEXTJOIN performs specialized calculations for analytical ap..."]
    WEBSERVICE["WEBSERVICE<br/>WEBSERVICE performs specialized calculations for analytical ..."]
    FVSCHEDULE["FVSCHEDULE<br/>FVSCHEDULE performs specialized calculations for analytical ..."]
    EXPAND["EXPAND<br/>EXPAND performs specialized calculations for analytical appl..."]
    DROP["DROP<br/>DROP performs specialized calculations for analytical applic..."]
    WRAPROWS["WRAPROWS<br/>WRAPROWS performs specialized calculations for analytical ap..."]
    ENCODEURL["ENCODEURL<br/>ENCODEURL performs specialized calculations for analytical a..."]
    RRI["RRI<br/>RRI performs specialized calculations for analytical applica..."]
    TEXTBEFORE["TEXTBEFORE<br/>TEXTBEFORE performs specialized calculations for analytical ..."]
    INFO["INFO<br/>INFO performs specialized calculations for analytical applic..."]
    WRAPCOLS["WRAPCOLS<br/>WRAPCOLS performs specialized calculations for analytical ap..."]
    SORTBY["SORTBY<br/>SORTBY performs specialized calculations for analytical appl..."]
    TOROW["TOROW<br/>TOROW performs specialized calculations for analytical appli..."]
    VDB["VDB<br/>VDB performs specialized calculations for analytical applica..."]
    CHOOSECOLS["CHOOSECOLS<br/>CHOOSECOLS performs specialized calculations for analytical ..."]
    STOCKHISTORY["STOCKHISTORY<br/>STOCKHISTORY performs specialized calculations for analytica..."]
    VSTACK["VSTACK<br/>VSTACK performs specialized calculations for analytical appl..."]
    BYCOL["BYCOL<br/>BYCOL performs specialized calculations for analytical appli..."]
    REDUCE["REDUCE<br/>REDUCE performs specialized calculations for analytical appl..."]
    RANDARRAY["RANDARRAY<br/>RANDARRAY performs specialized calculations for analytical a..."]
    CHOOSEROWS["CHOOSEROWS<br/>CHOOSEROWS performs specialized calculations for analytical ..."]
    CUMPRINC["CUMPRINC<br/>CUMPRINC performs specialized calculations for analytical ap..."]
    VALUETOTEXT["VALUETOTEXT<br/>VALUETOTEXT performs specialized calculations for analytical..."]
    PDURATION["PDURATION<br/>PDURATION performs specialized calculations for analytical a..."]
    ARRAYTOTEXT["ARRAYTOTEXT<br/>ARRAYTOTEXT performs specialized calculations for analytical..."]
    MAKEARRAY["MAKEARRAY<br/>MAKEARRAY performs specialized calculations for analytical a..."]
    SEQUENCE["SEQUENCE<br/>SEQUENCE performs specialized calculations for analytical ap..."]
    LAMBDA["LAMBDA<br/>LAMBDA performs specialized calculations for analytical appl..."]
    SORT["SORT<br/>SORT performs specialized calculations for analytical applic..."]
    CELL["CELL<br/>CELL performs specialized calculations for analytical applic..."]
    BYROW["BYROW<br/>BYROW performs specialized calculations for analytical appli..."]
    TEXTSPLIT["TEXTSPLIT<br/>TEXTSPLIT performs specialized calculations for analytical a..."]
    HSTACK["HSTACK<br/>HSTACK performs specialized calculations for analytical appl..."]
    IF["IF<br/>External Function"]
    TOCOL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TOCOL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TOCOL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TOCOL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TOCOL -.-> IFERROR
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
    FILTERXML --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FILTERXML --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FILTERXML --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    FILTERXML -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FILTERXML -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SCAN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SCAN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SCAN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SCAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SCAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TEXTAFTER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TEXTAFTER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TEXTAFTER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TEXTAFTER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TEXTAFTER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MAP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MAP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    MAP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    MAP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MAP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TEXTJOIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TEXTJOIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TEXTJOIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TEXTJOIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TEXTJOIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    WEBSERVICE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    WEBSERVICE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    WEBSERVICE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    WEBSERVICE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    WEBSERVICE -.-> IFERROR
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
    EXPAND --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    EXPAND --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    EXPAND --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    EXPAND -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    EXPAND -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DROP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DROP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DROP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DROP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DROP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    WRAPROWS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    WRAPROWS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    WRAPROWS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    WRAPROWS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    WRAPROWS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ENCODEURL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ENCODEURL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ENCODEURL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ENCODEURL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ENCODEURL -.-> IFERROR
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
    IF["IF<br/>Related Function"]
    RRI -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    RRI -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TEXTBEFORE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TEXTBEFORE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TEXTBEFORE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TEXTBEFORE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TEXTBEFORE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    INFO --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    INFO --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    INFO --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    INFO -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    INFO -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    WRAPCOLS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    WRAPCOLS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    WRAPCOLS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    WRAPCOLS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    WRAPCOLS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SORTBY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SORTBY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SORTBY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SORTBY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SORTBY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TOROW --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TOROW --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TOROW --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TOROW -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TOROW -.-> IFERROR
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
    CHOOSECOLS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHOOSECOLS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CHOOSECOLS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CHOOSECOLS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CHOOSECOLS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    STOCKHISTORY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    STOCKHISTORY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    STOCKHISTORY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    STOCKHISTORY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    STOCKHISTORY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    VSTACK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VSTACK --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    VSTACK --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    VSTACK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    VSTACK -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BYCOL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BYCOL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BYCOL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BYCOL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BYCOL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    REDUCE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    REDUCE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    REDUCE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    REDUCE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    REDUCE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RANDARRAY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    RANDARRAY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    RANDARRAY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    RANDARRAY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    RANDARRAY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CHOOSEROWS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHOOSEROWS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CHOOSEROWS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CHOOSEROWS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CHOOSEROWS -.-> IFERROR
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
    VALUETOTEXT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VALUETOTEXT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    VALUETOTEXT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    VALUETOTEXT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    VALUETOTEXT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PDURATION --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PDURATION --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    PDURATION --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    PDURATION -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PDURATION -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ARRAYTOTEXT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ARRAYTOTEXT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ARRAYTOTEXT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ARRAYTOTEXT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ARRAYTOTEXT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MAKEARRAY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MAKEARRAY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    MAKEARRAY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    MAKEARRAY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MAKEARRAY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SEQUENCE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SEQUENCE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SEQUENCE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SEQUENCE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SEQUENCE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LAMBDA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    LAMBDA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    LAMBDA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    LAMBDA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LAMBDA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SORT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SORT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SORT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SORT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SORT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CELL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CELL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CELL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CELL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CELL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BYROW --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BYROW --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BYROW --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BYROW -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BYROW -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TEXTSPLIT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TEXTSPLIT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TEXTSPLIT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TEXTSPLIT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TEXTSPLIT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HSTACK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HSTACK --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    HSTACK --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    HSTACK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    HSTACK -.-> IFERROR
    class IFERROR external
    class TOCOL Excel-specific
    class CUMIPMT Excel-specific
    class FILTERXML Excel-specific
    class SCAN Excel-specific
    class TEXTAFTER Excel-specific
    class MAP Excel-specific
    class TEXTJOIN Excel-specific
    class WEBSERVICE Excel-specific
    class FVSCHEDULE Excel-specific
    class EXPAND Excel-specific
    class DROP Excel-specific
    class WRAPROWS Excel-specific
    class ENCODEURL Excel-specific
    class RRI Excel-specific
    class TEXTBEFORE Excel-specific
    class INFO Excel-specific
    class WRAPCOLS Excel-specific
    class SORTBY Excel-specific
    class TOROW Excel-specific
    class VDB Excel-specific
    class CHOOSECOLS Excel-specific
    class STOCKHISTORY Excel-specific
    class VSTACK Excel-specific
    class BYCOL Excel-specific
    class REDUCE Excel-specific
    class RANDARRAY Excel-specific
    class CHOOSEROWS Excel-specific
    class CUMPRINC Excel-specific
    class VALUETOTEXT Excel-specific
    class PDURATION Excel-specific
    class ARRAYTOTEXT Excel-specific
    class MAKEARRAY Excel-specific
    class SEQUENCE Excel-specific
    class LAMBDA Excel-specific
    class SORT Excel-specific
    class CELL Excel-specific
    class BYROW Excel-specific
    class TEXTSPLIT Excel-specific
    class HSTACK Excel-specific
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 39
