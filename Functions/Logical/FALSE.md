---
domain: Spreadsheet Functions
category: Logical
subcategory: Boolean Values
purpose:
  - Conditional Logic
use-case:
  - Blank Row Handling
  - Default Flag Values
  - Placeholder Results
related:
  - AND
  - IF
  - NOT
  - OR
  - 'TRUE'
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/false-function
  - https://support.google.com/docs/answer/3093302
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Boolean False
  - Logical False
tags:
  - boolean
  - excel
  - flags
  - logical
  - sheets
---

# FALSE

## Description

**FALSE** returns the logical value FALSE. It takes no arguments, so the formula is always written as `=FALSE()` with empty parentheses. The result behaves like any other logical value, so it can be used in IF, AND, OR, and NOT tests and in calculations, where FALSE counts as 0.

In most sheets you do not need the function, because typing the word FALSE directly produces the same value in Microsoft Excel. The function is useful when a formula must return FALSE as its result, such as the "no" branch of an IF that also contains other logic. It also helps when a workbook is shared with other spreadsheet programs that expect the function form.

Google Sheets usually converts a typed FALSE to the logical value, so the function is rarely required there either. Use the function for clarity in a formula, or to make a result explicit in a flag column.

The opposite constant is [TRUE](TRUE.md). When FALSE needs to be the result of a test, [IF](IF.md) provides the branching. When FALSE is one input to a logical test, [AND](AND.md), [OR](OR.md), and [NOT](NOT.md) combine it with other conditions.

## Syntax

```excel
=FALSE()
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/FALSE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| None | Not applicable | The function takes no arguments. Keep the empty parentheses. |

### Return Value

The logical value FALSE. It is not the text "FALSE", so a cell that holds it can be used directly in a test. In arithmetic, FALSE is treated as 0.

## Examples

### Example 1: Basic Result

```excel
=FALSE()
```

**Result:** `FALSE`

The formula returns the logical value. Typing the word FALSE in a cell gives the same result in Microsoft Excel.

### Example 2: Flag for a Blank Row

```excel
=IF(A2="", FALSE(), A2>100)
```

**Result:** `FALSE` when A2 is empty, and `TRUE` when A2 holds 150

When the row is empty, the formula returns FALSE instead of comparing a blank cell. This keeps blank rows from appearing as TRUE in a count of active records.

### Example 3: Replacing a Text Error With FALSE

```excel
=IFERROR(VALUE(A2), FALSE())
```

**Result:** `FALSE` when A2 holds "n/a"

VALUE cannot convert "n/a", so IFERROR returns FALSE. The result is a clear logical value that later tests can read.

### Example 4: Choosing Between Two Messages

```excel
=IF(FALSE(), "Yes", "No")
```

**Result:** `No`

The test is always FALSE, so the second message is returned. Use the same pattern when a branch should be fixed to one outcome, such as while a feature is switched off.

### Example 5: FALSE in Arithmetic

```excel
=FALSE()+10
```

**Result:** `10`

FALSE counts as 0 in arithmetic, so adding it to 10 returns 10. This is the basis of formulas that multiply a flag by a value to include or exclude it.

## Story Problems

### Problem 1: Active Customers

A shop lists customers and the number of orders each placed this month. A blank order count means the row is not a customer yet. The shop wants TRUE for customers with at least one order and FALSE for every other row.

| Customer | Orders |
| --- | --- |
| Ada | 4 |
| Ben | |
| Cy | 0 |
| Dee | 7 |

**Task:** Enter the formula in C2, fill it down to C5, and count the customers who show TRUE.

**Solution:**

```excel
=IF(B2="", FALSE(), B2>0)
```

**Answer:** `2` customers show TRUE, Ada and Dee. Ben is blank and Cy has no orders, so both show FALSE.

<!-- Image 2: Flag Column Results. See Images/Logical/FALSE.md -->

### Problem 2: Readings That Are Numbers

A sensor export stores values as text. Some are numbers, one is a note, and one cell is empty. The team wants TRUE for each usable positive reading.

| Reading |
| --- |
| 12 |
| n/a |
| 7 |
| |

**Task:** Enter the formula in B2, fill it down to B5, and count the TRUE results.

**Solution:**

```excel
=IFERROR(A2*1>0, FALSE())
```

**Answer:** `2` readings are usable, 12 and 7. The note "n/a" cannot be multiplied, so IFERROR returns FALSE for it. The empty cell counts as 0 in the multiplication, so its test is FALSE as well.

## Use Cases

### Blank Row Handling

**Scenario:** A contact list uses a helper column to mark rows that have an email address and a name. Rows that are still being typed should not count.

```excel
=IF(AND(A2<>"", B2<>""), TRUE, FALSE())
```

**Why It Works:** The result is always a logical value, so a COUNTIF for TRUE gives a reliable count of complete rows. The function form makes the FALSE branch explicit to whoever reads the formula.

### Default Flag Values

**Scenario:** A task tracker has a flag column that marks overdue items. Items without a due date should not be flagged.

```excel
=IF(C2="", FALSE(), C2<TODAY())
```

**Why It Works:** Items with no due date keep a FALSE flag, so they are excluded from overdue filters and totals.

### Placeholder Results

**Scenario:** A template contains a feature switch that is not yet ready. The formula keeps the branch in place so the team can enable it later by changing one cell.

```excel
=IF(FeatureOn, A2*2, FALSE())
```

**Why It Works:** While the switch is off, the cell shows FALSE instead of an error or an empty result, and the formulas that read it still receive a logical value.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error after adding arguments | An argument was typed inside the parentheses. | Remove the argument. FALSE() takes none. |
| Text "FALSE" instead of a logical value | The cell is formatted as text, or the value was typed with an apostrophe. | Clear the text format and enter the formula again. |
| Count returns 0 for FALSE | The flag cells hold text such as "FALSE", not the logical value. | Rewrite the formula with FALSE() so the cell stores a logical value, then count with COUNTIF. |
| Value is 0 instead of FALSE | The flag was added or multiplied, which turns it into a number. | Test the flag with IF instead of doing arithmetic on it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Typing FALSE directly gives the same result. The function is included for compatibility with other programs. |
| Google Sheets | Available | Usually converts a typed FALSE, so the function is rarely needed. Returns the logical value FALSE. |

## Tips and Best Practices

- Use the function form in formulas that must read clearly, such as the FALSE branch of an IF.
- Return FALSE rather than an empty string when the result is used in a logical test.
- Keep flags as logical values so filters, COUNTIF, and SUMPRODUCT treat them consistently.
- Use TRUE and FALSE results together, such as a TRUE branch and a FALSE branch, when building flag columns.
- Test a flag column with one blank row, one error, and one value of each result to confirm the count.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AND](AND.md) | Returns FALSE when any argument is FALSE. |
| [IF](IF.md) | Returns FALSE from its own test or from the FALSE branch. |
| [NOT](NOT.md) | Reverses FALSE to TRUE, and TRUE to FALSE. |
| [OR](OR.md) | Returns FALSE only when every argument is FALSE. |
| [TRUE](TRUE.md) | Returns the opposite logical value. |

## Official Documentation

- [Microsoft Support: FALSE function](https://support.microsoft.com/en-us/excel/functions/false-function)
- [Google Docs Editors Help: FALSE](https://support.google.com/docs/answer/3093302)
