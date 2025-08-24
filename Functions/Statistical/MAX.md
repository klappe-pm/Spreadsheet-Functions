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
# MAX

## MAX Description

Returns the maximum (largest) value from a set of numbers or ranges. Ignores empty cells, text values, and logical values, focusing solely on numerical extremes. Essential for range analysis, outlier detection, quality control limits, and performance benchmarking in statistical analysis.

> [!f(x)] MAX Syntax
>
> ```spreadsheets
> MAX(number1, [number2], [number3], ...)
> MAX(range)
> MAX(range1, range2, ...)
> ```
>
> **Parameters:**
> - `number1` (required): First number, cell reference, or range to evaluate
> - `number2, number3, ...` (optional): Additional numbers, cell references, or ranges (up to 255 arguments)

> [!f(x)] MAX Examples
>
> ```spreadsheets
> // Basic maximum calculation
> MAX(15, 42, 7, 89, 23) → 89
> 
> // Maximum of a range
> MAX(A1:A50) → highest value in range A1:A50
> 
> // Performance analysis
> MAX(B2:B25) → 156.7 (best quarterly performance)
> 
> // Temperature monitoring
> MAX(C1:C365) → 98.6 (highest daily temperature recorded)
> 
> // Multi-range maximum
> MAX(D2:D10, F2:F10, H5) → combines multiple datasets for overall maximum
> ```

## Use Cases

### [[Extreme value analysis and outlier detection]]
- **Statistical process control**: Identify maximum values in manufacturing data to establish upper control limits and detect process variations
- **Environmental monitoring**: Track maximum pollution levels, temperature readings, and rainfall amounts for regulatory compliance reporting
- **Financial risk assessment**: Analyze maximum losses, drawdowns, and volatility spikes for risk management and stress testing procedures
- **Performance benchmarking**: Identify peak performance metrics across teams, departments, or time periods for best practice identification

### [[Quality control and specification limits]]  
- **Manufacturing tolerance analysis**: Establish upper specification limits based on maximum acceptable product dimensions and performance parameters
- **Service level monitoring**: Track maximum response times, queue lengths, and processing delays for service quality assurance
- **Safety compliance monitoring**: Monitor maximum exposure levels, accident rates, and incident frequencies for workplace safety management
- **Capacity planning analysis**: Determine maximum resource utilization levels for infrastructure planning and scaling decisions

### [[Range analysis and data distribution]]
- **Market analysis**: Calculate price ranges by finding maximum and minimum values across different markets and time periods
- **Academic performance assessment**: Identify highest test scores, grade distributions, and achievement ranges for educational evaluation
- **Sales performance tracking**: Analyze maximum sales figures across territories, products, and sales representatives for territory optimization
- **Scientific experiment analysis**: Determine measurement ranges and identify potential outliers in experimental data collection

## Related

### Similar Functions

- [[MIN]] - Returns minimum value, complementary to MAX for complete range analysis and statistical distribution characterization
- [[LARGE]] - Returns kth largest value, providing more detailed extreme value analysis beyond just the maximum
- [[RANK]] - Shows position of values within dataset, contextualizing maximum values within overall distribution
- [[PERCENTILE]] - Calculates any percentile (MAX approximates 100th percentile) for comprehensive distribution analysis
- [[MAXIFS]] - Returns maximum value meeting specific criteria, enabling conditional extreme value analysis

## Range and Distribution Functions

### [[MIN]]
MAX and MIN together define the complete data range, essential for understanding data spread, establishing control limits, and identifying outliers in statistical analysis.

```spreadsheets
// Complete range analysis
="Range: " & MIN(A1:A50) & " to " & MAX(A1:A50) & " (span: " & (MAX(A1:A50)-MIN(A1:A50)) & ")"
// Provides comprehensive range summary: "Range: 23.4 to 89.7 (span: 66.3)"

// Range-based outlier detection
=IF(OR(B5>MAX(B2:B30)-0.1*(MAX(B2:B30)-MIN(B2:B30)), B5<MIN(B2:B30)+0.1*(MAX(B2:B30)-MIN(B2:B30))), "Extreme value", "Normal range")
// Identifies values in outer 10% of range

// Normalization using range
=(C5-MIN(C1:C40))/(MAX(C1:C40)-MIN(C1:C40))
// Min-max normalization: scales values to 0-1 range using extremes
```

### [[AVERAGE]]  
MAX with AVERAGE shows how extreme values relate to central tendency, crucial for understanding data distribution characteristics and identifying potential outliers.

```spreadsheets
// Distance from mean analysis
=MAX(D2:D35) & " maximum is " & (MAX(D2:D35)-AVERAGE(D2:D35)) & " units above mean of " & AVERAGE(D2:D35)
// Shows maximum's deviation from average

// Upper quartile approximation
=IF(MAX(E1:E40)>AVERAGE(E1:E40)+2*STDEV(E1:E40), "Potential outlier", "Within expected range")
// Uses maximum to detect outliers beyond 2 standard deviations

// Performance ranking context
="Top performer: " & MAX(F2:F25) & " vs average: " & AVERAGE(F2:F25) & " (+" & ((MAX(F2:F25)/AVERAGE(F2:F25)-1)*100) & "%)"
// Shows top performance as percentage above average
```

## Statistical Control Functions

### [[STDEV]]
MAX with STDEV enables z-score calculations for extreme values, essential for statistical outlier detection and quality control limit establishment.

```spreadsheets
// Z-score for maximum value
=(MAX(G1:G30)-AVERAGE(G1:G30))/STDEV(G1:G30)
// Calculates how many standard deviations maximum is from mean

// Upper control limit calculation
=AVERAGE(H2:H50) + 3*STDEV(H2:H50) & " UCL, actual max: " & MAX(H2:H50)
// Compares actual maximum with 3-sigma control limit

// Process capability assessment
=IF(MAX(I1:I100)<AVERAGE(I1:I100)+3*STDEV(I1:I100), "Process in control", "Maximum exceeds control limits")
// Determines if maximum indicates out-of-control process
```

### [[COUNT]]
MAX with COUNT provides context for extreme value significance by showing sample size, essential for statistical interpretation of maximum values.

```spreadsheets
// Maximum with sample context
=MAX(J2:J40) & " maximum from n=" & COUNT(J2:J40) & " observations"
// Provides maximum value with sample size context

// Extreme value probability estimation
="Max " & MAX(K1:K25) & " has ~" & 1/COUNT(K1:K25)*100 & "% probability in this sample"
// Estimates probability of observing the maximum value

// Data completeness for maximum reliability
=IF(COUNT(L2:L30)/ROWS(L2:L30)>=0.9, "Max " & MAX(L2:L30) & " reliable", "Need more data")
// Validates maximum reliability based on data completeness
```

## Ranking and Comparison Functions

### [[LARGE]]
MAX equals LARGE(range,1). LARGE provides additional extreme values beyond just the maximum, enabling more comprehensive extreme value analysis.

```spreadsheets
// Top values analysis
=MAX(M1:M50) & " (1st), " & LARGE(M1:M50, 2) & " (2nd), " & LARGE(M1:M50, 3) & " (3rd) largest"
// Shows top three values including maximum

// Gap analysis in extreme values
=(MAX(N2:N35)-LARGE(N2:N35, 2)) & " gap between 1st and 2nd highest values"
// Analyzes gap between maximum and second-largest value

// Top percentile identification
="Top 10%: values above " & LARGE(O1:O40, CEILING(COUNT(O1:O40)*0.1, 1))
// Identifies threshold for top 10% using LARGE function
```

### [[RANK]]
RANK provides the position context for MAX values, showing where the maximum ranks within the overall dataset distribution.

```spreadsheets
// Maximum value ranking verification
="Value " & P5 & " ranks #" & RANK(P5, P2:P30, 0) & " (max is " & MAX(P2:P30) & ")"
// Shows individual value ranking compared to maximum

// Percentile rank of maximum
=RANK(MAX(Q1:Q25), Q1:Q25, 0) & " rank out of " & COUNT(Q1:Q25) & " (" & (1-RANK(MAX(Q1:Q25), Q1:Q25, 0)/COUNT(Q1:Q25))*100 & " percentile)"
// Shows maximum's percentile rank in distribution

// Performance tier classification
=IF(R5>=MAX(R2:R50)*0.9, "Top tier", IF(R5>=MAX(R2:R50)*0.7, "High tier", "Lower tier"))
// Classifies values relative to maximum performance
```
