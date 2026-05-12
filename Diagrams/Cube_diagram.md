# Cube Functions Relationship Diagram

This diagram shows the relationships between functions in the Cube category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Cube fill:#E17055,stroke:#333,stroke-width:2px,color:#000
    CUBERANKEDMEMBER["CUBERANKEDMEMBER<br/>CUBERANKEDMEMBER performs specialized calculations for analy..."]
    CUBEMEMBER["CUBEMEMBER<br/>CUBEMEMBER performs specialized calculations for analytical ..."]
    CUBESET["CUBESET<br/>CUBESET performs specialized calculations for analytical app..."]
    CUBESETCOUNT["CUBESETCOUNT<br/>CUBESETCOUNT performs specialized calculations for analytica..."]
    CUBEKPIMEMBER["CUBEKPIMEMBER<br/>CUBEKPIMEMBER performs specialized calculations for analytic..."]
    CUBEVALUE["CUBEVALUE<br/>CUBEVALUE performs specialized calculations for analytical a..."]
    IF["IF<br/>External Function"]
    CUBERANKEDMEMBER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBERANKEDMEMBER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBERANKEDMEMBER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CUBERANKEDMEMBER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CUBERANKEDMEMBER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBEMEMBER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBEMEMBER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBEMEMBER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CUBEMEMBER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CUBEMEMBER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBESET --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBESET --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBESET --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CUBESET -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CUBESET -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBESETCOUNT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBESETCOUNT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBESETCOUNT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CUBESETCOUNT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CUBESETCOUNT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBEKPIMEMBER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBEKPIMEMBER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBEKPIMEMBER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CUBEKPIMEMBER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CUBEKPIMEMBER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBEVALUE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBEVALUE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBEVALUE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CUBEVALUE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CUBEVALUE -.-> IFERROR
    class IFERROR external
    class CUBERANKEDMEMBER Cube
    class CUBEMEMBER Cube
    class CUBESET Cube
    class CUBESETCOUNT Cube
    class CUBEKPIMEMBER Cube
    class CUBEVALUE Cube
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 6
