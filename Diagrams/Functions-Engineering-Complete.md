---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Engineering
purpose:
  - Function Relationships
use-case:
  - Converting Number Systems
  - Working With Complex Numbers
related:
  - BESSELJ
  - BESSELY
  - BIN2DEC
  - BIN2HEX
  - BIN2OCT
  - BITAND
  - BITLSHIFT
  - BITOR
  - BITRSHIFT
  - BITXOR
  - COMPLEX
  - DEC2BIN
  - DEC2HEX
  - DEC2OCT
  - ERF
  - ERFC
  - HEX2BIN
  - HEX2DEC
  - HEX2OCT
  - IMABS
  - IMAGINARY
  - IMPRODUCT
  - IMREAL
  - IMSUM
  - OCT2BIN
  - OCT2DEC
  - OCT2HEX
level: 3
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - complex-numbers
  - engineering
  - number-conversion
---

# Engineering Functions

```mermaid

graph LR
    Engineering["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Engineering</b><br/>────────────────<br/>Engineering and technical calculations<br/><b>Total Functions:</b> 57</div>"]
    Engineering --> Bitwise["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Bitwise Operations</b><br/>────────────────<br/>Bitwise logical operations<br/><b>Functions:</b> 5</div>"]
    Engineering --> ComplexNumbers["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Complex Numbers</b><br/>────────────────<br/>Complex number calculations<br/><b>Functions:</b> 29</div>"]
    Engineering --> EngineeringCalc["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Engineering Calculations</b><br/>────────────────<br/>Specialized engineering functions<br/><b>Functions:</b> 11</div>"]
    Engineering --> NumberConversion["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Number Conversion</b><br/>────────────────<br/>Number base conversions<br/><b>Functions:</b> 12</div>"]
    %% Bitwise Operations (5 functions), showing all functions
    Bitwise --> BITAND["<div align='left' style='font-family: MonoLisa, monospace;'><b>BITAND</b><br/>────────────────<br/>Returns the bitwise AND of two numbers</div>"]
    BITAND --> BITANDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BITAND(number1, number2)</div>"]
    BITAND --> BITANDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BITAND(5, 3) → 1</div>"]
    Bitwise --> BITLSHIFT["<div align='left' style='font-family: MonoLisa, monospace;'><b>BITLSHIFT</b><br/>────────────────<br/>Shifts a number left by a specified number of bits</div>"]
    BITLSHIFT --> BITLSHIFTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BITLSHIFT(number, shift_amount)</div>"]
    BITLSHIFT --> BITLSHIFTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BITLSHIFT(5, 2) → 20</div>"]
    Bitwise --> BITOR["<div align='left' style='font-family: MonoLisa, monospace;'><b>BITOR</b><br/>────────────────<br/>Returns the bitwise OR of two numbers</div>"]
    BITOR --> BITORSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BITOR(number1, number2)</div>"]
    BITOR --> BITOREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BITOR(5, 3) → 7</div>"]
    Bitwise --> BITRSHIFT["<div align='left' style='font-family: MonoLisa, monospace;'><b>BITRSHIFT</b><br/>────────────────<br/>Shifts a number right by a specified number of bits</div>"]
    BITRSHIFT --> BITRSHIFTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BITRSHIFT(number, shift_amount)</div>"]
    BITRSHIFT --> BITRSHIFTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BITRSHIFT(20, 2) → 5</div>"]
    Bitwise --> BITXOR["<div align='left' style='font-family: MonoLisa, monospace;'><b>BITXOR</b><br/>────────────────<br/>Returns the bitwise XOR of two numbers</div>"]
    BITXOR --> BITXORSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BITXOR(number1, number2)</div>"]
    BITXOR --> BITXOREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BITXOR(5, 3) → 6</div>"]
    %% Complex Numbers (29 functions), showing key functions
    ComplexNumbers --> COMPLEX["<div align='left' style='font-family: MonoLisa, monospace;'><b>COMPLEX</b><br/>────────────────<br/>Converts real and imaginary coefficients into a complex number</div>"]
    COMPLEX --> COMPLEXSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>COMPLEX(real_num, i_num, [suffix])</div>"]
    COMPLEX --> COMPLEXEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=COMPLEX(3, 4) → &quot;3+4i&quot;</div>"]
    ComplexNumbers --> IMABS["<div align='left' style='font-family: MonoLisa, monospace;'><b>IMABS</b><br/>────────────────<br/>Returns the absolute value (modulus) of a complex number</div>"]
    IMABS --> IMABSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMABS(inumber)</div>"]
    IMABS --> IMABSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMABS(&quot;3+4i&quot;) → 5</div>"]
    ComplexNumbers --> IMAGINARY["<div align='left' style='font-family: MonoLisa, monospace;'><b>IMAGINARY</b><br/>────────────────<br/>Returns the imaginary coefficient of a complex number</div>"]
    IMAGINARY --> IMAGINARYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMAGINARY(inumber)</div>"]
    IMAGINARY --> IMAGINARYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMAGINARY(&quot;3+4i&quot;) → 4</div>"]
    ComplexNumbers --> IMREAL["<div align='left' style='font-family: MonoLisa, monospace;'><b>IMREAL</b><br/>────────────────<br/>Returns the real coefficient of a complex number</div>"]
    IMREAL --> IMREALSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMREAL(inumber)</div>"]
    IMREAL --> IMREALEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMREAL(&quot;3+4i&quot;) → 3</div>"]
    ComplexNumbers --> IMSUM["<div align='left' style='font-family: MonoLisa, monospace;'><b>IMSUM</b><br/>────────────────<br/>Returns the sum of complex numbers</div>"]
    IMSUM --> IMSUMSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMSUM(inumber1, [inumber2], ...)</div>"]
    IMSUM --> IMSUMEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMSUM(&quot;3+4i&quot;, &quot;5-3i&quot;) → &quot;8+i&quot;</div>"]
    ComplexNumbers --> IMPRODUCT["<div align='left' style='font-family: MonoLisa, monospace;'><b>IMPRODUCT</b><br/>────────────────<br/>Returns the product of complex numbers</div>"]
    IMPRODUCT --> IMPRODUCTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMPRODUCT(inumber1, [inumber2], ...)</div>"]
    IMPRODUCT --> IMPRODUCTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMPRODUCT(&quot;3+4i&quot;, &quot;5-3i&quot;) → &quot;27+11i&quot;</div>"]
    %% Engineering Calculations (11 functions), showing key functions
    EngineeringCalc --> BESSELJ["<div align='left' style='font-family: MonoLisa, monospace;'><b>BESSELJ</b><br/>────────────────<br/>Returns the Bessel function Jn(x)</div>"]
    BESSELJ --> BESSELJSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BESSELJ(x, n)</div>"]
    BESSELJ --> BESSELJEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BESSELJ(1.9, 2) → 0.329</div>"]
    EngineeringCalc --> BESSELY["<div align='left' style='font-family: MonoLisa, monospace;'><b>BESSELY</b><br/>────────────────<br/>Returns the Bessel function Yn(x)</div>"]
    BESSELY --> BESSELYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BESSELY(x, n)</div>"]
    BESSELY --> BESSELYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BESSELY(2.5, 1) → 0.146</div>"]
    EngineeringCalc --> ERF["<div align='left' style='font-family: MonoLisa, monospace;'><b>ERF</b><br/>────────────────<br/>Returns the error function integrated between two limits</div>"]
    ERF --> ERFSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ERF(lower_limit, [upper_limit])</div>"]
    ERF --> ERFEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ERF(0.745) → 0.70793</div>"]
    EngineeringCalc --> ERFC["<div align='left' style='font-family: MonoLisa, monospace;'><b>ERFC</b><br/>────────────────<br/>Returns the complementary error function</div>"]
    ERFC --> ERFCSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ERFC(x)</div>"]
    ERFC --> ERFCEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ERFC(0.5) → 0.4795</div>"]
    %% Number Conversion (12 functions), showing all functions
    NumberConversion --> BIN2DEC["<div align='left' style='font-family: MonoLisa, monospace;'><b>BIN2DEC</b><br/>────────────────<br/>Converts a binary number to decimal</div>"]
    BIN2DEC --> BIN2DECSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BIN2DEC(number)</div>"]
    BIN2DEC --> BIN2DECEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BIN2DEC(&quot;1010&quot;) → 10</div>"]
    NumberConversion --> BIN2HEX["<div align='left' style='font-family: MonoLisa, monospace;'><b>BIN2HEX</b><br/>────────────────<br/>Converts a binary number to hexadecimal</div>"]
    BIN2HEX --> BIN2HEXSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BIN2HEX(number, [places])</div>"]
    BIN2HEX --> BIN2HEXEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BIN2HEX(&quot;1010&quot;) → &quot;A&quot;</div>"]
    NumberConversion --> BIN2OCT["<div align='left' style='font-family: MonoLisa, monospace;'><b>BIN2OCT</b><br/>────────────────<br/>Converts a binary number to octal</div>"]
    BIN2OCT --> BIN2OCTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BIN2OCT(number, [places])</div>"]
    BIN2OCT --> BIN2OCTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BIN2OCT(&quot;1010&quot;) → &quot;12&quot;</div>"]
    NumberConversion --> DEC2BIN["<div align='left' style='font-family: MonoLisa, monospace;'><b>DEC2BIN</b><br/>────────────────<br/>Converts a decimal number to binary</div>"]
    DEC2BIN --> DEC2BINSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DEC2BIN(number, [places])</div>"]
    DEC2BIN --> DEC2BINEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DEC2BIN(10) → &quot;1010&quot;</div>"]
    NumberConversion --> DEC2HEX["<div align='left' style='font-family: MonoLisa, monospace;'><b>DEC2HEX</b><br/>────────────────<br/>Converts a decimal number to hexadecimal</div>"]
    DEC2HEX --> DEC2HEXSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DEC2HEX(number, [places])</div>"]
    DEC2HEX --> DEC2HEXEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DEC2HEX(10) → &quot;A&quot;</div>"]
    NumberConversion --> DEC2OCT["<div align='left' style='font-family: MonoLisa, monospace;'><b>DEC2OCT</b><br/>────────────────<br/>Converts a decimal number to octal</div>"]
    DEC2OCT --> DEC2OCTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DEC2OCT(number, [places])</div>"]
    DEC2OCT --> DEC2OCTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DEC2OCT(10) → &quot;12&quot;</div>"]
    NumberConversion --> HEX2BIN["<div align='left' style='font-family: MonoLisa, monospace;'><b>HEX2BIN</b><br/>────────────────<br/>Converts a hexadecimal number to binary</div>"]
    HEX2BIN --> HEX2BINSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HEX2BIN(number, [places])</div>"]
    HEX2BIN --> HEX2BINEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HEX2BIN(&quot;A&quot;) → &quot;1010&quot;</div>"]
    NumberConversion --> HEX2DEC["<div align='left' style='font-family: MonoLisa, monospace;'><b>HEX2DEC</b><br/>────────────────<br/>Converts a hexadecimal number to decimal</div>"]
    HEX2DEC --> HEX2DECSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HEX2DEC(number)</div>"]
    HEX2DEC --> HEX2DECEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HEX2DEC(&quot;A&quot;) → 10</div>"]
    NumberConversion --> HEX2OCT["<div align='left' style='font-family: MonoLisa, monospace;'><b>HEX2OCT</b><br/>────────────────<br/>Converts a hexadecimal number to octal</div>"]
    HEX2OCT --> HEX2OCTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HEX2OCT(number, [places])</div>"]
    HEX2OCT --> HEX2OCTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HEX2OCT(&quot;A&quot;) → &quot;12&quot;</div>"]
    NumberConversion --> OCT2BIN["<div align='left' style='font-family: MonoLisa, monospace;'><b>OCT2BIN</b><br/>────────────────<br/>Converts an octal number to binary</div>"]
    OCT2BIN --> OCT2BINSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>OCT2BIN(number, [places])</div>"]
    OCT2BIN --> OCT2BINEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=OCT2BIN(&quot;12&quot;) → &quot;1010&quot;</div>"]
    NumberConversion --> OCT2DEC["<div align='left' style='font-family: MonoLisa, monospace;'><b>OCT2DEC</b><br/>────────────────<br/>Converts an octal number to decimal</div>"]
    OCT2DEC --> OCT2DECSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>OCT2DEC(number)</div>"]
    OCT2DEC --> OCT2DECEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=OCT2DEC(&quot;12&quot;) → 10</div>"]
    NumberConversion --> OCT2HEX["<div align='left' style='font-family: MonoLisa, monospace;'><b>OCT2HEX</b><br/>────────────────<br/>Converts an octal number to hexadecimal</div>"]
    OCT2HEX --> OCT2HEXSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>OCT2HEX(number, [places])</div>"]
    OCT2HEX --> OCT2HEXEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=OCT2HEX(&quot;12&quot;) → &quot;A&quot;</div>"]

    style Engineering fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Bitwise fill:#F0FFFF,stroke:#333,stroke-width:2px
    style ComplexNumbers fill:#F0FFFF,stroke:#333,stroke-width:2px
    style EngineeringCalc fill:#F0FFFF,stroke:#333,stroke-width:2px
    style NumberConversion fill:#F0FFFF,stroke:#333,stroke-width:2px
    style BITAND fill:#F0FFF0,stroke:#333,stroke-width:2px
    style BITANDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BITANDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BITLSHIFT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style BITLSHIFTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BITLSHIFTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BITOR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style BITORSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BITOREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BITRSHIFT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style BITRSHIFTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BITRSHIFTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BITXOR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style BITXORSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BITXOREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style COMPLEX fill:#F0FFF0,stroke:#333,stroke-width:2px
    style COMPLEXSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style COMPLEXEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IMABS fill:#B9E9EB,stroke:#333,stroke-width:2px
    style IMABSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IMABSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IMAGINARY fill:#F0FFF0,stroke:#333,stroke-width:2px
    style IMAGINARYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IMAGINARYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IMREAL fill:#B9E9EB,stroke:#333,stroke-width:2px
    style IMREALSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IMREALEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IMSUM fill:#F0FFF0,stroke:#333,stroke-width:2px
    style IMSUMSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IMSUMEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IMPRODUCT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style IMPRODUCTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IMPRODUCTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BESSELJ fill:#F0FFF0,stroke:#333,stroke-width:2px
    style BESSELJSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BESSELJEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BESSELY fill:#B9E9EB,stroke:#333,stroke-width:2px
    style BESSELYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BESSELYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ERF fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ERFSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ERFEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ERFC fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ERFCSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ERFCEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BIN2DEC fill:#F0FFF0,stroke:#333,stroke-width:2px
    style BIN2DECSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BIN2DECEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BIN2HEX fill:#B9E9EB,stroke:#333,stroke-width:2px
    style BIN2HEXSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BIN2HEXEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BIN2OCT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style BIN2OCTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BIN2OCTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DEC2BIN fill:#B9E9EB,stroke:#333,stroke-width:2px
    style DEC2BINSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DEC2BINEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DEC2HEX fill:#F0FFF0,stroke:#333,stroke-width:2px
    style DEC2HEXSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DEC2HEXEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DEC2OCT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style DEC2OCTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DEC2OCTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HEX2BIN fill:#F0FFF0,stroke:#333,stroke-width:2px
    style HEX2BINSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HEX2BINEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HEX2DEC fill:#B9E9EB,stroke:#333,stroke-width:2px
    style HEX2DECSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HEX2DECEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HEX2OCT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style HEX2OCTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HEX2OCTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style OCT2BIN fill:#B9E9EB,stroke:#333,stroke-width:2px
    style OCT2BINSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style OCT2BINEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style OCT2DEC fill:#F0FFF0,stroke:#333,stroke-width:2px
    style OCT2DECSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style OCT2DECEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style OCT2HEX fill:#B9E9EB,stroke:#333,stroke-width:2px
    style OCT2HEXSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style OCT2HEXEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
```
