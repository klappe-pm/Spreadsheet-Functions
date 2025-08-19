---
fileName: Spreadsheets-Functions-Math-Trigonometry-Complete
area:
category:
subCategory:
topic:
subTopic: 
dateCreated: 2025-06-16
dateRevised: 2025-06-16
aliases: [Spreadsheets-Functions-Math-Trigonometry-Complete]
tags: []
---

# Spreadsheets-Functions-Math-Trigonometry-Complete

```mermaid

graph LR
    MathTrig["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Math & Trig</b><br/>────────────────<br/>Mathematical and trigonometric functions<br/><b>Total Functions:</b> 73</div>"]
    
    MathTrig --> BasicArithmetic["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Basic Arithmetic</b><br/>────────────────<br/>Basic mathematical operations<br/><b>Functions:</b> 18</div>"]
    
    MathTrig --> Trigonometry["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Trigonometry</b><br/>────────────────<br/>Trigonometric functions<br/><b>Functions:</b> 21</div>"]
    
    MathTrig --> AdvancedMath["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Advanced Math</b><br/>────────────────<br/>Advanced mathematical functions<br/><b>Functions:</b> 24</div>"]
    
    MathTrig --> MatrixOperations["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Matrix Operations</b><br/>────────────────<br/>Matrix and array operations<br/><b>Functions:</b> 4</div>"]
    
    MathTrig --> RandomNumbers["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Random Numbers</b><br/>────────────────<br/>Random number generation<br/><b>Functions:</b> 3</div>"]
    
    MathTrig --> Constants["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Constants</b><br/>────────────────<br/>Mathematical constants<br/><b>Functions:</b> 1</div>"]
    
    MathTrig --> NewFunctions["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>New Functions</b><br/>────────────────<br/>Modern mathematical functions<br/><b>Functions:</b> 2</div>"]
    
    %% Basic Arithmetic Functions (18 functions)
    BasicArithmetic --> ABS["<div align='left' style='font-family: MonoLisa, monospace;'><b>ABS</b><br/>────────────────<br/>Returns the absolute value of a number</div>"]
    ABS --> ABSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ABS(number)</div>"]
    ABS --> ABSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ABS(-5) → 5</div>"]
    
    BasicArithmetic --> CEILING["<div align='left' style='font-family: MonoLisa, monospace;'><b>CEILING</b><br/>────────────────<br/>Rounds a number up to the nearest multiple of significance</div>"]
    CEILING --> CEILINGSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CEILING(number, [significance])</div>"]
    CEILING --> CEILINGEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CEILING(2.1, 1) → 3</div>"]
    
    BasicArithmetic --> FLOOR["<div align='left' style='font-family: MonoLisa, monospace;'><b>FLOOR</b><br/>────────────────<br/>Rounds a number down to the nearest multiple of significance</div>"]
    FLOOR --> FLOORSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FLOOR(number, [significance])</div>"]
    FLOOR --> FLOOREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FLOOR(3.7, 1) → 3</div>"]
    
    BasicArithmetic --> ROUND["<div align='left' style='font-family: MonoLisa, monospace;'><b>ROUND</b><br/>────────────────<br/>Rounds a number to a specified number of digits</div>"]
    ROUND --> ROUNDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ROUND(number, num_digits)</div>"]
    ROUND --> ROUNDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ROUND(2.15, 1) → 2.2</div>"]
    
    BasicArithmetic --> ROUNDUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>ROUNDUP</b><br/>────────────────<br/>Rounds a number up, away from zero</div>"]
    ROUNDUP --> ROUNDUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ROUNDUP(number, num_digits)</div>"]
    ROUNDUP --> ROUNDUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ROUNDUP(2.11, 1) → 2.2</div>"]
    
    BasicArithmetic --> ROUNDDOWN["<div align='left' style='font-family: MonoLisa, monospace;'><b>ROUNDDOWN</b><br/>────────────────<br/>Rounds a number down, toward zero</div>"]
    ROUNDDOWN --> ROUNDDOWNSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ROUNDDOWN(number, num_digits)</div>"]
    ROUNDDOWN --> ROUNDDOWNEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ROUNDDOWN(3.99, 1) → 3.9</div>"]
    
    BasicArithmetic --> MOD["<div align='left' style='font-family: MonoLisa, monospace;'><b>MOD</b><br/>────────────────<br/>Returns the remainder from division</div>"]
    MOD --> MODSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MOD(number, divisor)</div>"]
    MOD --> MODEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MOD(10, 3) → 1</div>"]
    
    BasicArithmetic --> POWER["<div align='left' style='font-family: MonoLisa, monospace;'><b>POWER</b><br/>────────────────<br/>Returns the result of a number raised to a power</div>"]
    POWER --> POWERSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>POWER(number, power)</div>"]
    POWER --> POWEREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=POWER(5, 2) → 25</div>"]
    
    BasicArithmetic --> SQRT["<div align='left' style='font-family: MonoLisa, monospace;'><b>SQRT</b><br/>────────────────<br/>Returns a positive square root</div>"]
    SQRT --> SQRTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SQRT(number)</div>"]
    SQRT --> SQRTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SQRT(16) → 4</div>"]
    
    %% Trigonometry Functions (21 functions) - showing key functions
    Trigonometry --> SIN["<div align='left' style='font-family: MonoLisa, monospace;'><b>SIN</b><br/>────────────────<br/>Returns the sine of the given angle</div>"]
    SIN --> SINSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SIN(number)</div>"]
    SIN --> SINEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SIN(PI()/2) → 1</div>"]
    
    Trigonometry --> COS["<div align='left' style='font-family: MonoLisa, monospace;'><b>COS</b><br/>────────────────<br/>Returns the cosine of the given angle</div>"]
    COS --> COSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>COS(number)</div>"]
    COS --> COSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=COS(0) → 1</div>"]
    
    Trigonometry --> TAN["<div align='left' style='font-family: MonoLisa, monospace;'><b>TAN</b><br/>────────────────<br/>Returns the tangent of the given angle</div>"]
    TAN --> TANSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TAN(number)</div>"]
    TAN --> TANEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TAN(PI()/4) → 1</div>"]
    
    Trigonometry --> ASIN["<div align='left' style='font-family: MonoLisa, monospace;'><b>ASIN</b><br/>────────────────<br/>Returns the arcsine of a number</div>"]
    ASIN --> ASINSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ASIN(number)</div>"]
    ASIN --> ASINEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ASIN(1) → 1.5708</div>"]
    
    Trigonometry --> ACOS["<div align='left' style='font-family: MonoLisa, monospace;'><b>ACOS</b><br/>────────────────<br/>Returns the arccosine of a number</div>"]
    ACOS --> ACOSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ACOS(number)</div>"]
    ACOS --> ACOSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ACOS(1) → 0</div>"]
    
    Trigonometry --> ATAN["<div align='left' style='font-family: MonoLisa, monospace;'><b>ATAN</b><br/>────────────────<br/>Returns the arctangent of a number</div>"]
    ATAN --> ATANSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ATAN(number)</div>"]
    ATAN --> ATANEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ATAN(1) → 0.7854</div>"]
    
    %% Advanced Math Functions (24 functions) - showing key functions
    AdvancedMath --> LOG["<div align='left' style='font-family: MonoLisa, monospace;'><b>LOG</b><br/>────────────────<br/>Returns the logarithm of a number to a specified base</div>"]
    LOG --> LOGSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>LOG(number, [base])</div>"]
    LOG --> LOGEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=LOG(10, 10) → 1</div>"]
    
    AdvancedMath --> LN["<div align='left' style='font-family: MonoLisa, monospace;'><b>LN</b><br/>────────────────<br/>Returns the natural logarithm of a number</div>"]
    LN --> LNSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>LN(number)</div>"]
    LN --> LNEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=LN(EXP(1)) → 1</div>"]
    
    AdvancedMath --> EXP["<div align='left' style='font-family: MonoLisa, monospace;'><b>EXP</b><br/>────────────────<br/>Returns e raised to the power of a given number</div>"]
    EXP --> EXPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>EXP(number)</div>"]
    EXP --> EXPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=EXP(1) → 2.7183</div>"]
    
    AdvancedMath --> FACT["<div align='left' style='font-family: MonoLisa, monospace;'><b>FACT</b><br/>────────────────<br/>Returns the factorial of a number</div>"]
    FACT --> FACTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FACT(number)</div>"]
    FACT --> FACTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FACT(5) → 120</div>"]
    
    AdvancedMath --> GCD["<div align='left' style='font-family: MonoLisa, monospace;'><b>GCD</b><br/>────────────────<br/>Returns the greatest common divisor</div>"]
    GCD --> GCDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>GCD(number1, [number2], ...)</div>"]
    GCD --> GCDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=GCD(24, 36) → 12</div>"]
    
    AdvancedMath --> LCM["<div align='left' style='font-family: MonoLisa, monospace;'><b>LCM</b><br/>────────────────<br/>Returns the least common multiple</div>"]
    LCM --> LCMSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>LCM(number1, [number2], ...)</div>"]
    LCM --> LCMEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=LCM(5, 2) → 10</div>"]
    
    %% Matrix Operations (4 functions)
    MatrixOperations --> MDETERM["<div align='left' style='font-family: MonoLisa, monospace;'><b>MDETERM</b><br/>────────────────<br/>Returns the matrix determinant of an array</div>"]
    MDETERM --> MDETERMSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MDETERM(array)</div>"]
    MDETERM --> MDETERMEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MDETERM(A1:B2) → -3</div>"]
    
    MatrixOperations --> MINVERSE["<div align='left' style='font-family: MonoLisa, monospace;'><b>MINVERSE</b><br/>────────────────<br/>Returns the matrix inverse of an array</div>"]
    MINVERSE --> MINVERSESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MINVERSE(array)</div>"]
    MINVERSE --> MINVERSEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MINVERSE(A1:B2)</div>"]
    
    MatrixOperations --> MMULT["<div align='left' style='font-family: MonoLisa, monospace;'><b>MMULT</b><br/>────────────────<br/>Returns the matrix product of two arrays</div>"]
    MMULT --> MMULTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MMULT(array1, array2)</div>"]
    MMULT --> MMULTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MMULT(A1:B2, C1:D2)</div>"]
    
    MatrixOperations --> TRANSPOSE["<div align='left' style='font-family: MonoLisa, monospace;'><b>TRANSPOSE</b><br/>────────────────<br/>Returns the transpose of an array</div>"]
    TRANSPOSE --> TRANSPOSESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TRANSPOSE(array)</div>"]
    TRANSPOSE --> TRANSPOSEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TRANSPOSE(A1:C3)</div>"]
    
    %% Random Numbers (3 functions)
    RandomNumbers --> RAND["<div align='left' style='font-family: MonoLisa, monospace;'><b>RAND</b><br/>────────────────<br/>Returns a random number between 0 and 1</div>"]
    RAND --> RANDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>RAND()</div>"]
    RAND --> RANDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=RAND() → 0.285</div>"]
    
    RandomNumbers --> RANDBETWEEN["<div align='left' style='font-family: MonoLisa, monospace;'><b>RANDBETWEEN</b><br/>────────────────<br/>Returns a random number between specified numbers</div>"]
    RANDBETWEEN --> RANDBETWEENSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>RANDBETWEEN(bottom, top)</div>"]
    RANDBETWEEN --> RANDBETWEENEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=RANDBETWEEN(1, 100) → 42</div>"]
    
    RandomNumbers --> RANDARRAY_MATH["<div align='left' style='font-family: MonoLisa, monospace;'><b>RANDARRAY</b><br/>────────────────<br/>Generates an array of random numbers</div>"]
    RANDARRAY_MATH --> RANDARRAYMATHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>RANDARRAY([rows], [columns], [min], [max], [integer])</div>"]
    RANDARRAY_MATH --> RANDARRAYMATHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=RANDARRAY(3, 2, 1, 10, TRUE)</div>"]
    
    %% Constants (1 function)
    Constants --> PI_FUNC["<div align='left' style='font-family: MonoLisa, monospace;'><b>PI</b><br/>────────────────<br/>Returns the value of pi</div>"]
    PI_FUNC --> PIFUNCSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>PI()</div>"]
    PI_FUNC --> PIFUNCEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=PI() → 3.14159</div>"]
    
    %% New Functions (2 functions)
    NewFunctions --> SEQUENCE_MATH["<div align='left' style='font-family: MonoLisa, monospace;'><b>SEQUENCE</b><br/>────────────────<br/>Generates a list of sequential numbers</div>"]
    SEQUENCE_MATH --> SEQUENCEMATHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SEQUENCE(rows, [columns], [start], [step])</div>"]
    SEQUENCE_MATH --> SEQUENCEMATHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SEQUENCE(5) → {1;2;3;4;5}</div>"]
    
    NewFunctions --> PERMUTATIONA_MATH["<div align='left' style='font-family: MonoLisa, monospace;'><b>PERMUTATIONA</b><br/>────────────────<br/>Returns permutations with repetitions</div>"]
    PERMUTATIONA_MATH --> PERMUTATIONAMATHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>PERMUTATIONA(number, number_chosen)</div>"]
    PERMUTATIONA_MATH --> PERMUTATIONAMATHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=PERMUTATIONA(3, 2) → 9</div>"]
    
    %% Styling
    style MathTrig fill:#F0FFFF,stroke:#333,stroke-width:2px
    style BasicArithmetic fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Trigonometry fill:#F0FFFF,stroke:#333,stroke-width:2px
    style AdvancedMath fill:#F0FFFF,stroke:#333,stroke-width:2px
    style MatrixOperations fill:#F0FFFF,stroke:#333,stroke-width:2px
    style RandomNumbers fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Constants fill:#F0FFFF,stroke:#333,stroke-width:2px
    style NewFunctions fill:#F0FFFF,stroke:#333,stroke-width:2px
    
    %% Functions alternate: odd=green, even=blue (sample of 73 functions)
    style ABS fill:#F0FFF0,stroke:#333,stroke-width:2px
    style CEILING fill:#B9E9EB,stroke:#333,stroke-width:2px
    style FLOOR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ROUND fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ROUNDUP fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ROUNDDOWN fill:#B9E9EB,stroke:#333,stroke-width:2px
    style MOD fill:#F0FFF0,stroke:#333,stroke-width:2px
    style POWER fill:#B9E9EB,stroke:#333,stroke-width:2px
    style SQRT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style SIN fill:#B9E9EB,stroke:#333,stroke-width:2px
    style COS fill:#F0FFF0,stroke:#333,stroke-width:2px
    style TAN fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ASIN fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ACOS fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ATAN fill:#F0FFF0,stroke:#333,stroke-width:2px
    style LOG fill:#B9E9EB,stroke:#333,stroke-width:2px
    style LN fill:#F0FFF0,stroke:#333,stroke-width:2px
    style EXP fill:#B9E9EB,stroke:#333,stroke-width:2px
    style FACT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style GCD fill:#B9E9EB,stroke:#333,stroke-width:2px
    style LCM fill:#F0FFF0,stroke:#333,stroke-width:2px
    style MDETERM fill:#B9E9EB,stroke:#333,stroke-width:2px
    style MINVERSE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style MMULT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style TRANSPOSE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style RAND fill:#B9E9EB,stroke:#333,stroke-width:2px
    style RANDBETWEEN fill:#F0FFF0,stroke:#333,stroke-width:2px
    style RANDARRAY_MATH fill:#B9E9EB,stroke:#333,stroke-width:2px
    style PI_FUNC fill:#F0FFF0,stroke:#333,stroke-width:2px
    style SEQUENCE_MATH fill:#B9E9EB,stroke:#333,stroke-width:2px
    style PERMUTATIONA_MATH fill:#F0FFF0,stroke:#333,stroke-width:2px
    
    %% All syntax nodes - pink
    style ABSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CEILINGSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FLOORSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ROUNDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ROUNDUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ROUNDDOWNSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MODSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style POWERSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SQRTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SINSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style COSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TANSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ASINSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ACOSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ATANSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style LOGSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style LNSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style EXPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FACTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style GCDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style LCMSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MDETERMSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MINVERSESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MMULTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TRANSPOSESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style RANDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style RANDBETWEENSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style RANDARRAYMATHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style PIFUNCSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SEQUENCEMATHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style PERMUTATIONAMATHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    
    %% All example nodes - lavender
    style ABSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CEILINGEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FLOOREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ROUNDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ROUNDUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ROUNDDOWNEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MODEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style POWEREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SQRTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SINEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style COSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TANEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ASINEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ACOSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ATANEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style LOGEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style LNEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style EXPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FACTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style GCDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style LCMEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MDETERMEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MINVERSEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MMULTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TRANSPOSEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style RANDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style RANDBETWEENEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style RANDARRAYMATHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style PIFUNCEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SEQUENCEMATHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style PERMUTATIONAMATHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
```

---