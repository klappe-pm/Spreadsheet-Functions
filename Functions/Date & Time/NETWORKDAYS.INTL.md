---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Workdays
purpose:
  - Date Calculation
use-case:
  - Clinic Opening Days
  - Laboratory Turnaround Time
  - Shift Pattern Planning
related:
  - DATE
  - DAYS
  - NETWORKDAYS
  - SUMIFS
  - WORKDAY
  - WORKDAY.INTL
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/networkdays-intl-function
  - https://support.google.com/docs/answer/3295902
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Custom Weekend Workdays
  - International Workdays
tags:
  - business-days
  - custom-weekend
  - excel
  - sheets
  - workdays
---

# NETWORKDAYS.INTL

## Description

**NETWORKDAYS.INTL** counts the whole working days between two dates, excluding the weekend days and any holidays you list. It works like NETWORKDAYS but adds a weekend argument, so the weekend can be any combination of days. This matters for organizations whose weekend is Friday and Saturday, for businesses that close on a single weekday, and for shift patterns that rest on different days.

The weekend argument takes either a number code or a seven-character string. The number codes cover all two-day pairs and every single-day weekend, and the string lets you mark each day of the week explicitly. If you leave the argument out, Saturday and Sunday are the weekend, which makes the function behave exactly like NETWORKDAYS.

The function is inclusive of both dates, and the start date may be later than the end date. In that case the result is negative, and its size is the number of workdays between the two dates. A date outside the valid range for the spreadsheet returns `#NUM!`, and a weekend string of the wrong length or with characters other than 0 and 1 returns `#VALUE!`.

## Syntax

```excel
=NETWORKDAYS.INTL(start_date, end_date, [weekend], [holidays])
```

<!-- Image 1: Syntax Anatomy. See Images/Date & Time/NETWORKDAYS.INTL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `start_date` | Yes | The first date of the period. It may be earlier or later than end_date. |
| `end_date` | Yes | The last date of the period. |
| `weekend` | No | A weekend number from 1 to 7 or 11 to 17, or a seven-character string of 0 and 1 that starts with Monday. Omitted, it defaults to 1, which means Saturday and Sunday. |
| `holidays` | No | A range of cells or an array constant of dates to exclude. The dates can be in any order. |

### Weekend Numbers

| Number | Weekend Days |
| --- | --- |
| 1 or omitted | Saturday and Sunday |
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

### Weekend String

The string holds seven characters that start with Monday and end with Sunday. A `1` marks a non-workday, and a `0` marks a workday. For example, `"0000011"` makes Saturday and Sunday the weekend, and `"0010100"` makes Wednesday and Friday the weekend. A string of all 1s always returns 0.

### Return Value

An integer that counts the whole workdays between the two dates, excluding the weekend and holidays. The result is negative when start_date is later than end_date.

## Examples

### Example 1: Default Weekend

```excel
=NETWORKDAYS.INTL(A2,B2)
```

**Result:** `22` (when A2 contains June 1, 2026 and B2 contains June 30, 2026)

June 2026 has 30 days, and eight of them fall on a Saturday or Sunday. The remaining 22 are workdays.

### Example 2: Weekend Number for Friday and Saturday

```excel
=NETWORKDAYS.INTL(A2,B2,7)
```

**Result:** `22` (when A2 and B2 are the June 2026 dates from Example 1)

Weekend number 7 makes Friday and Saturday the weekend. June 2026 has eight Friday and Saturday dates, so the count is also 22, though the weekend days are different.

<!-- Image 2: Weekend Number Reference. See Images/Date & Time/NETWORKDAYS.INTL.md -->

### Example 3: Weekend String for Saturday and Sunday

```excel
=NETWORKDAYS.INTL(A2,B2,"0000011")
```

**Result:** `22`

The string marks Saturday and Sunday as weekend days. The result matches the default, which is useful as a check that the string is correct.

### Example 4: Sunday Only Weekend

```excel
=NETWORKDAYS.INTL(A2,B2,11)
```

**Result:** `26`

Weekend number 11 marks only Sundays as non-workdays. June 2026 has four Sundays, so 26 days remain.

### Example 5: Custom Weekend With Holidays

```excel
=NETWORKDAYS.INTL(A2,B2,"0010100",D2:D3)
```

**Result:** `21` (when D2 contains June 15, 2026 and D3 contains June 19, 2026)

The string makes Wednesday and Friday the weekend, which removes 8 days from June, leaving 22. June 15 is a Monday, so it is a workday and is removed. June 19 is a Friday, which is already a weekend day, so removing it changes nothing. The result is 21.

## Story Problems

### Problem 1: Weekly Closed Day Restaurant

A restaurant is closed every Monday. It also closes on Tuesday, June 16, 2026 for an equipment repair. Staff want the number of days the restaurant opens in June 2026.

| Period Start | Period End | Closed Day |
| --- | --- | --- |
| 2026-06-01 | 2026-06-30 | 2026-06-16 |

**Task:** Count the open days, using weekend number 12 for the Monday closure and the repair date as a holiday.

**Solution:**

```excel
=NETWORKDAYS.INTL(A2,B2,12,C2)
```

**Answer:** `24`. June 2026 has five Mondays, which leaves 25 open days. The repair closes one more day on June 16, so 24 days are open.

### Problem 2: Laboratory With a Friday and Saturday Weekend

A laboratory is closed on Fridays and Saturdays. It also observes a holiday on June 19, 2026, which falls on a Friday. Managers want the number of working days in June 2026.

| Period Start | Period End | Holiday |
| --- | --- | --- |
| 2026-06-01 | 2026-06-30 | 2026-06-19 |

**Task:** Count the working days with weekend number 7 and the holiday in C2.

**Solution:**

```excel
=NETWORKDAYS.INTL(A2,B2,7,C2)
```

**Answer:** `22`. Friday and Saturday give eight weekend days in June 2026. The holiday falls on a Friday, which is already excluded, so it does not reduce the count again.

## Use Cases

### Clinic Opening Days

**Scenario:** A clinic is open only on Mondays, Tuesdays and Thursdays. The billing team needs the number of open days in the month that contains the date in A2.

```excel
=NETWORKDAYS.INTL(DATE(YEAR(A2),MONTH(A2),1),EOMONTH(A2,0),"0010111")
```

**Why It Works:** EOMONTH finds the last day of the month, and DATE builds the first day. The string "0010111" reads Monday to Sunday, so the 1s mark Wednesday, Friday, Saturday and Sunday as non-workdays. Only Monday, Tuesday and Thursday count as open days.

### Shift Pattern Planning

**Scenario:** A plant crew rests on Wednesdays and Sundays. A planner needs the number of working days in a project window.

```excel
=NETWORKDAYS.INTL(B2,C2,"0010001")
```

**Why It Works:** The string reads Monday to Sunday, and the 1s mark Wednesday (position 3) and Sunday (position 7) as rest days. Every other day is a workday, so the count excludes exactly the crew's two rest days each week.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The weekend string has the wrong length or characters other than 0 and 1. | Use exactly seven characters that are all 0 or 1. |
| `#NUM!` | A date is outside the range the spreadsheet can store. | Check the date cells for typing errors. |
| Negative result | start_date is later than end_date. | Swap the dates, or accept the negative value as a backward count. |
| Count is wrong with a string | The string starts on Sunday instead of Monday. | Rewrite the string so that position 1 is Monday. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Accepts weekend numbers 1 to 7 and 11 to 17, and the seven-character string. |
| Google Sheets | Available | Same weekend options. Confirm the string starts on Monday in your own tests. |

## Tips and Best Practices

- Use the string form when you need a weekend pattern that no number code covers, and label the string in a cell next to the formula.
- Test a custom weekend by counting one week by hand and comparing it with the formula result.
- Keep the holiday list in a named range, so every workday formula in the workbook reads the same dates.
- Use NETWORKDAYS when the weekend is Saturday and Sunday, because it is simpler to read.
- Remember that a holiday on a day that is already a weekend does not change the count.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NETWORKDAYS](NETWORKDAYS.md) | Counts workdays with a fixed Saturday and Sunday weekend. |
| [WORKDAY](WORKDAY.md) | Returns the date that is a number of workdays after a start date. |
| [WORKDAY.INTL](WORKDAY.INTL.md) | Returns a workday offset with the same custom weekend options. |
| [DATE](DATE.md) | Builds the start date for the first day of a month or period. |
| [DAYS](DAYS.md) | Counts calendar days, including weekends, between two dates. |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Totals values inside a date window once the workday counts are known. |

## Official Documentation

- [Microsoft Support: NETWORKDAYS.INTL function](https://support.microsoft.com/en-us/excel/functions/networkdays-intl-function)
- [Google Docs Editors Help: NETWORKDAYS.INTL](https://support.google.com/docs/answer/3295902)
