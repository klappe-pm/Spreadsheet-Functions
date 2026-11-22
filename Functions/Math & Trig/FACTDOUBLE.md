---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Number Theory
purpose:
  - Arithmetic Operations
  - Counting
use-case:
  - Matched Sample Groups
  - Tournament Pairings
related:
  - COMBIN
  - FACT
  - GCD
  - MULTINOMIAL
  - PRODUCT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/factdouble-function
  - https://support.google.com/docs/answer/3093414
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Double Factorial
tags:
  - combinatorics
  - excel
  - factorial
  - sheets
---

# FACTDOUBLE

## Description

**FACTDOUBLE** returns the double factorial of a number. A double factorial multiplies a number by every other integer below it, stopping at 1 for odd inputs or at 2 for even inputs. For example, the double factorial of 7 is 7 × 5 × 3 × 1 = 105.

This differs from the ordinary factorial, which multiplies every integer. The ordinary factorial of 7 is 5,040, computed with the FACT function. Use FACTDOUBLE only when a counting formula calls for the double factorial, such as counting the ways to pair up an even number of items.

Excel and Sheets both remove the decimal part of the input before calculating, so 5.9 is treated as 5. Excel returns `#NUM!` for a negative input and `#VALUE!` for text. The Sheets help page does not describe error values for negative input, so check those inputs before relying on the result.

## Syntax

```excel
=FACTDOUBLE(number)
```

<!-- Image 1: Double Factorial Multiplication Steps. See Images/Math & Trig/FACTDOUBLE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value whose double factorial you want. Decimals are truncated to an integer. Negative values return `#NUM!` in Excel. In Sheets, this argument is named `value`. |

### Return Value

A number: the double factorial of the whole-number part of the input. Excel returns `#VALUE!` for non-numeric input and `#NUM!` for a negative number.

## Examples

### Example 1: Even Input

```excel
=FACTDOUBLE(6)
```

**Result:** `48`

The function multiplies the even numbers down from 6: 6 × 4 × 2 = 48.

### Example 2: Odd Input

```excel
=FACTDOUBLE(7)
```

**Result:** `105`

The function multiplies the odd numbers down from 7: 7 × 5 × 3 × 1 = 105.

### Example 3: Decimal Input Is Truncated

```excel
=FACTDOUBLE(5.9)
```

**Result:** `15`

The decimal part is removed first, so the calculation is FACTDOUBLE(5), which is 5 × 3 × 1 = 15.

<!-- Image 2: Even and Odd Multiplication Chains. See Images/Math & Trig/FACTDOUBLE.md -->

### Example 4: Reading the Input From a Cell

With the number 8 in `A2`:

```excel
=FACTDOUBLE(A2)
```

**Result:** `384`

The formula uses the cell reference, so changing A2 updates the result. The calculation is 8 × 6 × 4 × 2 = 384.

### Example 5: Counting Pairings

With the player count in `B2`:

```excel
=FACTDOUBLE(B2-1)
```

**Result:** `945` when B2 holds 10

For an even number of players, the double factorial of one less than the count gives the number of ways to pair everyone. The formula subtracts 1 before the call because the pairing count for 10 players is FACTDOUBLE(9).

## Story Problems

### Problem 1: Pairing Players for the First Round

A chess club has eight players for its opening round. Each player is matched with exactly one opponent, and the coordinator wants to know how many different sets of matches are possible.

| Round | Players |
| --- | --- |
| Opening | 8 |

**Task:** Enter the player count in `B2` and calculate the number of possible pairings, which is the double factorial of the player count minus 1.

**Solution:**

```excel
=FACTDOUBLE(B2-1)
```

**Answer:** `105`. The calculation is FACTDOUBLE(7) = 7 × 5 × 3 × 1, which counts every distinct way to pair eight players.

### Problem 2: Six Teams in One Round

A tournament has six teams in its first round, and the organizer wants the number of possible pairings before drawing the matches at random.

| Stage | Teams |
| --- | --- |
| First Round | 6 |

**Task:** Enter the team count in `B2` and calculate the number of possible pairings.

**Solution:**

```excel
=FACTDOUBLE(B2-1)
```

**Answer:** `15`. The calculation is FACTDOUBLE(5) = 5 × 3 × 1 = 15.

## Use Cases

### Tournament Pairings

**Scenario:** A coach shows players how many distinct first-round draws are possible before choosing one by lot.

```excel
=FACTDOUBLE(B2-1)
```

**Why It Works:** For an even number of players, the double factorial of one less than the count gives the number of ways to pair everyone. The formula does not check whether the count is even, so confirm that B2 holds an even number before you use the result.

### Matched Sample Groups

**Scenario:** A researcher lists how many ways ten specimens can be split into five matched pairs before a comparison study.

```excel
=FACTDOUBLE(B3-1)
```

**Why It Works:** The same pairing rule applies to any even count of items. Keep the item count in a labeled cell so the reviewer can check which count the result represents.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is negative. | Validate the source value with IF before calling the function. |
| `#VALUE!` | The input is text, not a number. | Convert the value to a number or correct the cell reference. |
| Unexpected result | A decimal was entered, so it was silently truncated. | Enter whole numbers in source cells, or round the value on purpose with ROUND or TRUNC before the call. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Negative input returns `#NUM!`; non-numeric input returns `#VALUE!`. |
| Google Sheets | Available | Same double factorial calculation. The argument is named `value`. The help page does not describe error values for negative input. |

## Tips and Best Practices

- Use FACTDOUBLE when the formula needs the double factorial. Use FACT when it needs the ordinary factorial.
- Validate user-entered counts before the call, because negative numbers return an error.
- Keep the input in a labeled cell so reviewers can see which count the result describes.
- Enter whole numbers in source cells so no decimal part is dropped without notice.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMBIN](COMBIN.md) | Counts combinations, which answers a different counting question. |
| [FACT](FACT.md) | Computes the ordinary factorial, which multiplies every integer. |
| [GCD](GCD.md) | Returns the greatest common divisor, another integer-based function. |
| [MULTINOMIAL](MULTINOMIAL.md) | Counts arrangements of items split into groups. |
| [PRODUCT](PRODUCT.md) | Multiplies a list of numbers, useful for building a product by hand. |

## Official Documentation

- [Microsoft Support: FACTDOUBLE function](https://support.microsoft.com/en-us/excel/functions/factdouble-function)
- [Google Docs Editors Help: FACTDOUBLE](https://support.google.com/docs/answer/3093414)
