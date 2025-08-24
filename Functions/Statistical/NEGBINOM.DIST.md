---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- statistical
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- statistical
- excel
- sheets
---
# NEGBINOM.DIST

## NEGBINOM.DIST Description

Calculates the negative binomial distribution probability, which models the number of failures before achieving a specified number of successes in independent trials. Returns either the cumulative distribution function (CDF) or probability mass function (PMF). Essential for reliability analysis, quality control, and modeling waiting times for success events.

> [!f(x)] NEGBINOM.DIST Syntax
>
> ```spreadsheets
> NEGBINOM.DIST(number_f, number_s, probability_s, cumulative)
> ```
>
> **Parameters:**
> - `number_f` (required): Number of failures (non-negative integer)
> - `number_s` (required): Number of successes required (positive integer) 
> - `probability_s` (required): Probability of success on each trial (0 < p ≤ 1)
> - `cumulative` (required): TRUE for cumulative probability (CDF), FALSE for exact probability (PMF)

> [!f(x)] NEGBINOM.DIST Examples
>
> ```spreadsheets
> // Probability of exactly 5 failures before 3 successes
> NEGBINOM.DIST(5, 3, 0.4, FALSE) → 0.0552 (5.52% probability)
> 
> // Cumulative probability of 5 or fewer failures before 3 successes
> NEGBINOM.DIST(5, 3, 0.4, TRUE) → 0.6826 (68.26% cumulative probability)
> 
> // Quality control: defects before 10 good units
> NEGBINOM.DIST(15, 10, 0.95, TRUE) → 0.0037 (0.37% chance of ≤15 defects)
> 
> // Sales calls: rejections before 2 sales with 20% success rate
> NEGBINOM.DIST(8, 2, 0.2, FALSE) → 0.0655 (6.55% chance of exactly 8 rejections)
> 
> // Manufacturing: failures before 5 successes with 80% success rate
> NEGBINOM.DIST(3, 5, 0.8, TRUE) → 0.9437 (94.37% chance of ≤3 failures)
> ```

## Use Cases

### [[Quality control and reliability testing]]
- **Defect analysis**: Calculate probabilities of specific numbers of defective units before achieving target good units for quality assessment
- **Burn-in testing**: Model failure patterns during product testing phases to determine optimal testing durations and acceptance criteria
- **Reliability engineering**: Analyze component failure rates and estimate mean time between failures for maintenance scheduling
- **Acceptance sampling**: Design sampling plans based on negative binomial models for lot acceptance or rejection decisions

### [[Sales and marketing analytics]]
- **Conversion modeling**: Predict number of prospect contacts needed before achieving target conversions for resource planning
- **Customer acquisition**: Model lead qualification processes and estimate costs per acquisition based on success probabilities  
- **Campaign optimization**: Analyze trial-and-error marketing campaigns to optimize budget allocation and targeting strategies
- **Sales forecasting**: Predict call volumes and rejection rates needed to achieve quarterly sales targets with known conversion rates

### [[Medical and clinical trials]]
- **Patient recruitment**: Model enrollment challenges and predict timeline for achieving target sample sizes in clinical studies
- **Treatment efficacy**: Analyze adverse events before achieving therapeutic success for drug safety evaluation
- **Disease progression**: Model relapse patterns and remission periods for chronic disease management planning
- **Diagnostic testing**: Calculate false positive rates and testing sequences needed for accurate diagnosis confirmation

## Related

### Similar Functions

- [[BINOM.DIST]] - Models fixed number of trials with varying successes (opposite scenario of NEGBINOM.DIST)
- [[POISSON.DIST]] - Models number of events in fixed time period, useful when success rate is very low
- [[GEOMEAN]] - Calculates geometric mean, related to geometric distribution (special case where number_s = 1)
- [[HYPGEOM.DIST]] - Models sampling without replacement, different probability model than negative binomial
- [[GAMMA.DIST]] - Related continuous distribution that can approximate negative binomial for large parameters

## Probability Distribution Functions

### [[AVERAGE]]
NEGBINOM.DIST models distributions where the mean number of failures equals number_s * (1-probability_s) / probability_s, useful for validating observed failure rates.

```spreadsheets
// Expected failures calculation
="Expected failures before " & C2 & " successes: " & C2*(1-D2)/D2 & ", Observed: " & AVERAGE(E2:E20)
// Compares theoretical mean with observed average failures

// Validation of distribution parameters
=IF(ABS(AVERAGE(F1:F30) - G1*(1-H1)/H1) < 0.5, "Parameters valid", "Check distribution fit")
// Tests if observed data matches theoretical negative binomial mean

// Quality control parameter estimation
="Process p-value: " & G10/(G10+AVERAGE(H2:H25)) & " for " & G10 & " required successes"
// Estimates success probability from observed failure patterns
```

### [[STDEV]]
NEGBINOM.DIST has variance equal to number_s * (1-probability_s) / probability_s², making STDEV useful for validating distribution assumptions.

```spreadsheets
// Distribution variance validation
="Theoretical SD: " & SQRT(I2*(1-J2)/(J2^2)) & ", Observed SD: " & STDEV(K2:K30)
// Compares theoretical standard deviation with sample standard deviation

// Process variability assessment
=IF(STDEV(L1:L25) > 1.2*SQRT(M1*(1-N1)/(N1^2)), "High variability", "Normal variation")
// Flags processes with higher than expected variability

// Control limit calculation
="UCL: " & O2*(1-P2)/P2 + 3*SQRT(O2*(1-P2)/(P2^2))
// Calculates upper control limit using negative binomial properties
```

## Probability Analysis Functions

### [[COUNT]]
COUNT validates sample sizes for negative binomial analysis and ensures sufficient data for parameter estimation and goodness-of-fit testing.

```spreadsheets
// Sample size validation for parameter estimation
=IF(COUNT(Q1:Q50)>=30, "Sufficient for estimation", "Need more data")
// Ensures adequate sample size for reliable parameter estimation

// Data completeness check
="Sample size: " & COUNT(R2:R40) & ", Power: " & IF(COUNT(R2:R40)>=25, "Good", "Limited")
// Assesses statistical power based on sample size

// Comparative analysis preparation
="Group A: n=" & COUNT(S1:S20) & ", Group B: n=" & COUNT(T1:T20)
// Prepares sample size information for comparison testing
```

### [[IF]]
IF enables conditional negative binomial calculations based on parameter values, data validation, and business rules for decision-making.

```spreadsheets
// Conditional probability calculation
=IF(U5>0, NEGBINOM.DIST(U5, V5, W5, TRUE), "Invalid input")
// Prevents errors with invalid number of failures parameter

// Business rule application
=IF(NEGBINOM.DIST(X5, Y5, Z5, TRUE)>0.95, "Accept batch", "Continue testing")
// Makes quality control decisions based on probability thresholds

// Parameter range validation
=IF(AND(AA5>=0, BB5>0, CC5>0, CC5<=1), NEGBINOM.DIST(AA5, BB5, CC5, TRUE), "Check parameters")
// Validates all parameters before calculation to prevent function errors
```

## Statistical Testing Functions

### [[CHISQ.TEST]]
CHISQ.TEST validates whether observed failure patterns follow the negative binomial distribution through goodness-of-fit testing.

```spreadsheets
// Goodness-of-fit test setup
="Expected frequency: " & DD5*NEGBINOM.DIST(EE5, FF5, GG5, FALSE)
// Calculates expected frequencies for chi-square goodness-of-fit test

// Distribution fit validation
=IF(CHISQ.TEST(HH2:HH10, II2:II10)<0.05, "Reject negative binomial", "Accept fit")
// Tests whether data follows negative binomial distribution

// Model selection support
="Chi-square p-value: " & CHISQ.TEST(JJ1:JJ8, KK1:KK8) & " (negative binomial vs observed)"
// Provides p-value for distribution model selection
```

### [[CONFIDENCE.NORM]]
CONFIDENCE.NORM constructs confidence intervals for negative binomial parameters using normal approximation for large samples.

```spreadsheets
// Confidence interval for success probability
="Success rate CI: " & LL5 & " ± " & CONFIDENCE.NORM(0.05, SQRT(LL5*(1-LL5)/MM5), MM5)
// Creates confidence interval for estimated success probability

// Parameter uncertainty quantification
="Failure rate range: " & (1-NN5-CONFIDENCE.NORM(0.05, SQRT(NN5*(1-NN5)/OO5), OO5)) & " to " & (1-NN5+CONFIDENCE.NORM(0.05, SQRT(NN5*(1-NN5)/OO5), OO5))
// Shows uncertainty range for failure probability estimates

// Sample size determination
="Required n for ±5% precision: " & CEILING((1.96/0.05)^2 * PP5*(1-PP5), 1)
// Calculates sample size needed for desired precision in parameter estimation
```

## Commonly Used With Functions Examples

### Data Validation and Error Handling
```spreadsheets
// Comprehensive parameter validation
=IF(AND(A5>=0, B5>0, C5>0, C5<=1), NEGBINOM.DIST(A5,B5,C5,TRUE), "Invalid parameters")
// Prevents calculation errors by validating all input parameters

// Range checking with feedback
=IF(D5<0, "Failures cannot be negative", IF(E5<=0, "Successes must be positive", NEGBINOM.DIST(D5,E5,F5,FALSE)))
// Provides specific error messages for parameter validation failures
```

### Business Decision Support
```spreadsheets
// Quality control decision making
=IF(NEGBINOM.DIST(G5,H5,I5,TRUE)>0.99, "Stop production - investigate", "Continue normal operations")
// Uses probability threshold to trigger quality control actions

// Resource planning based on probabilities
="Expected trials needed: " & (J5/K5) & ", Budget for " & CEILING((J5/K5)*1.2,1) & " trials"
// Combines negative binomial mean with business planning considerations
```

### Statistical Analysis and Reporting
```spreadsheets
// Comparative probability analysis
="P(≤" & L5 & " failures): " & ROUND(NEGBINOM.DIST(L5,M5,N5,TRUE)*100,2) & "% vs benchmark " & O5*100 & "%"
// Compares calculated probabilities against benchmark or target values

// Performance metrics with context
=CONCATENATE("Process efficiency: ", ROUND((1-NEGBINOM.DIST(P5,Q5,R5,TRUE))*100,1), "% chance of exceeding ", P5, " failures")
// Creates descriptive performance metrics using probability calculations
```
