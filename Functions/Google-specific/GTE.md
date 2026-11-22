---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Conditional Logic
use-case:
  - Minimum Score Approval
  - Sales Quota Checks
related:
  - AND
  - EQ
  - GT
  - IF
  - LTE
  - NE
level: 1
source:
  - https://support.google.com/docs/answer/3093975
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Greater Than or Equal
tags:
  - comparison
  - operator
  - sheets
---

# GTE

## Description

**GTE** compares two values and returns `TRUE` when the first is greater than or equal to the second. It returns `FALSE` otherwise. The function is the named form of the `>=` operator, so `=GTE(B2, C2)` and `=B2>=C2` produce the same result.

Use GTE when the comparison should be written as a function name, for example in a formula that a script or template generates, or when a reviewer finds a named function easier to read than a symbol. The result is a logical value, so it works directly inside IF, AND, OR and FILTER.

GTE tests for a boundary that counts as a match. A value equal to the second argument passes the test. For a strict test that excludes the boundary, use GT. Microsoft Excel has no GTE function, so Excel users write the `>=` operator instead.

## Syntax

```excel
=GTE(value1, value2)
```

<!-- Image 1: Operator Syntax Anatomy. See Images/Google-specific/GTE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The value to test. Usually a cell reference or a number. |
| `value2` | Yes | The value that `value1` is compared against. |

### Return Value

A logical value: `TRUE` when `value1` is greater than or equal to `value2`, and `FALSE` when it is less. GTE takes exactly two arguments.

## Examples

All examples use the figures in this small scorecard.

| Rep | Actual | Target |
| --- | --- | --- |
| Ruiz | 92 | 90 |
| Patel | 88 | 90 |
| Wong | 90 | 90 |

### Example 1: Compare Two Cells

```excel
=GTE(B2, C2)
```

**Result:** `TRUE`

Ruiz beat the target, so 92 is greater than or equal to 90.

### Example 2: A Value Below the Target

```excel
=GTE(B3, C3)
```

**Result:** `FALSE`

Patel's 88 is less than the 90 target.

### Example 3: Equal Values Pass

```excel
=GTE(B4, C4)
```

**Result:** `TRUE`

Wong's 90 exactly matches the target. The boundary value counts as a pass.

<!-- Image 2: Scorecard Comparison Results. See Images/Google-specific/GTE.md -->

### Example 4: Compare With a Literal Number

```excel
=GTE(B2, 100)
```

**Result:** `FALSE`

Ruiz's 92 is below 100, so the test fails.

### Example 5: Label the Result With IF

```excel
=IF(GTE(B2, C2), "Target met", "Below target")
```

**Result:** `Target met`

IF uses the logical value from GTE to choose the label.

## Story Problems

### Problem 1: Quarterly Sales Quota

A sales team earns a bonus when monthly sales reach the quota. Sales are in column B and quotas are in column C of `A1:C4`.

| Rep | Sales | Quota |
| --- | --- | --- |
| Iris | 5200 | 5000 |
| Jonah | 4800 | 5000 |
| Kira | 5000 | 5000 |

**Task:** In column D, show `TRUE` for each rep who met or beat the quota.

**Solution:**

```excel
=GTE(B2, C2)
```

Fill the formula down to D4.

**Answer:** `TRUE`, `FALSE` and `TRUE` for Iris, Jonah and Kira. Kira's sales equal the quota, so the bonus applies.

### Problem 2: Passing Mark Check

A training course requires at least 60 points on the final test. Scores are in column B of `A1:B4`, and the passing mark is in cell `E1`.

| Learner | Score |
| --- | --- |
| Lena | 72 |
| Marco | 58 |
| Noor | 60 |

**Task:** In column C, show whether each learner reached the passing mark held in `E1`.

**Solution:**

```excel
=GTE(B2, $E$1)
```

Fill the formula down to C4, with `E1` containing 60.

**Answer:** `TRUE`, `FALSE` and `TRUE` for Lena, Marco and Noor. Noor's score of 60 meets the mark exactly.

## Use Cases

### Minimum Score Approval

**Scenario:** A certification body approves applicants only when their practice exam score meets the minimum.

```excel
=IF(GTE(B2, $F$1), "Approved", "Retake")
```

**Why It Works:** GTE returns the logical test, and IF turns it into a readable decision. Changing the minimum in `F1` updates every decision at once.

### Sales Quota Checks

**Scenario:** A regional manager reviews whether each territory reached its target and flags any that fell short.

```excel
=IF(GTE(C2, D2), "On track", "Behind")
```

**Why It Works:** Comparing actual sales in C2 with the target in D2 keeps the rule visible in the sheet. Territories that match the target exactly are counted as on track.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for a value that looks equal | One side is text, such as a number typed as text. | Convert the text with VALUE or retype the source cell as a number. |
| Formula does not calculate | The function has fewer or more than two arguments. | Provide exactly two values. |
| Unexpected `FALSE` at the boundary | The test used GT instead of GTE. | Use GTE when equal values should pass. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use the `>=` operator, for example `=B2>=C2`. |
| Google Sheets | Available | Returns the same result as the `>=` operator. |

## Tips and Best Practices

- Use GTE when a named function suits the design, and the `>=` operator when a formula is written by hand.
- Store thresholds in their own cells and reference them with absolute references such as `$F$1`, so one change updates every test.
- Check that numbers are stored as numbers before comparing them; text that looks like a number can fail the test.
- Pair GTE with IF or AND to turn the logical result into labels or combined rules.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GT](GT.md) | Strictly greater than. Excludes the boundary value. |
| [LTE](LTE.md) | Less than or equal. The opposite test. |
| [EQ](EQ.md) | Tests whether two values are equal. |
| [NE](NE.md) | Tests whether two values differ. |
| [IF](../Logical/IF.md) | Uses the logical result to return a chosen value. |
| [AND](../Logical/AND.md) | Combines GTE with other conditions. |

## Official Documentation

- [Google Docs Editors Help: GTE](https://support.google.com/docs/answer/3093975)
