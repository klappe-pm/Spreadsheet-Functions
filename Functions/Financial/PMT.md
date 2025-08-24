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
tags:
- financial
- excel
- sheets
---
# PMT

## PMT Description

Calculates the periodic payment amount for a loan or investment based on a constant interest rate, fixed payment amount, and specified number of periods. PMT returns a negative value representing money paid out (cash outflow) from the borrower's perspective.

> [!f(x)] PMT Syntax
>
> ```spreadsheets
> PMT(rate, nper, pv, [fv], [type])
> ```
>
> **Parameters:**
> - `rate` (required): Interest rate per period as decimal (e.g., annual rate/12 for monthly payments)
> - `nper` (required): Total number of payment periods
> - `pv` (required): Present value (loan amount or initial investment)
> - `fv` (optional): Future value, defaults to 0 for loans
> - `type` (optional): 0 for payments at end of period (default), 1 for beginning

> [!f(x)] PMT Examples
>
> ```spreadsheets
> // 30-year mortgage calculation
> PMT(0.045/12, 30*12, 250000, 0, 0) → -1216.04
> // $250k loan at 4.5% annual rate, monthly payments
> 
> // Car loan with monthly payments
> PMT(0.06/12, 60, 25000) → -483.32
> // $25k car loan at 6% annual, 5-year term
> 
> // Investment savings goal
> PMT(0.08/12, 20*12, 0, 500000, 0) → -851.49
> // Monthly payment needed to accumulate $500k in 20 years at 8%
> 
> // Lease payment calculation
> PMT(0.04/12, 36, 30000, 15000, 1) → -465.44
> // 3-year lease, $30k value, $15k residual, payments due at start
> 
> // Education loan analysis
> PMT(0.055/12, 10*12, 80000, 0, 0) → -863.42
> // $80k student loan at 5.5%, 10-year repayment
> ```

## Use Cases

### [[Loan calculations]]
- **Mortgage affordability analysis**: Calculate monthly mortgage payments for different loan amounts, rates, and terms to determine affordable home prices
- **Auto loan planning**: Compare payment amounts across different financing options including loan terms, down payments, and interest rates
- **Personal loan evaluation**: Determine monthly payments for debt consolidation, home improvements, or major purchases
- **Student loan planning**: Calculate education loan payments considering different repayment periods and interest rates

### [[Investment planning]]  
- **Retirement savings**: Calculate required monthly contributions to reach retirement goals based on investment returns and time horizons
- **Education funding**: Determine monthly savings needed for children's education costs considering investment growth over time
- **Goal-based investing**: Calculate periodic investment amounts needed to achieve specific financial targets
- **Annuity planning**: Evaluate annuity payment options for retirement income planning

### [[Business financing]]
- **Equipment financing**: Calculate lease versus buy decisions by comparing equipment loan payments to lease payments
- **Working capital loans**: Determine monthly payments for business lines of credit and term loans
- **Real estate investment**: Calculate mortgage payments for investment properties to evaluate cash flow and profitability
- **Small business planning**: Evaluate financing options for business expansion, inventory, or capital improvements

## Related

### Similar Functions

- [[IPMT]] - Calculates interest portion of specific payment, used with PMT for loan analysis
- [[PPMT]] - Calculates principal portion of specific payment, complements PMT calculations
- [[PV]] - Calculates present value, inverse of PMT when solving for loan amount
- [[RATE]] - Calculates interest rate when PMT and other loan terms are known
- [[NPER]] - Calculates number of periods when PMT and other terms are known

## Loan Analysis Functions

### [[IPMT]]
IPMT calculates the interest portion of a specific payment period, working with PMT to break down loan payments into interest and principal components.

```spreadsheets
// Monthly payment breakdown for period 60
="Payment: " & PMT(0.05/12, 360, 200000) & " Interest: " & IPMT(0.05/12, 60, 360, 200000) & " Principal: " & PPMT(0.05/12, 60, 360, 200000)
// Shows total payment and its components

// First year interest calculation
=SUM(IPMT(0.06/12, ROW(1:12), 60, 25000))
// Total interest paid in first year of car loan

// Interest deduction planning for taxes
=ABS(SUM(IPMT(0.045/12, ROW(1:12), 360, A1)))
// Annual mortgage interest for tax deduction calculation
```

### [[PPMT]]  
PPMT calculates the principal portion of payments, complementing PMT analysis by showing how much of each payment reduces the loan balance.

```spreadsheets
// Principal payment progression analysis
="Month 12 principal: " & ABS(PPMT(0.04/12, 12, 360, 300000)) & " Month 120: " & ABS(PPMT(0.04/12, 120, 360, 300000))
// Shows how principal payments increase over time

// Loan balance calculation using PMT and PPMT
=A1 - SUM(PPMT(PMT(0.055/12, 120, A1)/ABS(PMT(0.055/12, 120, A1)), ROW(1:24), 120, A1))
// Balance after 2 years of payments

// Extra payment impact analysis
=PPMT(0.05/12, 60, 240, 150000) + 200
// Regular principal plus $200 extra payment
```

### [[CUMIPMT]]
Calculates cumulative interest between payment periods, extending PMT analysis to show total interest costs over specified timeframes.

```spreadsheets
// Total interest over loan life
="Monthly payment: " & PMT(0.06/12, 180, 100000) & " Total interest: " & ABS(CUMIPMT(0.06/12, 180, 100000, 1, 180, 0))
// 15-year loan payment and total interest cost

// Interest cost comparison for different terms
="30-year interest: " & ABS(CUMIPMT(0.055/12, 360, 200000, 1, 360, 0)) & " vs 15-year: " & ABS(CUMIPMT(0.055/12, 180, 200000, 1, 180, 0))
// Compare total interest for different loan terms

// Refinancing analysis
=ABS(CUMIPMT(0.04/12, 240, 180000, 1, 240, 0)) - ABS(CUMIPMT(0.06/12, 300, 200000, 61, 300, 0))
// Interest savings from refinancing existing loan
```

## Time Value Functions

### [[PV]]
PV calculates present value when PMT is known, enabling loan amount determination from affordability constraints or investment value calculations.

```spreadsheets
// Affordable loan amount from payment capacity
=PV(0.055/12, 360, PMT(0.055/12, 360, 250000), 0, 0)
// Loan amount affordable with $250k loan payment capacity

// Investment valuation using payment streams
=PV(0.08/12, 240, -PMT(0.06/12, 240, 150000), 0, 0)
// Present value of loan payments at different discount rate

// Lease versus buy analysis
=PV(0.05/12, 36, PMT(0.07/12, 36, 30000, 15000, 1), 0, 1)
// Present value of lease payments for comparison to purchase
```

### [[FV]]  
FV calculates future value with PMT, essential for investment planning and loan balance projections at different points in time.

```spreadsheets
// Investment growth with regular payments
="Monthly payment: " & PMT(0.07/12, 300, 0, 1000000, 0) & " grows to: " & FV(0.07/12, 300, PMT(0.07/12, 300, 0, 1000000, 0), 0, 0)
// Verify payment calculation with future value

// Loan balance after payments
=FV(0.045/12, 60, PMT(0.045/12, 360, 220000), 220000, 0)
// Remaining balance after 5 years of mortgage payments

// Sinking fund calculation
=FV(0.06/12, 120, PMT(0.06/12, 120, 0, 250000, 0), 0, 0)
// Future value of payments designed to accumulate $250k
```

### [[RATE]]
RATE determines interest rates when PMT and other loan terms are known, essential for yield analysis and loan comparison.

```spreadsheets
// Effective rate calculation from payment terms
=RATE(60, PMT(0.065/12, 60, 20000), 20000, 0, 0)*12
// Annual rate implicit in loan with known payment

// Investment return analysis
=RATE(240, -PMT(0.08/12, 240, 0, 500000, 0), 0, 500000, 0)*12
// Return rate needed to achieve $500k with calculated payments

// Lease rate determination
=RATE(36, PMT(0.04/12, 36, 25000, 12000, 1), 25000, -12000, 1)*12
// Implicit rate in lease with residual value
```

## Planning Functions

### [[NPER]]
NPER calculates time periods when PMT and other terms are known, essential for payoff timing and goal achievement planning.

```spreadsheets
// Loan payoff time with extra payments
=NPER(0.055/12, PMT(0.055/12, 360, 180000) - 200, 180000, 0, 0)
// Time to pay off mortgage with $200 extra monthly payment

// Investment goal timeline
=NPER(0.09/12, -PMT(0.09/12, 240, 0, 300000, 0), 0, 300000, 0)
// Periods needed to accumulate $300k with calculated payment

// Debt consolidation planning
=NPER(0.08/12, -1500, 45000, 0, 0)
// Time to pay off $45k debt with $1500 monthly payments
```

### [[IF]]
Essential for PMT scenario analysis and payment calculation validation, enabling conditional loan decisions and error handling.

```spreadsheets
// Payment affordability check
=IF(ABS(PMT(0.06/12, 240, A1))>B1, "Payment too high", PMT(0.06/12, 240, A1))
// Only show payment if affordable based on budget constraint

// Term optimization
=IF(ABS(PMT(0.055/12, 180, 200000))<2000, PMT(0.055/12, 180, 200000), PMT(0.055/12, 360, 200000))
// Choose 15-year if payment under $2000, otherwise 30-year

// Loan qualification logic
=IF(A1*0.28>=ABS(PMT(0.045/12, 360, B1)), "Qualified", "Increase down payment")
// Debt-to-income ratio check for mortgage approval
```

### [[ROUND]]
Critical for PMT results since payment amounts must be practical currency values, preventing calculation errors in loan schedules.

```spreadsheets
// Standard payment rounding
=ROUND(PMT(0.0575/12, 300, 185000), 2)
// Round to nearest cent for actual payment amount

// Conservative payment calculation
=ROUNDUP(ABS(PMT(0.06/12, 180, 125000)), 0)
// Round up to next dollar for budgeting safety margin

// Payment schedule consistency
=ROUND(PMT(A1/12, B1*12, C1), 2)
// Ensure consistent rounding across payment calculations
```
