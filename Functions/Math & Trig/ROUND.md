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

# ROUND

## ROUND Description

Rounds a number to a specified number of decimal places using standard mathematical rounding rules (0.5 rounds up). Positive digit counts round to decimal places, negative counts round to tens, hundreds, etc., and zero rounds to the nearest integer.

> [!f(x)] ROUND Syntax
>
> ```spreadsheets
> ROUND(number, num_digits)
> ```
>
> **Parameters:**
> - `number` (required): The numeric value to round
> - `num_digits` (required): Number of digits to round to (positive for decimals, negative for places left of decimal, 0 for integers)

> [!f(x)] ROUND Examples
>
> ```spreadsheets
> // Basic decimal rounding
> ROUND(3.14159, 2) → 3.14
> 
> // Round to nearest integer
> ROUND(15.67, 0) → 16
> 
> // Round to tens place
> ROUND(1234, -1) → 1230
> 
> // Financial calculation rounding
> ROUND(1299.999, 2) → 1300.00
> 
> // Percentage calculation with precision
> ROUND(0.15789 * 100, 1) → 15.8
> 
> // Complex calculation with rounding
> ROUND(SUM(A1:A10) / COUNT(A1:A10), 3) → rounds average to 3 decimals
> 
> // Scientific notation rounding
> ROUND(0.000456789, 6) → 0.000457
> ```

## Use Cases

### [[Financial calculations]]
- **Currency precision**: Round monetary values to two decimal places for accurate financial reporting and eliminate floating-point arithmetic errors
- **Tax calculations**: Apply precise rounding rules required by tax authorities for deductions, withholdings, and liability computations
- **Interest calculations**: Round compound interest, loan payments, and investment returns to appropriate precision levels for financial statements
- **Budget allocations**: Round departmental budgets and expense allocations to nearest dollar or hundred for practical management
- **Price calculations**: Round product prices, discounts, and markups to standard pricing conventions and eliminate fractional cents

### [[Data analysis]]
- **Statistical precision**: Round calculated means, standard deviations, and correlation coefficients to appropriate significant figures for reporting
- **Survey analysis**: Round percentage results and confidence intervals to meaningful precision levels for presentation and interpretation
- **Performance metrics**: Round KPIs, ratios, and benchmarks to standard reporting precision while maintaining analytical accuracy
- **Scientific measurements**: Apply appropriate rounding rules for experimental data, maintaining measurement uncertainty principles
- **Quality control**: Round defect rates, tolerance measurements, and specification compliance to engineering standards

### [[Report generation]]
- **Dashboard displays**: Round metrics and KPIs to clean, readable numbers that fit display constraints and user comprehension
- **Executive summaries**: Present financial figures, growth rates, and performance indicators with appropriate precision for decision-making
- **Comparative analysis**: Round competitive benchmarks, market data, and trend analysis to consistent precision levels
- **Presentation formatting**: Ensure consistent number formatting across charts, tables, and summary statistics for professional appearance
- **Compliance reporting**: Apply required rounding conventions for regulatory filings, audit reports, and official documentation

## Related

### Similar Functions

- [[ROUNDUP]] - Always rounds away from zero, useful for conservative estimates and ensuring minimum values
- [[ROUNDDOWN]] - Always rounds toward zero, ideal for maximum calculations and pessimistic projections
- [[CEILING]] - Rounds up to nearest integer or specified multiple, perfect for packaging and capacity planning
- [[FLOOR]] - Rounds down to nearest integer or specified multiple, essential for resource allocation and constraints
- [[TRUNC]] - Removes decimal portion without rounding, preserving integer part for counting applications

## Number Formatting Functions

### [[TEXT]]
Converts ROUND results to formatted strings with specific decimal places, currency symbols, and presentation formats for professional reporting.

```spreadsheets
// Currency formatting with precise rounding
=TEXT(ROUND(A1*1.08, 2), "$#,##0.00")
// Rounds to 2 decimals then formats as currency

// Percentage display with controlled precision
=TEXT(ROUND(B1/B2, 4), "0.00%")
// Rounds to 4 decimals then displays as percentage

// Scientific notation with rounded precision
=TEXT(ROUND(C1, 6), "0.000000E+00")
// Rounds to 6 decimals then formats in scientific notation
```

### [[FIXED]]
Formats ROUND results as text with specified decimal places, providing consistent presentation alongside numerical rounding precision.

```spreadsheets
// Financial report formatting
=FIXED(ROUND(SUM(Revenue), -3), 0) & "K"
// Rounds to nearest thousand then formats without decimals

// Measurement precision display
=FIXED(ROUND(D1*2.54, 2), 2) & " cm"
// Rounds centimeter conversion to 2 decimals with unit label

// Statistical report formatting
=FIXED(ROUND(STDEV(E1:E50), 3), 3) & " ±" & FIXED(ROUND(AVERAGE(E1:E50), 2), 2)
// Shows standard deviation and mean with appropriate precision
```

## Mathematical Calculation Functions

### [[SUM]]
Combines with ROUND for precise aggregate calculations, ensuring financial accuracy and eliminating cumulative floating-point errors in totals.

```spreadsheets
// Rounded sum for financial accuracy
=ROUND(SUM(F1:F20), 2)
// Sums values then rounds total to 2 decimal places

// Individual rounding versus total rounding comparison
=SUM(ROUND(G1:G10, 2)) & " vs " & ROUND(SUM(G1:G10), 2)
// Shows difference between rounding each item versus rounding the sum

// Cumulative rounding for progressive calculations
=ROUND(SUM(H1:H5) * 1.0825, 2)
// Applies tax calculation with precise rounding
```

### [[AVERAGE]]
Works with ROUND to provide precise mean calculations, essential for statistical reporting and performance metrics with appropriate significant figures.

```spreadsheets
// Statistical precision in averaging
=ROUND(AVERAGE(I1:I25), 3)
// Calculates mean and rounds to 3 decimal places

// Grade point average with standard precision
=ROUND(AVERAGE(J2:J15), 2) & " GPA"
// Rounds GPA calculation to hundredths place

// Performance metric with confidence display
=ROUND(AVERAGE(K1:K100), 1) & " ±" & ROUND(STDEV(K1:K100)/SQRT(COUNT(K1:K100)), 2)
// Shows rounded average with rounded standard error
```

## Conditional Logic Functions

### [[IF]]
Controls when ROUND is applied based on conditions, enabling context-sensitive precision and error handling in mathematical calculations.

```spreadsheets
// Conditional precision based on value magnitude
=IF(L1>1000, ROUND(L1, -1), ROUND(L1, 2))
// Rounds large numbers to tens, small numbers to cents

// Error-safe rounding with validation
=IF(ISNUMBER(M1), ROUND(M1, 2), "Invalid data")
// Only applies rounding to valid numeric values

// Tiered precision for different calculation types
=IF(N1="Currency", ROUND(O1, 2), IF(N1="Percentage", ROUND(O1*100, 1), ROUND(O1, 4)))
// Applies different precision rules based on data type
```

### [[MIN]]
Combines with ROUND for minimum value analysis with controlled precision, essential for threshold comparisons and boundary calculations.

```spreadsheets
// Minimum threshold with financial precision
=ROUND(MIN(P1:P30), 2)
// Finds minimum value and rounds to currency precision

// Performance floor analysis
="Minimum Performance: " & ROUND(MIN(Q1:Q20), 1) & " vs Target: " & ROUND(R1, 1)
// Compares rounded minimum to rounded target

// Quality control lower bound
=IF(ROUND(MIN(S1:S50), 3) < 0.95, "Below standard", "Acceptable")
// Applies quality threshold with precise rounding
```

## Precision Control Functions

### [[ABS]]
Works with ROUND for absolute value calculations with controlled precision, essential for variance analysis and error measurement.

```spreadsheets
// Variance analysis with precise rounding
=ROUND(ABS(Actual - Budget), 2)
// Calculates absolute variance rounded to cents

// Statistical deviation measurement
=ROUND(ABS(T1 - AVERAGE(T1:T20)), 4)
// Measures deviation from mean with 4-decimal precision

// Quality control tolerance checking
=ROUND(ABS(U1 - Target_Value) / Target_Value * 100, 2) & "% deviation"
// Calculates percentage deviation with 2-decimal precision
```