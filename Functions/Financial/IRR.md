---
domain: Spreadsheet Functions
category: Financial
subcategory: Investment Returns
purpose:
  - Financial Modeling
  - Investment Analysis
use-case:
  - Capital Budget Screening
  - Project Return Comparison
  - Startup Cash Flow Review
related:
  - MIRR
  - NPV
  - RATE
  - XIRR
  - XNPV
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/irr-function
  - https://support.google.com/docs/answer/3093231
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Internal Rate of Return
  - Project Return Rate
tags:
  - capital-budgeting
  - cash-flow
  - excel
  - sheets
---

# IRR

## Description

**IRR** returns the internal rate of return for a series of cash flows: the discount rate at which the net present value of those cash flows equals zero. Compare the result with a required return, such as a hurdle rate or cost of capital. If the IRR is higher than the hurdle rate, the investment clears the bar; if it is lower, it does not.

The cash flows must occur at regular intervals, such as yearly or monthly, and must be listed in time order. The first value is usually the investment, entered as a negative number, followed by income as positive numbers. The result is a rate per period, so a list of monthly cash flows returns a monthly rate that must be annualized before comparing it with an annual hurdle.

Use XIRR when cash flows fall on irregular dates. IRR cannot rank projects of different sizes on its own, because a small project can show a high IRR and still add less value than a large one. Check the NPV at the same rate before deciding.

## Syntax

```excel
=IRR(values, [guess])
```

<!-- Image 1: Cash Flow Range With Sign Convention. See Images/Financial/IRR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `values` | Yes | An array or range of cash flows in time order. It must contain at least one positive and one negative value. Text, logical values and blank cells are ignored. |
| `guess` | No | Your estimate of the result, entered as a decimal. The default is 0.1 (10%). Use it when the result is `#NUM!` or looks wrong. |

### Return Value

A decimal rate per period, such as `0.1098` for 10.98%. The rate matches the period of the cash flows: yearly flows return a yearly rate and monthly flows return a monthly rate. Excel returns `#NUM!` when no acceptable result is found after 20 tries.

## Examples

### Example 1: Basic Project Return

```excel
=IRR(B2:B6)
```

Where `B2` to `B6` hold `-50000`, `12000`, `15000`, `18000` and `21000`.

**Result:** `10.98%`

The 50,000 investment returns its cost plus a 10.98% annual return over five years.

### Example 2: Adding a Sixth Year

```excel
=IRR(B2:B7)
```

Where `B7` adds a final cash flow of `25000` to the list in Example 1.

**Result:** `20.80%`

The extra year of income raises the return sharply, which shows how sensitive IRR is to the final cash flows.

### Example 3: Supplying a Guess

```excel
=IRR(B2:B6, 0.15)
```

**Result:** `10.98%`

With one sign change in the cash flows there is only one IRR, so a different starting guess changes how quickly the function converges but not the answer.

### Example 4: Monthly Cash Flows, Annualized

Where `D2` holds `-24000` and `D3` to `D14` each hold `2200`:

```excel
=IRR(D2:D14)
```

**Result:** `1.50%` per month. Annualized with `=(1+IRR(D2:D14))^12-1`, the result is `19.53%`.

Monthly IRR must be annualized before it is compared with an annual hurdle rate.

### Example 5: A Negative Return

```excel
=IRR({-100000, 20000, 25000, 15000, 10000})
```

**Result:** `-14.39%`

The investment returns 70,000 on 100,000 over four years, so the rate is negative.

### Example 6: No Solution

```excel
=IRR({100, 200, 300})
```

**Result:** `#NUM!`

Every cash flow is positive, so no discount rate makes the net present value equal zero.

<!-- Image 2: Discounting Cash Flows to Zero. See Images/Financial/IRR.md -->

## Story Problems

### Problem 1: Equipment Upgrade Hurdle Test

A bakery considers a 50,000 oven upgrade. The expected net cash flows are in the table below, and the owners require an 8% return.

| Year | Cash Flow |
| --- | --- |
| 0 | -50000 |
| 1 | 12000 |
| 2 | 15000 |
| 3 | 18000 |
| 4 | 21000 |

**Task:** Find the annual IRR and state whether it clears the 8% hurdle.

**Solution:**

```excel
=IRR(B2:B6)
```

**Answer:** `10.98%`. It is above the 8% hurdle, so the upgrade passes this test. The NPV at 8% is 3,695.80, which confirms the project adds value.

### Problem 2: Vending Machine Monthly Return

A vending machine costs 24,000 and earns 2,200 net each month for a year. The owner wants the annual return.

| Month | Cash Flow |
| --- | --- |
| 0 | -24000 |
| 1 to 12 | 2200 each |

**Task:** Find the monthly IRR and convert it to an annual rate.

**Solution:**

```excel
=(1+IRR(D2:D14))^12-1
```

Here `D2` holds the month 0 value and `D3` to `D14` hold the twelve monthly values.

**Answer:** `19.53%` annual, from a monthly IRR of 1.50%.

<!-- Image 3: Results for the Return Problems. See Images/Financial/IRR.md -->

## Use Cases

### Capital Budget Screening

**Scenario:** A manufacturer screens equipment proposals against a 12% hurdle rate each quarter.

```excel
=IF(IRR(B2:B6) > HurdleRate, "Accept", "Reject")
```

**Why It Works:** The formula compares each project's IRR with the same hurdle rate. Pair it with NPV for the final decision, because IRR does not show the dollar value a project adds.

### Project Return Comparison

**Scenario:** A team compares two projects with the same cost but different timing of returns.

```excel
=IRR(ProjectA) - IRR(ProjectB)
```

**Why It Works:** The difference shows which project returns more per dollar invested. Projects of different sizes need NPV as well, because the higher IRR may come from a smaller investment.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | All cash flows have the same sign. | Enter the investment as a negative value and the returns as positive values. |
| `#NUM!` | The calculation did not converge in 20 tries. | Enter a different `guess`, such as a value near the expected return. |
| Wrong rate | A period is blank, so the blank is skipped and later flows move up one period. | Enter `0` for periods with no cash flow. |
| Rate looks too large or small | Monthly flows were read as an annual rate. | Annualize the result with `(1+IRR)^12-1`. |
| Several possible answers | The cash flows change sign more than once. | Compare NPV at your hurdle rate instead of relying on IRR alone. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Microsoft 365 and Excel for the web | Default guess is 0.1. Returns `#NUM!` after 20 tries. Stops when the result is accurate to 0.00001%. |
| Google Sheets | Available | Same argument order and default guess of 0.1. The page does not describe the iteration limit or the error values. |

## Tips and Best Practices

- Enter the initial investment as a negative value and every later cash flow as a positive value.
- Enter a 0 for any period with no cash flow so that the timing stays correct.
- Compare IRR with a hurdle rate, and check the NPV at that rate before approving a project.
- Use XIRR when the cash flows fall on actual dates instead of regular intervals.
- Use MIRR when the reinvestment rate for interim cash flows is known and differs from the IRR.
- Test the result by discounting the cash flows at the IRR: the NPV should be close to zero.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NPV](NPV.md) | Dollar value of the cash flows at a chosen rate. |
| [MIRR](MIRR.md) | IRR with separate finance and reinvestment rates. |
| [XIRR](XIRR.md) | IRR for cash flows on irregular dates. |
| [XNPV](XNPV.md) | NPV for cash flows on irregular dates. |
| [RATE](RATE.md) | Rate for a level annuity, rather than for irregular cash flows. |

## Official Documentation

- [Microsoft Support: IRR function](https://support.microsoft.com/en-us/excel/functions/irr-function)
- [Google Docs Editors Help: IRR](https://support.google.com/docs/answer/3093231)
