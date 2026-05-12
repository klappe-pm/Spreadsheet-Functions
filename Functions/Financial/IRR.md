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
- capital-budgeting
- return-calculation
- project-evaluation
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Internal Rate of Return
- Discount Rate
- Project Return Rate
tags:
- financial-modeling
- investment-analysis
- capital-budgeting
- roi
---

# IRR

## Description

**IRR (Internal Rate of Return)** calculates the discount rate at which the net present value (NPV) of a series of cash flows equals zero. In simpler terms, IRR tells you the "break-even" return rate of an investment--the annual percentage return the investment generates based on its cash flows. This is one of the most important metrics in capital budgeting because it lets you compare investment opportunities using a single, intuitive percentage figure: "This project returns 15% annually."

The mathematical concept behind IRR is elegant: given an initial investment (negative cash flow) followed by returns (positive cash flows), there exists a discount rate at which the present value of all returns exactly equals the initial investment. That rate is the IRR. If your required return (hurdle rate) is lower than the IRR, the investment creates value; if higher, it destroys value. An investment with a 20% IRR exceeds a 12% hurdle rate, so it should be accepted.

**Understanding sign conventions is absolutely critical for IRR:** The function requires at least one positive and one negative cash flow. The first cash flow (usually period 0) is typically negative--representing the initial investment (money leaving you). Subsequent cash flows are typically positive--representing returns (money coming back to you). If all cash flows have the same sign, IRR cannot be calculated because there is no break-even point. The order of values in the range represents the time sequence: first value is period 0, second is period 1, and so on.

IRR uses an iterative numerical method to find the solution, which has important implications. First, IRR may not converge to a solution for unusual cash flow patterns (multiple sign changes), returning #NUM!. Second, you can provide a "guess" parameter to help the iteration start near the expected answer. Third, IRR assumes all periods are equal length--for irregular timing, use XIRR instead. Both Excel and Google Sheets implement IRR identically.

## Syntax

> [!f(x)] IRR Syntax
>
> ```
> =IRR(values, [guess])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `values` | Yes | A range or array containing cash flows. Must include at least one positive and one negative value. Values are assumed to occur at regular intervals (monthly, annual, etc.) in sequential order. The first value is typically the initial investment (negative). |
| `guess` | No | An initial estimate of the IRR to help the iterative calculation converge. Enter as decimal (0.10 for 10%). Defaults to 0.1 (10%) if omitted. Useful when you expect an unusual IRR or the function returns #NUM!. |

### Return Value

Returns the internal rate of return per period as a decimal (e.g., 0.15 for 15%). The period matches your cash flow frequency--if cash flows are annual, IRR is annual; if monthly, IRR is monthly. For monthly IRR, annualize with: (1+IRR)^12 - 1.

## Examples

> [!f(x)] IRR Examples

### Example 1: Basic Project Investment
```
=IRR({-100000, 30000, 35000, 40000, 45000})
```
**Result:** `14.49%`

**Explanation:** An initial $100,000 investment generates cash flows of $30,000, $35,000, $40,000, and $45,000 over four years. The IRR of 14.49% means this investment yields approximately 14.5% annually. If your cost of capital is below 14.49%, this project adds value.

---

### Example 2: Using a Cell Range
```
=IRR(B2:B7)
```
Where B2=-50000, B3=10000, B4=15000, B5=18000, B6=20000, B7=12000

**Result:** `17.63%`

**Explanation:** IRR commonly uses cell ranges rather than arrays. The range must be in order: initial investment first (negative), followed by subsequent returns (positive). The 17.63% IRR indicates a strong return exceeding most hurdle rates.

---

### Example 3: Monthly Cash Flows (Annualizing)
```
Monthly IRR: =IRR(A1:A13) where A1=-24000, A2:A13=2200 each
Annual equivalent: =(1+IRR(A1:A13))^12 - 1
```
**Result:** Monthly IRR = `1.21%`, Annualized = `15.57%`

**Explanation:** For monthly cash flows, IRR returns a monthly rate. To compare with annual investments, annualize using the compound interest formula: (1+monthly_rate)^12 - 1. A monthly 1.21% equals an annual 15.57%.

---

### Example 4: Comparing Two Projects
```
Project A: =IRR({-200000, 50000, 60000, 70000, 80000, 90000}) = 16.37%
Project B: =IRR({-200000, 100000, 80000, 60000, 40000, 20000}) = 17.12%
```
**Result:** Project B has higher IRR

**Explanation:** Both projects cost $200,000 and return $350,000 total, but Project B has higher IRR because it returns more money earlier (time value). However, IRR alone should not determine the choice--consider NPV, project scale, and strategic fit.

---

### Example 5: Real Estate Investment
```
=IRR({-350000, 24000, 24000, 24000, 24000, 24000, 24000, 24000, 24000, 24000, 424000})
```
**Result:** `9.57%`

**Explanation:** Purchase a rental property for $350,000, receive $24,000 annual net rent for 9 years, then sell for $400,000 in year 10 (total year 10 cash flow = $24,000 rent + $400,000 sale = $424,000). The 9.57% annual return accounts for both rental income and appreciation.

---

### Example 6: Project with Losses in Early Years
```
=IRR({-500000, -100000, 50000, 150000, 250000, 300000, 350000})
```
**Result:** `12.58%`

**Explanation:** Initial $500,000 investment plus $100,000 additional funding in year 1 (both negative), then growing returns. IRR handles multiple negative cash flows--it finds the rate where NPV of all cash flows equals zero. The project eventually achieves 12.58% return despite early losses.

---

### Example 7: Using Guess Parameter for Unusual IRRs
```
=IRR({-1000, 4000, -4000, 1000}, 0.5)
```
**Result:** `50%` (or another valid solution)

**Explanation:** When cash flows change signs multiple times, there may be multiple valid IRRs. The guess parameter helps direct the function toward a particular solution. Without a guess, IRR might return #NUM! or an unexpected value. Always verify results with NPV when cash flows are irregular.

---

### Example 8: Negative IRR (Losing Investment)
```
=IRR({-100000, 20000, 25000, 15000, 10000})
```
**Result:** `-16.93%`

**Explanation:** The investment returns only $70,000 on a $100,000 investment over 4 years. The negative IRR indicates the investment loses money. At a -16.93% return, the investment destroys value at nearly 17% annually. Any negative IRR means you would have been better off not investing.

---

### Example 9: IRR Equals Zero (Break-Even)
```
=IRR({-100000, 25000, 25000, 25000, 25000})
```
**Result:** `0.00%`

**Explanation:** Total returns exactly equal the initial investment ($100,000 invested, $100,000 returned). IRR of 0% means the investment merely returned your principal with no gain--you would have done equally well leaving money in a 0% account. This is the break-even scenario.

---

### Example 10: Very High IRR (Caution!)
```
=IRR({-5000, 8000, 10000})
```
**Result:** `107.50%`

**Explanation:** A $5,000 investment that returns $18,000 over 2 years has an astronomical IRR. While mathematically correct, extremely high IRRs usually indicate either small investments, short timeframes, or data errors. High IRR on small investments may not compensate for time and risk.

---

### Example 11: #NUM! Error and How to Fix It
```
=IRR({100, 200, 300})       → #NUM! (all positive, no solution)
=IRR({-100, -200, -300})    → #NUM! (all negative, no solution)
=IRR({-100, 10, 10}, -0.5)  → May help find solution or confirm none exists
```
**Result:** Various error scenarios

**Explanation:** IRR requires at least one positive and one negative value. If cash flows all have the same sign, there is no discount rate that makes NPV equal zero. The #NUM! error also occurs if the iterative method does not converge--try different guess values or examine your cash flows for errors.

---

### Example 12: Relationship Between IRR and NPV
```
Cash flows: {-100000, 30000, 40000, 50000, 30000}
IRR: =IRR({-100000, 30000, 40000, 50000, 30000}) = 13.72%

Verify with NPV at IRR rate:
=NPV(0.1372, 30000, 40000, 50000, 30000) - 100000 = ~$0
```
**Result:** NPV equals zero at the IRR

**Explanation:** By definition, IRR is the rate where NPV = 0. This relationship is the best way to verify your IRR calculation. If NPV at the IRR is not close to zero, there may be an error in your cash flow data.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#NUM!` | All cash flows have the same sign (all positive or all negative) | IRR requires at least one positive and one negative value. Check that initial investment is negative and returns are positive. |
| `#NUM!` | Iterative calculation did not converge | Try a different guess value. If cash flows change signs multiple times, there may be multiple or no solutions. |
| `#VALUE!` | Text or non-numeric values in the cash flow range | Ensure all values are numbers. Check for hidden text, spaces, or error values in the range. |
| `Unexpectedly high/low IRR` | Period mismatch | If cash flows are monthly but you expected annual IRR, annualize: (1+IRR)^12 - 1. |
| `IRR seems wrong` | Cash flow order incorrect | First value should be the initial investment (negative). Subsequent values in time sequence. Verify the range starts at period 0. |
| `Different IRR than expected` | Non-standard cash flow pattern | Multiple sign changes can produce multiple IRRs. Consider MIRR or NPV for reinvestment rate clarity. |

## Use Cases

### [[Capital Budgeting - Project Selection]]

**Scenario:** A manufacturing company has a limited capital budget and must choose between three equipment upgrade projects, each requiring different investments and generating different returns over 5 years.

**Implementation:**
```
Project A: =IRR({-500000, 100000, 150000, 180000, 200000, 220000}) = 19.12%
Project B: =IRR({-300000, 80000, 90000, 100000, 110000, 120000}) = 21.47%
Project C: =IRR({-750000, 150000, 200000, 250000, 300000, 350000}) = 18.83%

Company hurdle rate: 12%
```

**Business Application:** All three projects exceed the 12% hurdle rate, meaning all create value. However, capital is limited to $800,000. Project B has the highest IRR, suggesting the most efficient use of capital. But choosing A+B ($800K) versus C ($750K) requires comparing combined value creation--NPV analysis complements IRR for this decision.

**Technical Details:** IRR is excellent for ranking efficiency but does not account for project scale. A small project with 25% IRR may create less total value than a large project with 18% IRR. Always calculate NPV alongside IRR for complete analysis. Also consider that IRR assumes reinvestment at the IRR rate--use MIRR if this assumption is unrealistic.

---

### [[Private Equity - Fund Performance]]

**Scenario:** A private equity investor needs to evaluate the performance of their investment over its life cycle--initial investment, capital calls, distributions, and final exit.

**Implementation:**
```
Year 0: -1,000,000 (initial investment)
Year 1: -500,000 (capital call)
Year 2: 200,000 (distribution)
Year 3: 300,000 (distribution)
Year 4: 400,000 (distribution)
Year 5: 2,500,000 (exit + final distribution)

=IRR({-1000000, -500000, 200000, 300000, 400000, 2500000})
```
**Result:** `24.87%` annual return

**Business Application:** Private equity firms report IRR as the primary performance metric because it accounts for the timing and size of cash flows. A 24.87% IRR significantly outperforms public markets, justifying the illiquidity and risk. Limited partners (investors) compare fund IRRs when deciding on future commitments.

**Technical Details:** PE cash flows are irregular, so technically XIRR (with dates) is more accurate. IRR here assumes annual periods. Also note that IRR can be gamed by timing cash flows--early distributions boost IRR even if total returns are modest. Consider also measuring total value to paid-in capital (TVPI) alongside IRR.

---

### [[Lease vs. Buy Analysis]]

**Scenario:** A company can purchase equipment for $100,000 or lease it for $2,500/month for 48 months. After the lease, the company has no ownership. If purchased, the equipment has $20,000 salvage value after 4 years.

**Implementation:**
```
Purchase scenario (monthly cash flows):
Month 0: -100,000 (purchase)
Months 1-47: 0 (no cash flow, you own it)
Month 48: 20,000 (salvage value)

Effective monthly cost of ownership: =PMT(0.08/12, 48, 100000, -20000) = -$2,012.12

Lease: $2,500/month

Comparison: Lease costs $487.88 more per month
Implicit lease rate: Find rate where $2,500 payment on $100,000 with $0 residual
=RATE(48, -2500, 100000, 0) * 12 = 12.68% annual
```

**Business Application:** The lease embeds a 12.68% financing rate, higher than the 8% assumed borrowing cost for purchase. If the company can borrow at less than 12.68%, purchasing is financially superior (assuming they can use the equipment for its full life). IRR/RATE helps reveal the implicit financing cost in lease agreements.

**Technical Details:** Leasing may still be preferred for non-financial reasons: flexibility, off-balance-sheet treatment (historically), maintenance inclusion, or technology obsolescence concerns. The analysis should include tax implications--depreciation shields for purchase vs. expense deduction for lease payments.

---

### [[Startup Investment - Venture Returns]]

**Scenario:** A venture capital firm invested $2 million in a startup. After additional funding rounds and eventual acquisition, they want to calculate their return.

**Implementation:**
```
Year 0: -2,000,000 (initial investment)
Year 2: -500,000 (follow-on investment, pro-rata)
Year 5: 15,000,000 (acquisition proceeds)

=IRR({-2000000, 0, -500000, 0, 0, 15000000})
```
**Result:** `41.73%` annual return

**Business Application:** A 41.73% IRR over 5 years represents an excellent venture investment--roughly 6x return on invested capital. VCs target 25%+ IRR to compensate for the high failure rate of startups. This calculation helps VCs evaluate individual investments and overall portfolio performance.

**Technical Details:** Venture returns are highly variable. The zero values for years 1, 3, and 4 indicate no cash flow--the investment was held. In practice, XIRR with actual dates is more accurate. Also, this does not account for fund-level expenses, carried interest, or the opportunity cost of capital tied up for 5 years.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 97 through Excel 365 and beyond)
- **Specific Behavior:** Uses Newton-Raphson or similar iteration. Maximum 20 iterations by default. Guess defaults to 10%.
- **Precision:** Continues until result is accurate to within 0.00001% (10^-7).

### Google Sheets
- **Availability:** All versions since launch
- **Specific Behavior:** Functionally identical to Excel. Same iterative approach and default guess.
- **Precision:** Same accuracy threshold as Excel.

### Both Platforms
- Requires at least one positive and one negative value
- Returns #NUM! if no solution exists or iteration does not converge
- Assumes equal periods between cash flows
- Returns rate per period (must annualize if periods are not annual)
- For irregular timing, use XIRR instead

## Tips and Best Practices

1. **First cash flow should be negative (investment out):** The standard IRR pattern is: negative initial investment, followed by positive returns. Reversing this still works but changes the interpretation--you would be calculating a borrowing cost rather than investment return.

2. **Match your cash flow period to your rate interpretation:** If cash flows are monthly, IRR returns a monthly rate. Annualize with (1+IRR)^12 - 1. If cash flows are quarterly, multiply appropriately. Misinterpreting the period leads to severely wrong conclusions.

3. **Use XIRR for irregular cash flow dates:** When cash flows do not occur at regular intervals (e.g., actual investment dates), XIRR provides more accurate results. XIRR also handles partial years correctly.

4. **Watch for multiple IRRs with unconventional cash flows:** When cash flows change from positive to negative multiple times (e.g., project with cleanup costs at the end), there may be multiple valid IRRs. In these cases, NPV at your hurdle rate is more reliable.

5. **Compare IRR to your hurdle rate:** IRR alone is not a decision--compare it to your required return (cost of capital, hurdle rate). Accept projects where IRR exceeds the hurdle rate; reject those where it falls short.

6. **Do not use IRR alone for mutually exclusive projects:** A smaller project may have higher IRR but create less total value than a larger project with lower IRR. Always calculate NPV to compare absolute value creation.

7. **Be skeptical of extremely high IRRs:** Very high IRRs often indicate small investments, short timeframes, or data errors. A 500% IRR on $1,000 over 3 months is less valuable than 20% IRR on $1,000,000 over 5 years. Scale matters.

8. **Use the guess parameter when you get #NUM!:** If IRR returns an error, try providing a guess close to your expected return. This helps the iteration converge. If no guess works, the cash flow pattern may truly have no solution--verify your data.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[XIRR]] | IRR with specific dates for each cash flow | When cash flows occur at irregular intervals, not evenly spaced |
| [[MIRR]] | Modified IRR with separate reinvestment rate | When you want to specify a realistic reinvestment rate rather than assuming reinvestment at IRR |
| [[NPV]] | Net present value at a specified rate | When you want to test value creation at your cost of capital rather than find the break-even rate |
| [[RATE]] | Interest rate for an annuity | When cash flows are equal (annuity payments) and you want the rate |

### Commonly Used Together

**[[NPV]]** - Net Present Value

*Combined with IRR for complete investment analysis:*
```
Cash flows: {-100000, 25000, 30000, 35000, 40000, 45000}
IRR: =IRR(above) = 15.42%
NPV at 10% hurdle: =NPV(0.10, 25000, 30000, 35000, 40000, 45000) - 100000 = $22,489

Decision: IRR (15.42%) > Hurdle (10%), so NPV is positive. Accept project.
```
IRR tells you the return rate; NPV tells you the dollar value created. Both should agree on accept/reject decisions.

---

**[[XIRR]]** - IRR with Dates

*For real-world cash flows with actual dates:*
```
Values: {-100000, 25000, 30000, 45000, 60000}
Dates: {1/1/2024, 4/15/2024, 10/1/2024, 6/30/2025, 12/31/2025}

=XIRR(values, dates) = 19.85% (more accurate than regular IRR)
```
XIRR handles partial years and irregular timing that IRR cannot.

---

**[[MIRR]]** - Modified Internal Rate of Return

*When reinvestment rate differs from IRR:*
```
Cash flows: {-100000, 30000, 40000, 50000, 60000}
IRR: =IRR(above) = 20.97%
MIRR (at 5% reinvestment, 10% finance): =MIRR(above, 0.10, 0.05) = 15.73%
```
MIRR is more realistic because it does not assume you can reinvest returns at the high IRR.

---

**[[PV]]** - Present Value

*Understanding the IRR relationship:*
```
At the IRR, PV of returns equals initial investment:
=PV(IRR_rate, nper, average_return) ≈ Initial_Investment
```
This mathematical relationship is the foundation of IRR--it is the rate where present value of inflows equals outflow.

---

**[[IF]]** - Investment Decision Automation

*Combined with IRR for automated recommendations:*
```
=IF(IRR(B2:B10) > C1, "ACCEPT - Exceeds hurdle rate", "REJECT - Below hurdle rate")
```
Where C1 contains the company's hurdle rate. Automates investment screening.

## Official Documentation

- **Microsoft Excel:** [IRR function](https://support.microsoft.com/en-us/office/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc)
- **Google Sheets:** [IRR function](https://support.google.com/docs/answer/3093233)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 97 (1997) | Original implementation with iterative method |
| Excel 2007+ | All subsequent versions | No changes to function behavior |
| Google Sheets | Original launch | Identical to Excel implementation |

---

*Last updated: 2026-01-10*
