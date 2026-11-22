---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Conditional Logic
use-case:
  - Cold Chain Compliance
  - Grade Band Assignment
related:
  - AND
  - FILTER
  - GTE
  - IF
  - LTE
level: 2
source:
  - https://support.google.com/docs/answer/10538337
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Is Between
tags:
  - comparison
  - logical
  - range-check
  - sheets
---

# ISBETWEEN

## Description

**ISBETWEEN** tests whether a value falls between a lower value and an upper value. It returns `TRUE` when the value is inside the range and `FALSE` when it is outside. By default both boundaries are included, so a value equal to either limit counts as inside the range.

Use ISBETWEEN for range checks such as acceptable temperatures, grade bands, tolerance limits and age eligibility. Two optional arguments control whether each boundary belongs to the range. Setting one to `FALSE` makes that end exclusive, so a value equal to that boundary returns `FALSE`.

ISBETWEEN is specific to Google Sheets. Microsoft Excel has no equivalent function, so Excel users combine two comparisons with AND. Write the bounds in the order lower, then upper, because the function tests the range from the lower value up to the upper value.

## Syntax

```excel
=ISBETWEEN(value_to_compare, lower_value, upper_value, [lower_value_is_inclusive], [upper_value_is_inclusive])
```

<!-- Image 1: Range Test Anatomy. See Images/Google-specific/ISBETWEEN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value_to_compare` | Yes | The value being tested, usually a cell reference. |
| `lower_value` | Yes | The lower boundary of the range. |
| `upper_value` | Yes | The upper boundary of the range. |
| `lower_value_is_inclusive` | No | `TRUE` when the lower boundary belongs to the range. The default is `TRUE`. |
| `upper_value_is_inclusive` | No | `TRUE` when the upper boundary belongs to the range. The default is `TRUE`. |

### Return Value

A logical value: `TRUE` when `value_to_compare` lies within the range, and `FALSE` when it lies outside. The optional arguments decide whether a value exactly equal to a boundary counts as inside.

## Examples

All examples test readings against a room temperature range of 18 to 24 degrees Celsius.

| Sensor | Reading |
| --- | --- |
| Lab A | 21 |
| Lab B | 24 |
| Lab C | 25 |
| Lab D | 17 |

### Example 1: Reading Inside the Range

```excel
=ISBETWEEN(B2, 18, 24)
```

**Result:** `TRUE`

Lab A reads 21, which is between 18 and 24.

### Example 2: Reading Equal to the Upper Limit

```excel
=ISBETWEEN(B3, 18, 24)
```

**Result:** `TRUE`

Lab B reads exactly 24. Both boundaries are included by default, so the reading passes.

### Example 3: Exclude the Upper Limit

```excel
=ISBETWEEN(24, 18, 24, TRUE, FALSE)
```

**Result:** `FALSE`

The upper boundary is exclusive, so a reading of exactly 24 falls outside the range.

### Example 4: Exclude the Lower Limit

```excel
=ISBETWEEN(18, 18, 24, FALSE, TRUE)
```

**Result:** `FALSE`

The lower boundary is exclusive, so a reading of exactly 18 falls outside the range.

<!-- Image 2: Boundary Inclusion Results. See Images/Google-specific/ISBETWEEN.md -->

### Example 5: Label Readings With IF

```excel
=IF(ISBETWEEN(B4, 18, 24), "In range", "Out of range")
```

**Result:** `Out of range`

Lab C reads 25, which is above the range. IF converts the logical result into a label.

## Story Problems

### Problem 1: Vaccine Storage Temperature

A clinic keeps vaccines between 2 and 8 degrees Celsius, and both limits are acceptable. Readings are in column B of `A1:B4`.

| Fridge | Reading |
| --- | --- |
| Fridge 1 | 5.2 |
| Fridge 2 | 8.4 |
| Fridge 3 | 2.0 |

**Task:** In column C, show whether each fridge is within the acceptable range.

**Solution:**

```excel
=ISBETWEEN(B2, 2, 8)
```

Fill the formula down to C4.

**Answer:** `TRUE`, `FALSE` and `TRUE` for Fridges 1, 2 and 3. Fridge 2 is above 8 degrees, and Fridge 3 is exactly at the lower limit, which the default allows.

### Problem 2: Grade Band for Scores Above 60 Up to 70

A school gives a grade band to scores that are above 60 and no higher than 70. A score of exactly 60 is not in the band, but a score of exactly 70 is. Scores are in column B of `A1:B5`.

| Student | Score |
| --- | --- |
| Ada | 60 |
| Ben | 66 |
| Cy | 70 |
| Dee | 71 |

**Task:** In column C, show `TRUE` for each score in the band.

**Solution:**

```excel
=ISBETWEEN(B2, 60, 70, FALSE, TRUE)
```

Fill the formula down to C5.

**Answer:** `FALSE`, `TRUE`, `TRUE` and `FALSE` for Ada, Ben, Cy and Dee. The lower limit is exclusive, so Ada's score of 60 is outside the band, and the upper limit is inclusive, so Cy's 70 is inside.

## Use Cases

### Cold Chain Compliance

**Scenario:** A pharmacy logs temperature readings and needs an alert whenever a reading leaves the approved range.

```excel
=IF(ISBETWEEN(C2, 2, 8), "OK", "Alert")
```

**Why It Works:** Both limits are inclusive by default, so a reading at exactly 2 or 8 degrees passes. The alert fires only for readings that are truly outside the range.

### Grade Band Assignment

**Scenario:** A teacher assigns a grade band to each score and needs the boundaries to follow the school's written policy.

```excel
=ISBETWEEN(B2, 60, 70, FALSE, TRUE)
```

**Why It Works:** Setting the lower argument to `FALSE` excludes exactly 60, while the upper argument of `TRUE` keeps 70 in the band. The two optional arguments match the policy wording.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Boundary value gives an unexpected result | The default inclusive setting does not match the rule. | Set the lower or upper argument to `FALSE` for an exclusive end. |
| Every result is `FALSE` | The lower and upper values are in the wrong order. | Put the lower limit before the upper limit. |
| Text in place of a number | A reading is stored as text, such as `21 C`. | Store readings as numbers in a separate column. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use `=AND(B2>=18, B2<=24)` for an inclusive range. Use `>` or `<` for an exclusive end. |
| Google Sheets | Available | Both optional arguments default to `TRUE`. |

## Tips and Best Practices

- Keep the lower and upper limits in their own cells, so the policy can change without editing each formula.
- Write the inclusion arguments explicitly when the rule depends on them, so a reviewer can see the intent.
- Use ISBETWEEN with FILTER to list only the records inside a range.
- Store the limits as numbers, not as text, before comparing.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AND](../Logical/AND.md) | Combines two comparisons, the Excel approach to a range test. |
| [GTE](GTE.md) | Tests whether a value is at least a lower limit. |
| [LTE](LTE.md) | Tests whether a value is at most an upper limit. |
| [IF](../Logical/IF.md) | Returns a label or value based on the range test. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the rows whose values fall inside the range. |

## Official Documentation

- [Google Docs Editors Help: ISBETWEEN](https://support.google.com/docs/answer/10538337)
