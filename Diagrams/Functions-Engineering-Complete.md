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
# Spreadsheets-Functions-Engineering-Complete

```mermaid

graph LR
    Engineering["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Engineering</b><br/>────────────────<br/>Engineering and technical calculations<br/><b>Total Functions:</b> 54</div>"]
    
    Engineering --> Bitwise["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Bitwise Operations</b><br/>────────────────<br/>Bitwise logical operations<br/><b>Functions:</b> 5</div>"]
    
    Engineering --> ComplexNumbers["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Complex Numbers</b><br/>────────────────<br/>Complex number calculations<br/><b>Functions:</b> 26</div>"]
    
    Engineering --> EngineeringCalc["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Engineering Calculations</b><br/>────────────────<br/>Specialized engineering functions<br/><b>Functions:</b> 11</div>"]
    
    Engineering --> NumberConversion["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Number Conversion</b><br/>────────────────<br/>Number base conversions<br/><b>Functions:</b> 12</div>"]
    
    %% Bitwise Operations (5 functions)
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
    
    %% Complex Numbers (26 functions) - showing key functions
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
    IMSUM --> IMSUMEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMSUM(&quot;3+4i&quot;, &quot;5-3i&quot;) → &quot;8+1i&quot;</div>"]
    
    ComplexNumbers --> IMPRODUCT["<div align='left' style='font-family: MonoLisa, monospace;'><b>IMPRODUCT</b><br/>────────────────<br/>Returns the product of complex numbers</div>"]
    IMPRODUCT --> IMPRODUCTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMPRODUCT(inumber1, [inumber2], ...)</div>"]
    IMPRODUCT --> IMPRODUCTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMPRODUCT(&quot;3+4i&quot;, &quot;5-3i&quot;) → &quot;27+11i&quot;</div>"]
    
    %% Engineering Calculations (11 functions) - showing key functions
    EngineeringCalc --> BESSELJ["<div align='left' style='font-family: MonoLisa, monospace;'><b>BESSELJ</b><br/>────────────────<br/>Returns the Bessel function Jn(x)</div>"]
    BESSELJ --> BESSELJSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BESSELJ(x, n)</div>"]
    BESSELJ --> BESSELJEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BESSELJ(1.9, 2) → 0.329</div>"]
    
    EngineeringCalc --> BESSELY["<div align='left' style='font-family: MonoLisa, monospace;'><b>BESSELY</b><br/>────────────────<br/>Returns the Bessel function Yn(x)</div>"]
    BESSELY --> BESSELYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BESSELY(x, n)</div>"]
    BESSELY --> BESSELYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BESSELY(2.5, 1) → 0.146</div>"]
    
    EngineeringCalc --> ERF["<div align='left' style='font-family: MonoLisa, monospace;'><b>ERF</b><br/>────────────────<br/>Returns the error function</div>"]
    ERF --> ERFSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ERF(lower_limit, [upper_limit])</div>"]
    ERF --> ERFEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ERF(0.74500) → 0.70793</div>"]
    
    EngineeringCalc --> ERFC["<div align='left' style='font-family: MonoLisa, monospace;'><b>ERFC</b><br/>────────────────<br/>Returns the complementary error function</div>"]
    ERFC --> ERFCSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ERFC(x)</div>"]
    ERFC --> ERFCEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>