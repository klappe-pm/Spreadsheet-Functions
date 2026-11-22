---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Arithmetic Operations
use-case:
  - Budget Totals
  - Invoice Line Totals
  - Two Part Fee Totals
related:
  - DIVIDE
  - EQ
  - GT
  - MINUS
  - MULTIPLY
  - SUM
level: 1
source:
  - https://support.google.com/docs/answer/3093590
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Add Two Numbers
tags:
  - arithmetic
  - operators
  - sheets
---

# ADD

## Description

**ADD** returns the sum of two numbers. It does exactly what the plus operator (`+`) does, so `=ADD(B2, C2)` and `=B2+C2` produce the same result. Google Sheets provides it as a named function so that operator calls can be written in the same style as other functions, for example when a formula is built from text or passed to another function.

Use ADD when you want to add two single values. It accepts only two scalar values. It does not accept ranges, and it cannot add a series of values in one call. For a total across a column or a range, use SUM instead.

ADD is one of several Google Sheets operator functions. Its siblings MINUS, MULTIPLY, DIVIDE and the comparison functions (EQ, GT and others) follow the same two-argument pattern. The function is available only in Google Sheets.

<!-- Image 1: ADD Formula Versus Operator. See Images/Google-specific/ADD.md -->

## Syntax

```excel
=ADD(value1, value2)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first number to add. It can be a number, a cell reference that holds a number, or another formula that returns one. |
| `value2` | Yes | The second number to add, with the same rules as `value1`. |

### Return Value

A number: the sum of `value1` and `value2`. The official page describes ADD as supporting the addition of two scalar values only, so a range argument or a third argument does not produce a valid total.

## Examples

### Example 1: Adding Two Cells

```excel
=ADD(B2, C2)
```

**Result:** `57.75` when B2 holds `45.50` and C2 holds `12.25`.

The formula returns the same value as `=B2+C2`. Use whichever form your team reads more easily.

### Example 2: Adding a Number Directly

```excel
=ADD(3, 4)
```

**Result:** `7`

Both arguments can be typed numbers instead of cell references, which is useful for quick checks while you build a larger formula.

### Example 3: Adding Inside Another Formula

```excel
=ROUND(ADD(B2, C2), 2)
```

**Result:** `57.75` when B2 holds `45.50` and C2 holds `12.25`.

The inner ADD produces the sum first, and ROUND then limits the result to two decimal places. This pattern keeps currency totals tidy when the inputs have more decimals than the display needs.

### Example 4: Adding a Single Value to a Running Figure

```excel
=ADD(B5, D4)
```

**Result:** The sum of the value in B5 and the carried balance in D4, for example `1730` when B5 holds `1250` and D4 holds `480`.

Using ADD for a two-value step keeps each formula short. Copy the formula down a column to carry the running figure forward row by row.

## Story Problems

### Problem 1: Two Part Service Fee

A repair shop charges a base fee and a separate add on fee for a parts warranty. The amounts are in `B2:B3`.

| Charge | Amount |
| --- | --- |
| Base fee | 45.50 |
| Warranty add on | 12.25 |

**Task:** Put the total of the two charges in `B5`.

**Solution:**

```excel
=ADD(B2, B3)
```

**Answer:** `57.75`, because 45.50 + 12.25 = 57.75.

### Problem 2: Combining Two Department Budgets

A small nonprofit keeps the approved budget for each department in `B2:B3`.

| Department | Approved Budget |
| --- | --- |
| Outreach | 1250 |
| Training | 480 |

**Task:** Put the combined budget in `B5` so the total can be compared with the cash on hand.

**Solution:**

```excel
=ADD(B2, B3)
```

**Answer:** `1730`, because 1250 + 480 = 1730.

<!-- Image 2: ADD Story Problem Totals. See Images/Google-specific/ADD.md -->

## Use Cases

### Invoice Line Totals

**Scenario:** An invoice shows a product price in column B and a separate delivery charge in column C. Each row needs a total that includes both.

```excel
=ADD(B2, C2)
```

**Why It Works:** The function adds the two values in the same row. When the sheet has many rows, the formula copies down cleanly and each row stays independent of the others.

### Budget Totals

**Scenario:** A project sheet keeps the labor budget and the materials budget in two cells, and the planner wants one combined figure at the top.

```excel
=ADD(B2, B3)
```

**Why It Works:** Two values produce one result with no range to manage. If a third category is added later, the formula needs a new argument, so SUM over the whole block is usually the better choice at that point.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected total | A range was passed in place of a single cell, and ADD accepts only scalar values. | Use `=SUM(A2:A10)` for a range or pass two single cells. |
| Formula rejected | Three or more arguments were typed. ADD takes exactly two. | Use `=ADD(A2, A3)` and add the third value with another ADD or a plus operator. |
| Blank result | A referenced cell is empty, so the total shows only the other value. | Check that both cells contain numbers before relying on the total. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available. The closest alternative is the plus operator, `=B2+B3`. | Excel has no ADD function. |
| Google Sheets | Available | Equivalent to the `+` operator. Accepts two scalar values only. |

## Tips and Best Practices

- Use `=B2+B3` in a shared workbook if colleagues may open the file in Excel, because the plus operator works in both programs.
- Use SUM for any total across a range; reserve ADD for two single values.
- Wrap the result in ROUND when the inputs contain fractions of a cent so the displayed total matches the invoice.
- Name the sheet cells clearly so the two arguments are easy to trace back to their sources.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DIVIDE](DIVIDE.md) | The matching operator function for division. |
| [MINUS](MINUS.md) | The matching operator function for subtraction. |
| [MULTIPLY](MULTIPLY.md) | The matching operator function for multiplication. |
| [EQ](EQ.md) | Tests whether two values are equal, often used on ADD results. |
| [GT](GT.md) | Tests whether one value is greater than another, often used on ADD results. |
| [SUM](../Math%20%26%20Trig/SUM.md) | Adds a range or many values; use it when ADD would need more than two arguments. |

## Official Documentation

- [Google Docs Editors Help: ADD](https://support.google.com/docs/answer/3093590)
