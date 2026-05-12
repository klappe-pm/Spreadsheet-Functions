---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- financial
subTopics:
- valuation
- time-value-of-money
- discounting
- investment-analysis
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Present Value
- Discounted Value
- Current Value
tags:
- financial-modeling
- valuation
- discounting
- investment-analysis
---

# PV

## Description

**PV (Present Value)** calculates what a future sum of money or series of payments is worth in today's dollars, given a specified interest (discount) rate. This is perhaps the most conceptually important financial function because it answers the fundamental investment question: "What should I pay today for money I will receive in the future?" Every asset valuation, bond pricing, lottery payout decision, and investment comparison ultimately relies on present value calculations.

The function is the mathematical expression of the **time value of money**--the principle that a dollar today is worth more than a dollar tomorrow because today's dollar can be invested to earn returns. PV works backward in time: if you know what you will receive in the future (whether a lump sum, regular payments, or both), PV tells you what that future money stream is equivalent to right now. The discount rate represents your required return or opportunity cost--what you could earn on that money elsewhere.

**Understanding sign conventions is essential:** In spreadsheet financial functions, cash flowing IN to you is positive, and cash flowing OUT is negative. For PV calculations: the payments you will receive in the future (pmt) should be positive; the future lump sum you will receive (fv) should also be positive; and the resulting PV is typically **negative** because it represents money you would pay out today to receive those future cash flows. If you are receiving positive future cash flows, you would need to pay a positive amount today (shown as negative in the formula result) to obtain them. To display PV as a positive number, use =-PV(...).

PV has been available since the earliest versions of both Excel and Google Sheets with identical behavior. The function assumes payments occur at the **end** of each period by default (ordinary annuity), but you can specify beginning-of-period payments using the type parameter. As with all time-value-of-money functions, the discount rate must match the payment period--for monthly payments, use a monthly rate.

## Syntax

> [!f(x)] PV Syntax
>
> ```
> =PV(rate, nper, pmt, [fv], [type])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `rate` | Yes | The interest (discount) rate per period. For annual discounting of monthly payments, use the annual rate divided by 12. Enter as decimal (0.06) or percentage (6%) divided by periods per year. |
| `nper` | Yes | The total number of payment periods. For 10 years of monthly payments, use 10*12 = 120. Must match the rate period--if rate is monthly, nper must be in months. |
| `pmt` | Yes | The payment received (or made) each period. For receiving payments, enter as positive. For making payments, enter as negative. Enter 0 if calculating PV of a single future lump sum only. |
| `fv` | No | The future value--a lump sum received at the end of all periods. Enter as positive for money you will receive. Defaults to 0 if omitted. |
| `type` | No | When payments occur: 0 (or omitted) = end of period (ordinary annuity); 1 = beginning of period (annuity due). Beginning-of-period payments have slightly higher PV. |

### Return Value

Returns a single numeric value representing the present value. When pmt and fv represent money you will receive (positive inputs), the result is negative--indicating money you would pay today to obtain those future cash flows. Use =-PV() or ABS(PV()) to display as a positive number.

## Examples

> [!f(x)] PV Examples

### Example 1: Present Value of Future Lump Sum
```
=PV(0.06, 10, 0, 100000)
```
**Result:** `-$55,839.48`

**Explanation:** Calculates what $100,000 received in 10 years is worth today at a 6% annual discount rate. There are no periodic payments (pmt=0). The negative result means you would need to invest $55,839.48 today to have $100,000 in 10 years at 6% growth. This is the flip side of FV--if $55,839 grows to $100,000, then $100,000 discounts back to $55,839.

---

### Example 2: Lottery Payout Comparison - Annuity vs. Lump Sum
```
=PV(0.05, 20, 50000)
```
**Result:** `-$623,110.52`

**Explanation:** A lottery offers $50,000 per year for 20 years (total $1,000,000) or a lump sum today. At a 5% discount rate, those future payments are worth $623,110 in today's dollars. If the lump sum offer is higher than this, take the lump sum. If lower, take the annuity.

---

### Example 3: How Much Loan Can You Afford?
```
=PV(0.065/12, 360, -2000)
```
**Result:** `$316,422.43`

**Explanation:** If you can afford a $2,000 monthly payment at 6.5% for 30 years, how much can you borrow? The payment is negative because it is money you will pay out. The positive result indicates the loan amount you receive. This is the core calculation for mortgage pre-approval.

---

### Example 4: Bond Valuation
```
=PV(0.05, 10, 60, 1000)
```
**Result:** `-$1,077.22`

**Explanation:** Value a bond that pays $60 annual coupon for 10 years, then returns $1,000 face value. At a 5% market rate, this bond is worth $1,077.22--a premium because its 6% coupon exceeds the 5% market rate. If market rates were 7%, the bond would trade at a discount.

---

### Example 5: Comparing Bond Prices at Different Market Rates
```
At 4% market rate: =PV(0.04, 10, 60, 1000) = -$1,162.22 (premium)
At 6% market rate: =PV(0.06, 10, 60, 1000) = -$1,000.00 (par)
At 8% market rate: =PV(0.08, 10, 60, 1000) = -$865.80 (discount)
```
**Result:** Bond prices inversely related to market rates

**Explanation:** A 6% coupon bond trades at par when market rates equal 6%. When market rates drop below the coupon rate, the bond's higher payments become more valuable (premium). When market rates rise above the coupon rate, those fixed payments become less attractive (discount).

---

### Example 6: Retirement Nest Egg Required
```
=PV(0.04/12, 300, 5000)
```
**Result:** `-$946,073.16`

**Explanation:** How much do you need at retirement to withdraw $5,000 monthly for 25 years (300 months), assuming 4% annual returns on the remaining balance? You need approximately $946,000. This is "reverse FV"--instead of calculating what savings grow to, you calculate what is needed to fund withdrawals.

---

### Example 7: Business Acquisition - Value of Cash Flows
```
=PV(0.12, 5, 200000, 500000)
```
**Result:** `-$1,005,311.79`

**Explanation:** A business generates $200,000 annual cash flow for 5 years, then can be sold for $500,000. At a 12% required return (accounting for business risk), these cash flows are worth about $1 million today. If the asking price is $900,000, it is a potentially good investment.

---

### Example 8: Lease vs. Buy - Present Value of Lease Payments
```
=PV(0.08/12, 36, -400, 0, 1)
```
**Result:** `$13,043.12`

**Explanation:** Value a 3-year lease with $400 monthly payments at the beginning of each month (type=1, typical for leases). The 8% is the company's borrowing rate. If purchasing outright costs $13,000, the lease and purchase have equivalent present value--other factors (maintenance, flexibility) should decide.

---

### Example 9: Structured Settlement Valuation
```
=PV(0.06, 15, 25000, 100000)
```
**Result:** `-$285,162.81`

**Explanation:** A settlement pays $25,000 annually for 15 years, plus a $100,000 final payment. At 6% discount rate, this is worth $285,163 today. Settlement purchasing companies offer less than this (their profit margin), typically 10-30% less.

---

### Example 10: Monthly Payments with Annual Rate Conversion
```
=PV(0.09/12, 48, 500)
```
**Result:** `-$20,092.39`

**Explanation:** Value of receiving $500 monthly for 4 years at 9% annual rate. Rate is divided by 12 for monthly; nper is 4*12=48 months. The $24,000 in total payments is worth $20,092 today because future payments are discounted.

---

### Example 11: Zero-Coupon Bond Valuation
```
=PV(0.05, 15, 0, 10000)
```
**Result:** `-$4,810.17`

**Explanation:** A zero-coupon bond pays no interest but returns $10,000 at maturity in 15 years. At 5% discount rate, it is worth $4,810 today. Zero-coupon bonds are pure time-value-of-money instruments--their entire return comes from the discount.

---

### Example 12: Present Value as Positive (for Reporting)
```
=-PV(0.07, 20, 15000)
```
**Result:** `$158,883.28`

**Explanation:** By negating the PV function, the result displays as a positive number, which is often clearer for reporting: "The present value of this income stream is $158,883." The negative sign before PV is purely for display--it does not change the underlying calculation.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Text values in parameters, or non-numeric inputs | Ensure all parameters are numbers. Check for hidden text formatting, spaces, or currency symbols in cells. |
| `#NUM!` | Impossible calculation (e.g., rate of -100%) | Verify rate is greater than -1. Rate of -100% causes division by zero. |
| `Unexpectedly small PV` | Rate entered as whole number instead of decimal | Use 0.06 for 6%, not 6. Alternatively, use 6% with the percent sign. |
| `Wrong present value` | Rate and nper period mismatch | Monthly payments need monthly rate (annual/12) and nper in months (years*12). |
| `Negative PV when expecting positive` | This is correct! PV is negative when valuing positive future cash flows | Use =-PV() for positive display. The negative indicates money you would pay to receive those cash flows. |
| `PV seems too high or low` | Discount rate does not match risk level | Higher risk investments need higher discount rates, producing lower PVs. Verify your rate reflects the true opportunity cost. |

## Use Cases

### [[Investment Property Valuation]]

**Scenario:** A real estate investor is evaluating a rental property generating $2,000 monthly net income. They expect to sell the property in 10 years for $300,000. What is a fair price today?

**Implementation:**
```
Monthly income for 10 years: 120 payments of $2,000
Future sale: $300,000
Required return for real estate: 8%

=PV(0.08/12, 120, 2000, 300000)
```
**Result:** `-$300,867.47` (Property is worth approximately $301,000)

**Business Application:** Real estate investors use PV to determine maximum purchase prices that will meet their return requirements. If the asking price exceeds the calculated PV, the investment will not meet the target return. Negotiating below PV creates excess returns.

**Technical Details:** The 8% discount rate reflects real estate risk--illiquidity, tenant risk, maintenance uncertainty. Adjust for specific property risks. Also consider that rental income typically increases over time; for accuracy, use NPV with projected growing rents rather than constant PMT.

---

### [[Pension Buyout Decision]]

**Scenario:** A company offers employees a choice: keep their pension ($2,500/month for life starting at 65) or accept a lump sum buyout today. The employee is 55 and expects to live to 85.

**Implementation:**
```
Monthly pension: $2,500 for 20 years (age 65-85)
But pension starts in 10 years
Step 1: PV at age 65 of pension payments
Step 2: Discount that value back to today

PV at age 65: =PV(0.05/12, 240, 2500) = -$378,959
PV at age 55: =PV(0.05, 10, 0, 378959) = -$232,623
```
**Result:** Pension is worth approximately $233,000 today

**Business Application:** Employees use PV to evaluate buyout offers objectively. If the company offers more than the calculated PV, the lump sum is better (assuming the employee can invest wisely). If less, keeping the pension is financially superior.

**Technical Details:** Pension valuation is complex--it depends on life expectancy, inflation adjustments (if any), survivor benefits, and the employee's personal discount rate. Risk tolerance matters too: the pension is guaranteed, while lump sum returns depend on investment performance.

---

### [[Business Acquisition - Discounted Cash Flow]]

**Scenario:** An investor is evaluating a small business that generates $150,000 annual cash flow. Cash flow is expected to remain stable for 7 years, after which the business can be sold for 3x cash flow.

**Implementation:**
```
Annual cash flow: $150,000 for 7 years
Terminal value: $150,000 * 3 = $450,000
Required return for small business: 15%

=PV(0.15, 7, 150000, 450000)
```
**Result:** `-$798,466.85`

**Business Application:** PV calculations form the foundation of discounted cash flow (DCF) analysis, the primary valuation method for acquisitions. The 15% discount rate reflects small business risk--higher than public companies. If the asking price is $700,000, there is a potential $98,000 margin of safety.

**Technical Details:** Real DCF analysis uses NPV with projected varying cash flows rather than constant PMT. The terminal value multiplier (3x in this example) depends on industry norms and growth expectations. Always sensitivity-test the discount rate--small changes significantly impact valuation.

---

### [[Lawsuit Settlement Evaluation]]

**Scenario:** A plaintiff won a lawsuit and is offered either a structured settlement of $50,000/year for 15 years or an immediate lump sum of $500,000.

**Implementation:**
```
Structured settlement: =PV(0.06, 15, 50000) = -$485,644
Lump sum offer: $500,000

Comparison:
At 6% discount rate, structured payments worth $485,644
Lump sum offer is $500,000
Lump sum is better by $14,356
```

**Business Application:** Personal injury attorneys and plaintiffs use PV to objectively compare settlement options. The key variable is the discount rate--which reflects what return the plaintiff could earn on a lump sum. A financially sophisticated plaintiff might use 7-8%; a conservative one might use 4-5%.

**Technical Details:** Also consider taxes (structured settlements are often tax-free while lump sum investment earnings may be taxed), inflation protection (some settlements include inflation adjustments), and personal financial discipline. A lump sum that gets spent unwisely is worth zero in practice.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 97 through Excel 365 and beyond)
- **Specific Behavior:** Standard 5-parameter function. Returns negative PV when valuing positive future cash flows.
- **Precision:** IEEE 754 double-precision floating point, accurate to 15 significant digits.

### Google Sheets
- **Availability:** All versions since launch
- **Specific Behavior:** Functionally identical to Excel. Same parameter order, defaults, and sign conventions.
- **Precision:** Same floating-point precision as Excel.

### Both Platforms
- Sign convention: Positive future cash flows (pmt, fv) produce negative PV (money paid out today)
- Rate and nper must use matching time periods
- FV defaults to 0; Type defaults to 0
- For positive PV display, use =-PV() or ABS(PV())

## Tips and Best Practices

1. **Match your rate to your period:** For monthly payments, divide annual rate by 12 and multiply years by 12. Quarterly: divide by 4, multiply by 4. Mismatched periods are the most common error and produce dramatically wrong answers.

2. **Use the right discount rate:** The discount rate should reflect your opportunity cost--what return you could earn on that money elsewhere at similar risk. Higher-risk cash flows require higher discount rates, producing lower present values.

3. **Remember: higher discount rates mean lower present values:** When valuing future money, more aggressive discounting (higher rates) makes that future money worth less today. This is why risky investments are worth less than safe ones with identical cash flows.

4. **Use =-PV() for positive display in reports:** The negative PV result is mathematically correct (representing outflow to obtain inflows), but often confusing in presentations. Negate the function for clearer reporting.

5. **Combine PV calculations for complex scenarios:** For a delayed annuity (payments starting in the future), first calculate PV at the start date of payments, then discount that lump sum back to today. Chain multiple PV calculations as needed.

6. **Sensitivity test your discount rate:** PV is highly sensitive to the discount rate. Calculate PV at multiple rates (optimistic, base case, pessimistic) to understand the range of possible values before making decisions.

7. **Use PV for loan affordability analysis:** With PMT known (what you can afford to pay), PV tells you the maximum loan amount. This is how banks calculate pre-approval amounts.

8. **Compare present values, not future totals:** When choosing between payment streams with different timing, always compare present values--not the sum of undiscounted payments. Timing matters.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[FV]] | Future value of present money | When you know today's amount and want to find future value |
| [[NPV]] | Net present value of irregular cash flows | When cash flows vary each period (not constant payments) |
| [[PMT]] | Payment per period | When you know PV and want to find required payments |
| [[NPER]] | Number of periods | When you know PV, payment, and rate, want to find time |
| [[RATE]] | Interest rate per period | When you know PV, payment, and nper, want to find rate |

### Commonly Used Together

**[[PMT]]** - Calculate Required Payments

*Combined with PV for loan analysis:*
```
Maximum loan amount at $2,000/month payment:
=PV(0.07/12, 360, -2000) = $300,714.42

Verify with PMT:
=PMT(0.07/12, 360, 300714.42) = -$2,000.00
```
PV finds loan amount from payment; PMT finds payment from loan amount.

---

**[[FV]]** - Future Value Verification

*Combined with PV for time-value consistency check:*
```
PV of $100,000 in 10 years at 6%:
=PV(0.06, 10, 0, 100000) = -$55,839.48

Verify: FV of that amount:
=FV(0.06, 10, 0, -55839.48) = $100,000.00
```
PV and FV are mathematical inverses--use them to cross-check calculations.

---

**[[NPV]]** - Variable Cash Flow Valuation

*Combined with PV for complex scenarios:*
```
Simple annuity: =PV(0.08, 5, 10000) = -$39,927.10

Variable cash flows: =NPV(0.08, 8000, 10000, 12000, 11000, 15000) = $42,637.87
```
Use PV for constant payments; use NPV when payments vary each period.

---

**[[IRR]]** - Finding Break-Even Rate

*Combined with PV for investment analysis:*
```
If investment costs $50,000 and pays $15,000/year for 5 years:
=IRR({-50000, 15000, 15000, 15000, 15000, 15000}) = 15.24%

At that rate, PV equals investment:
=PV(0.1524, 5, 15000) = -$50,000
```
IRR finds the rate where PV of cash flows equals the initial investment.

---

**[[IF]]** - Conditional Valuation

*Combined with PV for decision modeling:*
```
=IF(PV(0.06, 10, 20000) < -LumpSumOffer, "Take Lump Sum", "Keep Annuity")
```
Automate recommendation based on comparing PV to an alternative offer.

## Official Documentation

- **Microsoft Excel:** [PV function](https://support.microsoft.com/en-us/office/pv-function-23879d31-0e02-4321-be01-da16e8168cbd)
- **Google Sheets:** [PV function](https://support.google.com/docs/answer/3093188)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 97 (1997) | Original implementation with all 5 parameters |
| Excel 2007+ | All subsequent versions | No changes to function behavior |
| Google Sheets | Original launch | Identical to Excel implementation |

---

*Last updated: 2026-01-10*
