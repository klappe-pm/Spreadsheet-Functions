---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: math & trig
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# SQRT

## SQRT Description

Calculates the square root of a positive number, returning the principal (positive) root. SQRT is fundamental for geometric calculations, statistical analysis, and mathematical models requiring root operations. Returns an error for negative inputs.

> [!f(x)] SQRT Syntax
>
> ```spreadsheets
> SQRT(number)
> ```
>
> **Parameters:**
> - `number` (required): A positive numeric value for which to calculate the square root

> [!f(x)] SQRT Examples
>
> ```spreadsheets
> // Basic square root
> SQRT(16) → 4
> 
> // Perfect square
> SQRT(25) → 5
> 
> // Decimal result
> SQRT(10) → 3.162278
> 
> // Fractional input
> SQRT(0.25) → 0.5
> 
> // Distance calculation
> SQRT((x2-x1)^2 + (y2-y1)^2) → Euclidean distance
> 
> // Standard deviation calculation
> SQRT(SUM((values - mean)^2) / (count - 1)) → sample standard deviation
> 
> // Variance to standard deviation
> SQRT(VAR.S(A1:A20)) → converts variance to standard deviation
> ```

## Use Cases

### [[Statistical analysis]]
- **Standard deviation**: Convert variance to standard deviation for measuring data dispersion in original units of measurement
- **Root mean square**: Calculate RMS values for electrical engineering, signal processing, and quality control applications
- **Confidence intervals**: Compute standard errors and confidence bounds using square root relationships in statistical formulas
- **Normalization**: Transform squared data back to linear scale for interpretable results in regression and correlation analysis
- **Sample size calculations**: Determine required sample sizes using square root relationships in power analysis and precision estimation

### [[Geometric calculations]]
- **Distance formulas**: Calculate Euclidean distances between points in 2D and 3D space for mapping and spatial analysis
- **Area and perimeter**: Find side lengths from areas, radii from areas, and other geometric dimension relationships
- **Pythagorean theorem**: Solve for unknown sides in right triangles for construction, navigation, and engineering applications
- **Circle calculations**: Determine radii from areas, chord lengths, and other circular measurements in architectural design
- **Volume calculations**: Calculate dimensions from volumes, surface areas, and other 3D geometric relationships

### [[Engineering calculations]]
- **Structural analysis**: Calculate deflections, stresses, and load distributions using square root relationships in beam theory
- **Electrical engineering**: Compute RMS voltages, impedances, and power calculations in AC circuit analysis
- **Physics applications**: Solve kinematic equations, wave calculations, and energy relationships requiring square root operations
- **Quality control**: Calculate control limits, process capability indices, and measurement uncertainties in manufacturing
- **Optimization problems**: Find optimal solutions in engineering design where square root relationships define constraints

## Related

### Similar Functions

- [[POWER]] - Raises numbers to any power, with POWER(x, 0.5) equivalent to SQRT(x) for positive numbers
- [[SQRTPI]] - Calculates square root of a number multiplied by π, useful in statistical and geometric calculations
- [[EXP]] - Exponential function, inverse relationship to natural logarithms, complementary to square root operations
- [[LOG]] - Logarithm functions, inverse relationship to exponential and power functions including square roots
- [[ABS]] - Absolute value function, often used with SQRT to handle negative inputs safely

## Statistical Calculation Functions

### [[VAR]]
Combines with SQRT to convert variance to standard deviation, essential for statistical analysis and data interpretation in original units.

```spreadsheets
// Population standard deviation
=SQRT(VAR.P(A1:A50))
// Converts population variance to standard deviation

// Sample standard deviation comparison
=SQRT(VAR.S(B1:B30)) & " vs " & STDEV.S(B1:B30)
// Shows manual calculation versus built-in function

// Coefficient of variation calculation
=SQRT(VAR.S(C1:C25)) / AVERAGE(C1:C25) * 100 & "% CV"
// Calculates relative variability using square root of variance
```

### [[SUMSQ]]
Works with SQRT for root mean square calculations, essential for electrical engineering, physics, and quality control applications.

```spreadsheets
// Root mean square (RMS) calculation
=SQRT(SUMSQ(D1:D20) / COUNT(D1:D20))
// Calculates RMS value using sum of squares

// Standard error calculation
=SQRT(SUMSQ(E1:E40 - AVERAGE(E1:E40)) / (COUNT(E1:E40) - 1)) / SQRT(COUNT(E1:E40))
// Combines SUMSQ with SQRT for standard error

// Quality control range calculation
=SQRT(SUMSQ(F1:F15)) & " root sum of squares for tolerance analysis"
// Uses SUMSQ and SQRT for engineering tolerance calculations
```

## Distance and Geometric Functions

### [[SUM]]
Partners with SQRT in distance calculations, particularly for Euclidean distance formulas and geometric analysis applications.

```spreadsheets
// 2D Euclidean distance
=SQRT(SUM((G1:G2 - H1:H2)^2))
// Calculates distance between two points

// 3D distance calculation
=SQRT(SUM((I1:I3 - J1:J3)^2))
// Extends to three-dimensional space

// Multi-dimensional distance
=SQRT(SUM((K1:K10 - L1:L10)^2)) & " units distance"
// Generalizes to n-dimensional space
```

### [[POWER]]
Complementary to SQRT for exponential and root calculations, essential for geometric scaling and mathematical transformations.

```spreadsheets
// Verification that SQRT equals POWER(x, 0.5)
=SQRT(M1) & " = " & POWER(M1, 0.5)
// Shows equivalence between square root and fractional power

// Geometric mean using SQRT and POWER
=SQRT(POWER(N1*N2*N3, 1/3))
// Alternative geometric mean calculation

// Scaling factor calculation
=SQRT(POWER(Target_Area / Current_Area, 1)) & " linear scaling factor"
// Calculates scaling factor from area ratio
```

## Error Handling Functions

### [[IF]]
Controls SQRT application for negative numbers, implementing error checking and conditional square root calculations for robust formulas.

```spreadsheets
// Safe square root with error checking
=IF(O1>=0, SQRT(O1), "Error: Negative input")
// Prevents errors from negative inputs

// Conditional distance calculation
=IF(AND(P1>=0, Q1>=0), SQRT(P1^2 + Q1^2), "Invalid coordinates")
// Ensures valid inputs for distance calculations

// Statistical validation with square root
=IF(R1>0, SQRT(R1), "Cannot calculate standard deviation")
// Validates positive variance before square root
```

### [[ABS]]
Often precedes SQRT to handle potentially negative inputs, ensuring valid square root calculations in all scenarios.

```spreadsheets
// Absolute value before square root
=SQRT(ABS(S1))
// Takes square root of absolute value for safety

// Distance calculation with absolute differences
=SQRT(SUM(ABS(T1:T3 - U1:U3)^2))
// Ensures positive differences before squaring

// Error magnitude calculation
=SQRT(ABS(V1 - W1)^2) & " absolute deviation"
// Combines ABS and SQRT for error measurement
```

## Mathematical Analysis Functions

### [[AVERAGE]]
Integrates with SQRT for root mean square calculations, standard error computations, and statistical measure transformations.

```spreadsheets
// Root mean square using AVERAGE
=SQRT(AVERAGE((X1:X25)^2))
// Calculates RMS using average of squares

// Standard error of the mean
=SQRT(VAR.S(Y1:Y30)) / SQRT(COUNT(Y1:Y30))
// Uses SQRT in denominator for standard error calculation

// Normalized root mean square error
=SQRT(AVERAGE((Z1:Z20 - AA1:AA20)^2)) / AVERAGE(ABS(Z1:Z20)) & " NRMSE"
// Combines SQRT and AVERAGE for normalized error metric
```

### [[COUNT]]
Works with SQRT in statistical formulas, particularly for sample size adjustments and degrees of freedom calculations.

```spreadsheets
// Sample standard deviation formula
=SQRT(SUM((BB1:BB40 - AVERAGE(BB1:BB40))^2) / (COUNT(BB1:BB40) - 1))
// Manual standard deviation calculation using COUNT

// Standard error calculation
=SQRT(VAR.S(CC1:CC50)) / SQRT(COUNT(CC1:CC50))
// Standard error using square root of sample size

// Confidence interval width
=1.96 * SQRT(VAR.S(DD1:DD25)) / SQRT(COUNT(DD1:DD25)) & " 95% CI half-width"
// Uses COUNT with SQRT for confidence interval calculations
```