---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Time Values
purpose:
  - Time Calculation
use-case:
  - Appointment Scheduling
  - Call Center Staffing
  - Quarter Hour Reporting
related:
  - HOUR
  - MOD
  - NOW
  - SECOND
  - TIME
  - TIMEVALUE
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/minute-function
  - https://support.google.com/docs/answer/3093048
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Minute Of Time
  - Extract Minute
tags:
  - excel
  - sheets
  - time
  - time-component
  - time-extraction
---

# MINUTE

## Description

**MINUTE** returns the minute component of a time as an integer from 0 to 59. It ignores the hours and the seconds, so 3:27 PM returns 27 and 10:05 AM returns 5. Use it when you need to group or test times by minute, such as checking whether a log entry falls in the first 15 minutes of an hour.

Excel and Google Sheets store a time as a fraction of a day. Noon is 0.5 because it is half of a 24-hour day. MINUTE reads that fraction and converts it to a minute value, so a time typed into a cell, a value returned by TIME or TIMEVALUE, and a date-time value all work as input. A date that has no time portion, such as one made with DATE, has a time of 0:00:00, so MINUTE returns 0 for it.

MINUTE returns only the minute. To rebuild a clock reading, combine it with HOUR and SECOND, or use TEXT with a time format. If you need the total number of minutes between two times, subtract the times and multiply the result by 1440 instead.

## Syntax

```excel
=MINUTE(serial_number)
```

<!-- Image 1: Syntax Anatomy. See Images/Date & Time/MINUTE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `serial_number` | Yes | The time or date-time that contains the minute. It can be a cell that holds a time, a function that returns a time such as TIME or TIMEVALUE, or a decimal number such as 0.5. A text string in quotation marks such as `"18:45"` is also accepted by Microsoft Excel. |

### Return Value

An integer from 0 to 59 that is the minute portion of the time. Text that cannot be read as a time produces `#VALUE!` in Excel.

## Examples

### Example 1: Minute From a Time Cell

```excel
=MINUTE(A2)
```

**Result:** `27` (when A2 contains 3:27 PM)

The function ignores the hour and returns only the minutes part of the stored time.

### Example 2: Minute From the TIME Function

```excel
=MINUTE(TIME(14,5,30))
```

**Result:** `5`

TIME builds 2:05:30 PM, and MINUTE returns 5. The 30 seconds do not affect the result.

### Example 3: Minute From a Text Time

```excel
=MINUTE(TIMEVALUE("18:45"))
```

**Result:** `45`

TIMEVALUE converts the text `"18:45"` to a time value first. MINUTE then reads that value. Passing the raw text straight into MINUTE also works in Microsoft Excel, but converting it first makes the formula's intent clear.

### Example 4: Minute After Adding a Duration

```excel
=MINUTE(A2+TIME(0,50,0))
```

**Result:** `10` (when A2 contains 9:20 AM)

Adding 50 minutes to 9:20 AM gives 10:10 AM. The formula returns the minute of the new time, not the number of minutes added.

### Example 5: Seconds Converted to a Minute Value

```excel
=MINUTE(TIME(0,0,150))
```

**Result:** `2`

TIME accepts 150 seconds and rolls it over into 2 minutes and 30 seconds. MINUTE returns 2.

## Story Problems

### Problem 1: Call Center Quarter-Hour Staffing

A support team logs the time each call arrived in column B. The manager wants to know how many calls arrived in the first 15 minutes of an hour, because that period is staffed by a smaller crew.

| Call | Arrived At |
| --- | --- |
| 1 | 9:04 AM |
| 2 | 9:17 AM |
| 3 | 9:42 AM |
| 4 | 10:05 AM |
| 5 | 10:31 AM |

**Task:** Count the calls whose minute value is less than 15.

**Solution:**

```excel
=SUMPRODUCT(--(MINUTE(B2:B6)<15))
```

**Answer:** `2`. Calls 1 (minute 4) and 4 (minute 5) arrived in the first quarter hour. Calls 2, 3 and 5 arrived at minutes 17, 42 and 31.

<!-- Image 2: Quarter Hour Call Times. See Images/Date & Time/MINUTE.md -->

### Problem 2: Appointments on Quarter Hours

A clinic wants to see which appointments start on a quarter hour (minutes 0, 15, 30 or 45). The schedule is in column A.

| Appointment Time |
| --- |
| 1:00 PM |
| 1:15 PM |
| 1:30 PM |
| 1:52 PM |
| 2:00 PM |

**Task:** Count the appointments that start on a quarter hour.

**Solution:**

```excel
=SUMPRODUCT(--(MOD(MINUTE(A2:A6),15)=0))
```

**Answer:** `4`. The 1:52 PM appointment has minute 52, and 52 divided by 15 leaves a remainder of 7, so it is excluded. The other four start at minutes 0, 15, 30 and 0 of the next hour.

## Use Cases

### Quarter Hour Reporting

**Scenario:** A plant logs machine stops with timestamps and needs a count of stops that began in each quarter of the hour.

```excel
=INT(MINUTE(A2)/15)+1
```

**Why It Works:** Dividing the minute by 15 and taking the integer part gives 0, 1, 2 or 3 for the four quarters. Adding 1 gives a quarter number from 1 to 4 that can drive a COUNTIFS or a pivot table.

### Rounding Times to the Nearest Five Minutes

**Scenario:** Timesheet entries are recorded to the second, but payroll rounds each punch to the nearest five minutes.

```excel
=TIME(HOUR(A2),ROUND(MINUTE(A2)/5,0)*5,0)
```

**Why It Works:** MINUTE supplies the minute, ROUND moves it to the nearest multiple of 5 through the step count, and TIME rebuilds the time. A value of 60 from a minute close to 58 rolls over to the next hour, because TIME converts minutes above 59 correctly.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text that Excel cannot read as a time. | Convert the text with TIMEVALUE or re-enter it as a time. |
| Always 0 | The cell holds a whole date with no time portion. | Check that the source column contains a time or a date-time value. |
| Wrong minute from text such as `"12:00:00"` | Google Sheets does not convert some time text the way direct entry does. | Wrap the text in TIMEVALUE before passing it to MINUTE. |
| Unexpected value after adding time | The result crossed an hour boundary, so the minute restarted. | Use the full date-time value in comparisons instead of the minute alone. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Accepts text times in quotation marks as well as numbers and cell references. |
| Google Sheets | Available | Takes a cell reference, a function result or a number. Text input may need TIMEVALUE. |

## Tips and Best Practices

- Use MINUTE with HOUR and SECOND to test a time against a full clock threshold, for example HOUR(A2)*60+MINUTE(A2).
- Keep source times as true time values. Text times that look correct often return errors or the wrong component.
- Use MOD(MINUTE(A2),15) to test quarter-hour alignment rather than writing several equality tests.
- Subtract two times and multiply by 1440 to find the total minutes between them, because MINUTE ignores the hour.

## Related Functions

| Function | Relationship |
| --- | --- |
| [HOUR](HOUR.md) | Returns the hour component. Use it with MINUTE to compare times on a clock basis. |
| [SECOND](SECOND.md) | Returns the seconds component. Use it when precision to the second matters. |
| [TIME](TIME.md) | Builds a time from hour, minute and second values, the reverse of MINUTE. |
| [TIMEVALUE](TIMEVALUE.md) | Converts text such as "18:45" to a time value that MINUTE can read. |
| [NOW](NOW.md) | Returns the current date and time, which MINUTE can read directly. |
| [MOD](../Math%20%26%20Trig/MOD.md) | Tests quarter-hour or interval alignment of the minute value. |

## Official Documentation

- [Microsoft Support: MINUTE function](https://support.microsoft.com/en-us/excel/functions/minute-function)
- [Google Docs Editors Help: MINUTE](https://support.google.com/docs/answer/3093048)
