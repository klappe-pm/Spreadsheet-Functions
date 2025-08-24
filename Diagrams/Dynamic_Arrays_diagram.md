# Dynamic Arrays Functions Relationship Diagram

This diagram shows the relationships between functions in the Dynamic Arrays category and their connections to commonly used functions.

```mermaid
graph TD
    classDef DynamicArrays fill:#FD79A8,stroke:#333,stroke-width:2px,color:#000
    TAKE["TAKE<br/>TAKE performs specialized calculations for analytical applic..."]
    FILTER["FILTER<br/>FILTER performs specialized calculations for analytical appl..."]
    XLOOKUP["XLOOKUP<br/>XLOOKUP performs specialized calculations for analytical app..."]
    LET["LET<br/>LET performs specialized calculations for analytical applica..."]
    XMATCH["XMATCH<br/>XMATCH performs specialized calculations for analytical appl..."]
    SORT["SORT<br/>SORT performs specialized calculations for analytical applic..."]
    UNIQUE["UNIQUE<br/>UNIQUE performs specialized calculations for analytical appl..."]
    IF["IF<br/>External Function"]
    TAKE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TAKE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TAKE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TAKE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TAKE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FILTER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FILTER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FILTER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    FILTER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FILTER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    XLOOKUP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    XLOOKUP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    XLOOKUP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    XLOOKUP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    XLOOKUP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LET --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    LET --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    LET --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    LET -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LET -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    XMATCH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    XMATCH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    XMATCH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    XMATCH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    XMATCH -.-> IFERROR
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
    UNIQUE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    UNIQUE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    UNIQUE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    UNIQUE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    UNIQUE -.-> IFERROR
    class IFERROR external
    class TAKE DynamicArrays
    class FILTER DynamicArrays
    class XLOOKUP DynamicArrays
    class LET DynamicArrays
    class XMATCH DynamicArrays
    class SORT DynamicArrays
    class UNIQUE DynamicArrays
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 7
