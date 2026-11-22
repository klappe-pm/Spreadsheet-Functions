---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Arithmetic Operations
  - Conditional Logic
use-case:
  - Account Movement Direction
  - Trend Direction Labels
related:
  - ABS
  - IF
  - INT
  - SQRT
  - SUMPRODUCT
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/sign-function
  - https://support.google.com/docs/answer/3093513
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Number Sign
  - Sign Check
tags:
  - direction
  - excel
  - sheets
  - sign
---

# SIGN

## Description

**SIGN** tells you whether a number is positive, negative, or zero. It returns 1 for a positive number, -1 for a negative number, and 0 for zero. The function does not return the size of the number, only its direction.

Use SIGN to label direction in a table, such as deposits and withdrawals, rising and falling prices, or gains and losses. It is also useful when a formula must act differently for each direction. Combine SIGN with IF, SUMPRODUCT, or COUNTIF to count or label values by direction.

SIGN accepts any real number. Blank cells count as 0, so they return 0. Very small rounding errors matter: a value such as -0.0000001 returns -1, even though it is effectively zero. Use ROUND first when a tiny difference should not change the direction.

Microsoft Excel and Google Sheets return the same results for positive, negative, and zero inputs.

## Syntax

```excel
=SIGN(number)
```

<!-- Image 1: Sign Results on a Number Line. See Images/Math & Trig/SIGN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | Any real number whose sign you want. Blank cells are treated as 0. |

### Return Value

Returns 1 when the number is positive, -1 when the number is negative, and 0 when the number is zero. The function returns #VALUE! when the argument is text that cannot be read as a number.

## Examples

### Example 1: Positive Number

```excel
=SIGN(42)
```

**Result:** 1

The value is greater than zero, so SIGN returns 1. The size of the number does not change the result.

### Example 2: Negative Number

```excel
=SIGN(-7.5)
```

**Result:** -1

The value is below zero, so SIGN returns -1. The decimal part does not affect the direction.

<!-- Image 2: Sign for Positive, Negative and Zero Inputs. See Images/Math & Trig/SIGN.md -->

### Example 3: Zero

```excel
=SIGN(0)
```

**Result:** 0

Zero has no direction, so SIGN returns 0.

### Example 4: Tiny Negative Value

```excel
=SIGN(-0.001)
```

**Result:** -1

Even a very small negative value returns -1. If the source value came from a calculation that should be zero, round it first with ROUND.

### Example 5: Comparing Two Values

```excel
=SIGN(B2 - C2)
```

**Result:** -1 when B2 is 120 and C2 is 135

Subtracting one value from another and taking the sign tells you which value is larger. A result of -1 means the second value is higher, 1 means the first value is higher, and 0 means they are equal.

## Story Problems

### Problem 1: Counting Withdrawals in a Ledger

A small bookkeeping team receives a list of account movements. Deposits are positive, and withdrawals are negative. The team needs to count how many withdrawals appear in the list.

| Movement | Amount |
| --- | --- |
| Customer payment | 250 |
| Supplier invoice | -80 |
| Adjustment | 0 |
| Bank fee | -15.5 |
| Refund | 40 |

**Task:** Count the number of withdrawals in the list.

**Solution:**

```excel
=SUMPRODUCT(--(SIGN(B2:B6) = -1))
```

**Answer:** `2`, because the supplier invoice and the bank fee are negative. The zero adjustment is not a withdrawal.

### Problem 2: Direction of a Weekly Temperature Change

A weather station records the daily change in temperature over five days. The analyst wants one flag that shows whether the week ended warmer or cooler than it started.

| Day | Change (degrees) |
| --- | --- |
| Monday | 3.2 |
| Tuesday | -1.5 |
| Wednesday | 0 |
| Thursday | -0.4 |
| Friday | 2.0 |

**Task:** Find the sign of the total change for the week.

**Solution:**

```excel
=SIGN(SUM(B2:B6))
```

**Answer:** `1`, because the changes add up to 3.3 degrees. A value of 1 means the week ended warmer.

## Use Cases

### Account Movement Direction

**Scenario:** A treasury team labels every ledger line as an inflow or an outflow for a daily cash report.

```excel
=IF(SIGN(B2) = 1, "Inflow", IF(SIGN(B2) = -1, "Outflow", "No Movement"))
```

**Why It Works:** SIGN separates the three possible directions, and IF turns each result into a readable label. Zero amounts are labeled separately, so they are not counted as inflows.

### Trend Direction Labels

**Scenario:** A sales manager shows whether each product's monthly change is up, down, or flat in a dashboard.

```excel
=CHOOSE(SIGN(C2) + 2, "Down", "Flat", "Up")
```

**Why It Works:** SIGN returns -1, 0, or 1, and adding 2 turns those results into positions 1, 2, and 3 for CHOOSE. The label list is ordered from down to up.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text, not a number. | Convert the text with VALUE or correct the source cell. |
| Unexpected -1 | A rounding error near zero gives a tiny negative value. | Wrap the value in ROUND, such as ROUND(B2, 2), before SIGN. |
| Unexpected 0 | The cell is blank or contains an empty string. | Check the source data and confirm the value exists. |
| Size confused with direction | The result is taken for the amount. | Use ABS to return the size, and SIGN to return the direction. |
| `#NAME?` | The function name is misspelled. | Check that the name is spelled as SIGN. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows and Mac), Excel for the web, Excel 2024, Excel 2021, Excel 2019, and Excel 2016 | Returns 1, -1, or 0 for any real number. |
| Google Sheets | Available | Returns the same values as Excel for positive, negative, and zero inputs. |

## Tips and Best Practices

- Use SIGN with SUMPRODUCT to count positive, negative, or zero values in a range without a helper column.
- Round the source value when tiny calculation errors could flip the direction.
- Pair SIGN with ABS when a report needs both the size and the direction of a change.
- Label the direction values in a legend, so readers know that -1 means down and 1 means up.
- Use IF for readable labels, and keep SIGN for the numeric test.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ABS](ABS.md) | Returns the size of a number without its direction. |
| [IF](../Logical/IF.md) | Turns the SIGN result into a label or a branch in a formula. |
| [INT](INT.md) | Rounds down to an integer, which can be used when the direction of a whole number is needed. |
| [SQRT](SQRT.md) | Returns a square root, which is always positive and cannot be negative. |
| [SUMPRODUCT](SUMPRODUCT.md) | Counts or totals values based on their SIGN results across a range. |

## Official Documentation

- [Microsoft Support: SIGN function](https://support.microsoft.com/en-us/excel/functions/sign-function)
- [Google Docs Editors Help: SIGN](https://support.google.com/docs/answer/3093513)
