# Google-specific Functions Relationship Diagram

This diagram shows the relationships between functions in the Google-specific category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Google-specific fill:#A29BFE,stroke:#333,stroke-width:2px,color:#000
    EPOCHTODATE["EPOCHTODATE<br/>EPOCHTODATE performs date and time calculations for temporal..."]
    SCAN["SCAN<br/>SCAN performs specialized calculations for analytical applic..."]
    MAP["MAP<br/>MAP performs specialized calculations for analytical applica..."]
    SPARKLINE["SPARKLINE<br/>SPARKLINE performs specialized calculations for analytical a..."]
    SPLIT["SPLIT<br/>SPLIT performs specialized calculations for analytical appli..."]
    TRANSPOSE["TRANSPOSE<br/>TRANSPOSE performs specialized calculations for analytical a..."]
    LET["LET<br/>LET performs specialized calculations for analytical applica..."]
    REGEXMATCH["REGEXMATCH<br/>REGEXMATCH performs specialized calculations for analytical ..."]
    IMAGE["IMAGE<br/>IMAGE performs specialized calculations for analytical appli..."]
    IMPORTDATA["IMPORTDATA<br/>IMPORTDATA performs specialized calculations for analytical ..."]
    IMPORTXML["IMPORTXML<br/>IMPORTXML performs specialized calculations for analytical a..."]
    GOOGLETRANSLATE["GOOGLETRANSLATE<br/>GOOGLETRANSLATE performs specialized calculations for analyt..."]
    SORTN["SORTN<br/>SORTN performs specialized calculations for analytical appli..."]
    COUNTUNIQUE["COUNTUNIQUE<br/>COUNTUNIQUE performs specialized calculations for analytical..."]
    FLATTEN["FLATTEN<br/>FLATTEN performs specialized calculations for analytical app..."]
    REGEXEXTRACT["REGEXEXTRACT<br/>REGEXEXTRACT performs specialized calculations for analytica..."]
    REDUCE["REDUCE<br/>REDUCE performs specialized calculations for analytical appl..."]
    REGEXREPLACE["REGEXREPLACE<br/>REGEXREPLACE performs specialized calculations for analytica..."]
    QUERY["QUERY<br/>QUERY performs specialized calculations for analytical appli..."]
    ARRAYFORMULA["ARRAYFORMULA<br/>ARRAYFORMULA performs specialized calculations for analytica..."]
    DETECTLANGUAGE["DETECTLANGUAGE<br/>DETECTLANGUAGE performs specialized calculations for analyti..."]
    GOOGLEFINANCE["GOOGLEFINANCE<br/>GOOGLEFINANCE performs specialized calculations for analytic..."]
    IMPORTRANGE["IMPORTRANGE<br/>IMPORTRANGE performs specialized calculations for analytical..."]
    IMPORTHTML["IMPORTHTML<br/>IMPORTHTML performs specialized calculations for analytical ..."]
    GETJSON["GETJSON<br/>GETJSON performs specialized calculations for analytical app..."]
    JOIN["JOIN<br/>JOIN performs specialized calculations for analytical applic..."]
    ISBETWEEN["ISBETWEEN<br/>ISBETWEEN performs specialized calculations for analytical a..."]
    MAKEARRAY["MAKEARRAY<br/>MAKEARRAY performs specialized calculations for analytical a..."]
    BYCOL__["BYCOL _<br/>BYCOL _ performs specialized calculations for analytical app..."]
    IMPORTFEED["IMPORTFEED<br/>IMPORTFEED performs specialized calculations for analytical ..."]
    BYROW["BYROW<br/>BYROW performs specialized calculations for analytical appli..."]
    UNIQUE["UNIQUE<br/>UNIQUE performs specialized calculations for analytical appl..."]
    TODAY["TODAY<br/>External Function"]
    EPOCHTODATE --> TODAY
    class TODAY external
    IF["IF<br/>External Function"]
    EPOCHTODATE --> IF
    class IF external
    YEAR["YEAR<br/>External Function"]
    EPOCHTODATE --> YEAR
    class YEAR external
    TODAY["TODAY<br/>Related Function"]
    EPOCHTODATE -.-> TODAY
    class TODAY external
    NOW["NOW<br/>Related Function"]
    EPOCHTODATE -.-> NOW
    class NOW external
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
    SPARKLINE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SPARKLINE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SPARKLINE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SPARKLINE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SPARKLINE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SPLIT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SPLIT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SPLIT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SPLIT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SPLIT -.-> IFERROR
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
    REGEXMATCH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    REGEXMATCH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    REGEXMATCH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    REGEXMATCH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    REGEXMATCH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMAGE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMAGE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMAGE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMAGE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMAGE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMPORTDATA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPORTDATA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPORTDATA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMPORTDATA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMPORTDATA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMPORTXML --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPORTXML --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPORTXML --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMPORTXML -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMPORTXML -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GOOGLETRANSLATE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GOOGLETRANSLATE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    GOOGLETRANSLATE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    GOOGLETRANSLATE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GOOGLETRANSLATE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SORTN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SORTN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SORTN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SORTN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SORTN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUNTUNIQUE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUNTUNIQUE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COUNTUNIQUE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    COUNTUNIQUE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COUNTUNIQUE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FLATTEN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FLATTEN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FLATTEN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    FLATTEN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FLATTEN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    REGEXEXTRACT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    REGEXEXTRACT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    REGEXEXTRACT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    REGEXEXTRACT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    REGEXEXTRACT -.-> IFERROR
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
    REGEXREPLACE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    REGEXREPLACE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    REGEXREPLACE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    REGEXREPLACE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    REGEXREPLACE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    QUERY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    QUERY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    QUERY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    QUERY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    QUERY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ARRAYFORMULA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ARRAYFORMULA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ARRAYFORMULA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ARRAYFORMULA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ARRAYFORMULA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DETECTLANGUAGE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DETECTLANGUAGE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DETECTLANGUAGE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DETECTLANGUAGE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DETECTLANGUAGE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GOOGLEFINANCE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GOOGLEFINANCE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    GOOGLEFINANCE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    GOOGLEFINANCE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GOOGLEFINANCE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMPORTRANGE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPORTRANGE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPORTRANGE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMPORTRANGE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMPORTRANGE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMPORTHTML --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPORTHTML --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPORTHTML --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMPORTHTML -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMPORTHTML -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GETJSON --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GETJSON --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    GETJSON --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    GETJSON -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GETJSON -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    JOIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    JOIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    JOIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    JOIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    JOIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISBETWEEN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISBETWEEN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISBETWEEN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISBETWEEN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISBETWEEN -.-> IFERROR
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
    BYCOL__ --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BYCOL__ --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BYCOL__ --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BYCOL__ -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BYCOL__ -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMPORTFEED --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPORTFEED --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPORTFEED --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMPORTFEED -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMPORTFEED -.-> IFERROR
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
    class EPOCHTODATE Google-specific
    class SCAN Google-specific
    class MAP Google-specific
    class SPARKLINE Google-specific
    class SPLIT Google-specific
    class TRANSPOSE Google-specific
    class LET Google-specific
    class REGEXMATCH Google-specific
    class IMAGE Google-specific
    class IMPORTDATA Google-specific
    class IMPORTXML Google-specific
    class GOOGLETRANSLATE Google-specific
    class SORTN Google-specific
    class COUNTUNIQUE Google-specific
    class FLATTEN Google-specific
    class REGEXEXTRACT Google-specific
    class REDUCE Google-specific
    class REGEXREPLACE Google-specific
    class QUERY Google-specific
    class ARRAYFORMULA Google-specific
    class DETECTLANGUAGE Google-specific
    class GOOGLEFINANCE Google-specific
    class IMPORTRANGE Google-specific
    class IMPORTHTML Google-specific
    class GETJSON Google-specific
    class JOIN Google-specific
    class ISBETWEEN Google-specific
    class MAKEARRAY Google-specific
    class BYCOL__ Google-specific
    class IMPORTFEED Google-specific
    class BYROW Google-specific
    class UNIQUE Google-specific
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 32
