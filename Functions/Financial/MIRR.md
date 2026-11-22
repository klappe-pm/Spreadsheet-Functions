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
  - Reinvestment Rate Review
related:
  - FV
  - IRR
  - NPV
  - PV
  - XIRR
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/mirr-function
  - https://support.google.com/docs/answer/3093180
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Blended Project Return
  - Modified Internal Rate of Return
tags:
  - capital-budgeting
  - excel
  - reinvestment
  - sheets
---

# MIRR

## Description

**MIRR** returns the modified internal rate of return for a series of cash flows. Unlike IRR, which assumes that every cash flow is reinvested at the IRR itself, MIRR uses two separate rates: a finance rate for the money the business pays out, and a reinvestment rate for the money it receives and sets aside. That makes the result easier to defend when the reinvestment rate is known and differs from the project's IRR.

Enter the outflows as negative numbers and the inflows as positive numbers, in time order. The list must contain at least one negative and one positive value. MIRR assumes the cash flows occur at regular intervals, so use XIRR for irregular dates.

Use the finance rate for the cost of borrowing and the reinvestment rate for the return on cash held between periods. Both rates are entered as decimals, such as 0.09 for 9%.

## Syntax

```excel
=MIRR(values, finance_rate, reinvest_rate)
```

<!-- Image 1: Cash Flow Range and Two Rates. See Images/Financial/MIRR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `values` | Yes | An array or range of cash flows in time order. Negative values are payments and positive values are income. Text and blank cells are ignored, but zeros are included. |
| `finance_rate` | Yes | The interest rate paid on money used to fund the negative cash flows. |
| `reinvest_rate` | Yes | The rate earned when positive cash flows are reinvested until the end of the project. |

### Return Value

A decimal rate per period, such as `0.1333` for 13.33%. The function returns `#DIV/0!` in Excel when the values do not include at least one positive and one negative number.

## Examples

### Example 1: Standard Project

Cash flows in `B2` to `B6` are `-80000`, `25000`, `30000`, `35000` and `20000`.

```excel
=MIRR(B2:B6, 0.09, 0.12)
```

**Result:** `13.33%`

The outflow is financed at 9% and the inflows are reinvested at 12%, which gives a modified return of 13.33%.

### Example 2: Lower Reinvestment Rate

```excel
=MIRR(B2:B6, 0.09, 0.06)
```

**Result:** `10.80%`

Reinvesting the same inflows at 6% lowers the result, which shows how much the reinvestment assumption matters.

<!-- Image 2: Effect of the Reinvestment Rate. See Images/Financial/MIRR.md -->

### Example 3: Inline Array

```excel
=MIRR({-40000, 15000, 18000, 12000}, 0.08, 0.10)
```

**Result:** `7.69%`

A three-year project financed at 8% and reinvested at 10% returns 7.69% a year.

### Example 4: Catching a Missing Outflow

```excel
=IFERROR(MIRR({10000, 5000, 8000}, 0.08, 0.10), "Add a negative cash flow")
```

**Result:** `Add a negative cash flow`

Every value is positive, so the function returns `#DIV/0!` and `IFERROR` shows a message instead.

## Story Problems

### Problem 1: Bakery Oven Project

A bakery spends 80,000 on a new oven. The expected net cash flows for the next four years are in the table below. The owner borrows at 9% and expects to reinvest the returns at 12%.

| Year | Cash Flow |
| --- | --- |
| 0 | -80000 |
| 1 | 25000 |
| 2 | 30000 |
| 3 | 35000 |
| 4 | 20000 |

**Task:** Calculate the modified IRR, with the finance rate in `E2` (0.09) and the reinvestment rate in `E3` (0.12).

**Solution:**

```excel
=MIRR(B2:B6, E2, E3)
```

**Answer:** `13.33%`, the modified rate of return on the oven project.

### Problem 2: Comparing With the Plain IRR

The same oven project is evaluated with the standard IRR, which assumes reinvestment at the IRR itself.

| Item | Value |
| --- | --- |
| Cash flows | The same values as Problem 1 |

**Task:** Calculate the plain IRR and explain why it is higher than the MIRR.

**Solution:**

```excel
=IRR(B2:B6)
```

**Answer:** `14.29%`. The MIRR is lower because the 12% reinvestment rate is below the 14.29% IRR, so the inflows are not assumed to earn the full IRR.

<!-- Image 3: Comparison of MIRR and IRR for the Oven Project. See Images/Financial/MIRR.md -->

## Use Cases

### Capital Budget Screening

**Scenario:** A company with a known borrowing cost and a known reinvestment rate screens several projects each year.

```excel
=IF(MIRR(B2:B6, FinanceRate, ReinvestRate) > HurdleRate, "Accept", "Reject")
```

**Why It Works:** The named rates keep the assumptions visible, so finance can change the rates for a scenario without editing every project formula.

### Reinvestment Rate Review

**Scenario:** A planner tests how a project's return changes if cash can only be reinvested at a lower rate.

```excel
=MIRR(CashFlows, 9%, ReinvestRate)
```

**Why It Works:** Changing only the reinvestment rate shows the sensitivity of the return to that assumption. The finance rate stays fixed, so the comparison is clean.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | The values do not include both a positive and a negative number. | Enter the outflow as a negative value and the inflows as positive values. |
| Result far from the IRR | The reinvestment rate is far from the IRR, which is expected. | Check that the reinvestment rate reflects the cash you can actually reinvest. |
| Result looks wrong | The rates were entered as whole numbers, such as 9 instead of 0.09. | Enter the rates as decimals or percentages. |
| Wrong result | A blank cell was skipped, so later flows moved up a period. | Enter 0 for each period with no cash flow. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Microsoft 365 and Excel for the web | Returns `#DIV/0!` without both signs. Blank cells are ignored, and zeros are included. |
| Google Sheets | Available | Uses `cashflow_amounts`, `financing_rate` and `reinvestment_return_rate` in the same order. The page does not state the error values. |

## Tips and Best Practices

- Use the borrowing rate for the finance rate and the rate on idle cash for the reinvestment rate.
- Enter a 0 for any period with no cash flow so that the timing stays correct.
- Compare MIRR with the hurdle rate, not only with IRR, because it reflects a realistic reinvestment assumption.
- Show both the finance and reinvestment rates next to the result so that readers can see the assumptions.
- Use XIRR and XNPV when the cash flows fall on actual dates.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IRR](IRR.md) | Rate that sets NPV to zero, assuming reinvestment at the IRR. |
| [NPV](NPV.md) | Dollar value of the cash flows at a chosen rate. |
| [XIRR](XIRR.md) | IRR for cash flows on irregular dates. |
| [FV](FV.md) | Future value of a single rate and a level payment stream. |
| [PV](PV.md) | Present value of a single amount or a level payment stream. |

## Official Documentation

- [Microsoft Support: MIRR function](https://support.microsoft.com/en-us/excel/functions/mirr-function)
- [Google Docs Editors Help: MIRR](https://support.google.com/docs/answer/3093180)
