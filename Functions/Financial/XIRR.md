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
# XIRR

## XIRR Description

Calculates the internal rate of return for a series of cash flows that occur at irregular time intervals. XIRR provides the annualized rate of return that makes the net present value of all cash flows equal to zero, essential for evaluating investments with non-periodic cash flows and real-world timing.

> [!f(x)] XIRR Syntax
>
> ```spreadsheets
> XIRR(values, dates, [guess])
> ```
>
> **Parameters:**
> - `values` (required): Array of cash flows (negative for investments, positive for returns)
> - `dates` (required): Array of dates corresponding to each cash flow
> - `guess` (optional): Initial guess for iteration, defaults to 10%

> [!f(x)] XIRR Examples
>
> ```spreadsheets
> // Real estate investment return
> XIRR({-100000; 15000; 18000; 22000; 125000}, {DATE(2020,1,15); DATE(2020,12,31); DATE(2021,12,31); DATE(2022,12,31); DATE(2023,6,15)}) → 0.174
> // Property investment yields 17.4% annual return
> 
> // Startup investment analysis  
> XIRR({-250000; -150000; 0; 75000; 1200000}, {DATE(2019,3,1); DATE(2020,1,15); DATE(2021,1,1); DATE(2022,7,1); DATE(2023,11,30)}) → 0.485
> // Startup investment yields 48.5% IRR over irregular periods
> 
> // Private equity fund returns
> XIRR({-500000; -200000; 125000; 180000; 220000; 650000}, {DATE(2018,6,1); DATE(2019,3,15); DATE(2020,9,30); DATE(2021,12,15); DATE(2022,8,31); DATE(2024,1,31)}) → 0.168
> // PE fund generates 16.8% annual return
> 
> // Project cash flow evaluation
> XIRR({-75000; 18000; 22000; 25000; 28000; 15000}, {DATE(2023,1,1); DATE(2023,4,30); DATE(2023,9,15); DATE(2024,2,28); DATE(2024,8,31); DATE(2024,12,31)}) → 0.247
> // Project IRR of 24.7% with irregular timing
> 
> // Bond investment with coupon reinvestment
> XIRR({-102500; 2750; 2750; 2750; 105500}, {DATE(2024,1,15); DATE(2024,7,15); DATE(2025,1,15); DATE(2025,7,15); DATE(2026,1,15)}) → 0.0421
> // Bond yields 4.21% with semi-annual coupons
> ```

## Use Cases

### [[Investment performance analysis]]
- **Portfolio return calculation**: Calculate actual returns for investments with irregular contributions and withdrawals
- **Private investment evaluation**: Analyze returns from private equity, venture capital, and real estate investments
- **Mutual fund performance**: Evaluate fund performance considering actual investment timing and amounts
- **Alternative investment analysis**: Calculate returns for hedge funds, commodities, and other irregular cash flow investments

### [[Business project evaluation]]
- **Capital project assessment**: Evaluate business projects with irregular cash flows and timing
- **Merger and acquisition analysis**: Calculate IRR for M&A transactions with complex payment structures
- **Research and development ROI**: Analyze R&D investments with uncertain timing and payoffs
- **Expansion project evaluation**: Calculate returns for business expansion with phased investments and returns

### [[Personal financial planning]]
- **Retirement account analysis**: Calculate returns on retirement accounts with irregular contributions
- **Education funding evaluation**: Analyze education savings plans with varying contribution schedules
- **Investment property returns**: Calculate real estate investment returns with irregular rental income and expenses
- **Business investment tracking**: Evaluate personal business investments with irregular cash flows

## Related

### Similar Functions

- [[IRR]] - Calculates internal rate of return for periodic cash flows
- [[NPV]] - Calculates net present value for regular period cash flows
- [[XNPV]] - Calculates net present value for irregular date cash flows
- [[RATE]] - Calculates interest rate for regular payment schedules
- [[YIELD]] - Calculates bond yield for regular coupon payments

## Commonly Used With Functions Examples

### Investment Performance Analysis
```spreadsheets
// Complete investment evaluation
="Investment: " & A1 & " | XIRR: " & XIRR(B2:B10, C2:C10)*100 & "% | Total invested: $" & SUMIF(B2:B10, "<0", B2:B10)*-1 & " | Total returned: $" & SUMIF(B2:B10, ">0", B2:B10) & " | Multiple: " & SUMIF(B2:B10, ">0", B2:B10)/(SUMIF(B2:B10, "<0", B2:B10)*-1)
// Comprehensive investment analysis with XIRR and cash flow metrics

// Risk-adjusted return comparison
="XIRR: " & XIRR(A2:A15, B2:B15)*100 & "% vs Benchmark: " & C1*100 & "% | Excess return: " & (XIRR(A2:A15, B2:B15)-C1)*100 & "bps | Sharpe-like ratio: " & (XIRR(A2:A15, B2:B15)-D1)/E1
// Compare XIRR against benchmarks with risk adjustment
```

### Portfolio Management Analysis  
```spreadsheets
// Multi-investment portfolio XIRR
="Portfolio XIRR: " & XIRR(CONCATENATE(A2:A15, F2:F15, K2:K15), CONCATENATE(B2:B15, G2:G15, L2:L15))*100 & "% | Best performer: " & INDEX({"Stock A"; "Stock B"; "Stock C"}, MATCH(MAX(XIRR(A2:A15, B2:B15), XIRR(F2:F15, G2:G15), XIRR(K2:K15, L2:L15)), {XIRR(A2:A15, B2:B15); XIRR(F2:F15, G2:G15); XIRR(K2:K15, L2:L15)}, 0))
// Portfolio-level XIRR with individual investment ranking

// Dollar-weighted vs time-weighted returns
="Dollar-weighted (XIRR): " & XIRR(A2:A20, B2:B20)*100 & "% vs Time-weighted: " & ((PRODUCT(1+C2:C20))^(365/DAYS(MAX(B2:B20), MIN(B2:B20)))-1)*100 & "% | Timing impact: " & (XIRR(A2:A20, B2:B20)-((PRODUCT(1+C2:C20))^(365/DAYS(MAX(B2:B20), MIN(B2:B20)))-1))*100 & "bps"
// Compare dollar-weighted XIRR with time-weighted returns
```

### Business Financial Analysis
```spreadsheets
// Project evaluation with hurdle rate
=IF(XIRR(A2:A25, B2:B25)>C1, "Accept project - XIRR " & XIRR(A2:A25, B2:B25)*100 & "% exceeds hurdle rate " & C1*100 & "%", "Reject project - XIRR " & XIRR(A2:A25, B2:B25)*100 & "% below hurdle " & C1*100 & "%") & " | NPV at hurdle: $" & XNPV(C1, A2:A25, B2:B25)
// Project acceptance decision using XIRR vs hurdle rate with NPV

// Sensitivity analysis
="Base case XIRR: " & XIRR(A2:A15, B2:B15)*100 & "% | Optimistic (+20%): " & XIRR(A2:A15*1.2, B2:B15)*100 & "% | Pessimistic (-20%): " & XIRR(A2:A15*0.8, B2:B15)*100 & "% | Range: " & (XIRR(A2:A15*1.2, B2:B15)-XIRR(A2:A15*0.8, B2:B15))*100 & "pp"
// XIRR sensitivity analysis across scenarios
```