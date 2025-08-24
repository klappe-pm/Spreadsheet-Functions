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
    - 2025-08-17
  - - aliases
    - []
  - - tags
    - []
---
# NPV

## NPV Description

Calculates the net present value (NPV) of an investment by discounting a series of future cash flows back to their present value using a specified discount rate. NPV determines whether an investment will be profitable by comparing the present value of cash inflows to the initial investment cost.

> [!f(x)] NPV Syntax
>
> ```spreadsheets
> NPV(rate, value1, [value2], [value3], ...)
> NPV(rate, range)
> NPV(rate, range1, range2, ...)
> ```
>
> **Parameters:**
> - `rate` (required): Discount rate per period as decimal (e.g., 0.10 for 10%)
> - `value1` (required): First cash flow value or range of cash flows
> - `value2, value3, ...` (optional): Additional cash flow values or ranges

> [!f(x)] NPV Examples
>
> ```spreadsheets
> // Simple investment analysis - Initial cost not included in NPV
> NPV(0.10, 1000, 1200, 1500, 800) → 3347.20
> // With initial investment: 3347.20 - 4000 = -652.80 (reject project)
> 
> // Equipment purchase analysis
> NPV(0.12, A2:A6) → calculates NPV of cash flows in range A2:A6
> 
> // Multi-year project evaluation
> NPV(0.08, 15000, 18000, 22000, 25000, 12000) → 73254.74
> 
> // Real estate investment with negative initial cost
> NPV(0.09, -250000, 35000, 38000, 42000, 45000, 275000) → 67889.23
> 
> // Bond valuation using annual coupon payments
> NPV(0.06, 50, 50, 50, 50, 1050) → 1000.00 (par value bond)
> ```

## Use Cases

### [[Investment analysis]]
- **Capital budgeting decisions**: Evaluate multiple investment projects by comparing NPV values to select the most profitable options
- **Equipment replacement analysis**: Determine optimal timing for equipment replacement by comparing NPV of current versus new equipment cash flows
- **Real estate investment evaluation**: Calculate NPV of rental properties considering purchase price, rental income, expenses, and terminal sale value
- **Business acquisition analysis**: Assess acquisition targets by discounting projected future cash flows to determine fair valuation

### [[Project evaluation]]  
- **Research and development projects**: Evaluate R&D investments by discounting expected future revenues from new products or technologies
- **Infrastructure development**: Analyze large-scale infrastructure projects considering construction costs, operational savings, and economic benefits
- **Energy efficiency upgrades**: Calculate NPV of building improvements considering upfront costs versus long-term energy savings
- **Technology implementation**: Assess new system implementations by comparing costs against productivity gains and operational efficiencies

### [[Financial planning]]
- **Retirement planning**: Calculate present value of retirement savings needed to fund future income requirements
- **Education funding**: Determine present value of future education costs to establish appropriate savings targets
- **Loan comparison**: Compare different loan structures by calculating NPV of total payments under various terms and rates
- **Insurance decisions**: Evaluate insurance policies by comparing premiums paid versus expected claim benefits over time

## Related

### Similar Functions

- [[IRR]] - Calculates internal rate of return, the discount rate where NPV equals zero
- [[XNPV]] - Calculates NPV for irregular cash flow dates using specific dates instead of periods
- [[PV]] - Calculates present value of single payment or annuity, simpler version of NPV
- [[FV]] - Calculates future value, opposite time direction of NPV calculations
- [[MIRR]] - Modified internal rate of return addressing IRR limitations with different reinvestment assumptions

## Time Value Functions

### [[PV]]
Used with NPV for single payment present value calculations. PV handles uniform annuities while NPV manages irregular cash flows, often combined for complex financial modeling.

```spreadsheets
// Compare lump sum versus annuity using both functions
=NPV(0.08, 10000, 10000, 10000, 10000, 10000) 
// Returns: 39927.10 for irregular payments

=PV(0.08, 5, 10000, 0, 0)
// Returns: -39927.10 for uniform annuity (negative indicates payment)

// Combine for lease versus buy analysis
=NPV(0.06, A2:A25) + PV(0.06, 60, -500, 0, 0)
// NPV of purchase plus PV of lease payments for comparison
```

### [[FV]]  
Complementary to NPV by calculating future values. FV projects cash flows forward while NPV discounts them back, essential for complete investment analysis and goal planning.

```spreadsheets
// Investment growth analysis using both directions
="NPV: " & NPV(0.10, B2:B10) & " FV: " & FV(0.10, 8, 0, -NPV(0.10, B2:B10), 0)
// Shows both present and future value perspectives

// Retirement planning with NPV and FV
=NPV(0.07, C2:C35) & " needed now to fund " & FV(0.07, 30, -1000, 0, 0) & " goal"
// Present value needed versus future value target

// Project cash flow analysis
=IF(NPV(0.12, D2:D15)>0, FV(0.12, 10, 0, -NPV(0.12, D2:D15), 0), "Reject project")
// If NPV positive, calculate future value of net benefit
```

### [[RATE]]
Determines the discount rate when NPV and cash flows are known. RATE and NPV are inverse functions - RATE finds the rate that produces a target NPV.

```spreadsheets
// Find required return rate for break-even NPV
=RATE(5, 0, -10000, NPV(0.08, A2:A6)+10000, 0)
// Calculates rate needed for zero NPV

// Yield calculation using NPV and RATE
=RATE(10, 500, -NPV(0.06, B2:B11), 0, 0)
// Finds yield when NPV is treated as present value

// Risk-adjusted return analysis
=IF(NPV(0.10, C2:C8)>0, RATE(6, 0, -5000, NPV(0.10, C2:C8)+5000, 0), "Insufficient return")
// Calculates actual return rate if project meets hurdle rate
```

## Cash Flow Functions

### [[IRR]]
Works with NPV to provide complete investment analysis. IRR finds the rate where NPV equals zero, while NPV calculates value at a given rate. Both essential for capital budgeting decisions.

```spreadsheets
// Complete investment evaluation using NPV and IRR
="NPV at 10%: " & NPV(0.10, A2:A8) & " IRR: " & IRR(A1:A8) & "%"
// Shows profitability (NPV) and return rate (IRR)

// Investment ranking using both metrics
=IF(AND(NPV(0.12, B2:B10)>0, IRR(B1:B10)>0.15), "Accept", "Reject")
// Requires positive NPV and IRR above 15% threshold

// Risk assessment combining NPV and IRR
=NPV(0.10, C2:C15) & " value with " & IRR(C1:C15)*100 & "% return vs " & 10 & "% hurdle"
// Compares calculated return against required minimum
```

### [[MIRR]]  
Modified IRR addressing NPV assumptions about reinvestment rates. MIRR uses different rates for financing and reinvestment, providing more realistic return calculations alongside NPV.

```spreadsheets
// Compare IRR versus MIRR with NPV validation
="NPV: " & NPV(0.08, A2:A10) & " IRR: " & IRR(A1:A10) & " MIRR: " & MIRR(A1:A10, 0.08, 0.06)
// Shows all three profitability measures

// Conservative return analysis
=IF(NPV(0.10, B2:B12)>0, MIRR(B1:B12, 0.10, 0.06), "Project unprofitable at 10% discount")
// Only calculates MIRR if NPV is positive

// Risk-adjusted project comparison
=MIRR(C1:C20, RATE(19, 0, -100000, NPV(0.08, C2:C20)+100000, 0), 0.05)
// Uses actual project cost of capital with conservative reinvestment rate
```

## Valuation Functions

### [[XNPV]]
Enhanced NPV for irregular cash flow timing using specific dates. XNPV provides more precise calculations when cash flows don't occur at regular intervals.

```spreadsheets
// Irregular payment schedule analysis
=XNPV(0.10, A2:A15, B2:B15)  
// Where A2:A15 contains cash flows, B2:B15 contains dates

// Compare regular versus irregular timing
="Regular NPV: " & NPV(0.12, C2:C10) & " vs Actual timing: " & XNPV(0.12, C2:C10, D2:D10)
// Shows impact of actual timing on valuation

// Real estate cash flow with specific dates
=XNPV(0.09, E2:E50, F2:F50) - G1
// XNPV of rental cash flows minus initial purchase price
```

### [[NPER]]
Calculates time periods needed for investments, complementing NPV analysis by determining project duration for target returns.

```spreadsheets
// Time to recover investment using NPV
=NPER(0.10, 0, -NPV(0.10, A2:A20), SUM(A2:A20), 0)
// Periods needed for cash flows to equal NPV

// Goal-based investment planning
=NPER(IRR(B1:B15), 0, -10000, NPV(0.08, B2:B15)+10000, 0)
// Time needed for investment to reach NPV target

// Project duration analysis
="Project NPV: " & NPV(0.12, C2:C25) & " achieved over " & NPER(0.12, -2000, 0, NPV(0.12, C2:C25), 0) & " periods"
// Shows NPV and time frame for achievement
```
