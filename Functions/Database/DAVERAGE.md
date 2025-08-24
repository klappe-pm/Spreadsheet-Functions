---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- database
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- database
- excel
- sheets
---
# DAVERAGE

## DAVERAGE Description

Calculates the arithmetic mean (average) of values in a database that match specified criteria by evaluating records against multiple conditions. DAVERAGE works with structured data where the first row contains field headers and subsequent rows contain data records.

> [!f(x)] DAVERAGE Syntax
>
> ```spreadsheets
> DAVERAGE(database, field, criteria)
> ```
>
> **Parameters:**
> - `database` (required): The range of cells that makes up the database or list including headers
> - `field` (required): Column to average - can be column label (in quotes) or column number  
> - `criteria` (required): Range containing conditions that specify which records to average

> [!f(x)] DAVERAGE Examples
>
> ```spreadsheets
> // Average sales where region is "North"
> DAVERAGE(A1:E20, "Sales", G1:G2) → 3250.75
> 
> // Average score where grade > 80 and subject = "Math"  
> DAVERAGE(A1:F100, "Score", H1:I3) → 87.5
> 
> // Average price for specific product category
> DAVERAGE(Database, "Price", CategoryCriteria) → 24.99
> 
> // Average response time for department "Support"
> DAVERAGE(A1:D50, "ResponseTime", F1:F2) → 2.3
> 
> // Average salary where experience > 5 years
> DAVERAGE(Employees, "Salary", ExperienceCriteria) → 75000
> ```

## Use Cases

### [[Performance analysis]]
- **Employee productivity metrics**: Calculate average sales performance by department to identify training needs and set realistic targets
- **Customer service benchmarks**: Determine average response times and resolution rates to establish service level agreements and optimize processes
- **Manufacturing efficiency**: Track average production output per shift to identify bottlenecks and optimize resource allocation
- **Quality control standards**: Monitor average defect rates by production line to maintain quality standards and identify improvement opportunities
- **Website analytics**: Analyze average page load times and user session durations to optimize user experience and technical performance

### [[Financial planning]]
- **Budget forecasting**: Calculate average monthly expenses by category to create accurate annual budgets and identify spending patterns
- **Revenue projections**: Determine average sales per customer segment to forecast future revenue and plan resource allocation
- **Cost per acquisition**: Average marketing spend per customer by channel to optimize advertising budget allocation and ROI
- **Profit margin analysis**: Calculate average profit margins by product line to inform pricing strategies and product mix decisions
- **Investment performance**: Track average returns by investment type to guide portfolio allocation and risk management strategies

### [[Academic assessment]]
- **Grade distribution analysis**: Calculate average scores by subject and grade level to identify curriculum strengths and areas needing improvement
- **Student progress tracking**: Monitor average improvement rates across different student populations to personalize learning interventions
- **Teacher effectiveness**: Determine average student performance by instructor to inform professional development and recognition programs
- **Standardized test analysis**: Compute average scores by demographic groups to ensure educational equity and identify achievement gaps
- **Course difficulty calibration**: Analyze average completion times and success rates to balance academic rigor with accessibility

## Related

### Similar Functions

- [[DSUM]] - Sums values instead of averaging for database records matching criteria
- [[DCOUNT]] - Counts records matching criteria instead of averaging values  
- [[DMAX]] - Finds maximum value in database records matching criteria
- [[DMIN]] - Finds minimum value in database records matching criteria
- [[DGET]] - Retrieves single value from database record matching criteria

## Database Statistical Functions

### [[DSUM]]
Used with DAVERAGE to compare total values against per-record averages. Together they provide complete statistical context for understanding data distribution and aggregate performance.

```spreadsheets
// Sales performance comprehensive analysis
="Total Sales: " & DSUM(A1:F100,"Sales",H1:H2) & ", Average per Sale: " & DAVERAGE(A1:F100,"Sales",H1:H2)
// Example: "Total Sales: 125000, Average per Sale: 2500"

// Department payroll summary
=DSUM(Employees,"Salary",DeptCriteria) & " total payroll, " & DAVERAGE(Employees,"Salary",DeptCriteria) & " average salary"
// Shows both aggregate compensation and normalized per-employee view

// Revenue distribution analysis
="Total: $" & DSUM(Revenue,"Amount",Criteria) & " | Avg: $" & DAVERAGE(Revenue,"Amount",Criteria) & 
" | Count: " & DCOUNT(Revenue,"Amount",Criteria)
// Complete statistical summary combining sum, average, and count
```

### [[DCOUNT]]  
Frequently paired with DAVERAGE to validate sample sizes and ensure statistical significance. DCOUNT confirms the number of records being averaged and helps assess data reliability.

```spreadsheets
// Average with sample size validation
=DAVERAGE(A1:E100,"Score",G1:G2) & " (n=" & DCOUNT(A1:E100,"Score",G1:G2) & ")"
// Returns: "87.5 (n=24)" showing average with sample size

// Minimum sample size enforcement
=IF(DCOUNT(Database,"Value",Criteria)>=10, DAVERAGE(Database,"Value",Criteria), "Insufficient sample size")
// Only calculates average if at least 10 records match criteria

// Statistical confidence validation
=DAVERAGE(Data,"Result",Criteria) & " ± " & (DSTDEV(Data,"Result",Criteria)/SQRT(DCOUNT(Data,"Result",Criteria)))
// Shows average with standard error margin for confidence intervals
```

## Comparison Functions

### [[DMAX]]
Combined with DAVERAGE to understand performance distribution and identify outliers above the mean. DMAX shows peak performance while DAVERAGE provides baseline context.

```spreadsheets
// Performance range analysis
="Best: " & DMAX(A1:E200,"Performance",G1:G2) & " vs Average: " & DAVERAGE(A1:E200,"Performance",G1:G2)
// Shows gap between top performer and typical performance

// Outlier detection using averages and maximums
=IF(DMAX(B1:B15,"Value",Criteria)>DAVERAGE(B1:B15,"Value",Criteria)*1.5, "Outlier detected", "Normal distribution")
// Identifies values significantly above average (50% higher)

// Goal setting based on current performance
="Current Avg: " & DAVERAGE(Sales,"Amount",Criteria) & " | Target: " & DAVERAGE(Sales,"Amount",Criteria)*1.2
// Sets performance targets 20% above current average
```

### [[DMIN]]
Works with DAVERAGE to show complete performance range and identify underperformers. DMIN reveals lowest values while DAVERAGE provides context for improvement potential.

```spreadsheets
// Complete performance summary
="Range: " & DMIN(A1:F50,"Score",H1:H3) & " to " & DMAX(A1:F50,"Score",H1:H3) & ", Average: " & DAVERAGE(A1:F50,"Score",H1:H3)
// Provides full statistical summary with central tendency

// Below-average performance analysis
="Bottom: " & DMIN(Performance,"Rating",Criteria) & " | Gap from Average: " & 
(DAVERAGE(Performance,"Rating",Criteria)-DMIN(Performance,"Rating",Criteria))
// Shows improvement potential for lowest performer

// Quality threshold validation
=IF(DMIN(Products,"Quality",Criteria)<DAVERAGE(Products,"Quality",Criteria)*0.8, "Quality alert: minimum too low", "Acceptable range")
// Alerts when minimum falls more than 20% below average
```

## Statistical Functions

### [[DSTDEV]]
Essential companion to DAVERAGE for understanding data variability around the mean. DSTDEV measures spread while DAVERAGE provides central tendency for complete statistical analysis.

```spreadsheets
// Performance variability analysis
="Average: " & DAVERAGE(A1:E100,"Score",Criteria) & " ± " & DSTDEV(A1:E100,"Score",Criteria)
// Shows average score with standard deviation range

// Consistency evaluation
=IF(DSTDEV(Performance,"Rating",Criteria)<DAVERAGE(Performance,"Rating",Criteria)*0.2, "Consistent", "High variability")
// Identifies whether performance is consistent (low standard deviation relative to mean)

// Quality control limits
="Target: " & DAVERAGE(Quality,"Measure",Criteria) & " | Control Limits: ±" & 2*DSTDEV(Quality,"Measure",Criteria)
// Establishes quality control boundaries at 2 standard deviations from mean
```

## Conditional Logic Functions

### [[IF]]
Critical for conditional averaging and data validation. IF enables DAVERAGE to work with dynamic criteria, handle empty result sets gracefully, and provide contextual results.

```spreadsheets
// Conditional average with validation
=IF(DCOUNT(A1:E100,"Value",G1:G2)>5, DAVERAGE(A1:E100,"Value",G1:G2), "Insufficient data for average")
// Only calculates average with adequate sample size

// Performance tier classification
=IF(DAVERAGE(B2:B15,"Score",Criteria)>=90, "Excellent", IF(DAVERAGE(B2:B15,"Score",Criteria)>=70, "Good", "Needs Improvement"))
// Categorizes average performance into tiers

// Error-resistant averaging
=IF(ISERROR(DAVERAGE(Database,"Values",CriteriaRange)), "Invalid criteria or data", DAVERAGE(Database,"Values",CriteriaRange))
// Prevents error display when DAVERAGE encounters invalid conditions
```

### [[AVERAGEIF]]
Alternative to DAVERAGE for simpler single-criterion averaging. AVERAGEIF works with single columns while DAVERAGE handles complex multi-field databases with multiple criteria.

```spreadsheets
// Compare DAVERAGE vs AVERAGEIF approaches
=DAVERAGE(A1:C100,"Score",E1:E2) & " (DAVERAGE) vs " & AVERAGEIF(B1:B100,">=80",C1:C100) & " (AVERAGEIF)"
// Shows difference between database and range-based averaging

// Method selection based on criteria complexity
=IF(ROWS(CriteriaRange)>2, DAVERAGE(Database,"Value",CriteriaRange), AVERAGEIF(RangeA,Condition,RangeB))
// Uses DAVERAGE for complex criteria, AVERAGEIF for simple conditions

// Validation between DAVERAGE and AVERAGEIF results
=IF(ABS(DAVERAGE(Data,"Amount",SingleCriteria)-AVERAGEIF(Data,"Amount",">100"))<0.01, "Verified", "Discrepancy")
// Confirms DAVERAGE accuracy against AVERAGEIF for single criteria
```

## Commonly Used With Functions Examples

### Employee Performance Review System
```spreadsheets
// Comprehensive performance analysis with percentile ranking
=DAVERAGE(Performance,"Rating",EmployeeCriteria) & " avg rating | " &
IF(DAVERAGE(Performance,"Rating",EmployeeCriteria)>DAVERAGE(Performance,"Rating",AllEmployees)*1.1, "Top 25%", "Standard")
// Individual performance versus company average with tier classification

// Department comparison with statistical significance
="Dept Avg: " & DAVERAGE(Performance,"Score",DeptCriteria) & " | Company Avg: " & DAVERAGE(Performance,"Score",AllDepts) & 
" | Significant: " & IF(ABS(DAVERAGE(Performance,"Score",DeptCriteria)-DAVERAGE(Performance,"Score",AllDepts))>DSTDEV(Performance,"Score",AllDepts), "Yes", "No")
// Statistical comparison between department and overall company performance
```

### Student Academic Progress Tracking  
```spreadsheets
// Grade trend analysis with improvement tracking
="Current Avg: " & DAVERAGE(Grades,"Score",CurrentSemester) & 
" | Previous: " & DAVERAGE(Grades,"Score",PreviousSemester) & 
" | Improvement: " & ROUND((DAVERAGE(Grades,"Score",CurrentSemester)-DAVERAGE(Grades,"Score",PreviousSemester))/DAVERAGE(Grades,"Score",PreviousSemester)*100,1) & "%"
// Shows semester-over-semester improvement percentage

// Class ranking with percentile calculations
="Student Avg: " & DAVERAGE(StudentGrades,"Score",StudentCriteria) & 
" | Class Avg: " & DAVERAGE(StudentGrades,"Score",ClassCriteria) & 
" | Percentile: " & ROUND(COUNTIFS(GradeRange,"<"&DAVERAGE(StudentGrades,"Score",StudentCriteria))/COUNTA(GradeRange)*100,0) & "%"
// Individual student performance with class context and percentile ranking
```

### Sales Performance Dashboard
```spreadsheets
// Territory performance with goal attainment
="Territory Avg: $" & DAVERAGE(Sales,"Revenue",TerritoryCriteria) & 
" | Goal: $" & TerritoryGoal & " | Attainment: " & ROUND(DAVERAGE(Sales,"Revenue",TerritoryCriteria)/TerritoryGoal*100,1) & "%" &
" | vs Company: " & ROUND(DAVERAGE(Sales,"Revenue",TerritoryCriteria)/DAVERAGE(Sales,"Revenue",AllTerritories)*100-100,1) & "%"
// Complete territory analysis with goal tracking and company comparison

// Seasonal performance analysis with trend identification
=DAVERAGE(Sales,"Amount",Q1Criteria) & "/" & DAVERAGE(Sales,"Amount",Q2Criteria) & "/" & 
DAVERAGE(Sales,"Amount",Q3Criteria) & "/" & DAVERAGE(Sales,"Amount",Q4Criteria) & 
" | Trend: " & IF(DAVERAGE(Sales,"Amount",Q4Criteria)>DAVERAGE(Sales,"Amount",Q1Criteria),"Growing","Declining")
// Quarterly average comparison with year-over-year trend analysis
```

### Customer Satisfaction Analysis
```spreadsheets
// Service quality metrics with benchmark comparison
="Satisfaction: " & DAVERAGE(Surveys,"Rating",ServiceCriteria) & "/10" &
" | Response Time: " & DAVERAGE(Support,"Hours",ServiceCriteria) & "h avg" &
" | vs Industry: " & IF(DAVERAGE(Surveys,"Rating",ServiceCriteria)>IndustryBenchmark,"Above","Below") & " standard"
// Multi-metric service analysis with industry benchmarking

// Customer segment analysis with value correlation
="Avg Satisfaction: " & DAVERAGE(Customers,"Satisfaction",SegmentCriteria) & 
" | Avg Spend: $" & DAVERAGE(Customers,"AnnualSpend",SegmentCriteria) & 
" | Correlation: " & IF(DAVERAGE(Customers,"Satisfaction",SegmentCriteria)>7 AND DAVERAGE(Customers,"AnnualSpend",SegmentCriteria)>5000,"High Value","Review")
// Customer satisfaction and spending correlation analysis
```

### Quality Control Monitoring
```spreadsheets
// Production quality trends with control limits
="Current Avg: " & DAVERAGE(Production,"QualityScore",CurrentPeriod) & 
" | Target: " & QualityTarget & " | Status: " & 
IF(DAVERAGE(Production,"QualityScore",CurrentPeriod)>=QualityTarget*0.95,"On Target","Below Standard") &
" | Variation: ±" & DSTDEV(Production,"QualityScore",CurrentPeriod)
// Comprehensive quality analysis with target comparison and variation monitoring
```
