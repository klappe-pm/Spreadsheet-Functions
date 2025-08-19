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

# MIN

## MIN Description

Returns the minimum (smallest) value from a set of numbers or ranges. Ignores empty cells, text values, and logical values, focusing solely on numerical minimums. Essential for range analysis, baseline identification, quality control limits, and performance floor analysis in statistical evaluation.

> [!f(x)] MIN Syntax
>
> ```spreadsheets
> MIN(number1, [number2], [number3], ...)
> MIN(range)
> MIN(range1, range2, ...)
> ```
>
> **Parameters:**
> - `number1` (required): First number, cell reference, or range to evaluate
> - `number2, number3, ...` (optional): Additional numbers, cell references, or ranges (up to 255 arguments)

> [!f(x)] MIN Examples
>
> ```spreadsheets
> // Basic minimum calculation
> MIN(15, 42, 7, 89, 23) → 7
> 
> // Minimum of a range
> MIN(A1:A50) → lowest value in range A1:A50
> 
> // Cost analysis
> MIN(B2:B25) → 12.50 (lowest unit cost found)
> 
> // Temperature monitoring
> MIN(C1:C365) → -15.2 (lowest daily temperature recorded)
> 
> // Multi-range minimum
> MIN(D2:D10, F2:F10, H5) → combines multiple datasets for overall minimum
> ```

## Use Cases

### [[Baseline and floor analysis]]
- **Performance benchmarking**: Identify minimum acceptable performance levels across teams, departments, or operational periods
- **Cost optimization**: Find lowest costs, prices, or expenses for budget planning and vendor evaluation decisions
- **Quality assurance**: Establish minimum quality thresholds and identify underperforming products or processes
- **Safety standards**: Determine minimum safety margins and compliance levels required for regulatory adherence

### [[Risk assessment and worst-case analysis]]
- **Financial risk modeling**: Identify minimum portfolio values, worst-case scenarios, and downside protection levels
- **Supply chain analysis**: Track minimum inventory levels, shortest lead times, and most constrained resource availability
- **Capacity planning**: Determine minimum system capacity, lowest throughput rates, and bottleneck identification
- **Environmental monitoring**: Monitor minimum acceptable environmental conditions and critical threshold violations

### [[Statistical distribution analysis]]
- **Data range calculation**: Establish lower bounds for data normalization, scaling, and statistical modeling procedures
- **Outlier detection**: Identify extremely low values that may indicate data errors or unusual system behavior
- **Process control**: Set lower control limits for statistical process control and quality management systems
- **Market analysis**: Analyze minimum prices, lowest performance metrics, and competitive baseline establishment

## Related

### Similar Functions

- [[MAX]] - Returns maximum value, complementary to MIN for complete range analysis and statistical distribution characterization
- [[SMALL]] - Returns kth smallest value, providing detailed minimum value analysis beyond just the absolute minimum
- [[RANK]] - Shows position of values within dataset, contextualizing minimum values within overall distribution
- [[PERCENTILE]] - Calculates any percentile (MIN approximates 0th percentile) for comprehensive distribution analysis  
- [[MINIFS]] - Returns minimum value meeting specific criteria, enabling conditional minimum value analysis

## Range and Distribution Functions

### [[MAX]]
MIN and MAX together define the complete data range, essential for understanding data spread, establishing control limits, and comprehensive statistical analysis.

```spreadsheets
// Complete range analysis
="Range: " & MIN(A1:A50) & " to " & MAX(A1:A50) & " (span: " & (MAX(A1:A50)-MIN(A1:A50)) & ")"
// Provides comprehensive range summary: "Range: 23.4 to 89.7 (span: 66.3)"

// Range-based normalization
=(B5-MIN(B1:B40))/(MAX(B1:B40)-MIN(B1:B40))
// Min-max normalization: scales values to 0-1 range using extremes

// Range-based outlier detection
=IF(ABS(C5-MIN(C2:C30))<0.1*(MAX(C2:C30)-MIN(C2:C30)), "Near minimum - investigate", "Normal range")
// Identifies values suspiciously close to minimum
```

### [[AVERAGE]]
MIN with AVERAGE shows how extreme low values relate to central tendency, crucial for understanding data distribution and identifying performance gaps.

```spreadsheets
// Distance below mean analysis
=AVERAGE(D2:D35) - MIN(D2:D35) & " units between average (" & AVERAGE(D2:D35) & ") and minimum (" & MIN(D2:D35) & ")"
// Shows how far minimum falls below average

// Lower performance gap analysis
="Worst performer: " & MIN(E2:E25) & " vs average: " & AVERAGE(E2:E25) & " (-" & ((1-MIN(E2:E25)/AVERAGE(E2:E25))*100) & "%)"
// Shows lowest performance as percentage below average

// Distribution skewness indicator
=IF((AVERAGE(F1:F40)-MIN(F1:F40))>(MAX(F1:F40)-AVERAGE(F1:F40)), "Left-skewed distribution", "Right-skewed or symmetric")
// Uses minimum distance from mean to assess distribution shape
```

## Statistical Control Functions

### [[STDEV]]
MIN with STDEV enables z-score calculations for extreme low values, essential for statistical outlier detection and quality control limit establishment.

```spreadsheets
// Z-score for minimum value
=(MIN(G1:G30)-AVERAGE(G1:G30))/STDEV(G1:G30)
// Calculates how many standard deviations minimum is below mean

// Lower control limit calculation  
=AVERAGE(H2:H50) - 3*STDEV(H2:H50) & " LCL, actual min: " & MIN(H2:H50)
// Compares actual minimum with 3-sigma lower control limit

// Process capability assessment
=IF(MIN(I1:I100)>AVERAGE(I1:I100)-3*STDEV(I1:I100), "Process in control", "Minimum below control limits")
// Determines if minimum indicates out-of-control process
```

### [[COUNT]]
MIN with COUNT provides context for extreme value significance by showing sample size, essential for statistical interpretation of minimum values.

```spreadsheets
// Minimum with sample context
=MIN(J2:J40) & " minimum from n=" & COUNT(J2:J40) & " observations"
// Provides minimum value with sample size context

// Extreme value probability estimation
="Min " & MIN(K1:K25) & " has ~" & 1/COUNT(K1:K25)*100 & "% probability in this sample"
// Estimates probability of observing the minimum value

// Data completeness for minimum reliability
=IF(COUNT(L2:L30)/ROWS(L2:L30)>=0.9, "Min " & MIN(L2:L30) & " reliable", "Need more data")
// Validates minimum reliability based on data completeness
```

## Ranking and Comparison Functions

### [[SMALL]]
MIN equals SMALL(range,1). SMALL provides additional low extreme values beyond just the minimum, enabling comprehensive low-end analysis.

```spreadsheets
// Bottom values analysis
=MIN(M1:M50) & " (lowest), " & SMALL(M1:M50, 2) & " (2nd), " & SMALL(M1:M50, 3) & " (3rd) smallest"
// Shows bottom three values including minimum

// Gap analysis in low values
=(SMALL(N2:N35, 2)-MIN(N2:N35)) & " gap between lowest and 2nd lowest values"
// Analyzes gap between minimum and second-smallest value

// Bottom percentile identification
="Bottom 10%: values below " & SMALL(O1:O40, CEILING(COUNT(O1:O40)*0.1, 1))
// Identifies threshold for bottom 10% using SMALL function
```

### [[RANK]]
RANK provides the position context for MIN values, showing where the minimum ranks within the overall dataset distribution.

```spreadsheets
// Minimum value ranking verification
="Value " & P5 & " ranks #" & RANK(P5, P2:P30, 1) & " (min is " & MIN(P2:P30) & ")"
// Shows individual value ranking compared to minimum (ascending order)

// Percentile rank of minimum
=RANK(MIN(Q1:Q25), Q1:Q25, 1) & " rank out of " & COUNT(Q1:Q25) & " (" & RANK(MIN(Q1:Q25), Q1:Q25, 1)/COUNT(Q1:Q25)*100 & " percentile)"
// Shows minimum's percentile rank in distribution

// Performance tier classification
=IF(R5<=MIN(R2:R50)*1.1, "Bottom tier", IF(R5<=MIN(R2:R50)*1.3, "Low tier", "Higher tier"))
// Classifies values relative to minimum performance baseline
```

## Conditional Logic Functions

### [[IF]]
MIN enables conditional logic for threshold analysis, quality control decisions, and automated alert systems based on minimum value detection.

```spreadsheets
// Quality control threshold
=IF(MIN(S1:S25)<10, "ALERT: Value below minimum threshold", "All values acceptable")
// Triggers alert when any value falls below acceptable minimum

// Performance improvement targeting
=IF(MIN(T2:T30)<AVERAGE(T2:T30)*0.7, "Focus on improving lowest performers", "Performance spread acceptable")
// Identifies when minimum performers need attention

// Safety compliance monitoring
=IF(MIN(U1:U50)>=5, "Safety standards met", "CRITICAL: Safety violation detected")
// Monitors minimum safety levels for compliance
```

## Commonly Used With Functions Examples

### Quality Control Dashboard
```spreadsheets
// Process monitoring with control limits
="Process: " & $A$1 & " | Min: " & MIN(B2:B50) & " | Max: " & MAX(B2:B50) & " | Range: " & (MAX(B2:B50)-MIN(B2:B50)) & " | Status: " & IF(AND(MIN(B2:B50)>=C1, MAX(B2:B50)<=D1), "✅ IN SPEC", "⚠️ OUT OF SPEC")
// Complete process control monitoring with specification limits

// Statistical process control
=IF(MIN(E2:E30)<AVERAGE(E2:E30)-3*STDEV(E2:E30), "🚨 LOWER CONTROL VIOLATION: " & MIN(E2:E30), "✅ Process stable, min: " & MIN(E2:E30))
// Lower control limit monitoring with statistical thresholds
```

### Cost Analysis System
```spreadsheets
// Vendor cost comparison
="Best Price: $" & MIN(F2:F10) & " | Worst: $" & MAX(F2:F10) & " | Savings: $" & (MAX(F2:F10)-MIN(F2:F10)) & " | Vendor: " & INDEX(G2:G10, MATCH(MIN(F2:F10), F2:F10, 0))
// Complete cost analysis with vendor identification

// Budget optimization
=IF(MIN(H2:H25)>0, "All categories funded, min: $" & MIN(H2:H25), "BUDGET DEFICIT: " & ABS(MIN(H2:H25)) & " shortfall in " & INDEX(I2:I25, MATCH(MIN(H2:H25), H2:H25, 0)))
// Budget adequacy analysis with deficit identification
```

### Performance Management
```spreadsheets
// Team performance analysis
="Team: " & $J$1 & " | Top: " & MAX(K2:K20) & " | Bottom: " & MIN(K2:K20) & " | Spread: " & ROUND((MAX(K2:K20)-MIN(K2:K20))/AVERAGE(K2:K20)*100,1) & "% | " & IF(MIN(K2:K20)/AVERAGE(K2:K20)<0.8, "🎯 COACHING NEEDED", "✅ BALANCED TEAM")
// Performance spread analysis with coaching recommendations

// Improvement tracking
="Period: " & L1 & " | Current Min: " & MIN(M2:M30) & " | Previous: " & MIN(N2:N30) & " | Change: " & ROUND((MIN(M2:M30)-MIN(N2:N30))/MIN(N2:N30)*100,1) & "% | " & IF(MIN(M2:M30)>MIN(N2:N30), "⬆️ IMPROVING", "⬇️ DECLINING")
// Period-over-period minimum performance tracking
```
