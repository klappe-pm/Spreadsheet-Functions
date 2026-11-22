---
domain: Spreadsheet Functions
category: Financial
subcategory: Investment Returns
purpose:
  - Investment Analysis
use-case:
  - Franchise Stake Returns
  - Irregular Project Funding
  - Private Deal Comparison
related:
  - IRR
  - MIRR
  - NPV
  - PV
  - XNPV
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/xirr-function
  - https://support.google.com/docs/answer/3093266
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Irregular Internal Rate of Return
  - Return on Irregular Cash Flows
tags:
  - cash-flow
  - excel
  - internal-rate-of-return
  - irregular-dates
  - sheets
---

# XIRR

## Description

**XIRR** returns the internal rate of return for a series of cash flows that fall on irregular dates. You give it a list of amounts, where money you pay out is negative and money you receive is positive, and a matching list of dates. The result is the annual rate at which the present value of all the cash flows adds up to zero.

Use XIRR when deposits, withdrawals or payments do not follow a fixed schedule, such as a private investment with a capital call, a partial distribution and a final sale. XNPV takes the same inputs but uses a discount rate you supply, so it returns a dollar value instead of a rate.

## Syntax

```excel
=XIRR(values, dates, [guess])
```

<!-- Image 1: Cash Flow Layout. See Images/Financial/XIRR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `values` | Yes | The cash flows as a range or array. Payments out are negative and receipts are positive. The list must contain at least one negative and one positive value. |
| `dates` | Yes | The date of each cash flow, in the same order as `values`. Enter dates with DATE or cell references, not as text. Every date must fall on or after the first date. |
| `guess` | No | Your estimate of the annual rate. When omitted, XIRR starts from 10 percent (0.1). |

### Return Value

An annual rate as a decimal, such as 0.1578. Format the cell as a percentage to display it as 15.78%. When XIRR cannot find a rate, it returns an error; see Common Errors.

## Examples

All examples use this investment. The labels are in row 1, the dates are in `A2:A5`, and the cash flows are in `B2:B5`.

| Date | Cash Flow |
| --- | --- |
| 2024-03-01 | -5000 |
| 2024-09-15 | 1500 |
| 2025-02-01 | 2200 |
| 2025-08-20 | 2100 |

### Example 1: Annual Return on the Investment

```excel
=XIRR(B2:B5, A2:A5)
```

**Result:** `15.78%`

The first cash flow is the outlay. The three later receipts arrive on irregular dates, and XIRR converts that timing into one annual rate.

### Example 2: Supplying a Starting Guess

```excel
=XIRR(B2:B5, A2:A5, 0.2)
```

**Result:** `15.78%`

The guess of 0.2 tells XIRR where to start its search. When the search converges, the answer is the same as in Example 1.

<!-- Image 2: Sign Convention for Cash Flows. See Images/Financial/XIRR.md -->

### Example 3: Flagging a Target Return

```excel
=IF(XIRR(B2:B5, A2:A5) >= 0.12, "Meets target", "Below target")
```

**Result:** `Meets target`

The formula compares the rate with a 12 percent hurdle and returns a decision label instead of a number.

### Example 4: Guarding Against Errors

```excel
=IFERROR(XIRR(B2:B5, A2:A5), "Check cash flows")
```

**Result:** `15.78%`

If the cash flows are edited so that no negative value remains, the cell shows `Check cash flows` instead of an error code.

## Story Problems

### Problem 1: Franchise Stake Return

A sandwich shop owner buys a share of a franchise location and receives payouts on irregular dates. The labels are in row 1, with the dates in column A and the cash flows in column B.

| Date | Cash Flow |
| --- | --- |
| 2023-05-01 | -20000 |
| 2023-11-30 | 1800 |
| 2024-06-15 | 3200 |
| 2025-01-10 | 19500 |

**Task:** Find the annual return on the stake from the dates and amounts in `A1:B5`.

**Solution:**

```excel
=XIRR(B2:B5, A2:A5)
```

**Answer:** `14.14%`. The owner receives 24,500 in total on a 20,000 investment. The gain of 4,500 arrives over about 1.7 years, so the annual return is 14.14 percent.

### Problem 2: Private Loan Repayments

A private lender advances 10,000 on January 15, 2024. Repayments come back on irregular dates, as shown below.

| Date | Cash Flow |
| --- | --- |
| 2024-01-15 | -10000 |
| 2024-07-15 | 2500 |
| 2025-01-15 | 4000 |
| 2025-06-15 | 5000 |

**Task:** Find the annual yield the lender earns on the loan.

**Solution:**

```excel
=XIRR(B2:B5, A2:A5)
```

**Answer:** `14.03%`. The lender gets back 11,500 on a 10,000 loan. Because 2,500 comes back after six months, the money returns early enough that the compound annual rate is 14.03 percent.

<!-- Image 3: Results Panel for the Story Problems. See Images/Financial/XIRR.md -->

## Use Cases

### Private Deal Comparison

**Scenario:** An analyst compares two private investments that send cash on different dates and needs the annual return on each.

```excel
=XIRR(Deals[Cash Flow], Deals[Date])
```

**Why It Works:** The structured references point at a table named Deals, so cash flows added as new rows join the calculation automatically. Each deal gets its own table, and the same formula is copied for each one.

### Irregular Project Funding

**Scenario:** A developer receives stage payments and funds overruns when they happen, so one column mixes capital calls and receipts.

```excel
=XIRR(Project[Amount], Project[Date], 0.1)
```

**Why It Works:** Capital calls are entered as negative amounts and receipts as positive, so XIRR reads the timing and direction from one column. The explicit 0.1 guess matches the default and documents the starting assumption.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The values contain no negative number or no positive number. | Include at least one payment out and one receipt. |
| `#NUM!` | A date comes before the first date in the list. | Move the earliest date to the first row. |
| `#NUM!` | The values and dates ranges have different sizes. | Select ranges with the same number of rows. |
| `#NUM!` | XIRR does not find a rate within 100 tries. | Supply a closer estimate in the `guess` argument. |
| `#VALUE!` | A date is text or is not a valid date. | Re-enter the date with DATE or as a date value. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions, including Excel for the web | Later payments are discounted on a 365-day year. Dates are truncated to whole numbers. |
| Google Sheets | Available | Same argument order and default guess of 0.1. The help page does not list error conditions, so test edge cases such as all-positive values. |

## Tips and Best Practices

- Use a table for the cash flows so the ranges grow with new rows.
- Check a result by entering it as the rate in XNPV; the answer should be close to zero.
- Leave `guess` out unless XIRR returns `#NUM!`, then try an estimate near the expected rate.
- Format the result as a percentage so the rate reads clearly, and keep the raw value for other formulas.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IRR](IRR.md) | Internal rate of return for cash flows on evenly spaced periods. |
| [MIRR](MIRR.md) | Internal rate of return that uses separate finance and reinvestment rates. |
| [NPV](NPV.md) | Net present value for cash flows on evenly spaced periods. |
| [PV](PV.md) | Present value of a loan or investment with regular payments. |
| [XNPV](XNPV.md) | Net present value for the same irregular dates, given a discount rate. |

## Official Documentation

- [Microsoft Support: XIRR function](https://support.microsoft.com/en-us/excel/functions/xirr-function)
- [Google Docs Editors Help: XIRR](https://support.google.com/docs/answer/3093266)
