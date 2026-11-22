---
domain: Spreadsheet Functions
category: Database
subcategory: Database Aggregation
purpose:
  - Counting
  - Database Queries
use-case:
  - Customer Reach Reports
  - Event Attendance Counts
  - Unique Buyer Totals
related:
  - COUNTIFS
  - COUNTUNIQUE
  - DCOUNTA
  - DSUM
  - FILTER
  - UNIQUE
level: 3
source:
  - https://support.google.com/docs/answer/9584429
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Count Unique If
  - Distinct Count With Criteria
tags:
  - criteria
  - database
  - distinct-values
  - sheets
---

# COUNTUNIQUEIFS

## Description

**COUNTUNIQUEIFS** counts the distinct values in one column, using only the rows that meet one or more conditions set on other columns. A customer who places ten orders in a month is counted once, which makes it the right choice when the question is "How many different people?" rather than "How many rows?"

Each condition pairs a criteria range with a criterion, the same way COUNTIFS works. A row is included only when it passes every condition. The function returns 0 when no row passes all of them. The count range and every criteria range must cover the same number of rows and columns.

COUNTUNIQUEIFS is a Google Sheets function listed in the Database category of the Google Docs Editors help. Microsoft Excel does not have a function with this name. In Excel 365, combine UNIQUE and FILTER instead, as shown in the Platform Differences section.

Use COUNTIFS when you want to count rows. Use COUNTUNIQUEIFS when duplicate values in the counted column should be treated as one.

## Syntax

```excel
=COUNTUNIQUEIFS(count_unique_range, criteria_range1, criterion1, [criteria_range2, criterion2, ...])
```

<!-- Image 1: COUNTUNIQUEIFS Syntax Anatomy. See Images/Database/COUNTUNIQUEIFS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `count_unique_range` | Yes | The column whose distinct values are counted, such as `A2:A9`. Duplicates inside this range are counted once. |
| `criteria_range1` | Yes | The first range that each row is tested against. It must have the same number of rows and columns as `count_unique_range`. |
| `criterion1` | Yes | The condition applied to `criteria_range1`, such as `"Web"`, `">20"` or a cell reference. |
| `criteria_range2, criterion2, ...` | No | Optional pairs of extra ranges and conditions. A row must pass all of them. |

### Return Value

A whole number: the count of distinct values in `count_unique_range` among the rows that pass every condition. It returns 0 when no row passes all conditions.

## Examples

All examples use this purchase list in `A1:C9`, with headers in row 1.

| Customer | Channel | Amount |
| --- | --- | --- |
| Ana | Web | 120 |
| Ben | Store | 45 |
| Ana | Store | 80 |
| Cara | Web | 210 |
| Ben | Web | 30 |
| Cara | Web | 150 |
| Dev | Store | 60 |
| Ana | Web | 25 |

### Example 1: One Text Condition

```excel
=COUNTUNIQUEIFS(A2:A9, B2:B9, "Web")
```

**Result:** `3`

The Web rows name Ana, Cara, Ben, Cara and Ana. Ana, Cara and Ben are the three different customers, so the result is 3 rather than 5.

<!-- Image 2: Distinct Customers Versus Rows. See Images/Database/COUNTUNIQUEIFS.md -->

### Example 2: One Numeric Condition

```excel
=COUNTUNIQUEIFS(A2:A9, C2:C9, ">50")
```

**Result:** `3`

Five rows have an amount above 50: Ana (120), Ana (80), Cara (210), Cara (150) and Dev (60). The distinct customers are Ana, Cara and Dev.

### Example 3: Two Conditions

```excel
=COUNTUNIQUEIFS(A2:A9, B2:B9, "Web", C2:C9, ">100")
```

**Result:** `2`

Three Web rows exceed 100: Ana (120), Cara (210) and Cara (150). They belong to two customers, Ana and Cara.

### Example 4: Condition From a Cell

Cell `E2` holds `Store`.

```excel
=COUNTUNIQUEIFS(A2:A9, B2:B9, E2)
```

**Result:** `3`

The Store rows belong to Ben, Ana and Dev, so three customers qualify. Changing `E2` to `Web` would return 3 as well, because Ana, Cara and Ben are the Web customers.

## Story Problems

### Problem 1: Event Attendees Who Rated a Workshop Well

A conference team records one rating per session attended in `A1:C9`.

| Attendee | Session | Rating |
| --- | --- | --- |
| Priya | Workshop | 5 |
| Tom | Keynote | 4 |
| Priya | Keynote | 3 |
| Lena | Workshop | 4 |
| Tom | Workshop | 5 |
| Omar | Workshop | 3 |
| Lena | Workshop | 5 |
| Sam | Panel | 4 |

**Task:** Count the different attendees who rated a Workshop 4 or higher.

**Solution:**

```excel
=COUNTUNIQUEIFS(A2:A9, B2:B9, "Workshop", C2:C9, ">=4")
```

**Answer:** `3`. Priya (5), Lena (4 and 5) and Tom (5) qualify. Lena appears twice but is counted once. Omar rated his workshop 3, so he does not qualify.

<!-- Image 3: Workshop Attendee Result. See Images/Database/COUNTUNIQUEIFS.md -->

### Problem 2: Pickers Who Handled Large Zone B Batches

A warehouse lead logs each batch a picker completes in `A1:C9`.

| Picker | Zone | Lines Picked |
| --- | --- | --- |
| Ines | B | 40 |
| Joel | A | 65 |
| Ines | B | 55 |
| Kai | B | 70 |
| Joel | B | 20 |
| Kai | C | 90 |
| Ines | A | 30 |
| Lou | B | 50 |

**Task:** Count the different pickers who completed a Zone B batch of at least 50 lines.

**Solution:**

```excel
=COUNTUNIQUEIFS(A2:A9, B2:B9, "B", C2:C9, ">=50")
```

**Answer:** `3`. Ines (55), Kai (70) and Lou (50) qualify. Joel's Zone B batch has only 20 lines, and Kai's 90-line batch is in Zone C.

## Use Cases

### Customer Reach Reports

**Scenario:** A marketing lead wants the number of different customers who bought through the web channel for more than 100.

```excel
=COUNTUNIQUEIFS(Orders[Customer], Orders[Channel], "Web", Orders[Amount], ">100")
```

**Why It Works:** A customer with several large web orders is counted once. Structured references keep the range in step with the table as orders are added.

### Event Attendance Counts

**Scenario:** An events coordinator counts the people who attended any Workshop, using the session names in column B and the attendance flag in column D.

```excel
=COUNTUNIQUEIFS(Attendance!A2:A500, Attendance!B2:B500, "Workshop", Attendance!D2:D500, "Yes")
```

**Why It Works:** Each attendee who attended a workshop counts once, even when the same person attended several sessions. The flag column keeps no-shows out of the total.

### Unique Buyer Totals

**Scenario:** A sales analyst keeps a product name in `H1` and a start date in `H2`, and needs the number of different buyers since that date.

```excel
=COUNTUNIQUEIFS(Sales!A2:A500, Sales!B2:B500, $H$1, Sales!C2:C500, ">="&$H$2)
```

**Why It Works:** The product and date live in cells, so the analyst can change them without rewriting the formula. The `&` operator joins the date to the comparison sign.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` in Excel | Excel has no COUNTUNIQUEIFS function. | Use the Microsoft 365 alternative in Platform Differences. |
| `0` returned | No row passes every condition. | Test each condition with COUNTIF to find the one that removes every row. |
| Error or unexpected result | The ranges have different numbers of rows or columns. | Select the same number of rows in every range, such as `A2:A9` and `B2:B9`. |
| Count is higher than expected | Names with extra spaces, such as `"Ana "`, can count as different values from `"Ana"`. | Clean the names with `TRIM` before counting. |
| Count matches rows, not people | The formula uses COUNTIFS, which does not remove duplicates. | Switch to COUNTUNIQUEIFS when duplicates should count once. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Closest alternative in Microsoft 365: `=COUNTA(UNIQUE(FILTER(A2:A9, B2:B9="Web")))`, which needs dynamic array support. Wrap it in `IFERROR(..., 0)` because FILTER returns an error when no row matches. |
| Google Sheets | Available | Listed in the Database category. The help page gives its syntax and examples without sample results, so test the formula on known data before you rely on it. |

## Tips and Best Practices

- Use COUNTUNIQUEIFS for "how many different," and COUNTIFS for "how many rows."
- Keep every range the same length, and extend them together when new rows are added.
- Clean text before counting, because spaces and capital letters can make the same name look different.
- Store each condition in its own cell, so a report can change its filters without a new formula.
- Test a small list by hand once, so you know the function treats duplicates the way you expect.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNTIFS](../Statistical/COUNTIFS.md) | Counts rows, including repeats, that meet several conditions. |
| [COUNTUNIQUE](../Math%20%26%20Trig/COUNTUNIQUE.md) | Counts distinct values in one range with no conditions. |
| [DCOUNTA](DCOUNTA.md) | Counts non-empty values in a list that match a criteria range, in Excel. |
| [DSUM](DSUM.md) | Adds a field for the rows that match a criteria range. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the matching rows, which you can pass to UNIQUE or COUNTA. |
| [UNIQUE](../Lookup%20%26%20Reference/UNIQUE.md) | Returns the distinct values, which you can count with COUNTA. |

## Official Documentation

- [Google Docs Editors Help: COUNTUNIQUEIFS](https://support.google.com/docs/answer/9584429)
