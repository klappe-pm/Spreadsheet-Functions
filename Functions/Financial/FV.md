---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- financial
subTopics:
- investment-analysis
- time-value-of-money
- retirement-planning
- compound-growth
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Future Value
- Compound Interest
- Investment Growth
tags:
- financial-modeling
- investment-analysis
- retirement-planning
- compound-interest
---

# FV

## Description

**FV (Future Value)** calculates what a series of regular payments or a lump sum will be worth at a future date, given a constant interest rate. This is one of the most empowering financial functions because it answers the question that drives all savings and investing: "How much will I have in the future?" Whether planning for retirement, saving for education, or projecting investment growth, FV reveals the power of compound interest and regular contributions over time.

The function embodies the **time value of money** principle--the concept that money today can earn returns and become more money tomorrow. FV works forward in time: given what you have now (present value), what you will add regularly (payments), and the rate of return, it calculates the accumulated total at the end. This is the opposite perspective from PV, which works backward from future amounts to present values. Understanding FV helps you visualize why starting to save early matters so much--the same contributions made 10 years earlier can result in dramatically higher final balances.

**Understanding sign conventions is essential:** In spreadsheet financial functions, cash flowing OUT of your pocket is negative, and cash flowing IN to you is positive. For a savings plan: the money you deposit (pmt) is negative because it leaves your pocket; any initial investment (pv) is also negative for the same reason; and the FV result is typically **positive** because it represents money you will receive in the future. However, if you are modeling a loan from the lender's perspective, signs flip--principal lent is negative (money out), and future value of repayments is positive (money back).

FV has been available since the earliest versions of both Excel and Google Sheets with identical behavior. The function assumes contributions occur at the **end** of each period by default (ordinary annuity), but you can specify beginning-of-period contributions (annuity due) using the optional type parameter--this makes a noticeable difference over long time periods. Critical reminder: the interest rate must match the payment period--for monthly contributions, use a monthly rate (annual rate divided by 12).

## Syntax

> [!f(x)] FV Syntax
>
> ```
> =FV(rate, nper, pmt, [pv], [type])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `rate` | Yes | The interest rate per period. For a 7% annual return with monthly contributions, use 0.07/12. Must be expressed as a decimal (0.07) or percentage (7%) divided by the number of periods per year. |
| `nper` | Yes | The total number of payment periods. For 30 years of monthly contributions, use 30*12 = 360. Must match the rate period--if rate is monthly, nper must be in months. |
| `pmt` | Yes | The payment made each period. Must be the same throughout. Enter as negative for money you pay out (savings deposits). Enter 0 if calculating growth of a lump sum only. |
| `pv` | No | The present value--the lump sum you start with today. Enter as negative for money you are investing. Defaults to 0 if omitted (starting from nothing). |
| `type` | No | When payments are made: 0 (or omitted) = end of period (ordinary annuity); 1 = beginning of period (annuity due). Beginning-of-period yields slightly higher FV because each payment has one extra period to grow. |

### Return Value

Returns a single numeric value representing the future value. For savings/investments where you are depositing money (negative pmt and/or pv), the result is positive (money you will receive). The sign follows cash flow logic: positive = money coming to you.

## Examples

> [!f(x)] FV Examples

### Example 1: Monthly Retirement Contributions
```
=FV(0.07/12, 360, -500, 0)
```
**Result:** `$610,003.10`

**Explanation:** Calculates the future value of contributing $500 per month for 30 years at 7% annual return. The payment is negative because it represents money leaving your pocket each month. Starting from $0 (pv omitted defaults to 0), you will accumulate over $610,000. Total contributions: only $180,000. The remaining $430,000 is investment growth.

---

### Example 2: Lump Sum Investment Growth
```
=FV(0.08, 20, 0, -10000)
```
**Result:** `$46,609.57`

**Explanation:** Calculates what a one-time $10,000 investment grows to in 20 years at 8% annual return. There are no periodic payments (pmt=0). The present value is negative because you are putting that money in. This demonstrates pure compound growth--$10,000 becomes nearly $47,000 with no additional contributions.

---

### Example 3: Combining Lump Sum with Regular Contributions
```
=FV(0.06/12, 240, -400, -25000)
```
**Result:** `$308,621.69`

**Explanation:** Starting with $25,000 and adding $400 monthly for 20 years at 6% annual return. Both pv (-25000) and pmt (-400) are negative because they represent money you invest. The initial lump sum grows while regular contributions add and compound. This models a typical 401(k) rollover plus ongoing contributions scenario.

---

### Example 4: Beginning-of-Period Contributions
```
=FV(0.07/12, 360, -500, 0, 1)
```
**Result:** `$613,561.78`

**Explanation:** Same as Example 1, but with contributions at the beginning of each month (type=1) instead of the end. The difference is $3,558.68 more--because each payment gets one extra month to earn returns. For long-term savings, contributing early in each period (like on payday) yields noticeably better results.

---

### Example 5: Child's Education Savings
```
=FV(0.05/12, 216, -300)
```
**Result:** `$97,568.08`

**Explanation:** Saving $300 monthly for a child's education from birth to age 18 (216 months) at 5% annual return. Parents contributing $300/month put in $64,800 total but end up with nearly $100,000 due to 18 years of compounding. This shows why 529 plans work well even with modest contributions.

---

### Example 6: Annual Bonus Investment
```
=FV(0.09, 25, -5000)
```
**Result:** `$423,504.48`

**Explanation:** Investing a $5,000 annual bonus for 25 years at 9% annual return. Note: rate is annual (0.09), nper is years (25), and payment is yearly (-5000). No division needed because all periods are annual. Total invested: $125,000. Final value: $423,504.

---

### Example 7: Compare Rates - Sensitivity Analysis
```
Conservative (5%): =FV(0.05/12, 360, -500) = $418,691.24
Moderate (7%): =FV(0.07/12, 360, -500) = $610,003.10
Aggressive (9%): =FV(0.09/12, 360, -500) = $902,768.68
```
**Result:** Higher rates dramatically increase final value

**Explanation:** Same $500 monthly contribution over 30 years shows the exponential impact of return rates. The difference between 5% and 9% is nearly $500,000 on the same contributions. This analysis helps investors understand risk/reward trade-offs and why portfolio allocation matters.

---

### Example 8: How Starting Early Matters
```
Start at 25, retire at 65: =FV(0.07/12, 480, -300) = $795,823.80
Start at 35, retire at 65: =FV(0.07/12, 360, -300) = $366,001.86
Start at 45, retire at 65: =FV(0.07/12, 240, -300) = $155,928.56
```
**Result:** Starting 10 years earlier more than doubles the outcome

**Explanation:** Contributing $300/month at 7% shows the power of time. Starting at 25 produces more than double what starting at 35 produces, and more than 5x what starting at 45 produces. The total contributions differ ($144,000 vs $108,000 vs $72,000), but time-compounding dominates.

---

### Example 9: Quarterly Contributions
```
=FV(0.08/4, 40, -2500, -10000)
```
**Result:** `$160,101.92`

**Explanation:** Quarterly contributions of $2,500 for 10 years (40 quarters) at 8% annual rate, starting with $10,000. Rate is divided by 4 for quarterly. This models business profit sharing or periodic bonus investments.

---

### Example 10: Zero Interest (Pure Savings)
```
=FV(0, 120, -1000)
```
**Result:** `$120,000.00`

**Explanation:** With 0% interest, FV simply sums the contributions. 120 payments of $1,000 equals $120,000. This is useful for comparison--showing how much is "just savings" vs compound growth. It is also the correct formula for modeling non-interest-bearing accounts.

---

### Example 11: Negative Future Value (Loan Payoff from Lender View)
```
=FV(0.06/12, 60, 500, -25000)
```
**Result:** `-$3,645.81`

**Explanation:** From a lender's perspective: they gave out $25,000 (negative pv) and receive $500/month payments (positive pmt). The negative FV indicates the loan is not fully paid off--$3,645.81 still owed after 60 months. This validates that the payment would not fully amortize the loan in 5 years.

---

### Example 12: Using Cell References for What-If Analysis
```
=FV(A1/12, A2*12, -A3, -A4, A5)
```
Where A1=0.08 (rate), A2=30 (years), A3=600 (monthly), A4=20000 (initial), A5=0 (type)

**Result:** `$994,024.56`

**Explanation:** Building FV with cell references enables interactive what-if analysis. Users can adjust any input and instantly see the future value change. This approach is essential for financial planning tools and retirement calculators.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Text values in parameters, or non-numeric inputs | Ensure all parameters are numbers. Check for hidden text formatting, spaces, or non-numeric characters. |
| `#NUM!` | Impossible calculation (e.g., rate of -100%) | Verify rate is greater than -1. A rate of -100% or less creates division by zero internally. |
| `Unexpectedly small result` | Rate entered as whole number instead of decimal | Use 0.08 for 8%, not 8. Alternatively, use 8% with the percent sign if your spreadsheet supports it. |
| `Wrong future value` | Rate and nper period mismatch | If contributions are monthly, rate must be monthly (annual/12) and nper must be in months (years*12). |
| `Negative FV when expecting positive` | Sign convention confusion | Remember: money you invest (pv, pmt) should be negative. If both inputs are positive, FV will be negative. |
| `Result differs from online calculator` | Type parameter or rounding differences | Check if the calculator uses beginning-of-period. Also verify compounding frequency matches your formula. |

## Use Cases

### [[Retirement Savings Projection]]

**Scenario:** A 30-year-old employee wants to project their 401(k) balance at age 65, including employer match, and determine if they are on track for a $1,000,000 goal.

**Implementation:**
```
Employee contribution: $500/month
Employer match (50% up to 6%): $250/month
Total monthly: $750
Current balance: $45,000

=FV(0.07/12, 420, -750, -45000)
```
**Result:** `$1,497,842.32`

**Business Application:** HR departments and financial advisors use FV projections to help employees understand their retirement trajectory. Showing concrete numbers motivates higher contribution rates and earlier enrollment. Companies can demonstrate the value of employer matching programs by showing match impact on final balances.

**Technical Details:** The 7% return assumption is a common long-term equity average; adjust for more conservative allocations. Real retirement planning must also consider inflation--this nominal FV should be adjusted by expected inflation (typically 2-3%) for purchasing power reality.

---

### [[Education Savings - 529 Plan Projections]]

**Scenario:** New parents want to save for their child's college education starting at birth, with a target of $150,000 by age 18.

**Implementation:**
```
To find required monthly contribution:
Target FV = $150,000
nper = 18 * 12 = 216 months
rate = 0.06 / 12 (6% annual return)

Use PMT to solve backward:
=PMT(0.06/12, 216, 0, 150000) = -$487.47/month

Verify with FV:
=FV(0.06/12, 216, -487.47) = $150,002.88
```

**Business Application:** Financial planners use FV to show parents the realistic savings requirements for education goals. Many parents underestimate college costs or overestimate how much their savings will grow. FV calculations provide a reality check and help establish appropriate savings rates early.

**Technical Details:** 529 plan returns vary by investment option. Use conservative estimates (4-5%) for shorter timeframes or when the child is closer to college age. Also factor in potential tuition inflation (historically 5-7% annually) when setting target amounts.

---

### [[Business Capital Accumulation]]

**Scenario:** A small business owner wants to build a $500,000 equipment replacement fund over 10 years by setting aside profits quarterly.

**Implementation:**
```
Target: $500,000 in 10 years
Assumed return: 4% (conservative, business savings)
Quarterly periods: 40

Required quarterly deposit:
=PMT(0.04/4, 40, 0, 500000) = -$10,271.62

With existing $50,000 seed fund:
=PMT(0.04/4, 40, -50000, 500000) = -$8,738.05

Current plan projection with $9,000/quarter deposits:
=FV(0.04/4, 40, -9000, -50000) = $510,098.09
```

**Business Application:** Business owners use FV for capital planning, ensuring adequate reserves for major purchases, expansions, or economic downturns. Regular projections help CFOs adjust savings rates as business conditions change.

**Technical Details:** Business savings often earn lower returns than personal investments due to liquidity needs. Use conservative rates (3-5%) for funds that must be available. Consider tax implications--business investment income may be taxed differently than personal accounts.

---

### [[Emergency Fund Growth Tracking]]

**Scenario:** An individual is building a 6-month emergency fund of $30,000 and wants to track projected completion date and final balance with continued savings.

**Implementation:**
```
Current emergency fund: $12,000
Monthly addition: $800
Target: $30,000
High-yield savings rate: 4.5%

Months until target (using NPER):
=NPER(0.045/12, -800, -12000, 30000) = 21.4 months

If continue saving for 36 months total:
=FV(0.045/12, 36, -800, -12000) = $42,714.65
```

**Business Application:** Personal finance apps and banking tools use FV to help customers visualize savings progress. Showing projected completion dates and "what if I keep going" scenarios encourages savings behavior. Banks use similar projections to market high-yield savings accounts.

**Technical Details:** Emergency funds should be in liquid accounts, limiting investment options. High-yield savings (4-5%), money market accounts, or short-term CDs are appropriate. FV at these modest rates still demonstrates value of consistent saving plus interest earnings versus pure cash stashing.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 97 through Excel 365 and beyond)
- **Specific Behavior:** Standard 5-parameter function. Negative pmt/pv for investments, positive result for future value.
- **Precision:** IEEE 754 double-precision floating point, accurate to 15 significant digits.

### Google Sheets
- **Availability:** All versions since launch
- **Specific Behavior:** Functionally identical to Excel. Same parameter order, defaults, and sign conventions.
- **Precision:** Same floating-point precision as Excel.

### Both Platforms
- Sign convention: Outflows (deposits, investments) are negative; inflows (future receipts) are positive
- Rate and nper must use matching time periods
- PV defaults to 0; Type defaults to 0
- Compounding is per-period (matches rate frequency)
- Use number formatting for currency display

## Tips and Best Practices

1. **Match your rate to your period:** For monthly contributions, divide annual rate by 12 and multiply years by 12. This is the most common error. Quarterly: divide by 4. Weekly: divide by 52. Mismatched periods produce wildly incorrect results.

2. **Use negative numbers for money you invest:** Deposits and initial investments should be negative (money leaving you). The positive FV result then correctly represents money coming back to you. This consistency prevents sign confusion in complex models.

3. **Compare with and without contributions:** Calculate FV with just the lump sum (pmt=0) and with just contributions (pv=0), then compare to the combined result. This shows the relative contribution of initial investment vs. ongoing savings to the final balance.

4. **Always run multiple scenarios:** Investment returns are uncertain. Calculate FV at conservative (4-5%), moderate (6-7%), and optimistic (8-10%) rates. If your plan only works at optimistic rates, you need to increase contributions or adjust expectations.

5. **Consider beginning-of-period contributions (type=1):** If you can contribute at the start of each month rather than the end, you gain extra compounding. Over 30 years, this can add tens of thousands of dollars with no additional contributions.

6. **Account for inflation in long-term projections:** A future value of $1,000,000 in 30 years has less purchasing power than today. Divide by (1+inflation_rate)^years for real (inflation-adjusted) value. At 3% inflation, $1M in 30 years equals about $412,000 in today's dollars.

7. **Use FV for goal-setting verification:** Once you calculate required contributions using PMT or NPER, verify with FV to confirm you reach your target. This cross-check catches input errors and builds confidence in your plan.

8. **Document your assumptions:** Future value projections are only as good as their assumptions. Always record what rate you used and why, as well as whether the rate is nominal or real (inflation-adjusted). This helps when revisiting projections years later.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[PV]] | Present value of future cash flows | When you know the future amount and want to find today's equivalent value |
| [[PMT]] | Payment per period | When you know the target FV and want to find required contributions |
| [[NPER]] | Number of periods | When you know target FV and contribution, want to find time required |
| [[RATE]] | Interest rate per period | When you know contributions, time, and target FV, want to find required return |
| [[FVSCHEDULE]] | FV with variable interest rates | When your investment earns different rates in different periods |

### Commonly Used Together

**[[PMT]]** - Required Contribution Calculator

*Combined with FV for goal-setting:*
```
Target future value: $500,000 in 25 years at 7%
Required monthly: =PMT(0.07/12, 300, 0, 500000) = -$625.86

Verify: =FV(0.07/12, 300, -625.86) = $500,000.09
```
Use PMT to find what you need to save, then FV to verify and explore what-if scenarios.

---

**[[PV]]** - Present Value Comparison

*Combined with FV for equivalence analysis:*
```
Future target: =FV(0.06/12, 240, -500) = $232,175.55
Present equivalent: =PV(0.06, 20, 0, -232175.55) = $72,410.09
```
Determine: is a $232K future value worth more than a $72K lump sum today? At 6% over 20 years, they are equivalent.

---

**[[NPV]]** - Net Present Value

*Combined with FV for investment comparison:*
```
Option A: Contribute $500/month for 20 years = FV of $232K
Option B: Invest $80,000 lump sum now
Which is better? =NPV(0.06/20, {-500 for 240 periods}) vs -80000

Or simpler: =PV(0.06/12, 240, -500) = $69,647
Since $69,647 < $80,000, the lump sum is better (at 6%)
```
NPV and PV help compare options with different timing patterns.

---

**[[IF]]** - Conditional Projections

*Combined with FV for scenario analysis:*
```
=IF(B1="Conservative", FV(0.05/12, 360, -500),
   IF(B1="Moderate", FV(0.07/12, 360, -500),
   FV(0.09/12, 360, -500)))
```
Allow users to select assumptions and see projections update dynamically.

---

**[[NPER]]** - Time to Goal

*Combined with FV for planning flexibility:*
```
How long to reach $100,000 saving $400/month at 6%?
=NPER(0.06/12, -400, 0, 100000) = 177.4 months (14.8 years)

What balance after exactly 15 years?
=FV(0.06/12, 180, -400) = $104,737.66
```
NPER finds time-to-goal; FV confirms or shows alternative endpoints.

## Official Documentation

- **Microsoft Excel:** [FV function](https://support.microsoft.com/en-us/office/fv-function-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3)
- **Google Sheets:** [FV function](https://support.google.com/docs/answer/3093224)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 97 (1997) | Original implementation with all 5 parameters |
| Excel 2007+ | All subsequent versions | No changes to function behavior |
| Google Sheets | Original launch | Identical to Excel implementation |

---

*Last updated: 2026-01-10*
