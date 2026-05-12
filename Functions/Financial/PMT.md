---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- financial
subTopics:
- loan-calculations
- time-value-of-money
- debt-analysis
- amortization
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Payment
- Loan Payment
- Mortgage Payment
tags:
- financial-modeling
- loan-analysis
- debt-management
- amortization
---

# PMT

## Description

**PMT (Payment)** calculates the periodic payment required to pay off a loan or achieve a future savings goal, assuming constant payments and a constant interest rate. This is one of the most practical financial functions because it answers a question everyone asks: "How much will my monthly payment be?" Whether you are buying a house, financing a car, or planning retirement savings, PMT gives you the exact periodic payment amount.

The function is built on the **time value of money** principle--the idea that money available today is worth more than the same amount in the future because of its earning potential. PMT works backward from this concept: given a loan amount (present value), an interest rate, and a number of payments, it calculates what equal payment amount, when made regularly, will exactly pay off the debt. For savings, it calculates what you need to deposit regularly to reach a future goal.

**Understanding sign conventions is critical:** In spreadsheet financial functions, cash you pay OUT is negative, and cash you receive IN is positive. For a loan: the principal you receive is positive (money coming to you), but the payment you make each month is negative (money leaving you). This means PMT typically returns a **negative number** for loans because it represents money leaving your pocket. If you want a positive number (for display purposes), either use `=-PMT(...)` or wrap in ABS(). For savings calculations where you are making deposits (negative) to reach a future goal (positive), the same logic applies.

PMT has been available since the earliest versions of both Excel and Google Sheets and works identically across platforms. The function assumes payments occur at the **end** of each period by default (ordinary annuity), but you can specify beginning-of-period payments (annuity due) using the optional type parameter. Remember: the interest rate must match the payment frequency--for monthly payments, use a monthly interest rate (annual rate divided by 12).

## Syntax

> [!f(x)] PMT Syntax
>
> ```
> =PMT(rate, nper, pv, [fv], [type])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `rate` | Yes | The interest rate per period. For a 6% annual rate with monthly payments, use 0.06/12 or 0.5%. Must be expressed as a decimal (0.06) or percentage (6%) divided by the number of periods per year. |
| `nper` | Yes | The total number of payment periods. For a 30-year mortgage with monthly payments, use 30*12 = 360. Must match the rate period--if rate is monthly, nper must be in months. |
| `pv` | Yes | The present value--the total amount that a series of future payments is worth now. For loans, this is the loan principal (positive, as you receive this money). For savings, this is typically 0 or the current balance. |
| `fv` | No | The future value--the cash balance you want after the last payment. For loans, this is usually 0 (fully paid off). For savings, this is your target amount. Defaults to 0 if omitted. |
| `type` | No | When payments are due: 0 (or omitted) = end of period (ordinary annuity); 1 = beginning of period (annuity due). Most loans use end-of-period payments. |

### Return Value

Returns a single numeric value representing the payment per period. For loans where you are paying off debt, this is typically negative (money leaving you). For annuities where you are receiving payments, this would be positive.

## Examples

> [!f(x)] PMT Examples

### Example 1: Basic Monthly Loan Payment
```
=PMT(0.06/12, 360, 200000)
```
**Result:** `-$1,199.10`

**Explanation:** Calculates the monthly payment for a $200,000 mortgage at 6% annual interest over 30 years (360 months). The annual rate 0.06 is divided by 12 for monthly rate. The negative result indicates this is money you pay out each month. The borrower will pay $1,199.10 per month.

---

### Example 2: Display Payment as Positive Number
```
=-PMT(0.06/12, 360, 200000)
```
**Result:** `$1,199.10`

**Explanation:** By placing a negative sign before PMT, the result displays as a positive number. This is purely for display purposes--the payment is still money leaving your pocket. Many financial models use this approach for clearer presentation.

---

### Example 3: Car Loan with 5-Year Term
```
=PMT(0.049/12, 60, 25000)
```
**Result:** `-$470.51`

**Explanation:** Monthly payment for a $25,000 car loan at 4.9% APR over 5 years (60 months). Car loans typically have shorter terms than mortgages, resulting in higher monthly payments relative to the loan amount but less total interest paid.

---

### Example 4: Savings Goal - Retirement Contribution
```
=PMT(0.07/12, 360, 0, 1000000)
```
**Result:** `-$820.07`

**Explanation:** How much to save monthly to reach $1,000,000 in 30 years at 7% annual return. Note: pv is 0 (starting from nothing), and fv is 1,000,000 (target). The negative result means you must deposit $820.07 each month. The sign convention is consistent--money leaving you is negative.

---

### Example 5: Savings with Starting Balance
```
=PMT(0.06/12, 240, -50000, 500000)
```
**Result:** `-$586.55`

**Explanation:** Monthly savings needed to grow $50,000 to $500,000 in 20 years at 6%. The existing balance is entered as -50000 (negative) because it represents money you have already "paid out" of your pocket into savings. The future value of 500000 is positive (money you will receive). You need to add $586.55 monthly.

---

### Example 6: Beginning-of-Period Payments (Annuity Due)
```
=PMT(0.06/12, 360, 200000, 0, 1)
```
**Result:** `-$1,193.14`

**Explanation:** Same $200,000 mortgage as Example 1, but with payments at the beginning of each period (type=1), like rent. The payment is slightly lower ($5.96 less) because each payment has one more period to earn interest before the next payment is due. Lease payments often work this way.

---

### Example 7: Quarterly Payments
```
=PMT(0.08/4, 20, 50000)
```
**Result:** `-$3,055.56`

**Explanation:** Quarterly payment on a $50,000 loan at 8% annual rate for 5 years. Rate is divided by 4 for quarterly rate (2% per quarter). Number of periods is 5 years times 4 = 20 quarters. This demonstrates that PMT works for any consistent payment frequency--just match rate and nper.

---

### Example 8: Balloon Payment Loan
```
=PMT(0.07/12, 60, 300000, -100000)
```
**Result:** `-$4,950.58`

**Explanation:** Monthly payment for a $300,000 loan with a $100,000 balloon payment due at the end of 5 years. The future value of -100000 represents debt still owed (you will need to pay it, hence negative from your perspective). Payments are lower than a fully amortizing loan because you are not paying off the full principal.

---

### Example 9: Interest-Only Loan Approximation
```
=PMT(0.06/12, 360, 200000, -200000)
```
**Result:** `-$1,000.00`

**Explanation:** When future value equals present value (both the loan amount), the payment covers interest only--no principal reduction. At 6% on $200,000, monthly interest is $1,000 exactly. This is not a true interest-only loan function, but demonstrates the relationship between payment components.

---

### Example 10: Weekly Payment Calculation
```
=PMT(0.05/52, 260, 15000)
```
**Result:** `-$68.68`

**Explanation:** Weekly payment for a $15,000 loan at 5% over 5 years. Rate is divided by 52 (weeks per year), and nper is 5 years times 52 = 260 weekly payments. Some loans offer weekly or bi-weekly payment options, which can reduce total interest by accelerating principal paydown.

---

### Example 11: Comparing Loan Terms
```
15-year: =PMT(0.055/12, 180, 250000) = -$2,042.71
30-year: =PMT(0.06/12, 360, 250000) = -$1,498.88
```
**Result:** 15-year pays more monthly but less total

**Explanation:** A 15-year mortgage at 5.5% has a $544 higher monthly payment than a 30-year at 6%, but total payments are $367,688 vs $539,595--a savings of $171,907. PMT helps borrowers understand the trade-off between monthly affordability and total cost.

---

### Example 12: Using Cell References
```
=PMT(A1/12, A2*12, A3)
```
Where A1=0.065 (rate), A2=30 (years), A3=350000 (loan amount)

**Result:** `-$2,212.24`

**Explanation:** Building PMT with cell references allows users to change inputs and instantly see new payment amounts. This is the foundation of mortgage calculators and loan comparison spreadsheets. Note the conversion: A1/12 converts annual to monthly rate, A2*12 converts years to months.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Text values in parameters, or non-numeric rate/nper/pv | Ensure all parameters are numbers. Check for hidden text formatting or spaces. |
| `#NUM!` | Impossible calculation (e.g., rate of -100% or nper of 0) | Verify rate is not -1 or less. Ensure nper is at least 1. Check that the combination of values is mathematically possible. |
| `Unexpectedly large payment` | Rate entered as whole number instead of decimal | Convert percentage to decimal: use 0.06 not 6 for 6%. Or use 6% with the percent sign. |
| `Wrong payment amount` | Rate and nper period mismatch | If payments are monthly, rate must be monthly (annual/12) and nper must be in months (years*12). |
| `Payment shows as negative` | This is correct! PMT returns negative for payments out | Use =-PMT() or ABS(PMT()) if you need positive display. Understand: negative = money leaving you. |
| `Different result in calculator` | Rounding differences or type parameter | Online calculators may round differently. Also check if your calculator assumes beginning-of-period payments. |

## Use Cases

### [[Mortgage Affordability Analysis]]

**Scenario:** A first-time homebuyer wants to understand what house price they can afford based on their maximum comfortable monthly payment of $2,500, with a 20% down payment available.

**Implementation:**
```
If PMT(0.065/12, 360, Loan_Amount) = -2500
Then Loan_Amount = PV(0.065/12, 360, -2500) = $394,915
With 20% down: Max house price = $394,915 / 0.80 = $493,644
```

**Business Application:** Real estate professionals and loan officers use PMT calculations to help clients set realistic price ranges before house hunting. By working backward from a comfortable payment, buyers avoid falling in love with homes they cannot afford. Banks use the same calculations for loan pre-approval letters.

**Technical Details:** Include property taxes and insurance in the total payment analysis. A home at this price with $400/month taxes and $150/month insurance would have a total PITI (Principal, Interest, Taxes, Insurance) of $3,050, which may exceed the buyer's true comfort zone.

---

### [[Business Equipment Lease vs. Buy Decision]]

**Scenario:** A company needs a $100,000 piece of equipment and must decide between purchasing with a bank loan versus leasing. The equipment has a 7-year useful life.

**Implementation:**
```
Bank Loan: =PMT(0.08/12, 84, 100000) = -$1,560.35/month
Lease Quote: $1,450/month for 7 years

Comparison:
Total Loan Cost: $1,560.35 * 84 = $131,069 (but you own the asset)
Total Lease Cost: $1,450 * 84 = $121,800 (no ownership)
```

**Business Application:** CFOs and financial analysts use PMT to standardize comparisons between different financing options. The analysis must include residual value, tax implications (depreciation vs. expense), and opportunity cost of capital. PMT provides the base payment figures for the complete financial model.

**Technical Details:** For leases, use type=1 (beginning of period) since most leases require first and last payment upfront. Also consider that lease rates often embed a higher effective interest rate than bank loans--you can back-calculate the implicit rate using RATE function.

---

### [[Debt Payoff Strategy Comparison]]

**Scenario:** An individual has $50,000 in student loans at 5.5% interest and wants to compare payoff strategies: 10-year standard, 15-year extended, and aggressive 5-year payoff.

**Implementation:**
```
10-year standard: =PMT(0.055/12, 120, 50000) = -$542.64
15-year extended: =PMT(0.055/12, 180, 50000) = -$408.54
5-year aggressive: =PMT(0.055/12, 60, 50000) = -$953.87

Total Interest:
10-year: ($542.64 * 120) - $50,000 = $15,117
15-year: ($408.54 * 180) - $50,000 = $23,537
5-year:  ($953.87 * 60) - $50,000 = $7,232
```

**Business Application:** Financial advisors use PMT to help clients visualize the true cost of different repayment timelines. While lower monthly payments seem attractive, showing the total interest difference ($23,537 vs $7,232 is an extra $16,305) often motivates clients to choose more aggressive payoff plans when feasible.

**Technical Details:** The analysis should include opportunity cost--money used for aggressive debt payoff cannot be invested elsewhere. If investment returns exceed loan interest (after tax), a longer payoff with lower payments and more investing might be optimal. PMT enables these scenario comparisons.

---

### [[Retirement Income Planning]]

**Scenario:** A retiree has $800,000 in savings and wants to know how much they can withdraw monthly over 25 years, assuming 4% annual return on remaining balance.

**Implementation:**
```
=PMT(0.04/12, 300, -800000, 0)
```
**Result:** `$4,213.89/month` (positive because you are receiving money)

**Business Application:** Financial planners use PMT in reverse--instead of calculating how much to save, they calculate how much a nest egg can sustainably provide. This helps retirees balance lifestyle desires against longevity risk (outliving their money).

**Technical Details:** The present value is negative because it represents money you "have" (the opposite of owing). The calculation assumes level withdrawals; real retirement planning adds inflation adjustments, variable returns (sequence of returns risk), and reserves for healthcare. Consider also calculating with fv = some reserve amount rather than 0.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 97 through Excel 365 and beyond)
- **Specific Behavior:** Accepts the standard 5 parameters. Type parameter defaults to 0 (end of period).
- **Precision:** Uses IEEE 754 double-precision floating point, generally accurate to 15 significant digits.

### Google Sheets
- **Availability:** All versions since launch
- **Specific Behavior:** Functionally identical to Excel. Same parameter order and defaults.
- **Precision:** Same floating-point precision as Excel.

### Both Platforms
- Return value is negative for payments you make (loans, savings deposits)
- Return value is positive for payments you receive (annuity income)
- Rate and nper must use matching periods (both monthly, both annual, etc.)
- FV defaults to 0; Type defaults to 0
- Use financial number format for currency display

## Tips and Best Practices

1. **Always match rate and nper periods:** This is the most common error. For monthly payments: rate = annual_rate/12 and nper = years*12. For quarterly: rate = annual_rate/4 and nper = years*4. Mismatched periods give dramatically wrong results.

2. **Understand the sign convention:** Money you pay out is negative; money you receive is positive. A loan principal you receive is positive (pv), but your payments are negative (PMT result). For savings, your deposits are negative (going out), and your future value is positive (you will receive it).

3. **Use =-PMT() for positive display:** If you want payments to display as positive numbers in reports, negate the formula. This is purely cosmetic--the underlying cash flow direction does not change.

4. **Include type parameter for lease calculations:** Leases typically require payment at the beginning of each period (type=1). Omitting this when modeling leases will slightly understate the effective payment burden.

5. **Round appropriately for real-world use:** PMT returns precise values like $1,199.1006. Actual loan payments are rounded to cents, which can create minor differences between your model and actual statements over the loan life.

6. **Build flexible models with cell references:** Instead of hardcoding values, use cells for rate, term, and principal. This allows quick what-if analysis: "What if rates go up 0.5%?" or "What if we choose a 15-year instead of 30-year term?"

7. **Calculate total cost, not just payment:** Monthly payment alone does not tell the full story. Multiply PMT by nper to see total payments, then subtract pv to see total interest. A lower monthly payment over more years often costs much more in total.

8. **Verify with IPMT and PPMT:** Use IPMT and PPMT to break down payments into interest and principal components. The first payment's IPMT + PPMT should equal your PMT result--this validates your formula is set up correctly.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[PPMT]] | Principal portion of a specific payment | When you need to know how much of payment #N goes to principal |
| [[IPMT]] | Interest portion of a specific payment | When you need to know how much of payment #N goes to interest |
| [[NPER]] | Number of periods to pay off loan | When you know the payment amount and want to find how long to pay off |
| [[RATE]] | Interest rate per period | When you know the payment and want to find the effective interest rate |
| [[PV]] | Present value of future payments | When you know payments and want to find how much can be borrowed |
| [[FV]] | Future value of investments | When you know payments and want to find ending balance |

### Commonly Used Together

**[[IPMT]]** - Interest Portion of Payment

*Combined with PMT for amortization schedules:*
```
Payment: =PMT($B$1/12, $B$2*12, $B$3)
Interest portion (month 1): =IPMT($B$1/12, 1, $B$2*12, $B$3)
Principal portion: =Payment - Interest
```
Building a full amortization table shows how each payment splits between interest and principal, with principal portion growing over time.

---

**[[PPMT]]** - Principal Portion of Payment

*Combined with PMT to verify amortization:*
```
=IPMT(...) + PPMT(...) should equal =PMT(...)
```
The interest plus principal portions of any payment must sum to the total payment. Use this relationship to validate your formulas.

---

**[[CUMIPMT]]** - Cumulative Interest Paid

*Calculate total interest over a range of periods:*
```
Total interest paid in year 1: =CUMIPMT(0.06/12, 360, 200000, 1, 12, 0)
Total interest over loan life: =PMT(...) * nper - pv
```
CUMIPMT shows total interest between any two payments--useful for tax deduction estimates or comparing payoff strategies.

---

**[[PV]]** - Present Value

*Combined with PMT for affordability analysis:*
```
If max_payment = -2000
Affordable loan amount: =PV(0.06/12, 360, -2000)
```
Working backward from a target payment to find the loan amount you can afford.

---

**[[IF]]** - Conditional Logic

*Combined with PMT for scenario modeling:*
```
=IF(B1="15-year", PMT(0.055/12, 180, 250000), PMT(0.06/12, 360, 250000))
```
Allow users to select loan terms and see payments update dynamically.

## Official Documentation

- **Microsoft Excel:** [PMT function](https://support.microsoft.com/en-us/office/pmt-function-0214da64-9a63-4996-bc20-214433fa6441)
- **Google Sheets:** [PMT function](https://support.google.com/docs/answer/3093185)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 97 (1997) | Original implementation with all 5 parameters |
| Excel 2007+ | All subsequent versions | No changes to function behavior |
| Google Sheets | Original launch | Identical to Excel implementation |

---

*Last updated: 2026-01-10*
