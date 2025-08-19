---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: financial
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# FV

## FV Description

Calculates the future value of an investment or savings plan based on constant periodic payments and a fixed interest rate. FV projects what current investments or regular payments will be worth at a future date, essential for retirement planning, savings goals, and investment growth analysis.

> [!f(x)] FV Syntax
>
> ```spreadsheets
> FV(rate, nper, pmt, [pv], [type])
> ```
>
> **Parameters:**
> - `rate` (required): Interest rate per period as decimal (e.g., annual rate/12 for monthly)
> - `nper` (required): Total number of payment periods
> - `pmt` (required): Payment amount per period (negative for payments made, positive for payments received)
> - `pv` (optional): Present value or initial lump sum amount, defaults to 0
> - `type` (optional): 0 for payments at end of period (default), 1 for beginning

> [!f(x)] FV Examples
>
> ```spreadsheets
> // Retirement savings projection
> FV(0.08/12, 30*12, -500, 0, 0) → 679516.38
> // $500 monthly for 30 years at 8% annual grows to $679,516
> 
> // Investment growth with lump sum start
> FV(0.07, 20, -1000, -10000, 0) → 54436.81
> // $10k initial + $1k annual at 7% for 20 years
> 
> // Education savings goal
> FV(0.06/12, 18*12, -200, -5000, 0) → 88435.50
> // $5k initial + $200 monthly for 18 years at 6%
> 
> // Simple compound interest calculation
> FV(0.05, 10, 0, -25000, 0) → 40722.25
> // $25k invested at 5% for 10 years, no additional payments
> 
> // Annuity due calculation (payments at beginning)
> FV(0.09/12, 25*12, -800, 0, 1) → 797764.92
> // $800 monthly payments at start of each month for 25 years
> ```

## Use Cases

### [[Investment planning]]
- **Retirement savings projections**: Calculate future value of 401k contributions and investment growth to ensure adequate retirement funding
- **Goal-based investing**: Determine future value of regular investments to achieve specific financial targets like home down payments
- **Portfolio growth analysis**: Project long-term investment portfolio values considering regular contributions and market returns
- **Education funding**: Calculate future value of college savings plans considering tuition inflation and investment returns

### [[Savings planning]]  
- **Emergency fund accumulation**: Project future value of regular savings to build adequate emergency reserves
- **Vacation and travel planning**: Calculate savings needed for major trips and experiences considering investment growth
- **Major purchase planning**: Determine future value of savings for cars, homes, or other significant purchases
- **Holiday and gift savings**: Plan seasonal savings accounts with future value projections for holiday expenses

### [[Business forecasting]]
- **Cash flow projections**: Forecast future cash balances considering regular business income and expense patterns
- **Capital accumulation**: Plan for future equipment purchases or expansion by projecting business savings growth
- **Sinking fund calculations**: Determine future value of business reserves for debt repayment or major capital expenditures
- **Employee benefit planning**: Project future values of pension contributions and profit-sharing plans

## Related

### Similar Functions

- [[PV]] - Calculates present value, inverse direction of FV calculations
- [[NPV]] - Calculates net present value for irregular cash flows, extends FV concept
- [[PMT]] - Calculates payment amount when FV target is known
- [[RATE]] - Calculates interest rate when FV and other terms are known
- [[NPER]] - Calculates time periods when FV target and other terms are known

## Time Value Functions

### [[PV]]
PV and FV are inverse functions for time value calculations. PV discounts future values to present, while FV compounds present values to future. Essential for complete financial analysis.

```spreadsheets
// Investment validation using both PV and FV
="Present cost: " & PV(0.08, 20, -1000, FV(0.08, 20, -1000, 0, 0), 0) & " Future value: " & FV(0.08, 20, -1000, 0, 0)
// Verify calculations work in both directions

// Time value demonstration
="$50,000 today equals " & FV(0.06, 15, 0, -50000, 0) & " in 15 years at 6%"
// Shows compound growth from present to future

// Investment comparison analysis
=FV(0.07, 25, -2000, PV(0.07, 25, -2000, 0, 0), 0)
// Future value starting from present value calculation
```

### [[NPV]]  
NPV works with present values while FV projects to future values. Both essential for complete investment analysis considering different time perspectives.

```spreadsheets
// Investment horizon analysis
="NPV: " & NPV(0.09, A2:A15) & " FV equivalent: " & FV(0.09, 13, 0, -NPV(0.09, A2:A15), 0)
// Compare net present value to equivalent future value

// Multi-period investment planning
=FV(0.08, 10, 0, NPV(0.08, B2:B20), 0)
// Future value of net present value from irregular cash flows

// Goal-based investment validation
=IF(FV(0.10, 20, -1500, 0, 0)>500000, NPV(0.10, C2:C21), "Increase payments")
// Use NPV analysis if FV goal is met
```

### [[PMT]]
PMT and FV work together for savings goal planning. PMT calculates required payments when FV target is known, while FV projects results of given payments.

```spreadsheets
// Savings goal calculation
="Need " & ABS(PMT(0.07/12, 25*12, 0, FV(0.07/12, 25*12, -800, 0, 0), 0)) & " monthly for " & FV(0.07/12, 25*12, -800, 0, 0) & " goal"
// Required payment for calculated future value

// Retirement planning validation
=FV(0.08, 30, PMT(0.08, 30, 0, -1000000, 0), 0, 0)
// Should equal $1,000,000 if payment calculation correct

// Investment adequacy check
=IF(FV(0.06, 20, A1, 0, 0)>=B1, "Adequate payments", PMT(0.06, 20, 0, -B1, 0))
// Show current FV or required payment adjustment
```

## Goal Planning Functions

### [[RATE]]
RATE determines required return rates when FV targets and other terms are known. RATE and FV work together to solve for unknown variables in investment planning.

```spreadsheets
// Required return calculation
="Need " & RATE(20, -1500, 0, FV(0.08, 20, -1500, 0, 0), 0)*100 & "% return for target"
// Rate needed to achieve calculated future value

// Investment performance validation
=FV(RATE(15, -2000, 0, 500000, 0), 15, -2000, 0, 0)
// Should equal $500,000 if rate calculation correct

// Goal feasibility analysis
=IF(RATE(25, -1000, 0, FV(0.10, 25, -1000, 0, 0), 0)<=0.12, "Achievable", "Unrealistic target")
// Check if required rate is reasonable
```

### [[NPER]]  
NPER calculates time required when FV targets and other terms are known. NPER and FV together determine timelines for achieving financial goals.

```spreadsheets
// Time to goal calculation
="Need " & NPER(0.09, -1800, 0, FV(0.09, 30, -1800, 0, 0), 0) & " years for target"
// Time needed to achieve calculated future value

// Early retirement planning
=NPER(0.08, -3000, -50000, FV(0.08, 25, -3000, -50000, 0), 0)
// Should equal 25 years if future value calculated correctly

// Goal timeline optimization
=FV(0.07, NPER(0.07, -2500, 0, 750000, 0), -2500, 0, 0)
// Future value achieved in calculated time period
```

### [[IF]]
Essential for FV scenario analysis and goal validation. IF enables conditional future value calculations and investment decision logic.

```spreadsheets
// Goal achievement validation
=IF(FV(0.08, 25, -1200, -10000, 0)>=300000, "Goal achieved", "Increase savings")
// Check if future value meets target

// Risk-adjusted planning
=IF(FV(0.06, 20, A1, B1, 0)<FV(0.10, 20, A1, B1, 0)*0.8, "Conservative approach", "Aggressive strategy")
// Compare conservative versus optimistic returns

// Retirement readiness assessment
=IF(FV(0.07, C1, D1, E1, 0)>=F1*25, "Ready to retire", "Need " & F1*25-FV(0.07, C1, D1, E1, 0) & " more")
// Use 25x annual expenses rule for retirement
```

## Commonly Used With Functions Examples

### Investment Growth Analysis
```spreadsheets
// Complete investment projection with validation
="Initial: $" & ABS(A1) & " + $" & ABS(B1) & " monthly = $" & ROUND(FV(0.08/12, C1*12, B1, A1, 0), 0) & " in " & C1 & " years"
// Shows initial amount, monthly contribution, and future value result

// Risk scenario comparison
="Conservative (5%): $" & FV(0.05, 20, -1000, 0, 0) & " vs Aggressive (10%): $" & FV(0.10, 20, -1000, 0, 0)
// Compare future values at different return rates
```

### Retirement Planning Comprehensive
```spreadsheets
// Retirement adequacy calculation
=IF(FV(0.07, 65-A1, -B1*12, C1, 0)>=D1*25, "On track", "Short by $" & ROUND(D1*25-FV(0.07, 65-A1, -B1*12, C1, 0), 0))
// Where A1=current age, B1=monthly savings, C1=current balance, D1=annual expenses

// Multiple savings vehicle projection
="401k: $" & FV(0.08, 25, -A1, B1, 0) & " + IRA: $" & FV(0.07, 25, -C1, D1, 0) & " = Total: $" & FV(0.08, 25, -A1, B1, 0)+FV(0.07, 25, -C1, D1, 0)
// Combine multiple retirement account projections
```

### Education Funding Strategy
```spreadsheets
// College savings projection with inflation
="Current tuition: $" & A1 & " inflated to: $" & FV(0.04, B1, 0, -A1, 0) & " needs savings of: $" & ABS(PMT(0.06/12, B1*12, 0, FV(0.04, B1, 0, -A1, 0), 0))
// Account for tuition inflation in savings planning

// Multiple child education planning
="Child 1 ($" & FV(0.06, 10, -C1, 0, 0) & ") + Child 2 ($" & FV(0.06, 15, -C2, 0, 0) & ") = Total needed: $" & FV(0.06, 10, -C1, 0, 0)+FV(0.06, 15, -C2, 0, 0)
// Plan for multiple children's education costs
```
