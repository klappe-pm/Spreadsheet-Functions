---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Time Values
purpose:
  - Data Cleaning
  - Time Calculation
use-case:
  - Badge Export Cleanup
  - Shift Hours From Text
  - Timestamp Import
related:
  - DATEVALUE
  - HOUR
  - MINUTE
  - NOW
  - TEXT
  - TIME
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/timevalue-function
  - https://support.google.com/docs/answer/3267350
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Text To Time
  - Time From Text
tags:
  - excel
  - import
  - sheets
  - text-conversion
  - time
---

# TIMEVALUE

## Description

**TIMEVALUE** converts a text string that holds a time into a decimal fraction of a day. The text can use a 12-hour format with AM or PM, or a 24-hour format. The result is a number from 0 (12:00:00 AM) to just under 1 (11:59:59 PM), so 12:00 PM returns 0.5.

Use TIMEVALUE when times arrive as text from an export, a web page or a manual entry, and the sheet must subtract, compare or sum them. Text that looks like a time does not behave like one in calculations, so convert it first and then apply the arithmetic to the converted values.

TIMEVALUE ignores any date that appears in the text. A string such as "22-Aug-2011 6:35 AM" returns only the time part, 0.274306. To combine the time with a date, add the result to a date value built with DATE or DATEVALUE.

## Syntax

```excel
=TIMEVALUE(time_text)
```

<!-- Image 1: Syntax Anatomy. See Images/Date & Time/TIMEVALUE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `time_text` | Yes | A text string that holds a time, written in quotation marks or as a reference to a cell that contains such text. Accepted forms include `"2:15 PM"`, `"18:45"` and `"14:15:30"`. A date in the text is ignored. |

### Return Value

A decimal number from 0 to just under 1 that represents the time of day. Text that Excel or Google Sheets cannot read as a time returns `#VALUE!`.

## Examples

### Example 1: Twelve-Hour Time

```excel
=TIMEVALUE("2:15 PM")
```

**Result:** `0.59375`

2:15 PM is 14.25 hours into the day. Dividing by 24 gives 0.59375.

### Example 2: Twenty-Four-Hour Time

```excel
=TIMEVALUE("18:45")
```

**Result:** `0.78125`

18:45 is 18.75 hours into the day, which is 0.78125 of a day.

<!-- Image 2: Accepted Time Text Formats. See Images/Date & Time/TIMEVALUE.md -->

### Example 3: Date and Time in One String

```excel
=TIMEVALUE("22-Aug-2011 6:35 AM")
```

**Result:** `0.274306` (displays as 6:35 AM)

The date part is ignored. Only the time is converted.

### Example 4: Seconds in a Text Time

```excel
=TIMEVALUE("14:15:30")
```

**Result:** `0.594097`

The seconds count as part of the fraction. 14:15:30 is 51,330 seconds into the day, and 51,330 divided by 86,400 is 0.594097.

### Example 5: Reformatting Text Times

```excel
=TEXT(TIMEVALUE(A2),"h:mm AM/PM")
```

**Result:** `7:05 AM` (when A2 contains the text `"7:05"`)

TIMEVALUE turns the text into a time, and TEXT returns a display string in a chosen format. The combination is useful when a report needs a consistent style.

## Story Problems

### Problem 1: Badge Export Hours

A badge system exports clock-in and clock-out times as text. An analyst wants the hours worked for one shift.

| Clock In | Clock Out |
| --- | --- |
| 7:05 AM | 3:40 PM |

**Task:** Convert both text times and calculate the hours between them, rounded to two decimal places.

**Solution:**

```excel
=ROUND((TIMEVALUE(B2)-TIMEVALUE(A2))*24,2)
```

**Answer:** `8.58`. The span from 7:05 AM to 3:40 PM is 8 hours and 35 minutes, which is 8.5833 hours before rounding.

### Problem 2: Latest Punch in a Text Column

A shift log stores three text punches in column C: `"09:30"`, `"9:05 AM"` and `"5:15 PM"`. The supervisor wants the latest of them as a clock reading.

| Punch |
| --- |
| 09:30 |
| 9:05 AM |
| 5:15 PM |

**Task:** Find the latest punch and show it as a 12-hour clock reading.

**Solution:**

```excel
=TEXT(SUMPRODUCT(MAX(TIMEVALUE(C2:C4))),"h:mm AM/PM")
```

**Answer:** `5:15 PM`. The three texts convert to 9:30 AM, 9:05 AM and 5:15 PM, and 5:15 PM is the latest. SUMPRODUCT wraps the array so the formula also works in versions of Excel that need array entry for MAX.

## Use Cases

### Cleaning an Imported Timesheet

**Scenario:** A payroll system exports start times as text in mixed formats. The timesheet needs real time values before totals can be calculated.

```excel
=TIMEVALUE(TRIM(A2))
```

**Why It Works:** TRIM removes stray spaces that often come with exported text, and TIMEVALUE then converts the cleaned string. Wrapping the formula in IFERROR can flag rows that still fail, which keeps bad values visible.

### Converting Shift Lengths

**Scenario:** A staffing sheet lists shift start and end times as text. Managers need the length of each shift in hours.

```excel
=(TIMEVALUE(C2)-TIMEVALUE(B2))*24
```

**Why It Works:** Subtracting two converted times gives the elapsed fraction of a day, and multiplying by 24 turns it into hours. Shifts that cross midnight need extra logic, because the subtraction would be negative.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The text is not in a recognized time format. | Rewrite the text as hh:mm or h:mm AM/PM, or clean it with TRIM and SUBSTITUTE. |
| Negative hours | An overnight shift ends before its start time when subtracted. | Add 1 to the end time when it is less than the start time. |
| Wrong time when a date is present | The date was expected to shift the time. | TIMEVALUE ignores dates, so combine a date and a time with addition. |
| Time looks like a number | The cell is formatted as General or Number. | Format the result cell as a time. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Accepts 12-hour and 24-hour text and ignores any date in the string. |
| Google Sheets | Available | Accepts 12-hour or 24-hour text and returns a fraction of a day. |

## Tips and Best Practices

- Convert text times once in a helper column, then run all arithmetic on the converted values.
- Use TRIM before TIMEVALUE when source data has extra spaces.
- Add 1 to an end time that is earlier than its start time when a shift crosses midnight.
- Use TIMEVALUE with DATEVALUE to build complete date-time values from text exports.
- Check a sample of converted values by eye after each import, because a single bad format can produce a valid but wrong number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATEVALUE](DATEVALUE.md) | Converts a text date to a date value. Use it with TIMEVALUE for full timestamps. |
| [TIME](TIME.md) | Builds a time from numbers rather than text. |
| [HOUR](HOUR.md) | Returns the hour from a time value after conversion. |
| [MINUTE](MINUTE.md) | Returns the minute from a time value after conversion. |
| [NOW](NOW.md) | Returns the current date and time as a value, not as text. |
| [TEXT](../Text/TEXT.md) | Formats a time value as a display string. |

## Official Documentation

- [Microsoft Support: TIMEVALUE function](https://support.microsoft.com/en-us/excel/functions/timevalue-function)
- [Google Docs Editors Help: TIMEVALUE](https://support.google.com/docs/answer/3267350)
