---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Construction
purpose:
  - Time Calculation
use-case:
  - Meeting Schedule Building
  - Shift Length Calculation
  - Time Offset Calculation
related:
  - DATE
  - HOUR
  - MINUTE
  - NOW
  - SECOND
  - TIMEVALUE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/time-function
  - https://support.google.com/docs/answer/3093056
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Build Time
  - Make Time
tags:
  - excel
  - rollover
  - sheets
  - time
  - time-construction
---

# TIME

## Description

**TIME** builds a time value from three separate numbers: an hour, a minute and a second. The result is a decimal fraction of a day, so 12:00 PM is 0.5 and 6:00 AM is 0.25. Format the cell as a time to see a clock reading, or leave it as a number when you want to use it in arithmetic.

TIME is most useful when the hour, minute and second come from other cells or calculations. A shift that starts at 6:30, a meeting that begins at 13:15 plus a 75-minute offset, or a fixed cutoff such as 17:00 can all be built with TIME and then compared, added or subtracted like any other time.

TIME also accepts values outside the normal clock ranges and rolls them over. An hour of 27 becomes 3 AM, and 750 minutes becomes 12 hours and 30 minutes. Microsoft's documentation describes this behavior for each argument from 0 to 32767. Negative inputs are not documented, so avoid them.

## Syntax

```excel
=TIME(hour, minute, second)
```

<!-- Image 1: Syntax Anatomy. See Images/Date & Time/TIME.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `hour` | Yes | A whole number from 0 to 32767. Values above 23 are divided by 24 and the remainder is used as the hour. |
| `minute` | Yes | A whole number from 0 to 32767. Values above 59 are converted into hours and minutes. |
| `second` | Yes | A whole number from 0 to 32767. Values above 59 are converted into minutes, hours and seconds. |

Decimal values are truncated to whole numbers in Google Sheets. Text input returns `#VALUE!`.

### Return Value

A decimal number from 0 (12:00:00 AM) to just under 1 (11:59:59 PM). In Excel, a cell formatted as General changes to a time format after the formula is entered. Text input and references to text return `#VALUE!`.

## Examples

### Example 1: A Plain Time

```excel
=TIME(9,30,0)
```

**Result:** `0.395833` (displays as 9:30 AM when the cell is formatted as a time)

9.5 hours out of 24 is 0.395833, which is the stored value for 9:30 AM.

### Example 2: Hour Above 23

```excel
=TIME(27,0,0)
```

**Result:** `0.125` (displays as 3:00 AM)

The hour 27 is divided by 24, which leaves a remainder of 3. The result is the same as TIME(3,0,0).

### Example 3: Minute Above 59

```excel
=TIME(0,750,0)
```

**Result:** `0.520833` (displays as 12:30 PM)

750 minutes is 12 hours and 30 minutes, so the formula returns 12:30 PM.

### Example 4: Time From Three Cells

```excel
=TIME(A2,B2,C2)
```

**Result:** `0.739815` (displays as 5:45:20 PM) when A2 contains 17, B2 contains 45 and C2 contains 20

The three cell values combine into a single time. The displayed value uses the seconds that the number 0.739815 holds.

### Example 5: Length of a Shift

```excel
=TIME(14,0,0)-TIME(9,15,0)
```

**Result:** `0.197917` (displays as 4:45)

Subtracting two time values gives the elapsed time as a fraction of a day. Multiply by 24 to see the result in hours, which gives 4.75.

## Story Problems

### Problem 1: Warehouse Shift Hours

A warehouse shift starts at 6:30 AM and ends at 2:45 PM. Workers take one unpaid 30-minute break. Payroll wants the paid hours.

| Item | Time |
| --- | --- |
| Shift start | 6:30 AM |
| Shift end | 2:45 PM |
| Unpaid break | 0:30 |

**Task:** Build the shift start, shift end and break with TIME, then calculate the paid hours.

**Solution:**

```excel
=(TIME(14,45,0)-TIME(6,30,0)-TIME(0,30,0))*24
```

**Answer:** `7.75`. The shift is 8 hours and 15 minutes long, and the 30-minute break leaves 7 hours and 45 minutes, which is 7.75 hours.

<!-- Image 2: Shift Timeline With Break. See Images/Date & Time/TIME.md -->

### Problem 2: Meeting Start From Hour and Minute Cells

A scheduling tool stores a meeting's start as an hour in A2 (13) and a minute in B2 (75). The minute value is above 59, so the start time needs to roll over.

| Hour | Minute |
| --- | --- |
| 13 | 75 |

**Task:** Build the start time as a time value and display it as a clock reading.

**Solution:**

```excel
=TIME(A2,B2,0)
```

**Answer:** `0.59375`, which displays as 2:15 PM. Seventy-five minutes after 1:00 PM is 2:15 PM, so the formula carries the extra 60 minutes into the hour.

## Use Cases

### Building Cutoff Times

**Scenario:** An order desk accepts same-day shipments until 3:30 PM. Each order row needs a flag that shows whether its timestamp is before the cutoff.

```excel
=IF(B2<TIME(15,30,0),"Ship Today","Next Day")
```

**Why It Works:** TIME creates the cutoff as a number in the same format as the timestamps in column B. The comparison uses the full stored value, so column B should hold only times. If it holds date-time values, compare MOD(B2,1) with the cutoff instead, because MOD keeps the time fraction and drops the date.

### Adding an Offset to a Start Time

**Scenario:** A training session starts at 9:00 AM. Each module lasts 45 minutes, and a planner needs the start time of the fourth module.

```excel
=TIME(9,0,0)+TIME(0,45,0)*3
```

**Why It Works:** TIME converts both the start and the module length into fractions of a day, so multiplying the length by 3 gives the offset for three module lengths. The fourth module starts three intervals after the first, which is 135 minutes later, so the result displays as 11:15 AM.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text, or a reference to text. | Convert the value to a number with VALUE or enter the number directly. |
| Displays as a date | The cell was General before the formula was entered, so Excel changed its format. | Format the cell as a time after entering the formula. |
| Unexpected clock reading | A value such as 27 for the hour rolled over to the next day. | Check the inputs. Use values from 0 to 23 for the hour in normal schedules. |
| Result looks like a decimal | The cell is formatted as a number. | Apply a time number format such as h:mm AM/PM. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Overflow rules are documented for values from 0 to 32767. |
| Google Sheets | Available | Recalculates out-of-range values silently and truncates decimals to whole numbers. |

## Tips and Best Practices

- Use TIME with cell references rather than typed numbers so that schedules can be changed in one place.
- Add or subtract TIME results directly, then multiply by 24 to convert the result to hours.
- Avoid negative values, because the documentation does not describe them.
- Use HOUR, MINUTE and SECOND to read the parts of a time back out after you build it.
- Keep inputs in clock range for schedules so that the result is easy to check by eye.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TIMEVALUE](TIMEVALUE.md) | Converts a text time such as "18:45" to a time value. Use it when the time starts as text. |
| [HOUR](HOUR.md) | Returns the hour part of a time, the reverse of building one. |
| [MINUTE](MINUTE.md) | Returns the minute part of a time. |
| [SECOND](SECOND.md) | Returns the seconds part of a time. |
| [NOW](NOW.md) | Returns the current date and time, which TIME values can be added to. |
| [DATE](DATE.md) | Builds the date part. Add it to TIME to create a full date-time value. |

## Official Documentation

- [Microsoft Support: TIME function](https://support.microsoft.com/en-us/excel/functions/time-function)
- [Google Docs Editors Help: TIME](https://support.google.com/docs/answer/3093056)
