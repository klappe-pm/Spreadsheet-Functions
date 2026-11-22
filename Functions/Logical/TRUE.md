---
domain: Spreadsheet Functions
category: Logical
subcategory: Boolean Values
purpose:
  - Conditional Logic
use-case:
  - Conditional Flag Output
  - Default Flag Values
  - Logical Test Data
related:
  - AND
  - 'FALSE'
  - IF
  - NOT
  - OR
  - XOR
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/true-function
  - https://support.google.com/docs/answer/3093307
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - boolean
  - excel
  - logical
  - sheets
---

# TRUE

## Description

**TRUE** returns the logical value TRUE. It takes no arguments, so the formula is `=TRUE()` with empty parentheses. In most formulas you can type the word TRUE directly, and both Excel and Google Sheets read it as the same logical value.

Microsoft describes the function as provided mainly for compatibility with other spreadsheet programs. Use it when a formula should show the logical value explicitly, when a formula is moved from another program, or when you want the output of an IF branch to be a logical value rather than a text label.

The function is simple, but it matters in logical formulas. A TRUE result can feed another function such as AND, OR, NOT or XOR, or it can be counted with COUNTIF to tally flags.

## Syntax

```excel
=TRUE()
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/TRUE.md -->

### Parameters

The function takes no parameters. Leave the parentheses empty.

### Return Value

The logical value TRUE. The function does not produce an error.

## Examples

### Example 1: Basic Call

```excel
=TRUE()
```

**Result:** `TRUE`

The function returns the logical value TRUE. The result is a logical value, not the text "TRUE".

### Example 2: Explicit Output From IF

Cell `B2` holds `120`.

```excel
=IF(B2>=100, TRUE(), FALSE())
```

**Result:** `TRUE`

The condition is met, so IF returns TRUE(). Because B2>=100 already returns TRUE or FALSE, this formula gives the same answer as the comparison alone. Use the longer form when the output must be written as an explicit IF branch.

### Example 3: Typed Literal Instead of the Function

Cell `B2` holds `Yes`.

```excel
=IF(B2="Yes", TRUE, FALSE)
```

**Result:** `TRUE`

Typing TRUE and FALSE as literals gives the same result as the functions. Most workbooks use the literal form because it is shorter.

### Example 4: Reversing a Logical Value

```excel
=NOT(TRUE())
```

**Result:** `FALSE`

NOT reverses its argument. Since TRUE() returns TRUE, NOT returns FALSE.

## Story Problems

### Problem 1: Loan Pre-Approval Flags

A lender marks an applicant as pre-approved when the credit score is at least 650. The scores are in `B2:B5`, and the flags go in column C.

| Applicant | Credit Score |
| --- | --- |
| Ana | 700 |
| Ben | 610 |
| Cy | 655 |
| Dee | 540 |

**Task:** In column C, return TRUE for each applicant with a score of at least 650, using TRUE() and FALSE() in the IF branches. Then count how many applicants are pre-approved.

**Solution:**

```excel
=IF(B2>=650, TRUE(), FALSE())
```

```excel
=COUNTIF(C2:C5, TRUE)
```

**Answer:** `2`. Ana (700) and Cy (655) are at or above 650. Ben (610) and Dee (540) are below it.

<!-- Image 2: Pre-Approval Flags. See Images/Logical/TRUE.md -->

### Problem 2: Active Subscriptions

A software team tracks account status in `A1:B6`, with the status in column B. An account counts as active when its status is `Active`.

| Account | Status |
| --- | --- |
| Acme | Active |
| Birch | Paused |
| Cedar | Active |
| Dune | Cancelled |
| Elm | Active |

**Task:** In column C, mark each account TRUE when its status is `Active`, then count the TRUE values.

**Solution:**

```excel
=IF(B2="Active", TRUE, FALSE)
```

```excel
=COUNTIF(C2:C6, TRUE)
```

**Answer:** `3`. Acme, Cedar and Elm are active. Birch is paused and Dune is cancelled.

## Use Cases

### Conditional Flag Output

**Scenario:** A report needs a logical flag for each order, so other formulas can filter or count the orders that meet a rule.

```excel
=IF(C2>=500, TRUE(), FALSE())
```

**Why It Works:** Each row returns a true logical value rather than a text label, so COUNTIF and filters can use the result directly.

### Default Flag Values

**Scenario:** A checklist template starts every item as included, and a reviewer changes the few items that should be excluded.

```excel
=IF(D2="", TRUE(), D2)
```

**Why It Works:** A blank cell gets TRUE by default, while a value entered by the reviewer is kept. Check that the entered values are TRUE or FALSE so the flags stay consistent.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The function name is misspelled, such as `TURE()`. | Correct the spelling. |
| Text `TRUE` instead of a logical value | The result was joined to text with `&`, which turns it into text. | Keep the logical value, or use IF to create a text label on purpose. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 through Excel 2024, Microsoft 365, and Excel for the web | Takes no arguments. Microsoft provides it mainly for compatibility with other spreadsheet programs. |
| Google Sheets | Available | Takes no arguments. Google Sheets usually converts the TRUE literal to the same logical value. |

## Tips and Best Practices

- Type TRUE directly in most formulas and use TRUE() when the explicit function form makes the formula clearer or when porting from another program.
- Use TRUE and FALSE in IF branches when the output must be a logical value that other formulas can test.
- Keep flags as logical values, not text, so COUNTIF and filters behave predictably.
- Use NOT with TRUE() only when a reversed logical value is needed; comparing with the opposite operator is often shorter.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AND](AND.md) | Returns TRUE only when every condition is TRUE. |
| [FALSE](FALSE.md) | Returns the logical value FALSE, the counterpart of TRUE. |
| [IF](IF.md) | Chooses between TRUE and FALSE or between other outputs. |
| [NOT](NOT.md) | Reverses a logical value. |
| [OR](OR.md) | Returns TRUE when at least one condition is TRUE. |
| [XOR](XOR.md) | Returns TRUE when an odd number of conditions are TRUE. |

## Official Documentation

- [Microsoft Support: TRUE function](https://support.microsoft.com/en-us/excel/functions/true-function)
- [Google Docs Editors Help: TRUE](https://support.google.com/docs/answer/3093307)
