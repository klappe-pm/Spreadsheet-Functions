---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - statistical
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-17
  - - aliases
    - []
  - - tags
    - []
---
# COUNT

## COUNT Description

Counts the number of cells containing numeric values in a specified range or set of arguments. Ignores empty cells, text values, logical values, and error values, providing an accurate count of numerical data points for statistical analysis.

> [!f(x)] COUNT Syntax
>
> ```spreadsheets
> COUNT(value1, [value2], [value3], ...)
> COUNT(range)
> COUNT(range1, range2, ...)
> ```
>
> **Parameters:**
> - `value1` (required): First value, cell reference, or range to count
> - `value2, value3, ...` (optional): Additional values, cell references, or ranges (up to 255 arguments)

> [!f(x)] COUNT Examples
>
> ```spreadsheets
> // Basic count of numeric values
> COUNT(10, 20, 30, "text", TRUE) → 3
> 
> // Count values in a range
> COUNT(A1:A10) → counts numeric cells in range A1:A10
> 
> // Count across multiple ranges
> COUNT(B2:B10, D2:D10, F5) → combines counts from multiple sources
> 
> // Sample size for statistical analysis
> COUNT(C1:C50) → 45 (indicates 5 empty/non-numeric cells)
> 
> // Data completeness check
> COUNT(E2:E25) & " of " & ROWS(E2:E25) & " responses collected"
> ```

## Use Cases

### [[Sample size determination]]
- **Statistical power analysis**: Verify minimum sample sizes required for hypothesis testing and confidence interval calculations
- **Survey response tracking**: Monitor data collection progress by counting valid numerical responses versus target sample size
- **Clinical trial enrollment**: Track patient recruitment numbers and ensure adequate statistical power for medical research studies
- **Market research validation**: Confirm sufficient respondent counts across demographic segments for reliable statistical inference

### [[Data quality assessment]]  
- **Missing data analysis**: Identify gaps in datasets by comparing COUNT results with expected total observations
- **Data cleaning validation**: Verify that data transformation processes haven't inadvertently removed valid numerical entries
- **Import verification**: Confirm successful data imports by checking that numerical field counts match source system records
- **Real-time monitoring**: Track data stream completeness in automated reporting systems and trigger alerts for data quality issues

### [[Statistical significance testing]]
- **Degrees of freedom calculation**: Determine sample sizes for t-tests, chi-square tests, and ANOVA procedures requiring accurate counts
- **Power analysis preparation**: Calculate actual sample sizes achieved versus planned sizes to assess statistical power and effect detection capability
- **Correlation analysis setup**: Verify paired data completeness before computing correlation coefficients and regression models
- **Confidence interval computation**: Use counts to calculate standard errors and construct appropriate confidence bounds for population parameters

## Related

### Similar Functions

- [[COUNTA]] - Counts all non-empty cells including text and logical values, broader scope than COUNT for data presence verification
- [[COUNTIF]] - Counts cells meeting specific criteria, enabling conditional counting for segmented statistical analysis
- [[COUNTIFS]] - Counts with multiple criteria, essential for complex statistical filtering and cross-tabulation analysis  
- [[COUNTBLANK]] - Counts empty cells, complementary to COUNT for complete data coverage assessment
- [[COUNTUNIQUE]] - Counts distinct values, crucial for categorical data analysis and frequency distribution studies

## Statistical Validation Functions

### [[AVERAGE]]
Combined with COUNT to calculate reliable means and validate statistical assumptions. COUNT ensures adequate sample sizes while AVERAGE provides central tendency measures for population inference.

```spreadsheets
// Statistical summary with sample size
=AVERAGE(A1:A50) & " (n=" & COUNT(A1:A50) & ", " & 100*COUNT(A1:A50)/ROWS(A1:A50) & "% complete)"
// Returns: "76.3 (n=47, 94% complete)" showing mean, count, and data completeness

// Minimum sample size validation for t-test
=IF(COUNT(B2:B30)>=30, "Large sample: use z-test", "Small sample: use t-test")
// Determines appropriate statistical test based on sample size

// Confidence interval calculation
=AVERAGE(C1:C25) & " ± " & CONFIDENCE.NORM(0.05, STDEV(C1:C25), COUNT(C1:C25))
// Computes 95% confidence interval using sample count for degrees of freedom
```

### [[STDEV]]  
COUNT provides the denominator for standard deviation calculations and validates minimum sample requirements for reliable variance estimates in statistical inference procedures.

```spreadsheets
// Standard error calculation
=STDEV(D2:D40)/SQRT(COUNT(D2:D40))
// Uses count for standard error computation in hypothesis testing

// Coefficient of variation with sample size check
=IF(COUNT(E1:E20)>=10, STDEV(E1:E20)/AVERAGE(E1:E20)*100 & "% CV", "Insufficient data")
// Only calculates CV with adequate sample size

// Statistical power assessment
="n=" & COUNT(F1:F50) & ", Power=" & IF(COUNT(F1:F50)>=25, "Adequate", "Low")
// Evaluates whether sample size provides sufficient statistical power
```

## Data Completeness Functions

### [[SUM]]
COUNT validates SUM calculations by indicating how many values contributed to the total, essential for interpreting aggregate statistics and identifying data gaps in financial analysis.

```spreadsheets
// Revenue analysis with data quality check
=SUM(G2:G13) & " total revenue from " & COUNT(G2:G13) & " of " & ROWS(G2:G13) & " months"
// Shows total with data completeness: "150000 total revenue from 11 of 12 months"

// Average calculation verification
=IF(ABS(SUM(H1:H25)/COUNT(H1:H25)-AVERAGE(H1:H25))<0.01, "Calculation verified", "Data error")
// Confirms mathematical accuracy using count for division

// Weighted analysis preparation
="Valid data points: " & COUNT(I2:I50) & ", Missing: " & (ROWS(I2:I50)-COUNT(I2:I50))
// Quantifies available data for weighted statistical procedures
```

### [[MAX]]
COUNT provides context for extreme value analysis by showing sample sizes, crucial for understanding outlier significance and statistical distribution characteristics.

```spreadsheets
// Outlier analysis with sample context
=MAX(J1:J100) & " maximum from n=" & COUNT(J1:J100) & " observations"
// Shows extreme value with statistical context: "95.3 maximum from n=87 observations"

// Range analysis with data completeness
="Range: " & (MAX(K2:K30)-MIN(K2:K30)) & " from " & COUNT(K2:K30) & " complete records"
// Provides range statistics with sample size validation

// Percentile calculation readiness
=IF(COUNT(L1:L40)>=20, "Sample adequate for percentiles", "Need more data for reliable percentiles")
// Validates minimum sample size for percentile calculations
```

## Conditional Analysis Functions

### [[IF]]
COUNT enables sophisticated conditional logic for statistical decision-making, sample size validation, and automated quality control in data analysis workflows.

```spreadsheets
// Statistical test selection based on sample size
=IF(COUNT(M2:M50)>=30, "Use normal distribution", IF(COUNT(M2:M50)>=15, "Use t-distribution", "Non-parametric test"))
// Selects appropriate statistical test based on sample size

// Data quality gate for analysis
=IF(COUNT(N1:N25)/ROWS(N1:N25)>=0.8, "Proceed with analysis", "Collect more data")
// Requires 80% data completeness before statistical analysis

// Balanced sample validation
=IF(ABS(COUNT(O2:O26)-COUNT(P2:P26))<=2, "Balanced groups", "Unbalanced: adjust analysis")
// Ensures group sizes are similar for comparative statistical tests
```
