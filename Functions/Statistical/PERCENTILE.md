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
# PERCENTILE

## PERCENTILE Description

Calculates the k-th percentile of values in a dataset, where k is between 0 and 1. Returns the value below which k% of data points fall. Uses exclusive method that requires the percentile to be strictly between 0 and 1. Essential for performance evaluation, benchmarking, quality control, and statistical analysis.

> [!f(x)] PERCENTILE Syntax
>
> ```spreadsheets
> PERCENTILE(array, k)
> ```
>
> **Parameters:**
> - `array` (required): Range or array of numeric values
> - `k` (required): Percentile rank between 0 and 1 (exclusive), where 0.5 = 50th percentile (median)

> [!f(x)] PERCENTILE Examples
>
> ```spreadsheets
> // 50th percentile (median) of test scores
> PERCENTILE({65,70,75,80,85,90,95}, 0.5) → 80 (median value)
> 
> // 90th percentile for performance benchmarking
> PERCENTILE(A2:A50, 0.9) → 87.5 (90% of values below this)
> 
> // 25th percentile (first quartile) of sales data
> PERCENTILE(B1:B100, 0.25) → 15000 (Q1 value)
> 
> // 95th percentile for quality control limits
> PERCENTILE(C2:C200, 0.95) → 99.2 (upper control threshold)
> 
> // 10th percentile for risk assessment
> PERCENTILE(D1:D75, 0.1) → 5.8 (bottom 10% threshold)
> ```

## Use Cases

### [[Performance evaluation and ranking]]
- **Employee assessment**: Determine performance thresholds for salary bands, promotions, and performance improvement plans
- **Academic grading**: Establish grade cutoffs based on test score distributions for curved grading systems
- **Sales benchmarking**: Set sales targets and identify top performers using historical performance percentiles
- **Quality ratings**: Create quality assessment categories based on customer satisfaction score distributions

### [[Risk management and compliance]]
- **Value-at-Risk calculation**: Determine portfolio loss thresholds at specified confidence levels for risk reporting requirements
- **Credit risk assessment**: Set credit approval thresholds based on historical default rate percentiles across customer segments
- **Operational risk monitoring**: Establish control limits for process metrics using percentile-based thresholds
- **Regulatory compliance**: Meet industry requirements for percentile-based reporting and risk capital calculations

### [[Quality control and process improvement]]
- **Manufacturing tolerances**: Set specification limits based on process capability percentiles to maintain quality standards
- **Service level agreements**: Define SLA thresholds using response time percentiles for customer service commitments
- **Defect rate monitoring**: Establish quality control limits using defect rate percentiles for continuous improvement
- **Process capability analysis**: Evaluate process performance using percentile-based capability indices and improvement targets

## Related

### Similar Functions

- [[PERCENTILE.INC]] - Inclusive percentile calculation that allows k=0 and k=1 (includes endpoints)
- [[PERCENTILE.EXC]] - Exclusive percentile calculation identical to PERCENTILE function behavior
- [[QUARTILE]] - Calculates quartiles (25th, 50th, 75th percentiles) with simpler syntax
- [[MEDIAN]] - Returns 50th percentile (equivalent to PERCENTILE(array, 0.5))
- [[PERCENTRANK]] - Inverse function that finds percentile rank for a given value

## Statistical Summary Functions

### [[AVERAGE]]
PERCENTILE provides position-based statistics while AVERAGE gives central tendency, offering complementary views of data distribution.

```spreadsheets
// Central tendency vs positional analysis
="Mean: " & ROUND(AVERAGE(A1:A40), 2) & 
", Median (50th %ile): " & ROUND(PERCENTILE(A1:A40, 0.5), 2) & 
", Skew indicator: " & IF(AVERAGE(A1:A40)>PERCENTILE(A1:A40, 0.5), "Right-skewed", "Left-skewed")
// Compares mean and median to assess distribution shape

// Performance distribution summary
="Average performance: " & ROUND(AVERAGE(B2:B30), 1) & 
", Top 25% threshold: " & ROUND(PERCENTILE(B2:B30, 0.75), 1) & 
", Gap from mean: " & ROUND(PERCENTILE(B2:B30, 0.75) - AVERAGE(B2:B30), 1)
// Shows relationship between average performance and top quartile

// Quality assessment using both measures
="Process average: " & AVERAGE(C1:C50) & "±" & STDEV(C1:C50) & 
", 99% specification: " & PERCENTILE(C1:C50, 0.99) & 
", Meets target: " & IF(PERCENTILE(C1:C50, 0.99) < TARGET, "Yes", "No")
// Combines parametric (mean/SD) and non-parametric (percentile) approaches
```

### [[COUNT]]
COUNT validates sample size for reliable percentile calculations and ensures adequate data representation across the distribution.

```spreadsheets
// Sample size validation for percentiles
=IF(COUNT(D1:D25) >= 20, "Sample size adequate (n=" & COUNT(D1:D25) & "), 90th percentile: " & PERCENTILE(D1:D25, 0.9), "Need larger sample for reliable percentiles")
// Ensures minimum sample size for meaningful percentile calculation

// Data completeness assessment
="Valid observations: " & COUNT(E2:E100) & "/" & COUNTA(E2:E100) & 
" (" & ROUND(COUNT(E2:E100)/COUNTA(E2:E100)*100, 1) & "%), 75th percentile: " & PERCENTILE(E2:E100, 0.75)
// Shows data completeness impact on percentile reliability

// Confidence in percentile estimates
="Percentile confidence: " & IF(COUNT(F1:F60) > 30, "High (n=" & COUNT(F1:F60) & ")", "Moderate (n=" & COUNT(F1:F60) & ")") & 
", 95th percentile: " & PERCENTILE(F1:F60, 0.95)
// Assesses confidence level based on sample size for percentile estimation
```

## Distribution Analysis Functions

### [[QUARTILE]]
QUARTILE provides quick access to common percentiles (25th, 50th, 75th), while PERCENTILE offers flexibility for any percentile value.

```spreadsheets
// Complete quartile analysis using PERCENTILE
="Q1 (25th): " & PERCENTILE(G1:G35, 0.25) & 
", Q2 (50th): " & PERCENTILE(G1:G35, 0.5) & 
", Q3 (75th): " & PERCENTILE(G1:G35, 0.75) & 
", IQR: " & (PERCENTILE(G1:G35, 0.75) - PERCENTILE(G1:G35, 0.25))
// Uses PERCENTILE to calculate all quartiles and interquartile range

// Percentile vs QUARTILE comparison
="PERCENTILE method - Q1: " & PERCENTILE(H2:H40, 0.25) & ", Q3: " & PERCENTILE(H2:H40, 0.75) & 
", QUARTILE method - Q1: " & QUARTILE(H2:H40, 1) & ", Q3: " & QUARTILE(H2:H40, 3)
// Compares results between PERCENTILE and QUARTILE functions (should be identical)

// Extended percentile analysis beyond quartiles
="P10: " & PERCENTILE(I1:I50, 0.1) & ", P90: " & PERCENTILE(I1:I50, 0.9) & 
", P95: " & PERCENTILE(I1:I50, 0.95) & ", P99: " & PERCENTILE(I1:I50, 0.99)
// Uses PERCENTILE for analysis beyond standard quartiles
```

### [[PERCENTRANK]]
PERCENTILE and PERCENTRANK are inverse functions: PERCENTILE finds value for rank, PERCENTRANK finds rank for value.

```spreadsheets
// Inverse relationship demonstration
="Value at 75th percentile: " & PERCENTILE(J1:J30, 0.75) & 
", Rank of that value: " & PERCENTRANK(J1:J30, PERCENTILE(J1:J30, 0.75)) & 
" (should be 0.75)"
// Shows perfect inverse relationship between functions

// Performance ranking and thresholds
="Performance threshold (80th %ile): " & PERCENTILE(K2:K45, 0.8) & 
", Your score " & K5 & " ranks at: " & ROUND(PERCENTRANK(K2:K45, K5)*100, 1) & " percentile"
// Combines threshold setting with individual performance ranking

// Quality control limits and assessment
="Control limit (99th %ile): " & PERCENTILE(L1:L100, 0.99) & 
", Current value " & L101 & " percentile: " & ROUND(PERCENTRANK(L1:L100, L101)*100, 1) & "%"
// Uses percentile for limit setting and percentrank for current assessment
```

## Statistical Testing Functions

### [[IF]]
IF enables conditional percentile calculations, threshold-based decisions, and error handling for robust analysis.

```spreadsheets
// Conditional percentile with sample size validation
=IF(COUNT(M1:M40) >= 10, PERCENTILE(M1:M40, 0.9), "Insufficient data for 90th percentile")
// Ensures adequate sample size before calculating percentiles

// Performance category assignment using percentiles
=IF(N5 >= PERCENTILE(N1:N50, 0.9), "Top 10%", IF(N5 >= PERCENTILE(N1:N50, 0.75), "Upper quartile", IF(N5 >= PERCENTILE(N1:N50, 0.5), "Above median", "Below median")))
// Categorizes individual performance based on percentile thresholds

// Quality control alerts using percentile thresholds
=IF(O5 > PERCENTILE(O1:O30, 0.95), "ALERT: Value exceeds 95th percentile", IF(O5 < PERCENTILE(O1:O30, 0.05), "ALERT: Value below 5th percentile", "Within normal range"))
// Triggers alerts based on percentile-based control limits
```

### [[ROUND]]
ROUND improves readability of percentile results and ensures appropriate precision for reporting and decision-making.

```spreadsheets
// Formatted percentile reporting
="Performance Metrics:" & CHAR(10) & 
"25th percentile: " & ROUND(PERCENTILE(P1:P25, 0.25), 2) & CHAR(10) & 
"50th percentile: " & ROUND(PERCENTILE(P1:P25, 0.5), 2) & CHAR(10) & 
"75th percentile: " & ROUND(PERCENTILE(P1:P25, 0.75), 2) & CHAR(10) & 
"90th percentile: " & ROUND(PERCENTILE(P1:P25, 0.9), 2)
// Creates formatted percentile summary with appropriate precision

// Business reporting with rounded percentiles
="Quality Thresholds - " & 
"Good (75th %ile): " & ROUND(PERCENTILE(Q2:Q50, 0.75), 1) & ", " & 
"Excellent (90th %ile): " & ROUND(PERCENTILE(Q2:Q50, 0.9), 1) & ", " & 
"Outstanding (95th %ile): " & ROUND(PERCENTILE(Q2:Q50, 0.95), 1)
// Business-friendly percentile thresholds with appropriate rounding

// Statistical summary with consistent precision
="Distribution Summary (n=" & COUNT(R1:R40) & "): " & 
"P5=" & ROUND(PERCENTILE(R1:R40, 0.05), 3) & ", " & 
"P95=" & ROUND(PERCENTILE(R1:R40, 0.95), 3) & ", " & 
"Range=" & ROUND(PERCENTILE(R1:R40, 0.95) - PERCENTILE(R1:R40, 0.05), 3)
// Consistent precision for statistical reporting
```

## Commonly Used With Functions Examples

### Performance Management and Benchmarking
```spreadsheets
// Comprehensive performance evaluation
="Employee Performance Analysis:" & CHAR(10) & 
"Score: " & A5 & " (Percentile: " & ROUND(PERCENTRANK(A1:A50, A5)*100,0) & "%)" & CHAR(10) & 
"Performance Bands:" & CHAR(10) & 
"• Exceeds Expectations (>80th): " & ROUND(PERCENTILE(A1:A50, 0.8),1) & "+" & CHAR(10) & 
"• Meets Expectations (20-80th): " & ROUND(PERCENTILE(A1:A50, 0.2),1) & "-" & ROUND(PERCENTILE(A1:A50, 0.8),1) & CHAR(10) & 
"• Needs Improvement (<20th): " & "<" & ROUND(PERCENTILE(A1:A50, 0.2),1) & CHAR(10) & 
"Category: " & IF(A5>=PERCENTILE(A1:A50,0.8),"Exceeds",IF(A5>=PERCENTILE(A1:A50,0.2),"Meets","Needs Improvement"))
// Complete performance evaluation with percentile-based categories
```

### Quality Control and Process Analysis
```spreadsheets
// Statistical process control using percentiles
="Process Control Chart (n=" & COUNT(B1:B100) & "):" & CHAR(10) & 
"Center Line (50th %ile): " & ROUND(PERCENTILE(B1:B100, 0.5), 2) & CHAR(10) & 
"Upper Control Limit (99.7th %ile): " & ROUND(PERCENTILE(B1:B100, 0.997), 2) & CHAR(10) & 
"Lower Control Limit (0.3rd %ile): " & ROUND(PERCENTILE(B1:B100, 0.003), 2) & CHAR(10) & 
"Current Status: " & IF(OR(C5>PERCENTILE(B1:B100,0.997), C5<PERCENTILE(B1:B100,0.003)), "OUT OF CONTROL", "IN CONTROL")
// Process control using percentile-based limits instead of standard deviation
```

### Risk Assessment and Financial Analysis
```spreadsheets
// Value-at-Risk analysis using percentiles
="Portfolio Risk Analysis (n=" & COUNT(D1:D252) & " trading days):" & CHAR(10) & 
"Daily Returns:" & CHAR(10) & 
"• 95% VaR (worst 5%): " & ROUND(PERCENTILE(D1:D252, 0.05)*100, 2) & "%" & CHAR(10) & 
"• 99% VaR (worst 1%): " & ROUND(PERCENTILE(D1:D252, 0.01)*100, 2) & "%" & CHAR(10) & 
"• Expected Shortfall (avg of worst 5%): " & ROUND(AVERAGE(IF(D1:D252<=PERCENTILE(D1:D252,0.05),D1:D252))*100, 2) & "%" & CHAR(10) & 
"Risk Level: " & IF(PERCENTILE(D1:D252,0.05)<-0.05, "HIGH RISK", IF(PERCENTILE(D1:D252,0.05)<-0.02, "MODERATE RISK", "LOW RISK"))
// Comprehensive risk analysis using percentile-based measures
```
