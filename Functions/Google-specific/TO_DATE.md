---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Parser Functions
purpose:
  - Date Calculation
  - Number Formatting
use-case:
  - Export Date Cleanup
  - Sensor Timestamp Conversion
  - Shipment Date Reports
related:
  - DATE
  - DATEVALUE
  - N
  - TO_PURE_NUMBER
  - TO_TEXT
level: 2
source:
  - https://support.google.com/docs/answer/3094239
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Number To Date
  - Serial To Date
tags:
  - conversion
  - dates
  - serial-numbers
  - sheets
---

# TO_DATE

## Description

**TO_DATE** converts a number into a date. Google Sheets stores every date as a serial number, the count of days since December 30, 1899, and a fraction of a day for the time. When a system exports dates as plain numbers such as `45658`, TO_DATE tells Sheets to display that number as a date and time.

Use TO_DATE when a column of numbers should look like dates, for example after importing a file from a system that writes serial numbers. A whole number becomes a date at midnight, and a decimal part adds the time of day. A negative number is a date before December 30, 1899.

TO_DATE only works on numbers. If the input is text, the function returns it unchanged, so `"2025-03-15"` stays text. To turn a date string into a date, use DATEVALUE. To build a date from separate year, month and day values, use DATE. TO_DATE is the reverse of showing a date as a number, which you can do with N.

## Syntax

```excel
=TO_DATE(value)
```

<!-- Image 1: Serial Number Versus Date Display. See Images/Google-specific/TO_DATE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The number, or a reference to a cell that holds a number, to show as a date. A fraction adds the time of day. Non-numeric input is returned unchanged. |

### Return Value

A date, or a date and time when the input has a fractional part. If the input is not numeric, the function returns that input unchanged instead of an error. The official documentation does not list error values or numeric limits for TO_DATE.

## Examples

Each example is a separate formula. Example 2 uses the serial number in cell `A2`.

### Example 1: Whole Number of Days

```excel
=TO_DATE(45658)
```

**Result:** `1/1/2025` (displayed as a date)

The number 45658 is 45,658 days after December 30, 1899, which is January 1, 2025.

### Example 2: Serial Number From a Cell

```excel
=TO_DATE(A2)
```

**Result:** `1/6/2025` when `A2` holds `45663`

The function reads the number in the cell and displays it as a date. The cell with the formula is the one that changes format, and `A2` keeps its number.

### Example 3: Number With a Time of Day

```excel
=TO_DATE(45658.4375)
```

**Result:** `1/1/2025 10:30 AM` (displayed as a date and time)

The fraction 0.4375 is 10.5 hours of a day, so the result includes 10:30 AM.

<!-- Image 2: Serial Number Versus Date Display, Time Example. See Images/Google-specific/TO_DATE.md -->

### Example 4: A Date Before 1900

```excel
=TO_DATE(-1)
```

**Result:** `12/29/1899` (displayed as a date)

Negative numbers count backward from December 30, 1899, so -1 is the day before.

### Example 5: Text Input Returned Unchanged

```excel
=TO_DATE("2025-03-15")
```

**Result:** `2025-03-15` (still text, not a date)

Because the input is text, TO_DATE returns it as it was. Use DATEVALUE to convert text like this into a date.

## Story Problems

### Problem 1: Latest Shipment Date

A warehouse export lists four shipment dates as serial numbers in `B2:B5`. The manager needs the date of the most recent shipment.

| Order | Ship Serial |
| --- | --- |
| O-101 | 45658 |
| O-102 | 45663 |
| O-103 | 45672 |
| O-104 | 45689 |

**Task:** Find the latest shipment and show it as a date in `D2`.

**Solution:**

```excel
=TO_DATE(MAX(B2:B5))
```

**Answer:** `2/1/2025`. The largest serial, 45689, is order O-104, which is February 1, 2025.

<!-- Image 3: Latest Shipment Date Result. See Images/Google-specific/TO_DATE.md -->

### Problem 2: Sensor Reading Time

A temperature sensor logs each reading as a serial number with the time in the decimal part. The reading in `B2` is `45658.8125`.

**Task:** Show the date and time of the reading in `C2`.

**Solution:**

```excel
=TO_DATE(B2)
```

**Answer:** January 1, 2025 at 7:30 PM. The fraction 0.8125 is 19.5 hours, which is 7:30 PM.

## Use Cases

### Export Date Cleanup

**Scenario:** A billing system exports invoice dates as plain numbers, and the finance team needs them to sort and filter as dates.

```excel
=TO_DATE(B2:B500)
```

**Why It Works:** Sheets applies the date display to each result. Check that the input column holds numbers and not text, because text comes back unchanged.

### Sensor Timestamp Conversion

**Scenario:** A monitoring device writes readings as serial numbers with the time of day after the decimal point.

```excel
=TO_DATE(C2)
```

**Why It Works:** The fraction carries the time, so one formula shows both the date and the time without splitting the value into parts.

### Shipment Date Reports

**Scenario:** A summary sheet shows the most recent shipment date for each warehouse, and the source data arrives as serial numbers.

```excel
=TO_DATE(MAX(Shipments!B2:B500))
```

**Why It Works:** MAX finds the largest serial number, which is the latest date, and TO_DATE displays it as a date.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Input comes back unchanged | The value is text, such as `"2025-03-15"`. | Convert the text with DATEVALUE, or build the date with DATE. |
| Result is a tiny decimal such as `0.0005` | A date typed with slashes, such as `10/10/2000`, is calculated as division. | Enter the date as text with DATEVALUE, or use DATE with separate parts. |
| Dates are off by about four years | The source file uses the 1904 date system from some older spreadsheet files, which counts from a different start date. | Check the source system, and subtract 1,462 days from its serial numbers before converting. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Format the cell as a date, or use DATE to build a date from year, month and day. |
| Google Sheets | Available | Displays a number as a date and time. Non-numeric input is returned unchanged. |

## Tips and Best Practices

- Check that the input is numeric with ISNUMBER before converting a column.
- Use DATEVALUE for text dates and TO_DATE for serial numbers, so each formula matches the type of data it receives.
- Keep the original numbers in one column and the converted dates in another, so you can check the conversion.
- Give the time part its own cell if you need to total hours, because a time fraction is easy to misread as a date.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](../Date%20%26%20Time/DATE.md) | Builds a date from year, month and day values. |
| [DATEVALUE](../Date%20%26%20Time/DATEVALUE.md) | Converts a date written as text into a date. |
| [N](../Information/N.md) | Returns a date's serial number, the reverse of TO_DATE. |
| [TO_PURE_NUMBER](TO_PURE_NUMBER.md) | Removes date formatting from a value and returns its serial number. |
| [TO_TEXT](TO_TEXT.md) | Converts a number to text while keeping its format. |

## Official Documentation

- [Google Docs Editors Help: TO_DATE](https://support.google.com/docs/answer/3094239)
