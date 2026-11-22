---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Parts
purpose:
  - Date Calculation
use-case:
  - Fiscal Year Labels
  - Leap Year Checks
  - Year Over Year Totals
related:
  - DATE
  - DATEDIF
  - DAY
  - MONTH
  - TODAY
  - YEARFRAC
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/year-function
  - https://support.google.com/docs/answer/3093061
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Extract Year
  - Year Number
tags:
  - date
  - excel
  - fiscal-year
  - sheets
  - year-extraction
---

# YEAR

## Description

**YEAR** returns the year of a date as a whole number, such as 2026. It reads the date value in the cell, not the way the date is displayed, so a cell that shows "Nov 22, 2026" and a cell that shows "2026-11-22" give the same result.

Use YEAR to group records by year, to label fiscal years, to compare the year of two dates, and to build year-based totals. It is one of the basic date-part functions. MONTH and DAY return the other two parts of a date, and DATE builds a date from its parts.

YEAR returns a number, not a date. Adding 1 to the result gives the next year as a number, such as 2027. To move a full date forward by a year, rebuild it with DATE, for example `DATE(YEAR(A2)+1, MONTH(A2), DAY(A2))`. Time values in a date-and-time cell are ignored.

## Syntax

```excel
=YEAR(serial_number)
```

<!-- Image 1: Date Cell and Year Result. See Images/Date & Time/YEAR.md -->

Google Sheets names the argument `date`, as in `YEAR(date)`. The argument is positional, so the same formulas work on both platforms.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `serial_number` (Excel) or `date` (Sheets) | Yes | The date to read. Use a cell that contains a date, the result of DATE, TODAY, or DATEVALUE, or a serial number. |

### Return Value

A whole number from 1900 to 9999 in Excel. The result is always a Gregorian year, even when the date is displayed in another calendar such as Hijri. A text value that the application cannot read as a date returns `#VALUE!`.

## Examples

All examples use the date 11/22/2026 in cell A2 unless the example shows its own date.

### Example 1: Year From a Date Cell

```excel
=YEAR(A2)
```

**Result:** `2026`

The formula reads the date stored in A2 and returns only its year.

### Example 2: Year From a DATE Result

```excel
=YEAR(DATE(1969, 7, 20))
```

**Result:** `1969`

DATE builds the date first, and YEAR returns the year of that date. This pattern is useful for checking a date that a formula built.

### Example 3: Fiscal Year Starting in July

```excel
=YEAR(A2) + IF(MONTH(A2) >= 7, 1, 0)
```

**Result:** `2027`

A fiscal year that starts on July 1 is named for the calendar year in which it ends. November 2026 falls in the fiscal year that ends in June 2027. Put the starting month in its own cell and replace the 7 with that cell for other year starts.

<!-- Image 2: Fiscal Year Boundary in July. See Images/Date & Time/YEAR.md -->

### Example 4: Leap Year Test

```excel
=DAY(DATE(YEAR(A2), 2, 29)) = 29
```

**Result:** `FALSE`

If the year is a leap year, February 29 exists and DATE returns it, so DAY returns 29. In 2026, DATE(2026, 2, 29) rolls over to March 1, so DAY returns 1 and the test returns FALSE. For a date in 2028, the result is TRUE.

### Example 5: Year From a Text Date

```excel
=YEAR(DATEVALUE("3/15/2026"))
```

**Result:** `2026`

Text is not always read as a date. DATEVALUE converts the text to a date value first, and YEAR then reads that value. The result depends on the date order of the locale, so use DATE with numbers when the source is ambiguous.

## Story Problems

### Problem 1: Invoice Totals for 2026

An office keeps its invoices in A2:B6. Column A holds the invoice date and column B holds the amount.

| Invoice Date | Amount |
| --- | --- |
| 03/10/2025 | 500 |
| 11/05/2025 | 750 |
| 02/14/2026 | 1200 |
| 08/30/2026 | 900 |
| 10/01/2026 | 300 |

<!-- Image 3: Invoice Table Grouped by Year. See Images/Date & Time/YEAR.md -->

**Task:** Total the amounts for invoices dated in 2026.

**Solution:**

```excel
=SUMPRODUCT((YEAR(A2:A6)=2026)*B2:B6)
```

**Answer:** `2400`. The 2026 invoices are 1200, 900 and 300. The two invoices from 2025 are excluded.

### Problem 2: Fiscal Year of a Donation

A charity starts its fiscal year on July 1. A donation is dated 08/15/2026 in A2.

**Task:** Return the fiscal year that ends in the calendar year of the next June.

**Solution:**

```excel
=YEAR(A2) + IF(MONTH(A2) >= 7, 1, 0)
```

**Answer:** `2027`. August 2026 is after the July start, so the donation belongs to the fiscal year that runs from July 2026 to June 2027.

### Problem 3: Rent Calculation for a Leap Year

A lease starts on 02/01/2028 in A2. The rent formula divides the annual rent by 366 days in a leap year and 365 otherwise.

**Task:** Label the lease year as a leap year or a common year.

**Solution:**

```excel
=IF(DAY(DATE(YEAR(A2), 2, 29)) = 29, "Leap Year", "Common Year")
```

**Answer:** `Leap Year`. 2028 is divisible by 4 and is not a century year, so February has 29 days.

## Use Cases

### Fiscal Year Labels

**Scenario:** A finance team labels each transaction with its fiscal year, which starts in April, so reports group by fiscal year rather than calendar year.

```excel
="FY" & (YEAR(A2) + IF(MONTH(A2) >= 4, 1, 0))
```

**Why It Works:** Transactions from April onward move to the next fiscal year. The label joins the text "FY" to the year number. Keep the start month in a named cell so the finance team can change it without editing the formula.

### Leap Year Checks

**Scenario:** A billing system needs to know whether a contract year has 366 days before it prorates a monthly fee.

```excel
=IF(DAY(DATE(YEAR(A2), 2, 29)) = 29, 366, 365)
```

**Why It Works:** The DATE and DAY pair detects a leap year without a long divisibility test. The result is the number of days in the year that contains the date in A2.

### Year Over Year Totals

**Scenario:** A sales log lists orders from several years, and the manager needs the total for each year on one summary sheet.

```excel
=SUMPRODUCT((YEAR(Orders[Date]) = 2026) * Orders[Amount])
```

**Why It Works:** YEAR converts each date to its year, so the comparison selects only the 2026 rows. Change the year in the formula, or point it at a cell, to build totals for other years.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The cell holds text that the application cannot read as a date. | Convert the text with DATEVALUE or enter the date with DATE. |
| Error value | The source cell already contains an error, which YEAR returns unchanged. | Fix the source cell, or wrap the formula in IFERROR. |
| Wrong year from text | A text date such as `1/2/2026` is read with a different day and month order. | Enter the date with DATE so the order is not ambiguous. |
| Result is not a date | YEAR returns a number, not a date. | Use `DATE(YEAR(A2) + 1, MONTH(A2), DAY(A2))` to move a date by a year. |
| Unexpected result in Google Sheets | A typed date inside the function is read as a division, such as `10/10/2000`. | Pass a cell reference, DATE, or DATEVALUE result instead. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns the year of the stored date value. Text dates depend on the regional date settings. |
| Google Sheets | Available | Argument is named `date` and must be a cell reference, a date-returning function, or a serial number. Typed dates inside the function are not converted. |

## Tips and Best Practices

- Extract the year into a helper column when many formulas need it, so YEAR is calculated once for each row.
- Use DATE with YEAR and MONTH to move a date by years or months while keeping the date value.
- Put a fiscal start month in a named cell so every fiscal year formula uses the same boundary.
- Check text dates with a simple test, such as `ISNUMBER(A2)`, before summing by year.
- Use DATEDIF for complete years between two dates. YEAR(B2) minus YEAR(A2) counts calendar years crossed, not full years.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds a date from year, month and day, the reverse of the date-part functions. |
| [DATEDIF](DATEDIF.md) | Counts complete years, months or days between two dates. |
| [DAY](DAY.md) | Returns the day of the month. |
| [MONTH](MONTH.md) | Returns the month number, used with YEAR for fiscal years. |
| [TODAY](TODAY.md) | Returns the current date, often passed to YEAR for the current year. |
| [YEARFRAC](YEARFRAC.md) | Returns the fraction of a year between two dates. |

## Official Documentation

- [Microsoft Support: YEAR function](https://support.microsoft.com/en-us/excel/functions/year-function)
- [Google Docs Editors Help: YEAR](https://support.google.com/docs/answer/3093061)
