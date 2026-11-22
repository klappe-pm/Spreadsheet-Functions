---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Arithmetic
purpose:
  - Date Calculation
use-case:
  - Contract Durations
  - Customer Account Age
  - Employee Tenure
related:
  - DATE
  - DAYS
  - DAYS360
  - EDATE
  - NETWORKDAYS
  - TODAY
  - YEARFRAC
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/datedif-function
  - https://support.google.com/docs/answer/6055612
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Date Difference
  - Months Between Dates
tags:
  - date-arithmetic
  - date-difference
  - excel
  - sheets
---

# DATEDIF

## Description

**DATEDIF** returns the difference between two dates in whole years, whole months or days, depending on the unit code you give it. It is the standard way to answer questions such as "how many complete years has this employee worked" or "how many full months remain on this contract." Subtracting two dates gives only a count of days, so DATEDIF is the choice when you need a count in larger units.

DATEDIF counts a unit only once it is complete. A month is not counted until the end date reaches the same day of the month as the start date. For example, from January 31 to February 28 is zero complete months, because February has no 31st. The function is documented in both Excel and Google Sheets.

Microsoft describes DATEDIF as provided for compatibility with older Lotus 1-2-3 workbooks, and it warns that the `"MD"` unit can return negative, zero or inaccurate results. For new work, use `"Y"`, `"M"` and `"D"`, or use DATE and subtraction for the remaining parts.

## Syntax

```excel
=DATEDIF(start_date, end_date, unit)
```

<!-- Image 1: Start Date, End Date and Unit Code. See Images/Date & Time/DATEDIF.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `start_date` | Yes | The earlier date. Enter a cell that contains a date, a function that returns a date, or a date serial number. |
| `end_date` | Yes | The later date. In Excel, the result is `#NUM!` when this date is earlier than `start_date`. |
| `unit` | Yes | A text code in quotation marks that sets the unit of the result. The codes are listed below. |

### Return Value

A whole number in the unit you choose. The unit codes are:

| Unit | Returns |
| --- | --- |
| `"Y"` | Complete years between the two dates. |
| `"M"` | Complete months between the two dates. |
| `"D"` | Total days between the two dates. |
| `"MD"` | Days left after the complete months and years are removed. Microsoft warns this code can be inaccurate. |
| `"YM"` | Complete months left after the complete years are removed. |
| `"YD"` | Days between the dates, ignoring years. Use it for the days since the last anniversary. |

## Examples

### Example 1: Complete Years

```excel
=DATEDIF(A2, B2, "Y")
```

**Result:** With A2 set to June 30, 1990 and B2 set to June 29, 2026, the result is `35`.

The 35th anniversary falls on June 30, 2025, and June 30, 2026 has not yet arrived, so the result stays at 35 complete years.

### Example 2: Complete Months

```excel
=DATEDIF(A2, B2, "M")
```

**Result:** With A2 set to February 10, 2024 and B2 set to February 9, 2026, the result is `23`.

The 24th month would end on February 10, 2026, which is one day after B2, so it is not yet complete.

<!-- Image 2: Complete Versus Partial Months. See Images/Date & Time/DATEDIF.md -->

### Example 3: Total Days

```excel
=DATEDIF(A2, B2, "D")
```

**Result:** With A2 set to March 1, 2026 and B2 set to April 15, 2026, the result is `45`.

March has 31 days, so March 1 to April 1 is 31 days, and April 1 to April 15 adds 14 more.

### Example 4: Guard Against Reversed Dates

```excel
=IF(A2 > B2, "Check dates", DATEDIF(A2, B2, "D"))
```

**Result:** With A2 later than B2, the result is `Check dates`. With the dates in order, the day count is returned.

Excel returns `#NUM!` when the start is later than the end, so this check keeps a report readable when a date is typed in the wrong column.

### Example 5: Age in Complete Years

```excel
=DATEDIF(A2, TODAY(), "Y")
```

**Result:** The complete years between the birth date in A2 and today.

The result changes each day only when a birthday passes, so it is a reliable input for age bands and eligibility checks.

## Story Problems

### Problem 1: Years of Service

A company tracks hire dates in `A1:B4`. The HR team needs each employee's complete years of service as of November 22, 2026.

| Employee | Hire Date |
| --- | --- |
| Avery | March 14, 2015 |
| Blake | November 30, 2019 |
| Casey | June 1, 2024 |

**Task:** Put the report date in `D1`, then return the complete years of service for each employee in column C.

**Solution:**

```excel
=DATEDIF(B2, $D$1, "Y")
```

**Answer:** Avery has 11 complete years, because the 2026 anniversary of March 14 has passed. Blake has 6 complete years, because November 30 has not yet arrived in 2026. Casey has 2 complete years.

### Problem 2: Contract Length

A consultant's contract runs from July 31, 2025 to March 15, 2026. The client wants the length in complete months and in days.

| Contract Start | Contract End |
| --- | --- |
| July 31, 2025 | March 15, 2026 |

**Task:** Return the complete months in one cell and the total days in another.

**Solution:**

```excel
=DATEDIF(A2, B2, "M")
=DATEDIF(A2, B2, "D")
```

**Answer:** 7 complete months and 227 days. The eighth month would end on March 31, which is after March 15, so it is not counted.

## Use Cases

### Employee Tenure Report

**Scenario:** An HR team needs a tenure band for each employee, such as under 2 years, 2 to 5 years, or over 5 years.

```excel
=IF(DATEDIF(B2, TODAY(), "Y") < 2, "Under 2", IF(DATEDIF(B2, TODAY(), "Y") <= 5, "2 to 5", "Over 5"))
```

**Why It Works:** DATEDIF counts complete years, so a tenure band changes only after the anniversary has passed. Using complete years avoids rounding an employee into a band too early.

### Contract Term Tracking

**Scenario:** A procurement team lists contracts and wants to flag any contract that has been running for 12 or more complete months.

```excel
=IF(DATEDIF(B2, C2, "M") >= 12, "Renewal Review", "Active")
```

**Why It Works:** Using the complete month count ensures that a contract running 11 months and 25 days is not flagged early.

### Customer Account Age

**Scenario:** A subscription service offers a loyalty discount to customers with an account older than 3 complete years.

```excel
=IF(DATEDIF(B2, TODAY(), "Y") >= 3, "Loyalty", "Standard")
```

**Why It Works:** DATEDIF gives a whole number of years, so the test does not depend on the time of day or the display format of the dates.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The start date is later than the end date (Excel). | Check the order of the dates, or guard the formula with IF. |
| `#VALUE!` | A date argument is text that cannot be read as a date. | Convert the text with DATEVALUE or DATE. |
| Date shown instead of a number | The result cell has a date format. | Format the result cell as Number. |
| Negative or odd result with `"MD"` | Microsoft warns this unit can be inaccurate. | Compute the remaining days with DATE, for example `end - DATE(YEAR(end), MONTH(end), DAY(start))`. |
| Unexpected month count | The end day is earlier than the start day, so the last month is not complete. | Expect this behavior, or use `"D"` and divide by 30.44 for an estimate. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns `#NUM!` when start_date is later than end_date. Microsoft does not recommend `"MD"`. |
| Google Sheets | Available | Same unit codes. The documentation does not state what happens when start_date is later than end_date, so test that case before relying on it. |

## Tips and Best Practices

- Use `"Y"` for complete years, `"M"` for complete months and `"D"` for total days, and avoid `"MD"`.
- Put the report date in its own cell, such as `$D$1`, so every row uses the same end date.
- Check that the start date is earlier than the end date before calculating, especially with imported data.
- Keep the result cell formatted as Number, because a date format makes a count look like a date.
- Use DAYS for a simple day count when you do not need units, because DAYS only returns days.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds a fixed date to use as an end date or a start of month. |
| [DAYS](DAYS.md) | Returns the total days between two dates, with the arguments in end-then-start order. |
| [DAYS360](DAYS360.md) | Counts days on a 360-day year, which is common for interest calculations. |
| [EDATE](EDATE.md) | Adds months to a date, the reverse of counting months between two dates. |
| [NETWORKDAYS](NETWORKDAYS.md) | Counts working days between two dates instead of calendar days. |
| [TODAY](TODAY.md) | Supplies the current date as the end date for ages and tenure. |
| [YEARFRAC](YEARFRAC.md) | Returns the fraction of a year between two dates, useful when a decimal is needed. |

## Official Documentation

- [Microsoft Support: DATEDIF function](https://support.microsoft.com/en-us/excel/functions/datedif-function)
- [Google Docs Editors Help: DATEDIF](https://support.google.com/docs/answer/6055612)
