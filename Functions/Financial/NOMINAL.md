---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - financial
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
# NOMINAL

## NOMINAL Description

Calculates the nominal annual interest rate given the effective interest rate and the number of compounding periods per year. NOMINAL converts effective rates back to nominal rates, essential for comparing loan offers, investment products, and understanding how compounding frequency affects advertised interest rates.

> [!f(x)] NOMINAL Syntax
>
> ```spreadsheets
> NOMINAL(effect_rate, npery)
> ```
>
> **Parameters:**
> - `effect_rate` (required): Effective annual interest rate as decimal (e.g., 0.08 for 8%)
> - `npery` (required): Number of compounding periods per year (1=annually, 2=semi-annually, 4=quarterly, 12=monthly, 365=daily)

> [!f(x)] NOMINAL Examples
>
> ```spreadsheets
> // Convert 8.24% effective rate to nominal with monthly compounding
> NOMINAL(0.0824, 12) → 0.0795
> // 8.24% effective equals 7.95% nominal with monthly compounding
> 
> // Credit card APR analysis
> NOMINAL(0.2297, 12) → 0.2075
> // 22.97% effective rate equals 20.75% nominal APR
> 
> // Investment product comparison
> NOMINAL(0.0516, 4) → 0.0508
> // 5.16% effective return equals 5.08% nominal with quarterly compounding
> 
> // Savings account rate conversion
> NOMINAL(0.0253, 365) → 0.0250
> // 2.53% effective rate equals 2.50% nominal with daily compounding
> 
> // Mortgage rate back-calculation
> NOMINAL(0.0619, 2) → 0.0609
> // 6.19% effective rate equals 6.09% nominal with semi-annual compounding
> ```

## Use Cases

### [[Interest rate analysis]]
- **Loan comparison studies**: Convert effective rates back to nominal rates to understand original loan terms and APR calculations
- **Credit product evaluation**: Analyze credit card and personal loan rates to understand true borrowing costs versus advertised rates
- **Mortgage rate validation**: Verify mortgage APR calculations by converting effective rates back to nominal terms
- **Financial product transparency**: Understand relationship between advertised rates and actual compounding effects

### [[Investment planning]]
- **CD and savings analysis**: Compare certificate of deposit and savings account rates by converting effective yields to nominal rates
- **Bond investment evaluation**: Analyze bond yields by understanding nominal versus effective rate relationships across different compounding periods
- **Retirement account planning**: Evaluate retirement account options by converting effective returns to nominal rates for comparison
- **Investment performance reporting**: Present investment returns in both nominal and effective terms for comprehensive analysis

### [[Business financial modeling]]
- **Cost of capital calculations**: Convert effective borrowing costs back to nominal rates for financial reporting and analysis
- **Budget and forecast modeling**: Use nominal rates in financial models while understanding effective rate implications
- **Vendor financing analysis**: Evaluate supplier financing options by converting effective rates to nominal terms
- **Capital structure optimization**: Analyze debt instruments by understanding nominal versus effective rate trade-offs

## Related

### Similar Functions

- [[EFFECT]] - Calculates effective rate from nominal rate, inverse of NOMINAL function
- [[RATE]] - Calculates interest rate per period for loan and investment calculations
- [[IRR]] - Calculates internal rate of return for irregular cash flows
- [[YIELD]] - Calculates yield to maturity for bonds and securities
- [[XIRR]] - Calculates internal rate of return for irregular time periods

## Interest Rate Conversion Functions

### [[EFFECT]]
EFFECT and NOMINAL are complementary functions for interest rate conversion. EFFECT converts nominal to effective rates, while NOMINAL converts effective back to nominal rates.

```spreadsheets
// Rate conversion validation
="Nominal: " & NOMINAL(0.0824, 12)*100 & "% converts to Effective: " & EFFECT(NOMINAL(0.0824, 12), 12)*100 & "%"
// Should return original effective rate of 8.24%

// Loan rate analysis
="APR: " & NOMINAL(EFFECT(0.195, 12), 12)*100 & "% with effective rate: " & EFFECT(0.195, 12)*100 & "%"
// Compare nominal APR with effective rate

// Investment rate comparison
=IF(EFFECT(NOMINAL(0.063, 4), 4)>0.063, "Higher effective rate", "Matches original")
// Validate rate conversion accuracy
```

### [[RATE]]
RATE calculates periodic interest rates while NOMINAL works with annual rates. Both essential for comprehensive interest rate analysis.

```spreadsheets
// Monthly payment rate conversion
="Monthly rate: " & RATE(60, -350, 18000, 0, 0)*12*100 & "% nominal vs " & NOMINAL(EFFECT(RATE(60, -350, 18000, 0, 0)*12, 12), 12)*100 & "% calculated"
// Compare calculated rate with NOMINAL conversion

// Loan rate validation
=NOMINAL((1+RATE(36, -285, 9500, 0, 0))^12-1, 12)
// Convert periodic rate to nominal annual rate

// Investment return analysis
=IF(NOMINAL(EFFECT(RATE(20, -1000, 0, 25000, 0), 1), 12)>0.10, "High return", "Moderate return")
// Use RATE with NOMINAL for annual rate comparison
```

### [[IRR]]
IRR provides effective returns while NOMINAL can convert these to nominal equivalents for standardized comparison across investments.

```spreadsheets
// Investment return standardization
="IRR: " & IRR(A2:A15)*100 & "% effective vs " & NOMINAL(IRR(A2:A15), 12)*100 & "% nominal equivalent"
// Compare IRR effective return with nominal equivalent

// Multi-investment comparison
=NOMINAL(IRR(B2:B20), 4) - NOMINAL(IRR(C2:C20), 4)
// Compare investments using nominal rate equivalents

// Performance reporting
=IF(NOMINAL(IRR(D2:D25), 12)>0.08, IRR(D2:D25), "Below threshold")
// Use nominal threshold for IRR evaluation
```

## Loan Analysis Functions

### [[PMT]]
PMT uses periodic rates while NOMINAL helps convert between nominal and effective annual rates for loan payment calculations.

```spreadsheets
// Loan payment with rate conversion
="Payment using nominal: $" & ABS(PMT(NOMINAL(0.0824, 12)/12, 60, 25000, 0, 0)) & " vs effective: $" & ABS(PMT(0.0824/12, 60, 25000, 0, 0))
// Compare payments using different rate calculations

// Credit comparison analysis
=PMT(NOMINAL(EFFECT(A1, 12), 12)/12, B1, C1, 0, 0)
// Use NOMINAL for standardized rate comparison

// APR verification
=ABS(PMT(NOMINAL(0.2297, 12)/12, 24, 5000, 0, 0))
// Calculate payment using nominal rate derived from effective APR
```

### [[PV]]
PV and NOMINAL work together for present value calculations using converted interest rates for accurate financial analysis.

```spreadsheets
// Present value with rate conversion
="PV at nominal rate: $" & PV(NOMINAL(0.0619, 4)/4, 20, -1200, 0, 0) & " vs effective: $" & PV(0.0619/4, 20, -1200, 0, 0)
// Compare present values using different rate methods

// Investment valuation
=PV(NOMINAL(IRR(A2:A10), 12)/12, 60, B1, 0, 0)
// Use NOMINAL to convert IRR for PV calculation

// Loan comparison
=IF(PV(NOMINAL(0.078, 12)/12, 60, -A1, 0, 0)>PV(NOMINAL(0.0824, 12)/12, 60, -A1, 0, 0), "Lower rate better", "Higher rate acceptable")
// Compare loan present values using nominal rates
```

### [[FV]]
FV and NOMINAL enable future value calculations using standardized nominal rates for consistent investment projections.

```spreadsheets
// Investment projection with nominal rates
="Future value at " & NOMINAL(0.0824, 12)*100 & "%: $" & FV(NOMINAL(0.0824, 12)/12, 60, -500, 0, 0)
// Project investment using nominal rate equivalent

// Savings goal analysis
=FV(NOMINAL(EFFECT(0.0525, 365), 12)/12, 120, -A1, B1, 0)
// Convert daily compounding to monthly nominal for calculation

// Rate sensitivity analysis
=FV(NOMINAL(0.063, 4)/4, 80, -750, 0, 0) - FV(NOMINAL(0.0516, 4)/4, 80, -750, 0, 0)
// Compare future values using different nominal rates
```

## Investment Comparison Functions

### [[NPV]]
NPV uses effective discount rates while NOMINAL helps standardize rates for consistent net present value comparisons across investments.

```spreadsheets
// NPV with standardized rates
="NPV using nominal equivalent: $" & NPV(NOMINAL(0.0824, 12), A2:A25) & " vs effective: $" & NPV(0.0824, A2:A25)
// Compare NPV calculations using different rate methods

// Multi-project evaluation
=NPV(NOMINAL(EFFECT(0.09, 4), 1), B2:B15) - NPV(NOMINAL(EFFECT(0.09, 4), 1), C2:C15)
// Use NOMINAL for consistent project comparison

// Investment hurdle rate analysis
=IF(NPV(NOMINAL(0.12, 12), D2:D20)>0, "Accept project", "Reject project")
// Use nominal equivalent of hurdle rate for NPV
```

### [[YIELD]]
YIELD provides effective yields while NOMINAL converts these to nominal equivalents for bond and security comparison.

```spreadsheets
// Bond yield comparison
="Bond yield: " & YIELD(DATE(2024,1,1), DATE(2029,1,1), 0.05, 98.5, 100, 2, 1)*100 & "% effective vs " & NOMINAL(YIELD(DATE(2024,1,1), DATE(2029,1,1), 0.05, 98.5, 100, 2, 1), 2)*100 & "% nominal"
// Compare effective yield with nominal equivalent

// Investment grade analysis
=IF(NOMINAL(YIELD(A1, B1, C1, D1, 100, 2, 1), 2)>0.06, "High yield", "Investment grade")
// Use nominal yield for classification

// Portfolio yield analysis
=AVERAGE(NOMINAL(YIELD(A2, B2, C2, D2, 100, 2, 1), 2), NOMINAL(YIELD(A3, B3, C3, D3, 100, 2, 1), 2))
// Average nominal yields for portfolio analysis
```

## Commonly Used With Functions Examples

### Comprehensive Rate Analysis
```spreadsheets
// Complete interest rate comparison
="Product A: " & NOMINAL(0.0824, 12)*100 & "% nominal (" & EFFECT(NOMINAL(0.0824, 12), 12)*100 & "% effective) vs Product B: " & NOMINAL(0.0795, 4)*100 & "% nominal (" & EFFECT(NOMINAL(0.0795, 4), 4)*100 & "% effective)"
// Compare multiple financial products with both nominal and effective rates

// APR to payment calculation
="APR: " & NOMINAL(0.2297, 12)*100 & "% results in payment: $" & ABS(PMT(NOMINAL(0.2297, 12)/12, 60, 15000, 0, 0))
// Convert effective APR to nominal then calculate payment
```

### Investment Portfolio Analysis
```spreadsheets
// Multi-account retirement projection
="401k (monthly): $" & FV(NOMINAL(0.0824, 12)/12, 25*12, -A1, B1, 0) & " + IRA (quarterly): $" & FV(NOMINAL(0.078, 4)/4, 25*4, -C1, D1, 0) & " = Total: $" & FV(NOMINAL(0.0824, 12)/12, 25*12, -A1, B1, 0)+FV(NOMINAL(0.078, 4)/4, 25*4, -C1, D1, 0)
// Project retirement savings using nominal rates for different compounding

// Risk-adjusted return comparison
="Conservative: " & NOMINAL(0.0516, 365)*100 & "% vs Aggressive: " & NOMINAL(0.0824, 12)*100 & "% with difference: " & (NOMINAL(0.0824, 12)-NOMINAL(0.0516, 365))*100 & " percentage points"
// Compare investment strategies using nominal rate equivalents
```

### Business Financial Analysis
```spreadsheets
// Cost of capital calculation
="Debt cost: " & NOMINAL(0.0619, 2)*100 & "% + Equity cost: " & NOMINAL(0.095, 1)*100 & "% = WACC: " & (NOMINAL(0.0619, 2)*0.4+NOMINAL(0.095, 1)*0.6)*100 & "%"
// Calculate weighted average cost of capital using nominal rates

// Loan vs lease analysis
=IF(NPV(NOMINAL(0.078, 12), A2:A61)<NPV(NOMINAL(0.078, 12), B2:B61), "Loan better at " & NOMINAL(0.078, 12)*100 & "%", "Lease preferred")
// Compare financing options using nominal discount rate
```
