---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- diagrams
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- diagrams
- excel
- sheets
---
# Spreadsheets-Functions-Mathematics and Trigonometry

```mermaid

graph LR
    MathTrig["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Math & Trig</b><br/>────────────────<br/>Mathematical and trigonometric functions<br/><b>Total Functions:</b> 71</div>"]
    
    MathTrig --> BasicArith["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Basic Arithmetic</b><br/>────────────────<br/>Fundamental math operations<br/><b>Functions:</b> 18</div>"]
    
    %% Basic Arithmetic (18 functions)
    %% ABS - Function 1
    BasicArith --> ABS["<div align='left' style='font-family: MonoLisa, monospace;'><b>ABS</b><br/>────────────────<br/>Returns the absolute value of a number</div>"]
    ABS --> ABSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ABS(number)</div>"]
    ABS --> ABSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ABS(-5) → 5</div>"]
    
    %% CEILING.MATH - Function 2
    BasicArith --> CEILINGMATH["<div align='left' style='font-family: MonoLisa, monospace;'><b>CEILING.MATH</b><br/>────────────────<br/>Rounds a number up with customizable mode</div>"]
    CEILINGMATH --> CEILINGMATHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CEILING.MATH(number, [significance], [mode])</div>"]
    CEILINGMATH --> CEILINGMATHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CEILING.MATH(2.3, 1) → 3</div>"]
    
    %% CEILING - Function 3
    BasicArith --> CEILING["<div align='left' style='font-family: MonoLisa, monospace;'><b>CEILING</b><br/>────────────────<br/>Rounds a number up to the nearest multiple</div>"]
    CEILING --> CEILINGSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CEILING(number, [significance])</div>"]
    CEILING --> CEILINGEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CEILING(2.3, 1) → 3</div>"]
    
    %% FLOOR.MATH - Function 4
    BasicArith --> FLOORMATH["<div align='left' style='font-family: MonoLisa, monospace;'><b>FLOOR.MATH</b><br/>────────────────<br/>Rounds a number down with customizable mode</div>"]
    FLOORMATH --> FLOORMATHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FLOOR.MATH(number, [significance], [mode])</div>"]
    FLOORMATH --> FLOORMATHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FLOOR.MATH(2.7, 1) → 2</div>"]
    
    %% FLOOR - Function 5
    BasicArith --> FLOOR["<div align='left' style='font-family: MonoLisa, monospace;'><b>FLOOR</b><br/>────────────────<br/>Rounds a number down to the nearest multiple</div>"]
    FLOOR --> FLOORSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FLOOR(number, [significance])</div>"]
    FLOOR --> FLOOREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FLOOR(2.7, 1) → 2</div>"]
    
    %% INT - Function 6
    BasicArith --> INT["<div align='left' style='font-family: MonoLisa, monospace;'><b>INT</b><br/>────────────────<br/>Rounds a number down to the nearest integer</div>"]
    INT --> INTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>INT(number)</div>"]
    INT --> INTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=INT(3.7) → 3</div>"]
    
    %% MOD - Function 7
    BasicArith --> MOD["<div align='left' style='font-family: MonoLisa, monospace;'><b>MOD</b><br/>────────────────<br/>Returns the remainder after division</div>"]
    MOD --> MODSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MOD(number, divisor)</div>"]
    MOD --> MODEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MOD(10, 3) → 1</div>"]
    
    %% PRODUCT - Function 8
    BasicArith --> PRODUCT["<div align='left' style='font-family: MonoLisa, monospace;'><b>PRODUCT</b><br/>────────────────<br/>Multiplies a range of numbers</div>"]
    PRODUCT --> PRODUCTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>PRODUCT(value1, [value2, …])</div>"]
    PRODUCT --> PRODUCTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=PRODUCT(A1:A3) → 24</div>"]
    
    %% QUOTIENT - Function 9
    BasicArith --> QUOTIENT["<div align='left' style='font-family: MonoLisa, monospace;'><b>QUOTIENT</b><br/>────────────────<br/>Returns the integer portion of a division</div>"]
    QUOTIENT --> QUOTIENTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>QUOTIENT(numerator, denominator)</div>"]
    QUOTIENT --> QUOTIENTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=QUOTIENT(10, 3) → 3</div>"]
    
    %% ROUND - Function 10
    BasicArith --> ROUND["<div align='left' style='font-family: MonoLisa, monospace;'><b>ROUND</b><br/>────────────────<br/>Rounds a number to a specified number of digits</div>"]
    ROUND --> ROUNDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ROUND(number, [num_digits])</div>"]
    ROUND --> ROUNDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ROUND(2.345, 2) → 2.35</div>"]
    
    %% ROUNDDOWN - Function 11
    BasicArith --> ROUNDDOWN["<div align='left' style='font-family: MonoLisa, monospace;'><b>ROUNDDOWN</b><br/>────────────────<br/>Rounds a number down to a specified number of digits</div>"]
    ROUNDDOWN --> ROUNDDOWNSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ROUNDDOWN(number, [num_digits])</div>"]
    ROUNDDOWN --> ROUNDDOWNEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ROUNDDOWN(2.345, 2) → 2.34</div>"]
    
    %% ROUNDUP - Function 12
    BasicArith --> ROUNDUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>ROUNDUP</b><br/>────────────────<br/>Rounds a number up to a specified number of digits</div>"]
    ROUNDUP --> ROUNDUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ROUNDUP(number, [num_digits])</div>"]
    ROUNDUP --> ROUNDUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ROUNDUP(2.345, 2) → 2.35</div>"]
    
    %% SIGN - Function 13
    BasicArith --> SIGN["<div align='left' style='font-family: MonoLisa, monospace;'><b>SIGN</b><br/>────────────────<br/>Returns the sign of a number (1, 0, -1)</div>"]
    SIGN --> SIGNSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SIGN(number)</div>"]
    SIGN --> SIGNEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SIGN(-5) → -1</div>"]
    
    %% SUM - Function 14
    BasicArith --> SUM["<div align='left' style='font-family: MonoLisa, monospace;'><b>SUM</b><br/>────────────────<br/>Adds a range of numbers</div>"]
    SUM --> SUMSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SUM(value1, [value2, …])</div>"]
    SUM --> SUMEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SUM(A1:A5) → 50</div>"]
    
    %% SUMIF - Function 15
    BasicArith --> SUMIF["<div align='left' style='font-family: MonoLisa, monospace;'><b>SUMIF</b><br/>────────────────<br/>Adds numbers meeting a criterion</div>"]
    SUMIF --> SUMIFSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SUMIF(range, criterion, [sum_range])</div>"]
    SUMIF --> SUMIFEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SUMIF(A1:A5, &quot;&gt;10&quot;) → 25</div>"]
    
    %% SUMIFS - Function 16
    BasicArith --> SUMIFS["<div align='left' style='font-family: MonoLisa, monospace;'><b>SUMIFS</b><br/>────────────────<br/>Adds numbers meeting multiple criteria</div>"]
    SUMIFS --> SUMIFSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SUMIFS(sum_range, criteria_range1, criterion1, [criteria_range2, criterion2, …])</div>"]
    SUMIFS --> SUMIFSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SUMIFS(B1:B5, A1:A5, &quot;&gt;5&quot;, C1:C5, &quot;Yes&quot;) → 30</div>"]
    
    %% SUMPRODUCT - Function 17
    BasicArith --> SUMPRODUCT["<div align='left' style='font-family: MonoLisa, monospace;'><b>SUMPRODUCT</b><br/>────────────────<br/>Multiplies corresponding arrays and sums the products</div>"]
    SUMPRODUCT --> SUMPRODUCTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SUMPRODUCT(array1, [array2, …])</div>"]
    SUMPRODUCT --> SUMPRODUCTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SUMPRODUCT(A1:A3, B1:B3) → 32</div>"]
    
    %% SUMSQ - Function 18
    BasicArith --> SUMSQ["<div align='left' style='font-family: MonoLisa, monospace;'><b>SUMSQ</b><br/>────────────────<br/>Sums the squares of numbers</div>"]
    SUMSQ --> SUMSQSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SUMSQ(value1, [value2, …])</div>"]
    SUMSQ --> SUMSQEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SUMSQ(A1:A3) → 14</div>"]
    
    %% Styling
    style MathTrig fill:#F0FFFF,stroke:#333,stroke-width:2px
    style BasicArith fill:#F0FFFF,stroke:#333,stroke-width:2px
    %% Functions alternate colors
    style ABS fill:#F0FFF0,stroke:#333,stroke-width:2px
    style CEILINGMATH fill:#B9E9EB,stroke:#333,stroke-width:2px
    style CEILING fill:#F0FFF0,stroke:#333,stroke-width:2px
    style FLOORMATH fill:#B9E9EB,stroke:#333,stroke-width:2px
    style FLOOR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style INT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style MOD fill:#F0FFF0,stroke:#333,stroke-width:2px
    style PRODUCT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style QUOTIENT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ROUND fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ROUNDDOWN fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ROUNDUP fill:#B9E9EB,stroke:#333,stroke-width:2px
    style SIGN fill:#F0FFF0,stroke:#333,stroke-width:2px
    style SUM fill:#B9E9EB,stroke:#333,stroke-width:2px
    style SUMIF fill:#F0FFF0,stroke:#333,stroke-width:2px
    style SUMIFS fill:#B9E9EB,stroke:#333,stroke-width:2px
    style SUMPRODUCT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style SUMSQ fill:#B9E9EB,stroke:#333,stroke-width:2px
    %% All syntax nodes - pink
    style ABSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CEILINGMATHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CEILINGSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FLOORMATHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FLOORSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style INTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MODSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style PRODUCTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style QUOTIENTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ROUNDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ROUNDDOWNSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ROUNDUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SIGNSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SUMSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SUMIFSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SUMIFSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SUMPRODUCTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SUMSQSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    %% All example nodes - lavender
    style ABSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CEILINGMATHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CEILINGEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FLOORMATHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FLOOREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style INTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MODEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style PRODUCTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style QUOTIENTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ROUNDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ROUNDDOWNEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ROUNDUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SIGNEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SUMEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SUMIFEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SUMIFSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SUMPRODUCTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SUMSQEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
    
```