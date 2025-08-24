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
# MEDIAN

## MEDIAN Description

Calculates the median (middle value) of a dataset when values are arranged in ascending order. For odd-sized datasets, returns the middle value; for even-sized datasets, returns the average of the two middle values. Robust to outliers and provides better central tendency representation than AVERAGE for skewed distributions.

> [!f(x)] MEDIAN Syntax
>
> ```spreadsheets
> MEDIAN(number1, [number2], [number3], ...)
> MEDIAN(range)
> MEDIAN(range1, range2, ...)
> ```
>
> **Parameters:**
> - `number1` (required): First number, cell reference, or range containing numerical data
> - `number2, number3, ...` (optional): Additional numbers, cell references, or ranges (up to 255 arguments)

> [!f(x)] MEDIAN Examples
>
> ```spreadsheets
> // Basic median calculation
> MEDIAN(1, 3, 5, 7, 9) → 5 (middle value of odd-sized set)
> 
> // Even number of values
> MEDIAN(10, 20, 30, 40) → 25 (average of 20 and 30)
> 
> // Median of a range
> MEDIAN(A1:A50) → middle value from range A1:A50
> 
> // Salary analysis (robust to outliers)
> MEDIAN(B2:B100) → 45000 (typical salary, unaffected by executive outliers)
> 
> // Housing price analysis
> MEDIAN(C1:C500) → 285000 (median home price in market)
> ```

## Use Cases

### [[Robust central tendency analysis]]
- **Salary and income studies**: Calculate median wages to represent typical worker earnings without CEO/executive salary distortion
- **Housing market analysis**: Determine median home prices that better represent affordable housing than mean prices skewed by luxury properties
- **Academic performance assessment**: Use median test scores to understand typical student performance when grade distributions are skewed
- **Healthcare cost analysis**: Analyze median treatment costs to understand typical patient expenses without rare expensive case influence

### [[Outlier-resistant statistical reporting]]  
- **Quality control metrics**: Monitor median production times when occasional equipment failures create extreme outliers in manufacturing data
- **Customer satisfaction surveys**: Report median satisfaction scores when response distributions show ceiling/floor effects or extreme responses
- **Financial performance reporting**: Present median investment returns to show typical performance without distortion from exceptional gains/losses
- **Website analytics**: Analyze median page load times and session durations for representative user experience metrics

### [[Distribution analysis and comparison]]
- **Market research segmentation**: Compare median incomes, ages, and spending across demographic groups for market targeting strategies
- **Clinical trial analysis**: Report median survival times and biomarker levels when medical data often follows non-normal distributions
- **A/B testing evaluation**: Use median conversion rates and engagement metrics when treatment effects create skewed response distributions
- **Risk assessment studies**: Analyze median loss amounts and recovery times when risk events follow heavy-tailed distributions

## Related

### Similar Functions

- [[QUARTILE]] - Returns first, second (median), or third quartile values for more detailed distributional analysis
- [[PERCENTILE]] - Calculates any percentile (MEDIAN equals 50th percentile) for comprehensive distribution characterization
- [[MODE]] - Identifies most frequent value, complementary to median for understanding different aspects of central tendency
- [[AVERAGE]] - Calculates arithmetic mean, sensitive to outliers but essential for mathematical relationships with variance
- [[TRIMMEAN]] - Calculates mean after removing extreme values, bridging robust median and traditional mean approaches

## Central Tendency Analysis Functions

### [[AVERAGE]]
MEDIAN and AVERAGE together provide comprehensive central tendency analysis. Comparing them reveals distribution skewness and helps choose appropriate statistical measures for analysis.

```spreadsheets
// Distribution skewness assessment
=IF(ABS(AVERAGE(A1:A50)-MEDIAN(A1:A50))/STDEV(A1:A50)<0.5, "Symmetric", IF(AVERAGE(A1:A50)>MEDIAN(A1:A50), "Right-skewed", "Left-skewed"))
// Determines distribution shape using mean-median relationship

// Central tendency comparison
=AVERAGE(B2:B100) & " mean vs " & MEDIAN(B2:B100) & " median (difference: " & ABS(AVERAGE(B2:B100)-MEDIAN(B2:B100)) & ")"
// Shows both measures with absolute difference

// Outlier impact analysis
="Without outliers: mean=" & TRIMMEAN(C1:C30, 0.1) & ", median=" & MEDIAN(C1:C30)
// Compares trimmed mean with median to assess outlier sensitivity
```

### [[MODE]]  
MEDIAN and MODE together describe different aspects of central tendency - median shows positional center while mode shows frequency center, essential for comprehensive distribution analysis.

```spreadsheets
// Complete central tendency summary
="Mean: " & AVERAGE(D2:D40) & ", Median: " & MEDIAN(D2:D40) & ", Mode: " & MODE.SNGL(D2:D40)
// Provides all three measures of central tendency

// Distribution type classification
=IF(ABS(AVERAGE(E1:E25)-MEDIAN(E1:E25))<1, IF(ABS(MEDIAN(E1:E25)-MODE.SNGL(E1:E25))<1, "Normal-like", "Uniform-like"), "Skewed")
// Classifies distribution based on central tendency relationships

// Robust central value selection
=IF(COUNT(F2:F50)/ROWS(F2:F50)>0.8, MEDIAN(F2:F50), MODE.SNGL(F2:F50))
// Chooses median for continuous data, mode for sparse data
```

## Percentile and Ranking Functions

### [[QUARTILE]]
MEDIAN equals the second quartile (Q2). Together with Q1 and Q3, they provide complete quartile analysis essential for box plots and distribution characterization.

```spreadsheets
// Five-number summary
="Min: " & MIN(G1:G60) & ", Q1: " & QUARTILE(G1:G60, 1) & ", Median: " & MEDIAN(G1:G60) & ", Q3: " & QUARTILE(G1:G60, 3) & ", Max: " & MAX(G1:G60)
// Complete box plot summary statistics

// Interquartile range analysis
="IQR: " & (QUARTILE(H2:H45, 3)-QUARTILE(H2:H45, 1)) & " (50% of data spans this range around median " & MEDIAN(H2:H45) & ")"
// Shows middle 50% spread around median

// Outlier detection using IQR method
=IF(OR(I5<QUARTILE(I2:I50, 1)-1.5*(QUARTILE(I2:I50, 3)-QUARTILE(I2:I50, 1)), I5>QUARTILE(I2:I50, 3)+1.5*(QUARTILE(I2:I50, 3)-QUARTILE(I2:I50, 1))), "Outlier", "Normal")
// Identifies outliers using 1.5×IQR rule from median-based quartiles
```

### [[PERCENTILE]]
MEDIAN equals PERCENTILE(range, 0.5). Understanding this relationship enables flexible percentile analysis and sophisticated distribution studies.

```spreadsheets
// Median verification using percentiles
=MEDIAN(J1:J40) & " median equals " & PERCENTILE(J1:J40, 0.5) & " (50th percentile)"
// Demonstrates median-percentile equivalence

// Percentile analysis around median
="25th: " & PERCENTILE(K2:K35, 0.25) & ", Median: " & PERCENTILE(K2:K35, 0.5) & ", 75th: " & PERCENTILE(K2:K35, 0.75)
// Shows quartile percentiles including median

// Custom percentile analysis
="Median ± 1 decile: " & PERCENTILE(L1:L50, 0.4) & " to " & PERCENTILE(L1:L50, 0.6) & " (around " & MEDIAN(L1:L50) & ")"
// Analyzes distribution around median using custom percentiles
```

## Distribution Comparison Functions

### [[STDEV]]
MEDIAN with STDEV provides robust distribution analysis. STDEV shows spread while MEDIAN shows central location, together characterizing non-normal distributions effectively.

```spreadsheets
// Robust distribution summary
=MEDIAN(M2:M50) & " ± " & STDEV(M2:M50) & " (median ± SD for reference)"
// Shows median with standard deviation context

// Distribution normality assessment
=ABS((AVERAGE(N1:N30)-MEDIAN(N1:N30))/STDEV(N1:N30))
// Calculates normalized skewness using median-mean difference

// Outlier-resistant coefficient of variation
=STDEV(O2:O40)/MEDIAN(O2:O40)*100 & "% (CV using median as denominator)"
// Uses median instead of mean for outlier-resistant relative variability
```

### [[COUNT]]
COUNT validates MEDIAN calculations and enables conditional median analysis. Essential for ensuring adequate sample sizes for reliable median estimates.

```spreadsheets
// Median with sample size validation
=IF(COUNT(P1:P25)>=15, MEDIAN(P1:P25), "Need larger sample for reliable median")
// Ensures adequate sample size for stable median estimates

// Data completeness assessment
="Median: " & MEDIAN(Q2:Q30) & " from " & COUNT(Q2:Q30) & " of " & ROWS(Q2:Q30) & " values (" & COUNT(Q2:Q30)/ROWS(Q2:Q30)*100 & "% complete)"
// Shows median with data completeness information

// Conditional median analysis
="Group 1 median: " & MEDIAN(IF(R1:R50="A", S1:S50)) & ", Group 2: " & MEDIAN(IF(R1:R50="B", S1:S50))
// Calculates medians for different groups (requires array formula)
```
