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

# NORM.INV

## NORM.INV Description

Calculates the inverse of the normal cumulative distribution, returning the x-value for a given probability, mean, and standard deviation. The inverse function of NORM.DIST, essential for finding critical values, percentiles, confidence intervals, and control limits in quality control and statistical analysis.

> [!f(x)] NORM.INV Syntax
>
> ```spreadsheets
> NORM.INV(probability, mean, standard_dev)
> ```
>
> **Parameters:**
> - `probability` (required): Probability value between 0 and 1 (exclusive)
> - `mean` (required): Arithmetic mean (center) of the normal distribution
> - `standard_dev` (required): Standard deviation (spread) of the distribution (must be positive)

> [!f(x)] NORM.INV Examples
>
> ```spreadsheets
> // 95th percentile (top 5%) for standard normal
> NORM.INV(0.95, 0, 1) → 1.645 (95th percentile z-score)
> 
> // Upper specification limit for 99% yield
> NORM.INV(0.99, 100, 5) → 111.63 (only 1% exceed this value)
> 
> // Control chart upper control limit
> NORM.INV(0.9987, 50, 3) → 59.0 (3-sigma upper limit)
> 
> // Quality target for 90% compliance
> NORM.INV(0.9, 75, 10) → 87.82 (90th percentile value)
> 
> // Risk management: 5% Value-at-Risk
> NORM.INV(0.05, 10000, 2000) → 6710.2 (5% worst-case scenario)
> ```

## Use Cases

### [[Quality control and process design]]
- **Control chart limits**: Calculate upper and lower control limits using process mean and standard deviation for statistical process control
- **Specification setting**: Determine appropriate specification limits to achieve target defect rates and process capability indices
- **Process capability analysis**: Set realistic process targets based on natural variation and desired yield percentages
- **Acceptance criteria**: Design quality gates and inspection thresholds for manufacturing and service processes

### [[Risk management and financial modeling]]
- **Value at Risk (VaR) calculation**: Determine portfolio loss thresholds at specified confidence levels for risk reporting
- **Capital adequacy**: Calculate required capital reserves based on risk tolerance and loss distribution assumptions
- **Stress testing scenarios**: Generate critical values for worst-case scenario planning and regulatory compliance
- **Performance benchmarking**: Set performance targets and thresholds based on historical volatility and return distributions

### [[Statistical analysis and research]]
- **Confidence interval construction**: Calculate critical values for confidence intervals at various significance levels
- **Hypothesis testing**: Determine critical regions and rejection thresholds for statistical significance testing
- **Sample size planning**: Calculate effect sizes needed for desired statistical power in experimental design
- **Percentile analysis**: Convert probability requirements into actual measurement values for reporting and target-setting

## Related

### Similar Functions

- [[NORM.DIST]] - Forward normal distribution function; NORM.INV reverses NORM.DIST calculations
- [[NORM.S.INV]] - Standard normal inverse (mean=0, std=1); simplified version of NORM.INV
- [[PERCENTILE]] - Sample-based percentile calculation; NORM.INV provides theoretical percentiles
- [[CONFIDENCE.NORM]] - Calculates confidence interval width using normal distribution assumptions
- [[STANDARDIZE]] - Converts values to z-scores; opposite transformation of NORM.S.INV

## Distribution Analysis Functions

### [[AVERAGE]]
NORM.INV uses sample mean from AVERAGE as the distribution center, enabling calculation of percentiles and control limits based on actual process data.

```spreadsheets
// Process control limits using sample statistics
="UCL: " & NORM.INV(0.9987, AVERAGE(A2:A50), STDEV(A2:A50))
// Calculates upper control limit (3-sigma) using sample mean and standard deviation

// Performance targets based on historical data
="Top 10% threshold: " & NORM.INV(0.9, AVERAGE(B1:B30), STDEV(B1:B30))
// Sets performance target at 90th percentile using observed statistics

// Quality specification using process capability
="USL for 99% yield: " & NORM.INV(0.99, AVERAGE(C2:C40), STDEV(C2:C40))
// Designs upper specification limit for target defect rate
```

### [[STDEV]]
NORM.INV requires standard deviation from STDEV to determine the spread parameter, essential for calculating meaningful percentiles and critical values.

```spreadsheets
// Control chart implementation
="LCL: " & NORM.INV(0.0013, AVERAGE(D1:D25), STDEV(D1:D25))
="UCL: " & NORM.INV(0.9987, AVERAGE(D1:D25), STDEV(D1:D25))
// Creates symmetrical control limits using 3-sigma boundaries

// Process capability targets
="Cp=1.33 requires USL≥" & NORM.INV(0.99, AVERAGE(E2:E35), STDEV(E2:E35))
// Calculates specification limit needed for desired process capability

// Risk assessment threshold
="99% confidence limit: " & NORM.INV(0.99, AVERAGE(F1:F40), STDEV(F1:F40))
// Sets risk threshold using observed process variation
```

## Inverse Distribution Functions

### [[NORM.DIST]]
NORM.INV and NORM.DIST are mathematical inverses. NORM.INV finds x-values for probabilities, while NORM.DIST finds probabilities for x-values.

```spreadsheets
// Inverse relationship verification
=NORM.DIST(NORM.INV(G5, AVERAGE(G1:G20), STDEV(G1:G20)), AVERAGE(G1:G20), STDEV(G1:G20), TRUE)
// Should return original probability G5, demonstrating perfect inverse relationship

// Round-trip validation
="Original: " & H5 & ", Round-trip: " & NORM.INV(NORM.DIST(H5, AVERAGE(H1:H30), STDEV(H1:H30), TRUE), AVERAGE(H1:H30), STDEV(H1:H30))
// Validates inverse function accuracy for quality assurance

// Critical value calculation with verification
="Critical value: " & NORM.INV(0.05, AVERAGE(I2:I25), STDEV(I2:I25)) & ", P-value: " & NORM.DIST(NORM.INV(0.05, AVERAGE(I2:I25), STDEV(I2:I25)), AVERAGE(I2:I25), STDEV(I2:I25), TRUE)
// Shows critical value and verifies it produces correct probability
```

### [[PERCENTILE]]
NORM.INV provides theoretical percentiles assuming normal distribution, while PERCENTILE calculates actual percentiles from sample data.

```spreadsheets
// Theoretical vs empirical percentile comparison
="Theoretical 75th: " & NORM.INV(0.75, AVERAGE(J1:J50), STDEV(J1:J50)) & ", Actual 75th: " & PERCENTILE(J1:J50, 0.75)
// Compares normal distribution assumption with actual data distribution

// Distribution fit assessment
=IF(ABS(NORM.INV(0.5, AVERAGE(K2:K40), STDEV(K2:K40)) - PERCENTILE(K2:K40, 0.5)) < 0.1*STDEV(K2:K40), "Normal fit good", "Check distribution")
// Tests if data follows normal distribution by comparing median values

// Quality control comparison
="Spec based on normal: " & NORM.INV(0.99, AVERAGE(L1:L35), STDEV(L1:L35)) & ", Spec based on data: " & PERCENTILE(L1:L35, 0.99)
// Compares specification limits from theoretical vs empirical approaches
```

## Statistical Testing Functions

### [[CONFIDENCE.NORM]]
NORM.INV calculates the critical values needed for confidence interval construction, working with CONFIDENCE.NORM to set interval boundaries.

```spreadsheets
// Manual confidence interval calculation
="95% CI: " & AVERAGE(M1:M20) & " ± " & (NORM.INV(0.975, 0, 1) * STDEV(M1:M20)/SQRT(COUNT(M1:M20)))
// Constructs confidence interval using normal inverse for critical value

// Confidence interval validation
="Lower bound: " & (AVERAGE(N2:N30) - NORM.INV(0.975, 0, 1) * STDEV(N2:N30)/SQRT(COUNT(N2:N30)))
="Upper bound: " & (AVERAGE(N2:N30) + NORM.INV(0.975, 0, 1) * STDEV(N2:N30)/SQRT(COUNT(N2:N30)))
// Creates explicit upper and lower confidence bounds

// Sample size determination
="n required for ±2 margin: " & CEILING((NORM.INV(0.975, 0, 1) * STDEV(O1:O25) / 2)^2, 1)
// Calculates sample size needed for desired confidence interval width
```

### [[Z.TEST]]
NORM.INV provides critical values for z-test decisions, enabling manual hypothesis testing and p-value interpretation.

```spreadsheets
// Critical value for one-tailed test
="Critical value (α=0.05): " & NORM.INV(0.95, 0, 1) & ", Test statistic: " & (AVERAGE(P2:P35)-100)/(STDEV(P2:P35)/SQRT(COUNT(P2:P35)))
// Compares calculated test statistic with critical value

// Two-tailed test boundaries
="Reject if |z| > " & ABS(NORM.INV(0.025, 0, 1)) & ", z = " & ABS((AVERAGE(Q1:Q40)-50)/(STDEV(Q1:Q40)/SQRT(COUNT(Q1:Q40))))
// Sets rejection region boundaries for two-tailed hypothesis test

// Power analysis critical value
="Power = " & 1-NORM.DIST(NORM.INV(0.95, 0, 1) - (110-100)/(STDEV(R2:R30)/SQRT(COUNT(R2:R30))), 0, 1, TRUE)
// Calculates statistical power using critical value from NORM.INV
```

## Commonly Used With Functions Examples

### Quality Control and Process Management
```spreadsheets
// Complete control chart setup
="LCL: " & NORM.INV(0.0013, AVERAGE(A2:A50), STDEV(A2:A50)) & 
", Center: " & AVERAGE(A2:A50) & 
", UCL: " & NORM.INV(0.9987, AVERAGE(A2:A50), STDEV(A2:A50))
// Creates comprehensive control chart limits with center line

// Process capability specification
="For Cpk=1.33, set USL=" & NORM.INV(0.99, AVERAGE(B1:B30), STDEV(B1:B30)) & 
" and LSL=" & NORM.INV(0.01, AVERAGE(B1:B30), STDEV(B1:B30))
// Designs specification limits for target process capability
```

### Risk Assessment and Financial Planning
```spreadsheets
// Value-at-Risk calculation with confidence levels
="1% VaR: " & NORM.INV(0.01, AVERAGE(C2:C40), STDEV(C2:C40)) & 
", 5% VaR: " & NORM.INV(0.05, AVERAGE(C2:C40), STDEV(C2:C40))
// Calculates multiple VaR thresholds for risk management

// Performance target setting
="Target for top 25%: " & NORM.INV(0.75, AVERAGE(D1:D35), STDEV(D1:D35)) & 
" (based on " & COUNT(D1:D35) & " historical observations)"
// Sets performance targets based on historical distribution
```

### Statistical Analysis and Research
```spreadsheets
// Hypothesis testing decision framework
=IF((E5-100)/(STDEV(E1:E25)/SQRT(COUNT(E1:E25))) > NORM.INV(0.95, 0, 1), 
"Reject H0 at α=0.05", "Fail to reject H0")
// Makes hypothesis test decision using critical value comparison

// Confidence interval with interpretation
="Mean estimate: " & AVERAGE(F2:F30) & " ±" & 
NORM.INV(0.975, 0, 1) * STDEV(F2:F30)/SQRT(COUNT(F2:F30)) & 
" (95% CI)"
// Creates interpretable confidence interval statement
```
