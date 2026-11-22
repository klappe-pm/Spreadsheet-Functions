---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Conditional Logic
use-case:
  - Budget Overrun Checks
  - Target Tracking
  - Threshold Alerts
related:
  - EQ
  - GTE
  - IF
  - LT
  - LTE
  - NE
level: 2
source:
  - https://support.google.com/docs/answer/3098240
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Greater Than Test
tags:
  - comparison
  - logic
  - operators
  - sheets
---

# GT

## Description

**GT** tests whether the first value is strictly greater than the second. It returns `TRUE` when `value1` is larger than `value2` and `FALSE` otherwise. It is equivalent to the greater than operator (`>`), so `=GT(B2, C2)` and `=B2>C2` give the same answer.

Use GT when a threshold test should be written in function form, for example inside a formula that already uses function syntax. Most sheets use the `>` operator directly. The word strictly matters: when the two values are equal, GT returns `FALSE`. For a test that includes equal values, use GTE instead.

The official help page documents the rule for numbers. It does not state how text values compare, so test a sample before relying on GT for text. GT is available only in Google Sheets.

<!-- Image 1: GT Threshold Test. See Images/Google-specific/GT.md -->

## Syntax

```excel
=GT(value1, value2)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The value to test. It is treated as the left side of the greater than comparison. |
| `value2` | Yes | The value to test against. The function asks whether `value1` is strictly greater than it. |

### Return Value

`TRUE` when `value1` is strictly greater than `value2`, and `FALSE` when it is equal to or less than `value2`. The result is a logical value that IF, COUNTIF and similar functions can use.

## Examples

### Example 1: Spending Above a Budget

```excel
=GT(B2, C2)
```

**Result:** `TRUE` when B2 holds `620` and C2 holds `600`.

The actual spend is above the budget, so the test is true.

### Example 2: Equal Values Return False

```excel
=GT(B3, C3)
```

**Result:** `FALSE` when B3 and C3 both hold `300`.

Because GT is strict, two equal values never pass the test. Use GTE when equal values should count.

### Example 3: Typed Numbers

```excel
=GT(2, 3)
```

**Result:** `FALSE`

Two is not greater than three, so the test returns FALSE.

### Example 4: Flagging a Row With a Message

```excel
=IF(GT(B2, C2), "Over budget", "Within budget")
```

**Result:** `Over budget` when B2 is greater than C2, and `Within budget` otherwise.

Wrapping GT in IF turns the test into a readable label for a report.

## Story Problems

### Problem 1: Monthly Budget Check

Four departments spent the amounts in column B against the budgets in column C. The finance lead wants to count how many departments went over budget.

| Department | Spent | Budget |
| --- | --- | --- |
| Design | 450 | 500 |
| Field | 620 | 600 |
| Support | 300 | 300 |
| Sales | 915 | 900 |

**Task:** Fill `D2:D5` with a test for each department, then count the departments over budget.

**Solution:**

```excel
=GT(B2, C2)
```

Fill this formula down `D2:D5`, then count the true results with `=COUNTIF(D2:D5, TRUE)`.

**Answer:** `2`, because Field (620 against 600) and Sales (915 against 900) are over budget. Support spent exactly its budget, so GT returns FALSE for it.

<!-- Image 2: GT Budget Results Column. See Images/Google-specific/GT.md -->

### Problem 2: Sales Targets Reached

A rep has a monthly target of 40 deals. Five months of results are in column B.

| Month | Deals Closed |
| --- | --- |
| January | 38 |
| February | 44 |
| March | 40 |
| April | 52 |
| May | 39 |

**Task:** Count the months where the deals closed were strictly above the target of 40, with the target typed into `D1` and the test in `C2:C6`.

**Solution:**

```excel
=GT(B2, $D$1)
```

**Answer:** `2`, because February (44) and April (52) are above 40. March hit exactly 40, which GT does not count.

## Use Cases

### Budget Overrun Checks

**Scenario:** A project manager reviews cost reports and needs to see which cost lines have passed their approved amount.

```excel
=IF(GT(B2, C2), "Review", "On track")
```

**Why It Works:** The label appears only when actual cost is strictly above the approved amount. Equal values stay On track, which matches the rule that a budget exactly used is not an overrun.

### Target Tracking

**Scenario:** A sales manager wants the number of reps who beat quota in a region.

```excel
=COUNTIF(C2:C20, TRUE)
```

**Why It Works:** Place a GT test in column C for each rep, then count the TRUE results. The target can sit in a single labeled cell so changing it updates every test.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected `FALSE` for equal values | GT is strict and does not count equal values. | Use GTE when equal values should pass. |
| Unexpected `FALSE` | A number is stored as text. | Convert the text with VALUE, or re-enter the number. |
| Unexpected result for text | The official page does not document text comparison. | Test a few sample rows first, or compare cleaned values with a known rule. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available. The closest alternative is the greater than operator, `=B2>C2`. | Excel has no GT function. The operator gives the same strict comparison. |
| Google Sheets | Available | Equivalent to the `>` operator. Returns TRUE only when the first value is strictly greater. |

## Tips and Best Practices

- Use `=B2>C2` in workbooks that Excel users open, because the operator works in both programs.
- Use GTE for a test that should include the threshold itself, and GT for a strictly greater test.
- Store thresholds in one labeled cell and reference it, so a change to the target updates every test.
- Pair GT with COUNTIF or FILTER to count or list the rows that pass.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GTE](GTE.md) | Like GT, but also returns TRUE when the values are equal. |
| [LT](LT.md) | Tests whether the first value is less than the second. |
| [LTE](LTE.md) | Tests whether the first value is less than or equal to the second. |
| [EQ](EQ.md) | Tests whether two values are equal. |
| [NE](NE.md) | Tests whether two values differ. |
| [IF](../Logical/IF.md) | Turns the TRUE or FALSE result into a label or another value. |

## Official Documentation

- [Google Docs Editors Help: GT](https://support.google.com/docs/answer/3098240)
