# Math & Trig Functions Relationship Diagram

This diagram shows the relationships between functions in the Math & Trig category and their connections to commonly used functions.

```mermaid
graph TD
    classDef MathTrig fill:#4ECDC4,stroke:#333,stroke-width:2px,color:#000
    COT["COT<br/>COT calculates mathematical and trigonometric values for sci..."]
    PRODUCT["PRODUCT<br/>PRODUCT calculates mathematical and trigonometric values for..."]
    SEC["SEC<br/>SEC calculates mathematical and trigonometric values for sci..."]
    ARABIC["ARABIC<br/>ARABIC calculates mathematical and trigonometric values for ..."]
    LOG10["LOG10<br/>LOG10 calculates mathematical and trigonometric values for s..."]
    LCM["LCM<br/>LCM calculates mathematical and trigonometric values for sci..."]
    RAND["RAND<br/>RAND calculates mathematical and trigonometric values for sc..."]
    SUMIF["SUMIF<br/>SUMIF performs conditional calculations based on specified c..."]
    MROUND["MROUND<br/>MROUND calculates mathematical and trigonometric values for ..."]
    ROUND["ROUND<br/>ROUND rounds a number to a specified number of decimal place..."]
    POWER["POWER<br/>POWER calculates mathematical and trigonometric values for s..."]
    ATANH["ATANH<br/>ATANH calculates mathematical and trigonometric values for s..."]
    BASE["BASE<br/>BASE calculates mathematical and trigonometric values for sc..."]
    ACOS["ACOS<br/>ACOS calculates mathematical and trigonometric values for sc..."]
    ATAN["ATAN<br/>ATAN calculates mathematical and trigonometric values for sc..."]
    INT["INT<br/>INT calculates mathematical and trigonometric values for sci..."]
    EXP["EXP<br/>EXP calculates mathematical and trigonometric values for sci..."]
    MOD["MOD<br/>MOD calculates mathematical and trigonometric values for sci..."]
    COTH["COTH<br/>COTH calculates mathematical and trigonometric values for sc..."]
    CEILING_MATH["CEILING.MATH<br/>CEILING.MATH calculates mathematical and trigonometric value..."]
    SIN["SIN<br/>SIN calculates mathematical and trigonometric values for sci..."]
    RADIANS["RADIANS<br/>RADIANS calculates mathematical and trigonometric values for..."]
    ODD["ODD<br/>ODD calculates mathematical and trigonometric values for sci..."]
    SUMPRODUCT["SUMPRODUCT<br/>SUMPRODUCT calculates mathematical and trigonometric values ..."]
    ROUNDDOWN["ROUNDDOWN<br/>ROUNDDOWN calculates mathematical and trigonometric values f..."]
    SUM["SUM<br/>SUM adds all numbers in a range or list of arguments. This i..."]
    SERIESSUM["SERIESSUM<br/>SERIESSUM calculates mathematical and trigonometric values f..."]
    FACTDOUBLE["FACTDOUBLE<br/>FACTDOUBLE calculates mathematical and trigonometric values ..."]
    ISO_CEILING["ISO.CEILING<br/>ISO.CEILING calculates mathematical and trigonometric values..."]
    MMULT["MMULT<br/>MMULT calculates mathematical and trigonometric values for s..."]
    SINH["SINH<br/>SINH calculates mathematical and trigonometric values for sc..."]
    SIGN["SIGN<br/>SIGN calculates mathematical and trigonometric values for sc..."]
    COSH["COSH<br/>COSH calculates mathematical and trigonometric values for sc..."]
    SUMIFS["SUMIFS<br/>SUMIFS performs conditional calculations based on specified ..."]
    SQRTPI["SQRTPI<br/>SQRTPI calculates mathematical and trigonometric values for ..."]
    TANH["TANH<br/>TANH calculates mathematical and trigonometric values for sc..."]
    EVEN["EVEN<br/>EVEN calculates mathematical and trigonometric values for sc..."]
    LOG["LOG<br/>LOG calculates mathematical and trigonometric values for sci..."]
    SQRT["SQRT<br/>SQRT returns the positive square root of a number. The numbe..."]
    CEILING["CEILING<br/>CEILING calculates mathematical and trigonometric values for..."]
    SECH["SECH<br/>SECH calculates mathematical and trigonometric values for sc..."]
    SUBTOTAL["SUBTOTAL<br/>SUBTOTAL calculates mathematical and trigonometric values fo..."]
    FLOOR_MATH["FLOOR.MATH<br/>FLOOR.MATH calculates mathematical and trigonometric values ..."]
    RANDARRAY["RANDARRAY<br/>RANDARRAY calculates mathematical and trigonometric values f..."]
    MDETERM["MDETERM<br/>MDETERM calculates mathematical and trigonometric values for..."]
    QUOTIENT["QUOTIENT<br/>QUOTIENT calculates mathematical and trigonometric values fo..."]
    TRUNC["TRUNC<br/>TRUNC calculates mathematical and trigonometric values for s..."]
    ACOSH["ACOSH<br/>ACOSH calculates mathematical and trigonometric values for s..."]
    ASINH["ASINH<br/>ASINH calculates mathematical and trigonometric values for s..."]
    CSC["CSC<br/>CSC calculates mathematical and trigonometric values for sci..."]
    ROMAN["ROMAN<br/>ROMAN calculates mathematical and trigonometric values for s..."]
    SUMSQ["SUMSQ<br/>SUMSQ calculates mathematical and trigonometric values for s..."]
    AGGREGATE["AGGREGATE<br/>AGGREGATE calculates mathematical and trigonometric values f..."]
    FLOOR["FLOOR<br/>FLOOR calculates mathematical and trigonometric values for s..."]
    DECIMAL["DECIMAL<br/>DECIMAL calculates mathematical and trigonometric values for..."]
    MUNIT["MUNIT<br/>MUNIT calculates mathematical and trigonometric values for s..."]
    ABS["ABS<br/>ABS calculates mathematical and trigonometric values for sci..."]
    PI["PI<br/>PI calculates mathematical and trigonometric values for scie..."]
    MINVERSE["MINVERSE<br/>MINVERSE calculates mathematical and trigonometric values fo..."]
    MULTINOMIAL["MULTINOMIAL<br/>MULTINOMIAL calculates mathematical and trigonometric values..."]
    RANDBETWEEN["RANDBETWEEN<br/>RANDBETWEEN calculates mathematical and trigonometric values..."]
    SEQUENCE["SEQUENCE<br/>SEQUENCE calculates mathematical and trigonometric values fo..."]
    DEGREES["DEGREES<br/>DEGREES calculates mathematical and trigonometric values for..."]
    ASIN["ASIN<br/>ASIN calculates mathematical and trigonometric values for sc..."]
    CSCH["CSCH<br/>CSCH calculates mathematical and trigonometric values for sc..."]
    ROUNDUP["ROUNDUP<br/>ROUNDUP calculates mathematical and trigonometric values for..."]
    LN["LN<br/>LN calculates mathematical and trigonometric values for scie..."]
    TAN["TAN<br/>TAN calculates mathematical and trigonometric values for sci..."]
    FACT["FACT<br/>FACT calculates mathematical and trigonometric values for sc..."]
    COS["COS<br/>COS calculates mathematical and trigonometric values for sci..."]
    ATAN2["ATAN2<br/>ATAN2 calculates mathematical and trigonometric values for s..."]
    GCD["GCD<br/>GCD calculates mathematical and trigonometric values for sci..."]
    IF["IF<br/>External Function"]
    COT --> IF
    class IF external
    COT --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    COT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    COT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PRODUCT --> IF
    class IF external
    PRODUCT --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    PRODUCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    PRODUCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PRODUCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SEC --> IF
    class IF external
    SEC --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SEC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SEC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SEC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ARABIC --> IF
    class IF external
    ARABIC --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ARABIC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ARABIC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ARABIC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LOG10 --> IF
    class IF external
    LOG10 --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    LOG10 --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    LOG10 -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LOG10 -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LCM --> IF
    class IF external
    LCM --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    LCM --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    LCM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LCM -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RAND --> IF
    class IF external
    RAND --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    RAND --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    RAND -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    RAND -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SUMIF --> IF
    class IF external
    SUMIF --> SUM
    COUNT["COUNT<br/>External Function"]
    SUMIF --> COUNT
    class COUNT external
    IF["IF<br/>Related Function"]
    SUMIF -.-> IF
    class IF external
    SUMIF -.-> SUMIF
    IF["IF<br/>External Function"]
    MROUND --> IF
    class IF external
    MROUND --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    MROUND --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    MROUND -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MROUND -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ROUND --> IF
    class IF external
    ROUND --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ROUND --> AVERAGE
    class AVERAGE external
    ROUND -.-> ROUNDUP
    ROUND -.-> ROUNDDOWN
    IF["IF<br/>External Function"]
    POWER --> IF
    class IF external
    POWER --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    POWER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    POWER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    POWER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ATANH --> IF
    class IF external
    ATANH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ATANH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ATANH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ATANH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BASE --> IF
    class IF external
    BASE --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    BASE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    BASE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BASE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ACOS --> IF
    class IF external
    ACOS --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ACOS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ACOS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ACOS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ATAN --> IF
    class IF external
    ATAN --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ATAN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ATAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ATAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    INT --> IF
    class IF external
    INT --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    INT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    INT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    INT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    EXP --> IF
    class IF external
    EXP --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    EXP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    EXP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    EXP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MOD --> IF
    class IF external
    MOD --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    MOD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    MOD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MOD -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COTH --> IF
    class IF external
    COTH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    COTH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    COTH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COTH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CEILING_MATH --> IF
    class IF external
    CEILING_MATH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    CEILING_MATH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CEILING_MATH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CEILING_MATH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SIN --> IF
    class IF external
    SIN --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RADIANS --> IF
    class IF external
    RADIANS --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    RADIANS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    RADIANS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    RADIANS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ODD --> IF
    class IF external
    ODD --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ODD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ODD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ODD -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SUMPRODUCT --> IF
    class IF external
    SUMPRODUCT --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SUMPRODUCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SUMPRODUCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SUMPRODUCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ROUNDDOWN --> IF
    class IF external
    ROUNDDOWN --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ROUNDDOWN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ROUNDDOWN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ROUNDDOWN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SUM --> IF
    class IF external
    COUNT["COUNT<br/>External Function"]
    SUM --> COUNT
    class COUNT external
    AVERAGE["AVERAGE<br/>External Function"]
    SUM --> AVERAGE
    class AVERAGE external
    SUM -.-> SUMIF
    SUM -.-> SUMIFS
    IF["IF<br/>External Function"]
    SERIESSUM --> IF
    class IF external
    SERIESSUM --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SERIESSUM --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SERIESSUM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SERIESSUM -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FACTDOUBLE --> IF
    class IF external
    FACTDOUBLE --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    FACTDOUBLE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    FACTDOUBLE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FACTDOUBLE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISO_CEILING --> IF
    class IF external
    ISO_CEILING --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ISO_CEILING --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISO_CEILING -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISO_CEILING -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MMULT --> IF
    class IF external
    MMULT --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    MMULT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    MMULT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MMULT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SINH --> IF
    class IF external
    SINH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SINH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SINH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SINH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SIGN --> IF
    class IF external
    SIGN --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SIGN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SIGN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SIGN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COSH --> IF
    class IF external
    COSH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    COSH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    COSH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COSH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SUMIFS --> IF
    class IF external
    SUMIFS --> SUM
    COUNT["COUNT<br/>External Function"]
    SUMIFS --> COUNT
    class COUNT external
    IF["IF<br/>Related Function"]
    SUMIFS -.-> IF
    class IF external
    SUMIFS -.-> SUMIF
    IF["IF<br/>External Function"]
    SQRTPI --> IF
    class IF external
    SQRTPI --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SQRTPI --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SQRTPI -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SQRTPI -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TANH --> IF
    class IF external
    TANH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    TANH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TANH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TANH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    EVEN --> IF
    class IF external
    EVEN --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    EVEN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    EVEN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    EVEN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LOG --> IF
    class IF external
    LOG --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    LOG --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    LOG -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LOG -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SQRT --> IF
    class IF external
    SQRT --> ABS
    SQRT --> POWER
    SQRT -.-> POWER
    SQRT -.-> EXP
    IF["IF<br/>External Function"]
    CEILING --> IF
    class IF external
    CEILING --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    CEILING --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CEILING -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CEILING -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SECH --> IF
    class IF external
    SECH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SECH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SECH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SECH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SUBTOTAL --> IF
    class IF external
    SUBTOTAL --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SUBTOTAL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SUBTOTAL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SUBTOTAL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FLOOR_MATH --> IF
    class IF external
    FLOOR_MATH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    FLOOR_MATH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    FLOOR_MATH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FLOOR_MATH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RANDARRAY --> IF
    class IF external
    RANDARRAY --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    RANDARRAY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    RANDARRAY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    RANDARRAY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MDETERM --> IF
    class IF external
    MDETERM --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    MDETERM --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    MDETERM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MDETERM -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    QUOTIENT --> IF
    class IF external
    QUOTIENT --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    QUOTIENT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    QUOTIENT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    QUOTIENT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TRUNC --> IF
    class IF external
    TRUNC --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    TRUNC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TRUNC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TRUNC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ACOSH --> IF
    class IF external
    ACOSH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ACOSH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ACOSH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ACOSH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ASINH --> IF
    class IF external
    ASINH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ASINH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ASINH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ASINH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CSC --> IF
    class IF external
    CSC --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    CSC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CSC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CSC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ROMAN --> IF
    class IF external
    ROMAN --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ROMAN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ROMAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ROMAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SUMSQ --> IF
    class IF external
    SUMSQ --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SUMSQ --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SUMSQ -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SUMSQ -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    AGGREGATE --> IF
    class IF external
    AGGREGATE --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    AGGREGATE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    AGGREGATE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    AGGREGATE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FLOOR --> IF
    class IF external
    FLOOR --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    FLOOR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    FLOOR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FLOOR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DECIMAL --> IF
    class IF external
    DECIMAL --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    DECIMAL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DECIMAL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DECIMAL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MUNIT --> IF
    class IF external
    MUNIT --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    MUNIT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    MUNIT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MUNIT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ABS --> IF
    class IF external
    ABS --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ABS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ABS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ABS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PI --> IF
    class IF external
    PI --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    PI --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    PI -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PI -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MINVERSE --> IF
    class IF external
    MINVERSE --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    MINVERSE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    MINVERSE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MINVERSE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MULTINOMIAL --> IF
    class IF external
    MULTINOMIAL --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    MULTINOMIAL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    MULTINOMIAL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MULTINOMIAL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RANDBETWEEN --> IF
    class IF external
    RANDBETWEEN --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    RANDBETWEEN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    RANDBETWEEN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    RANDBETWEEN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SEQUENCE --> IF
    class IF external
    SEQUENCE --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    SEQUENCE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SEQUENCE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SEQUENCE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DEGREES --> IF
    class IF external
    DEGREES --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    DEGREES --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DEGREES -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DEGREES -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ASIN --> IF
    class IF external
    ASIN --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ASIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ASIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ASIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CSCH --> IF
    class IF external
    CSCH --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    CSCH --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CSCH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CSCH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ROUNDUP --> IF
    class IF external
    ROUNDUP --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ROUNDUP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ROUNDUP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ROUNDUP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LN --> IF
    class IF external
    LN --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    LN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    LN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TAN --> IF
    class IF external
    TAN --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    TAN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FACT --> IF
    class IF external
    FACT --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    FACT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    FACT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FACT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COS --> IF
    class IF external
    COS --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    COS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    COS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ATAN2 --> IF
    class IF external
    ATAN2 --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    ATAN2 --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ATAN2 -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ATAN2 -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GCD --> IF
    class IF external
    GCD --> SUM
    AVERAGE["AVERAGE<br/>External Function"]
    GCD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    GCD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GCD -.-> IFERROR
    class IFERROR external
    class COT MathTrig
    class PRODUCT MathTrig
    class SEC MathTrig
    class ARABIC MathTrig
    class LOG10 MathTrig
    class LCM MathTrig
    class RAND MathTrig
    class SUMIF MathTrig
    class MROUND MathTrig
    class ROUND MathTrig
    class POWER MathTrig
    class ATANH MathTrig
    class BASE MathTrig
    class ACOS MathTrig
    class ATAN MathTrig
    class INT MathTrig
    class EXP MathTrig
    class MOD MathTrig
    class COTH MathTrig
    class CEILING_MATH MathTrig
    class SIN MathTrig
    class RADIANS MathTrig
    class ODD MathTrig
    class SUMPRODUCT MathTrig
    class ROUNDDOWN MathTrig
    class SUM MathTrig
    class SERIESSUM MathTrig
    class FACTDOUBLE MathTrig
    class ISO_CEILING MathTrig
    class MMULT MathTrig
    class SINH MathTrig
    class SIGN MathTrig
    class COSH MathTrig
    class SUMIFS MathTrig
    class SQRTPI MathTrig
    class TANH MathTrig
    class EVEN MathTrig
    class LOG MathTrig
    class SQRT MathTrig
    class CEILING MathTrig
    class SECH MathTrig
    class SUBTOTAL MathTrig
    class FLOOR_MATH MathTrig
    class RANDARRAY MathTrig
    class MDETERM MathTrig
    class QUOTIENT MathTrig
    class TRUNC MathTrig
    class ACOSH MathTrig
    class ASINH MathTrig
    class CSC MathTrig
    class ROMAN MathTrig
    class SUMSQ MathTrig
    class AGGREGATE MathTrig
    class FLOOR MathTrig
    class DECIMAL MathTrig
    class MUNIT MathTrig
    class ABS MathTrig
    class PI MathTrig
    class MINVERSE MathTrig
    class MULTINOMIAL MathTrig
    class RANDBETWEEN MathTrig
    class SEQUENCE MathTrig
    class DEGREES MathTrig
    class ASIN MathTrig
    class CSCH MathTrig
    class ROUNDUP MathTrig
    class LN MathTrig
    class TAN MathTrig
    class FACT MathTrig
    class COS MathTrig
    class ATAN2 MathTrig
    class GCD MathTrig
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in this category: 72
