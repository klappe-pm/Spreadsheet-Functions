# Logical Functions Relationship Diagram

This diagram shows the relationships between functions in the Logical category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Logical fill:#96CEB4,stroke:#333,stroke-width:2px,color:#000
    FILTER["FILTER<br/>FILTER evaluates logical conditions and implements condition..."]
    XOR["XOR<br/>XOR evaluates logical conditions and implements conditional ..."]
    NOT["NOT<br/>NOT evaluates logical conditions and implements conditional ..."]
    IF["IF<br/>IF performs a logical test and returns one value if true and..."]
    AND["AND<br/>AND returns TRUE if all arguments are TRUE, and FALSE if any..."]
    IFNA["IFNA<br/>IFNA evaluates logical conditions and implements conditional..."]
    ISNA["ISNA<br/>ISNA evaluates logical conditions and implements conditional..."]
    IFS["IFS<br/>IFS performs conditional calculations based on specified cri..."]
    ISERR["ISERR<br/>ISERR evaluates logical conditions and implements conditiona..."]
    ISERROR["ISERROR<br/>ISERROR evaluates logical conditions and implements conditio..."]
    SWITCH["SWITCH<br/>SWITCH evaluates logical conditions and implements condition..."]
    IFERROR["IFERROR<br/>IFERROR evaluates logical conditions and implements conditio..."]
    LAMBDA["LAMBDA<br/>LAMBDA evaluates logical conditions and implements condition..."]
    OR["OR<br/>OR returns TRUE if any argument is TRUE, and FALSE only if a..."]
    FILTER --> IF
    SUM["SUM<br/>External Function"]
    FILTER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FILTER --> AVERAGE
    class AVERAGE external
    FILTER -.-> IF
    FILTER -.-> IFERROR
    XOR --> IF
    SUM["SUM<br/>External Function"]
    XOR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    XOR --> AVERAGE
    class AVERAGE external
    XOR -.-> IF
    XOR -.-> IFERROR
    NOT --> IF
    SUM["SUM<br/>External Function"]
    NOT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    NOT --> AVERAGE
    class AVERAGE external
    NOT -.-> IF
    NOT -.-> IFERROR
    IF --> AND
    IF --> OR
    IF --> IFERROR
    IF -.-> IFS
    IF -.-> IFERROR
    AND --> IF
    AND --> OR
    AND --> NOT
    AND -.-> OR
    AND -.-> NOT
    IFNA --> IF
    SUM["SUM<br/>External Function"]
    IFNA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IFNA --> AVERAGE
    class AVERAGE external
    IFNA -.-> IF
    IFNA -.-> IFERROR
    ISNA --> IF
    SUM["SUM<br/>External Function"]
    ISNA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISNA --> AVERAGE
    class AVERAGE external
    ISNA -.-> IF
    ISNA -.-> IFERROR
    IFS --> IF
    SUM["SUM<br/>External Function"]
    IFS --> SUM
    class SUM external
    COUNT["COUNT<br/>External Function"]
    IFS --> COUNT
    class COUNT external
    IFS -.-> IF
    SUMIF["SUMIF<br/>Related Function"]
    IFS -.-> SUMIF
    class SUMIF external
    ISERR --> IF
    SUM["SUM<br/>External Function"]
    ISERR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISERR --> AVERAGE
    class AVERAGE external
    ISERR -.-> IF
    ISERR -.-> IFERROR
    ISERROR --> IF
    SUM["SUM<br/>External Function"]
    ISERROR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISERROR --> AVERAGE
    class AVERAGE external
    ISERROR -.-> IF
    ISERROR -.-> IFERROR
    SWITCH --> IF
    SUM["SUM<br/>External Function"]
    SWITCH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SWITCH --> AVERAGE
    class AVERAGE external
    SWITCH -.-> IF
    SWITCH -.-> IFERROR
    IFERROR --> IF
    SUM["SUM<br/>External Function"]
    IFERROR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IFERROR --> AVERAGE
    class AVERAGE external
    IFERROR -.-> IF
    IFERROR -.-> IFERROR
    LAMBDA --> IF
    SUM["SUM<br/>External Function"]
    LAMBDA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    LAMBDA --> AVERAGE
    class AVERAGE external
    LAMBDA -.-> IF
    LAMBDA -.-> IFERROR
    OR --> IF
    OR --> AND
    OR --> NOT
    OR -.-> AND
    OR -.-> NOT
    class FILTER Logical
    class XOR Logical
    class NOT Logical
    class IF Logical
    class AND Logical
    class IFNA Logical
    class ISNA Logical
    class IFS Logical
    class ISERR Logical
    class ISERROR Logical
    class SWITCH Logical
    class IFERROR Logical
    class LAMBDA Logical
    class OR Logical
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 14
