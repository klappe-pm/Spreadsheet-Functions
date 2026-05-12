# Web Functions Relationship Diagram

This diagram shows the relationships between functions in the Web category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Web fill:#00B894,stroke:#333,stroke-width:2px,color:#000
    IMPORTJSON["IMPORTJSON<br/>IMPORTJSON performs specialized calculations for analytical ..."]
    IF["IF<br/>External Function"]
    IMPORTJSON --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPORTJSON --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPORTJSON --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMPORTJSON -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMPORTJSON -.-> IFERROR
    class IFERROR external
    class IMPORTJSON Web
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 1
