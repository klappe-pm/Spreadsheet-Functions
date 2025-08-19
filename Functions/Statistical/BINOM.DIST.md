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

# BINOM.DIST

## BINOM.DIST Description

Returns the individual term or cumulative binomial distribution probability. Used for calculating the probability of achieving a specific number of successes in a fixed number of independent trials, each with the same probability of success. Essential for quality control, A/B testing, and reliability analysis.

> [!f(x)] BINOM.DIST Syntax
>
> ```spreadsheets
> BINOM.DIST(number_s, trials, probability_s, cumulative)
> ```
>
> **Parameters:**
> - `number_s` (required): Number of successes in trials
> - `trials` (required): Number of independent trials
> - `probability_s` (required): Probability of success on each trial
> - `cumulative` (required): TRUE for cumulative distribution, FALSE for individual probability

> [!f(x)] BINOM.DIST Examples
>
> ```spreadsheets
> // Probability of exactly 3 successes in 10 trials
> BINOM.DIST(3, 10, 0.5, FALSE) → 0.117
> 
> // Cumulative probability of 3 or fewer successes
> BINOM.DIST(3, 10, 0.5, TRUE) → 0.172
> 
> // Quality control: 2 defects in 20 items
> BINOM.DIST(2, 20, 0.05, FALSE) → 0.189
> 
> // A/B test: 15 or fewer conversions in 100 trials
> BINOM.DIST(15, 100, 0.12, TRUE) → 0.762
> 
> // Reliability: exactly 1 failure in 5 components
> BINOM.DIST(1, 5, 0.1, FALSE) → 0.328
> ```

## Use Cases

### [[Quality control]]
- **Defect rate analysis**: Calculate probability of finding specific numbers of defective items in production batches
- **Inspection sampling**: Determine acceptance criteria for lot sampling based on binomial probabilities
- **Process monitoring**: Assess whether observed defect counts indicate process changes or normal variation
- **Six Sigma projects**: Analyze before/after defect rates to measure improvement effectiveness

### [[A/B testing]]
- **Conversion rate analysis**: Calculate statistical significance of conversion rate differences between test variants
- **Sample size determination**: Estimate required sample sizes to detect meaningful conversion rate changes
- **Confidence intervals**: Establish confidence bounds for conversion rates in marketing experiments
- **Power analysis**: Determine probability of detecting true differences in conversion rates

### [[Reliability engineering]]
- **System failure analysis**: Model probability of component failures in redundant systems
- **Maintenance scheduling**: Calculate probability of equipment failures within maintenance intervals
- **Warranty analysis**: Predict warranty claim rates based on product failure probabilities
- **Risk assessment**: Evaluate probability of system failures given individual component reliabilities

## Related

### Similar Functions

- [[POISSON.DIST]] - Approximates binomial when n is large and p is small
- [[NORM.DIST]] - Normal approximation to binomial for large n and moderate p
- [[HYPGEOM.DIST]] - Sampling without replacement version of binomial distribution
- [[NEGBINOM.DIST]] - Number of trials needed to achieve r successes
- [[BETA.DIST]] - Conjugate prior distribution for binomial parameter estimation

## Statistical Analysis Functions

### [[COMBIN]]
Calculates combinations used in binomial probability formula. COMBIN provides the "n choose k" coefficient that appears in the binomial probability calculation.

```spreadsheets
// Manual binomial calculation verification
=COMBIN(A1, B1) * (C1^B1) * ((1-C1)^(A1-B1))
// Manually calculates what BINOM.DIST(B1, A1, C1, FALSE) returns

// Expected number of combinations
="Combinations: " & COMBIN(D1, E1) & ", Probability: " & BINOM.DIST(E1, D1, F1, FALSE)
// Shows relationship between combinations and binomial probability

// Sampling analysis
=COMBIN(G1, H1) & " ways to select " & H1 & " items from " & G1
// Used with BINOM.DIST for sampling probability calculations
```

### [[IF]]
Essential for conditional binomial analysis and statistical decision making. IF enables BINOM.DIST to trigger alerts, validate parameters, and provide contextual probability interpretations.

```spreadsheets
// Statistical significance testing
=IF(BINOM.DIST(I1, J1, K1, TRUE)<0.05, "Statistically significant", "Not significant")
// Tests if observed results are significantly different from expected

// Quality control decision
=IF(BINOM.DIST(L1, M1, 0.05, FALSE)>0.1, "INVESTIGATE: Unusual defect pattern", "Normal variation")
// Flags unusual defect patterns for investigation

// A/B test interpretation
=IF(BINOM.DIST(N1, O1, P1, TRUE)<0.025, "Reject null hypothesis", "Fail to reject")
// Makes statistical decisions based on binomial test results
```

## Mathematical Functions

### [[ROUND]]
Used with BINOM.DIST to format probability outputs for reporting and presentation. ROUND ensures binomial probabilities are displayed with appropriate precision.

```spreadsheets
// Formatted probability report
="P(X=" & Q1 & ") = " & ROUND(BINOM.DIST(Q1, R1, S1, FALSE), 4)
// Shows individual probability with 4 decimal places

// Percentage format for presentations
=ROUND(BINOM.DIST(T1, U1, V1, TRUE)*100, 2) & "% cumulative probability"
// Converts to percentage with 2 decimal places

// Quality metrics dashboard
="Defect Rate: " & ROUND(W1/X1*100, 1) & "% | Probability: " & ROUND(BINOM.DIST(W1, X1, Y1, FALSE)*100, 1) & "%"
// Combined rate and probability reporting with consistent formatting
```

### [[SUM]]
Combined with BINOM.DIST to calculate probability ranges and expected values. SUM enables calculation of probability intervals and validation of cumulative probabilities.

```spreadsheets
// Probability range calculation
=BINOM.DIST(Z1, AA1, BB1, TRUE) - BINOM.DIST(CC1-1, AA1, BB1, TRUE)
// P(CC1 ≤ X ≤ Z1) using cumulative distribution differences

// Expected value verification
=SUM(ROW(1:DD1)*BINOM.DIST(ROW(1:DD1)-1, DD1-1, EE1, FALSE))
// Calculates expected value using definition: Σ(k × P(X=k))

// Distribution validation
=SUM(BINOM.DIST(ROW(0:FF1)-1, FF1, GG1, FALSE))
// Should equal 1.0 - validates that all probabilities sum to 1
```

## Commonly Used With Functions Examples

### Quality Control Dashboard
```spreadsheets
// Production quality monitoring
="Batch: " & $A$1 & " | Defects: " & B2 & "/" & C2 & " (" & ROUND(B2/C2*100,1) & "%) | Expected: " & ROUND(C2*$D$1*100,1) & "% | P-value: " & ROUND(1-BINOM.DIST(B2-1, C2, $D$1, TRUE), 4) & " | " & IF(1-BINOM.DIST(B2-1, C2, $D$1, TRUE)<0.05, "🚨 INVESTIGATE", "✅ NORMAL")
// Complete quality control analysis with statistical significance

// Process capability assessment
=IF(COUNT(E2:E50)>=30, "Defect rate: " & ROUND(SUM(E2:E50)/COUNT(E2:E50)*100,1) & "% | Control limit: " & ROUND(BINOM.INV(COUNT(E2:E50), 0.05, 0.95)/COUNT(E2:E50)*100,1) & "%", "Need more data (n=" & COUNT(E2:E50) & ")")
// Statistical process control with adequate sample validation
```

### A/B Test Analysis
```spreadsheets
// Conversion rate comparison
="Variant: " & $F$1 & " | Conversions: " & G2 & "/" & H2 & " (" & ROUND(G2/H2*100,1) & "%) | Control: " & ROUND($I$1*100,1) & "% | Significance: " & IF(BINOM.DIST(G2, H2, $I$1, TRUE)<0.025, "✅ SIGNIFICANT", IF(BINOM.DIST(G2, H2, $I$1, TRUE)>0.975, "✅ SIGNIFICANT", "⚠ NOT SIGNIFICANT"))
// Two-tailed significance test for A/B experiments

// Power analysis for sample sizing
=IF(J2>0, "Power: " & ROUND((1-BINOM.DIST(BINOM.INV(J2, K2, 0.05), J2, K2+L2, TRUE))*100,1) & "% | Need n≥" & CEILING(((NORM.S.INV(0.95)+NORM.S.INV(0.8))^2)*(K2*(1-K2)+((K2+L2)*(1-(K2+L2)))/(L2^2)),1), "Set effect size")
// Statistical power calculation with minimum sample size recommendation
```

### Reliability Engineering
```spreadsheets
// System reliability analysis
="System: " & $M$1 & " | Components: " & N2 & " | Failures: " & O2 & " | Individual Reliability: " & ROUND((1-P2)*100,1) & "% | System Reliability: " & ROUND((1-BINOM.DIST(0, N2, P2, FALSE))*100,1) & "% | MTBF: " & ROUND(1/(N2*P2),1) & " cycles"
// Complete reliability analysis with mean time between failures

// Preventive maintenance planning
=IF(BINOM.DIST(Q2, R2, S2, TRUE)>0.9, "Maintenance due: High failure probability (" & ROUND(BINOM.DIST(Q2, R2, S2, TRUE)*100,1) & "%)", "Continue operation: Low failure risk (" & ROUND(BINOM.DIST(Q2, R2, S2, TRUE)*100,1) & "%)")
// Maintenance scheduling based on cumulative failure probability
```
