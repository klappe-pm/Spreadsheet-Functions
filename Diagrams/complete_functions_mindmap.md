---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Overview
purpose:
  - Function Relationships
use-case:
  - Finding Related Functions
  - Browsing the Function Library
related:
  - ABS
  - ASIN
  - AVERAGE
  - BIN2DEC
  - BITAND
  - CEILING
  - CELL
  - CHAR
  - CHISQ.DIST
  - COMPLEX
  - CONCATENATE
  - DAVERAGE
  - DB
  - DEC2BIN
  - DEGREES
  - DGET
  - EXP
  - F.DIST
  - FILTER
  - HEX2DEC
  - HOUR
  - IF
  - IFERROR
  - IMPORTDATA
  - IMPORTRANGE
  - IMPOWER
  - IMREAL
  - IMSIN
  - IMSUM
  - ISBLANK
  - ISREF
  - MOD
  - NORM.DIST
  - NPV
  - PMT
  - SHEET
  - SORT
  - SUM
  - TODAY
  - XLOOKUP
level: 3
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
---

# Excel and Google Sheets Functions Mind Map

This mind map shows the Excel and Google Sheets functions in the library, grouped by category, with the functions that relate to each other. It does not show every function.

```mermaid
mindmap
  root((Excel & Google Sheets Functions))
    Statistical
      Basic Stats
        AVERAGE
          SUM
          COUNT
          MIN
          MAX
        MEDIAN
          PERCENTILE
          QUARTILE
        MODE
          FREQUENCY
      Advanced Stats
        STDEV
          VAR
          COVAR
        CORREL
          PEARSON
        REGRESSION
          LINEST
          LOGEST
          TREND
          GROWTH
      Distributions
        NORM.DIST
          NORM.INV
          NORM.S.DIST
          NORM.S.INV
        T.DIST
          T.INV
          T.TEST
        CHISQ.DIST
          CHISQ.INV
          CHISQ.TEST
        F.DIST
          F.INV
          F.TEST

    Math & Trig
      Basic Math
        SUM
          SUMIF
          SUMIFS
          SUMPRODUCT
        ABS
          SIGN
          INT
          ROUND
        MOD
          QUOTIENT
          GCD
          LCM
      Trigonometry
        SIN
          COS
          TAN
        ASIN
          ACOS
          ATAN
          ATAN2
        SINH
          COSH
          TANH
        DEGREES
          RADIANS
          PI
      Advanced Math
        EXP
          LN
          LOG
          LOG10
        POWER
          SQRT
          FACT
        RAND
          RANDBETWEEN
        CEILING
          FLOOR
          TRUNC

    Logical
      Core Logic
        IF
          AND
          OR
          NOT
        IFS
          SWITCH
        IFERROR
          IFNA
          ISERROR
          ISNA
      Testing Functions
        ISBLANK
          ISNUMBER
          ISTEXT
          ISLOGICAL
        ISERR
          ISEVEN
          ISODD
      Advanced Logic
        XOR
        LAMBDA
        FILTER

    Text
      Basic Text
        CONCATENATE
          CONCAT
          TEXTJOIN
        LEFT
          RIGHT
          MID
        LEN
          FIND
          SEARCH
        UPPER
          LOWER
          PROPER
      Text Manipulation
        SUBSTITUTE
          REPLACE
        TRIM
          CLEAN
          EXACT
        SPLIT
        VALUE
          TEXT
          DOLLAR
      Advanced Text
        CHAR
          CODE
          UNICODE
        REPT

    Lookup & Reference
      Basic Lookup
        VLOOKUP
          HLOOKUP
          XLOOKUP
        INDEX
          MATCH
          CHOOSE
        LOOKUP
      Advanced Lookup
        INDIRECT
          OFFSET
          ADDRESS
        HYPERLINK
        TRANSPOSE
        SORT
          SORTBY
          UNIQUE
        FILTER
          QUERY
      Array Functions
        SEQUENCE
        RANDARRAY

    Date & Time
      Basic Date
        TODAY
          NOW
          DATE
          TIME
        YEAR
          MONTH
          DAY
        HOUR
          MINUTE
          SECOND
      Date Calculations
        DATEDIF
          DAYS
        WORKDAY
          NETWORKDAYS
        EDATE
          EOMONTH
      Time Functions
        TIMEVALUE
          DATEVALUE
        WEEKDAY
          WEEKNUM
          YEARFRAC

    Financial
      Loan Calculations
        PMT
          PV
          FV
          NPER
          RATE
        IPMT
          PPMT
        CUMIPMT
          CUMPRINC
      Investment Analysis
        NPV
          IRR
          XIRR
          MIRR
        DB
          DDB
          SLN
          SYD
      Securities
        PRICE
          YIELD
          ACCRINT
        DURATION
          MDURATION

    Engineering
      Number Systems
        DEC2BIN
          DEC2OCT
          DEC2HEX
        BIN2DEC
          BIN2OCT
          BIN2HEX
        OCT2DEC
          OCT2BIN
          OCT2HEX
        HEX2DEC
          HEX2BIN
          HEX2OCT
      Complex Numbers
        COMPLEX
          IMABS
          IMARGUMENT
        IMREAL
          IMAGINARY
          IMCONJUGATE
        IMSUM
          IMSUB
          IMPRODUCT
          IMDIV
        IMPOWER
          IMSQRT
          IMEXP
          IMLN
          IMLOG10
          IMLOG2
        IMSIN
          IMCOS
          IMTAN
        IMSINH
          IMCOSH
          IMTANH
      Bitwise Operations
        BITAND
          BITOR
          BITXOR
        BITLSHIFT
          BITRSHIFT
      Engineering Functions
        BESSEL
          BESSELJ
          BESSELY
          BESSELI
          BESSELK
        ERF
          ERFC
        DELTA
          GESTEP
        CONVERT

    Database
      Database Functions
        DAVERAGE
          DCOUNT
          DCOUNTA
          DMAX
          DMIN
          DSUM
        DGET
          DPRODUCT
          DSTDEV
          DVAR

    Information
      Cell Information
        CELL
          INFO
          TYPE
        ISREF
          ISERROR
          ISLOGICAL
          ISNUMBER
          ISTEXT
        ISBLANK
          ISEVEN
          ISODD
        ISFORMULA
          ISNONTEXT
        N
          NA
          ERROR.TYPE
        SHEET
          SHEETS
          ROW
          ROWS
          COLUMN
          COLUMNS

    Web
      Web Functions
        WEBSERVICE
        IMPORTDATA
          IMPORTFEED
          IMPORTHTML
          IMPORTRANGE
          IMPORTXML

    Dynamic Array Functions
      Array Functions
        FILTER
          SORT
          SORTBY
          UNIQUE
        SEQUENCE
          RANDARRAY
        XLOOKUP
          XMATCH

    Excel Functions
      Core Excel Functions
        XLOOKUP
          XMATCH
        STOCKHISTORY
        FORMULATEXT
        AGGREGATE
        SUBTOTAL
      Web Access
        WEBSERVICE

    Google-Specific
      Google Functions
        ARRAYFORMULA
        QUERY
        IMPORTRANGE
          IMPORTHTML
          IMPORTXML
          IMPORTDATA
          IMPORTFEED
        GOOGLETRANSLATE
        GOOGLEFINANCE
        IMAGE
        SPARKLINE
        REGEXMATCH
          REGEXEXTRACT
          REGEXREPLACE
        SPLIT
        JOIN

    Cube
      OLAP Functions
        CUBEKPIMEMBER
        CUBEMEMBER
          CUBEMEMBERPROPERTY
        CUBESET
          CUBESETCOUNT
        CUBEVALUE
          CUBERANKEDMEMBER
```

## Mind Map Structure

### Top-Level Branches

The map has 15 top-level branches. Thirteen match library categories. Dynamic Array Functions and Excel Functions group functions across categories. The Add-in & Automation category is not shown.

1. **Statistical**: Data analysis and statistical calculations
2. **Math & Trig**: Mathematical and trigonometric operations
3. **Logical**: Decision making and conditional logic
4. **Text**: String manipulation and text processing
5. **Lookup & Reference**: Data retrieval and array operations
6. **Date & Time**: Temporal calculations and formatting
7. **Financial**: Business and financial modeling
8. **Engineering**: Technical and scientific calculations
9. **Database**: Data filtering and aggregation
10. **Information**: Cell and worksheet metadata
11. **Web**: Internet data import and web services
12. **Cube**: OLAP and multidimensional data analysis
13. **Google-Specific**: Google Sheets functions and their related functions
14. **Dynamic Array Functions**: Functions that return arrays spilling into neighboring cells
15. **Excel Functions**: Functions available in Excel, several of which also work in Google Sheets

### Key Relationships Shown

- **Hierarchical Structure**: Functions grouped by logical relationships
- **Cross-Category Connections**: How functions from different categories work together
- **Functional Families**: Related functions that build on each other
- **Platform Differences**: Excel and Google Sheets implementations

## Usage Notes

- **576 Total Functions** in the library, across 14 categories
- **Indentation levels** show function relationships and dependencies
- **Branching structure** illustrates how functions connect and relate to each other
