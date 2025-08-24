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
# CORREL

## CORREL Description

Calculates the Pearson product-moment correlation coefficient between two datasets, measuring the linear relationship strength and direction. Returns values from -1 (perfect negative correlation) to +1 (perfect positive correlation), with 0 indicating no linear relationship. Essential for regression analysis, portfolio theory, and multivariate statistical procedures.

> [!f(x)] CORREL Syntax
>
> ```spreadsheets
> CORREL(array1, array2)
> ```
>
> **Parameters:**
> - `array1` (required): First array or range of numerical values
> - `array2` (required): Second array or range of numerical values (must be same size as array1)

> [!f(x)] CORREL Examples
>
> ```spreadsheets
> // Basic correlation calculation
> CORREL(A1:A20, B1:B20) → 0.87 (strong positive correlation)
> 
> // Sales vs advertising correlation
> CORREL(C2:C25, D2:D25) → 0.65 (moderate positive relationship)
> 
> // Temperature vs ice cream sales
> CORREL(E1:E365, F1:F365) → 0.78 (seasonal correlation pattern)
> 
> // Stock price correlation analysis
> CORREL(G2:G100, H2:H100) → -0.23 (weak negative correlation)
> 
> // Academic performance correlation
> CORREL(I5:I50, J5:J50) → 0.92 (very strong positive correlation)
> ```

## Use Cases

### [[Financial portfolio analysis]]
- **Asset correlation assessment**: Analyze correlations between stock returns, bond yields, and commodities for diversification strategy development
- **Risk management optimization**: Identify highly correlated assets to reduce portfolio concentration risk and improve risk-adjusted returns  
- **Hedge fund strategy analysis**: Measure correlation between hedge fund returns and market indices to assess alternative investment benefits
- **Currency risk evaluation**: Analyze correlations between foreign exchange rates and business revenues for multinational corporations

### [[Marketing and business intelligence]]  
- **Sales performance analysis**: Measure correlations between advertising spend, seasonal factors, and sales revenue to optimize marketing budgets
- **Customer behavior studies**: Analyze relationships between demographics, purchase history, and customer lifetime value for targeted marketing
- **Website optimization**: Correlate page load times, bounce rates, and conversion rates to identify technical improvement priorities
- **Product performance metrics**: Assess correlations between product features, pricing, and customer satisfaction scores

### [[Scientific research and experimentation]]
- **Clinical trial analysis**: Measure correlations between treatment dosages, biomarkers, and patient outcomes for drug development studies
- **Environmental monitoring**: Analyze relationships between pollution levels, weather patterns, and health indicators for policy development
- **Manufacturing quality control**: Correlate process parameters with product quality metrics to optimize production efficiency
- **Agricultural research**: Study correlations between soil conditions, weather patterns, and crop yields for precision agriculture

## Related

### Similar Functions

- [[PEARSON]] - Identical to CORREL, calculates Pearson correlation coefficient using the same mathematical formula
- [[RSQ]] - Returns R-squared (coefficient of determination), which equals CORREL squared for measuring explained variance
- [[COVAR]] - Calculates covariance between datasets, the numerator in correlation calculation before standardization
- [[FISHER]] - Transforms correlation coefficients to Fisher's z-scale for statistical hypothesis testing procedures
- [[SLOPE]] - Calculates regression slope coefficient, related to correlation through standard deviation ratio

## Regression Analysis Functions

### [[RSQ]]
CORREL and RSQ are mathematically related (RSQ = CORREL²). RSQ shows variance explained while CORREL shows relationship strength and direction, essential for comprehensive regression analysis.

```spreadsheets
// Correlation and R-squared relationship
=CORREL(A1:A50, B1:B50) & " correlation, " & RSQ(A1:A50, B1:B50) & " R-squared (" & CORREL(A1:A50, B1:B50)^2 & ")"
// Shows relationship: "0.85 correlation, 0.7225 R-squared (0.7225)"

// Model strength interpretation
=IF(RSQ(C2:C30, D2:D30)>0.8, "Strong model (R²=" & RSQ(C2:C30, D2:D30) & ")", "Weak model")
// Interprets model strength using R-squared derived from correlation

// Explained variance calculation
="Correlation explains " & RSQ(E1:E40, F1:F40)*100 & "% of variance"
// Converts correlation to percentage of variance explained
```

### [[SLOPE]]  
SLOPE and CORREL are related through the ratio of standard deviations. Understanding both provides complete linear relationship characterization for prediction and interpretation.

```spreadsheets
// Slope-correlation relationship verification
=SLOPE(G2:G25, H2:H25) & " slope, " & CORREL(G2:G25, H2:H25)*STDEV(G2:G25)/STDEV(H2:H25) & " calculated"
// Verifies mathematical relationship between slope and correlation

// Regression equation with correlation context
="y = " & INTERCEPT(I1:I30, J1:J30) & " + " & SLOPE(I1:I30, J1:J30) & "x (r=" & CORREL(I1:I30, J1:J30) & ")"
// Complete regression equation with correlation coefficient

// Standardized regression coefficient
=CORREL(K2:K40, L2:L40)
// In simple regression, standardized coefficient equals correlation
```

## Covariance and Variance Functions

### [[COVAR]]
COVAR provides the numerator for CORREL calculation. Together they show both absolute covariance and standardized correlation, essential for portfolio theory and multivariate analysis.

```spreadsheets
// Manual correlation calculation
=COVAR(M1:M50, N1:N50)/(STDEV(M1:M50)*STDEV(N1:N50))
// Calculates correlation using covariance and standard deviations

// Portfolio covariance matrix preparation
="Cov(A,B): " & COVAR(O2:O60, P2:P60) & ", Corr: " & CORREL(O2:O60, P2:P60)
// Shows both covariance and correlation for portfolio analysis

// Risk decomposition analysis
="Covariance contributes " & ABS(COVAR(Q1:Q25, R1:R25))/VAR(Q1:Q25)*100 & "% to total risk"
// Analyzes covariance contribution to portfolio risk
```

### [[VAR]]
VAR provides denominators for correlation calculations and enables variance decomposition analysis. Essential for understanding how correlation relates to individual variable variability.

```spreadsheets
// Correlation decomposition
="Correlation: " & COVAR(S2:S30, T2:T30)/SQRT(VAR(S2:S30)*VAR(T2:T30))
// Manual correlation using variance instead of standard deviation

// Relative variability comparison
=VAR(U1:U40)/VAR(V1:V40) & " variance ratio, " & CORREL(U1:U40, V1:V40) & " correlation"
// Compares individual variabilities with joint correlation

// Standardization impact analysis
="Raw correlation: " & CORREL(W2:W35, X2:X35) & ", Standardized: " & CORREL((W2:W35-AVERAGE(W2:W35))/STDEV(W2:W35), (X2:X35-AVERAGE(X2:X35))/STDEV(X2:X35))
// Shows correlation is invariant to linear transformations
```

## Statistical Significance Functions

### [[T.TEST]]
CORREL provides the basis for testing correlation significance. T.TEST and related functions determine if observed correlations differ significantly from zero.

```spreadsheets
// Correlation significance test statistic
=CORREL(Y1:Y30, Z1:Z30)*SQRT((COUNT(Y1:Y30)-2)/(1-CORREL(Y1:Y30, Z1:Z30)^2))
// Calculates t-statistic for testing if correlation equals zero

// Confidence interval for correlation (approximate)
=CORREL(AA2:AA50, BB2:BB50) & " ± " & 1.96/SQRT(COUNT(AA2:AA50)-3)
// Rough confidence interval using Fisher transformation approximation

// Sample size for correlation detection
="Need n=" & CEILING((1.96/0.3)^2+3, 1) & " to detect r=0.3 with 80% power"
// Sample size calculation for correlation studies
```

### [[COUNT]]
COUNT validates correlation calculations by ensuring adequate sample sizes for reliable correlation estimates and statistical significance testing.

```spreadsheets
// Correlation with sample size validation
=IF(COUNT(CC1:CC25)>=20, CORREL(CC1:CC25, DD1:DD25), "Need larger sample")
// Only calculates correlation with adequate sample size

// Degrees of freedom for correlation
="Correlation: " & CORREL(EE2:EE40, FF2:FF40) & " (df=" & (COUNT(EE2:EE40)-2) & ")"
// Shows correlation with degrees of freedom for significance testing

// Missing data impact assessment  
="Complete pairs: " & COUNT(GG1:GG30) & " of " & ROWS(GG1:GG30) & " (" & COUNT(GG1:GG30)/ROWS(GG1:GG30)*100 & "%)"
// Assesses data completeness for correlation reliability
```
