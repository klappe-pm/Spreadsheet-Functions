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
# PEARSON

## PEARSON Description

Calculates the Pearson product-moment correlation coefficient between two datasets, measuring the strength and direction of linear relationship. Returns values between -1 and +1, where values near ±1 indicate strong linear correlation and values near 0 indicate weak linear correlation. Essential for regression analysis, data validation, and relationship identification.

> [!f(x)] PEARSON Syntax
>
> ```spreadsheets
> PEARSON(array1, array2)
> ```
>
> **Parameters:**
> - `array1` (required): First dataset (independent variable or x-values)
> - `array2` (required): Second dataset (dependent variable or y-values) 
> - Both arrays must have equal number of data points

> [!f(x)] PEARSON Examples
>
> ```spreadsheets
> // Strong positive correlation
> PEARSON({1,2,3,4,5}, {2,4,6,8,10}) → 1.0 (perfect positive correlation)
> 
> // Moderate negative correlation
> PEARSON({10,8,6,4,2}, {1,3,5,7,9}) → -1.0 (perfect negative correlation)
> 
> // Sales vs advertising correlation
> PEARSON(A2:A12, B2:B12) → 0.85 (strong positive relationship)
> 
> // Temperature vs energy usage correlation
> PEARSON(C1:C365, D1:D365) → -0.72 (strong negative relationship)
> 
> // No linear correlation example
> PEARSON({1,2,3,2,1}, {1,4,9,4,1}) → 0.0 (no linear relationship despite functional relationship)
> ```

## Use Cases

### [[Market research and business analytics]]
- **Customer behavior analysis**: Measure correlation between customer satisfaction scores and retention rates for loyalty program optimization
- **Sales performance evaluation**: Analyze relationships between marketing spend and sales revenue across different channels and time periods
- **Product feature correlation**: Identify which product features correlate most strongly with customer preference ratings and purchase decisions
- **Pricing strategy optimization**: Examine correlations between price points and demand volumes to optimize pricing models

### [[Quality control and process improvement]]
- **Process variable relationships**: Identify correlations between manufacturing parameters and product quality metrics for process optimization
- **Predictive maintenance**: Analyze correlations between equipment sensor readings and failure rates to predict maintenance needs
- **Supply chain optimization**: Measure relationships between supplier performance metrics and delivery success rates
- **Six Sigma analysis**: Identify input variables that correlate most strongly with process outcomes for targeted improvement efforts

### [[Financial and risk analysis]]
- **Portfolio diversification**: Calculate correlations between asset returns to optimize portfolio diversification and risk management
- **Market risk assessment**: Analyze correlations between market indicators and portfolio performance for risk modeling
- **Economic forecasting**: Measure relationships between leading indicators and economic outcomes for predictive modeling
- **Credit risk evaluation**: Examine correlations between financial ratios and default rates for credit scoring models

## Related

### Similar Functions

- [[CORREL]] - Identical to PEARSON; both calculate Pearson correlation coefficient with same syntax and results
- [[RSQ]] - Calculates coefficient of determination (R²), which is the square of PEARSON correlation coefficient
- [[COVAR]] - Calculates covariance, the numerator component of correlation before standardization
- [[SLOPE]] - Calculates slope of regression line; related to correlation through standard deviations
- [[INTERCEPT]] - Calculates y-intercept of regression line; complements PEARSON in regression analysis

## Data Relationship Functions

### [[AVERAGE]]
PEARSON uses means of both datasets in its calculation, with correlation measuring deviations from means relative to standard deviations.

```spreadsheets
// Manual correlation calculation verification
=(SUMPRODUCT((A1:A10-AVERAGE(A1:A10))*(B1:B10-AVERAGE(B1:B10))))/(SQRT(SUMPRODUCT((A1:A10-AVERAGE(A1:A10))^2))*SQRT(SUMPRODUCT((B1:B10-AVERAGE(B1:B10))^2)))
// Should equal PEARSON(A1:A10, B1:B10), showing role of averages in correlation

// Correlation strength interpretation
="Correlation: " & ROUND(PEARSON(C2:C20, D2:D20), 3) & 
" (X̄=" & ROUND(AVERAGE(C2:C20), 2) & ", Ȳ=" & ROUND(AVERAGE(D2:D20), 2) & ")"
// Shows correlation with context of means for both variables

// Relationship validation with means
=IF(ABS(PEARSON(E1:E25, F1:F25))>0.7, "Strong correlation: both variables deviate from means (" & AVERAGE(E1:E25) & ", " & AVERAGE(F1:F25) & ") in predictable patterns", "Weak correlation")
// Explains correlation strength in terms of mean deviations
```

### [[STDEV]]
PEARSON standardizes covariance by the product of standard deviations, making correlation a dimensionless measure of linear relationship strength.

```spreadsheets
// Correlation components breakdown
="Covariance: " & COVAR(G1:G30, H1:H30) & 
", Std Dev X: " & STDEV(G1:G30) & 
", Std Dev Y: " & STDEV(H1:H30) & 
", Correlation: " & PEARSON(G1:G30, H1:H30)
// Shows how PEARSON equals covariance divided by product of standard deviations

// Standardized relationship strength
="Correlation " & PEARSON(I2:I40, J2:J40) & " means 1 SD change in X associates with " & PEARSON(I2:I40, J2:J40) & " SD change in Y"
// Interprets correlation coefficient in terms of standard deviation changes

// Data preprocessing impact on correlation
="Raw correlation: " & PEARSON(K1:K20, L1:L20) & 
", Standardized correlation: " & PEARSON((K1:K20-AVERAGE(K1:K20))/STDEV(K1:K20), (L1:L20-AVERAGE(L1:L20))/STDEV(L1:L20))
// Shows correlation is unchanged by standardization (should be identical)
```

## Regression Analysis Functions

### [[RSQ]]
RSQ returns the square of PEARSON correlation coefficient, representing the proportion of variance in one variable explained by the other.

```spreadsheets
// R-squared validation from correlation
="Correlation: " & PEARSON(M1:M35, N1:N35) & 
", R-squared: " & RSQ(M1:M35, N1:N35) & 
", Manual R²: " & PEARSON(M1:M35, N1:N35)^2
// Demonstrates RSQ equals PEARSON squared

// Explained variance interpretation
="Linear relationship explains " & ROUND(RSQ(O2:O30, P2:P30)*100, 1) & "% of variance (r=" & ROUND(PEARSON(O2:O30, P2:P30), 3) & ")"
// Shows percentage of variance explained using R-squared from correlation

// Model fit assessment
=IF(RSQ(Q1:Q25, R1:R25) > 0.5, "Strong predictive relationship (r=" & ROUND(PEARSON(Q1:Q25, R1:R25), 3) & ")", "Weak predictive power")
// Uses R-squared threshold based on correlation strength for model evaluation
```

### [[SLOPE]]
SLOPE calculates the regression line slope, which is related to PEARSON through the ratio of standard deviations.

```spreadsheets
// Relationship between slope and correlation
="Slope: " & SLOPE(S1:S40, T1:T40) & 
", Correlation: " & PEARSON(T1:T40, S1:S40) & 
", Expected slope: " & PEARSON(T1:T40, S1:S40) * STDEV(S1:S40) / STDEV(T1:T40)
// Shows slope equals correlation times ratio of standard deviations

// Regression equation construction
="Y = " & INTERCEPT(U2:U30, V2:V30) & " + " & SLOPE(U2:U30, V2:V30) & "X (r=" & PEARSON(V2:V30, U2:U30) & ")"
// Constructs complete regression equation with correlation coefficient

// Standardized vs unstandardized relationships
="Unstandardized slope: " & SLOPE(W1:W20, X1:X20) & 
", Standardized slope (β): " & PEARSON(X1:X20, W1:W20) & 
", Interpretation: correlation is standardized slope"
// Shows correlation as standardized regression coefficient
```

## Statistical Analysis Functions

### [[COUNT]]
COUNT ensures equal sample sizes for correlation calculation and validates data completeness before analysis.

```spreadsheets
// Sample size validation
=IF(COUNT(Y1:Y50)=COUNT(Z1:Z50), "Equal samples (n=" & COUNT(Y1:Y50) & "), r=" & PEARSON(Y1:Y50, Z1:Z50), "Unequal sample sizes - check data")
// Validates equal sample sizes required for correlation calculation

// Statistical significance estimation
="Correlation r=" & PEARSON(AA2:AA25, BB2:BB25) & 
" with n=" & COUNT(AA2:AA25) & 
", Critical r(α=0.05)≈" & ROUND(1.96/SQRT(COUNT(AA2:AA25)-2), 3)
// Provides approximate critical value for correlation significance testing

// Data quality assessment
="Valid pairs: " & COUNT(CC1:CC30) & "/" & COUNTA(CC1:CC30) & 
", Correlation: " & IF(COUNT(CC1:CC30)>=10, PEARSON(CC1:CC30, DD1:DD30), "Insufficient data")
// Ensures minimum sample size before calculating correlation
```

### [[IF]]
IF enables conditional correlation analysis, significance testing, and interpretation based on correlation strength and sample characteristics.

```spreadsheets
// Correlation strength interpretation
=IF(ABS(PEARSON(EE1:EE40, FF1:FF40))>0.8, "Very strong", IF(ABS(PEARSON(EE1:EE40, FF1:FF40))>0.6, "Strong", IF(ABS(PEARSON(EE1:EE40, FF1:FF40))>0.4, "Moderate", IF(ABS(PEARSON(EE1:EE40, FF1:FF40))>0.2, "Weak", "Very weak")))) & " linear relationship"
// Categorizes correlation strength using standard thresholds

// Direction and significance assessment
="Relationship: " & IF(PEARSON(GG2:GG35, HH2:HH35)>0, "Positive", "Negative") & 
", Strength: " & IF(ABS(PEARSON(GG2:GG35, HH2:HH35))>0.05, "Potentially significant", "Likely not significant")
// Interprets both direction and potential significance of correlation

// Business decision support
=IF(PEARSON(II1:II30, JJ1:JJ30)>0.7, "Strong predictor - recommend using in model", IF(PEARSON(II1:II30, JJ1:JJ30)>0.3, "Moderate predictor - consider inclusion", "Weak predictor - exclude from model"))
// Makes model inclusion decisions based on correlation thresholds
```

## Commonly Used With Functions Examples

### Data Analysis and Research
```spreadsheets
// Comprehensive correlation analysis
="Variables: " & "X (M=" & ROUND(AVERAGE(A1:A25),2) & ", SD=" & ROUND(STDEV(A1:A25),2) & ") vs " & 
"Y (M=" & ROUND(AVERAGE(B1:B25),2) & ", SD=" & ROUND(STDEV(B1:B25),2) & ")" & CHAR(10) & 
"Correlation: r=" & ROUND(PEARSON(A1:A25, B1:B25),3) & 
" (" & IF(PEARSON(A1:A25, B1:B25)>0,"Positive","Negative") & " " & 
IF(ABS(PEARSON(A1:A25, B1:B25))>0.7,"Strong",IF(ABS(PEARSON(A1:A25, B1:B25))>0.3,"Moderate","Weak")) & ")" & CHAR(10) &
"Variance explained: " & ROUND(PEARSON(A1:A25, B1:B25)^2*100,1) & "%"
// Complete correlation summary with descriptive statistics
```

### Business Intelligence and Performance Metrics
```spreadsheets
// Key performance indicator relationships
="Marketing ROI Analysis:" & CHAR(10) &
"Spend vs Revenue: r=" & ROUND(PEARSON(C2:C13, D2:D13),3) & " (R²=" & ROUND(PEARSON(C2:C13, D2:D13)^2,3) & ")" & CHAR(10) &
"Spend vs Leads: r=" & ROUND(PEARSON(C2:C13, E2:E13),3) & " (R²=" & ROUND(PEARSON(C2:C13, E2:E13)^2,3) & ")" & CHAR(10) &
"Leads vs Revenue: r=" & ROUND(PEARSON(E2:E13, D2:D13),3) & " (R²=" & ROUND(PEARSON(E2:E13, D2:D13)^2,3) & ")"
// Multi-variable correlation matrix for business analysis
```

### Quality Control and Process Optimization
```spreadsheets
// Process parameter correlation matrix
="Process Control Correlations (n=" & COUNT(F1:F20) & "):" & CHAR(10) &
"Temperature vs Yield: r=" & ROUND(PEARSON(F1:F20, G1:G20),3) & 
IF(ABS(PEARSON(F1:F20, G1:G20))>0.7, " (STRONG)", IF(ABS(PEARSON(F1:F20, G1:G20))>0.3, " (MODERATE)", " (WEAK)")) & CHAR(10) &
"Pressure vs Quality: r=" & ROUND(PEARSON(H1:H20, I1:I20),3) &
IF(ABS(PEARSON(H1:H20, I1:I20))>0.7, " (STRONG)", IF(ABS(PEARSON(H1:H20, I1:I20))>0.3, " (MODERATE)", " (WEAK)")) & CHAR(10) &
"Recommendation: " & IF(MAX(ABS(PEARSON(F1:F20, G1:G20)), ABS(PEARSON(H1:H20, I1:I20)))>0.6, "Focus on strongly correlated variables", "Investigate other factors")
// Process improvement prioritization based on correlation strengths
```
