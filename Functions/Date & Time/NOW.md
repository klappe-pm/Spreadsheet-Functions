---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Time Values
purpose:
  - Time Calculation
use-case:
  - Current Timestamp Display
  - Deadline Countdown
  - Elapsed Time Tracking
related:
  - HOUR
  - MINUTE
  - SECOND
  - TEXT
  - TIME
  - TODAY
  - WORKDAY
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/now-function
  - https://support.google.com/docs/answer/3092981
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Current Date and Time
  - Current Timestamp
tags:
  - current-time
  - excel
  - sheets
  - time
  - volatile
---

# NOW

## Description

**NOW** returns the current date and time as a single serial number. The whole number part holds the date, and the decimal part holds the time of day. A value of 0.5 is noon, so 46000.75 would represent 6:00 PM on the day with serial number 46000. Format the cell as a date and time to read it, or leave it as a number to use it in arithmetic.

NOW takes no arguments, but the parentheses are required. Its value changes whenever the spreadsheet recalculates, which in Excel happens on most edits, on a manual recalculation and when a workbook is opened. It does not tick every second. A formula that uses NOW therefore shows the time of the last recalculation, not the moment the cell was typed.

Because the value keeps changing, NOW is not a reliable timestamp for a log entry. A cell that records when a row was completed should be filled with a static value, either by pasting values or by a script. NOW is best used for live displays, elapsed time and countdowns, where a changing value is the goal. For the date alone, use TODAY.

## Syntax

```excel
=NOW()
```

<!-- Image 1: Syntax Anatomy. See Images/Date & Time/NOW.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| *(none)* | No | NOW takes no arguments. The empty parentheses must still be typed. |

### Return Value

A decimal serial number for the current date and time. The integer part is the number of days since the spreadsheet's date origin, and the fraction is the time of day. Microsoft's documentation gives an example: serial number 45658 is January 1, 2025, so a value of 45658.5 is noon on that date.

## Examples

### Example 1: Current Date and Time

```excel
=NOW()
```

**Result:** the current date and time, shown in the cell's format (for example, `11/22/2026 2:05 PM`). The stored value changes with each recalculation.

Apply a date and time format to the cell. Without a format, the cell may show a serial number.

### Example 2: Date Part Only

```excel
=INT(NOW())
```

**Result:** the current date as a serial number, which displays as today's date

INT removes the decimal part, which holds the time, and leaves only the date. The result matches TODAY.

### Example 3: Time Part Only

```excel
=NOW()-INT(NOW())
```

**Result:** the current time as a fraction of a day, which displays as a time such as 2:05 PM when formatted as a time

Subtracting the date part leaves the time fraction. Format the cell as a time to read it.

<!-- Image 2: Serial Number Anatomy. See Images/Date & Time/NOW.md -->

### Example 4: Hours Until a Deadline

```excel
=(A2-NOW())*24
```

**Result:** the number of hours from now until the date and time in A2, which is negative once that moment has passed

Subtracting two date-time values gives days, so multiply by 24 to convert the difference to hours. A deadline 36 hours away returns 36.

### Example 5: Time 30 Minutes From Now

```excel
=NOW()+TIME(0,30,0)
```

**Result:** the current date and time plus 30 minutes

TIME(0,30,0) is the fraction of a day that equals 30 minutes, so adding it moves the value forward by half an hour. The same approach works with any number of hours or minutes.

## Story Problems

### Problem 1: Parking Garage Timer

A parking garage records the time a car entered and left. The garage bills by the hour and rounds the stay to two decimal places.

| Entry | Exit |
| --- | --- |
| 2026-11-22 08:15 | 2026-11-22 17:40 |

**Task:** Calculate the length of the stay in hours, rounded to two decimal places.

**Solution:**

```excel
=ROUND((B2-A2)*24,2)
```

**Answer:** `9.42`. The stay is 9 hours and 25 minutes, which is 9.4167 hours before rounding. The formula works with fixed times, so the result does not change when the sheet is reopened.

### Problem 2: Open Support Ticket Age

A help desk shows how long each ticket has been open. The age in column C depends on the current time, so the exact value cannot be fixed in this guide.

| Ticket | Opened |
| --- | --- |
| 1042 | 2026-11-22 09:30 |

**Task:** Show the hours each ticket has been open as of the moment the sheet is viewed.

**Solution:**

```excel
=ROUND((NOW()-B2)*24,1)
```

**Answer:** The result is the hours between 9:30 AM on November 22, 2026 and the time the sheet is calculated. It is not a fixed number. Opening the sheet at 11:00 AM would show 1.5 hours, and each later recalculation shows a larger value.

## Use Cases

### Dashboard Refresh Stamp

**Scenario:** An operations dashboard shows the time its figures were last calculated, so that readers can judge how current the data is.

```excel
="Updated "&TEXT(NOW(),"mmm d, yyyy h:mm AM/PM")
```

**Why It Works:** TEXT turns the current date and time into a readable label that is joined to a fixed prefix. The label refreshes on each recalculation. Because the value is volatile, avoid many copies of NOW in large workbooks. Put the formula in one cell and reference it elsewhere.

### Deadline Countdown

**Scenario:** A grant application closes at a fixed date and time stored in B2. The team wants to show remaining hours and stop at zero once the deadline passes.

```excel
=MAX(0,ROUND((B2-NOW())*24,1))
```

**Why It Works:** Subtracting NOW from the deadline gives the remaining time in days, and multiplying by 24 converts it to hours. MAX keeps the result at zero after the deadline, so the countdown never shows a negative number.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument was entered, or the formula is used in a function that needs a number. | Remove the argument, because NOW takes none. Keep the parentheses. |
| Serial number instead of a date | The cell is still formatted as General or Number. | Apply a date and time format. |
| Timestamp keeps changing | NOW is volatile and updates on recalculation. | Paste the value as static or use a script to record the time. |
| Wrong hour in a shared sheet | The sheet's time zone setting may differ from the local time of the people reading it. | Check File > Settings > Time zone and state the time zone on the sheet. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Recalculates on worksheet changes, manual recalculation and when a macro runs. Serial 1 is January 1, 1900 in the default date system. |
| Google Sheets | Available | Google's NOW reference describes the value as the date and time at the last recalculation and does not describe time zones. Check the time zone under File > Settings and test a =NOW() cell. |

## Tips and Best Practices

- Keep one NOW formula in a single cell, then reference that cell from the rest of the sheet to reduce recalculation.
- Use TODAY instead of NOW when only the date matters.
- Record permanent timestamps as static values, because a formula that contains NOW keeps changing.
- Note the time zone on any sheet that shares NOW values across regions.
- Use ROUND or TEXT to control the decimal places and display of an elapsed-time result.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TODAY](TODAY.md) | Returns only the current date, with no time part. |
| [HOUR](HOUR.md) | Returns the hour of the current time. |
| [MINUTE](MINUTE.md) | Returns the minute of the current time. |
| [SECOND](SECOND.md) | Returns the seconds of the current time. |
| [TIME](TIME.md) | Builds a fixed time to add to or subtract from NOW. |
| [TEXT](../Text/TEXT.md) | Formats the current date and time as a label. |
| [WORKDAY](WORKDAY.md) | Returns a future workday from the current date when the date is also needed. |

## Official Documentation

- [Microsoft Support: NOW function](https://support.microsoft.com/en-us/excel/functions/now-function)
- [Google Docs Editors Help: NOW](https://support.google.com/docs/answer/3092981)
