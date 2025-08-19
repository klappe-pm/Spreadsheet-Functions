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

# IRR

## IRR Description

Calculates the internal rate of return (IRR) for a series of cash flows, representing the discount rate at which the net present value (NPV) of all cash flows equals zero. IRR is the break-even rate of return for an investment, indicating the maximum rate of borrowing that would still make the project profitable.

> [!f(x)] IRR Syntax
>
> ```spreadsheets
> IRR(values, [guess])
> ```
>
> **Parameters:**
> - `values` (required): Array or range containing cash flows, must include at least one positive and one negative value
> - `guess` (optional): Initial estimate for IRR calculation, defaults to 0.1 (10%)

> [!f(x)] IRR Examples
>
> ```spreadsheets
> // Simple investment project analysis
> IRR(A1:A6) → 0.2343 (23.43% return)
> // Where A1=-10000, A2=2000, A3=3000, A4=4000, A5=4000, A6=3000
> 
> // Equipment purchase with salvage value
> IRR({-50000, 12000, 15000, 18000, 20000, 35000}) → 0.1547 (15.47%)
> 
> // Real estate investment including sale
> IRR(B1:B11) → calculates IRR for 10-year real estate investment
> // B1=-250000 (purchase), B2:B10=monthly net income, B11=sale proceeds
> 
> // Start-up business cash flows with initial guess
> IRR(C1:C8, 0.15) → uses 15% as starting point for iteration
> 
> // Bond yield calculation
> IRR({-980, 50, 50, 50, 1050}) → 0.0563 (5.63% yield to maturity)
> ```

## Use Cases

### [[Capital budgeting]]
- **Investment project evaluation**: Compare IRR against required rate of return (hurdle rate) to accept or reject capital investments
- **Project ranking decisions**: Rank multiple projects by IRR when capital is limited, selecting highest return investments first
- **Equipment replacement analysis**: Calculate IRR of new equipment versus continuing with existing equipment maintenance costs
- **Acquisition analysis**: Determine IRR of business acquisitions to evaluate against alternative investment opportunities

### [[Performance measurement]]  
- **Portfolio return analysis**: Calculate IRR of investment portfolios considering all deposits, withdrawals, and market value changes
- **Fund manager evaluation**: Assess mutual fund or private equity performance using IRR to account for timing of cash flows
- **Real estate investment returns**: Measure property investment performance including purchase, improvements, rental income, and sale proceeds
- **Venture capital returns**: Evaluate startup investments considering multiple funding rounds and eventual exit valuations

### [[Financial planning]]
- **Retirement savings optimization**: Calculate IRR needed from investment portfolio to meet retirement income goals
- **Education funding strategies**: Determine required return rates for education savings plans to meet future tuition costs  
- **Loan refinancing decisions**: Compare IRR of current loan payments versus refinancing costs and new payment schedule
- **Life insurance evaluation**: Calculate IRR of permanent life insurance policies considering premiums, cash value growth, and benefits

## Related

### Similar Functions

- [[NPV]] - Calculates net present value, IRR is the rate where NPV equals zero
- [[MIRR]] - Modified internal rate of return using different financing and reinvestment rates
- [[XIRR]] - IRR for irregular cash flow dates using specific dates instead of periods
- [[RATE]] - Calculates rate for annuity payments, simpler version for uniform cash flows
- [[YIELD]] - Calculates bond yield to maturity, specialized IRR for bond pricing

## Time Value Functions

### [[NPV]]
IRR and NPV are complementary functions for investment analysis. NPV calculates dollar value at given rate, while IRR finds the rate for zero NPV. Both essential for complete project evaluation.

```spreadsheets
// Complete investment analysis using both metrics
="IRR: " & IRR(A1:A10)*100 & "% NPV at 12%: $" & NPV(0.12, A2:A10) + A1
// Shows both return rate and dollar value

// Investment decision logic
=IF(AND(IRR(B1:B15)>0.15, NPV(0.12, B2:B15)+B1>0), "Accept", "Reject")
// Requires IRR above 15% AND positive NPV at 12%

// Risk-adjusted comparison
=IRR(C1:C20) & " vs hurdle rate " & 0.12 & " with NPV of " & NPV(0.12, C2:C20)+C1
// Compares calculated IRR against required minimum rate
```

### [[RATE]]  
RATE calculates interest rates for uniform annuities while IRR handles irregular cash flows. RATE is simpler for standard loans and investments with equal payments.

```spreadsheets
// Compare loan rate versus investment IRR
="Loan rate: " & RATE(60, -500, 25000, 0, 0)*12 & " Investment IRR: " & IRR(A1:A15)
// Monthly loan rate annualized versus project IRR

// Break-even analysis using both functions
=IF(IRR(B1:B30)>RATE(24, -1000, 20000, 0, 0)*12, "Investment beats loan", "Finance with debt")
// Compare investment return versus financing cost

// Refinancing decision support
=RATE(120, -PMT(IRR(C1:C10)/12, 120, -100000, 0, 0), 95000, 0, 0)*12
// New loan rate based on IRR cash flow capacity
```

### [[PV]]
PV calculates present value of annuities while IRR finds the discount rate. Combined, they validate cash flow projections and investment assumptions.

```spreadsheets
// Validate IRR calculation using PV
=PV(IRR(A1:A20), 19, 0, -SUM(A2:A20), 0) + A1
// Should equal zero if IRR is correct

// Investment goal planning
=PV(IRR(B1:B25), 24, 0, -500000, 0)
// Present value needed to achieve $500k using calculated IRR

// Cash flow adequacy test
=IF(PV(IRR(C1:C15)/4, 56, 0, -200000, 0)<ABS(C1), "Sufficient initial investment", "Need more capital")
// Tests if initial investment adequate for target future value
```

## Advanced IRR Functions

### [[MIRR]]
Modified IRR addresses IRR limitations by using separate rates for financing (negative cash flows) and reinvestment (positive cash flows), providing more realistic return calculations.

```spreadsheets
// Compare IRR versus MIRR for realistic assessment
="Standard IRR: " & IRR(A1:A12)*100 & "% MIRR: " & MIRR(A1:A12, 0.10, 0.06)*100 & "%"
// IRR assumes reinvestment at IRR rate, MIRR uses market rates

// Conservative return analysis
=IF(MIRR(B1:B20, 0.08, 0.05)>0.12, "Acceptable return", "Below threshold")
// Uses borrowing rate 8%, reinvestment rate 5%, threshold 12%

// Risk-adjusted project evaluation
=MIRR(C1:C25, IRR(C1:C25), 0.04)
// Uses project's own IRR for financing, 4% for safe reinvestment
```

### [[XIRR]]  
XIRR calculates IRR for irregular cash flow dates using specific dates instead of assuming periodic intervals, essential for real-world investment analysis.

```spreadsheets
// Compare periodic versus actual date IRR
="Periodic IRR: " & IRR(A2:A20) & " Actual dates: " & XIRR(A2:A20, B2:B20)
// Where B column contains specific dates

// Real estate investment with irregular cash flows  
=XIRR(C2:C50, D2:D50)
// Accounts for actual rental payment dates and improvement costs

// Private equity fund analysis
="Fund IRR with timing: " & XIRR(E2:E30, F2:F30)*100 & "%"
// Considers actual capital call and distribution dates
```

### [[YIELD]]
YIELD calculates bond yield to maturity, a specialized IRR for bond investments considering price, coupon rate, and time to maturity.

```spreadsheets
// Bond analysis using IRR versus YIELD
="IRR method: " & IRR({-950, 40, 40, 40, 1040})*2 & " YIELD function: " & YIELD(TODAY(), TODAY()+365*3, 0.04, 95, 100, 2)
// Compare direct cash flow IRR versus bond yield calculation

// Bond portfolio yield analysis
=YIELD(DATE(2025,1,1), DATE(2030,1,1), IRR(A1:A11), 98, 100, 1)
// Uses IRR as coupon rate to find equivalent yield

// Credit spread analysis
=YIELD(B1, B2, 0.05, B3, 100, 2) - IRR(C1:C11)
// Spread between bond yield and comparable investment IRR
```

## Validation Functions

### [[IF]]
Essential for IRR validation and decision logic since IRR can return errors or unrealistic results. IF provides error handling and conditional investment decisions.

```spreadsheets
// IRR validation with error handling
=IF(ISERROR(IRR(A1:A15)), "No valid IRR found", IRR(A1:A15)*100 & "%")
// Handles cases where IRR cannot be calculated

// Investment decision logic
=IF(IRR(B1:B25)>0.15, "Accept project", IF(IRR(B1:B25)>0.10, "Consider", "Reject"))
// Tiered decision making based on IRR thresholds

// Multiple IRR detection
=IF(COUNT(IF(NPV(ROW(1:50)/100, C2:C20)+C1=0, ROW(1:50)/100))>1, "Multiple IRRs possible", IRR(C1:C20))
// Warns when cash flows might produce multiple IRR solutions
```

### [[ISERROR]]
Critical for IRR error handling since IRR may not converge or may not exist for certain cash flow patterns. ISERROR prevents formula errors in financial models.

```spreadsheets
// Robust IRR calculation with fallback
=IF(ISERROR(IRR(A1:A30)), "IRR undefined - check cash flows", ROUND(IRR(A1:A30)*100, 2) & "%")
// Provides user-friendly error message

// IRR existence validation
=IF(ISERROR(IRR(B1:B40)), IF(SUM(B1:B40)>0, "All positive cash flows", "All negative cash flows"), "IRR: " & IRR(B1:B40))
// Diagnoses why IRR calculation failed

// Investment screening with error protection  
=IF(ISERROR(IRR(C1:C50)), "Skip", IF(IRR(C1:C50)>0.12, "Invest", "Pass"))
// Safely evaluates multiple investment opportunities
```
