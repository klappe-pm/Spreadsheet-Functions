---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Financial Modeling
use-case:
  - Bank Statement Signs
  - Expense Reversal
related:
  - ABS
  - MINUS
  - UNARY_PERCENT
  - UPLUS
level: 1
source:
  - https://support.google.com/docs/answer/3093606
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Negate Number
  - Reverse Sign
tags:
  - arithmetic
  - operators
  - sheets
  - sign
---

# UMINUS

## Description

**UMINUS** returns a number with its sign reversed. A positive value becomes negative, and a negative value becomes positive. The official description says it is equivalent to multiplying the number by -1, so `UMINUS(5)` returns `-5` and `UMINUS(-4)` returns `4`.

Use UMINUS when a formula needs the opposite sign of a value and you want the operation written as a function. A common case is a list of expenses recorded as positive amounts that must be treated as outflows in a cash flow total. In formulas, the same result comes from the unary minus operator, as in `=-A2`. UMINUS is the function form of that operator, which can be easier to read inside a longer formula or when the argument is a complex expression.

UMINUS does not change the input cell. It only returns the reversed value in the cell that contains the formula. Apply it to a single value or to a total. To reverse each value in a column, use a row-by-row formula or ARRAYFORMULA.

## Syntax

```excel
=UMINUS(value)
```

<!-- Image 1: Sign Reversal of a Value. See Images/Google-specific/UMINUS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The number, or a reference to a cell that holds a number, whose sign you want reversed. |

### Return Value

The same number with the opposite sign. Zero stays zero. The official documentation does not list error conditions or limits for UMINUS.

## Examples

Each example is a separate formula, and cell references assume the values shown in the example.

### Example 1: Positive Number

```excel
=UMINUS(15)
```

**Result:** `-15`

The positive value becomes negative.

### Example 2: Negative Number

```excel
=UMINUS(-4)
```

**Result:** `4`

Reversing a negative number gives the positive number with the same size.

### Example 3: Cell Reference

```excel
=UMINUS(A2)
```

**Result:** `-250` when `A2` holds `250`

The formula reads the cell, reverses its sign and displays the result in the formula cell. `A2` keeps its original value.

### Example 4: Expression as the Argument

```excel
=UMINUS(B2*C2)
```

**Result:** `-102` when `B2` holds `12` and `C2` holds `8.5`

The multiplication runs first, and its product is reversed. This form is useful when the argument is a calculation rather than a single cell.

<!-- Image 2: Expression Reversed Inside UMINUS. See Images/Google-specific/UMINUS.md -->

### Example 5: Reversing Twice

```excel
=UMINUS(UMINUS(7))
```

**Result:** `7`

Reversing the sign twice returns the original number, which confirms the result is the same magnitude with the sign flipped each time.

## Story Problems

### Problem 1: Withdrawals as Outflows

A bank statement records three withdrawals as positive amounts in `B2:B4`. The reconciliation sheet needs the total of the withdrawals as a negative outflow.

| Date | Withdrawal |
| --- | --- |
| Mon | 120 |
| Tue | 45.5 |
| Thu | 300 |

**Task:** Calculate the total withdrawals as a negative amount in `B6`.

**Solution:**

```excel
=UMINUS(SUM(B2:B4))
```

**Answer:** `-465.5`, because 120 + 45.5 + 300 = 465.5, and the sign is reversed.

<!-- Image 3: Withdrawal Total With Reversed Sign. See Images/Google-specific/UMINUS.md -->

### Problem 2: Net Cash Position

A household budget records income of 2000 in `B2` and an expense of 1350.25 in `B3`. The expense is entered as a positive amount, but the net position needs it as an outflow.

**Task:** Calculate the net position in `B5` by adding the income to the expense with its sign reversed.

**Solution:**

```excel
=B2+UMINUS(B3)
```

**Answer:** `649.75`, because 2000 minus 1350.25 is 649.75.

## Use Cases

### Bank Statement Signs

**Scenario:** A reconciliation sheet imports withdrawals as positive numbers, but the cash flow report shows outflows as negative.

```excel
=UMINUS(SUM(D2:D40))
```

**Why It Works:** The sum is calculated first, and UMINUS gives the outflow total the sign the report requires.

### Expense Reversal

**Scenario:** A project budget records each expense as a positive cost, and a summary row must subtract the expenses from the funding amount.

```excel
=E2+UMINUS(SUM(E3:E9))
```

**Why It Works:** The reversal is written as a function, so the subtraction is explicit. SUM turns the range into one total first, and UMINUS reverses that total.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result is unexpected for a range | The formula passes a whole range to UMINUS, which is written for a single value. | Wrap the range in SUM to reverse the total, or use ARRAYFORMULA to reverse each value. |
| Sign is reversed twice | The value was already negated in a source formula, and UMINUS reversed it again. | Check the source formula, and remove one negation. |
| Result is text | The input is text, and the sign cannot be reversed as a number. | Convert the input to a number before reversing it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available as a function | Use the unary minus operator, such as `=-A2`, to reverse the sign. |
| Google Sheets | Available | Works as a function and matches the unary minus operator for a single value. |

## Tips and Best Practices

- Use the unary minus operator for simple formulas, and UMINUS when the argument is a long expression.
- Reverse a total rather than each row when the report only needs the total with the opposite sign.
- Keep the source amounts positive in the data and reverse them in the report, so the source stays easy to read.
- Use ABS when you need the size of a value regardless of its sign.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ABS](../Math%20%26%20Trig/ABS.md) | Returns the absolute value, which removes the sign instead of reversing it. |
| [MINUS](MINUS.md) | Subtracts one number from another as a function. |
| [UNARY_PERCENT](UNARY_PERCENT.md) | Interprets a number as a percentage by dividing it by 100. |
| [UPLUS](UPLUS.md) | Returns a number unchanged, the counterpart to UMINUS. |

## Official Documentation

- [Google Docs Editors Help: UMINUS](https://support.google.com/docs/answer/3093606)
