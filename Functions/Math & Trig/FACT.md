---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Number Theory
purpose:
  - Arithmetic Operations
use-case:
  - Schedule Permutations
  - Seating Arrangements
related:
  - COMBIN
  - COMBINA
  - FACTDOUBLE
  - MULTINOMIAL
  - PERMUT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/fact-function
  - https://support.google.com/docs/answer/3093412
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Factorial
tags:
  - combinatorics
  - excel
  - sheets
---

# FACT

## Description

**FACT** returns the factorial of a nonnegative number, written n!. The factorial is the product of every whole number from 1 up to n, so 5! is 1 times 2 times 3 times 4 times 5, which equals 120. By definition, 0! is 1.

Use FACT to count the ways to arrange a set of distinct items in order, such as seating guests or scheduling tasks. When the input has a decimal part, FACT drops the decimal part before it calculates, so FACT(4.7) is the same as FACT(4). A negative input returns `#NUM!` in Excel.

Factorials grow quickly. A small increase in the input can produce a much larger result, so check that the result is large enough to be meaningful for the decision you are making.

## Syntax

```excel
=FACT(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/FACT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A nonnegative number. Decimal parts are truncated. Google Sheets names this argument `value`. |

### Return Value

A number: the factorial of the integer part of the input. The function returns `#NUM!` in Excel when the input is negative, and `#VALUE!` when the input is not numeric.

## Examples

### Example 1: Factorial of Five

```excel
=FACT(5)
```

**Result:** `120`

The product 1 times 2 times 3 times 4 times 5 is 120.

### Example 2: Factorial of Zero

```excel
=FACT(0)
```

**Result:** `1`

By definition, the factorial of 0 is 1.

### Example 3: Decimal Input

```excel
=FACT(1.9)
```

**Result:** `1`

The decimal part is removed first, so the function calculates the factorial of 1.

### Example 4: Larger Input

```excel
=FACT(10)
```

**Result:** `3628800`

Ten items can be arranged in 3,628,800 different orders.

<!-- Image 2: Factorial Growth Table. See Images/Math & Trig/FACT.md -->

### Example 5: Negative Input

```excel
=FACT(-1)
```

**Result:** `#NUM!`

A factorial is defined only for nonnegative numbers, so a negative input returns an error in Excel.

## Story Problems

### Problem 1: Seating Arrangements

A host has two tables of guests. Each table seats its guests in a row, and the host wants the total number of possible seating orders for the two tables.

| Table | Guests |
| --- | --- |
| Table 1 | 3 |
| Table 2 | 5 |

**Task:** Add the factorial of the guest count for each table.

**Solution:**

```excel
=FACT(B2)+FACT(B3)
```

**Answer:** `126`. Table 1 has 3! = 6 orders and Table 2 has 5! = 120 orders, which add to 126.

### Problem 2: Truncated Input

A survey tool stores a sample size that includes a decimal part. The analyst needs the factorial of the sample size as a whole number.

| Sample | Input |
| --- | --- |
| Sample set | 4.7 |

**Task:** Calculate the factorial of the input in B2.

**Solution:**

```excel
=FACT(B2)
```

**Answer:** `24`. FACT drops the decimal part, so 4.7 becomes 4, and 4! is 24.

## Use Cases

### Seating Arrangements

**Scenario:** A planning sheet lists the guest count for each table in a table named Tables. The total number of seating orders is needed for a discussion about seating plans.

```excel
=SUMPRODUCT(FACT(Tables[Guests]))
```

**Why It Works:** SUMPRODUCT calculates the factorial for each table and adds the results. The counts should be whole numbers, because a decimal part is removed before the calculation.

### Schedule Permutations

**Scenario:** A scheduler needs the number of ways to choose and order a few tasks from a longer list. The list size is in B2 and the number of tasks chosen is in C2.

```excel
=FACT(B2)/FACT(B2-C2)
```

**Why It Works:** Dividing the factorial of the list size by the factorial of the remaining items counts the ordered choices. With 10 tasks and 3 chosen, the result is 720.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is negative. | Check the source value, because a factorial needs a nonnegative input. |
| `#VALUE!` | The input is text or another non-numeric value. | Check the source cell, or convert the text to a number. |
| Unexpected value | A decimal input was truncated. | Round the input with ROUND first if you need a different whole number. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in the Math and trigonometry group. | The argument is named `number`. A negative input returns `#NUM!`. |
| Google Sheets | Available | The argument is named `value`. The page documents truncation of a decimal part. It does not describe negative inputs, so test them before relying on the result. |

## Tips and Best Practices

- Use ROUND or INT deliberately before FACT when the input may contain decimals.
- Use PERMUT or COMBIN when the problem asks for a selection from a larger set, rather than a full arrangement.
- Keep the input small enough that the result stays meaningful to the business question.
- Check one known value, such as FACT(5) = 120, when you build a larger model around it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMBIN](COMBIN.md) | Counts selections where order does not matter. |
| [COMBINA](COMBINA.md) | Counts selections with repetition allowed, where order does not matter. |
| [FACTDOUBLE](FACTDOUBLE.md) | Multiplies every second whole number, a related product. |
| [MULTINOMIAL](MULTINOMIAL.md) | Extends the factorial to several groups of items. |
| [PERMUT](../Statistical/PERMUT.md) | Counts ordered selections from a larger set, built from factorials. |

## Official Documentation

- [Microsoft Support: FACT function](https://support.microsoft.com/en-us/excel/functions/fact-function)
- [Google Docs Editors Help: FACT](https://support.google.com/docs/answer/3093412)
