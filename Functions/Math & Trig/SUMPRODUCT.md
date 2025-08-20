---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: math & trig
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# SUMPRODUCT

## SUMPRODUCT Description

Multiplies corresponding values in two or more arrays and returns the sum of those products. Essential for weighted calculations, conditional sums with multiple criteria, and complex analytical operations without array formulas.

> [!f(x)] SUMPRODUCT Syntax
>
> ```spreadsheets
> SUMPRODUCT(array1, [array2], [array3], ...)
> ```
>
> **Parameters:**
> - `array1` (required): First array or range of values
> - `array2, array3, ...` (optional): Additional arrays (up to 255 arrays)

> [!f(x)] SUMPRODUCT Examples
>
> ```spreadsheets
> // Basic weighted calculation
> SUMPRODUCT(A1:A5, B1:B5) → sum of A1*B1 + A2*B2 + ... + A5*B5
> 
> // Quantity × Price calculation
> SUMPRODUCT(C1:C10, D1:D10) → total value of inventory
> 
> // Conditional counting (count where both conditions true)
> SUMPRODUCT((E1:E100>50)*(F1:F100="Yes")) → count matching criteria
> 
> // Weighted average components
> SUMPRODUCT(G1:G20, H1:H20)/SUM(H1:H20) → weighted average
> 
> // Multiple criteria sum
> SUMPRODUCT((I1:I50="A")*(J1:J50>100)*K1:K50) → conditional sum
> ```

## Use Cases

### [[Weighted calculations]]
- **Portfolio analysis**: Calculate weighted returns, risk metrics, and asset allocation impacts for investment portfolios
- **Grade calculations**: Compute weighted averages for courses with different credit hours and importance levels
- **Performance metrics**: Aggregate weighted KPIs, customer satisfaction scores, and quality measurements
- **Financial modeling**: Determine weighted cost of capital, loan payments, and risk-adjusted returns

### [[Inventory and sales analysis]]  
- **Revenue calculations**: Multiply quantities by unit prices across product lines for total sales analysis
- **Inventory valuation**: Calculate total inventory value by combining quantities with unit costs
- **Margin analysis**: Determine profitability by multiplying sales volumes with profit margins per product
- **Forecasting**: Weight historical sales data by recency and seasonality factors for demand prediction

### [[Conditional analysis]]
- **Multi-criteria filtering**: Count or sum records meeting multiple simultaneous conditions without complex formulas
- **Segmentation analysis**: Analyze customer behavior, sales performance, and market segments with multiple filters
- **Quality control**: Calculate defect rates, compliance scores, and performance metrics with complex criteria
- **Resource planning**: Allocate resources based on multiple priority factors and availability constraints

## Related

### Similar Functions

- [[SUM]] - Adds values without multiplication, simpler aggregation for basic totals
- [[PRODUCT]] - Multiplies values without summing, useful for compound calculations
- [[SUMIF]] - Sums with single condition, less flexible than SUMPRODUCT for multiple criteria
- [[SUMIFS]] - Sums with multiple conditions, alternative to SUMPRODUCT for conditional aggregation
- [[AVERAGE]] - Calculates means, often combined with SUMPRODUCT for weighted averages

## Conditional Functions

### [[SUMIFS]]
Alternative to SUMPRODUCT for multiple criteria sums, with different syntax but similar functionality for conditional aggregation.

```spreadsheets
// Compare SUMPRODUCT vs SUMIFS for multiple criteria
=SUMPRODUCT((A1:A100="X")*(B1:B100>50)*C1:C100)
// SUMPRODUCT approach with logical arrays

=SUMIFS(C1:C100, A1:A100, "X", B1:B100, ">50")
// SUMIFS equivalent with explicit criteria syntax

// Complex criteria favor SUMPRODUCT
=SUMPRODUCT((D1:D50>AVERAGE(D1:D50))*(E1:E50<MEDIAN(E1:E50))*F1:F50)
// Dynamic criteria difficult with SUMIFS
```

### [[COUNTIFS]]
Complementary counting function, often used alongside SUMPRODUCT for comprehensive conditional analysis.

```spreadsheets
// Count and sum with same criteria
=COUNTIFS(A1:A100, ">10", B1:B100, "<50") & " items, " & 
 SUMPRODUCT((A1:A100>10)*(B1:B100<50)*C1:C100) & " total"
// Shows both count and sum for same conditions

// Percentage calculation
=SUMPRODUCT((D1:D200="Yes")*(E1:E200>100)*F1:F200)/SUMPRODUCT((D1:D200="Yes")*F1:F200)
// Calculates percentage of subset meeting additional criteria
```

## Mathematical Functions

### [[AVERAGE]]
Frequently combined with SUMPRODUCT to create weighted averages and complex mean calculations.

```spreadsheets
// Weighted average calculation
=SUMPRODUCT(A1:A10, B1:B10)/SUM(B1:B10)
// Values A1:A10 weighted by factors B1:B10

// Conditional weighted average
=SUMPRODUCT((C1:C50="Active")*D1:D50*E1:E50)/SUMPRODUCT((C1:C50="Active")*E1:E50)
// Weighted average for active items only

// Compare simple vs weighted average
=AVERAGE(F1:F20) & " (simple) vs " & SUMPRODUCT(F1:F20, G1:G20)/SUM(G1:G20) & " (weighted)"
// Shows difference between calculation methods
```

### [[SUM]]
Often used with SUMPRODUCT denominators for percentage and ratio calculations in analytical applications.

```spreadsheets
// Market share calculation
=SUMPRODUCT(H1:H20, I1:I20)/SUM(SUMPRODUCT(H1:H100, I1:I100))
// Calculates segment share of total weighted value

// Contribution analysis
=SUMPRODUCT((J1:J30="Product A")*K1:K30*L1:L30)/SUM(K1:K30*L1:L30)*100 & "%"
// Shows Product A contribution to total revenue

// Efficiency ratio
=SUMPRODUCT(M1:M25, N1:N25)/SUM(M1:M25) & " weighted efficiency"
// Calculates resource-weighted efficiency metric
```

## Commonly Used With Functions Examples

### SUMPRODUCT with Financial Analysis
```spreadsheets
// Portfolio weighted return
=SUMPRODUCT(A1:A10, B1:B10)/SUM(B1:B10)*100 & "% weighted return"
// Returns A1:A10 weighted by allocations B1:B10

// Risk-adjusted performance
=SUMPRODUCT(C1:C20, D1:D20, E1:E20)/SUMPRODUCT(D1:D20, E1:E20)
// Returns weighted by allocation and risk factors
```

### SUMPRODUCT with Inventory Management
```spreadsheets
// Total inventory value by category
=SUMPRODUCT((F1:F100="Electronics")*G1:G100*H1:H100)
// Electronics inventory quantity × unit cost

// Weighted average cost
=SUMPRODUCT(I1:I50, J1:J50, K1:K50)/SUMPRODUCT(I1:I50, J1:J50)
// Cost weighted by quantity and priority factors
```

### SUMPRODUCT with Performance Analysis
```spreadsheets
// Weighted KPI score
=SUMPRODUCT(L1:L8, M1:M8)/SUM(M1:M8)*100 & "% overall score"
// KPIs L1:L8 weighted by importance M1:M8

// Conditional performance metric
=SUMPRODUCT((N1:N30>O1:O30)*(P1:P30="Target")*Q1:Q30)/SUMPRODUCT((P1:P30="Target")*Q1:Q30)
// Performance for targets exceeding benchmarks
```
