---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Workdays
purpose:
  - Date Calculation
use-case:
  - Custom Weekend Calendars
  - Lab Turnaround Dates
  - Shift Rotation Planning
related:
  - DATE
  - NETWORKDAYS
  - NETWORKDAYS.INTL
  - WEEKDAY
  - WORKDAY
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/workday-intl-function
  - https://support.google.com/docs/answer/3294972
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Custom Weekend Workdays
  - Workdays With Custom Weekend
tags:
  - business-days
  - custom-weekend
  - date
  - excel
  - sheets
---

# WORKDAY.INTL

## Description

**WORKDAY.INTL** returns the date that is a given number of working days before or after a start date, with a weekend that you choose. It works like WORKDAY, which always treats Saturday and Sunday as the weekend, but adds a weekend argument. The weekend can be a numeric code, such as 11 for Sunday only, or a seven-character string of 1s and 0s that marks each day of the week.

Use WORKDAY.INTL for calendars that do not follow the Saturday and Sunday weekend, such as a lab that is closed on Fridays and Saturdays, a shift pattern with rotating days off, or a store that is open every day except Sunday. The optional holiday list works the same way as in WORKDAY.

The function is best used when the weekend is fixed for the whole calendar. When each row needs a different weekend, put the weekend code or string in its own column and reference that cell.

## Syntax

```excel
=WORKDAY.INTL(start_date, days, [weekend], [holidays])
```

<!-- Image 1: Weekend Codes and Strings. See Images/Date & Time/WORKDAY.INTL.md -->

Google Sheets uses the argument names `start_date`, `num_days`, `weekend` and `holidays`. The order matches Excel, so the same formulas work on both platforms.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `start_date` | Yes | The date to count from. The value is truncated to a whole number. |
| `days` | Yes | The number of working days to add (positive) or subtract (negative). Zero returns the start date. The value is truncated to a whole number. |
| `weekend` | No | A weekend code from 1 to 7 or 11 to 17, or a string of seven 1s and 0s that starts on Monday. A 1 marks a non-working day. The default is 1 (Saturday and Sunday). |
| `holidays` | No | A range of cells or an array constant of dates that are not working days. |

### Weekend Codes

| Code | Non-Working Days |
| --- | --- |
| 1 (default) | Saturday and Sunday |
| 2 | Sunday and Monday |
| 3 | Monday and Tuesday |
| 4 | Tuesday and Wednesday |
| 5 | Wednesday and Thursday |
| 6 | Thursday and Friday |
| 7 | Friday and Saturday |
| 11 | Sunday only |
| 12 | Monday only |
| 13 | Tuesday only |
| 14 | Wednesday only |
| 15 | Thursday only |
| 16 | Friday only |
| 17 | Saturday only |

The string form lists the days from Monday to Sunday. For example, `"0000011"` makes Saturday and Sunday the weekend, and `"0010001"` makes Wednesday and Sunday the weekend. The string `"1111111"` is not valid, because it would leave no working days.

### Return Value

A date serial number for the resulting working day. Excel returns `#NUM!` when weekend is 0 or when a date is outside the valid range. It returns `#VALUE!` when the weekend string has the wrong length or contains characters other than 0 and 1.

## Examples

All examples use the Friday 11/20/2026 in cell A2 unless the example shows its own date.

<!-- Image 2: Sunday Only Versus Default Weekend. See Images/Date & Time/WORKDAY.INTL.md -->

### Example 1: Sunday as the Only Weekend Day

```excel
=WORKDAY.INTL(A2, 5, 11)
```

**Result:** `11/26/2026`

With weekend code 11, Saturday counts as a working day. Five working days after Friday November 20 are Saturday 21, Monday 23, Tuesday 24, Wednesday 25 and Thursday 26.

### Example 2: The Default Weekend

```excel
=WORKDAY.INTL(A2, 5)
```

**Result:** `11/27/2026`

Without a weekend argument, Saturday and Sunday are skipped. The five working days are Monday 23 through Friday 27.

### Example 3: Friday and Saturday as the Weekend

```excel
=WORKDAY.INTL(A2, 5, "0000110")
```

**Result:** `11/26/2026`

The string marks Friday (position 5) and Saturday (position 6) with 1, so Sunday 22 is the first working day and Thursday 26 is the fifth.

### Example 4: Sunday and Monday as the Weekend

```excel
=WORKDAY.INTL(A2, 5, 2)
```

**Result:** `11/27/2026`

Code 2 skips Sunday and Monday. Saturday 21 is working day 1, and the fifth working day is Friday November 27.

### Example 5: Counting Backward Past Holidays

```excel
=WORKDAY.INTL(A2, -2, 1, H2:H4)
```

**Result:** `12/23/2026` when A2 holds 12/29/2026

The holidays in H2:H4 are 12/24/2026, 12/25/2026 and 01/01/2027. Counting back from Tuesday December 29, Monday 28 is the first working day, and Wednesday 23 is the second, because the weekend and the holidays of December 24 and 25 are skipped.

## Story Problems

### Problem 1: Lab Turnaround on a Friday and Saturday Weekend

A testing lab does not work on Fridays or Saturdays. A sample received on Friday 12/18/2026 needs four working days for analysis.

**Task:** Find the date the results are ready, when the weekend is Friday and Saturday.

**Solution:**

```excel
=WORKDAY.INTL(A2, 4, 7)
```

**Answer:** `12/23/2026`. The four working days are Sunday 20, Monday 21, Tuesday 22 and Wednesday 23.

### Problem 2: Rotating Shift Days Off

A crew is off on Wednesdays and Sundays. The string for that weekend is `"0010001"`, which marks position 3 (Wednesday) and position 7 (Sunday). The crew starts a job on Friday 11/20/2026 and needs six working days.

**Task:** Find the date of the sixth working day.

**Solution:**

```excel
=WORKDAY.INTL(A2, 6, "0010001")
```

**Answer:** `11/28/2026`. The working days are Saturday 21, Monday 23, Tuesday 24, Thursday 26, Friday 27 and Saturday 28.

### Problem 3: Stores Open Every Day Except Sunday

A store is closed only on Sundays and on the holidays of 12/24/2026 and 12/25/2026. An order is placed on Saturday 12/19/2026 and the shop promises delivery in seven working days.

**Task:** Find the promised delivery date, with holidays in D2:D3 and weekend code 11.

**Solution:**

```excel
=WORKDAY.INTL(A2, 7, 11, D2:D3)
```

**Answer:** `12/30/2026`. The working days are Monday 21, Tuesday 22, Wednesday 23, Saturday 26, Monday 28, Tuesday 29 and Wednesday 30, because the holidays on 24 and 25 are skipped.

## Use Cases

### Custom Weekend Calendars

**Scenario:** A regional office works Saturday to Wednesday. Its project plan needs the end date of each task in working days.

```excel
=WORKDAY.INTL(B2, C2, 6)
```

**Why It Works:** Code 6 marks Thursday and Friday as the weekend, so the formula skips those days. Keep the weekend code in a labeled cell so the office can change its calendar without editing formulas.

### Lab Turnaround Dates

**Scenario:** A lab with a Friday and Saturday closure promises results within a set number of working days after receipt.

```excel
=WORKDAY.INTL(A2, B2, 7, Holidays)
```

**Why It Works:** Code 7 closes Friday and Saturday. The `Holidays` name points to the lab's closure dates, so the promised date moves correctly when a holiday falls inside the window.

### Shift Rotation Planning

**Scenario:** A plant assigns each crew a fixed pattern of days off, written as a seven-character string in column C.

```excel
=WORKDAY.INTL(A2, B2, C2)
```

**Why It Works:** Each crew's string is read as its own weekend, so one formula covers every pattern. Check that every string has exactly seven characters of 1s and 0s, because any other text returns `#VALUE!`.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | weekend is 0, or a date is outside the valid range. | Use a valid weekend code and check the dates. |
| `#VALUE!` | The weekend string is not seven characters, or it contains other characters. | Use exactly seven 1s and 0s, starting with Monday. |
| Error | The string is all 1s, which leaves no working day and is not valid. | Leave at least one day marked 0. |
| Result matches WORKDAY | The weekend argument is omitted or set to 1. | Set the code or string for the calendar you need. |
| Holiday ignored | The holiday cells hold text. | Convert the holiday cells to dates. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Accepts weekend codes 1 to 7 and 11 to 17 and the seven-character string. |
| Google Sheets | Available | Accepts the same numeric codes and string. The argument is named `weekend`. |

## Tips and Best Practices

- Store the weekend code or string in a labeled cell, not inside the formula, so the calendar is easy to change.
- Use the string form when the weekend is not a simple run of days, such as Wednesday and Sunday.
- Check each new weekend pattern with a short known schedule before you use it for deadlines.
- Keep holiday dates in a named range, and enter them as real dates.
- Use WORKDAY when the weekend is always Saturday and Sunday, because the formula is shorter.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds a start date from year, month and day. |
| [NETWORKDAYS](NETWORKDAYS.md) | Counts working days between two dates with a Saturday and Sunday weekend. |
| [NETWORKDAYS.INTL](NETWORKDAYS.INTL.md) | Counts working days between two dates with a custom weekend. |
| [WEEKDAY](WEEKDAY.md) | Returns the day of the week, useful for building custom weekend tests. |
| [WORKDAY](WORKDAY.md) | Adds working days with a fixed Saturday and Sunday weekend. |

## Official Documentation

- [Microsoft Support: WORKDAY.INTL function](https://support.microsoft.com/en-us/excel/functions/workday-intl-function)
- [Google Docs Editors Help: WORKDAY.INTL](https://support.google.com/docs/answer/3294972)
