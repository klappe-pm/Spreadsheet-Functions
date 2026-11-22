---
domain: Spreadsheet Functions
category: Logical
subcategory: Conditional Tests
purpose:
  - Conditional Logic
use-case:
  - Commission Tiers
  - Letter Grade Bands
  - Shipping Rate Bands
related:
  - AND
  - CHOOSE
  - IF
  - OR
  - SWITCH
  - XLOOKUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/ifs-function
  - https://support.google.com/docs/answer/7014145
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Multiple IF
  - Nested IF Alternative
tags:
  - conditional-logic
  - excel
  - logical
  - nested-if
  - sheets
---

# IFS

## Description

**IFS** tests a series of conditions in order and returns the value paired with the first condition that is TRUE. You write each condition followed by its result, so a grading scale or a rate table reads as one flat list instead of a stack of nested IF functions.

Use IFS when you have three or more branches and each branch has its own result. Two-branch decisions are clearer with IF. When each branch matches an exact value, such as a status code, SWITCH is often shorter. IFS fits range tests such as score thresholds, weight bands and commission tiers.

The order of the pairs decides the result. IFS stops at the first TRUE condition, so list the most specific or highest threshold first. IFS has no built-in default. If no condition is TRUE, it returns #N/A, so finish with `TRUE` followed by the default value to act as an "else" branch.

## Syntax

```excel
=IFS(logical_test1, value_if_true1, [logical_test2, value_if_true2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/IFS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `logical_test1` | Yes | The first condition to test. It must evaluate to TRUE or FALSE, such as `A2>=90`, `ISBLANK(A2)` or `TRUE`. |
| `value_if_true1` | Yes | The value returned when `logical_test1` is TRUE. It can be a number, text, a cell reference or a formula. |
| `logical_test2` | No | The next condition. It is tested only when every earlier condition is FALSE. |
| `value_if_true2` | No | The value returned when its paired condition is TRUE. Each test needs a matching value. |
| `...` | No | Further condition and value pairs. Microsoft Excel accepts up to 127 pairs. |

### Return Value

The value paired with the first condition that is TRUE. If no condition is TRUE and no `TRUE` default is included, the result is `#N/A`. A test that does not evaluate to TRUE or FALSE returns `#VALUE!`.

## Examples

### Example 1: Letter Grade From a Score

```excel
=IFS(A2>=90,"A",A2>=80,"B",A2>=70,"C",A2>=60,"D",TRUE,"F")
```

**Result:** `B` when A2 holds 85.

The test for 85 fails the first condition (85 is below 90) and passes the second (85 is at least 80), so the formula stops there. The final `TRUE,"F"` pair catches every score below 60.

### Example 2: Replacing a Nested IF

```excel
=IF(B2="Red","Stop",IF(B2="Yellow","Caution",IF(B2="Green","Go","Unknown")))
```

```excel
=IFS(B2="Red","Stop",B2="Yellow","Caution",B2="Green","Go",TRUE,"Unknown")
```

**Result:** `Caution` when B2 holds `Yellow`.

Both formulas return the same value. The IFS version has one pair per condition, so each branch can be checked without counting parentheses.

<!-- Image 2: Nested IF Versus IFS Layout. See Images/Logical/IFS.md -->

### Example 3: Commission Tier With the Rate Applied

```excel
=IFS(C2>=100000,C2*0.1,C2>=50000,C2*0.06,C2>=10000,C2*0.02,TRUE,0)
```

**Result:** `4320` when C2 holds 72000.

The sales figure 72000 is at least 50000 but below 100000, so the 6% rate applies: 72000 × 0.06 = 4320. If the 10000 test were placed first, the same sale would match it and return 1440 (2%). The highest threshold must come first.

### Example 4: Text Result From a Weight Band

```excel
=IFS(D2>50,"Freight",D2>10,"Ground",D2>1,"Priority Mail",TRUE,"First Class")
```

**Result:** `Ground` when D2 holds 12.5.

The weight is above 10 but not above 50, so the second pair returns "Ground". The TRUE pair returns "First Class" for anything at or below 1 kg, including zero.

### Example 5: What Happens Without a Default

```excel
=IFS(E2>0,"Positive",E2<0,"Negative")
```

**Result:** `#N/A` when E2 holds 0.

Zero is neither above 0 nor below 0, so no condition is TRUE and IFS returns `#N/A`. Adding `TRUE,"Zero"` as the last pair returns a label instead.

## Story Problems

### Problem 1: Late Fees by Days Overdue

A small firm charges late fees on five invoices. The fee is 50 for more than 30 days late, 25 for 15 to 30 days, 10 for 1 to 14 days, and 0 when the invoice is on time.

| Invoice | Days Late |
| --- | --- |
| INV-101 | 0 |
| INV-102 | 5 |
| INV-103 | 20 |
| INV-104 | 45 |
| INV-105 | 31 |

**Task:** Fill column C with each invoice's fee, then total the fees in C7.

**Solution:**

```excel
=IFS(B2>30,50,B2>14,25,B2>0,10,TRUE,0)
```

```excel
=SUM(C2:C6)
```

**Answer:** `135`. The fees are 0, 10, 25, 50 and 50, and 0 + 10 + 25 + 50 + 50 = 135.

### Problem 2: Counting Items to Reorder

A parts store keeps a reorder point of 20 units in E1. Items at or below that level need a new order.

| Item | Units in Stock |
| --- | --- |
| Bolts | 0 |
| Nuts | 15 |
| Washers | 20 |
| Brackets | 45 |
| Hinges | 30 |

**Task:** Count the items that need a reorder.

**Solution:**

```excel
=COUNTIF(B2:B6,"<="&E1)
```

**Answer:** `3`. Bolts (0), Nuts (15) and Washers (20) are at or below 20. For a label on each row, use `=IFS(B2<=0,"Out of Stock",B2<=$E$1,"Reorder",B2<=2*$E$1,"Low",TRUE,"OK")`.

<!-- Image 3: Stock Status Worksheet. See Images/Logical/IFS.md -->

## Use Cases

### Letter Grade Bands

**Scenario:** A teacher converts percentage scores into letter grades for a class roster, with a fallback label for scores below the lowest band.

```excel
=IFS(Score>=90,"A",Score>=80,"B",Score>=70,"C",TRUE,"Below C")
```

**Why It Works:** The bands run from highest to lowest, and the TRUE pair catches every remaining score. Changing a cut-off means editing one pair.

### Commission Tiers

**Scenario:** A sales team earns a higher rate on each band of monthly sales.

```excel
=IFS(Sales>=100000,Sales*0.1,Sales>=50000,Sales*0.06,TRUE,Sales*0.03)
```

**Why It Works:** Each tier applies to the whole sale, so the highest band must be tested first. The TRUE pair gives the base rate.

### Shipping Rate Bands

**Scenario:** An online store selects a shipping class from the package weight in kilograms.

```excel
=IFS(Weight>50,"Freight",Weight>10,"Ground",Weight>1,"Priority Mail",TRUE,"First Class")
```

**Why It Works:** The bands are readable by anyone who maintains the price list, and the labels feed directly into a shipping table or a report.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | No condition is TRUE and there is no default. | Add `TRUE,"default value"` as the final pair. |
| `#VALUE!` | A test returns something other than TRUE or FALSE. | Use a comparison or a logical function as the test. |
| Too few arguments | A condition has no value after it. | Make sure every test is followed by its result. |
| Wrong result | A broad condition appears before a specific one. | Move the most specific or highest threshold to the front. |
| `#NAME?` | The workbook opened in an Excel version without IFS. | Use nested IF, or update to a version that lists IFS as available. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2019, Excel 2021, Excel 2024, Microsoft 365 (Windows, Mac and web) | Accepts up to 127 condition and value pairs. Returns `#N/A` when no condition is TRUE and no default is given. |
| Google Sheets | Available | Conditions can be booleans, numbers, arrays or references. Returns `#N/A` when no condition is TRUE. The help page does not state a pair limit. |

## Tips and Best Practices

- Finish every IFS with `TRUE,default` unless you want `#N/A` to flag unhandled cases.
- Order range tests from the highest threshold to the lowest so each value matches only one band.
- Put blank checks such as `A2=""` before numeric tests, because a blank cell can match a comparison in unexpected ways.
- Keep thresholds in cells and reference them with absolute addresses such as `$E$1` so a policy change needs one edit.
- Switch to SWITCH for exact matches, and to XLOOKUP against a bands table when the list grows past about ten pairs.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IF](IF.md) | Tests one condition and returns one of two values. Use it for two branches. |
| [SWITCH](SWITCH.md) | Matches one value against exact options. Use it when branches are not ranges. |
| [CHOOSE](../Lookup%20%26%20Reference/CHOOSE.md) | Returns a value by position number. Use it when the choice is already a number. |
| [XLOOKUP](../Lookup%20%26%20Reference/XLOOKUP.md) | Looks up a value in a bands table kept on the sheet. |
| [AND](AND.md) | Combines several tests inside one IFS condition. |
| [OR](OR.md) | Lets any of several tests trigger the same result. |

## Official Documentation

- [Microsoft Support: IFS function](https://support.microsoft.com/en-us/excel/functions/ifs-function)
- [Google Docs Editors Help: IFS](https://support.google.com/docs/answer/7014145)
