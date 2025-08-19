---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: statistical
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# VAR

## VAR Description

Calculates the sample variance of a dataset, measuring the average squared deviation from the mean. Uses the n-1 denominator (Bessel's correction) for unbiased estimation of population variance, fundamental to statistical analysis as variance forms the basis for standard deviation, correlation, and advanced statistical procedures.

> [!f(x)] VAR Syntax
>
> ```spreadsheets
> VAR(number1, [number2], [number3], ...)
> VAR(range)
> VAR(range1, range2, ...)
> ```
>
> **Parameters:**
> - `number1` (required): First number, cell reference, or range containing sample data
> - `number2, number3, ...` (optional): Additional numbers, cell references, or ranges (up to 255 arguments)

> [!f(x)] VAR Examples
>
> ```spreadsheets
> // Basic variance calculation
> VAR(2, 4, 6, 8, 10) → 10
> 
> // Variance of a range
> VAR(A1:A25) → calculates sample variance for values in A1:A25
> 
> // Process capability analysis
> VAR(B2:B100) → 15.67 (variance in manufacturing measurements)
> 
> // Portfolio risk assessment
> VAR(C1:C60) → 0.0024 (variance of monthly returns)
> 
> // Quality control variance
> VAR(D2:D30, F2:F30) → combines multiple datasets for variance analysis
> ```

## Use Cases

### [[ANOVA and experimental design]]
- **Analysis of variance procedures**: Calculate within-group and between-group variances to test for significant differences across experimental conditions
- **Factorial experiment analysis**: Partition total variance into main effects and interaction components for comprehensive experimental interpretation
- **Randomized block design**: Assess treatment effects by comparing treatment variance against block and error variance components
- **Power analysis for experiments**: Use pilot variance estimates to determine required sample sizes for detecting meaningful effect sizes

### [[Portfolio and financial risk management]]  
- **Modern portfolio theory**: Calculate asset return variances for optimal portfolio construction and risk-return optimization analysis
- **Value at Risk calculations**: Use variance with normal distribution assumptions to estimate potential losses at specified confidence levels
- **Beta coefficient computation**: Calculate systematic risk by analyzing covariance between asset returns and market returns relative to market variance
- **Options pricing models**: Input variance parameters into Black-Scholes and binomial option pricing models for derivative valuation

### [[Quality control and process monitoring]]
- **Statistical process control**: Monitor process stability by tracking variance changes over time using control charts and capability studies
- **Measurement system analysis**: Assess measurement precision and accuracy by partitioning total variance into repeatability and reproducibility components
- **Design of experiments**: Use variance components to identify significant process factors and optimize operating conditions
- **Six Sigma methodology**: Calculate defect rates and process capability indices using variance to quantify process performance against specifications

## Related

### Similar Functions

- [[VAR.S]] - Identical to VAR, calculates sample variance using n-1 denominator for unbiased population variance estimation
- [[VAR.P]] - Calculates population variance using n denominator when analyzing complete populations rather than samples
- [[STDEV]] - Square root of VAR, provides variance in original measurement units for easier interpretation
- [[VARA]] - Includes text and logical values in calculation, treating text as 0 and FALSE as 0, TRUE as 1
- [[VARP]] - Legacy population variance function, equivalent to VAR.P for complete dataset analysis

## Variance Decomposition Functions

### [[STDEV]]
VAR is the foundation for STDEV calculation (STDEV = √VAR). VAR provides the mathematical basis while STDEV offers results in original measurement units for practical interpretation.

```spreadsheets
// Variance and standard deviation relationship
=VAR(A1:A30) & " (variance), " & STDEV(A1:A30) & " (SD), " & SQRT(VAR(A1:A30)) & " (√VAR)"
// Demonstrates mathematical relationship: "25.6 (variance), 5.06 (SD), 5.06 (√VAR)"

// Coefficient of variation using variance
=SQRT(VAR(B2:B40))/AVERAGE(B2:B40)*100 & "% CV"
// Calculates CV using variance: more computationally stable for large datasets

// Signal-to-noise ratio
="SNR: " & (AVERAGE(C1:C50)^2)/VAR(C1:C50)
// Uses variance to calculate signal-to-noise ratio in measurement analysis
```

### [[AVERAGE]]  
VAR measures spread around the mean calculated by AVERAGE. The mathematical relationship (variance = average of squared deviations from mean) makes them fundamental partners in statistical analysis.

```spreadsheets
// Manual variance calculation verification
=SUMPRODUCT((D2:D20-AVERAGE(D2:D20))^2)/(COUNT(D2:D20)-1)
// Verifies VAR function: should equal VAR(D2:D20)

// Standardized values (z-scores) preparation
=(E5-AVERAGE(E2:E30))/SQRT(VAR(E2:E30))
// Converts individual values to z-scores using variance

// Analysis of variance components
="Total variance: " & VAR(F1:F50) & ", Explained by mean: " & AVERAGE(F1:F50)^2
// Decomposes total variation into signal and noise components
```

## Statistical Testing Functions

### [[F.DIST]]
VAR enables F-test calculations for comparing variances between groups. Essential for ANOVA procedures and testing homogeneity of variance assumptions.

```spreadsheets
// F-test for equal variances
=VAR(G1:G25)/VAR(H1:H30)
// Calculates F-statistic for testing equality of two population variances

// ANOVA preparation: within-group variance
=(VAR(I2:I10)+VAR(J2:J10)+VAR(K2:K10))/3
// Pools within-group variances for one-way ANOVA analysis

// Bartlett's test preparation
="Pooled variance: " & ((COUNT(L1:L20)-1)*VAR(L1:L20)+(COUNT(M1:M25)-1)*VAR(M1:M25))/((COUNT(L1:L20)+COUNT(M1:M25)-2))
// Calculates pooled variance estimate for homogeneity testing
```

### [[CHISQ.TEST]]
VAR provides the denominator for chi-square goodness-of-fit tests and enables variance-based test statistics in categorical data analysis.

```spreadsheets
// Chi-square test statistic component
=(AVERAGE(N2:N30)-50)^2/VAR(N2:N30)
// Calculates standardized deviation for chi-square testing

// Variance stabilization assessment
=VAR(SQRT(O1:O40))
// Tests whether square root transformation stabilizes variance

// Heteroscedasticity detection
=VAR(P2:P25)/VAR(Q2:Q25)
// Compares variances across groups to detect heteroscedasticity
```

## Financial Analysis Functions

### [[COVAR]]
VAR serves as the denominator in correlation calculations (correlation = covariance / (SD1 × SD2)) and enables portfolio variance decomposition analysis.

```spreadsheets
// Correlation calculation using variance
=COVAR(R1:R50, S1:S50)/SQRT(VAR(R1:R50)*VAR(S1:S50))
// Manual correlation calculation using variance components

// Portfolio variance calculation
=VAR(T2:T60)+VAR(U2:U60)+2*COVAR(T2:T60, U2:U60)
// Two-asset portfolio variance: w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁₂ (assuming equal weights)

// Beta coefficient calculation
=COVAR(V1:V36, W1:W36)/VAR(W1:W36)
// Calculates systematic risk (beta) using market variance as denominator
```

### [[RSQ]]
VAR enables R-squared calculations by comparing explained variance to total variance, fundamental for regression analysis and model evaluation.

```spreadsheets
// R-squared manual calculation
=1-VAR(X2:X50-FORECAST.LINEAR(X2:X50, Y2:Y50, X2:X50))/VAR(X2:X50)
// Calculates coefficient of determination using variance components

// Explained variance ratio
=VAR(FORECAST.LINEAR(Z2:Z40, AA2:AA40, Z2:Z40))/VAR(Z2:Z40)
// Shows proportion of variance explained by regression model

// Model comparison using variance
="Model 1 error variance: " & VAR(BB2:BB30) & ", Model 2: " & VAR(CC2:CC30)
// Compares model performance using residual variance
```
