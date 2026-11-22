---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Data Validation
  - Type Checking
use-case:
  - Date Column Validation
  - Import Date Checks
related:
  - DATEVALUE
  - ISBLANK
  - ISEMAIL
  - ISNUMBER
  - ISTEXT
level: 2
source:
  - https://support.google.com/docs/answer/9061381
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - data-validation
  - date-checks
  - sheets
  - type-checks
---

# ISDATE

## Description

**ISDATE** tests whether a value is a date. It returns TRUE when the value can be read as a date and FALSE when it cannot. Use it to check text that was pasted or imported, such as `July 20 1969`, before other formulas try to calculate with it.

ISDATE is most useful for text. A month name on its own, such as `July`, returns FALSE because it does not identify a day and year. An impossible date such as `Feb 30` also returns FALSE.

The documentation does not list every format that Google Sheets accepts, so test the values you expect in your own file before you rely on the check. ISDATE is available in Google Sheets only. Excel has no ISDATE function, so use the closest alternative shown in Platform Differences.

## Syntax

```excel
=ISDATE(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISDATE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value to test. Put date text in quotation marks, or pass a cell reference such as `A2`. |

### Return Value

TRUE when the value is a date that Google Sheets can read. FALSE for text that is not a date, a month name without a day and year, an impossible date, or other content.

## Examples

### Example 1: Full Date Text

```excel
=ISDATE("July 20 1969")
```

**Result:** `TRUE`

The text includes a month, a day and a year, which makes it a complete date.

### Example 2: Month Name Only

```excel
=ISDATE("July")
```

**Result:** `FALSE`

A month name does not identify a single day, so the test returns FALSE.

### Example 3: Impossible Date

```excel
=ISDATE("Feb 30")
```

**Result:** `FALSE`

February has no 30th day, so the value is not a valid date.

### Example 4: Cell That Holds a Date

Cell A2 holds a date entered as a date value, 15 March 2025.

```excel
=ISDATE(A2)
```

**Result:** `TRUE`

A cell reference is tested as the value in the cell, so a real date returns TRUE.

<!-- Image 2: Date Text Check Results. See Images/Information/ISDATE.md -->

### Example 5: Flagging a Bad Entry

Cell A3 holds the text `Feb 30`.

```excel
=IF(ISDATE(A3), "Valid date", "Fix date")
```

**Result:** `Fix date`

The IF formula gives the user a clear message to correct the entry.

## Story Problems

### Problem 1: Checking Shipping Dates in an Import

A supplier file sends ship dates as text. Some entries are complete and some are not.

| Order | Ship Date |
| --- | --- |
| 1001 | March 4 2025 |
| 1002 | Feb 30 2025 |
| 1003 | June |
| 1004 | May 9 2025 |

**Task:** Put `=ISDATE(B2)` in C2, fill it down to row 5, and count the TRUE results in C2:C5.

**Solution:**

```excel
=COUNTIF(C2:C5, TRUE)
```

**Answer:** `2`. Orders 1001 and 1004 are complete dates. Order 1002 is an impossible date and order 1003 is a month name only.

### Problem 2: Routing Rows With Bad Dates

A calendar column in A2:A4 holds `July 20 1969`, `July` and `Feb 30`. The team wants a label next to each entry.

**Task:** Put a formula in B2 that returns `Date` when A2 is a date and `Not a date` otherwise, then fill it down to row 4.

**Solution:**

```excel
=IF(ISDATE(A2), "Date", "Not a date")
```

**Answer:** Row 2 shows `Date`. Rows 3 and 4 show `Not a date`, so two entries need correction.

## Use Cases

### Date Column Validation

**Scenario:** A project tracker accepts start dates typed by many people, and the schedule formulas fail when a start date is text that is not a real date.

```excel
=IF(ISDATE(D2), "OK", "Check start date")
```

**Why It Works:** The label flags each row before the schedule formulas run, so the owner can fix the entry at its source.

### Import Date Checks

**Scenario:** A nightly import brings in order dates as text, and the team wants to route bad rows to a review sheet.

```excel
=IF(ISDATE(B2), "OK", "Review")
```

**Why It Works:** Filling the formula down gives each row a label, so the team can filter the sheet for `Review` and fix those orders before the import is used.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| FALSE for a month name | `July` alone does not identify a day and year. | Enter the full date. |
| FALSE for an impossible date | The day does not exist in that month. | Correct the source value. |
| Unexpected result for a locale | Date text is read with the sheet's locale settings. | Match the sheet locale or build dates with DATE. |
| FALSE for an accepted-looking format | The exact formats are not all documented. | Test the format in the sheet before you rely on the result. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Closest alternative: `=ISNUMBER(DATEVALUE(A2))`, which returns TRUE when Excel can read the text as a date. |
| Google Sheets | Available | Tests whether text or a cell value is a date. The exact accepted formats are not fully listed. |

## Tips and Best Practices

- Run ISDATE on a sample of real values before you build a long validation chain.
- Use ISNUMBER when a cell should already hold a real date value.
- Combine ISDATE with IF to return a message rather than a bare TRUE or FALSE.
- Build dates from parts with DATE when the source values are reliable, because that avoids text parsing.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATEVALUE](../Date%20%26%20Time/DATEVALUE.md) | Converts date text to a date serial number. |
| [ISBLANK](ISBLANK.md) | Tests whether a cell is empty. |
| [ISEMAIL](ISEMAIL.md) | Tests whether text has the shape of an email address. |
| [ISNUMBER](ISNUMBER.md) | Tests whether a value is a number, including a real date value. |
| [ISTEXT](ISTEXT.md) | Tests whether a value is text, such as a date typed as words. |

## Official Documentation

- [Google Docs Editors Help: ISDATE](https://support.google.com/docs/answer/9061381)
