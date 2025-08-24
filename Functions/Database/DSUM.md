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
# DSUM

## DSUM Description

Sums values in a database that match specified criteria by evaluating a database table against multiple conditions. DSUM works with structured data where the first row contains field headers and subsequent rows contain data records.

> [!f(x)] DSUM Syntax
>
> ```spreadsheets
> DSUM(database, field, criteria)
> ```
>
> **Parameters:**
> - `database` (required): The range of cells that makes up the database or list including headers
> - `field` (required): Column to sum - can be column label (in quotes) or column number  
> - `criteria` (required): Range containing conditions that specify which records to sum

> [!f(x)] DSUM Examples
>
> ```spreadsheets
> // Sum sales where region is "West"
> DSUM(A1:E20, "Sales", G1:G2) → 45000
> 
> // Sum quantities where price > 50 and category = "Electronics"  
> DSUM(A1:F100, 3, H1:I3) → 850
> 
> // Sum revenue for multiple product categories
> DSUM(Database, "Revenue", CriteriaRange) → 125000
> 
> // Sum hours worked by department "Marketing"
> DSUM(A1:D50, "Hours", F1:F2) → 320
> 
> // Sum inventory values where stock level < 10
> DSUM(Inventory, "Value", StockCriteria) → 12500
> ```

## Use Cases

### [[Sales analysis]]
- **Regional sales totals**: Sum revenue by geographic regions to identify top-performing markets and allocate resources effectively
- **Product category performance**: Calculate total sales for specific product lines to inform inventory and marketing decisions
- **Customer segment analysis**: Sum purchases by customer type (B2B vs B2C) to understand revenue composition and targeting strategies
- **Time period comparisons**: Total sales for specific quarters or months to analyze seasonal trends and year-over-year growth
- **Sales rep performance**: Sum individual salesperson revenues to calculate commissions and identify top performers

### [[Financial reporting]]
- **Expense categorization**: Sum expenses by department or category to create detailed budget reports and identify cost centers
- **Revenue recognition**: Total income streams by source type to understand business diversification and dependency risks
- **Cost analysis**: Sum variable costs by product line to calculate true profitability and inform pricing decisions
- **Budget variance**: Compare actual vs planned expenses by summing costs within specific date ranges and categories
- **Tax calculations**: Sum deductible expenses and taxable income by category to prepare accurate tax returns

### [[Inventory management]]
- **Stock valuation**: Sum inventory values by warehouse location to understand asset distribution and insurance needs
- **Reorder analysis**: Total quantities for items below reorder points to generate comprehensive purchase orders
- **Product performance**: Sum sales quantities by product category to identify fast-moving vs slow-moving inventory
- **Supplier analysis**: Sum purchase amounts by vendor to negotiate better terms and evaluate supplier relationships
- **Seasonal planning**: Sum historical sales by season to forecast inventory needs and prevent stockouts

## Related

### Similar Functions

- [[DAVERAGE]] - Calculates average instead of sum for database records matching criteria
- [[DCOUNT]] - Counts records matching criteria instead of summing values  
- [[DMAX]] - Finds maximum value in database records matching criteria
- [[DMIN]] - Finds minimum value in database records matching criteria
- [[DGET]] - Retrieves single value from database record matching criteria

## Database Query Functions

### [[DCOUNT]]
Used with DSUM to validate record counts before summing values. DCOUNT ensures data integrity by confirming the number of records being summed and helps identify data quality issues.

```spreadsheets
// Validate sum with record count
=DSUM(A1:E100,"Sales",G1:G2) & " from " & DCOUNT(A1:E100,"Sales",G1:G2) & " records"
// Returns: "45000 from 23 records"

// Conditional summing with count validation
=IF(DCOUNT(Database,"Amount",Criteria)>0, DSUM(Database,"Amount",Criteria), "No matching records")
// Only calculates sum if matching records exist

// Average calculation using DSUM and DCOUNT
=DSUM(A1:D50,"Revenue",F1:F3)/DCOUNT(A1:D50,"Revenue",F1:F3)
// Manually calculates average when DAVERAGE isn't available
```

### [[DAVERAGE]]  
Frequently paired with DSUM to show both total values and per-record averages. Together they provide complete statistical summary of database subsets matching specific criteria.

```spreadsheets
// Sales performance summary
="Total: " & DSUM(A1:F100,"Sales",H1:H2) & ", Average: " & DAVERAGE(A1:F100,"Sales",H1:H2)
// Example: "Total: 125000, Average: 5434"

// Department analysis combining sum and average
=DSUM(Employees,"Salary",DeptCriteria) & " total payroll, " & DAVERAGE(Employees,"Salary",DeptCriteria) & " average salary"
// Provides both aggregate and normalized compensation views

// Budget variance with totals and averages
="Variance Sum: " & DSUM(Budget,"Variance",Criteria) & ", Avg Variance: " & DAVERAGE(Budget,"Variance",Criteria)
// Shows both total budget deviation and per-item average variance
```

## Comparison Functions

### [[DMAX]]
Combined with DSUM to understand data distribution and identify highest contributors to totals. DMAX shows peak values while DSUM provides aggregate context for proportion analysis.

```spreadsheets
// Top performer analysis
="Highest Sale: " & DMAX(A1:E200,"Sales",G1:G2) & " of " & DSUM(A1:E200,"Sales",G1:G2) & " total"
// Shows individual contribution versus total performance

// Range analysis for quality control
=DMAX(Inventory,"Value",Criteria) & " max vs " & DSUM(Inventory,"Value",Criteria) & " total inventory"
// Identifies highest-value items within total inventory context

// Performance distribution analysis
="Top: " & DMAX(Sales,"Amount",RegionCriteria) & ", Total: " & DSUM(Sales,"Amount",RegionCriteria)
// Shows concentration of sales performance
```

### [[DMIN]]
Works with DSUM to show complete value range and identify lowest contributors. DMIN reveals underperformers while DSUM provides context for their impact on totals.

```spreadsheets
// Complete range with totals
="Range: " & DMIN(A1:F50,"Revenue",H1:H3) & " to " & DMAX(A1:F50,"Revenue",H1:H3) & ", Total: " & DSUM(A1:F50,"Revenue",H1:H3)
// Provides full statistical summary including aggregates

// Low performer impact analysis
="Lowest: " & DMIN(Performance,"Score",Criteria) & ", affecting total of " & DSUM(Performance,"Score",Criteria)
// Shows underperformer impact on aggregate performance

// Quality control with minimum thresholds
=IF(DMIN(Products,"Quality",Criteria)<DSUM(Products,"Quality",Criteria)/DCOUNT(Products,"Quality",Criteria)*0.8, "Quality alert", "Acceptable")
// Alerts when minimum quality falls below 80% of average
```

## Conditional Logic Functions

### [[IF]]
Essential for conditional database operations and error handling. IF enables DSUM to work with dynamic criteria, handle empty result sets gracefully, and provide contextual results.

```spreadsheets
// Conditional sum with validation
=IF(DCOUNT(A1:E100,"Sales",G1:G2)>0, DSUM(A1:E100,"Sales",G1:G2), "No sales found")
// Only calculates sum when matching records exist

// Tiered analysis based on sum results
=IF(DSUM(Revenue,"Amount",Criteria)>=100000, "High Performer", IF(DSUM(Revenue,"Amount",Criteria)>=50000, "Average", "Needs Attention"))
// Categorizes performance based on sum results

// Error-resistant database summing
=IF(ISERROR(DSUM(Database,"Values",CriteriaRange)), "Invalid criteria or data", DSUM(Database,"Values",CriteriaRange))
// Prevents error display when DSUM encounters invalid data
```

### [[SUMIF]]
Alternative to DSUM for simpler single-criterion summing. SUMIF works with single columns while DSUM handles complex multi-field databases with multiple criteria.

```spreadsheets
// Compare DSUM vs SUMIF approaches
=DSUM(A1:C100,"Sales",E1:E2) & " (DSUM) vs " & SUMIF(B1:B100,"West",C1:C100) & " (SUMIF)"
// Shows difference between database and range-based summing

// When to use DSUM over SUMIF
=IF(ROWS(CriteriaRange)>2, DSUM(Database,"Amount",CriteriaRange), SUMIF(Database,"Amount",SimpleCriteria))
// Uses DSUM for complex criteria, SUMIF for simple ones

// Validation between DSUM and SUMIF results  
=IF(ABS(DSUM(Data,"Value",SingleCriteria)-SUMIF(Data,"Value",Condition))<0.01, "Verified", "Discrepancy")
// Confirms DSUM accuracy against SUMIF for single criteria
```

## Commonly Used With Functions Examples

### Sales Commission Calculation
```spreadsheets
// Calculate total commissions by sales rep with performance tiers
=IF(DSUM(Sales,"Amount",RepCriteria)>=100000, 
   DSUM(Sales,"Amount",RepCriteria)*0.08, 
   DSUM(Sales,"Amount",RepCriteria)*0.05)
// Higher commission rate for sales exceeding $100,000

// Regional bonus calculation combining multiple criteria
=DSUM(Sales,"Amount",RegionCriteria)*IF(DCOUNT(Sales,"CustomerID",RegionCriteria)>50, 0.02, 0.01)
// Bonus rate increases with customer count in region
```

### Inventory Valuation Report
```spreadsheets
// Complete inventory analysis with stock alerts
="Total Value: $" & DSUM(Inventory,"Value",AllItems) & 
" | Low Stock Value: $" & DSUM(Inventory,"Value",LowStockCriteria) &
" | Avg Item Value: $" & DAVERAGE(Inventory,"Value",AllItems)
// Comprehensive inventory financial summary

// Reorder analysis with cost projections
=DSUM(Inventory,"ReorderCost",BelowMinCriteria) & 
" needed to restock " & DCOUNT(Inventory,"SKU",BelowMinCriteria) & " items"
// Total cost to bring all items to minimum stock levels
```

### Budget Variance Analysis
```spreadsheets
// Department budget performance with variance calculations
="Actual: $" & DSUM(Expenses,"Actual",DeptCriteria) & 
" vs Budget: $" & DSUM(Expenses,"Budget",DeptCriteria) & 
" | Variance: " & (DSUM(Expenses,"Budget",DeptCriteria)-DSUM(Expenses,"Actual",DeptCriteria))
// Shows spending versus budget with dollar variance

// Multi-period trend analysis
=DSUM(Budget,"Q1",Criteria) & "/" & DSUM(Budget,"Q2",Criteria) & 
"/" & DSUM(Budget,"Q3",Criteria) & "/" & DSUM(Budget,"Q4",Criteria)
// Quarterly totals for trend analysis
```

### Customer Analysis Dashboard
```spreadsheets
// Customer segmentation with revenue analysis
="VIP Customers: $" & DSUM(Customers,"Revenue",VIPCriteria) & 
" (" & ROUND(DSUM(Customers,"Revenue",VIPCriteria)/DSUM(Customers,"Revenue",AllCriteria)*100,1) & "%)"
// VIP customer revenue with percentage of total

// Geographic performance comparison
="West: " & DSUM(Sales,"Amount",WestCriteria) & 
" | East: " & DSUM(Sales,"Amount",EastCriteria) & 
" | Winner: " & IF(DSUM(Sales,"Amount",WestCriteria)>DSUM(Sales,"Amount",EastCriteria),"West","East")
// Regional comparison with winner identification
```

### Quality Control Reporting
```spreadsheets
// Production quality metrics with cost impact
="Defect Cost: $" & DSUM(Production,"DefectCost",DefectCriteria) & 
" from " & DCOUNT(Production,"BatchID",DefectCriteria) & " batches" &
" | Rate: " & ROUND(DCOUNT(Production,"BatchID",DefectCriteria)/DCOUNT(Production,"BatchID",AllBatches)*100,2) & "%"
// Comprehensive quality cost analysis with defect rates
```
