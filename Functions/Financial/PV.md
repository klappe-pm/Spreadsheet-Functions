---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- financial
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
---

# PV

## PV Description

PV calculates the present value of an investment based on constant payments and a constant interest rate.

> [!f(x)] PV Syntax
>
> ```spreadsheets
> PV(rate, nper, pmt, [fv], [type])
> ```
>
> **Parameters:**
> - `rate` (required): Interest rate per period
> - `nper` (required): Number of payment periods
> - `pmt` (required): Payment amount per period
> - `fv` (optional): Future value (default 0)
> - `type` (optional): 0=end of period, 1=beginning

> [!f(x)] PV Examples
>
> ```spreadsheets
> PV(0.05, 10, -1000) → present_value // PV of annuity
> 
> PV(A1/12, B1*12, C1) → loan_amount // Monthly loan calculation
> 
> PV(0.08, 5, 0, 10000) → pv_lump_sum // PV of future lump sum
> ```

## Use Cases

### [[Financial Analysis]]
- **Implementation**: Calculate financial metrics including NPV, IRR, loan payments, and investment returns
- **Business Application**: Support investment decisions, loan analysis, and financial planning processes
- **Technical Details**: Ensure accurate interest calculations, handle different compounding periods, and validate assumptions

### [[Investment Planning]]
- **Implementation**: Evaluate investment opportunities using time value of money calculations and risk analysis
- **Business Application**: Support capital budgeting, retirement planning, and investment portfolio management
- **Technical Details**: Consider cash flow timing, discount rates, and sensitivity analysis for robust planning

### [[Loan Analysis]]
- **Implementation**: Calculate loan payments, amortization schedules, and debt service requirements
- **Business Application**: Support lending decisions, borrowing analysis, and debt management strategies
- **Technical Details**: Handle different payment frequencies, variable rates, and loan structure complexity

## Related

### Similar Functions

- [[FV]] - Related financial function for analytical calculations
- [[PMT]] - Related financial function for analytical calculations
- [[RATE]] - Related financial function for analytical calculations
- [[NPER]] - Related financial function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with PV for conditional logic and decision making:*
```spreadsheets
=IF(PV(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies PV to a range and compares the result to a threshold, returning different text based on the condition

**[[PMT]]** - Related function for analytical workflows

*Use PMT with PV for enhanced analytical workflows:*
```spreadsheets
=PMT(PV(A1:A10))
```
This formula combines PMT and PV for comprehensive data analysis

**[[RATE]]** - Related function for analytical workflows

*Use RATE with PV for enhanced analytical workflows:*
```spreadsheets
=RATE(PV(A1:A10))
```
This formula combines RATE and PV for comprehensive data analysis
