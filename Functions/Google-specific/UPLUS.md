---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Financial Modeling
use-case:
  - Ledger Column Checks
  - Sign Preservation Templates
related:
  - MINUS
  - UMINUS
  - UNARY_PERCENT
level: 1
source:
  - https://support.google.com/docs/answer/3093608
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Unary Plus
tags:
  - arithmetic
  - operators
  - sheets
---

# UPLUS

## Description

**UPLUS** returns a specified number unchanged. It takes a value and gives it back exactly as it is, with the same sign and size. The official description calls it the function form of the unary plus operator, which in formulas is simply a plus sign placed in front of a value, such as `=+A2`.

Because the function does nothing to the value, its use is mainly structural. It can mark a formula as a deliberate positive value, keep the sign convention of a template consistent with a neighboring column that uses UMINUS, or make a formula easier to read when the argument is a long expression. For example, `UPLUS(-4)` returns `-4`, and `UPLUS(A2)` returns whatever number is in `A2`.

UPLUS is not a conversion tool. It does not turn text into a number, change a percentage into a decimal, or round a value. If you need one of those changes, use a function designed for it, such as TO_PERCENT, UNARY_PERCENT, or ROUND.

## Syntax

```excel
=UPLUS(value)
```

<!-- Image 1: Value Returned Unchanged. See Images/Google-specific/UPLUS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The number, or a reference to a cell that holds a number, to return unchanged. |

### Return Value

The same number, with the same sign. The official documentation does not describe error conditions or limits for UPLUS.

## Examples

Each example is a separate formula, and the cell references assume the values shown in each example.

### Example 1: Negative Number

```excel
=UPLUS(-4)
```

**Result:** `-4`

The sign is kept, so a negative value stays negative.

### Example 2: Positive Number

```excel
=UPLUS(12)
```

**Result:** `12`

A positive value is returned as it is.

### Example 3: Cell Reference

```excel
=UPLUS(A2)
```

**Result:** `-250` when `A2` holds `-250`

The formula displays the same value that the cell holds, and the source cell does not change.

### Example 4: Expression as the Argument

```excel
=UPLUS(B2-C2)
```

**Result:** `-75` when `B2` holds `120` and `C2` holds `195`

The subtraction runs first, and the difference is returned unchanged.

<!-- Image 2: Expression Returned Unchanged. See Images/Google-specific/UPLUS.md -->

### Example 5: Unary Plus Operator

```excel
=+A2
```

**Result:** `-250` when `A2` holds `-250`

The plus sign before a cell reference returns the same result as UPLUS for a single value.

## Story Problems

### Problem 1: Ledger Sign Check

A ledger column records each account movement with its sign: deposits are positive, and withdrawals are negative. The template uses UPLUS to show the value for a withdrawal row, so the sign is visible in the report.

| Entry | Amount |
| --- | --- |
| Rent | -250 |
| Payment received | 400 |

**Task:** Show the amount for the rent row in `D2` with its sign kept.

**Solution:**

```excel
=UPLUS(B2)
```

**Answer:** `-250`. The function returns the value unchanged, so the withdrawal stays negative.

### Problem 2: Net Movement Total

Three transactions in `B2:B4` are 120, -45.5 and 300. The team wants the net movement shown in `B6` with the same sign as the sum.

**Task:** Return the net movement in `B6` without changing its sign.

**Solution:**

```excel
=UPLUS(SUM(B2:B4))
```

**Answer:** `374.5`, because 120 plus 300 is 420, less 45.5 is 374.5, and UPLUS returns that total unchanged.

<!-- Image 3: Net Movement Total With UPLUS. See Images/Google-specific/UPLUS.md -->

## Use Cases

### Ledger Column Checks

**Scenario:** An accountant reviews a ledger where each row must show its sign, and a template uses the same formula structure in every row.

```excel
=UPLUS(B2)
```

**Why It Works:** The formula keeps the sign of each entry, so reviewers can see withdrawals and deposits at a glance without changing the values.

### Sign Preservation Templates

**Scenario:** A budget template has a column of outflows written as negative numbers, and a summary column must keep the same sign convention for each subtotal.

```excel
=UPLUS(SUM(C2:C12))
```

**Why It Works:** The subtotal is returned without a sign change, which keeps the template's convention consistent across rows.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Expected a conversion but nothing changed | UPLUS returns its input unchanged and does not convert text or formats. | Use TO_PERCENT, UNARY_PERCENT, VALUE, or ROUND for the conversion you need. |
| Value looks wrong after the formula | The argument is a longer expression with a different order of operations than intended. | Add parentheses inside the argument to make the order explicit. |
| Formula adds nothing to the result | UPLUS has no effect on the value, so removing it does not change the result. | Keep it only where it documents intent, or remove it from the formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available as a function | A plus sign before a value, such as `=+A2`, returns the value unchanged. |
| Google Sheets | Available | Works as a function, and the same result comes from the unary plus operator. |

## Tips and Best Practices

- Use UPLUS sparingly, because a formula without it returns the same value.
- Pair UPLUS with UMINUS when a template must show the sign of a value explicitly in both directions.
- Use parentheses in the argument rather than relying on UPLUS to group a calculation.
- Use a conversion function instead of UPLUS when the task is to change a format or a type.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MINUS](MINUS.md) | Subtracts one number from another as a function. |
| [UMINUS](UMINUS.md) | Reverses the sign of a number, the opposite of UPLUS for negative values. |
| [UNARY_PERCENT](UNARY_PERCENT.md) | Interprets a number as a percentage, which changes the value. |

## Official Documentation

- [Google Docs Editors Help: UPLUS](https://support.google.com/docs/answer/3093608)
