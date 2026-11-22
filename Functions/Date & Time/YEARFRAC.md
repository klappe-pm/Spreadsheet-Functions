---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Arithmetic
purpose:
  - Bond Analysis
  - Date Calculation
use-case:
  - Accrued Interest Estimates
  - Partial Year Lease Charges
  - Prorated Contract Fees
related:
  - DATEDIF
  - DAYS
  - DAYS360
  - EDATE
  - YEAR
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/yearfrac-function
  - https://support.google.com/docs/answer/3092989
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Fraction of Year
  - Year Fraction
tags:
  - date
  - day-count
  - excel
  - financial
  - sheets
---

# YEARFRAC

## Description

**YEARFRAC** returns the part of a year that lies between two dates, as a decimal. A result of 0.5 means half a year. The function is useful for charging a share of an annual amount, such as a prorated fee or an accrued interest amount, for a period shorter than a full year.

The optional basis argument decides how the days and the year are counted. The default, basis 0, uses the US (NASD) 30/360 method, which treats every month as 30 days and the year as 360 days. Basis 1 uses actual days and the real length of the year. Basis 2 divides actual days by 360, and basis 3 divides actual days by 365. Basis 4 is the European 30/360 method, which is close to basis 0 but adjusts end-of-month dates differently.

Choose the basis that your contract or financial convention names. For a general calculation of elapsed time, basis 1 is usually the most intuitive choice. The function is most common in fixed-income finance, where bond and loan terms define the basis.

## Syntax

```excel
=YEARFRAC(start_date, end_date, [basis])
```

<!-- Image 1: Start Date, End Date and Basis. See Images/Date & Time/YEARFRAC.md -->

Google Sheets names the last argument `day_count_convention`, as in `YEARFRAC(start_date, end_date, [day_count_convention])`. The values are the same, so the formulas work on both platforms.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `start_date` | Yes | The first date of the period. Use a cell that contains a date, the result of DATE, or a serial number. |
| `end_date` | Yes | The last date of the period, entered the same way as the start date. |
| `basis` | No | The day count method from 0 to 4. The default is 0. Values outside 0 to 4 return `#NUM!`. |

### Basis Values

| Basis | Day Count Method |
| --- | --- |
| 0 (default) | US (NASD) 30/360 |
| 1 | Actual/actual |
| 2 | Actual/360 |
| 3 | Actual/365 |
| 4 | European 30/360 |

### Return Value

A decimal number, usually between 0 and 1 for a period shorter than a year, and greater than 1 for longer periods. The function returns `#VALUE!` when a date is not valid, and `#NUM!` when basis is outside 0 to 4.

## Examples

Examples 1 to 4 use 03/15/2026 in A2 and 09/01/2026 in B2. Example 5 uses its own dates.

<!-- Image 2: Basis Results for One Period. See Images/Date & Time/YEARFRAC.md -->

### Example 1: Default Basis

```excel
=YEARFRAC(A2, B2)
```

**Result:** `0.4611`

Under 30/360, the period from March 15 to September 1 counts as 166 days on a 360-day year. The result is shown rounded to four decimal places.

### Example 2: Actual Days Over Actual Year Length

```excel
=YEARFRAC(A2, B2, 1)
```

**Result:** `0.4658`

The period is 170 actual days, and 2026 has 365 days, so the result is 170 divided by 365.

### Example 3: Actual Days Over 360

```excel
=YEARFRAC(A2, B2, 2)
```

**Result:** `0.4722`

The 170 actual days are divided by 360, which gives a slightly larger fraction than basis 1.

### Example 4: Actual Days Over 365

```excel
=YEARFRAC(A2, B2, 3)
```

**Result:** `0.4658`

For a period inside a non-leap year, basis 3 gives the same result as basis 1 because both divide by 365.

### Example 5: A Period That Spans Two Years

```excel
=YEARFRAC(C2, D2)
```

**Result:** `1.6944` when C2 holds 06/10/2025 and D2 holds 02/20/2027

Under 30/360, the period is 610 days, which is 1 year and 250 days on the 360-day basis. The whole year and the fraction are added together.

## Story Problems

### Problem 1: Prorated Contract Fee

A software license costs 12,000 for a full year. It starts on 03/15/2026 and ends on 09/01/2026. The contract names actual days over actual year length, which is basis 1.

| Item | Value |
| --- | --- |
| Annual fee (C2) | 12000 |
| Start date (A2) | 03/15/2026 |
| End date (B2) | 09/01/2026 |

**Task:** Find the fee for the partial year.

**Solution:**

```excel
=C2*YEARFRAC(A2, B2, 1)
```

**Answer:** `5,589.04`. The default basis would give 5,533.33, so the basis named in the contract matters.

### Problem 2: Accrued Interest on a Loan

A loan of 250,000 carries 6 percent annual interest. Interest accrues from 03/15/2026 to 09/01/2026 on the default 30/360 basis.

**Task:** Find the interest accrued for the period.

**Solution:**

```excel
=250000*0.06*YEARFRAC(A2, B2)
```

**Answer:** `6,916.67`. The fraction is 0.4611, and 15,000 multiplied by that fraction gives the accrued amount.

### Problem 3: Lease Charge Across Two Years

A lease costs 9,600 per year and runs from 06/10/2025 to 02/20/2027. The lease uses the default 30/360 basis.

**Task:** Find the total lease charge for the full period.

**Solution:**

```excel
=9600*YEARFRAC(C2, D2)
```

**Answer:** `16,266.67`. The fraction is 1.6944 years, so the charge is 9,600 multiplied by 1.6944.

## Use Cases

### Accrued Interest Estimates

**Scenario:** A treasury analyst estimates interest that has built up on a bond between coupon dates.

```excel
=Principal*Rate*YEARFRAC(LastCoupon, SettlementDate, 0)
```

**Why It Works:** The fraction is the share of the year that has passed on the 30/360 basis, which bond conventions use for many instruments. Check the basis in the bond terms before you rely on the result.

### Partial Year Lease Charges

**Scenario:** A property manager charges tenants for a partial first year, using the actual days in the year.

```excel
=AnnualRent*YEARFRAC(MoveIn, LeaseEnd, 1)
```

**Why It Works:** Basis 1 divides the actual number of days by the length of the year, which matches a daily proration. Round the result to cents with ROUND before you invoice.

### Prorated Contract Fees

**Scenario:** A consultant bills a retainer that starts in the middle of the year and must show the calculation to the client.

```excel
=RetainerFee*YEARFRAC(StartDate, EndDate, 1)
```

**Why It Works:** The formula shows the fee as a share of the annual amount. Basis 1 is easier to explain than 30/360, because every day counts as a real day.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A date is not valid, often because it was typed as text. | Enter the dates with DATE or convert them with DATEVALUE. |
| `#NUM!` | basis is less than 0 or greater than 4. | Use a basis from 0 to 4. |
| Small unexpected result | Dates were typed as text or as numbers that were read as divisions in Google Sheets. | Pass cell references, DATE results or DATEVALUE results. |
| Different result from the contract | The default basis 0 was used when the contract names another basis. | Set basis to the value named in the contract. |
| Odd fraction with February dates | Basis 0 can return an incorrect result when the start date is the last day of February. | Compare with basis 1 or check the convention in the contract. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Accepts basis 0 to 4. The default is basis 0. |
| Google Sheets | Available | Named `day_count_convention`. Accepts 0 to 4 with the same meanings. Basis 1 is recommended for non-financial use. |

## Tips and Best Practices

- Read the basis from the contract or bond terms first, and write it into the formula, so the calculation can be audited.
- Use basis 1 for simple proration of days, and basis 0 only when a contract or bond names it.
- Multiply by the annual amount outside the function and round the final result to cents.
- Keep the start and end dates in cells, so the same formula works for every row of a schedule.
- Compare the results from two bases on a known period to see how much the convention changes a charge.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATEDIF](DATEDIF.md) | Counts complete days, months or years between two dates. |
| [DAYS](DAYS.md) | Counts the days between two dates for a simple day total. |
| [DAYS360](DAYS360.md) | Counts days on a 360-day year, the basis used by many financial calculations. |
| [EDATE](EDATE.md) | Adds months to a date, useful for building payment schedules. |
| [YEAR](YEAR.md) | Returns the year of a date, useful for checking which year a period falls in. |

## Official Documentation

- [Microsoft Support: YEARFRAC function](https://support.microsoft.com/en-us/excel/functions/yearfrac-function)
- [Google Docs Editors Help: YEARFRAC](https://support.google.com/docs/answer/3092989)
