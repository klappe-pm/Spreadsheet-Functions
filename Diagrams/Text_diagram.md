---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Text
purpose:
  - Function Relationships
use-case:
  - Choosing a Text Function
  - Cleaning and Converting Text
related:
  - ASC
  - AVERAGE
  - BAHTTEXT
  - CHAR
  - CLEAN
  - CODE
  - CONCAT
  - CONCATENATE
  - DOLLAR
  - EXACT
  - FIND
  - FIXED
  - IF
  - IFERROR
  - JIS
  - JOIN
  - LEFT
  - LEN
  - LOWER
  - MID
  - NUMBERVALUE
  - PHONETIC
  - PROPER
  - REGEXEXTRACT
  - REGEXMATCH
  - REGEXREPLACE
  - REPLACE
  - REPT
  - RIGHT
  - SEARCH
  - SPLIT
  - SUBSTITUTE
  - SUM
  - T
  - TEXT
  - TEXTAFTER
  - TEXTBEFORE
  - TEXTSPLIT
  - TRIM
level: 2
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - excel
  - google-sheets
  - text
---

# Text Functions Relationship Diagram

This diagram shows the relationships between functions in the Text category and their connections to commonly used functions. It shows 40 of the category's functions.

```mermaid
graph TD
    classDef Text fill:#45B7D1,stroke:#333,stroke-width:2px,color:#000
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
    TEXT["TEXT<br/>Formats a number, date or time as text using a format pattern"]
    FIND["FIND<br/>Finds one text string inside another, case-sensitive"]
    BAHTTEXT["BAHTTEXT<br/>Converts a number to Thai baht text"]
    TEXTAFTER["TEXTAFTER<br/>Returns the text that comes after a delimiter"]
    LOWER["LOWER<br/>Converts text to lowercase"]
    SEARCH["SEARCH<br/>Finds one text string inside another, case-insensitive"]
    TEXTJOIN["TEXTJOIN<br/>Joins text from several items with a delimiter"]
    SPLIT["SPLIT<br/>Divides text at a delimiter into separate cells"]
    DOLLAR["DOLLAR<br/>Formats a number as currency text"]
    EXACT["EXACT<br/>Tests whether two text strings are identical, case-sensitive"]
    PROPER["PROPER<br/>Capitalizes the first letter of each word"]
    REGEXMATCH["REGEXMATCH<br/>Tests whether text matches a regular expression"]
    REPLACE["REPLACE<br/>Replaces part of a text string by position"]
    T["T<br/>Returns text if the value is text, otherwise an empty string"]
    TEXTBEFORE["TEXTBEFORE<br/>Returns the text that comes before a delimiter"]
    VALUE["VALUE<br/>Converts text that looks like a number into a number"]
    NUMBERVALUE["NUMBERVALUE<br/>Converts text to a number using set separators"]
    JIS["JIS<br/>Converts half-width characters to full-width (East Asian text)"]
    MID["MID<br/>Returns characters from the middle of a text string"]
    ASC["ASC<br/>Converts full-width characters to half-width (East Asian text)"]
    PHONETIC["PHONETIC<br/>Returns the furigana (phonetic guide) stored with text"]
    CLEAN["CLEAN<br/>Removes nonprintable characters from text"]
    REGEXEXTRACT["REGEXEXTRACT<br/>Returns the part of text that matches a regular expression"]
    LEFT["LEFT<br/>Returns a set number of characters from the start of text"]
    CONCAT["CONCAT<br/>Joins text from several items with no delimiter"]
    UNICODE["UNICODE<br/>Returns the Unicode number of the first character"]
    SUBSTITUTE["SUBSTITUTE<br/>Replaces existing text with new text in a string"]
    REGEXREPLACE["REGEXREPLACE<br/>Replaces text that matches a regular expression"]
    UNICHAR["UNICHAR<br/>Returns the character for a Unicode number"]
    CONCATENATE["CONCATENATE<br/>Joins several text items into one string"]
    RIGHT["RIGHT<br/>Returns a set number of characters from the end of text"]
    CODE["CODE<br/>Returns the numeric code of the first character"]
    JOIN["JOIN<br/>Joins the values of arrays using a delimiter"]
    TRIM["TRIM<br/>Removes extra spaces, keeping single spaces between words"]
    UPPER["UPPER<br/>Converts text to uppercase"]
    FIXED["FIXED<br/>Rounds a number to fixed decimals and returns text"]
    LEN["LEN<br/>Returns the number of characters in a text string"]
    REPT["REPT<br/>Repeats text a set number of times"]
    TEXTSPLIT["TEXTSPLIT<br/>Splits text into rows and columns using delimiters"]
    CHAR["CHAR<br/>Returns the character for a code number"]
    IF["IF<br/>Returns one value if a condition is TRUE, another if FALSE"]
    SUM["SUM<br/>Adds numbers"]
    AVERAGE["AVERAGE<br/>Returns the arithmetic mean of its numeric arguments"]
    IFERROR["IFERROR<br/>Returns a replacement value when a formula returns an error"]
    TEXT --> IF
    TEXT --> SUM
    TEXT --> AVERAGE
    TEXT -.-> IF
    TEXT -.-> IFERROR
    FIND --> IF
    FIND --> SUM
    FIND --> AVERAGE
    FIND -.-> IF
    FIND -.-> IFERROR
    BAHTTEXT --> IF
    BAHTTEXT --> SUM
    BAHTTEXT --> AVERAGE
    BAHTTEXT -.-> IF
    BAHTTEXT -.-> IFERROR
    TEXTAFTER --> IF
    TEXTAFTER --> SUM
    TEXTAFTER --> AVERAGE
    TEXTAFTER -.-> IF
    TEXTAFTER -.-> IFERROR
    LOWER --> IF
    LOWER --> SUM
    LOWER --> AVERAGE
    LOWER -.-> IF
    LOWER -.-> IFERROR
    SEARCH --> IF
    SEARCH --> SUM
    SEARCH --> AVERAGE
    SEARCH -.-> IF
    SEARCH -.-> IFERROR
    TEXTJOIN --> IF
    TEXTJOIN --> SUM
    TEXTJOIN --> AVERAGE
    TEXTJOIN -.-> IF
    TEXTJOIN -.-> IFERROR
    SPLIT --> IF
    SPLIT --> SUM
    SPLIT --> AVERAGE
    SPLIT -.-> IF
    SPLIT -.-> IFERROR
    DOLLAR --> IF
    DOLLAR --> SUM
    DOLLAR --> AVERAGE
    DOLLAR -.-> IF
    DOLLAR -.-> IFERROR
    EXACT --> IF
    EXACT --> SUM
    EXACT --> AVERAGE
    EXACT -.-> IF
    EXACT -.-> IFERROR
    PROPER --> IF
    PROPER --> SUM
    PROPER --> AVERAGE
    PROPER -.-> IF
    PROPER -.-> IFERROR
    REGEXMATCH --> IF
    REGEXMATCH --> SUM
    REGEXMATCH --> AVERAGE
    REGEXMATCH -.-> IF
    REGEXMATCH -.-> IFERROR
    REPLACE --> IF
    REPLACE --> SUM
    REPLACE --> AVERAGE
    REPLACE -.-> IF
    REPLACE -.-> IFERROR
    T --> IF
    T --> SUM
    T --> AVERAGE
    T -.-> IF
    T -.-> IFERROR
    TEXTBEFORE --> IF
    TEXTBEFORE --> SUM
    TEXTBEFORE --> AVERAGE
    TEXTBEFORE -.-> IF
    TEXTBEFORE -.-> IFERROR
    VALUE --> IF
    VALUE --> SUM
    VALUE --> AVERAGE
    VALUE -.-> IF
    VALUE -.-> IFERROR
    NUMBERVALUE --> IF
    NUMBERVALUE --> SUM
    NUMBERVALUE --> AVERAGE
    NUMBERVALUE -.-> IF
    NUMBERVALUE -.-> IFERROR
    JIS --> IF
    JIS --> SUM
    JIS --> AVERAGE
    JIS -.-> IF
    JIS -.-> IFERROR
    MID --> IF
    MID --> SUM
    MID --> AVERAGE
    MID -.-> IF
    MID -.-> IFERROR
    ASC --> IF
    ASC --> SUM
    ASC --> AVERAGE
    ASC -.-> IF
    ASC -.-> IFERROR
    PHONETIC --> IF
    PHONETIC --> SUM
    PHONETIC --> AVERAGE
    PHONETIC -.-> IF
    PHONETIC -.-> IFERROR
    CLEAN --> IF
    CLEAN --> SUM
    CLEAN --> AVERAGE
    CLEAN -.-> IF
    CLEAN -.-> IFERROR
    REGEXEXTRACT --> IF
    REGEXEXTRACT --> SUM
    REGEXEXTRACT --> AVERAGE
    REGEXEXTRACT -.-> IF
    REGEXEXTRACT -.-> IFERROR
    LEFT --> IF
    LEFT --> LEN
    LEFT --> FIND
    LEFT -.-> RIGHT
    LEFT -.-> MID
    CONCAT --> IF
    CONCAT --> SUM
    CONCAT --> AVERAGE
    CONCAT -.-> IF
    CONCAT -.-> IFERROR
    UNICODE --> IF
    UNICODE --> SUM
    UNICODE --> AVERAGE
    UNICODE -.-> IF
    UNICODE -.-> IFERROR
    SUBSTITUTE --> IF
    SUBSTITUTE --> SUM
    SUBSTITUTE --> AVERAGE
    SUBSTITUTE -.-> IF
    SUBSTITUTE -.-> IFERROR
    REGEXREPLACE --> IF
    REGEXREPLACE --> SUM
    REGEXREPLACE --> AVERAGE
    REGEXREPLACE -.-> IF
    REGEXREPLACE -.-> IFERROR
    UNICHAR --> IF
    UNICHAR --> SUM
    UNICHAR --> AVERAGE
    UNICHAR -.-> IF
    UNICHAR -.-> IFERROR
    CONCATENATE --> IF
    CONCATENATE --> LEFT
    CONCATENATE --> RIGHT
    CONCATENATE -.-> CONCAT
    CONCATENATE -.-> TEXTJOIN
    RIGHT --> IF
    RIGHT --> LEN
    RIGHT --> FIND
    RIGHT -.-> LEFT
    RIGHT -.-> MID
    CODE --> IF
    CODE --> SUM
    CODE --> AVERAGE
    CODE -.-> IF
    CODE -.-> IFERROR
    JOIN --> IF
    JOIN --> SUM
    JOIN --> AVERAGE
    JOIN -.-> IF
    JOIN -.-> IFERROR
    TRIM --> IF
    TRIM --> SUM
    TRIM --> AVERAGE
    TRIM -.-> IF
    TRIM -.-> IFERROR
    UPPER --> IF
    UPPER --> SUM
    UPPER --> AVERAGE
    UPPER -.-> IF
    UPPER -.-> IFERROR
    FIXED --> IF
    FIXED --> SUM
    FIXED --> AVERAGE
    FIXED -.-> IF
    FIXED -.-> IFERROR
    LEN --> IF
    LEN --> LEFT
    LEN --> RIGHT
    LEN -.-> LEFT
    LEN -.-> RIGHT
    REPT --> IF
    REPT --> SUM
    REPT --> AVERAGE
    REPT -.-> IF
    REPT -.-> IFERROR
    TEXTSPLIT --> IF
    TEXTSPLIT --> SUM
    TEXTSPLIT --> AVERAGE
    TEXTSPLIT -.-> IF
    TEXTSPLIT -.-> IFERROR
    CHAR --> IF
    CHAR --> SUM
    CHAR --> AVERAGE
    CHAR -.-> IF
    CHAR -.-> IFERROR
    class TEXT,FIND,BAHTTEXT,TEXTAFTER,LOWER,SEARCH,TEXTJOIN,SPLIT,DOLLAR,EXACT,PROPER,REGEXMATCH,REPLACE,T,TEXTBEFORE,VALUE,NUMBERVALUE,JIS,MID,ASC,PHONETIC,CLEAN,REGEXEXTRACT,LEFT,CONCAT,UNICODE,SUBSTITUTE,REGEXREPLACE,UNICHAR,CONCATENATE,RIGHT,CODE,JOIN,TRIM,UPPER,FIXED,LEN,REPT,TEXTSPLIT,CHAR Text
    class IF,SUM,AVERAGE,IFERROR external
```

## Legend

- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in This Category: 54
