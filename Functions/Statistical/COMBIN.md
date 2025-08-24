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
# COMBIN

## COMBIN Description

Returns the number of combinations (ways to choose k items from n items) where order doesn't matter. Calculates "n choose k" combinations using the formula n!/(k!(n-k)!). Essential for probability calculations, sample size planning, statistical hypothesis testing, and combinatorial analysis in research and quality control.

> [!f(x)] COMBIN Syntax
>
> ```spreadsheets
> COMBIN(number, number_chosen)
> ```
>
> **Parameters:**
> - `number` (required): Total number of items (n ≥ 0)
> - `number_chosen` (required): Number of items to choose (k ≥ 0, k ≤ n)

> [!f(x)] COMBIN Examples
>
> ```spreadsheets
> // Basic combination calculation
> COMBIN(10, 3) → 120 (ways to choose 3 items from 10)
> 
> // Lottery probability analysis
> COMBIN(49, 6) → 13983816 (ways to choose 6 numbers from 49)
> 
> // Quality control sampling
> COMBIN(100, 5) → 75287520 (ways to select 5 items from batch of 100)
> 
> // Team selection scenarios
> COMBIN(15, 4) → 1365 (ways to choose 4 team members from 15 candidates)
> 
> // Clinical trial design
> COMBIN(200, 20) → ways to select 20 patients from 200 eligible participants
> ```

## Use Cases

### [[Probability and statistics]]
- **Sample size calculations**: Determine number of possible sample combinations for statistical power analysis and experiment design
- **Binomial probability calculations**: Calculate exact probabilities for binomial distributions using combination coefficients
- **Hypergeometric analysis**: Model sampling without replacement scenarios in quality control and survey research
- **Confidence interval construction**: Calculate exact confidence intervals for proportions using combinatorial methods

### [[Quality control and inspection]]
- **Acceptance sampling plans**: Design sampling strategies by calculating all possible ways to select inspection samples
- **Lot tolerance analysis**: Determine acceptance/rejection probabilities for different defect scenarios in batch inspections
- **Statistical process control**: Calculate control chart constants and detection probabilities for various sampling schemes
- **Risk assessment**: Evaluate probability of detecting defective items based on sampling combinations

### [[Experimental design and research]]
- **Treatment assignment**: Calculate number of ways to assign subjects to treatment groups in clinical trials and experiments
- **Survey sampling**: Determine possible sample combinations for stratified and cluster sampling methodologies
- **A/B testing**: Plan test group assignments and calculate statistical power for different experimental configurations
- **Cross-validation**: Design k-fold cross-validation schemes by calculating training/testing set combinations

## Related

### Similar Functions

- [[COMBINA]] - Combinations with repetition allowed, calculates ways to choose with replacement
- [[PERMUT]] - Permutations where order matters, calculates arrangements rather than selections
- [[FACT]] - Factorial function, used in combination formula calculation (n!)
- [[BINOM.DIST]] - Binomial distribution that uses COMBIN in its probability formula
- [[HYPGEOM.DIST]] - Hypergeometric distribution that relies on combination calculations

## Probability Distribution Functions

### [[BINOM.DIST]]
COMBIN provides the combination coefficient used in binomial probability calculations. BINOM.DIST uses COMBIN internally for exact probability computation.

```spreadsheets
// Manual binomial probability calculation
=COMBIN(A1, B1) * (C1^B1) * ((1-C1)^(A1-B1))
// Manually calculates what BINOM.DIST(B1, A1, C1, FALSE) returns

// Binomial coefficient verification
="C(" & D1 & "," & E1 & ") = " & COMBIN(D1, E1) & " coefficient in binomial expansion"
// Shows combination coefficient used in binomial theorem

// Probability mass function components
="P(X=" & F1 & ") uses C(" & G1 & "," & F1 & ") = " & COMBIN(G1, F1) & " ways"
// Explains combinatorial foundation of binomial probabilities
```

### [[HYPGEOM.DIST]]
HYPGEOM.DIST uses multiple COMBIN calculations for sampling without replacement probabilities. Understanding COMBIN helps interpret hypergeometric analysis.

```spreadsheets
// Manual hypergeometric probability
=COMBIN(H1, I1) * COMBIN(J1-H1, K1-I1) / COMBIN(J1, K1)
// Calculates hypergeometric probability using combination ratios

// Quality control sampling probability
="Ways to select " & L1 & " defects from " & M1 & " defective items: " & COMBIN(M1, L1)
// Part of hypergeometric sampling analysis

// Acceptance sampling calculation
="P(accept) uses combinations: " & COMBIN(N1, O1) & " × " & COMBIN(P1-N1, Q1-O1) & " / " & COMBIN(P1, Q1)
// Complete hypergeometric acceptance probability formula
```

## Factorial and Permutation Functions

### [[FACT]]
COMBIN uses factorial calculations internally. Understanding FACT helps validate COMBIN results and enables manual combination calculations.

```spreadsheets
// Manual combination calculation using factorials
=FACT(R1)/(FACT(S1)*FACT(R1-S1))
// Manual calculation of COMBIN(R1, S1) using factorial formula

// Combination formula verification
="C(" & T1 & "," & U1 & ") = " & T1 & "! / (" & U1 & "! × " & (T1-U1) & "!) = " & COMBIN(T1, U1)
// Shows mathematical relationship between combinations and factorials

// Large number approximation
=EXP(GAMMALN(V1+1) - GAMMALN(W1+1) - GAMMALN(V1-W1+1))
// Stirling approximation for large combinations to avoid overflow
```

### [[PERMUT]]
PERMUT counts arrangements while COMBIN counts selections. Together they provide complete combinatorial analysis for different ordering requirements.

```spreadsheets
// Combination vs permutation comparison
="Selections: " & COMBIN(X1, Y1) & ", Arrangements: " & PERMUT(X1, Y1) & " (ratio: " & PERMUT(X1, Y1)/COMBIN(X1, Y1) & ")"
// Shows difference between selecting and arranging items

// Ordering factor calculation
=PERMUT(Z1, Z1) & " ways to arrange " & Z1 & " selected items"
// Shows how many arrangements exist for each combination

// Complete counting analysis
="Total outcomes: " & COMBIN(AA1, BB1) & " selections × " & FACT(BB1) & " arrangements each"
// Comprehensive counting when both selection and ordering matter
```

## Statistical Planning Functions

### [[POWER]]
COMBIN supports statistical power calculations by determining the number of possible experimental configurations and sample combinations.

```spreadsheets
// Sample size adequacy assessment
="Possible samples: " & COMBIN(CC1, DD1) & " from population of " & CC1
// Assesses sampling adequacy for statistical inference

// Cross-validation planning
="CV folds: " & EE1 & ", Training combinations: " & COMBIN(EE1, EE1-1) & " possible"
// Plans cross-validation schemes using combination analysis

// Experimental design complexity
="Treatment groups: " & FF1 & ", Assignment combinations: " & COMBIN(GG1, FF1) & " possible"
// Evaluates experimental design complexity and balance requirements
```

### [[CONFIDENCE]]
COMBIN supports exact confidence interval calculations for discrete distributions and finite population scenarios.

```spreadsheets
// Exact binomial confidence interval bounds
="Lower bound combinations: " & SUM(COMBIN(HH1, ROW(0:II1)) * (JJ1^ROW(0:II1)) * ((1-JJ1)^(HH1-ROW(0:II1))))
// Uses combinations for exact confidence interval calculation

// Finite population confidence intervals
="Population combinations: " & COMBIN(KK1, LL1) & " for sampling confidence"
// Adjusts confidence calculations for finite population sampling

// Survey reliability assessment
=IF(COMBIN(MM1, NN1)>1000, "Adequate sampling diversity", "Limited sample combinations")
// Evaluates survey sampling adequacy using combination counts
```

## Conditional Logic Functions

### [[IF]]
IF enables conditional combination calculations and validates parameters for meaningful combinatorial analysis.

```spreadsheets
// Parameter validation for combinations
=IF(AND(OO1>=PP1, PP1>=0), COMBIN(OO1, PP1), "Invalid: k must be ≤ n and ≥ 0")
// Ensures valid combination parameters before calculation

// Sample size recommendation
=IF(COMBIN(QQ1, RR1)<100, "Need larger population for adequate sampling", COMBIN(QQ1, RR1) & " combinations available")
// Recommends minimum population sizes based on combination availability

// Complexity assessment for experimental design
=IF(COMBIN(SS1, TT1)>10000, "Very complex design - consider simplification", "Manageable complexity: " & COMBIN(SS1, TT1) & " combinations")
// Assesses experimental design complexity using combination counts
```

## Commonly Used With Functions Examples

### Quality Control Sampling System
```spreadsheets
// Acceptance sampling plan design
="Lot size: " & A1 & " | Sample: " & B1 & " | Possible samples: " & COMBIN(A1, B1) & " | Accept if ≤" & C1 & " defects | Risk: " & ROUND(SUM(BINOM.DIST(ROW(0:C1), B1, D1, FALSE))*100, 2) & "%"
// Complete acceptance sampling analysis using combinations for sample diversity

// Inspection strategy optimization
=IF(COMBIN(E1, F1)>1000000, "Use statistical sampling: " & F1 & " from " & E1, "Consider full inspection: only " & COMBIN(E1, F1) & " combinations")
// Recommends inspection strategy based on combinatorial complexity
```

### Clinical Trial Design
```spreadsheets
// Patient randomization planning
="Participants: " & G1 & " | Treatment groups: " & H1 & " | Group size: " & I1 & " | Assignment combinations: " & COMBIN(G1, I1) & " | Randomization seed options: " & FACT(H1)
// Complete randomization analysis for clinical trials

// Statistical power planning
=IF(COMBIN(J1, K1)*L1>10000, "Adequate power: " & COMBIN(J1, K1) & " sample combinations", "Underpowered study: consider larger n")
// Power analysis using combination-based sample size assessment
```

### Experimental Design Optimization
```spreadsheets
// A/B test configuration
="Total users: " & M1 & " | Test group: " & N1 & " | Control combinations: " & COMBIN(M1, N1) & " | Min detectable effect: " & ROUND(1.96*SQRT(O1*(1-O1)*(1/N1+1/(M1-N1))), 4)
// A/B test design with combinatorial sample analysis

// Cross-validation scheme planning
="Dataset size: " & P1 & " | K-folds: " & Q1 & " | Fold size: " & ROUND(P1/Q1, 0) & " | Training combinations: " & COMBIN(Q1, Q1-1) & " | Validation robustness: " & IF(COMBIN(Q1, Q1-1)>=10, "✅ ROBUST", "⚠️ LIMITED")
// Cross-validation planning with combination-based robustness assessment
```
