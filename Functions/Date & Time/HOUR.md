---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Time Values
purpose:
  - Time Calculation
use-case:
  - Call Center Staffing
  - Clinic Check-In Reports
  - Shift Scheduling
related:
  - MINUTE
  - NOW
  - SECOND
  - TIME
  - TIMEVALUE
  - TODAY
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/hour-function
  - https://support.google.com/docs/answer/3093045
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Extract Hour
  - Hour Of Day
tags:
  - excel
  - hour
  - sheets
  - time-component
  - time-extraction
---

# HOUR

## Description

**HOUR** returns the hour part of a time, as a whole number from 0 to 23. It reads the time portion of a date and time value, so 6:45 PM returns 18 and 12:00 AM returns 0. Use it to group events by hour, to find which shift a start time belongs to, or to build hour-level reports from time stamps.

Times are stored as fractions of a day. Noon is 0.5, and 7:30 AM is 0.3125. HOUR reads that fraction and returns the whole hours, so minutes and seconds are dropped rather than rounded. A date with no time part returns 0.

HOUR works best on real time values. Use the TIME function to build a time from its parts, or put a time in quotation marks, such as `"6:45 PM"`, when you write it directly in a formula. A bare time typed into a formula without quotation marks is not converted, and Excel returns an error for it.

## Syntax

```excel
=HOUR(serial_number)
```

<!-- Image 1: Time Value to Hour. See Images/Date & Time/HOUR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `serial_number` | Yes | The time to read. Use a cell that holds a time or a date and time, a function such as TIME or NOW, a decimal number, or a time in quotation marks. |

### Return Value

A whole number from 0 to 23. The value is 0 for midnight through 12:59 AM, and 23 for 11:00 PM through 11:59 PM. Minutes and seconds are not included in the result.

## Examples

### Example 1: Hour From a Time Cell

```excel
=HOUR(A2)
```

**Result:** With A2 holding 7:30 AM, the result is `7`.

The value in A2 is 0.3125 of a day. The whole hours are 7, and the 30 minutes are dropped.

### Example 2: Hour From the TIME Function

```excel
=HOUR(TIME(11, 40, 59))
```

**Result:** `11`

TIME builds 11:40:59, and HOUR returns the hour part. The minutes and seconds do not affect the result.

### Example 3: Hour From Text in Quotation Marks

```excel
=HOUR("20:49:59")
```

**Result:** `20`

A time in quotation marks is converted to a time value before HOUR reads it. Use this form for quick checks when a time is written in the formula.

### Example 4: Hour From a Date and Time

```excel
=HOUR(A2)
```

**Result:** With A2 holding August 4, 2026 at 6:45 PM, the result is `18`.

HOUR reads only the time portion of a date and time value, so the date does not change the result.

<!-- Image 2: Hour Bands on a 24-Hour Clock. See Images/Date & Time/HOUR.md -->

### Example 5: Morning or Afternoon Label

```excel
=IF(HOUR(A2) < 12, "Morning", "Afternoon")
```

**Result:** With A2 holding 2:15 PM, the result is `Afternoon`.

A 24-hour value below 12 is in the morning, so the test separates the two halves of the day.

## Story Problems

### Problem 1: Starting Hour for Each Shift

A warehouse lists three shift start times in `B2:B4`. The planner wants the starting hour of each shift for a staffing chart.

| Shift | Start Time |
| --- | --- |
| Early | 8:45 AM |
| Midday | 12:00 PM |
| Late | 7:30 PM |

**Task:** In column C, return the starting hour of each shift with HOUR.

**Solution:**

```excel
=HOUR(B2)
```

**Answer:** 8 for the early shift, 12 for the midday shift and 19 for the late shift. HOUR drops the 45 minutes and the 30 minutes, so the late shift starts in hour 19.

### Problem 2: Check-In Hours at a Clinic

A clinic records check-in times and needs the hour of each check-in on a 24-hour clock for a demand chart.

| Patient | Check-In |
| --- | --- |
| Patient A | 2:15 PM |
| Patient B | 6:40 PM |

**Task:** Return the 24-hour check-in hour for each patient in column C.

**Solution:**

```excel
=HOUR(B2)
```

**Answer:** 14 for Patient A, because 2:15 PM is 14:15, and 18 for Patient B, because 6:40 PM is 18:40.

## Use Cases

### Call Center Staffing

**Scenario:** A call center logs each call's start time and needs the number of calls handled in each hour for a staffing plan.

```excel
=HOUR(A2)
```

**Why It Works:** Each call gets an hour label from 0 to 23, and COUNTIF on those labels gives the hourly volume. The result is a standard grouping that a pivot table can use directly.

### Clinic Check-In Report

**Scenario:** A clinic checks patients in throughout the day and wants to find the busiest hours in each week.

```excel
=HOUR(B2)
```

**Why It Works:** The hour of each check-in becomes a grouping column. Counting rows by this column shows the peak hours.

### Shift Scheduling

**Scenario:** A payroll team needs to tag every shift that starts during the evening, so it can apply a shift premium.

```excel
=IF(HOUR(B2) >= 18, "Evening Premium", "Standard")
```

**Why It Works:** HOUR returns the start hour, and the comparison flags any shift that begins at 6 PM or later.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text that is not a time. | Use a real time value, TIME, or a time in quotation marks. |
| Error | A bare time such as `12:00:00` was typed into the formula without quotation marks. | Put the time in quotation marks, or use TIME(12, 0, 0). |
| `0` | The value has no time part, or it is exactly midnight. | Check that the cell holds a time, not just a date. |
| Unexpected hour | The value was a date only, or the time was in another time zone. | Confirm the time portion and the time zone of the source data. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns 0 to 23. Accepts text times in quotation marks. A bare time typed in the formula returns an error. |
| Google Sheets | Available | Returns the hour as a whole number from a time value, a date and time value or a time text string. |

## Tips and Best Practices

- Use TIME when building a time from hour, minute and second parts, so the formula does not depend on text.
- Remember that HOUR drops minutes, so use MINUTE if the minute matters.
- Use the 24-hour result to sort or group times, rather than comparing text such as "PM".
- Format helper columns as Number, so an hour label does not display as a time.
- Check the source time zone before grouping, because HOUR reads the stored time as it is.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MINUTE](MINUTE.md) | Returns the minute part of a time, the companion to HOUR. |
| [NOW](NOW.md) | Returns the current date and time, a common input for HOUR. |
| [SECOND](SECOND.md) | Returns the second part of a time. |
| [TIME](TIME.md) | Builds a time from hour, minute and second parts. |
| [TIMEVALUE](TIMEVALUE.md) | Converts a text time into a time value that HOUR can read. |
| [TODAY](TODAY.md) | Returns the current date, which has no time part and therefore returns 0 from HOUR. |

## Official Documentation

- [Microsoft Support: HOUR function](https://support.microsoft.com/en-us/excel/functions/hour-function)
- [Google Docs Editors Help: HOUR](https://support.google.com/docs/answer/3093045)
