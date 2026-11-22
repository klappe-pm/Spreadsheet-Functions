---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Conditional Logic
use-case:
  - Budget Underrun Flags
  - Reorder Point Alerts
related:
  - GT
  - GTE
  - IF
  - LTE
  - NE
level: 1
source:
  - https://support.google.com/docs/answer/3093596
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Less Than
tags:
  - comparison
  - operator
  - sheets
---

# LT

## Description

**LT** compares two values and returns `TRUE` when the first is strictly less than the second. It returns `FALSE` otherwise. The function is the named form of the `<` operator, so `=LT(B2, C2)` and `=B2<C2` produce the same result.

Use LT when the comparison should be written as a function name, for example in a formula that a script or template generates. The logical result works directly inside IF, AND, OR and FILTER.

LT is a strict test. A value equal to the second argument returns `FALSE`. For a test that includes the boundary, use LTE. Microsoft Excel has no LT function, so Excel users write the `<` operator instead.

## Syntax

```excel
=LT(value1, value2)
```

<!-- Image 1: Operator Syntax Anatomy. See Images/Google-specific/LT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The value to test. Usually a cell reference or a number. |
| `value2` | Yes | The value that `value1` is compared against. |

### Return Value

A logical value: `TRUE` when `value1` is less than `value2`, and `FALSE` when it is equal or greater. LT takes exactly two arguments.

## Examples

All examples use this budget check.

| Department | Spend | Budget |
| --- | --- | --- |
| Operations | 4200 | 5000 |
| Marketing | 5300 | 5000 |
| Finance | 5000 | 5000 |

### Example 1: Spend Below Budget

```excel
=LT(B2, C2)
```

**Result:** `TRUE`

Operations spent 4200, which is less than its 5000 budget.

### Example 2: Spend Over Budget

```excel
=LT(B3, C3)
```

**Result:** `FALSE`

Marketing spent 5300, which is more than its budget.

### Example 3: Equal Values Fail

```excel
=LT(B4, C4)
```

**Result:** `FALSE`

Finance spent exactly the budget. A strict test does not count an equal value as less.

<!-- Image 2: Budget Comparison Results. See Images/Google-specific/LT.md -->

### Example 4: Compare With a Literal Number

```excel
=LT(4200, 5000)
```

**Result:** `TRUE`

Both values are typed directly into the formula.

### Example 5: Flag Underspend With IF

```excel
=IF(LT(B2, C2), "Under budget", "Review")
```

**Result:** `Under budget`

IF turns the logical result into a label that managers can filter.

## Story Problems

### Problem 1: Stock Below the Reorder Point

A shop reorders an item when its stock falls below the reorder point. Stock is in column B and reorder points are in column C of `A1:C4`.

| Item | Stock | Reorder Point |
| --- | --- | --- |
| Mug | 14 | 20 |
| Tote | 25 | 25 |
| Pen | 8 | 12 |

**Task:** In column D, show `TRUE` for each item that must be reordered now.

**Solution:**

```excel
=LT(B2, C2)
```

Fill the formula down to D4.

**Answer:** `TRUE`, `FALSE` and `TRUE` for Mug, Tote and Pen. The tote is exactly at its reorder point, so it does not need an order yet under a strict test.

### Problem 2: Delivery Lead Time Under Five Days

A supplier must deliver within fewer than five days to qualify for a rush bonus. Lead times are in column B of `A1:B4`, and the limit of 5 is typed into cell `E1`.

| Order | Lead Time (Days) |
| --- | --- |
| A-101 | 3 |
| A-102 | 5 |
| A-103 | 4 |

**Task:** In column C, show whether each order qualifies.

**Solution:**

```excel
=LT(B2, $E$1)
```

Fill the formula down to C4.

**Answer:** `TRUE`, `FALSE` and `TRUE` for A-101, A-102 and A-103. A five-day delivery is not fewer than five days, so A-102 does not qualify.

## Use Cases

### Budget Underrun Flags

**Scenario:** A finance lead highlights departments that have spent less than their approved budget so that surplus can be reviewed.

```excel
=IF(LT(B2, C2), "Underspent", "")
```

**Why It Works:** The formula returns a label only when spend is strictly below budget, so departments exactly at budget stay blank.

### Reorder Point Alerts

**Scenario:** A warehouse team lists every item that needs a purchase order today.

```excel
=FILTER(A2:A20, ARRAYFORMULA(LT(B2:B20, C2:C20)))
```

**Why It Works:** ARRAYFORMULA makes LT compare each stock level with its reorder point, and FILTER returns only the items where the test is `TRUE`.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for a value that looks smaller | One side is text, such as a number typed as text. | Convert the text with VALUE or retype the source cell as a number. |
| Equal values return `FALSE` | LT is strict and excludes the boundary. | Use LTE when equal values should pass. |
| Formula does not calculate | The function has fewer or more than two arguments. | Provide exactly two values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use the `<` operator, for example `=B2<C2`. |
| Google Sheets | Available | Returns the same result as the `<` operator. |

## Tips and Best Practices

- Choose LT or LTE based on whether the boundary value should count as a match.
- Keep thresholds in their own cells and use absolute references such as `$E$1` so that one edit updates every row.
- Check that compared values are numbers, not text, before relying on the result.
- Use LT with FILTER to pull out only the rows that fail a limit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LTE](LTE.md) | Less than or equal. Includes the boundary value. |
| [GT](GT.md) | Strictly greater than. The opposite test. |
| [GTE](GTE.md) | Greater than or equal. The opposite test with the boundary included. |
| [NE](NE.md) | Tests whether two values differ. |
| [IF](../Logical/IF.md) | Uses the logical result to return a chosen value. |

## Official Documentation

- [Google Docs Editors Help: LT](https://support.google.com/docs/answer/3093596)
