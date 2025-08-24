---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - database
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-19
  - - aliases
    - []
  - - tags
    - []
---
# DMIN

## DMIN Description

Finds the minimum (lowest) value in a database that matches specified criteria by evaluating records against multiple conditions. DMIN works with structured data where the first row contains field headers and subsequent rows contain data records.

> [!f(x)] DMIN Syntax
>
> ```spreadsheets
> DMIN(database, field, criteria)
> ```
>
> **Parameters:**
> - `database` (required): The range of cells that makes up the database or list including headers
> - `field` (required): Column to find minimum - can be column label (in quotes) or column number  
> - `criteria` (required): Range containing conditions that specify which records to evaluate

> [!f(x)] DMIN Examples
>
> ```spreadsheets
> // Find lowest price where category is "Electronics"
> DMIN(A1:E20, "Price", G1:G2) → 29.99
> 
> // Find minimum response time where department = "Support"  
> DMIN(A1:F100, "ResponseTime", H1:I3) → 0.5
> 
> // Find lowest score in specific grade level
> DMIN(Database, "Score", GradeCriteria) → 62
> 
> // Find minimum inventory level for critical items
> DMIN(A1:D50, "StockLevel", F1:F2) → 3
> 
> // Find lowest salary where position = "Intern"
> DMIN(Employees, "Salary", InternCriteria) → 35000
> ```

## Use Cases

### [[Bottleneck identification]]
- **Performance baseline establishment**: Find minimum response times, throughput rates, or processing speeds to identify system bottlenecks and performance constraints
- **Resource constraint analysis**: Identify minimum available capacity, staffing levels, or budget allocations that limit operational effectiveness
- **Quality floor determination**: Find minimum acceptable quality scores, customer satisfaction ratings, or compliance levels to establish improvement baselines
- **Efficiency gap identification**: Locate minimum productivity levels, utilization rates, or output measures to focus improvement efforts where they're most needed
- **Service level monitoring**: Track minimum service delivery metrics to ensure all customers receive baseline service quality and identify underperforming areas

### [[Cost optimization]]
- **Budget floor analysis**: Identify minimum costs, prices, or expenses across categories to establish cost baselines and identify savings opportunities
- **Vendor comparison**: Find minimum supplier prices, delivery times, or service levels to negotiate better terms and optimize procurement strategies
- **Resource allocation**: Determine minimum resource requirements for projects, departments, or processes to optimize resource distribution and utilization
- **Pricing strategy**: Identify minimum competitor prices or market rates to develop competitive pricing while maintaining profitability margins
- **Operational efficiency**: Find minimum operational costs per unit, transaction, or customer to identify best practices and improvement targets

### [[Risk monitoring]]
- **Early warning systems**: Track minimum safety margins, buffer levels, or threshold values to trigger alerts before critical situations develop
- **Compliance validation**: Monitor minimum regulatory requirements, quality standards, or performance thresholds to ensure continuous compliance
- **Capacity planning**: Identify minimum capacity levels during peak demand to ensure adequate resource provisioning and service availability
- **Financial stability**: Track minimum cash flows, profit margins, or financial ratios to maintain operational stability and meet obligations
- **Security assessment**: Monitor minimum security scores, access controls, or incident response times to maintain acceptable risk levels

## Related

### Similar Functions

- [[DMAX]] - Finds maximum value instead of minimum for database records matching criteria
- [[DAVERAGE]] - Calculates average instead of minimum for database records matching criteria
- [[DSUM]] - Sums values instead of finding minimum for database records matching criteria
- [[DCOUNT]] - Counts records instead of finding minimum for database records matching criteria
- [[DGET]] - Retrieves single value from database record matching criteria

## Database Range Functions

### [[DMAX]]
Used with DMIN to show complete value range and identify performance spread. Together they provide full context for understanding data distribution and identifying improvement opportunities.

```spreadsheets
// Complete performance range with improvement potential
="Lowest: " & DMIN(A1:F50,"Performance",H1:H3) & " | Highest: " & DMAX(A1:F50,"Performance",H1:H3) & 
" | Improvement Gap: " & (DMAX(A1:F50,"Performance",H1:H3)-DMIN(A1:F50,"Performance",H1:H3))
// Shows full performance spectrum and quantifies improvement opportunity

// Quality control range validation
=IF((DMAX(Quality,"Measure",Criteria)-DMIN(Quality,"Measure",Criteria))<ToleranceLimit,"Within Spec","Exceeds Tolerance")
// Validates that range between maximum and minimum stays within acceptable tolerance

// Consistency analysis with range assessment
="Most Consistent: " & IF((DMAX(Teams,"Variance",Criteria)-DMIN(Teams,"Variance",Criteria))<1,"Team Alpha","Team Beta") & 
" | Range: " & (DMAX(Teams,"Variance",Criteria)-DMIN(Teams,"Variance",Criteria))
// Identifies most consistent performer based on minimum range between max and min
```

### [[DAVERAGE]]  
Frequently paired with DMIN to compare worst performance against typical performance. Shows relationship between minimum risk and average expectation.

```spreadsheets
// Below-average performance analysis
="Worst: " & DMIN(A1:F100,"Rating",H1:H2) & " | Average: " & DAVERAGE(A1:F100,"Rating",H1:H2) & 
" | Gap: " & (DAVERAGE(A1:F100,"Rating",H1:H2)-DMIN(A1:F100,"Rating",H1:H2)) & 
" (" & ROUND((DAVERAGE(A1:F100,"Rating",H1:H2)-DMIN(A1:F100,"Rating",H1:H2))/DAVERAGE(A1:F100,"Rating",H1:H2)*100,1) & "%)"
// Shows improvement needed to bring minimum performance up to average level

// Risk assessment with baseline comparison
=IF(DMIN(Risk,"Score",Criteria)<DAVERAGE(Risk,"Score",Criteria)*0.5,"High risk individual identified","Acceptable risk range")
// Alerts when minimum risk score falls below 50% of average, indicating potential issues

// Support threshold analysis
="Support Floor: " & DMIN(Support,"ResponseTime",Criteria) & "h | Target: " & DAVERAGE(Support,"ResponseTime",Criteria) & 
"h | Improvement Needed: " & (DAVERAGE(Support,"ResponseTime",Criteria)-DMIN(Support,"ResponseTime",Criteria)) & "h"
// Shows how much improvement is needed to bring worst response time up to average
```

## Statistical Analysis Functions

### [[DSTDEV]]
Combined with DMIN for outlier detection and statistical quality control. DMIN identifies extreme low values while DSTDEV provides context for their statistical significance.

```spreadsheets
// Statistical outlier detection for underperformers
=IF(DMIN(A1:E100,"Score",Criteria)<DAVERAGE(A1:E100,"Score",Criteria)-2*DSTDEV(A1:E100,"Score",Criteria),
   "Underperformer detected: " & DMIN(A1:E100,"Score",Criteria), "Within acceptable range")
// Identifies underperformers using 2-sigma rule (minimum below 2 standard deviations from mean)

// Control chart lower limit analysis
="Lower Control Limit: " & DAVERAGE(Process,"Measure",Criteria) - 3*DSTDEV(Process,"Measure",Criteria) & 
" | Current Min: " & DMIN(Process,"Measure",Criteria) & 
" | Status: " & IF(DMIN(Process,"Measure",Criteria)>DAVERAGE(Process,"Measure",Criteria)-3*DSTDEV(Process,"Measure",Criteria),"In Control","Out of Control")
// Compares current minimum against statistically-derived lower control limit

// Process capability floor analysis
="Min Observed: " & DMIN(Production,"Measurement",Criteria) & " | Lower Spec: " & LowerSpecLimit & 
" | Safety Margin: " & (DMIN(Production,"Measurement",Criteria)-LowerSpecLimit) & 
" | Sigma Level: " & (DAVERAGE(Production,"Measurement",Criteria)-LowerSpecLimit)/DSTDEV(Production,"Measurement",Criteria)
// Evaluates how close minimum values come to lower specification limits
```

## Conditional Logic Functions

### [[IF]]
Essential for conditional minimum finding and threshold-based alerts. IF enables DMIN to work with dynamic criteria and provide contextual results based on minimum values.

```spreadsheets
// Critical threshold monitoring with alerts
=IF(DMIN(A1:E100,"StockLevel",G1:G2)<ReorderPoint, "REORDER ALERT: " & DMIN(A1:E100,"StockLevel",G1:G2) & " units remaining", "Stock levels adequate")
// Generates reorder alerts when minimum stock levels fall below critical thresholds

// Performance intervention targeting
=IF(DMIN(Performance,"Rating",TeamCriteria)<6, "Team intervention needed - lowest: " & DMIN(Performance,"Rating",TeamCriteria), "Team performing adequately")
// Identifies teams requiring intervention based on their lowest performer's rating

// Budget constraint validation
=IF(DMIN(Budgets,"Remaining",DeptCriteria)<1000, "Budget crisis: $" & DMIN(Budgets,"Remaining",DeptCriteria) & " remaining", "Budget stable")
// Alerts when any department's remaining budget falls below critical minimum
```

### [[MIN]]
Alternative to DMIN for simpler single-range minimum finding. MIN works with single ranges while DMIN handles complex multi-field databases with multiple criteria.

```spreadsheets
// Compare DMIN vs MIN approaches
=DMIN(A1:C100,"Value",E1:E2) & " (DMIN with criteria) vs " & MIN(C1:C100) & " (MIN of entire range)"
// Shows difference between conditional database minimum and simple range minimum

// Method selection based on filtering needs
=IF(ISBLANK(CriteriaRange), MIN(ValueRange), DMIN(Database,"Value",CriteriaRange))
// Uses MIN for simple cases, DMIN when criteria-based filtering is required

// Cross-validation between DMIN and MIN
=IF(DMIN(Data,"Amount",AllRecords)=MIN(AmountRange), "Minimum functions validated", "Check data integrity")
// Validates DMIN accuracy against MIN when considering all records
```

## Commonly Used With Functions Examples

### Supply Chain Risk Management
```spreadsheets
// Critical stock level monitoring with supplier context
="Critical Stock Alert: " & DMIN(Inventory,"StockLevel",CriticalItems) & " units" & 
" | Supplier: " & INDEX(Suppliers,MATCH(DMIN(Inventory,"StockLevel",CriticalItems),StockLevels,0),SupplierColumn) & 
" | Lead Time: " & INDEX(Suppliers,MATCH(DMIN(Inventory,"StockLevel",CriticalItems),StockLevels,0),LeadTimeColumn) & " days" &
" | Reorder Status: " & IF(DMIN(Inventory,"StockLevel",CriticalItems)<SafetyStock,"URGENT","Monitor")
// Comprehensive low stock analysis with supplier information and urgency assessment

// Vendor performance floor analysis
="Worst Delivery: " & DMIN(Vendors,"DeliveryDays",ActiveVendors) & " days" & 
" | Best: " & DMAX(Vendors,"DeliveryDays",ActiveVendors) & " days" & 
" | Reliability Gap: " & (DMAX(Vendors,"DeliveryDays",ActiveVendors)-DMIN(Vendors,"DeliveryDays",ActiveVendors)) & " days" &
" | Standards Met: " & IF(DMIN(Vendors,"DeliveryDays",ActiveVendors)<=StandardDeliveryTime,"Yes","Review Needed")
// Vendor performance analysis showing delivery time range and standard compliance
```

### Quality Assurance Monitoring
```spreadsheets
// Quality floor with batch traceability
="Lowest Quality: " & DMIN(Production,"QualityScore",CurrentBatch) & "/100" & 
" | Batch: " & INDEX(Production,MATCH(DMIN(Production,"QualityScore",CurrentBatch),QualityRange,0),BatchColumn) & 
" | Operator: " & INDEX(Production,MATCH(DMIN(Production,"QualityScore",CurrentBatch),QualityRange,0),OperatorColumn) &
" | Action Required: " & IF(DMIN(Production,"QualityScore",CurrentBatch)<QualityThreshold,"Immediate Review","Monitor")
// Quality control with batch tracking and operator identification for lowest quality

// Process control with statistical limits
="Process Min: " & DMIN(ProcessData,"Measurement",ControlPeriod) & 
" | Lower Limit: " & (ProcessMean-3*ProcessStdDev) & 
" | Status: " & IF(DMIN(ProcessData,"Measurement",ControlPeriod)>ProcessMean-3*ProcessStdDev,"In Control","Out of Control") &
" | Improvement Needed: " & MAX(0,(ProcessMean-3*ProcessStdDev)-DMIN(ProcessData,"Measurement",ControlPeriod))
// Statistical process control with control limits and improvement quantification
```

### Customer Service Excellence
```spreadsheets
// Response time floor with team accountability
="Fastest Response: " & DMIN(Support,"ResponseHours",ThisMonth) & "h" & 
" | Team: " & INDEX(Teams,MATCH(DMIN(Support,"ResponseHours",ThisMonth),ResponseTimes,0),TeamColumn) & 
" | Agent: " & INDEX(Teams,MATCH(DMIN(Support,"ResponseHours",ThisMonth),ResponseTimes,0),AgentColumn) &
" | vs SLA: " & DMIN(Support,"ResponseHours",ThisMonth)/SLATarget*100 & "% of target" &
" | Recognition: " & IF(DMIN(Support,"ResponseHours",ThisMonth)<SLATarget*0.5,"Outstanding","Good")
// Response time analysis with team identification and SLA comparison

// Customer satisfaction floor analysis
="Lowest Satisfaction: " & DMIN(Surveys,"Rating",RecentSurveys) & "/10" & 
" | Department: " & INDEX(Departments,MATCH(DMIN(Surveys,"Rating",RecentSurveys),Ratings,0),DeptColumn) & 
" | Improvement Opportunity: " & (TargetRating-DMIN(Surveys,"Rating",RecentSurveys)) & " points" &
" | Priority: " & IF(DMIN(Surveys,"Rating",RecentSurveys)<6,"High","Medium")
// Customer satisfaction with department accountability and improvement planning
```

### Financial Performance Monitoring
```spreadsheets
// Profit margin floor with product analysis
="Lowest Margin: " & DMIN(Products,"ProfitMargin",ActiveProducts)*100 & "%" & 
" | Product: " & INDEX(Products,MATCH(DMIN(Products,"ProfitMargin",ActiveProducts),Margins,0),ProductColumn) & 
" | Revenue Impact: $" & INDEX(Products,MATCH(DMIN(Products,"ProfitMargin",ActiveProducts),Margins,0),RevenueColumn) &
" | Action: " & IF(DMIN(Products,"ProfitMargin",ActiveProducts)<MinAcceptableMargin,"Price Review","Monitor")
// Product profitability analysis with revenue context and pricing recommendations

// Cash flow minimum tracking
="Minimum Cash: $" & DMIN(CashFlow,"Balance",ForecastPeriod) & 
" | Month: " & INDEX(Months,MATCH(DMIN(CashFlow,"Balance",ForecastPeriod),Balances,0),1) & 
" | vs Minimum Required: $" & MinimumCash & 
" | Status: " & IF(DMIN(CashFlow,"Balance",ForecastPeriod)>MinimumCash,"Safe","Credit Line Needed")
// Cash flow forecasting with minimum balance tracking and financing needs assessment
```

### Employee Development Focus
```spreadsheets
// Performance improvement targeting
="Development Priority: " & INDEX(Employees,MATCH(DMIN(Performance,"OverallRating",Department),Ratings,0),NameColumn) & 
" (Rating: " & DMIN(Performance,"OverallRating",Department) & "/10)" & 
" | Improvement Plan: " & (TargetRating-DMIN(Performance,"OverallRating",Department)) & " points needed" &
" | Timeline: " & IF(DMIN(Performance,"OverallRating",Department)<6,"60 days","90 days") &
" | Manager: " & INDEX(Employees,MATCH(DMIN(Performance,"OverallRating",Department),Ratings,0),ManagerColumn)
// Employee development with personalized improvement planning and manager assignment
```

## Commonly Used With Functions Examples

### Portfolio Risk Assessment
```spreadsheets
// Investment risk floor with diversification analysis
="Highest Risk Position: " & DMAX(Portfolio,"RiskScore",Holdings)*100 & "%" & 
" | Lowest Risk: " & DMIN(Portfolio,"RiskScore",Holdings)*100 & "%" & 
" | Risk Spread: " & (DMAX(Portfolio,"RiskScore",Holdings)-DMIN(Portfolio,"RiskScore",Holdings))*100 & "%" &
" | Diversification: " & IF((DMAX(Portfolio,"RiskScore",Holdings)-DMIN(Portfolio,"RiskScore",Holdings))<0.5,"Well Diversified","Review Allocation")
// Portfolio risk analysis with diversification assessment using min/max risk spread
```
