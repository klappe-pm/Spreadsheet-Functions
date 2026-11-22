---
domain: Spreadsheet Functions
category: Financial
subcategory: Investment Returns
purpose:
  - Financial Modeling
  - Investment Analysis
use-case:
  - Lease Payment Valuation
  - Milestone Payment Schedules
  - Project Acceptance Tests
related:
  - FV
  - IRR
  - NPV
  - PV
  - XIRR
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/xnpv-function
  - https://support.google.com/docs/answer/3093268
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Irregular Net Present Value
  - Discounted Value of Irregular Cash Flows
tags:
  - cash-flow
  - discounting
  - excel
  - irregular-dates
  - sheets
---

# XNPV

## Description

**XNPV** returns the net present value of cash flows that fall on irregular dates. You give it a discount rate, a list of amounts and a list of dates. The first date marks the start of the schedule, and every later cash flow is discounted back to that start. A positive result means the cash flows are worth more than the rate you required; a negative result means they are worth less.

Use XNPV for milestone payments, leases, or any investment whose payments do not land on a regular calendar. When the payments are evenly spaced, NPV gives the same kind of answer with simpler inputs.

## Syntax

```excel
=XNPV(rate, values, dates)
```

<!-- Image 1: Discount Rate and Schedule Layout. See Images/Financial/XNPV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The discount rate as a decimal, such as 0.08 for 8 percent. |
| `values` | Yes | The cash flows as a range or array. Payments out are negative and receipts are positive. The list must contain at least one negative and one positive value. |
| `dates` | Yes | The date of each cash flow, in the same order as `values`. The first date marks the start; every other date must be later than it, but the dates after the first may appear in any order. |

### Return Value

A single number in the same currency as the cash flows, valued as of the first date. When an argument is invalid, XNPV returns an error; see Common Errors.

## Examples

All examples use this schedule. The labels are in row 1, the dates are in `A2:A5`, and the cash flows are in `B2:B5`. The rate label is in `D1`, and the rate 0.08 is in `D2`.

| Date | Cash Flow |
| --- | --- |
| 2025-01-01 | -12000 |
| 2025-07-01 | 3500 |
| 2026-01-01 | 4200 |
| 2026-06-30 | 5000 |

### Example 1: Net Present Value at a Fixed Rate

```excel
=XNPV(0.08, B2:B5, A2:A5)
```

**Result:** `-284.96`

At 8 percent, the three later receipts are worth 284.96 less than the 12,000 paid on January 1, 2025.

### Example 2: Using a Rate Cell

```excel
=XNPV(D2, B2:B5, A2:A5)
```

**Result:** `-284.96`

Keeping the rate in its own cell lets you change it without editing the formula.

<!-- Image 2: Result at Two Discount Rates. See Images/Financial/XNPV.md -->

### Example 3: Testing a Lower Rate

```excel
=XNPV(0.05, B2:B5, A2:A5)
```

**Result:** `65.03`

At 5 percent the same schedule has a positive value, so the investment clears that lower hurdle.

### Example 4: Accept or Reject Decision

```excel
=IF(XNPV(D2, B2:B5, A2:A5) >= 0, "Accept", "Reject")
```

**Result:** `Reject`

The decision follows from the sign of the result at the rate in `D2`.

### Example 5: Rounded Result

```excel
=ROUND(XNPV(0.12, B2:B5, A2:A5), 2)
```

**Result:** `-719.64`

ROUND fixes the result at two decimals for reports. The same schedule at 12 percent is worth less than at 8 percent.

## Story Problems

### Problem 1: Bakery Oven Savings

A bakery considers a 25,000 oven that saves money on irregular dates. The purchase is the first row, and the savings follow. The labels are in row 1, the dates are in column A, and the amounts are in column B.

| Date | Cash Flow |
| --- | --- |
| 2024-04-01 | -25000 |
| 2024-10-01 | 6000 |
| 2025-04-01 | 7500 |
| 2025-10-01 | 8200 |
| 2026-04-01 | 4000 |

**Task:** Put the required return of 9% in `D2` and find the net present value of the oven at that rate using `A2:A6` and `B2:B6`.

**Solution:**

```excel
=XNPV(D2, B2:B6, A2:A6)
```

**Answer:** `-1801.45`. The savings are worth about 1,800 less than the purchase price at 9 percent, so the oven does not meet the required return.

<!-- Image 3: Results Panel for the Story Problems. See Images/Financial/XNPV.md -->

### Problem 2: Developer Milestone Payments

A developer pays 8,000 to start a site survey on March 1, 2025. Client milestone payments follow on the dates below.

| Date | Cash Flow |
| --- | --- |
| 2025-03-01 | -8000 |
| 2025-09-01 | 2500 |
| 2026-03-01 | 3000 |
| 2026-09-01 | 4000 |

**Task:** Find the value of the project at a 10% rate, measured as of March 1, 2025.

**Solution:**

```excel
=XNPV(0.10, B2:B5, A2:A5)
```

**Answer:** `575.77`. The discounted receipts exceed the 8,000 survey cost by 575.77, so the project is worth doing at 10 percent.

## Use Cases

### Milestone Payment Schedules

**Scenario:** A contractor values a multi-stage job whose payments are due on negotiated dates rather than on a monthly calendar.

```excel
=XNPV(DiscountRate, Milestones[Amount], Milestones[Due Date])
```

**Why It Works:** Structured references keep the schedule in one table, and the named cell `DiscountRate` lets the contractor test several discount rates without rewriting the formula.

### Lease Payment Valuation

**Scenario:** A company compares the discounted value of lease payments with the price of buying the equipment outright.

```excel
=XNPV(DiscountRate, Lease[Payment], Lease[Payment Date])
```

**Why It Works:** When the lease payments fall on irregular dates, XNPV discounts each one from the first date, so the total can be compared directly with the purchase price if the purchase is entered as the first row.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A value or date is text, or a date is not valid. | Enter amounts as numbers and dates with DATE or as date values. |
| `#NUM!` | A date comes before the first date. | Move the earliest date to the first row. |
| `#NUM!` | The values and dates ranges have different sizes. | Select ranges with the same number of rows. |
| Result far from expected | The rate was typed as 8 instead of 0.08, which discounts every payment by 800 percent a year. | Enter the rate as a decimal or as a percentage-formatted value. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions, including Excel for the web | Later payments are discounted on a 365-day year. Dates are truncated to whole numbers. |
| Google Sheets | Available | Same cash flow layout. The rate argument is named `discount`. The help page does not state the return value or list error conditions. |

## Tips and Best Practices

- Keep each amount in the same row as its date; XNPV pairs them by position, not by label.
- Store the discount rate in a labeled cell so each scenario can be tested without editing the formula.
- Build a small table of rates and their results to find the rate at which the value becomes zero.
- Include the outlay as a negative amount in the first row so the start date is the purchase date.

## Related Functions

| Function | Relationship |
| --- | --- |
| [XIRR](XIRR.md) | Returns the rate at which XNPV equals zero for the same cash flows. |
| [NPV](NPV.md) | Net present value for cash flows on evenly spaced periods. |
| [PV](PV.md) | Present value of a loan or investment with regular payments. |
| [FV](FV.md) | Future value of an investment at a constant rate. |
| [IRR](IRR.md) | Internal rate of return for cash flows on evenly spaced periods. |

## Official Documentation

- [Microsoft Support: XNPV function](https://support.microsoft.com/en-us/excel/functions/xnpv-function)
- [Google Docs Editors Help: XNPV](https://support.google.com/docs/answer/3093268)
