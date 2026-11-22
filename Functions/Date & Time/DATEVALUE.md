---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Construction
purpose:
  - Data Cleaning
  - Date Calculation
use-case:
  - Converting Imported Dates
  - Dates Stored as Text
  - Legacy System Exports
related:
  - DATE
  - DAY
  - MONTH
  - TIMEVALUE
  - TODAY
  - VALUE
  - YEAR
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/datevalue-function
  - https://support.google.com/docs/answer/3093039
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Convert Text To Date
  - Text To Date
tags:
  - date-conversion
  - excel
  - sheets
  - text-dates
---

# DATEVALUE

## Description

**DATEVALUE** converts a date that is stored as text into a date serial number, which Excel and Google Sheets can then format, compare and calculate with. Use it when an import, a web page or a copy and paste leaves dates as text such as `4/18/2026`. A cell formatted as a date can look right while still holding text, and DATEVALUE is the fix for that case.

The text has to follow a date format the spreadsheet recognizes. Excel accepts formats such as `8/22/2011`, `22-MAY-2011` and `2011/02/23`. Google Sheets accepts any format it would convert if the same text were typed into a cell without quotation marks, and the accepted formats depend on the region and language settings of the spreadsheet.

DATEVALUE ignores any time in the text, so `7/4/2026 18:30` returns the date only. Use TIMEVALUE for the time part. For text that is split into separate year, month and day pieces, DATE with VALUE is more reliable than DATEVALUE because it does not depend on the text layout.

## Syntax

```excel
=DATEVALUE(date_text)
```

<!-- Image 1: Text Date Becomes a Serial Number. See Images/Date & Time/DATEVALUE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `date_text` | Yes | The date as text, either typed in quotation marks or taken from a cell that holds the text. Any time in the text is ignored. |

### Return Value

A date serial number. In Excel's default 1900 date system, the result must fall between January 1, 1900 and December 31, 9999, or the function returns `#VALUE!`. When the text omits the year, Excel uses the current year from the computer's clock.

## Examples

### Example 1: Convert a Text Date

```excel
=DATEVALUE("4/18/2026")
```

**Result:** `46130`, which displays as `4/18/2026` once the cell is formatted as a date.

The text is read as month, day and year. The serial number is the value that DATE and date arithmetic use.

### Example 2: Year First Text

```excel
=DATEVALUE("2026/02/23")
```

**Result:** A serial number for February 23, 2026.

Excel accepts a year-first layout in this form. Test the format in your own locale before using it across a whole column.

### Example 3: Time Is Ignored

```excel
=DATEVALUE("7/4/2026 18:30")
```

**Result:** `46207`, the serial number for July 4, 2026.

The 18:30 part is dropped. Combine this result with TIMEVALUE if you need both parts.

<!-- Image 2: Text Layouts Accepted by DATEVALUE. See Images/Date & Time/DATEVALUE.md -->

### Example 4: Extract the Day From Text

```excel
=DAY(DATEVALUE("3/14/2026"))
```

**Result:** `14`

DATEVALUE turns the text into a serial number, and DAY reads the day from that number. This pattern works for any text date that DATEVALUE accepts.

### Example 5: Trap Bad Text

```excel
=IFERROR(DATEVALUE(A2), "Check date")
```

**Result:** The date serial number when A2 holds a recognized date, or `Check date` when it does not.

Wrap the conversion in IFERROR when a column may hold blank or malformed text, so one bad row does not break the totals below it.

## Story Problems

### Problem 1: Converting Order Dates

A web shop exports order dates as text in column A. The analyst needs the order dates as real dates to sort them by month.

| Order | Order Date (text) |
| --- | --- |
| 1001 | 3/14/2026 |
| 1002 | 2/14/2026 |
| 1003 | 1/30/2026 |

**Task:** Convert the order date in B2 and return the month number of the first order with MONTH.

**Solution:**

```excel
=MONTH(DATEVALUE(B2))
```

**Answer:** `3`. The text 3/14/2026 becomes March 14, 2026, and MONTH returns 3.

### Problem 2: Days Late for a Payment

A utility bill was due on the text date `1/30/2026` and paid on the text date `2/14/2026`. The team needs the number of days the payment was late.

| Bill | Due Date (text) | Paid Date (text) |
| --- | --- | --- |
| Water | 1/30/2026 | 2/14/2026 |

**Task:** Subtract the due date from the paid date after converting both texts with DATEVALUE.

**Solution:**

```excel
=DATEVALUE(C2) - DATEVALUE(B2)
```

**Answer:** `15` days late. January 30 to February 14 is 15 days, because January has 1 day left after the 30th and February 14 adds 14 more.

## Use Cases

### Importing Bank Transactions

**Scenario:** A bank export puts transaction dates in text, and the finance team needs to group the transactions by week.

```excel
=DATEVALUE(A2) - WEEKDAY(DATEVALUE(A2), 2) + 1
```

**Why It Works:** DATEVALUE provides the serial number, and WEEKDAY with type 2 gives the Monday of that week to subtract from the date. The result groups transactions into weeks that start on Monday.

### Cleaning a Legacy Export

**Scenario:** A legacy system writes dates as text, and some rows contain blank cells or malformed values that must be flagged.

```excel
=IF(A2="", "", IFERROR(DATEVALUE(A2), "Invalid"))
```

**Why It Works:** The blank check keeps empty rows empty, and IFERROR marks any text that DATEVALUE cannot read, so the problem rows are easy to filter.

### Matching Text Dates to a Calendar

**Scenario:** A planner has a list of text dates and wants to count how many fall in the current year.

```excel
=SUMPRODUCT(--(YEAR(DATEVALUE(A2:A100)) = YEAR(TODAY())))
```

**Why It Works:** DATEVALUE converts the whole range, YEAR reads each year, and the comparison with TODAY counts matches. Blank or invalid rows return errors, so clean the range first.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The text is not in a recognized date format. | Reformat the text as month/day/year or year/month/day, or use DATE with separate parts. |
| `#VALUE!` | The date is outside 1900 to 9999 (Excel). | Check the source data for a wrong year. |
| `#VALUE!` | The argument is a number, not text (Sheets). | Use the number directly, or convert it with DATE. |
| Wrong month or day | Regional settings read day and month in a different order. | Use a year-first layout, or build the date from separate parts with DATE. |
| Wrong year | The text omits the year, so the current year is used. | Include the four-digit year in the text. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Accepts Excel date formats, ignores time, and returns `#VALUE!` outside 1900 to 9999. Missing years use the current year. |
| Google Sheets | Available | Accepts the date formats Sheets recognizes when typed, which depend on region and language settings. Numeric arguments return `#VALUE!`. |

## Tips and Best Practices

- Test the text format in the same locale as the people who will open the file.
- Use DATE with VALUE on separate parts when the layout of the text is not guaranteed.
- Always include the year in text dates, because a missing year silently uses the current year.
- Wrap conversions in IFERROR when a column may contain blanks or malformed entries.
- Convert a column once into real dates, then delete the text copy, so later formulas do not repeat the conversion.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds a date from separate year, month and day values, which is safer for unusual text layouts. |
| [DAY](DAY.md) | Reads the day from the serial number that DATEVALUE returns. |
| [MONTH](MONTH.md) | Reads the month from the converted date, for grouping. |
| [TIMEVALUE](TIMEVALUE.md) | Converts the time part of a text value, which DATEVALUE ignores. |
| [TODAY](TODAY.md) | Supplies the current date for comparisons with converted dates. |
| [VALUE](../Text/VALUE.md) | Converts text that holds a number, not a date, to a number. |
| [YEAR](YEAR.md) | Reads the year from the converted date. |

## Official Documentation

- [Microsoft Support: DATEVALUE function](https://support.microsoft.com/en-us/excel/functions/datevalue-function)
- [Google Docs Editors Help: DATEVALUE](https://support.google.com/docs/answer/3093039)
