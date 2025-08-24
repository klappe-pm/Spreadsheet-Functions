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
# PV

## PV Description

Calculates the present value of an investment or loan based on a constant interest rate, regular payments, and a specified number of periods. PV determines what a series of future payments or a future lump sum is worth today, fundamental for investment valuation and loan analysis.

> [!f(x)] PV Syntax
>
> ```spreadsheets
> PV(rate, nper, pmt, [fv], [type])
> ```
>
> **Parameters:**
> - `rate` (required): Interest rate per period as decimal (e.g., annual rate/12 for monthly)
> - `nper` (required): Total number of payment periods
> - `pmt` (required): Payment amount per period (negative for payments made, positive for payments received)
> - `fv` (optional): Future value or lump sum amount, defaults to 0
> - `type` (optional): 0 for payments at end of period (default), 1 for beginning

> [!f(x)] PV Examples
>
> ```spreadsheets
> // Annuity present value calculation
> PV(0.08/12, 20*12, -500, 0, 0) → 59777.15
> // Present value of $500 monthly payments for 20 years at 8% annual
> 
> // Loan amount calculation from payment capacity
> PV(0.055/12, 30*12, -1500, 0, 0) → 260221.50
> // Maximum loan amount for $1500 monthly payment at 5.5% over 30 years
> 
> // Bond valuation with face value
> PV(0.06/2, 10*2, 40, 1000, 0) → 1000.00
> // Present value of bond paying $40 semi-annually, $1000 face value
> 
> // Lottery payment present value
> PV(0.07, 20, 50000, 0, 1) → 529702.67
> // Present value of $50k annual payments for 20 years, payments at start
> 
// Retirement annuity valuation
> PV(0.05, 25, -2000, 100000, 0) → 36329.61
> // Present value of retirement plan: $2k annual payments plus $100k lump sum
> ```

## Use Cases

### [[Investment valuation]]
- **Bond pricing**: Calculate present value of bond coupon payments and principal repayment to determine fair market value
- **Stock dividend analysis**: Value dividend-paying stocks by discounting expected future dividend payments to present value
- **Annuity evaluation**: Determine present value of annuity contracts for retirement planning and insurance decisions
- **Real estate investment**: Calculate present value of rental income streams to evaluate property investment opportunities

### [[Loan analysis]]  
- **Mortgage affordability**: Determine maximum loan amount based on monthly payment capacity and prevailing interest rates
- **Debt consolidation**: Calculate present value of existing debt payments to compare with consolidation loan offers
- **Equipment financing**: Evaluate lease versus purchase decisions by comparing present values of payment streams
- **Business loan evaluation**: Assess loan terms by calculating present value of all payments and comparing to loan proceeds

### [[Financial planning]]
- **Retirement planning**: Calculate present value of required retirement income to determine current savings needs
- **Education funding**: Determine present value of future tuition costs to establish current savings targets
- **Insurance settlements**: Evaluate structured settlements by calculating present value of future payment streams
- **Estate planning**: Value future inheritance payments or trust distributions for current financial planning

## Related

### Similar Functions

- [[FV]] - Calculates future value, opposite direction of PV calculations
- [[NPV]] - Calculates net present value for irregular cash flows, extends PV concept
- [[PMT]] - Calculates payment amount, inverse of PV when solving for payments
- [[RATE]] - Calculates interest rate when PV and other terms are known
- [[NPER]] - Calculates time periods when PV and other terms are known

## Time Value Functions

### [[FV]]
FV and PV are inverse functions for time value calculations. PV discounts future values to present, while FV compounds present values to future. Essential for complete financial analysis.

```spreadsheets
// Investment validation using both PV and FV
="Initial investment: " & PV(0.07, 10, -1000, 0, 0) & " grows to: " & FV(0.07, 10, -1000, PV(0.07, 10, -1000, 0, 0), 0)
// Verify present value calculation with future value

// Savings goal planning
=PV(0.06, 15, PMT(0.06, 15, 0, FV(0.06, 15, -800, 0, 0), 0), 0, 0)
// Present value needed to fund future goal with calculated payment

// Time value demonstration
="$10,000 today vs " & FV(0.08, 20, 0, -10000, 0) & " in 20 years at 8%"
// Shows growth from present to future value
```

### [[NPV]]  
NPV extends PV concept to handle irregular cash flows and multiple periods. PV handles uniform payments while NPV manages varying cash flows over time.

```spreadsheets
// Compare regular versus irregular cash flows
="Regular PV: " & PV(0.10, 5, -5000, 0, 0) & " Irregular NPV: " & NPV(0.10, A2:A6)
// PV for equal payments versus NPV for varying amounts

// Investment decision comparison
=IF(PV(0.12, 10, -2000, 0, 0)>NPV(0.12, B2:B11), "Choose annuity", "Choose irregular payments")
// Compare uniform versus irregular payment streams

// Cash flow analysis validation
=PV(0.08, 20, -NPV(0.08, C2:C21)/20, 0, 0)
// Present value of average payment versus NPV of actual payments
```

### [[PMT]]
PMT and PV work together for loan and investment calculations. PMT calculates payments when PV is known, while PV determines loan amounts when payments are known.

```spreadsheets
// Loan capacity analysis
="Payment capacity: " & PMT(0.055/12, 360, PV(0.055/12, 360, -1800, 0, 0), 0, 0)
// Payment for loan amount based on present value calculation

// Investment funding calculation
=PV(0.09, 25, PMT(0.09, 25, 0, -500000, 0), 0, 0)
// Present value needed for payments that grow to $500k

// Affordability validation
=IF(ABS(PMT(0.06/12, 240, A1))<=B1, PV(0.06/12, 240, -B1, 0, 0), "Reduce loan amount")
// Maximum loan amount based on payment capacity
```

## Rate and Time Functions

### [[RATE]]
RATE calculates interest rates when PV and other loan terms are known. RATE and PV are inverse functions for determining unknown variables in time value calculations.

```spreadsheets
// Yield calculation from present value
=RATE(10, -500, PV(0.08, 10, -500, 0, 0), 0, 0)
// Rate that produces specific present value with given payments

// Investment return analysis
="Required rate: " & RATE(20, -1000, A1, 0, 0)*100 & "% for $1000 annual payments"
// Rate needed to justify present value investment

// Present value validation
=PV(RATE(15, -2000, 25000, 0, 0), 15, -2000, 0, 0)
// Should equal $25,000 if rate calculation correct
```

### [[NPER]]  
NPER calculates time periods when PV and other terms are known. NPER and PV together solve for time required to achieve financial goals.

```spreadsheets
// Investment duration analysis
=NPER(0.07, -1200, PV(0.07, 15, -1200, 0, 0), 0, 0)
// Should equal 15 years if present value calculated correctly

// Goal achievement timeline
="Need " & NPER(0.06, -800, A1, 0, 0) & " years to fund with $800 annual payments"
// Time required based on present value available

// Loan term optimization
=NPER(0.055/12, PMT(0.055/12, 360, PV(0.055/12, 360, -1400, 0, 0)), PV(0.055/12, 360, -1400, 0, 0), 0, 0)
// Verify loan term consistency across calculations
```

## Validation Functions

### [[IF]]
Essential for PV scenario analysis and investment decision logic. IF enables conditional present value calculations and validation of financial assumptions.

```spreadsheets
// Investment decision logic
=IF(PV(0.08, 10, -2000, 0, 0)>15000, "Accept investment", "Reject")
// Decision based on present value threshold

// Rate sensitivity analysis
=IF(PV(0.10, 20, -1500, 0, 0)<PV(0.12, 20, -1500, 0, 0)*0.9, "Rate sensitive", "Rate stable")
// Compare present values at different discount rates

// Payment affordability validation
=IF(PV(A1/12, B1*12, -C1, 0, 0)>D1, "Loan too large", PV(A1/12, B1*12, -C1, 0, 0))
// Only show present value if within budget constraints
```

### [[ISERROR]]
Critical for PV error handling since invalid parameters can cause calculation errors. ISERROR ensures robust financial models and user-friendly error messages.

```spreadsheets
// Robust present value calculation
=IF(ISERROR(PV(A1, B1, C1, D1, E1)), "Invalid parameters", PV(A1, B1, C1, D1, E1))
// Handle calculation errors gracefully

// Parameter validation
=IF(ISERROR(PV(0.05, 10, -1000, 0, 0)), "Check inputs", ROUND(PV(0.05, 10, -1000, 0, 0), 2))
// Validate inputs before showing result

// Investment screening
=IF(ISERROR(PV(B2, C2, D2, E2, F2)), "Skip", IF(PV(B2, C2, D2, E2, F2)>10000, "Consider", "Pass"))
// Screen investments with error protection
```

### [[ABS]]
Often used with PV since present value results can be negative depending on cash flow direction. ABS ensures consistent interpretation of present value amounts.

```spreadsheets
// Present value magnitude
="Investment worth " & ABS(PV(0.09, 15, -1800, 0, 0)) & " in today's dollars"
// Show absolute value for clarity

// Comparison analysis
=IF(ABS(PV(0.08, 20, -1000, 0, 0))>ABS(PV(0.10, 20, -1000, 0, 0)), "Lower rate better", "Higher rate acceptable")
// Compare present value magnitudes

// Budget planning
="Required funding: $" & ABS(PV(0.06, 25, -2500, 0, 0))
// Show funding requirement as positive amount
```
