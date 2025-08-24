# Text Functions Relationship Diagram

This diagram shows the relationships between functions in the Text category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Text fill:#45B7D1,stroke:#333,stroke-width:2px,color:#000
    TEXT["TEXT<br/>TEXT manipulates and analyzes text strings for data processi..."]
    FIND["FIND<br/>FIND manipulates and analyzes text strings for data processi..."]
    BAHTTEXT["BAHTTEXT<br/>BAHTTEXT manipulates and analyzes text strings for data proc..."]
    TEXTAFTER["TEXTAFTER<br/>TEXTAFTER manipulates and analyzes text strings for data pro..."]
    LOWER["LOWER<br/>LOWER manipulates and analyzes text strings for data process..."]
    SEARCH_["SEARCH-<br/>SEARCH- manipulates and analyzes text strings for data proce..."]
    TEXTJOIN["TEXTJOIN<br/>TEXTJOIN manipulates and analyzes text strings for data proc..."]
    SPLIT["SPLIT<br/>SPLIT manipulates and analyzes text strings for data process..."]
    DOLLAR["DOLLAR<br/>DOLLAR manipulates and analyzes text strings for data proces..."]
    EXACT["EXACT<br/>EXACT manipulates and analyzes text strings for data process..."]
    PROPER["PROPER<br/>PROPER manipulates and analyzes text strings for data proces..."]
    REGEXMATCH["REGEXMATCH<br/>REGEXMATCH manipulates and analyzes text strings for data pr..."]
    REPLACE["REPLACE<br/>REPLACE manipulates and analyzes text strings for data proce..."]
    T["T<br/>T manipulates and analyzes text strings for data processing ..."]
    TEXTBEFORE["TEXTBEFORE<br/>TEXTBEFORE manipulates and analyzes text strings for data pr..."]
    VALUE["VALUE<br/>VALUE manipulates and analyzes text strings for data process..."]
    NUMBERVALUE["NUMBERVALUE<br/>NUMBERVALUE manipulates and analyzes text strings for data p..."]
    JIS["JIS<br/>JIS manipulates and analyzes text strings for data processin..."]
    MID["MID<br/>MID manipulates and analyzes text strings for data processin..."]
    ASC["ASC<br/>ASC manipulates and analyzes text strings for data processin..."]
    PHONETIC["PHONETIC<br/>PHONETIC manipulates and analyzes text strings for data proc..."]
    CLEAN["CLEAN<br/>CLEAN manipulates and analyzes text strings for data process..."]
    REGEXEXTRACT["REGEXEXTRACT<br/>REGEXEXTRACT manipulates and analyzes text strings for data ..."]
    LEFT["LEFT<br/>LEFT extracts a specified number of characters from the begi..."]
    CONCAT["CONCAT<br/>CONCAT manipulates and analyzes text strings for data proces..."]
    UNICODE["UNICODE<br/>UNICODE manipulates and analyzes text strings for data proce..."]
    SUBSTITUTE["SUBSTITUTE<br/>SUBSTITUTE manipulates and analyzes text strings for data pr..."]
    REGEXREPLACE["REGEXREPLACE<br/>REGEXREPLACE manipulates and analyzes text strings for data ..."]
    UNICHAR["UNICHAR<br/>UNICHAR manipulates and analyzes text strings for data proce..."]
    CONCATENATE["CONCATENATE<br/>CONCATENATE joins multiple text strings into one string. Thi..."]
    RIGHT["RIGHT<br/>RIGHT extracts a specified number of characters from the end..."]
    CODE["CODE<br/>CODE manipulates and analyzes text strings for data processi..."]
    JOIN["JOIN<br/>JOIN manipulates and analyzes text strings for data processi..."]
    TRIM["TRIM<br/>TRIM manipulates and analyzes text strings for data processi..."]
    UPPER["UPPER<br/>UPPER manipulates and analyzes text strings for data process..."]
    FIXED["FIXED<br/>FIXED manipulates and analyzes text strings for data process..."]
    LEN["LEN<br/>LEN returns the number of characters in a text string, inclu..."]
    REPT["REPT<br/>REPT manipulates and analyzes text strings for data processi..."]
    TEXTSPLIT["TEXTSPLIT<br/>TEXTSPLIT manipulates and analyzes text strings for data pro..."]
    CHAR["CHAR<br/>CHAR manipulates and analyzes text strings for data processi..."]
    IF["IF<br/>External Function"]
    TEXT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TEXT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TEXT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TEXT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TEXT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FIND --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FIND --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FIND --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    FIND -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FIND -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BAHTTEXT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BAHTTEXT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BAHTTEXT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BAHTTEXT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BAHTTEXT -.-> IFERROR
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
    LOWER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    LOWER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    LOWER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    LOWER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LOWER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SEARCH_ --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SEARCH_ --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SEARCH_ --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SEARCH_ -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SEARCH_ -.-> IFERROR
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
    DOLLAR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DOLLAR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DOLLAR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DOLLAR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DOLLAR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    EXACT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    EXACT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    EXACT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    EXACT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    EXACT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PROPER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PROPER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    PROPER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    PROPER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PROPER -.-> IFERROR
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
    REPLACE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    REPLACE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    REPLACE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    REPLACE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    REPLACE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    T --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    T --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    T --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    T -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    T -.-> IFERROR
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
    VALUE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VALUE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    VALUE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    VALUE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    VALUE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    NUMBERVALUE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    NUMBERVALUE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    NUMBERVALUE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    NUMBERVALUE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    NUMBERVALUE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    JIS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    JIS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    JIS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    JIS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    JIS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MID --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MID --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    MID --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    MID -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MID -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ASC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ASC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ASC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ASC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ASC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PHONETIC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PHONETIC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    PHONETIC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    PHONETIC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PHONETIC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CLEAN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CLEAN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CLEAN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CLEAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CLEAN -.-> IFERROR
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
    LEFT --> IF
    class IF external
    LEFT --> LEN
    LEFT --> FIND
    LEFT -.-> RIGHT
    LEFT -.-> MID
    IF["IF<br/>External Function"]
    CONCAT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CONCAT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CONCAT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CONCAT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CONCAT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    UNICODE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    UNICODE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    UNICODE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    UNICODE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    UNICODE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SUBSTITUTE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SUBSTITUTE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SUBSTITUTE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SUBSTITUTE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SUBSTITUTE -.-> IFERROR
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
    UNICHAR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    UNICHAR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    UNICHAR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    UNICHAR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    UNICHAR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CONCATENATE --> IF
    class IF external
    CONCATENATE --> LEFT
    CONCATENATE --> RIGHT
    CONCATENATE -.-> CONCAT
    TEXTJOIN["TEXTJOIN<br/>Related Function"]
    CONCATENATE -.-> TEXTJOIN
    class TEXTJOIN external
    IF["IF<br/>External Function"]
    RIGHT --> IF
    class IF external
    RIGHT --> LEN
    RIGHT --> FIND
    RIGHT -.-> LEFT
    RIGHT -.-> MID
    IF["IF<br/>External Function"]
    CODE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CODE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CODE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CODE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CODE -.-> IFERROR
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
    TRIM --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TRIM --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TRIM --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TRIM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TRIM -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    UPPER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    UPPER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    UPPER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    UPPER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    UPPER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FIXED --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FIXED --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FIXED --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    FIXED -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FIXED -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LEN --> IF
    class IF external
    LEN --> LEFT
    LEN --> RIGHT
    LEN -.-> LEFT
    LEN -.-> RIGHT
    IF["IF<br/>External Function"]
    REPT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    REPT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    REPT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    REPT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    REPT -.-> IFERROR
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
    CHAR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHAR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CHAR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CHAR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CHAR -.-> IFERROR
    class IFERROR external
    class TEXT Text
    class FIND Text
    class BAHTTEXT Text
    class TEXTAFTER Text
    class LOWER Text
    class SEARCH_ Text
    class TEXTJOIN Text
    class SPLIT Text
    class DOLLAR Text
    class EXACT Text
    class PROPER Text
    class REGEXMATCH Text
    class REPLACE Text
    class T Text
    class TEXTBEFORE Text
    class VALUE Text
    class NUMBERVALUE Text
    class JIS Text
    class MID Text
    class ASC Text
    class PHONETIC Text
    class CLEAN Text
    class REGEXEXTRACT Text
    class LEFT Text
    class CONCAT Text
    class UNICODE Text
    class SUBSTITUTE Text
    class REGEXREPLACE Text
    class UNICHAR Text
    class CONCATENATE Text
    class RIGHT Text
    class CODE Text
    class JOIN Text
    class TRIM Text
    class UPPER Text
    class FIXED Text
    class LEN Text
    class REPT Text
    class TEXTSPLIT Text
    class CHAR Text
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 40
