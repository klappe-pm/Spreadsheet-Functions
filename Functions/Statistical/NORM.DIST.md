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
# NORM.DIST

## NORM.DIST Description

Calculates the normal distribution probability for a specified value, mean, and standard deviation. Returns either the cumulative distribution function (CDF) or probability density function (PDF) based on the cumulative parameter. Essential for hypothesis testing, quality control, risk analysis, and statistical modeling applications.

> [!f(x)] NORM.DIST Syntax
>
> ```spreadsheets
> NORM.DIST(x, mean, standard_dev, cumulative)
> ```
>
> **Parameters:**
> - `x` (required): Value for which to calculate the normal distribution
> - `mean` (required): Arithmetic mean (center) of the normal distribution
> - `standard_dev` (required): Standard deviation (spread) of the distribution (must be positive)
> - `cumulative` (required): TRUE for cumulative probability (CDF), FALSE for probability density (PDF)

> [!f(x)] NORM.DIST Examples
>
> ```spreadsheets
> // Cumulative probability (area under curve)
> NORM.DIST(85, 100, 15, TRUE) → 0.1587 (15.87% probability of x ≤ 85)
> 
> // Probability density (height of curve)
> NORM.DIST(100, 100, 15, FALSE) → 0.0266 (density at mean)
> 
> // Quality control probability
> NORM.DIST(2.5, 3.0, 0.2, TRUE) → 0.0062 (probability of defect)
> 
> // Standard normal distribution
> NORM.DIST(1.96, 0, 1, TRUE) → 0.975 (97.5% below 1.96 standard deviations)
> 
> // Manufacturing tolerance
> NORM.DIST(0.998, 1.000, 0.005, TRUE) → 0.3446 (34.46% below specification)
> ```

## Use Cases

### [[Quality control and Six Sigma analysis]]
- **Process capability studies**: Calculate probabilities of products falling within specification limits using process mean and standard deviation
- **Defect rate estimation**: Determine expected defect rates and sigma levels for manufacturing processes with normal distributions
- **Control chart analysis**: Calculate probabilities for control limit violations and out-of-control conditions in statistical process control
- **Acceptance sampling**: Design sampling plans by calculating probabilities of accepting or rejecting batches based on quality standards

### [[Risk management and financial modeling]]  
- **Value at Risk (VaR) calculations**: Estimate potential losses at specific confidence levels assuming normal distribution of returns
- **Portfolio optimization**: Calculate probabilities of portfolio returns falling within target ranges for asset allocation decisions
- **Credit risk assessment**: Model default probabilities and credit losses using normal distribution assumptions for loan portfolios
- **Option pricing support**: Provide probability calculations for Black-Scholes and other models requiring normal distribution inputs

### [[Hypothesis testing and statistical inference]]
- **Z-test calculations**: Calculate p-values and critical regions for hypothesis tests involving normally distributed test statistics
- **Confidence interval construction**: Determine probability coverage for confidence intervals using normal distribution properties
- **Sample size determination**: Calculate required sample sizes based on desired power and significance levels using normal approximations
- **Statistical significance testing**: Evaluate probability of observing test results under null hypothesis assumptions

## Related

### Similar Functions

- [[NORM.S.DIST]] - Standard normal distribution (mean=0, std=1), equivalent to NORM.DIST with standardized inputs
- [[NORM.INV]] - Inverse normal distribution, finds x-value for given probability (opposite of NORM.DIST cumulative)
- [[STANDARDIZE]] - Converts values to z-scores for use with standard normal distribution functions
- [[CONFIDENCE.NORM]] - Calculates confidence intervals using normal distribution properties
- [[Z.TEST]] - Performs z-tests using normal distribution for hypothesis testing procedures

## Distribution Analysis Functions

### [[AVERAGE]]
NORM.DIST uses the sample mean from AVERAGE as the distribution center parameter, essential for modeling real data with normal distribution assumptions.

```spreadsheets
// Process capability using sample statistics
=1-NORM.DIST(6.5, AVERAGE(A2:A50), STDEV(A2:A50), TRUE)+NORM.DIST(5.5, AVERAGE(A2:A50), STDEV(A2:A50), TRUE)
// Calculates probability of values falling within 5.5-6.5 range using sample mean

// Quality control probability assessment
="P(defect) = " & (1-NORM.DIST(AVERAGE(B1:B100)+3*STDEV(B1:B100), AVERAGE(B1:B100), STDEV(B1:B100), TRUE))*100 & "%"
// Estimates defect rate beyond 3-sigma limits using sample mean

// Performance probability analysis
="P(above average) = " & (1-NORM.DIST(AVERAGE(C2:C30), AVERAGE(C2:C30), STDEV(C2:C30), TRUE))*100 & "%"
// Always returns 50% as expected for normal distribution at mean
```

### [[STDEV]]  
NORM.DIST requires standard deviation from STDEV as the spread parameter, making them essential partners for normal distribution modeling of sample data.

```spreadsheets
// Probability of exceeding specification using sample SD
=1-NORM.DIST(105, AVERAGE(D1:D40), STDEV(D1:D40), TRUE)
// Calculates probability of exceeding upper specification limit

// Control limit probability
=NORM.DIST(AVERAGE(E2:E25)-2*STDEV(E2:E25), AVERAGE(E2:E25), STDEV(E2:E25), TRUE)
// Probability of falling below 2-sigma lower control limit (2.28%)

// Process sigma level calculation
="Sigma level: " & NORM.S.INV(1-0.000001) & " for " & 0.000001*100 & "% defect rate"
// Calculates sigma level corresponding to specific defect rates
```

## Probability Calculation Functions

### [[NORM.INV]]
NORM.DIST and NORM.INV are inverse functions. NORM.DIST gives probability for x-value, while NORM.INV gives x-value for probability.

```spreadsheets
// Inverse relationship verification
=NORM.INV(NORM.DIST(F5, AVERAGE(F1:F30), STDEV(F1:F30), TRUE), AVERAGE(F1:F30), STDEV(F1:F30))
// Should return original F5 value, demonstrating inverse relationship

// Critical value calculation
="95th percentile: " & NORM.INV(0.95, AVERAGE(G2:G40), STDEV(G2:G40))
// Finds value exceeded by only 5% of population

// Specification limit design
="USL for 1% defect rate: " & NORM.INV(0.99, AVERAGE(H1:H50), STDEV(H1:H50))
// Designs upper specification limit for target defect rate
```

### [[STANDARDIZE]]
STANDARDIZE converts values to z-scores for use with standard normal distribution, complementing NORM.DIST for standardized analysis.

```spreadsheets
// Z-score probability calculation
=NORM.DIST(STANDARDIZE(I5, AVERAGE(I2:I30), STDEV(I2:I30)), 0, 1, TRUE)
// Equivalent to NORM.DIST(I5, AVERAGE(I2:I30), STDEV(I2:I30), TRUE)

// Percentile rank calculation
=NORM.DIST(STANDARDIZE(J10, AVERAGE(J2:J40), STDEV(J2:J40)), 0, 1, TRUE)*100 & " percentile"
// Shows what percentile a specific value represents

// Standard score interpretation
="Z-score: " & STANDARDIZE(K15, AVERAGE(K2:K50), STDEV(K2:K50)) & ", Probability: " & NORM.S.DIST(STANDARDIZE(K15, AVERAGE(K2:K50), STDEV(K2:K50)), TRUE)
// Combines standardization with probability calculation
```

## Statistical Testing Functions

### [[CONFIDENCE.NORM]]
NORM.DIST validates confidence interval calculations by showing actual coverage probabilities for intervals constructed using normal distribution assumptions.

```spreadsheets
// Confidence interval coverage verification
=NORM.DIST(AVERAGE(L1:L25)+CONFIDENCE.NORM(0.05, STDEV(L1:L25), COUNT(L1:L25)), AVERAGE(L1:L25), STDEV(L1:L25)/SQRT(COUNT(L1:L25)), TRUE) - NORM.DIST(AVERAGE(L1:L25)-CONFIDENCE.NORM(0.05, STDEV(L1:L25), COUNT(L1:L25)), AVERAGE(L1:L25), STDEV(L1:L25)/SQRT(COUNT(L1:L25)), TRUE)
// Should return approximately 0.95 for 95% confidence interval

// Margin of error probability
="Probability within ±" & CONFIDENCE.NORM(0.05, STDEV(M2:M30), COUNT(M2:M30)) & ": " & NORM.DIST(AVERAGE(M2:M30)+CONFIDENCE.NORM(0.05, STDEV(M2:M30), COUNT(M2:M30)), AVERAGE(M2:M30), STDEV(M2:M30), TRUE) - NORM.DIST(AVERAGE(M2:M30)-CONFIDENCE.NORM(0.05, STDEV(M2:M30), COUNT(M2:M30)), AVERAGE(M2:M30), STDEV(M2:M30), TRUE)
// Shows actual probability coverage for confidence interval

// Critical region analysis
="P(Type I error) = " & 2*(1-NORM.DIST(1.96, 0, 1, TRUE)) & " for α=0.05 two-tailed test"
// Calculates actual Type I error probability for critical regions
```

### [[Z.TEST]]
NORM.DIST provides the theoretical foundation for Z.TEST calculations, enabling manual z-test computations and p-value verification.

```spreadsheets
// Manual z-test p-value calculation
=2*(1-NORM.DIST(ABS((AVERAGE(N1:N20)-50)/(STDEV(N1:N20)/SQRT(COUNT(N1:N20)))), 0, 1, TRUE))
// Calculates two-tailed p-value for testing if mean equals 50

// One-sample z-test verification
="Z-statistic: " & (AVERAGE(O2:O35)-100)/(STDEV(O2:O35)/SQRT(COUNT(O2:O35))) & ", P-value: " & 1-NORM.DIST((AVERAGE(O2:O35)-100)/(STDEV(O2:O35)/SQRT(COUNT(O2:O35))), 0, 1, TRUE)
// Manual calculation matching Z.TEST results

// Statistical power analysis
=1-NORM.DIST(1.645-(110-100)/(STDEV(P1:P30)/SQRT(COUNT(P1:P30))), 0, 1, TRUE)
// Calculates power for detecting mean difference of 10 units
```
