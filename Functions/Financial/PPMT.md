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
# PPMT

## PPMT Description

Calculates the principal payment portion of a loan payment for a specified period. PPMT determines how much of each loan payment goes toward reducing the principal balance, essential for amortization schedules, loan analysis, and understanding payment structure over time.

> [!f(x)] PPMT Syntax
>
> ```spreadsheets
> PPMT(rate, per, nper, pv, [fv], [type])
> ```
>
> **Parameters:**
> - `rate` (required): Interest rate per period as decimal (e.g., annual rate/12 for monthly)
> - `per` (required): Payment period for which to calculate principal payment (1 to nper)
> - `nper` (required): Total number of payment periods
> - `pv` (required): Present value (loan amount) as negative value
> - `fv` (optional): Future value or balloon payment, defaults to 0
> - `type` (optional): 0 for payments at end of period (default), 1 for beginning

> [!f(x)] PPMT Examples
>
> ```spreadsheets
> // First payment principal on 30-year mortgage
> PPMT(0.06/12, 1, 30*12, -250000, 0, 0) → -277.83
> // $277.83 of first payment goes to principal
> 
> // 12th payment principal analysis
> PPMT(0.075/12, 12, 15*12, -150000, 0, 0) → -658.44
> // $658.44 principal payment in month 12
> 
> // Auto loan payment breakdown
> PPMT(0.045/12, 24, 60, -25000, 0, 0) → -380.95
> // $380.95 principal in 24th payment of car loan
> 
> // Business loan with balloon payment
> PPMT(0.08/12, 36, 60, -75000, -15000, 0) → -1015.89
> // Principal payment in month 36 with $15k balloon
> 
> // Beginning-of-period payment analysis
> PPMT(0.055/12, 6, 10*12, -100000, 0, 1) → -736.81
> // 6th principal payment with payments at start of month
> ```

## Use Cases

### [[Loan payment analysis]]
- **Amortization schedule creation**: Calculate principal portion for each payment period to build complete payment schedules
- **Payment structure understanding**: Analyze how principal payments increase over time as interest decreases
- **Refinancing decisions**: Compare principal accumulation rates between different loan terms and rates
- **Early payment impact**: Calculate principal reductions from extra payments and accelerated schedules

### [[Financial planning]]
- **Equity building analysis**: Track home equity growth by calculating principal payments over time
- **Debt reduction strategies**: Plan debt payoff schedules by understanding principal payment progression
- **Budget planning**: Separate loan payments into interest and principal components for tax and budgeting purposes
- **Investment decision support**: Compare loan principal reduction versus alternative investment opportunities

### [[Business financial management]]
- **Asset financing analysis**: Calculate principal payments for equipment and real estate financing
- **Cash flow projections**: Separate loan payments into principal and interest for accurate cash flow modeling
- **Debt service coverage**: Analyze debt service requirements considering principal and interest components
- **Financial reporting**: Allocate loan payments between balance sheet (principal) and income statement (interest)

## Related

### Similar Functions

- [[IPMT]] - Calculates interest payment portion, complementary to PPMT
- [[PMT]] - Calculates total payment amount including principal and interest
- [[CUMPRINC]] - Calculates cumulative principal payments over multiple periods
- [[CUMIPMT]] - Calculates cumulative interest payments over multiple periods
- [[PV]] - Calculates present value of loan or annuity

## Commonly Used With Functions Examples

### Complete Payment Analysis
```spreadsheets
// Payment breakdown by component
="Payment " & A1 & ": Total $" & ABS(PMT(0.06/12, 30*12, -250000, 0, 0)) & " = Principal $" & ABS(PPMT(0.06/12, A1, 30*12, -250000, 0, 0)) & " + Interest $" & ABS(IPMT(0.06/12, A1, 30*12, -250000, 0, 0))
// Complete payment breakdown showing all components

// Amortization schedule
="Year " & A1 & " principal: $" & ABS(CUMPRINC(0.06/12, 30*12, -250000, (A1-1)*12+1, A1*12, 0)) & " | Remaining balance: $" & (250000-ABS(CUMPRINC(0.06/12, 30*12, -250000, 1, A1*12, 0)))
// Annual principal summary with remaining balance
```

### Loan Comparison Analysis
```spreadsheets
// 15-year vs 30-year mortgage comparison
="15-year principal payment " & A1 & ": $" & ABS(PPMT(0.06/12, A1, 15*12, -250000, 0, 0)) & " vs 30-year: $" & ABS(PPMT(0.06/12, A1, 30*12, -250000, 0, 0)) & " | Difference: $" & ABS(PPMT(0.06/12, A1, 15*12, -250000, 0, 0))-ABS(PPMT(0.06/12, A1, 30*12, -250000, 0, 0))
// Compare principal payments between different loan terms

// Refinancing impact analysis
=IF(ABS(PPMT(0.045/12, A1, 15*12, -200000, 0, 0))>ABS(PPMT(0.06/12, A1, 30*12, -250000, 0, 0)), "Refi builds equity faster by $" & ABS(PPMT(0.045/12, A1, 15*12, -200000, 0, 0))-ABS(PPMT(0.06/12, A1, 30*12, -250000, 0, 0)), "Current loan better")
// Refinancing principal building comparison
```

### Business Financial Planning
```spreadsheets
// Equipment financing cash flow impact
="Month " & A1 & " cash impact: Principal $" & ABS(PPMT(0.08/12, A1, 60, -50000, 0, 0)) & " + Interest $" & ABS(IPMT(0.08/12, A1, 60, -50000, 0, 0)) & " = Total $" & ABS(PMT(0.08/12, 60, -50000, 0, 0)) & " | Depreciation offset: $" & (50000/60)
// Equipment financing impact including tax benefits

// Multi-loan portfolio analysis
="Total principal payments: $" & ABS(PPMT(0.075/12, A1, 60, -30000, 0, 0)) + ABS(PPMT(0.065/12, A1, 72, -25000, 0, 0)) + ABS(PPMT(0.085/12, A1, 48, -15000, 0, 0)) & " | Total interest: $" & ABS(IPMT(0.075/12, A1, 60, -30000, 0, 0)) + ABS(IPMT(0.065/12, A1, 72, -25000, 0, 0)) + ABS(IPMT(0.085/12, A1, 48, -15000, 0, 0))
// Portfolio-level debt service analysis
```