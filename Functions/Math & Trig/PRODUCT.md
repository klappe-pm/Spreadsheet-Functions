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

# PRODUCT

## PRODUCT Description

Multiplies all numbers in a range or list of arguments, returning their mathematical product. Ignores empty cells, text, and logical values, making it ideal for compound calculations, growth rates, and probability computations.

> [!f(x)] PRODUCT Syntax
>
> ```spreadsheets
> PRODUCT(number1, [number2], [number3], ...)
> PRODUCT(range)
> PRODUCT(range1, range2, ...)
> ```
>
> **Parameters:**
> - `number1` (required): First number, cell reference, or range to multiply
> - `number2, number3, ...` (optional): Additional numbers, cell references, or ranges (up to 255 arguments)

> [!f(x)] PRODUCT Examples
>
> ```spreadsheets
> // Basic multiplication of numbers
> PRODUCT(2, 3, 4, 5) → 120
> 
> // Product of a range
> PRODUCT(A1:A5) → multiplies all values in range A1:A5
> 
> // Mixed arguments with ranges and numbers
> PRODUCT(B2:B6, 1.1, C8) → multiplies range B2:B6 by 1.1 and cell C8
> 
> // Compound growth calculation
> PRODUCT(1.05, 1.03, 1.07, 1.02) → 1.1832 (cumulative growth)
> 
> // Probability calculation
> PRODUCT(0.9, 0.85, 0.92) → 0.7038 (combined probability)
> ```

## Use Cases

### [[Financial calculations]]
- **Compound growth analysis**: Calculate cumulative returns over multiple periods for investment performance tracking
- **Discount calculations**: Apply sequential discounts to determine final pricing in complex promotional scenarios
- **Interest rate compounding**: Compute compound interest effects over multiple time periods with varying rates
- **Portfolio performance**: Track multiplicative effects of returns across different asset classes and time periods

### [[Probability and statistics]]  
- **Joint probability**: Calculate probability of multiple independent events occurring simultaneously
- **Reliability analysis**: Determine system reliability when multiple components must all function correctly
- **Quality control**: Compute overall yield rates when products pass through multiple quality checkpoints
- **Statistical modeling**: Generate compound probability distributions for risk assessment and forecasting

### [[Engineering and science]]
- **Scale factor calculations**: Apply multiple scaling factors in engineering design and manufacturing processes
- **Unit conversions**: Perform multi-step unit conversions involving several multiplicative conversion factors
- **Amplification ratios**: Calculate total gain in electronic circuits with multiple amplification stages
- **Chemical reactions**: Compute reaction rates and equilibrium constants involving multiple rate constants

## Related

### Similar Functions

- [[SUM]] - Adds numbers instead of multiplying, complementary aggregation function for different mathematical operations
- [[GEOMEAN]] - Calculates geometric mean using the nth root of products, related to PRODUCT for average calculations
- [[POWER]] - Raises numbers to powers, often combined with PRODUCT for complex exponential calculations
- [[FACT]] - Calculates factorials (special case of products), useful for combinatorial calculations with PRODUCT
- [[SUMPRODUCT]] - Multiplies corresponding array elements then sums them, combining PRODUCT and SUM operations

## Statistical Functions

### [[GEOMEAN]]
Closely related to PRODUCT as geometric mean equals the nth root of the product of n numbers, useful for average growth rates and proportional analysis.

```spreadsheets
// Verify geometric mean calculation
=GEOMEAN(A1:A5) vs POWER(PRODUCT(A1:A5), 1/COUNT(A1:A5))
// Both formulas should yield identical results

// Average growth rate calculation
=GEOMEAN(B2:B13)-1
// Calculates average monthly growth rate from multiplicative factors

// Investment return analysis
=POWER(PRODUCT(1+C2:C10), 1/COUNT(C2:C10))-1
// Manual geometric mean calculation for average returns
```

### [[SUMPRODUCT]]
Combines multiplication and addition operations, often used alongside PRODUCT for complex weighted calculations and array operations.

```spreadsheets
// Weighted product calculation
=PRODUCT(A2:A6)^(1/SUMPRODUCT(B2:B6))
// Uses SUMPRODUCT for weight normalization in geometric calculations

// Portfolio value calculation
=SUMPRODUCT(D2:D10, E2:E10) + PRODUCT(F2:F5)*G2
// Combines weighted sum with multiplicative factor

// Compound interest with varying principals
=SUMPRODUCT(H2:H12, PRODUCT(I2:I12))
// Complex financial calculation combining both functions
```

## Arithmetic Functions

### [[POWER]]
Frequently combined with PRODUCT for exponential calculations, compound growth, and complex mathematical formulations involving both multiplication and exponentiation.

```spreadsheets
// Compound interest with varying rates and periods
=A1*PRODUCT(POWER(1+B2:B13, C2:C13))
// Principal A1 with different rates B2:B13 and periods C2:C13

// Scale factor with exponential growth
=PRODUCT(D2:D6)*POWER(E2, F2)
// Base product D2:D6 multiplied by exponential factor E2^F2

// Risk-adjusted return calculation
=POWER(PRODUCT(1+G2:G25), 1/COUNT(G2:G25))-1
// Combines PRODUCT with POWER for geometric mean return
```

### [[SQRT]]
Combined with PRODUCT for statistical calculations, especially standard deviations and geometric relationships involving square roots of products.

```spreadsheets
// Standard deviation of product
=SQRT(PRODUCT(A1:A10^2)/COUNT(A1:A10) - PRODUCT(A1:A10)^(2/COUNT(A1:A10)))
// Complex statistical formula combining SQRT and PRODUCT

// Geometric standard deviation
=SQRT(PRODUCT((B2:B20/GEOMEAN(B2:B20))^2)^(1/COUNT(B2:B20)))
// Calculates geometric standard deviation using PRODUCT

// Distance calculation in multi-dimensional space
=SQRT(PRODUCT(C2:C5^2))
// Euclidean distance using product of squared coordinates
```

## Commonly Used With Functions Examples

### PRODUCT with Conditional Logic
```spreadsheets
// Conditional compound growth
=IF(A2>0, PRODUCT(1+B2:B13), "No growth data")
// Only calculates product if base value is positive

// Selective multiplication based on criteria
=PRODUCT(IF(C2:C10>D2:D10, C2:C10, 1))
// Multiplies only values where C > D, using 1 for others
```

### PRODUCT with Financial Analysis
```spreadsheets
// Multi-year investment growth
=E2*PRODUCT((1+F2:F11)*(1-G2:G11))
// Initial investment E2 with returns F2:F11 and fees G2:G11

// Currency conversion chain
=H2*PRODUCT(I2:I5)
// Amount H2 converted through multiple currency rates I2:I5
```

### PRODUCT with Statistical Modeling
```spreadsheets
// Monte Carlo simulation component
=PRODUCT(RAND()^(1/J2:J6))
// Generates random values following specific distributions

// Reliability calculation
=PRODUCT(K2:K8)*100&"% system reliability"
// Calculates overall system reliability from component reliabilities
```
