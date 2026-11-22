---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Parts
purpose:
  - Date Calculation
use-case:
  - Shift Scheduling
  - Weekday Labels
  - Weekend Flagging
related:
  - DATE
  - ISOWEEKNUM
  - NETWORKDAYS
  - TEXT
  - WEEKNUM
  - WORKDAY
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/weekday-function
  - https://support.google.com/docs/answer/3092985
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Day of Week
  - Weekday Number
tags:
  - date
  - excel
  - sheets
  - weekday-numbering
  - weekend
---

# WEEKDAY

## Description

**WEEKDAY** returns a whole number that identifies the day of the week for a date. By default, 1 is Sunday and 7 is Saturday. The optional return_type argument changes the numbering, for example so that Monday is 1, or so that Monday is 0.

Use WEEKDAY when a formula needs to test or group dates by day of the week: flag weekend rows, look up a shift pattern, or pick a day name from a list. WEEKDAY returns a number, not a name. To display the name, use TEXT with the `"dddd"` format or wrap the number in CHOOSE.

WEEKDAY counts days, while WEEKNUM counts weeks within the year. Excel accepts return_type values 1 to 3 and 11 to 17. Types 11 to 17 make the chosen day count as 1, from Monday (11) through Sunday (17). Google Sheets documents only types 1, 2 and 3.

## Syntax

```excel
=WEEKDAY(serial_number, [return_type])
```

<!-- Image 1: Weekday Numbering Scale. See Images/Date & Time/WEEKDAY.md -->

Google Sheets names the arguments `date` and `type`, as in `WEEKDAY(date, [type])`. The arguments are positional, so the same formulas work on both platforms.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `serial_number` (Excel) or `date` (Sheets) | Yes | The date to test: a cell that contains a date, the result of DATE or DATEVALUE, or a serial number. Dates typed as text can be read incorrectly. |
| `return_type` (Excel) or `type` (Sheets) | No | How the days are numbered. When omitted, the value is 1 (Sunday is 1). Excel accepts 1 to 3 and 11 to 17. Google Sheets accepts 1 to 3. |

### Return Value

An integer from 1 to 7 for return_type 1, 2, 11 to 17, or 0 to 6 for return_type 3. Excel returns `#NUM!` when return_type is not a supported value or when the date is outside the valid date range.

## Examples

All examples use the date 11/22/2026 (a Sunday) in cell A2.

<!-- Image 2: Return Type Results for One Sunday. See Images/Date & Time/WEEKDAY.md -->

### Example 1: Default Numbering

```excel
=WEEKDAY(A2)
```

**Result:** `1`

The default numbering counts Sunday as 1 and Saturday as 7, so the Sunday in A2 returns 1.

### Example 2: Monday as the First Day

```excel
=WEEKDAY(A2, 2)
```

**Result:** `7`

With return_type 2, Monday is 1 and Sunday is 7. Use this numbering when a report lists the week from Monday.

### Example 3: Monday as Zero

```excel
=WEEKDAY(A2, 3)
```

**Result:** `6`

Return_type 3 counts Monday as 0 and Sunday as 6. This suits formulas that add a day offset to a Monday start date.

### Example 4: Flag Weekend Dates

```excel
=IF(WEEKDAY(A2, 2)>5, "Weekend", "Weekday")
```

**Result:** `Weekend`

With return_type 2, Saturday is 6 and Sunday is 7, so any result above 5 is a weekend day.

### Example 5: Week Starting on Friday

```excel
=WEEKDAY(A2, 15)
```

**Result:** `3` (Excel only)

Return_type 15 numbers Friday as 1, Saturday as 2 and Sunday as 3. Google Sheets does not document this type.

## Story Problems

### Problem 1: Weekend Patient Visits at a Clinic

A clinic records visits for one week in A2:B8. Column A holds the date and column B holds the number of patients seen.

| Date | Patients |
| --- | --- |
| 11/16/2026 | 84 |
| 11/17/2026 | 91 |
| 11/18/2026 | 77 |
| 11/19/2026 | 88 |
| 11/20/2026 | 102 |
| 11/21/2026 | 130 |
| 11/22/2026 | 115 |

**Task:** Count the weekend days in the week, then total the patients seen on weekend days.

**Solution:**

```excel
=SUMPRODUCT((WEEKDAY(A2:A8, 2)>5)*1)
```

```excel
=SUMPRODUCT((WEEKDAY(A2:A8, 2)>5)*B2:B8)
```

**Answer:** `2` weekend days, and `245` patients (130 on Saturday plus 115 on Sunday). The first formula counts the weekend days and the second adds their patient counts.

### Problem 2: Naming a Meeting Day

A project team stores its next review date in B2 as 12/04/2026. The team wants the day name in a status cell.

**Task:** Return the day name for the date in B2, with Monday as the first day of the week.

**Solution:**

```excel
=CHOOSE(WEEKDAY(B2, 2), "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
```

**Answer:** `Friday`. With return_type 2, WEEKDAY returns 5 for a Friday, so CHOOSE returns the fifth name.

### Problem 3: Saturdays in the First Week of December

A shop lists the dates of the first week of December 2026 in A2:A8 and must count how many fall on a Saturday.

**Task:** Count the Saturdays in the list. With the default numbering, Saturday is 7.

**Solution:**

```excel
=SUMPRODUCT((WEEKDAY(A2:A8, 1)=7)*1)
```

**Answer:** `1`. Only December 5, 2026 is a Saturday in that list.

## Use Cases

### Shift Schedule Lookup

**Scenario:** A call center publishes its staffing pattern with the columns in Monday to Sunday order in B1:H1. Each date needs the matching column header.

```excel
=INDEX($B$1:$H$1, WEEKDAY(A2, 2))
```

**Why It Works:** Return_type 2 numbers Monday as 1, which matches the first column in the header row. With the default numbering, Monday through Saturday each return the column one position to the right of the correct one, and Sunday returns the Monday column.

### Weekend Premium Pay

**Scenario:** Payroll pays 50 percent more for hours worked on a Saturday or Sunday. Hours for each day are in C2 and the date is in A2.

```excel
=IF(WEEKDAY(A2, 2)>=6, C2*0.5, 0)
```

**Why It Works:** Saturday and Sunday return 6 and 7 with return_type 2, so the test catches both weekend days. Weekday rows return 0. Check the premium rule with payroll before using the formula, since some employers pay weekend premiums differently.

### Weekday Labels for a Date Column

**Scenario:** A report needs a short label beside each date, such as "Mon" or "Sat", without a helper table.

```excel
=TEXT(A2, "ddd")
```

**Why It Works:** TEXT formats the date with its weekday abbreviation directly. Use WEEKDAY instead when the formula needs the number for a test or an index, not a label.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | return_type is not 1 to 3 or 11 to 17 in Excel. | Use a supported value. |
| Wrong day | A date typed as text is read under a different date order. | Enter the date with DATE or convert it with DATEVALUE. |
| Date instead of a number | The result cell is formatted as a date, so Excel displays a date string. | Format the cell as Number or General. |
| Result off by one | A formula built for Monday-first numbering uses the default type 1. | Set return_type 2 or 3 to match the formula's expectation. |
| Error or unexpected number | A return_type from 11 to 17 is used in Google Sheets. | Use types 1 to 3 in Sheets, and check the numbering with a known date. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions | Accepts return_type 1 to 3 and 11 to 17. Other values return `#NUM!`. |
| Google Sheets | Available | Documents types 1 to 3 only. Argument names are `date` and `type`. |

## Tips and Best Practices

- Choose the return_type that matches the list of day labels the formula indexes into, so no offset arithmetic is needed.
- Use return_type 2 for Monday-first reports, because weekend days then test as values above 5.
- Keep dates as real date values in the cells. A date typed as text may not be read the way you expect.
- Use TEXT with `"dddd"` for a full day name and `"ddd"` for an abbreviation.
- Use WORKDAY or NETWORKDAYS when the question is about business days rather than the weekday number.
- Test the numbering with a known date, such as the Sunday 11/22/2026, before you copy a formula down a column.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds a date from year, month and day before testing its weekday. |
| [ISOWEEKNUM](ISOWEEKNUM.md) | Returns the ISO 8601 week number of a date. |
| [NETWORKDAYS](NETWORKDAYS.md) | Counts business days between two dates, skipping weekends. |
| [TEXT](../Text/TEXT.md) | Returns the weekday name when the formula needs a label instead of a number. |
| [WEEKNUM](WEEKNUM.md) | Returns the week of the year rather than the day of the week. |
| [WORKDAY](WORKDAY.md) | Adds business days to a date, which uses the same weekend rule. |

## Official Documentation

- [Microsoft Support: WEEKDAY function](https://support.microsoft.com/en-us/excel/functions/weekday-function)
- [Google Docs Editors Help: WEEKDAY](https://support.google.com/docs/answer/3092985)
