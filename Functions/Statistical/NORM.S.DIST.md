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

# NORM.S.DIST

## NORM.S.DIST Description

Calculates the standard normal distribution probability for a given z-score (standardized value). Uses mean of 0 and standard deviation of 1, equivalent to NORM.DIST(z, 0, 1, cumulative). Essential for hypothesis testing, standardized scoring, quality control, and converting any normal distribution to the standard reference distribution.

> [!f(x)] NORM.S.DIST Syntax
>
> ```spreadsheets
> NORM.S.DIST(z, cumulative)
> ```
>
> **Parameters:**
> - `z` (required): Standardized value (z-score) for which to calculate the standard normal distribution
> - `cumulative` (required): TRUE for cumulative probability (CDF), FALSE for probability density (PDF)

> [!f(x)] NORM.S.DIST Examples
>
> ```spreadsheets
> // Probability below 1 standard deviation
> NORM.S.DIST(1, TRUE) → 0.8413 (84.13% below z=1)
> 
> // Probability density at mean (z=0)
> NORM.S.DIST(0, FALSE) → 0.3989 (height of standard normal curve at center)
> 
> // Two-tailed test p-value calculation
> 2 * (1 - NORM.S.DIST(1.96, TRUE)) → 0.05 (5% significance level)
> 
> // Quality control: probability beyond 3 sigma
> 1 - NORM.S.DIST(3, TRUE) → 0.0013 (0.13% beyond 3 standard deviations)
> 
> // Percentile rank for standardized scores
> NORM.S.DIST(0.67, TRUE) → 0.75 (75th percentile at z=0.67)
> ```

## Use Cases

### [[Hypothesis testing and statistical inference]]
- **Z-test p-values**: Calculate p-values for standardized test statistics in one-sample and two-sample z-tests
- **Critical region analysis**: Determine probabilities of Type I and Type II errors using standard normal reference distribution
- **Statistical significance**: Convert test statistics to p-values for hypothesis testing across different statistical procedures
- **Power analysis**: Calculate statistical power and effect sizes using standardized distributions for experimental design

### [[Quality control and Six Sigma]]
- **Process capability assessment**: Convert process measurements to sigma levels using standard normal probabilities
- **Defect rate calculation**: Determine expected defect rates for processes with known z-scores and sigma levels
- **Control chart analysis**: Calculate probabilities for control limit violations using standardized process measurements
- **Specification analysis**: Evaluate process performance relative to specification limits using standard normal distribution

### [[Standardized scoring and ranking]]
- **Educational assessment**: Convert test scores to percentile ranks using standard normal distribution properties
- **Performance evaluation**: Create standardized performance metrics that compare across different scales and populations
- **Benchmarking analysis**: Convert business metrics to standardized scores for cross-industry or cross-period comparisons
- **Risk assessment**: Standardize risk metrics for portfolio analysis and comparative risk evaluation

## Related

### Similar Functions

- [[NORM.DIST]] - General normal distribution; NORM.S.DIST is equivalent to NORM.DIST(z, 0, 1, cumulative)
- [[NORM.S.INV]] - Inverse standard normal; finds z-score for given probability (opposite of NORM.S.DIST)
- [[STANDARDIZE]] - Converts values to z-scores for use with NORM.S.DIST
- [[Z.TEST]] - Performs z-tests using standard normal distribution for hypothesis testing
- [[CONFIDENCE.NORM]] - Uses standard normal critical values for confidence interval construction

## Standardization Functions

### [[STANDARDIZE]]
STANDARDIZE converts raw values to z-scores that can be used directly with NORM.S.DIST for probability calculations.

```spreadsheets
// Convert raw score to probability using standardization
=NORM.S.DIST(STANDARDIZE(A5, AVERAGE(A1:A20), STDEV(A1:A20)), TRUE)
// Equivalent to NORM.DIST(A5, AVERAGE(A1:A20), STDEV(A1:A20), TRUE)

// Percentile rank calculation
="Score " & B5 & " is at " & NORM.S.DIST(STANDARDIZE(B5, AVERAGE(B1:B30), STDEV(B1:B30)), TRUE)*100 & " percentile"
// Shows what percentile a raw score represents using standardization

// Quality assessment using standardized scores
=IF(ABS(STANDARDIZE(C5, AVERAGE(C1:C25), STDEV(C1:C25))) > 2, "Outlier (p=" & 2*(1-NORM.S.DIST(ABS(STANDARDIZE(C5, AVERAGE(C1:C25), STDEV(C1:C25))), TRUE)) & ")", "Normal range")
// Identifies outliers using 2-sigma rule with probability calculation
```

### [[AVERAGE]]
AVERAGE provides the mean for standardization calculations, enabling conversion of any normal distribution to standard normal form.

```spreadsheets
// Manual standardization with probability calculation
=(D5-AVERAGE(D1:D40))/STDEV(D1:D40) & " z-score, " & NORM.S.DIST((D5-AVERAGE(D1:D40))/STDEV(D1:D40), TRUE)*100 & " percentile"
// Shows both z-score and percentile rank for a value

// Process capability using standardization
="Cpk = " & MIN((AVERAGE(E2:E30)-LSL)/(3*STDEV(E2:E30)), (USL-AVERAGE(E2:E30))/(3*STDEV(E2:E30))) & ", Defect rate = " & (1-NORM.S.DIST(MIN((AVERAGE(E2:E30)-LSL)/STDEV(E2:E30), (USL-AVERAGE(E2:E30))/STDEV(E2:E30)), TRUE))*1000000 & " PPM"
// Calculates process capability and defect rate using standard normal

// Performance comparison across groups
="Group performance z-score: " & (AVERAGE(F1:F20)-100)/15 & ", Better than " & NORM.S.DIST((AVERAGE(F1:F20)-100)/15, TRUE)*100 & "% of population"
// Compares group average to population using standard normal
```

## Standard Normal Distribution Functions

### [[NORM.S.INV]]
NORM.S.DIST and NORM.S.INV are inverse functions. NORM.S.DIST gives probability for z-score, NORM.S.INV gives z-score for probability.

```spreadsheets
// Inverse relationship verification
=NORM.S.INV(NORM.S.DIST(G5, TRUE))
// Should return original G5 value, demonstrating inverse relationship

// Critical value and probability validation
="Critical z = " & NORM.S.INV(0.975) & ", Two-tailed p = " & 2*(1-NORM.S.DIST(NORM.S.INV(0.975), TRUE))
// Shows critical value and validates it produces correct significance level

// Percentile to z-score to percentile conversion
="90th percentile z = " & NORM.S.INV(0.9) & ", Verification: " & NORM.S.DIST(NORM.S.INV(0.9), TRUE)*100 & " percentile"
// Demonstrates perfect inverse relationship between functions
```

### [[Z.TEST]]
NORM.S.DIST provides the theoretical foundation for Z.TEST calculations, enabling manual z-test p-value computation.

```spreadsheets
// Manual one-sample z-test
="Z-statistic: " & (AVERAGE(H1:H25)-100)/(STDEV(H1:H25)/SQRT(COUNT(H1:H25))) & ", P-value: " & 2*(1-NORM.S.DIST(ABS((AVERAGE(H1:H25)-100)/(STDEV(H1:H25)/SQRT(COUNT(H1:H25)))), TRUE))
// Calculates two-tailed p-value for testing if mean equals 100

// Z-test result interpretation
="Test result: " & IF(2*(1-NORM.S.DIST(ABS((AVERAGE(I2:I30)-50)/(STDEV(I2:I30)/SQRT(COUNT(I2:I30)))), TRUE)) < 0.05, "Reject H0", "Fail to reject H0") & " (p = " & 2*(1-NORM.S.DIST(ABS((AVERAGE(I2:I30)-50)/(STDEV(I2:I30)/SQRT(COUNT(I2:I30)))), TRUE)) & ")"
// Makes hypothesis test decision with p-value

// Power analysis using standard normal
="Power for detecting μ=105: " & 1-NORM.S.DIST(1.645-(105-100)/(STDEV(J1:J20)/SQRT(COUNT(J1:J20))), TRUE)
// Calculates statistical power for specific alternative hypothesis
```

## Statistical Testing Functions

### [[CONFIDENCE.NORM]]
NORM.S.DIST validates confidence interval coverage by showing the actual probability within intervals constructed using standard normal critical values.

```spreadsheets
// Confidence interval coverage verification
="95% CI coverage: " & (NORM.S.DIST(1.96, TRUE) - NORM.S.DIST(-1.96, TRUE))*100 & "%"
// Verifies that ±1.96 z-scores contain 95% of standard normal distribution

// Margin of error probability calculation
="Probability within ±" & K5 & " standard errors: " & (NORM.S.DIST(K5, TRUE) - NORM.S.DIST(-K5, TRUE))*100 & "%"
// Shows coverage probability for any margin of error in standard normal units

// Sample size and confidence relationship
="For 99% CI, z = ±" & ABS(NORM.S.INV(0.005)) & ", Coverage = " & (NORM.S.DIST(ABS(NORM.S.INV(0.005)), TRUE) - NORM.S.DIST(-ABS(NORM.S.INV(0.005)), TRUE))*100 & "%"
// Demonstrates relationship between confidence level and z-critical values
```

### [[IF]]
IF enables conditional standard normal calculations, error handling, and decision-making based on z-scores and probabilities.

```spreadsheets
// Conditional probability calculation with validation
=IF(ISNUMBER(L5), NORM.S.DIST(L5, TRUE), "Invalid z-score")
// Prevents errors when z-score input is not numeric

// Statistical significance decision
=IF(ABS((AVERAGE(M1:M30)-100)/(STDEV(M1:M30)/SQRT(COUNT(M1:M30)))) > 1.96, "Significant at α=0.05", "Not significant")
// Makes significance decision based on critical z-value

// Quality control alert system
=IF(ABS(STANDARDIZE(N5, AVERAGE(N1:N20), STDEV(N1:N20))) > 2, "OUT OF CONTROL - p=" & 2*(1-NORM.S.DIST(ABS(STANDARDIZE(N5, AVERAGE(N1:N20), STDEV(N1:N20))), TRUE)), "In control")
// Triggers quality alerts based on standard normal probabilities
```

## Commonly Used With Functions Examples

### Statistical Testing and Hypothesis Evaluation
```spreadsheets
// Complete z-test with interpretation
="Sample mean: " & AVERAGE(A1:A25) & ", Z-stat: " & ROUND((AVERAGE(A1:A25)-100)/(STDEV(A1:A25)/SQRT(COUNT(A1:A25))),3) & 
", P-value: " & ROUND(2*(1-NORM.S.DIST(ABS((AVERAGE(A1:A25)-100)/(STDEV(A1:A25)/SQRT(COUNT(A1:A25)))), TRUE)),4) & 
", Result: " & IF(2*(1-NORM.S.DIST(ABS((AVERAGE(A1:A25)-100)/(STDEV(A1:A25)/SQRT(COUNT(A1:A25)))), TRUE))<0.05,"Significant","Not significant")
// Comprehensive z-test results with statistical decision
```

### Quality Control and Process Analysis
```spreadsheets
// Six Sigma process assessment
="Process mean: " & AVERAGE(B2:B50) & "±" & STDEV(B2:B50) & 
", Sigma level: " & NORM.S.INV(1-0.000001) & 
", Current defect rate: " & ROUND((1-NORM.S.DIST((USL-AVERAGE(B2:B50))/STDEV(B2:B50), TRUE))*1000000,0) & " PPM"
// Evaluates process capability using standard normal distribution

// Control chart probability analysis
="Probability of exceeding UCL: " & ROUND((1-NORM.S.DIST(3, TRUE))*100,4) & "%" &
", Probability below LCL: " & ROUND(NORM.S.DIST(-3, TRUE)*100,4) & "%" &
", Expected false alarms: " & ROUND(2*(1-NORM.S.DIST(3, TRUE))*100,4) & "%"
// Calculates control chart error rates using 3-sigma limits
```

### Performance Ranking and Standardized Scoring
```spreadsheets
// Comprehensive percentile ranking
="Raw score: " & C5 & 
", Z-score: " & ROUND(STANDARDIZE(C5, AVERAGE(C1:C30), STDEV(C1:C30)),2) & 
", Percentile: " & ROUND(NORM.S.DIST(STANDARDIZE(C5, AVERAGE(C1:C30), STDEV(C1:C30)), TRUE)*100,1) & "%" &
", Performance: " & IF(STANDARDIZE(C5, AVERAGE(C1:C30), STDEV(C1:C30))>1,"Above Average",IF(STANDARDIZE(C5, AVERAGE(C1:C30), STDEV(C1:C30))>-1,"Average","Below Average"))
// Complete performance analysis with standardized interpretation
```
