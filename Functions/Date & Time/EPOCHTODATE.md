---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Construction
purpose:
  - Data Import
  - Date Calculation
use-case:
  - Analytics Export Dates
  - API Log Timestamps
  - Event Timestamps
related:
  - DATE
  - DATEVALUE
  - NOW
  - TIME
  - TODAY
  - VALUE
level: 3
source:
  - https://support.google.com/docs/answer/13193461
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Epoch To Date
  - Unix Time To Date
tags:
  - date-conversion
  - epoch-time
  - sheets
  - timestamp
---

# EPOCHTODATE

## Description

**EPOCHTODATE** converts a Unix epoch timestamp into a date and time. A Unix timestamp counts the time since midnight on January 1, 1970 in Coordinated Universal Time (UTC), and many APIs, logs and analytics exports store dates in this form. The function accepts a timestamp in seconds, milliseconds or microseconds, selected by the optional `unit` argument, and it returns the date and time in UTC.

Use EPOCHTODATE whenever a column holds numbers such as `1700000000000` that are clearly too large to be dates. Without the function, those numbers would display as very large values. The result is in UTC, not in the spreadsheet's local time zone, so convert it with a time offset if your reports use local time.

EPOCHTODATE is a Google Sheets function. Excel does not have an equivalent, so the Platform Differences section shows the Excel formula that does the same job.

## Syntax

```excel
=EPOCHTODATE(timestamp, [unit])
```

<!-- Image 1: Timestamp Units. See Images/Date & Time/EPOCHTODATE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `timestamp` | Yes | The Unix epoch number. Negative timestamps are not accepted. Fractional milliseconds are shortened. |
| `unit` | No | The unit of the timestamp: `1` for seconds (the default), `2` for milliseconds, or `3` for microseconds. |

### Return Value

A date and time in UTC. The result is a date value that can be formatted, compared and used in other date functions. Negative timestamps are not accepted.

## Examples

### Example 1: Seconds, the Default Unit

```excel
=EPOCHTODATE(1700000000)
```

**Result:** `11/14/2023 22:13:20`, in UTC

The default unit is seconds, so no second argument is needed.

### Example 2: Milliseconds

```excel
=EPOCHTODATE(1700000000000, 2)
```

**Result:** `11/14/2023 22:13:20`, in UTC

The same moment in time is written as 1,700,000,000,000 milliseconds, so unit 2 is required.

<!-- Image 2: Same Moment in Three Units. See Images/Date & Time/EPOCHTODATE.md -->

### Example 3: Microseconds

```excel
=EPOCHTODATE(1700000000000000, 3)
```

**Result:** `11/14/2023 22:13:20`, in UTC

A microsecond timestamp has six more digits than the seconds value, and unit 3 makes the conversion exact.

### Example 4: Epoch Zero Plus One Day

```excel
=EPOCHTODATE(86400)
```

**Result:** `1/2/1970 0:00:00`, in UTC

One day is 86,400 seconds, so the timestamp lands on January 2, 1970 at midnight UTC.

## Story Problems

### Problem 1: Reading API Log Entries

An application writes the time of each request as milliseconds since the epoch. The support team needs the request times in readable UTC form.

| Request | Timestamp (ms) |
| --- | --- |
| R-4410 | 1700000000000 |

**Task:** Return the request time in `B2` as a date and time, using the millisecond unit.

**Solution:**

```excel
=EPOCHTODATE(A2, 2)
```

**Answer:** `11/14/2023 22:13:20` UTC. The millisecond unit must be given, or the value is read as seconds and produces a date far in the future or an error.

### Problem 2: Export File Timestamps

A report export stores its creation time in seconds since the epoch. The analyst wants the time in UTC and in Excel, which lacks EPOCHTODATE.

| Export | Timestamp (seconds) |
| --- | --- |
| Q2-Sales | 1650000000 |

**Task:** Return the time in Sheets with EPOCHTODATE, then give the Excel serial number for the same moment.

**Solution:**

```excel
=EPOCHTODATE(A2)
=A2 / 86400 + DATE(1970, 1, 1)
```

**Answer:** April 15, 2022 at 05:20:00 UTC in Sheets. In Excel the second formula gives the serial number 44666.2222, which displays as the same date and time.

## Use Cases

### API Log Timestamps

**Scenario:** A support team searches API logs that store request times in milliseconds, and it needs the request date for each row.

```excel
=EPOCHTODATE(B2, 2)
```

**Why It Works:** The unit argument tells the function that B2 is in milliseconds. The result is a real date that filters and sorts as expected.

### Analytics Export Dates

**Scenario:** An analytics tool exports event times as seconds, and a team wants the daily count of events.

```excel
=TEXT(EPOCHTODATE(A2), "yyyy-mm-dd")
```

**Why It Works:** EPOCHTODATE converts the timestamp, and TEXT formats the date as a label for a pivot table or a daily count.

### Converting to Local Time

**Scenario:** A regional office reports in UTC+2 and needs the event times shifted from UTC.

```excel
=EPOCHTODATE(A2) + 2/24
```

**Why It Works:** EPOCHTODATE returns UTC. Adding 2 hours, expressed as 2/24 of a day, moves the time to UTC+2. Change the number to match the office's offset.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Date far in the future | A millisecond or microsecond value was read as seconds. | Pass the correct unit: 2 for milliseconds or 3 for microseconds. |
| Unexpected time | The result is in UTC, not local time. | Add the offset for your time zone. |
| Error | A negative timestamp was passed. | Check the source data, because negative timestamps are not accepted. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | No epoch function. Use `=A2 / 86400 + DATE(1970, 1, 1)` for seconds, or `=A2 / 86400000 + DATE(1970, 1, 1)` for milliseconds. The result is a UTC serial number. |
| Google Sheets | Available | Units 1 (seconds, default), 2 (milliseconds) and 3 (microseconds). The result is in UTC. |

## Tips and Best Practices

- Always pass the unit when the timestamp is not in seconds, because the wrong unit gives a date far from the expected one.
- Keep the raw timestamp column beside the converted column, so you can check the conversion.
- Convert to local time only when the report needs it, and document the offset you used.
- Use the Excel formula from Platform Differences when a workbook must open in Excel.
- Check that timestamps are not negative before converting, because the function does not accept them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds a date from parts, and is the building block of the Excel alternative. |
| [DATEVALUE](DATEVALUE.md) | Converts a date written as text, the other common input to date functions. |
| [NOW](NOW.md) | Returns the current date and time, for comparing against converted timestamps. |
| [TIME](TIME.md) | Builds a time value from hour, minute and second parts. |
| [TODAY](TODAY.md) | Returns the current date, for filtering converted timestamps to today. |
| [VALUE](../Text/VALUE.md) | Converts text that holds a number, such as an exported timestamp, into a number. |

## Official Documentation

- [Google Docs Editors Help: EPOCHTODATE](https://support.google.com/docs/answer/13193461)
