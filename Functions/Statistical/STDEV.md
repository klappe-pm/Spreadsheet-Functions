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
# STDEV

## STDEV Description

Calculates the sample standard deviation of a dataset, measuring the amount of variation or dispersion from the mean. Uses the n-1 denominator (Bessel's correction) for unbiased estimation of population standard deviation from sample data, making it essential for inferential statistics.

> [!f(x)] STDEV Syntax
>
> ```spreadsheets
> STDEV(number1, [number2], [number3], ...)
> STDEV(range)
> STDEV(range1, range2, ...)
> ```
>
> **Parameters:**
> - `number1` (required): First number, cell reference, or range containing sample data
> - `number2, number3, ...` (optional): Additional numbers, cell references, or ranges (up to 255 arguments)

> [!f(x)] STDEV Examples
>
> ```spreadsheets
> // Basic standard deviation calculation
> STDEV(10, 15, 20, 25, 30) → 7.91
> 
> // Standard deviation of a range
> STDEV(A1:A20) → calculates sample SD for values in A1:A20
> 
> // Quality control analysis
> STDEV(B2:B50) → 2.34 (process variation measurement)
> 
> // Financial risk assessment
> STDEV(C1:C12) → 0.085 (monthly return volatility)
> 
> // Multiple range calculation
> STDEV(D2:D10, F2:F10, H5) → combines data from multiple sources
> ```

## Use Cases

### [[Quality control and process variation]]
- **Manufacturing tolerance analysis**: Monitor production consistency by tracking standard deviations of product dimensions against specification limits
- **Six Sigma process improvement**: Calculate process capability indices (Cp, Cpk) using standard deviation to identify improvement opportunities
- **Laboratory testing reliability**: Assess measurement precision by analyzing standard deviations of replicate test results across different conditions
- **Service delivery consistency**: Monitor customer service metrics like response times to maintain consistent quality standards

### [[Financial risk analysis]]  
- **Portfolio volatility measurement**: Calculate investment risk by analyzing standard deviations of historical returns across different time periods
- **Value at Risk (VaR) calculations**: Use standard deviation with normal distribution assumptions to estimate potential portfolio losses
- **Credit risk assessment**: Analyze payment timing variability and default probability distributions for loan portfolio management
- **Currency exchange rate analysis**: Measure foreign exchange volatility to inform hedging strategies and international business decisions

### [[Statistical inference and hypothesis testing]]
- **Confidence interval construction**: Calculate margins of error using standard deviation and appropriate critical values for population parameter estimation
- **Sample size determination**: Use expected standard deviations to calculate required sample sizes for desired statistical power in experimental design
- **Outlier detection and analysis**: Identify data points beyond 2-3 standard deviations from the mean for data quality assessment
- **Comparative analysis preparation**: Calculate pooled standard deviations for two-sample t-tests and analysis of variance procedures

## Related

### Similar Functions

- [[STDEV.S]] - Identical to STDEV, calculates sample standard deviation using n-1 denominator for unbiased population estimates
- [[STDEV.P]] - Calculates population standard deviation using n denominator when analyzing complete populations rather than samples
- [[VAR]] - Calculates sample variance (STDEV squared), fundamental measure of spread used in advanced statistical procedures
- [[STDEVA]] - Includes text and logical values in calculation, useful when non-numeric data represents meaningful variation
- [[STDEVP]] - Legacy population standard deviation function, equivalent to STDEV.P for complete dataset analysis

## Variability Measurement Functions

### [[AVERAGE]]
STDEV measures spread around the mean calculated by AVERAGE. Together they provide complete distributional summary - central tendency and dispersion - essential for statistical description and inference.

```spreadsheets
// Complete statistical summary
=AVERAGE(A1:A30) & " ± " & STDEV(A1:A30) & " (mean ± 1 SD)"
// Returns: "75.2 ± 8.4 (mean ± 1 SD)" showing central tendency and spread

// Coefficient of variation for relative comparison
=STDEV(B2:B25)/AVERAGE(B2:B25)*100 & "% CV"
// Shows relative variability: "12.3% CV" for comparing datasets with different scales

// Normal distribution description
="68% of data falls between " & (AVERAGE(C1:C40)-STDEV(C1:C40)) & " and " & (AVERAGE(C1:C40)+STDEV(C1:C40))
// Describes normal distribution properties using empirical rule
```

### [[COUNT]]  
COUNT validates STDEV calculations by showing sample size, crucial for determining statistical significance and reliability of standard deviation estimates in inferential procedures.

```spreadsheets
// Standard error calculation
=STDEV(D2:D50)/SQRT(COUNT(D2:D50))
// Calculates standard error of the mean for confidence interval construction

// Sample size adequacy check
=IF(COUNT(E1:E25)>=15, STDEV(E1:E25), "Need larger sample for reliable SD")
// Ensures adequate sample size for stable standard deviation estimates

// Degrees of freedom calculation
="Standard deviation: " & STDEV(F2:F30) & " (df=" & (COUNT(F2:F30)-1) & ")"
// Shows SD with degrees of freedom for statistical test preparation
```

## Distribution Analysis Functions

### [[MAX]]
Combined with STDEV to assess data range and identify outliers. MAX shows extreme values while STDEV provides context for determining if these values are statistically unusual.

```spreadsheets
// Outlier detection using z-score
=IF((MAX(G1:G40)-AVERAGE(G1:G40))/STDEV(G1:G40)>3, "Outlier detected", "Normal variation")
// Identifies outliers more than 3 standard deviations from mean

// Range-to-standard deviation ratio
=(MAX(H2:H30)-MIN(H2:H30))/STDEV(H2:H30)
// Assesses data distribution shape - ratio of ~6 suggests normal distribution

// Quality control limits
="UCL: " & (AVERAGE(I1:I25)+3*STDEV(I1:I25)) & ", LCL: " & (AVERAGE(I1:I25)-3*STDEV(I1:I25))
// Sets statistical process control limits at ±3 standard deviations
```

### [[MIN]]
Works with STDEV to establish complete distributional bounds and assess symmetry. MIN combined with STDEV helps identify skewness and distribution characteristics.

```spreadsheets
// Distribution symmetry assessment
=IF(ABS((AVERAGE(J2:J35)-MEDIAN(J2:J35))/STDEV(J2:J35))<0.5, "Symmetric", "Skewed")
// Uses standard deviation to normalize mean-median difference for skewness detection

// Lower control limit calculation
=MAX(0, AVERAGE(K1:K20)-3*STDEV(K1:K20))
// Ensures lower control limit doesn't go below zero in quality control

// Data transformation assessment
="Original SD: " & STDEV(L2:L40) & ", Log SD: " & STDEV(LN(L2:L40))
// Compares variability before and after log transformation
```

## Statistical Testing Functions

### [[CONFIDENCE.NORM]]
STDEV provides the variability measure needed for confidence interval calculations. Together they construct interval estimates for population parameters from sample data.

```spreadsheets
// 95% confidence interval for population mean
=AVERAGE(M1:M50) & " ± " & CONFIDENCE.NORM(0.05, STDEV(M1:M50), COUNT(M1:M50))
// Constructs confidence interval using sample standard deviation

// Margin of error calculation
="Margin of error: ±" & 1.96*STDEV(N2:N100)/SQRT(COUNT(N2:N100))
// Calculates margin of error for large sample confidence intervals

// Required sample size for desired precision
="Need n=" & CEILING((1.96*STDEV(O1:O30)/0.5)^2, 1) & " for ±0.5 margin of error"
// Estimates required sample size using pilot standard deviation
```

### [[T.INV]]
STDEV enables t-distribution calculations for small sample inference. Critical for hypothesis testing and confidence intervals when population standard deviation is unknown.

```spreadsheets
// t-distribution confidence interval
=AVERAGE(P2:P25) & " ± " & T.INV(0.025, COUNT(P2:P25)-1)*STDEV(P2:P25)/SQRT(COUNT(P2:P25))
// Constructs t-based confidence interval using sample standard deviation

// t-statistic calculation for hypothesis test
=(AVERAGE(Q1:Q20)-100)/(STDEV(Q1:Q20)/SQRT(COUNT(Q1:Q20)))
// Calculates t-statistic for testing if mean equals 100

// Statistical power assessment
=IF(STDEV(R2:R30)<5, "High power", "Low power - large variability reduces detection ability")
// Assesses whether standard deviation allows adequate statistical power
```
