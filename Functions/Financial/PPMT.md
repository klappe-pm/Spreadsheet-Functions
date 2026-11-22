---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
purpose:
  - Loan Analysis
use-case:
  - Amortization Schedules
  - Business Loan Planning
  - Loan Principal Tracking
related:
  - CUMIPMT
  - CUMPRINC
  - IPMT
  - PMT
  - PV
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/ppmt-function
  - https://support.google.com/docs/answer/3093187
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Principal Payment
tags:
  - amortization
  - excel
  - loan-payments
  - sheets
---

# PPMT

## Description

**PPMT** returns the principal part of a loan payment for one specific period. Each regular payment from PMT contains some interest and some principal. The interest part is the balance at the start of the period multiplied by the rate, and the principal part is the rest of the payment. PPMT returns that principal part, so the principal and interest parts together equal the payment.

The rate and the number of periods must use the same time unit, and the period you request must fall between 1 and the number of periods. Early payments carry mostly interest, and later payments carry mostly principal, so the same loan shows a rising principal figure over time.

Use PPMT to build an amortization schedule or to find how much of a particular payment reduces the balance. Use IPMT for the interest part of the same payment, and use CUMPRINC to add up the principal over several periods.

## Syntax

```excel
=PPMT(rate, per, nper, pv, [fv], [type])
```

<!-- Image 1: Principal and Interest Split. See Images/Financial/PPMT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The interest rate per period. For monthly payments on an annual rate, use the annual rate divided by 12. |
| `per` | Yes | The payment period to calculate. It must be a whole number from 1 to `nper`. |
| `nper` | Yes | The total number of payments. It must use the same period unit as the rate. |
| `pv` | Yes | The present value, the amount borrowed or the lump sum that the payments are worth today. |
| `fv` | No | The cash balance you want after the last payment. Omitted means 0. |
| `type` | No | When payments fall due: `0` or omitted for the end of each period, or `1` for the beginning of each period. |

### Return Value

A number: the principal part of the payment for the requested period. Excel shows it as a negative number when the loan amount is positive, which matches the sign convention used by PMT. The function returns an error when the period is outside 1 to `nper`, or when an argument is text that cannot be read as a number.

## Examples

### Example 1: Principal in the First Month

```excel
=PPMT(6%/12, 1, 60, 25000)
```

**Result:** `-358.32`

Of the 483.32 monthly payment on the loan in the PMT examples, 125.00 is interest in month 1 and the remaining 358.32 reduces the balance.

### Example 2: Principal in the Last Month

```excel
=PPMT(6%/12, 60, 60, 25000)
```

**Result:** `-480.92`

In the final month almost the entire payment is principal, because only a small balance remains to accrue interest.

<!-- Image 2: Principal Rising Over the Schedule. See Images/Financial/PPMT.md -->

### Example 3: Principal in Year 2 of an Annual Loan

```excel
=PPMT(8%, 2, 5, 50000)
```

**Result:** `-9204.65`

For a five year loan of 50,000 at 8% with annual payments, the second year's payment reduces the balance by 9,204.65.

## Story Problems

### Problem 1: Principal in Month 10 of a Car Loan

A driver borrows 22,000 at 6.9% annual interest, repaid over 48 monthly payments. The driver wants to know how much of the 10th payment reduces the balance.

| Term | Value |
| --- | --- |
| Annual rate | 6.90% |
| Period | 10 |
| Number of months | 48 |
| Amount borrowed | 22000 |

**Task:** Find the principal part of the 10th monthly payment.

**Solution:**

```excel
=PPMT(B2/12, B3, B4, B5)
```

**Answer:** `-420.44`, which means 420.44 of the 10th payment reduces the balance. The rest of that payment is interest.

### Problem 2: Principal in Year 3 of a Business Loan

A business borrows 75,000 at 9% a year and repays it in four equal annual payments made at the end of each year. The owner wants the principal part of the third payment.

**Task:** Find the principal part of the payment in year 3.

**Solution:**

```excel
=PPMT(B2, B3, B4, B5)
```

Here `B2` is 9%, `B3` is 3, `B4` is 4 and `B5` is 75000.

**Answer:** `-19485.02`. Late in the loan, most of each payment reduces the balance.

<!-- Image 3: Story Problem Inputs and Output. See Images/Financial/PPMT.md -->

## Use Cases

### Amortization Schedules

**Scenario:** A lender builds a schedule that lists the principal and interest portions for every payment of a loan.

```excel
=PPMT(Rate/12, ROW()-1, Months, LoanAmount)
```

**Why It Works:** The period number comes from the row, so filling the formula down produces the principal column of the schedule. The interest column uses IPMT with the same arguments.

### Loan Principal Tracking

**Scenario:** A finance team wants to know how much principal a borrower has repaid by a given payment.

```excel
=-CUMPRINC(Rate/12, Months, LoanAmount, 1, PaymentsMade, 0)
```

**Why It Works:** CUMPRINC adds the principal over a range of periods, and the negative sign converts the result into a positive amount of principal repaid.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error result | The period is outside 1 to `nper`. | Use a period number from 1 to the total number of payments. |
| Principal far too small | The annual rate was used with a monthly term. | Divide the annual rate by 12 for monthly payments. |
| Sign appears reversed | PPMT follows the same sign convention as PMT. | Read the result as the principal portion of the payment, and keep the sign consistent across formulas. |
| `#VALUE!` | An argument is text that cannot be read as a number. | Enter numbers, or convert text values with `VALUE`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Arguments are named `rate`, `per`, `nper`, `pv`, `fv` and `type`. |
| Google Sheets | Available | Arguments are named `rate`, `period`, `number_of_periods`, `present_value`, `future_value` and `end_or_beginning`. |

## Tips and Best Practices

- Check that the principal and interest parts for one period add up to the payment from PMT.
- Use the same period unit for the rate and the number of periods, and keep the period number in that unit.
- Fill the formula down a column with a row based period number to build a full amortization schedule quickly.
- Use CUMPRINC when you need the total principal over several periods rather than one period.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PMT](PMT.md) | Returns the total payment that PPMT splits into principal and interest. |
| [IPMT](IPMT.md) | Returns the interest part of the same payment for one period. |
| [CUMPRINC](CUMPRINC.md) | Adds up the principal paid over a range of periods. |
| [CUMIPMT](CUMIPMT.md) | Adds up the interest paid over a range of periods. |
| [PV](PV.md) | Returns the present value of the loan that the payments repay. |

## Official Documentation

- [Microsoft Support: PPMT function](https://support.microsoft.com/en-us/excel/functions/ppmt-function)
- [Google Docs Editors Help: PPMT](https://support.google.com/docs/answer/3093187)
