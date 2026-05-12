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
- capital-budgeting
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Net Present Value
- Present Value of Cash Flows
tags:
- financial-modeling
- investment-analysis
- dcf
---

# NPV

## Description

**NPV (Net Present Value)** calculates the present value of a series of future cash flows, discounted at a specified rate, minus the initial investment. This is one of the most fundamental functions in financial analysis because it answers a critical question: "Is this investment worth more than it costs?" A positive NPV means the investment is expected to generate more value than it costs (good investment), while a negative NPV means you'd be better off putting your money elsewhere.

The core concept behind NPV is the **time value of money**—the principle that a dollar today is worth more than a dollar tomorrow. If someone offers you $1,000 today or $1,000 in five years, you should take it today. Why? Because you could invest that $1,000 now and have more than $1,000 in five years. NPV uses a discount rate (typically your required rate of return or cost of capital) to convert all future cash flows into their equivalent present-day values, making them directly comparable.

**Critical distinction from PV:** The NPV function assumes cash flows occur at the **end** of each period and start from period 1, not period 0. This means your initial investment (which happens at time 0) is NOT included in the NPV calculation—you must subtract it separately. This trips up many users: `=NPV(rate, cash_flows) - initial_investment` is the correct formula, NOT `=NPV(rate, initial_investment, cash_flows)`. If you include your initial investment as the first cash flow, NPV will incorrectly discount it by one period.

NPV was available in the earliest versions of both Excel and Google Sheets. The function works identically across platforms, but be aware that the NPV function uses a simplified approach that assumes all cash flows occur at regular intervals. For irregular cash flows (payments on specific dates), use XNPV instead.

## Syntax

> [!f(x)] NPV Syntax
>
> ```
> =NPV(rate, value1, [value2], [value3], ...)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `rate` | Yes | The discount rate per period. Must match the period of your cash flows—if cash flows are annual, use annual rate; if monthly, use monthly rate. Enter as decimal (0.10 for 10%) or percentage (10%). |
| `value1` | Yes | First cash flow occurring at the end of period 1. Use positive numbers for inflows (revenue) and negative numbers for outflows (costs). |
| `value2, value3, ...` | No | Additional cash flows for periods 2, 3, etc. Up to 254 arguments in Excel, unlimited in Google Sheets. Can be individual values or ranges. |

### Return Value

Returns a single numeric value representing the net present value of all cash flows discounted at the specified rate. The result is in the same currency/unit as your input cash flows.

## Examples

> [!f(x)] NPV Examples

### Example 1: Basic Investment Analysis
```
=NPV(0.10, 3000, 4200, 6800)
```
**Result:** `$11,329.41`

**Explanation:** This calculates the present value of receiving $3,000 at end of year 1, $4,200 at end of year 2, and $6,800 at end of year 3, using a 10% annual discount rate. If the initial investment was $10,000, this investment creates $1,329.41 in value (NPV minus initial investment = $11,329.41 - $10,000 = $1,329.41 net value).

---

### Example 2: Complete Investment Decision with Initial Outlay
```
=NPV(0.08, B2:B6) - B1
```
Where B1 = -50000 (initial investment), B2:B6 = 15000, 15000, 15000, 15000, 15000 (annual returns)

**Result:** `$9,908.82`

**Explanation:** This is the correct way to calculate NPV for a typical investment. The initial $50,000 investment at time 0 is subtracted separately (not included in the NPV function), while the five annual $15,000 cash flows are discounted at 8%. The positive result indicates this investment creates nearly $10,000 in value above the required 8% return.

---

### Example 3: Project Comparison
```
Project A: =NPV(0.12, 20000, 25000, 30000, 35000) - 80000
Project B: =NPV(0.12, 50000, 30000, 20000, 10000) - 80000
```
**Result A:** `$5,040.32`
**Result B:** `$8,627.19`

**Explanation:** Both projects require $80,000 initial investment with 12% cost of capital. Project B has higher NPV despite lower total cash flows ($110,000 vs $110,000) because more money comes in earlier. This demonstrates why NPV is superior to simply adding up returns—it accounts for timing.

---

### Example 4: Monthly Cash Flows with Annual Rate
```
=NPV(0.12/12, C2:C25) - C1
```
**Result:** Depends on data

**Explanation:** When dealing with monthly cash flows but you have an annual discount rate, divide the rate by 12. This formula evaluates 24 months of cash flows (C2:C25) with a 12% annual rate converted to 1% monthly. The initial investment in C1 is subtracted at the end.

---

### Example 5: Handling Negative Cash Flows (Losses)
```
=NPV(0.10, -5000, 10000, 15000, 20000) - 25000
```
**Result:** `$5,471.43`

**Explanation:** NPV handles negative cash flows naturally. Here, year 1 shows a $5,000 loss (perhaps additional investment or operating loss), followed by positive returns. Initial investment of $25,000 is subtracted. Despite the year 1 loss, the project still creates value.

---

### Example 6: Comparing Different Discount Rates (Sensitivity Analysis)
```
=NPV(0.05, $B$2:$B$6) - $B$1   → Low risk scenario
=NPV(0.10, $B$2:$B$6) - $B$1   → Base case
=NPV(0.15, $B$2:$B$6) - $B$1   → High risk scenario
```
**Result:** Different NPVs showing sensitivity

**Explanation:** Running NPV at multiple discount rates shows how sensitive your investment decision is to changes in required return. Higher discount rates always produce lower NPVs because future cash flows are worth less today. If NPV stays positive even at high rates, the investment is robust.

---

### Example 7: Find Break-Even Discount Rate (IRR Connection)
```
Step 1: =NPV(0.15, B2:B10) - B1  → Check if positive or negative
Step 2: Adjust rate until NPV ≈ 0
Or use: =IRR(B1:B10)
```
**Result:** The rate where NPV = 0 is the IRR

**Explanation:** The discount rate that makes NPV equal to zero is the Internal Rate of Return (IRR). If your required return is less than the IRR, the project adds value. This connection between NPV and IRR is fundamental to investment analysis.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Text values in cash flow range, or non-numeric rate | Ensure all cash flows are numbers. Check for hidden text, spaces, or formatted-as-text numbers. |
| `#NUM!` | Rate equals -1 (dividing by zero internally) | Rate of -100% is mathematically invalid. Use realistic discount rates. |
| `#DIV/0!` | Rare, but can occur with malformed inputs | Check all parameters are valid numbers. |
| Incorrect result | Including initial investment in NPV function | Subtract initial investment separately: `=NPV(rate, cash_flows) - initial_investment` |
| Wrong magnitude | Using annual rate with monthly cash flows | Match rate period to cash flow period. Divide annual rate by 12 for monthly flows. |

## Use Cases

### [[Capital Budgeting: Equipment Purchase Decision]]

**Scenario:** A manufacturing company needs to decide whether to purchase a $500,000 CNC machine that will generate cost savings over 7 years.

**Implementation:**
```
=NPV(0.10, C2:C8) - 500000
```
Where C2:C8 contains annual savings: 80000, 95000, 110000, 115000, 120000, 125000, 130000

**Business Application:** Capital budgeting decisions require comparing the cost of equipment against future benefits. NPV provides a single number that tells management whether the investment clears their 10% hurdle rate. Finance teams use this to prioritize limited capital across multiple project proposals.

**Technical Details:** Include all relevant cash flows: savings, maintenance costs, residual/salvage value at end of life. Discount rate should reflect company's weighted average cost of capital (WACC) or project-specific risk-adjusted rate.

---

### [[Real Estate Investment Analysis]]

**Scenario:** An investor is evaluating a rental property priced at $300,000 with expected annual net rental income over 10 years, plus estimated sale price.

**Implementation:**
```
=NPV(0.08, D2:D10, D11) - 300000
```
Where D2:D10 = annual rental income ($24,000-$30,000 growing), D11 = sale price ($400,000)

**Business Application:** Real estate investors use NPV to compare properties with different price points, income profiles, and appreciation potential. A property with higher purchase price might have better NPV due to superior cash flows or appreciation—NPV captures this holistically.

**Technical Details:** Use net cash flows (rental income minus expenses, taxes, vacancy allowance). The discount rate should reflect the investor's required return accounting for real estate's illiquidity and risk. Consider using XNPV if cash flows occur on irregular dates.

---

### [[Startup Valuation with Negative Early Cash Flows]]

**Scenario:** A venture capitalist is valuing a startup that will burn cash for 3 years before becoming profitable.

**Implementation:**
```
=NPV(0.25, -200000, -150000, -50000, 100000, 300000, 500000, 750000) - 1000000
```
Initial investment: $1M. Years 1-3: losses. Years 4-7: growing profits.

**Business Application:** Startups typically have J-curve cash flow patterns—losses early, profits later. NPV properly accounts for both the early cash burn and delayed profitability. High discount rates (25%+) reflect startup risk.

**Technical Details:** For startups, include realistic growth assumptions and failure probability. Some analysts calculate NPV under multiple scenarios (success, moderate success, failure) and weight by probability.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 97 through Excel 365 and beyond)
- **Specific Behavior:** Accepts up to 254 value arguments. Works identically whether values are individual cells, ranges, or mixed.

### Google Sheets
- **Availability:** All versions since launch
- **Specific Behavior:** Functionally identical to Excel. No argument limit restrictions for practical purposes.

### Both Platforms
- Cash flows are assumed to occur at the END of each period (period 1 = end of period 1)
- Initial investment at time 0 must be handled separately (subtract from result)
- For cash flows on specific dates, use XNPV instead

## Tips and Best Practices

1. **Always subtract initial investment separately:** The most common NPV mistake is including the initial investment as the first cash flow. Remember: NPV function only handles period 1 onward.

2. **Match your rate to your cash flow periods:** Annual cash flows require annual rate. Monthly cash flows require monthly rate (annual ÷ 12). Mismatched periods give wildly wrong answers.

3. **Include all relevant cash flows:** Beyond obvious revenue, include working capital requirements, tax effects, maintenance costs, salvage value, and opportunity costs.

4. **Use consistent signs:** Positive = cash inflow (money received), Negative = cash outflow (money paid). Mixing conventions creates confusing results.

5. **Document your discount rate assumption:** Your NPV is only as good as your discount rate. Use WACC for corporate projects, required return for personal investments, or risk-adjusted rates for uncertain projects.

6. **Perform sensitivity analysis:** Calculate NPV at multiple discount rates to understand how sensitive your decision is to rate assumptions.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[XNPV]] | NPV with specific dates for each cash flow | When cash flows occur at irregular intervals (not evenly spaced periods) |
| [[PV]] | Present value of a single future amount or annuity | When you have equal, regular payments (like a loan or lease) |
| [[IRR]] | Finds the discount rate where NPV equals zero | When you want to find the break-even rate rather than test a specific rate |
| [[XIRR]] | IRR with specific dates for each cash flow | When you need IRR but cash flows are irregular |

### Commonly Used Together

**[[IRR]]** - Internal Rate of Return

*Combined with NPV for comprehensive investment analysis:*
```
NPV at required rate: =NPV(0.10, B2:B10) - B1
Project's IRR: =IRR(B1:B10)
Decision: If IRR > required rate, NPV will be positive
```
These two functions validate each other. If your NPV at 10% is positive, your IRR must be greater than 10%.

---

**[[IF]]** - Conditional Logic

*Combined with NPV for investment decision automation:*
```
=IF(NPV(0.10, B2:B10) - B1 > 0, "INVEST", "REJECT")
```
Automatically flag investment recommendations based on NPV thresholds.

---

**[[MAX]]** - Maximum Value

*Combined with NPV for project selection:*
```
=MAX(NPV(0.10, Project_A_CashFlows) - A1, NPV(0.10, Project_B_CashFlows) - B1, NPV(0.10, Project_C_CashFlows) - C1)
```
When choosing between mutually exclusive projects, select the one with highest NPV.

---

**[[XNPV]]** - NPV with Dates

*When cash flows have irregular timing:*
```
=XNPV(0.10, B2:B15, A2:A15)
```
If your cash flows don't occur at regular intervals, XNPV allows you to specify exact dates for accurate discounting.

## Official Documentation

- **Microsoft Excel:** [NPV function](https://support.microsoft.com/en-us/office/npv-function-8672cb67-2576-4d07-b67b-ac28acf2a568)
- **Google Sheets:** [NPV function](https://support.google.com/docs/answer/3093184)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 97 (1997) | Original implementation |
| Excel 2007+ | All subsequent versions | No changes to function behavior |
| Google Sheets | Original launch | Identical to Excel implementation |

---

*Last updated: 2026-01-10*
