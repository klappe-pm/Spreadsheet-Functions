---
domain: Spreadsheet Functions
category: Financial
subcategory: Investment Returns
purpose:
  - Financial Modeling
  - Investment Analysis
use-case:
  - Capital Budget Screening
  - Discount Rate Sensitivity
  - Project Value Comparison
related:
  - IRR
  - MIRR
  - PV
  - XIRR
  - XNPV
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/npv-function
  - https://support.google.com/docs/answer/3093184
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Net Present Value
  - Present Value of Cash Flows
tags:
  - capital-budgeting
  - cash-flow
  - excel
  - sheets
---

# NPV

## Description

**NPV** returns the net present value of a series of future cash flows, discounted at a rate you choose. It answers the question "Is this investment worth more than it costs?" A positive result means the discounted cash flows exceed the cost at that rate, and a negative result means they fall short.

NPV discounts each cash flow back to today, so a dollar received later is worth less than a dollar received now. The function assumes the cash flows are equally spaced and occur at the end of each period, and that the first value is discounted by one full period. The initial investment happens today, so it is not part of the NPV function. Subtract it, or add it as a negative number, outside the function: `=NPV(rate, cash flows) + initial_cash_flow`.

Enter the rate per period, so an annual rate fits annual cash flows and a monthly rate fits monthly cash flows. For cash flows on irregular dates, use XNPV instead.

## Syntax

```excel
=NPV(rate, value1, [value2], ...)
```

<!-- Image 1: Discount Rate and Cash Flow Ranges. See Images/Financial/NPV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The discount rate per period, as a decimal such as 0.09 or a percentage such as 9%. |
| `value1` | Yes | The first cash flow, received at the end of period 1. Income is positive and payments are negative. |
| `value2, ...` | No | Later cash flows in period order. Excel accepts up to 254 value arguments, and each can be a single value or a range. |

### Return Value

A single number in the same currency as the cash flows. The result is the present value of the cash flows at the chosen rate, not the net gain after the initial cost.

## Examples

All examples use an initial cost of 12,000 entered as `-12000` in `B1`, and cash flows of 4,000, 5,000 and 6,000 in `B2` to `B4`.

### Example 1: Net Present Value at 9%

```excel
=NPV(0.09, B2:B4) + B1
```

**Result:** `511.23`

The three cash flows are worth 12,511.23 today at 9%, which is 511.23 more than the 12,000 cost.

### Example 2: Sensitivity to the Discount Rate

```excel
=NPV(0.06, B2:B4) + B1
```

**Result:** `1261.28` at 6%

```excel
=NPV(0.12, B2:B4) + B1
```

**Result:** `-171.92` at 12%

The same cash flows create value at 6% and destroy value at 12%, which shows how much the required return matters.

<!-- Image 2: Net Present Value at Three Discount Rates. See Images/Financial/NPV.md -->

### Example 3: Monthly Cash Flows With an Annual Rate

Where `C1` holds `-30000` and `C2` to `C25` each hold `1500`:

```excel
=NPV(0.12/12, C2:C25) + C1
```

**Result:** `1865.08`

The 12% annual rate becomes 1% a month, and the 24 monthly receipts are discounted at that monthly rate.

### Example 4: Negative Cash Flow in Year One

```excel
=NPV(0.10, -5000, 10000, 15000, 20000) - 25000
```

**Result:** `3649.00`

A loss of 5,000 in year one is discounted with the rest, and the 25,000 cost is subtracted outside the function.

### Example 5: Checking the IRR

```excel
=NPV(IRR(B1:B4), B2:B4) + B1
```

**Result:** `0.00`

At the IRR of 11.22%, the present value of the returns equals the cost, so the NPV is zero.

## Story Problems

### Problem 1: Packaging Line Upgrade at 9%

A food producer considers a packaging upgrade that costs 12,000 and returns the cash flows in the table below. Its required return is 9%.

| Year | Cash Flow |
| --- | --- |
| 0 | -12000 |
| 1 | 4000 |
| 2 | 5000 |
| 3 | 6000 |

**Task:** Calculate the NPV at 9% and state whether the upgrade creates value.

**Solution:**

```excel
=NPV(9%, B2:B4) + B1
```

**Answer:** `511.23`. The upgrade creates 511.23 of value at a 9% required return, so it is worth approving.

### Problem 2: The Same Upgrade at 12%

The finance team reruns Problem 1 with a 12% required return, because the upgrade carries more risk than expected.

| Year | Cash Flow |
| --- | --- |
| 0 | -12000 |
| 1 | 4000 |
| 2 | 5000 |
| 3 | 6000 |

**Task:** Calculate the NPV at 12% and state whether the upgrade still creates value.

**Solution:**

```excel
=NPV(12%, B2:B4) + B1
```

**Answer:** `-171.92`. At 12% the cash flows are worth less than the cost, so the upgrade does not meet the required return.

<!-- Image 3: NPV Results for the Upgrade Problems. See Images/Financial/NPV.md -->

## Use Cases

### Capital Budget Screening

**Scenario:** A manufacturer screens equipment proposals against its weighted average cost of capital each quarter.

```excel
=NPV(WACC, ReturnRange) + InitialCost
```

**Why It Works:** Entering the cost as a negative number and the expected returns as a range keeps each project's cash flows in one row. Projects with a positive NPV clear the cost of capital, and ranking them by NPV shows which adds the most value.

### Discount Rate Sensitivity

**Scenario:** A portfolio manager tests a project at several required returns before committing funds.

```excel
=NPV(RateCell, ReturnRange) + InitialCost
```

**Why It Works:** Filling a column of rates against the same formula shows the break-even rate, where the NPV crosses zero. A project that stays positive across a wide range of rates is less sensitive to the choice of discount rate.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Wrong result by one period of discounting | The initial cost was included as the first value of NPV. | Keep the initial cost outside NPV and add it with `+` or subtract it. |
| Result off by a large factor | An annual rate was used with monthly cash flows. | Divide the annual rate by 12 for monthly cash flows. |
| Result lower than expected | A blank or text cell was skipped, so a year is missing. | Enter 0 for periods with no cash flow and check the count of values. |
| Result too small or too large | Income and costs have the same sign. | Enter costs as negative numbers and income as positive numbers. |
| Too many arguments in Excel | More than 254 separate arguments were listed. | Put the cash flows in a range and pass the range as one argument. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Microsoft 365 and Excel for the web | Discounts the first value by one period. Accepts 1 to 254 value arguments. Non-numeric values are skipped. |
| Google Sheets | Available | Uses `discount` and `cashflow1, [cashflow2, ...]`. The page does not state the timing convention or the argument limit, so test the result on a known example before relying on it. |

## Tips and Best Practices

- Keep the initial cost outside the NPV function, and add it to the result so that the timing is correct.
- Match the rate to the cash flow period: annual rate for yearly flows and monthly rate for monthly flows.
- Enter costs as negative numbers and returns as positive numbers, and keep that convention across the sheet.
- Run the NPV at several rates to see how sensitive the decision is to the discount rate.
- Use the IRR at the same cash flows to confirm the break-even rate.
- Use XNPV when the cash flows fall on actual dates.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IRR](IRR.md) | The discount rate at which NPV equals zero. |
| [MIRR](MIRR.md) | Return with separate finance and reinvestment rates. |
| [XNPV](XNPV.md) | NPV for cash flows on irregular dates. |
| [XIRR](XIRR.md) | IRR for cash flows on irregular dates. |
| [PV](PV.md) | Present value of a level stream of payments, used when every payment is the same. |

## Official Documentation

- [Microsoft Support: NPV function](https://support.microsoft.com/en-us/excel/functions/npv-function)
- [Google Docs Editors Help: NPV](https://support.google.com/docs/answer/3093184)
