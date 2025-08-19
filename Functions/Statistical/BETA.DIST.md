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

# BETA.DIST

## BETA.DIST Description

Returns the beta probability distribution function, commonly used in statistics for modeling random variables constrained between 0 and 1. The beta distribution is particularly useful for modeling proportions, probabilities, and percentages in Bayesian analysis, project management, and quality control.

> [!f(x)] BETA.DIST Syntax
>
> ```spreadsheets
> BETA.DIST(x, alpha, beta, cumulative, [A], [B])
> ```
>
> **Parameters:**
> - `x` (required): Value at which to evaluate the function (between A and B)
> - `alpha` (required): First shape parameter (must be > 0)
> - `beta` (required): Second shape parameter (must be > 0)  
> - `cumulative` (required): TRUE for cumulative distribution function, FALSE for probability density function
> - `A` (optional): Lower bound of interval (default = 0)
> - `B` (optional): Upper bound of interval (default = 1)

> [!f(x)] BETA.DIST Examples
>
> ```spreadsheets
> // Basic beta distribution probability
> BETA.DIST(0.4, 2, 5, TRUE) → 0.82944
> 
> // Project completion probability
> BETA.DIST(0.8, 3, 2, TRUE) → 0.896
> 
> // Quality control with custom bounds
> BETA.DIST(95, 8, 4, TRUE, 90, 100) → 0.563
> 
> // Probability density function
> BETA.DIST(0.3, 4, 6, FALSE) → 2.4576
> 
> // Risk assessment calculation
> BETA.DIST(A2, $B$1, $C$1, TRUE, 0, 1) → calculates cumulative probability for risk values
> ```

## Use Cases

### [[Project management]]
- **Task completion modeling**: Use beta distribution to model task completion probabilities based on optimistic and pessimistic estimates
- **Schedule risk analysis**: Calculate probability of project completion within specified timeframes using historical data
- **Resource allocation**: Model resource utilization rates and capacity planning with beta-distributed assumptions
- **Milestone tracking**: Assess probability of reaching project milestones based on current progress and historical patterns

### [[Quality control]]
- **Defect rate modeling**: Model proportion of defective items in manufacturing processes using beta distribution
- **Process capability analysis**: Analyze process performance within specification limits using beta-distributed quality metrics
- **Inspection sampling**: Calculate probabilities for acceptance sampling plans based on beta-distributed defect rates
- **Continuous improvement**: Model improvement rates and success probabilities for quality initiatives

### [[Financial modeling]]
- **Portfolio optimization**: Model asset correlation coefficients and portfolio weights using beta distributions
- **Risk assessment**: Calculate value-at-risk and expected shortfall using beta-distributed loss percentages
- **Credit scoring**: Model default probabilities and recovery rates with beta-distributed parameters
- **Market analysis**: Analyze market volatility and return distributions constrained between bounds

## Related

### Similar Functions

- [[GAMMA.DIST]] - Related continuous distribution, beta is special case of gamma distributions
- [[NORM.DIST]] - Normal distribution, different shape but similar statistical applications
- [[WEIBULL.DIST]] - Another bounded distribution used for reliability and survival analysis
- [[F.DIST]] - F-distribution, ratio of two beta-distributed random variables
- [[BETA.INV]] - Inverse beta distribution for finding x values given probabilities

## Statistical Analysis Functions

### [[BETA.INV]]
Complementary function that finds the x-value for a given probability in beta distribution. BETA.INV is essential for confidence intervals and statistical inference with beta distributions.

```spreadsheets
// Confidence interval calculation
="Lower: " & BETA.INV(0.025, A1, B1) & ", Upper: " & BETA.INV(0.975, A1, B1)
// 95% confidence interval for beta distribution

// Quality control limits
=IF(BETA.DIST(C1, 8, 4, TRUE)>0.95, "Exceeds upper limit", "Within tolerance")
// Combined with BETA.INV to set control limits: BETA.INV(0.95, 8, 4)

// Project completion targets
=BETA.INV(0.9, D1, E1) & " completion probability for 90% confidence"
// Finds completion rate needed for 90% confidence level
```

### [[GAMMA]]
Used to calculate gamma functions needed for beta distribution parameters. GAMMA provides the mathematical foundation for beta distribution calculations and parameter estimation.

```spreadsheets
// Beta function calculation
=GAMMA(F1)*GAMMA(G1)/GAMMA(F1+G1)
// Calculates beta function B(α,β) used in beta distribution normalization

// Parameter validation
=IF(AND(H1>0, I1>0), BETA.DIST(0.5, H1, I1, TRUE), "Invalid parameters: alpha and beta must be positive")
// Validates parameters before beta distribution calculation

// Distribution comparison
="Beta mean: " & (J1/(J1+K1)) & ", Gamma ratio: " & GAMMA(J1)/GAMMA(J1+K1)
// Shows relationship between beta and gamma functions
```

## Comparison Functions

### [[IF]]
Critical for conditional beta distribution analysis and parameter validation. IF enables BETA.DIST to handle edge cases, validate parameters, and provide contextual probability assessments.

```spreadsheets
// Parameter validation with beta distribution
=IF(AND(L1>0, M1>0, N1>=0, N1<=1), BETA.DIST(N1, L1, M1, TRUE), "Invalid inputs")
// Validates all parameters before calculation

// Risk category assignment
=IF(BETA.DIST(O1, 3, 7, TRUE)<0.3, "Low Risk", IF(BETA.DIST(O1, 3, 7, TRUE)<0.7, "Medium Risk", "High Risk"))
// Categorizes risk levels based on beta distribution probabilities

// Quality acceptance decision
=IF(BETA.DIST(P1, Q1, R1, TRUE, 0.9, 1)>0.8, "ACCEPT", "REJECT")
// Makes accept/reject decisions based on beta-distributed quality scores
```

### [[ROUND]]
Used with BETA.DIST to format probability outputs for reporting and decision-making. ROUND ensures beta distribution results are presented in meaningful precision levels.

```spreadsheets
// Formatted probability reporting
="Completion probability: " & ROUND(BETA.DIST(S1, T1, U1, TRUE)*100, 1) & "%"
// Displays beta probability as rounded percentage

// Statistical summary with formatting
="P(X≤" & V1 & ") = " & ROUND(BETA.DIST(V1, W1, X1, TRUE), 4)
// Properly formatted cumulative probability statement

// Risk metrics dashboard
=ROUND(BETA.DIST(Y1, Z1, AA1, TRUE), 3) & " (" & ROUND(BETA.DIST(Y1, Z1, AA1, TRUE)*100, 1) & "%)"
// Shows both decimal probability and percentage with appropriate rounding
```

## Commonly Used With Functions Examples

### Project Risk Dashboard
```spreadsheets
// Comprehensive project risk assessment
="Project: " & $A$1 & " | Progress: " & ROUND(B2*100,1) & "% | Risk Score: " & ROUND(BETA.DIST(B2, $C$1, $D$1, TRUE)*100,1) & "% | Status: " & IF(BETA.DIST(B2, $C$1, $D$1, TRUE)<0.3, "✓ ON TRACK", IF(BETA.DIST(B2, $C$1, $D$1, TRUE)<0.7, "⚠ AT RISK", "🚨 HIGH RISK"))
// Complete project risk dashboard with color-coded status

// Schedule confidence analysis
=IF(BETA.DIST(E2, F2, G2, TRUE)>0.8, "High confidence (" & ROUND(BETA.DIST(E2, F2, G2, TRUE)*100,1) & "%)", "Review schedule (" & ROUND(BETA.DIST(E2, F2, G2, TRUE)*100,1) & "%)")
// Schedule confidence with probability-based recommendations
```

### Quality Control System
```spreadsheets
// Manufacturing quality assessment
="Batch: " & $H$1 & " | Quality Score: " & I2 & " | Probability: " & ROUND(BETA.DIST(I2, $J$1, $K$1, TRUE, 0.8, 1)*100,1) & "% | " & IF(BETA.DIST(I2, $J$1, $K$1, TRUE, 0.8, 1)>0.95, "✅ PASS", IF(BETA.DIST(I2, $J$1, $K$1, TRUE, 0.8, 1)>0.8, "⚠ MARGINAL", "❌ FAIL"))
// Quality control decision system with beta-distributed thresholds

// Process capability monitoring
=IF(COUNT(L2:L50)>=30, "Capability: " & ROUND(BETA.DIST(AVERAGE(L2:L50), M1, N1, TRUE)*100,1) & "% | n=" & COUNT(L2:L50), "Insufficient data (n=" & COUNT(L2:L50) & ")")
// Process capability analysis with adequate sample size validation
```

### Financial Risk Analysis
```spreadsheets
// Portfolio risk assessment
="Asset: " & $O$1 & " | Return: " & ROUND(P2*100,1) & "% | Risk Percentile: " & ROUND(BETA.DIST(P2, Q1, R1, TRUE)*100,1) & "% | Classification: " & IF(BETA.DIST(P2, Q1, R1, TRUE)<0.25, "Conservative", IF(BETA.DIST(P2, Q1, R1, TRUE)<0.75, "Moderate", "Aggressive"))
// Investment classification based on beta-distributed risk metrics

// Value-at-Risk calculation
="VaR(95%): " & ROUND(BETA.INV(0.95, S1, T1)*100,1) & "% | Current: " & ROUND(U2*100,1) & "% | Margin: " & ROUND((BETA.INV(0.95, S1, T1)-U2)*100,1) & "%"
// Value-at-Risk calculation with safety margin analysis
```
