# Lookup & Reference Functions Relationship Diagram

This diagram shows the relationships between functions in the Lookup & Reference category and their connections to commonly used functions.

```mermaid
graph TD
    classDef LookupReference fill:#FECA57,stroke:#333,stroke-width:2px,color:#000
    TAKE["TAKE<br/>TAKE performs specialized calculations for analytical applic..."]
    FILTER["FILTER<br/>FILTER performs specialized calculations for analytical appl..."]
    XLOOKUP["XLOOKUP<br/>XLOOKUP performs specialized calculations for analytical app..."]
    COLUMNS["COLUMNS<br/>COLUMNS performs specialized calculations for analytical app..."]
    INDIRECT["INDIRECT<br/>INDIRECT performs specialized calculations for analytical ap..."]
    TRANSPOSE["TRANSPOSE<br/>TRANSPOSE performs specialized calculations for analytical a..."]
    EXPAND["EXPAND<br/>EXPAND performs specialized calculations for analytical appl..."]
    MATCH["MATCH<br/>MATCH searches for a value in a range and returns the relati..."]
    DROP["DROP<br/>DROP performs specialized calculations for analytical applic..."]
    COLUMN["COLUMN<br/>COLUMN performs specialized calculations for analytical appl..."]
    WRAPROWS["WRAPROWS<br/>WRAPROWS performs specialized calculations for analytical ap..."]
    XMATCH["XMATCH<br/>XMATCH performs specialized calculations for analytical appl..."]
    ROWS["ROWS<br/>ROWS performs specialized calculations for analytical applic..."]
    WRAPCOLS["WRAPCOLS<br/>WRAPCOLS performs specialized calculations for analytical ap..."]
    ROW["ROW<br/>ROW performs specialized calculations for analytical applica..."]
    CHOOSECOLS["CHOOSECOLS<br/>CHOOSECOLS performs specialized calculations for analytical ..."]
    CHOOSE["CHOOSE<br/>CHOOSE performs specialized calculations for analytical appl..."]
    VSTACK["VSTACK<br/>VSTACK performs specialized calculations for analytical appl..."]
    INDEX["INDEX<br/>INDEX returns the value at a specified row and column inters..."]
    ADDRESS["ADDRESS<br/>ADDRESS performs specialized calculations for analytical app..."]
    CHOOSEROWS["CHOOSEROWS<br/>CHOOSEROWS performs specialized calculations for analytical ..."]
    OFFSET["OFFSET<br/>OFFSET performs specialized calculations for analytical appl..."]
    HLOOKUP["HLOOKUP<br/>HLOOKUP performs specialized calculations for analytical app..."]
    VLOOKUP["VLOOKUP<br/>VLOOKUP searches for a value in the first column of a range ..."]
    GETPIVOTDATA["GETPIVOTDATA<br/>GETPIVOTDATA performs specialized calculations for analytica..."]
    AREAS["AREAS<br/>AREAS performs specialized calculations for analytical appli..."]
    LOOKUP["LOOKUP<br/>LOOKUP performs specialized calculations for analytical appl..."]
    HYPERLINK["HYPERLINK<br/>HYPERLINK performs specialized calculations for analytical a..."]
    HSTACK["HSTACK<br/>HSTACK performs specialized calculations for analytical appl..."]
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
    COLUMNS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COLUMNS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COLUMNS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    COLUMNS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COLUMNS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    INDIRECT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    INDIRECT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    INDIRECT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    INDIRECT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    INDIRECT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TRANSPOSE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TRANSPOSE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TRANSPOSE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TRANSPOSE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TRANSPOSE -.-> IFERROR
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
    MATCH --> INDEX
    IF["IF<br/>External Function"]
    MATCH --> IF
    class IF external
    MAX["MAX<br/>External Function"]
    MATCH --> MAX
    class MAX external
    MATCH -.-> INDEX
    FIND["FIND<br/>Related Function"]
    MATCH -.-> FIND
    class FIND external
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
    COLUMN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COLUMN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COLUMN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    COLUMN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COLUMN -.-> IFERROR
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
    ROWS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ROWS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ROWS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ROWS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ROWS -.-> IFERROR
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
    ROW --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ROW --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ROW --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ROW -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ROW -.-> IFERROR
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
    CHOOSE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHOOSE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CHOOSE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CHOOSE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CHOOSE -.-> IFERROR
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
    INDEX --> MATCH
    IF["IF<br/>External Function"]
    INDEX --> IF
    class IF external
    SMALL["SMALL<br/>External Function"]
    INDEX --> SMALL
    class SMALL external
    INDEX -.-> MATCH
    INDEX -.-> OFFSET
    IF["IF<br/>External Function"]
    ADDRESS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ADDRESS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ADDRESS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ADDRESS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ADDRESS -.-> IFERROR
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
    OFFSET --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    OFFSET --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    OFFSET --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    OFFSET -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    OFFSET -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HLOOKUP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HLOOKUP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    HLOOKUP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    HLOOKUP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    HLOOKUP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    VLOOKUP --> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    VLOOKUP --> IFERROR
    class IFERROR external
    VLOOKUP --> MATCH
    VLOOKUP -.-> HLOOKUP
    VLOOKUP -.-> INDEX
    IF["IF<br/>External Function"]
    GETPIVOTDATA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GETPIVOTDATA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    GETPIVOTDATA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    GETPIVOTDATA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GETPIVOTDATA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    AREAS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    AREAS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    AREAS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    AREAS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    AREAS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LOOKUP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    LOOKUP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    LOOKUP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    LOOKUP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LOOKUP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HYPERLINK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HYPERLINK --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    HYPERLINK --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    HYPERLINK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    HYPERLINK -.-> IFERROR
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
    class TAKE LookupReference
    class FILTER LookupReference
    class XLOOKUP LookupReference
    class COLUMNS LookupReference
    class INDIRECT LookupReference
    class TRANSPOSE LookupReference
    class EXPAND LookupReference
    class MATCH LookupReference
    class DROP LookupReference
    class COLUMN LookupReference
    class WRAPROWS LookupReference
    class XMATCH LookupReference
    class ROWS LookupReference
    class WRAPCOLS LookupReference
    class ROW LookupReference
    class CHOOSECOLS LookupReference
    class CHOOSE LookupReference
    class VSTACK LookupReference
    class INDEX LookupReference
    class ADDRESS LookupReference
    class CHOOSEROWS LookupReference
    class OFFSET LookupReference
    class HLOOKUP LookupReference
    class VLOOKUP LookupReference
    class GETPIVOTDATA LookupReference
    class AREAS LookupReference
    class LOOKUP LookupReference
    class HYPERLINK LookupReference
    class HSTACK LookupReference
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 29
