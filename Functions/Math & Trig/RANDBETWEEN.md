---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Random Numbers
purpose:
  - Randomization
use-case:
  - Random Audit Selection
  - Randomized Prize Draws
  - Test Data Generation
related:
  - INDEX
  - INT
  - RAND
  - RANDARRAY
  - ROUND
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/randbetween-function
  - https://support.google.com/docs/answer/3093507
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Random Integer
  - Random Whole Number
tags:
  - excel
  - integers
  - randomization
  - sheets
---

# RANDBETWEEN

## Description

**RANDBETWEEN** returns a random whole number between two values you specify. Both endpoints can be returned. `=RANDBETWEEN(1,100)` can return 1, 100, or any whole number in between. The function takes the lower bound first and the upper bound second, and both must be provided. Negative bounds work, so `=RANDBETWEEN(-1,1)` returns -1, 0 or 1.

Use RANDBETWEEN for random whole numbers such as dice rolls, ticket draws, row picks for an audit, and test data. It is the integer counterpart of RAND, which returns decimals. When you need a decimal range instead, use RAND with a scaling formula.

RANDBETWEEN recalculates when the worksheet recalculates, so each recalculation can produce a new number. Repeats are possible because each result is independent of the others. If a draw must not repeat, combine RANDBETWEEN with a list and a check for duplicates, or use a shuffling approach built on RANDARRAY.

## Syntax

```excel
=RANDBETWEEN(bottom, top)
```

<!-- Image 1: Lower and Upper Bounds. See Images/Math & Trig/RANDBETWEEN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `bottom` | Yes | The smallest whole number the function can return. Can be a number, a cell reference or a formula result. |
| `top` | Yes | The largest whole number the function can return. Both bounds are included in the possible results. |

### Return Value

A whole number greater than or equal to `bottom` and less than or equal to `top`. The result changes whenever the worksheet recalculates. A text argument returns `#VALUE!`.

<!-- Image 2: Random Draw Results. See Images/Math & Trig/RANDBETWEEN.md -->

## Examples

### Example 1: Whole Number From 1 to 100

```excel
=RANDBETWEEN(1,100)
```

**Result:** a whole number from 1 to 100, such as 37, which changes on recalculation

Both 1 and 100 are possible results, because the bounds are inclusive.

### Example 2: Negative Bounds

```excel
=RANDBETWEEN(-5,5)
```

**Result:** a whole number from -5 to 5

The range includes negative values and zero. This form is useful for random adjustments in either direction.

### Example 3: Bounds From Cells

The lowest invoice number is in cell `A2`, which holds `10`, and the highest is in `A3`, which holds `20`.

```excel
=RANDBETWEEN(A2,A3)
```

**Result:** a whole number from 10 to 20

Keeping the bounds in cells lets you change the range without editing the formula.

### Example 4: Simulated Die Roll

```excel
=RANDBETWEEN(1,6)
```

**Result:** a whole number from 1 to 6

Each face has an equal chance of appearing. Repeated recalculations can produce the same face several times in a row.

### Example 5: Coin Flip

```excel
=RANDBETWEEN(0,1)
```

**Result:** either 0 or 1

Reading 0 as tails and 1 as heads gives a simple coin flip, and both outcomes are equally likely.

## Story Problems

### Problem 1: Winning Ticket in a Prize Draw

A store sells 120 raffle tickets, numbered 1 to 120. The draw picks one winning number.

| Item | Value |
| --- | --- |
| Lowest Ticket Number | 1 |
| Highest Ticket Number | 120 |

**Task:** Write a formula that picks the winning ticket number.

**Solution:**

```excel
=RANDBETWEEN(1,120)
```

**Answer:** A whole number from 1 to 120, which is the winning ticket. Both 1 and 120 can win. The number changes on each recalculation, so record the result once the draw is made.

### Problem 2: Random Audit Row

An auditor must check one invoice from a list. The invoice rows run from row 2 to row 85 of the sheet.

| Item | Value |
| --- | --- |
| First Data Row | 2 |
| Last Data Row | 85 |

**Task:** Write a formula that returns a random row number for the auditor to review.

**Solution:**

```excel
=RANDBETWEEN(B2,B3)
```

**Answer:** A whole number from 2 to 85, which is the row to audit. With B2 holding 2 and B3 holding 85, the formula returns a row number that can be used with INDEX to pull the invoice.

## Use Cases

### Random Audit Selection

**Scenario:** An internal audit team selects one invoice at random from a list of 200 entries.

```excel
=INDEX(A2:A200, RANDBETWEEN(1, COUNTA(A2:A200)))
```

**Why It Works:** RANDBETWEEN picks a position from 1 up to the number of filled entries, and INDEX returns the value at that position. Paste the selected value as a fixed record once the audit is documented.

### Randomized Prize Draws

**Scenario:** A community group holds a draw from all tickets sold, and the total is kept in a cell.

```excel
=RANDBETWEEN(1,B2)
```

**Why It Works:** The upper bound comes from `B2`, which holds the total number of tickets sold. Changing the total updates the range without editing the formula.

### Test Data Generation

**Scenario:** A developer builds a sample order table with quantities that look realistic.

```excel
=RANDBETWEEN(1,500)
```

**Why It Works:** Each cell receives a whole-number quantity between 1 and 500. Copy the formula down the table, then paste as values before the data is shared.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | One of the bounds is text. | Convert the cell to a number, or re-enter the bound. |
| Result is not a whole number | The formula was combined with RAND or a decimal without rounding. | Use RANDBETWEEN alone, or wrap the expression in ROUND. |
| Unexpected range with decimal bounds | The bounds are decimals, and Google Sheets moves them to whole numbers. | Enter whole-number bounds, or round them before the call. |
| Same number appears again | Each recalculation is independent, so repeats are possible. | Build a list without repeats with a duplicate check, or use a shuffle method. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | Two required arguments, bottom and top. Both bounds are included. |
| Google Sheets | Available | Same two arguments, named low and high. Decimal bounds are adjusted: the minimum moves to the next integer above low, and the maximum moves to the next integer below high. |

## Tips and Best Practices

- Keep the bounds in labeled cells so that the range can change without editing formulas.
- Use RAND for decimals and RANDBETWEEN for whole numbers.
- Paste random results as values once a draw, audit or sample is final.
- Use whole-number bounds so that both platforms return the same range.
- Confirm that the lower bound is smaller than the upper bound before you share the formula, because the official pages do not describe a reversed range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [INDEX](../Lookup%20%26%20Reference/INDEX.md) | Returns the item at a random position chosen by RANDBETWEEN. |
| [INT](INT.md) | Rounds down to a whole number, a way to build integers from RAND. |
| [RAND](RAND.md) | Returns a random decimal instead of a whole number. |
| [RANDARRAY](RANDARRAY.md) | Returns a block of random numbers, including whole numbers, in one formula. |
| [ROUND](ROUND.md) | Converts a decimal result to a whole number or a fixed number of places. |

## Official Documentation

- [Microsoft Support: RANDBETWEEN function](https://support.microsoft.com/en-us/excel/functions/randbetween-function)
- [Google Docs Editors Help: RANDBETWEEN](https://support.google.com/docs/answer/3093507)
