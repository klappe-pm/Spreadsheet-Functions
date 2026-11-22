---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Engineering
purpose:
  - Function Relationships
use-case:
  - Converting Number Systems
  - Working With Complex Numbers
  - Solving Engineering Problems
related:
  - AVERAGE
  - BESSELJ
  - BESSELK
  - BESSELY
  - BIN2DEC
  - BIN2OCT
  - BITAND
  - BITLSHIFT
  - BITOR
  - BITRSHIFT
  - BITXOR
  - COMPLEX
  - DEC2BIN
  - DEC2OCT
  - DELTA
  - ERF.PRECISE
  - ERFC.PRECISE
  - IF
  - IFERROR
  - IMABS
  - IMAGINARY
  - IMARGUMENT
  - IMCONJUGATE
  - IMCOS
  - IMCOSH
  - IMCSC
  - IMDIV
  - IMEXP
  - IMLN
  - IMLOG10
  - IMLOG2
  - IMPOWER
  - IMSECH
  - IMSINH
  - IMSQRT
  - IMSUM
  - IMTAN
  - OCT2BIN
  - OCT2DEC
  - SUM
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

# Engineering Functions Relationship Diagram

This diagram shows the relationships between functions in the Engineering category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Engineering fill:#FF9F43,stroke:#333,stroke-width:2px,color:#000
    DEC2BIN["DEC2BIN<br/>Converts a signed decimal number to binary"]
    IMLOG10["IMLOG10<br/>Returns the base-10 logarithm of a complex number"]
    BIN2DEC["BIN2DEC<br/>Converts a signed binary number to decimal"]
    OCT2DEC["OCT2DEC<br/>Converts a signed octal number to decimal"]
    BESSELK["BESSELK<br/>Returns the modified Bessel function Kn(x)"]
    BITOR["BITOR<br/>Returns the bitwise OR of two numbers"]
    BITAND["BITAND<br/>Returns the bitwise AND of two numbers"]
    IMCOS["IMCOS<br/>Returns the cosine of a complex number"]
    IMCONJUGATE["IMCONJUGATE<br/>Returns the complex conjugate of a complex number"]
    IMTAN["IMTAN<br/>Returns the tangent of a complex number"]
    DELTA["DELTA<br/>Tests whether two numeric values are equal"]
    OCT2BIN["OCT2BIN<br/>Converts a signed octal number to binary"]
    BESSELJ["BESSELJ<br/>Returns the Bessel function Jn(x)"]
    DEC2OCT["DEC2OCT<br/>Converts a signed decimal number to octal"]
    BITLSHIFT["BITLSHIFT<br/>Shifts a number left by a set number of bits"]
    IMABS["IMABS<br/>Returns the absolute value (modulus) of a complex number"]
    IMAGINARY["IMAGINARY<br/>Returns the imaginary coefficient of a complex number"]
    BIN2OCT["BIN2OCT<br/>Converts a signed binary number to octal"]
    COMPLEX["COMPLEX<br/>Converts real and imaginary coefficients into a complex number"]
    BITXOR["BITXOR<br/>Returns the bitwise XOR of two numbers"]
    BESSELY["BESSELY<br/>Returns the Bessel function Yn(x)"]
    IMCSC["IMCSC<br/>Returns the cosecant of a complex number"]
    BITRSHIFT["BITRSHIFT<br/>Shifts a number right by a set number of bits"]
    IMPOWER["IMPOWER<br/>Returns a complex number raised to an integer power"]
    IMLN["IMLN<br/>Returns the natural logarithm of a complex number"]
    IMLOG2["IMLOG2<br/>Returns the base-2 logarithm of a complex number"]
    IMCOSH["IMCOSH<br/>Returns the hyperbolic cosine of a complex number"]
    IMDIV["IMDIV<br/>Returns the quotient of two complex numbers"]
    IMSINH["IMSINH<br/>Returns the hyperbolic sine of a complex number"]
    IMSUM["IMSUM<br/>Returns the sum of complex numbers"]
    ERFC_PRECISE["ERFC.PRECISE<br/>Returns the complementary error function from x to infinity"]
    IMSECH["IMSECH<br/>Returns the hyperbolic secant of a complex number"]
    IMARGUMENT["IMARGUMENT<br/>Returns the argument theta of a complex number in radians"]
    ERF_PRECISE["ERF.PRECISE<br/>Returns the error function integrated between 0 and x"]
    IMSQRT["IMSQRT<br/>Returns the square root of a complex number"]
    IMEXP["IMEXP<br/>Returns the exponential of a complex number"]
    ERFC["ERFC<br/>Returns the complementary error function"]
    IMSIN["IMSIN<br/>Returns the sine of a complex number"]
    ERF["ERF<br/>Returns the error function integrated between two limits"]
    BESSELI["BESSELI<br/>Returns the modified Bessel function In(x)"]
    HEX2DEC["HEX2DEC<br/>Converts a signed hexadecimal number to decimal"]
    IMREAL["IMREAL<br/>Returns the real coefficient of a complex number"]
    GESTEP["GESTEP<br/>Returns 1 if a number is at or above a step value, else 0"]
    HEX2BIN["HEX2BIN<br/>Converts a signed hexadecimal number to binary"]
    IMCSCH["IMCSCH<br/>Returns the hyperbolic cosecant of a complex number"]
    IMSUB["IMSUB<br/>Returns the difference between two complex numbers"]
    DEC2HEX["DEC2HEX<br/>Converts a signed decimal number to hexadecimal"]
    IMCOT["IMCOT<br/>Returns the cotangent of a complex number"]
    IMPRODUCT["IMPRODUCT<br/>Returns the product of complex numbers"]
    OCT2HEX["OCT2HEX<br/>Converts a signed octal number to hexadecimal"]
    HEX2OCT["HEX2OCT<br/>Converts a signed hexadecimal number to octal"]
    BIN2HEX["BIN2HEX<br/>Converts a signed binary number to hexadecimal"]
    IMSEC["IMSEC<br/>Returns the secant of a complex number"]
    CONVERT["CONVERT<br/>Converts a number from one unit of measure to another"]
    IMCOTH["IMCOTH<br/>Returns the hyperbolic cotangent of a complex number"]
    IMLOG["IMLOG<br/>Returns the logarithm of a complex number in a given base"]
    IMTANH["IMTANH<br/>Returns the hyperbolic tangent of a complex number"]
    IF["IF<br/>External Function"]
    DEC2BIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DEC2BIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DEC2BIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DEC2BIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DEC2BIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMLOG10 --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMLOG10 --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMLOG10 --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMLOG10 -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMLOG10 -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BIN2DEC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BIN2DEC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BIN2DEC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BIN2DEC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BIN2DEC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    OCT2DEC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    OCT2DEC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    OCT2DEC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    OCT2DEC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    OCT2DEC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BESSELK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BESSELK --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BESSELK --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BESSELK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BESSELK -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BITOR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BITOR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BITOR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BITOR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BITOR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BITAND --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BITAND --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BITAND --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BITAND -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BITAND -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCOS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCOS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCOS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMCOS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMCOS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCONJUGATE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCONJUGATE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCONJUGATE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMCONJUGATE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMCONJUGATE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMTAN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMTAN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMTAN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMTAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMTAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DELTA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DELTA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DELTA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DELTA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DELTA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    OCT2BIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    OCT2BIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    OCT2BIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    OCT2BIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    OCT2BIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BESSELJ --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BESSELJ --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BESSELJ --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BESSELJ -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BESSELJ -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DEC2OCT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DEC2OCT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DEC2OCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DEC2OCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DEC2OCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BITLSHIFT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BITLSHIFT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BITLSHIFT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BITLSHIFT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BITLSHIFT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMABS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMABS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMABS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMABS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMABS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMAGINARY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMAGINARY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMAGINARY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMAGINARY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMAGINARY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BIN2OCT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BIN2OCT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BIN2OCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BIN2OCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BIN2OCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COMPLEX --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COMPLEX --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    COMPLEX --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    COMPLEX -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    COMPLEX -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BITXOR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BITXOR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BITXOR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BITXOR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BITXOR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BESSELY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BESSELY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BESSELY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BESSELY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BESSELY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCSC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCSC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCSC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMCSC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMCSC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BITRSHIFT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BITRSHIFT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BITRSHIFT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BITRSHIFT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BITRSHIFT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMPOWER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPOWER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPOWER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMPOWER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMPOWER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMLN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMLN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMLN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMLN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMLN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMLOG2 --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMLOG2 --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMLOG2 --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMLOG2 -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMLOG2 -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCOSH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCOSH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCOSH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMCOSH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMCOSH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMDIV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMDIV --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMDIV --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMDIV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMDIV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSINH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSINH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSINH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMSINH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMSINH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSUM --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSUM --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSUM --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMSUM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMSUM -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ERFC_PRECISE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ERFC_PRECISE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ERFC_PRECISE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ERFC_PRECISE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ERFC_PRECISE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSECH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSECH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSECH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMSECH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMSECH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMARGUMENT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMARGUMENT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMARGUMENT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMARGUMENT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMARGUMENT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ERF_PRECISE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ERF_PRECISE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ERF_PRECISE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ERF_PRECISE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ERF_PRECISE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSQRT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSQRT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSQRT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMSQRT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMSQRT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMEXP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMEXP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMEXP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMEXP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMEXP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ERFC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ERFC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ERFC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ERFC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ERFC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMSIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMSIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ERF --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ERF --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ERF --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ERF -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ERF -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BESSELI --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BESSELI --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BESSELI --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BESSELI -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BESSELI -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HEX2DEC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HEX2DEC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    HEX2DEC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    HEX2DEC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    HEX2DEC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMREAL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMREAL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMREAL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMREAL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMREAL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GESTEP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GESTEP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    GESTEP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    GESTEP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    GESTEP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HEX2BIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HEX2BIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    HEX2BIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    HEX2BIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    HEX2BIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCSCH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCSCH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCSCH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMCSCH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMCSCH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSUB --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSUB --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSUB --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMSUB -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMSUB -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DEC2HEX --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DEC2HEX --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DEC2HEX --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DEC2HEX -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DEC2HEX -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCOT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCOT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCOT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMCOT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMCOT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMPRODUCT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPRODUCT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPRODUCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMPRODUCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMPRODUCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    OCT2HEX --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    OCT2HEX --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    OCT2HEX --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    OCT2HEX -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    OCT2HEX -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HEX2OCT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HEX2OCT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    HEX2OCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    HEX2OCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    HEX2OCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BIN2HEX --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BIN2HEX --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BIN2HEX --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BIN2HEX -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BIN2HEX -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMSEC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMSEC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMSEC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMSEC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMSEC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CONVERT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CONVERT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CONVERT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CONVERT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CONVERT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMCOTH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMCOTH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMCOTH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMCOTH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMCOTH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMLOG --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMLOG --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMLOG --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMLOG -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMLOG -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    IMTANH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMTANH --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMTANH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    IMTANH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    IMTANH -.-> IFERROR
    class IFERROR external
    class DEC2BIN Engineering
    class IMLOG10 Engineering
    class BIN2DEC Engineering
    class OCT2DEC Engineering
    class BESSELK Engineering
    class BITOR Engineering
    class BITAND Engineering
    class IMCOS Engineering
    class IMCONJUGATE Engineering
    class IMTAN Engineering
    class DELTA Engineering
    class OCT2BIN Engineering
    class BESSELJ Engineering
    class DEC2OCT Engineering
    class BITLSHIFT Engineering
    class IMABS Engineering
    class IMAGINARY Engineering
    class BIN2OCT Engineering
    class COMPLEX Engineering
    class BITXOR Engineering
    class BESSELY Engineering
    class IMCSC Engineering
    class BITRSHIFT Engineering
    class IMPOWER Engineering
    class IMLN Engineering
    class IMLOG2 Engineering
    class IMCOSH Engineering
    class IMDIV Engineering
    class IMSINH Engineering
    class IMSUM Engineering
    class ERFC_PRECISE Engineering
    class IMSECH Engineering
    class IMARGUMENT Engineering
    class ERF_PRECISE Engineering
    class IMSQRT Engineering
    class IMEXP Engineering
    class ERFC Engineering
    class IMSIN Engineering
    class ERF Engineering
    class BESSELI Engineering
    class HEX2DEC Engineering
    class IMREAL Engineering
    class GESTEP Engineering
    class HEX2BIN Engineering
    class IMCSCH Engineering
    class IMSUB Engineering
    class DEC2HEX Engineering
    class IMCOT Engineering
    class IMPRODUCT Engineering
    class OCT2HEX Engineering
    class HEX2OCT Engineering
    class BIN2HEX Engineering
    class IMSEC Engineering
    class CONVERT Engineering
    class IMCOTH Engineering
    class IMLOG Engineering
    class IMTANH Engineering
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (`-.->`)**: "Similar functions" relationships
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in This Category: 57
