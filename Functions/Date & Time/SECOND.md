---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Time Values
purpose:
  - Time Calculation
use-case:
  - Call Duration Analysis
  - Dispatch Log Review
  - Timestamp Validation
related:
  - HOUR
  - MINUTE
  - MOD
  - NOW
  - TIME
  - TIMEVALUE
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/second-function
  - https://support.google.com/docs/answer/3093054
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Second Of Time
  - Extract Second
tags:
  - excel
  - sheets
  - time
  - time-component
  - time-extraction
---

# SECOND

## Description

**SECOND** returns the seconds component of a time as an integer from 0 to 59. It ignores the hour and the minute, so 7:12:45 AM returns 45 and 2:03:00 PM returns 0. Use it when a log, timestamp or duration must be checked to the second.

Spreadsheets store a time as a fraction of a day, and SECOND reads that fraction and converts it back to seconds. A value typed as a time, a result from TIME or TIMEVALUE, and a date-time value from NOW all work as input. A date entered without a time portion counts as 0:00:00, so SECOND returns 0 for it.

SECOND returns only the seconds part of a time. A duration such as 0:04:12 has a seconds component of 12, not a total of 252 seconds. To find the total seconds in a duration, multiply it by 86400.

## Syntax

```excel
=SECOND(serial_number)
```

<!-- Image 1: Syntax Anatomy. See Images/Date & Time/SECOND.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `serial_number` | Yes | The time or date-time that contains the seconds. It can be a cell that holds a time, a function result such as TIME or TIMEVALUE, or a decimal number that represents a time of day. |

### Return Value

An integer from 0 to 59 that is the seconds portion of the time. Text that cannot be read as a time produces `#VALUE!` in Excel.

## Examples

### Example 1: Seconds From a Time Cell

```excel
=SECOND(A2)
```

**Result:** `45` (when A2 contains 7:12:45 AM)

The function returns the seconds value stored in the time and ignores the hour and minute.

### Example 2: Seconds From the TIME Function

```excel
=SECOND(TIME(11,40,59))
```

**Result:** `59`

TIME builds 11:40:59 AM, and SECOND returns the last part of that time.

### Example 3: Seconds From a Text Time

```excel
=SECOND(TIMEVALUE("20:49:59"))
```

**Result:** `59`

TIMEVALUE converts the text to a time value first. Passing a raw text string to SECOND is less reliable in Google Sheets, so converting it first is the safer pattern.

### Example 4: Seconds Above 59 From TIME

```excel
=SECOND(TIME(0,0,125))
```

**Result:** `5`

TIME rolls 125 seconds into 2 minutes and 5 seconds, so SECOND returns 5.

### Example 5: Minutes and Seconds as Text

```excel
=MINUTE(A2)&":"&TEXT(SECOND(A2),"00")
```

**Result:** `12:45` (when A2 contains 7:12:45 AM)

Pairing SECOND with MINUTE rebuilds the mm:ss part of a time. The "00" format keeps a leading zero, so 0 seconds shows as 00 rather than 0.

## Story Problems

### Problem 1: Dispatch Timestamps

A dispatch center records four timestamps in column A. Supervisors review any entry whose seconds value is 30 or more, because those entries were logged late in the minute.

| Timestamp |
| --- |
| 2:02:15 PM |
| 2:02:58 PM |
| 2:03:07 PM |
| 2:03:44 PM |

**Task:** Count the timestamps whose seconds value is 30 or more.

**Solution:**

```excel
=SUMPRODUCT(--(SECOND(A2:A5)>=30))
```

**Answer:** `2`. The entries at 2:02:58 PM and 2:03:44 PM have seconds of 58 and 44. The other two entries have seconds of 15 and 7.

<!-- Image 2: Timestamp Component Split. See Images/Date & Time/SECOND.md -->

### Problem 2: Odd Call Durations

Each row in column B holds a call length in hours, minutes and seconds, such as 0:04:12 for four minutes and twelve seconds. The quality team wants the number of calls whose seconds component is odd.

| Duration |
| --- |
| 0:04:12 |
| 0:00:58 |
| 0:12:30 |
| 0:02:05 |

**Task:** Count the durations whose seconds component is odd.

**Solution:**

```excel
=SUMPRODUCT(--(MOD(SECOND(B2:B5),2)=1))
```

**Answer:** `1`. Only 0:02:05 has an odd seconds value (5). The seconds of the other three durations are 12, 58 and 30, which are all even.

## Use Cases

### Call Duration Checks

**Scenario:** A call center exports durations as times. Reports need a rule that flags any call whose seconds value is above 50, because those calls were usually rounded up in the phone system.

```excel
=IF(SECOND(B2)>50,"Review","OK")
```

**Why It Works:** SECOND isolates the seconds part of the duration, so the comparison runs on that single component. The formula does not depend on the length of the call, so it works the same for a 30-second call and a 20-minute call.

### Splitting a Timestamp Into Columns

**Scenario:** A logging system writes timestamps as one value, but an analysis sheet needs hours, minutes and seconds in separate columns.

```excel
=HOUR(A2)
=MINUTE(A2)
=SECOND(A2)
```

**Why It Works:** Each function reads a different component of the same time value, so one timestamp in column A produces three numeric columns that can be sorted, filtered or averaged.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text that Excel cannot read as a time. | Convert the text with TIMEVALUE or re-enter the time. |
| Always 0 | The cell holds a date with no time portion. | Confirm the source column includes times. |
| Wrong result for a total duration | SECOND returns only the seconds part of the time. | Multiply the duration by 86400 to get the total seconds. |
| Unexpected value after rounding | A time such as 2:59:59.999 is displayed as 3:00:00 but stored with a fraction. | Round the time with ROUND(A2*86400,0)/86400 before extracting the seconds. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Accepts text times in quotation marks as well as numbers and cell references. |
| Google Sheets | Available | Takes a cell reference, a function result or a number. Text times are more reliable after TIMEVALUE. |

## Tips and Best Practices

- Use SECOND with MINUTE and HOUR to rebuild or split a time without losing precision.
- Convert text times with TIMEVALUE before extracting parts, so that the same formula works in both Excel and Google Sheets.
- Multiply a duration by 86400 when you need its total seconds.
- Use TEXT with "00" when you display seconds in a label, so that 5 seconds shows as 05.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MINUTE](MINUTE.md) | Returns the minute component. Use it with SECOND to read a full mm:ss value. |
| [HOUR](HOUR.md) | Returns the hour component of the same time. |
| [TIME](TIME.md) | Builds a time from hour, minute and second values, the reverse of SECOND. |
| [TIMEVALUE](TIMEVALUE.md) | Converts text such as "20:49:59" to a time value that SECOND can read. |
| [NOW](NOW.md) | Returns the current date and time, including a seconds value. |
| [MOD](../Math%20%26%20Trig/MOD.md) | Tests parity or interval alignment of the seconds value. |

## Official Documentation

- [Microsoft Support: SECOND function](https://support.microsoft.com/en-us/excel/functions/second-function)
- [Google Docs Editors Help: SECOND](https://support.google.com/docs/answer/3093054)
