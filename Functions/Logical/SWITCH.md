---
domain: Spreadsheet Functions
category: Logical
subcategory: Conditional Tests
purpose:
  - Conditional Logic
  - Data Cleaning
use-case:
  - Department Code Labels
  - Discount Tiers
  - Status Code Translation
related:
  - CHOOSE
  - IF
  - IFNA
  - IFS
  - VLOOKUP
  - XLOOKUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/switch-function
  - https://support.google.com/docs/answer/7013690
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Case Statement
  - Switch Case
  - Value Mapping
tags:
  - conditional
  - excel
  - logical
  - lookup-alternative
  - sheets
  - value-matching
---

# SWITCH

## Description

**SWITCH** tests one expression against a list of values and returns the result paired with the first value that matches. It works like a case statement in programming: the expression appears once, followed by value and result pairs, with an optional default at the end. Use it to translate codes into labels, such as department numbers into department names or status letters into descriptions.

SWITCH is easier to read than nested IF formulas for the same kind of mapping. Each value sits beside its result, so a reviewer can scan the list without tracing parentheses. Example 2 shows the same color mapping written both ways.

SWITCH compares the expression with each value, so it does not test ranges such as "greater than 10". Use IFS for range tests or for several unrelated conditions. When the mapping lives in a table on the sheet, a lookup function such as XLOOKUP is easier to update than a long SWITCH formula.

Microsoft lists SWITCH for Excel 2019 and later, Microsoft 365, and Excel for the web. Check the version before you share a workbook with someone on an older release.

## Syntax

```excel
=SWITCH(expression, value1, result1, [value2, result2], ..., [default])
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/SWITCH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `expression` | Yes | The value to test, such as a cell reference or a formula result. |
| `value1` | Yes | The first value to compare with the expression. Microsoft allows up to 126 value and result pairs. |
| `result1` | Yes | The value returned when `value1` matches the expression. Every value needs a result. |
| `value2, result2` | No | Additional pairs, checked in order when the earlier values do not match. |
| `default` | No | The value returned when nothing matches. It must be the last argument. Without it, an unmatched expression returns `#N/A`. |

### Return Value

The result paired with the first matching value. When no value matches, SWITCH returns the default if one is given, or `#N/A` if none is given.

## Examples

### Example 1: Department Code Translation

Cell `A2` holds `2`.

```excel
=SWITCH(A2, 1, "Sales", 2, "Marketing", 3, "Engineering", 4, "Finance", "Unknown")
```

**Result:** `Marketing`

The expression matches the second value, so its result is returned. A code such as `9` would return the default, `Unknown`.

### Example 2: Nested IF Versus SWITCH

Cell `A2` holds `G`. Both formulas return the same color.

```excel
=IF(A2="R", "Red", IF(A2="G", "Green", IF(A2="B", "Blue", "Unknown")))
```

```excel
=SWITCH(A2, "R", "Red", "G", "Green", "B", "Blue", "Unknown")
```

**Result:** `Green`

The SWITCH version has one value and one result per line when you format it with line breaks in the formula bar. Adding a fourth color means adding one pair, not one more level of nesting.

<!-- Image 2: Nested IF Versus SWITCH. See Images/Logical/SWITCH.md -->

### Example 3: Several Values With the Same Result

Cell `B2` holds the three-letter day abbreviation `Sat`.

```excel
=SWITCH(B2, "Mon", "Weekday", "Tue", "Weekday", "Wed", "Weekday", "Thu", "Weekday", "Fri", "Weekday", "Sat", "Weekend", "Sun", "Weekend", "Unknown")
```

**Result:** `Weekend`

Several values can share one result. Each pair is still separate, so the list is easy to extend.

### Example 4: No Default Supplied

Cell `A2` holds `5`, which is not in the list.

```excel
=SWITCH(A2, 1, "Low", 2, "Medium", 3, "High")
```

**Result:** `#N/A`

Without a default, an unmatched expression returns `#N/A`. Some teams keep this on purpose to flag missing codes. Most workbooks should add a default instead.

### Example 5: Returning Numbers for a Calculation

Cell `A2` holds `10` and cell `B2` holds `kg`.

```excel
=A2*SWITCH(B2, "kg", 2.205, "lb", 1, "oz", 0.0625, 0)
```

**Result:** `22.05`

SWITCH can return numbers as well as text. The conversion factor for kilograms is 2.205 pounds, so 10 kg becomes 22.05 lb. The final `0` makes an unknown unit return 0 instead of a wrong conversion.

### Example 6: Range Tests With TRUE as the Expression

Cell `A2` holds a test score of `85`.

```excel
=SWITCH(TRUE, A2>=90, "A", A2>=80, "B", A2>=70, "C", "F")
```

**Result:** `B`

Each value is a condition that returns TRUE or FALSE, and the first TRUE wins. IFS is clearer for this kind of grading, so use this pattern only when a SWITCH is already required.

## Story Problems

### Problem 1: Pickup Store Labels

A retailer exports units sold by store code in `A1:B6`.

| Store Code | Units Sold |
| --- | --- |
| 1 | 40 |
| 3 | 25 |
| 2 | 35 |
| 9 | 18 |
| 4 | 42 |

**Task:** In column C, label each row with its store name: 1 is Downtown, 2 is Airport, 3 is Mall, and 4 is Harbor. Any other code should read Unknown Store. Then count the rows that show Unknown Store.

**Solution:**

```excel
=SWITCH(A2, 1, "Downtown", 2, "Airport", 3, "Mall", 4, "Harbor", "Unknown Store")
```

```excel
=COUNTIF(C2:C6, "Unknown Store")
```

**Answer:** `1`. Only store code 9 is missing from the list, so only that row returns Unknown Store.

### Problem 2: Membership Discounts

A club gives discounts by membership level. The level code is in column B and the order total is in column C.

| Member | Level | Order Total |
| --- | --- | --- |
| Ana | G | 200 |
| Ben | S | 150 |
| Cy | B | 90 |
| Dee | X | 300 |
| Eli | S | 80 |

**Task:** In column D, calculate each discount with SWITCH: G earns 15%, S earns 10%, B earns 5%, and any other level earns 0%. Then total the discounts.

**Solution:**

```excel
=C2*SWITCH(B2, "G", 0.15, "S", 0.10, "B", 0.05, 0)
```

```excel
=SUM(D2:D6)
```

**Answer:** `57.5`. The discounts are 30 (Ana), 15 (Ben), 4.5 (Cy), 0 (Dee), and 8 (Eli), which total 57.5.

<!-- Image 3: Discount Tiers Worksheet. See Images/Logical/SWITCH.md -->

## Use Cases

### Department Code Labels

**Scenario:** An HR export stores each employee's department as a number, but the report needs the department name.

```excel
=SWITCH(B2, 10, "Operations", 20, "Finance", 30, "People", "Check Code")
```

**Why It Works:** Each code appears once beside its label, and the default flags any unknown code so it does not reach the report unnoticed.

### Discount Tiers

**Scenario:** A membership program sets a discount for each level, and the discount must update when a level code changes.

```excel
=C2*SWITCH(B2, "G", 0.15, "S", 0.10, "B", 0.05, 0)
```

**Why It Works:** The zero default gives unrecognized levels no discount, which is visible in the totals. Filter the column for 0 to find level codes that need correcting.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | No value matches and no default was given. | Add a default as the last argument. |
| Unexpected default | The expression has extra spaces or hidden characters, so it does not match the value. | Wrap the expression in TRIM, such as `=SWITCH(TRIM(A2), ...)`. |
| `#NAME?` | The version of the spreadsheet program does not include SWITCH. | Use nested IF or a lookup table instead. |
| Wrong result | The same value appears twice in the list. | SWITCH returns the first match, so remove or correct the duplicate. |
| Formula rejected | More than 126 value and result pairs were entered in Excel. | Move the mapping into a lookup table. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2019 and later, Excel 2021, Excel 2024, Microsoft 365, and Excel for the web | Up to 126 value and result pairs. Without a default, no match returns `#N/A`. |
| Google Sheets | Available | Same expression, value and default pattern. The Google page does not state the no-match result without a default, so include a default. |

## Tips and Best Practices

- Always include a default so an unexpected code shows a clear label instead of `#N/A`.
- Use SWITCH for discrete codes and IFS for range tests.
- Wrap the expression in TRIM when the codes come from an export that may contain extra spaces.
- Move a mapping into a lookup table once it grows past about 15 pairs, so the formula stays short.
- Keep the value list in one order that a reviewer can scan, such as numeric or alphabetical.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSE](../Lookup%20%26%20Reference/CHOOSE.md) | Returns a value by its position in a list, useful when the codes are 1, 2, 3 in sequence. |
| [IF](IF.md) | A single test with two outcomes; use it for one condition. |
| [IFNA](IFNA.md) | Replaces the `#N/A` that SWITCH returns when no default is given. |
| [IFS](IFS.md) | Tests several independent conditions, including ranges. |
| [VLOOKUP](../Lookup%20%26%20Reference/VLOOKUP.md) | Looks up values from a table on the sheet, useful when the mapping is stored in cells. |
| [XLOOKUP](../Lookup%20%26%20Reference/XLOOKUP.md) | Looks up values from a table and has a built-in argument for missing values. |

## Official Documentation

- [Microsoft Support: SWITCH function](https://support.microsoft.com/en-us/excel/functions/switch-function)
- [Google Docs Editors Help: SWITCH](https://support.google.com/docs/answer/7013690)
