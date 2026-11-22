---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Conditional Logic
  - Type Checking
use-case:
  - Alternating Row Shading
  - Even Count in a Column
  - Round Robin Assignments
related:
  - IF
  - ISNUMBER
  - ISODD
  - MOD
  - ROW
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/iseven-function
  - https://support.google.com/docs/answer/3093419
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - excel
  - information
  - sheets
  - type-checking
---

# ISEVEN

## Description

**ISEVEN** returns TRUE when a number is an even integer and FALSE for everything else, including odd integers, decimals and text. It is the simplest way to split a list of whole numbers into two alternating groups inside a formula.

Use ISEVEN inside IF, FILTER, SUMPRODUCT or conditional formatting when the result depends on whether a number is even. Both Microsoft Excel and Google Sheets define the test in terms of integers, so round or truncate decimals before testing them.

ISEVEN is the mirror of ISODD. For a test that works with any divisor, not just 2, use MOD(value, 2) = 0 instead.

## Syntax

```excel
=ISEVEN(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISEVEN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The number or cell reference to test. Text is not converted, so convert a number stored as text with VALUE first. |

### Return Value

TRUE when `value` is an even integer, or a reference to a cell that holds one. FALSE when the value is odd, is a decimal, or is text. An invalid argument such as a misspelled name returns an error.

## Examples

### Example 1: Basic Usage

Cell A2 holds `14`.

```excel
=ISEVEN(A2)
```

**Result:** `TRUE`

14 divided by 2 leaves no remainder, so the function returns TRUE.

### Example 2: Labeling Rows

Cell B2 holds `7`.

```excel
=IF(ISEVEN(B2),"Even","Odd")
```

**Result:** `Odd`

The IF function turns the TRUE or FALSE result into a readable label.

### Example 3: Alternating Pattern by Row Number

```excel
=ISEVEN(ROW(A2))
```

**Result:** `TRUE` in row 2, `FALSE` in row 3, `TRUE` in row 4

ROW returns the row number of each formula cell. Copying the formula down produces an alternating pattern.

### Example 4: Testing a Rounded Value

Cell C2 holds `8.6`.

```excel
=ISEVEN(ROUND(C2, 0))
```

**Result:** `FALSE`

ROUND turns 8.6 into 9, which is odd. Test the rounded value, not the decimal, to get a predictable answer.

<!-- Image 2: Alternating Row Pattern. See Images/Information/ISEVEN.md -->

## Story Problems

### Problem 1: Even Badge Numbers at Check-In

A facility gives each visitor a badge number. The organizers want to count how many badges in the list are even.

| Visitor | Badge |
| --- | --- |
| Harper | 1012 |
| Ines | 1015 |
| Jonah | 1020 |
| Kira | 1033 |
| Lou | 1048 |
| Mateo | 1051 |

**Task:** Count the even badge numbers in `B2:B7`.

**Solution:**

```excel
=SUMPRODUCT(ISEVEN(B2:B7)*1)
```

**Answer:** `3`. Badges 1012, 1020 and 1048 are even.

### Problem 2: Pallet Counts on a Rack

A warehouse records the number of pallets on each rack row. Rows with an even count are assigned to the second shift.

| Rack Row | Pallets |
| --- | --- |
| R1 | 6 |
| R2 | 9 |
| R3 | 4 |
| R4 | 11 |
| R5 | 8 |
| R6 | 10 |

**Task:** Count the rows with an even pallet count in `B2:B7`.

**Solution:**

```excel
=SUMPRODUCT(ISEVEN(B2:B7)*1)
```

**Answer:** `4`. Rows R1, R3, R5 and R6 hold 6, 4, 8 and 10 pallets.

## Use Cases

### Alternating Row Shading

**Scenario:** A printed report is easier to read when every other row has a light background.

```excel
=ISEVEN(ROW())
```

**Why It Works:** Use this formula as a conditional formatting rule on the table range. Rows where the formula returns TRUE get the shade. The rule keeps working when rows are added or sorted.

### Round Robin Assignments

**Scenario:** A support manager splits incoming tickets between two agents by ticket number.

```excel
=IF(ISEVEN(A2),"Agent A","Agent B")
```

**Why It Works:** Even ticket numbers go to Agent A and odd numbers go to Agent B. The split is fixed, so the same ticket always reaches the same agent.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for a number that looks even | The value is stored as text, such as a number imported from a CSV file. | Convert it with `=ISEVEN(VALUE(A2))` or change the cell format to Number. |
| `FALSE` for a whole-looking number | The value is a decimal such as 4.5 or 10.0001. | Round or truncate first with ROUND or TRUNC. |
| `#NAME?` | The function name is misspelled. | Correct the spelling to ISEVEN. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Excel 2024, Excel 2021, Excel 2019, Excel 2016 and Excel for the web. | Returns TRUE only for even integers. Works in conditional formatting and dynamic array formulas. |
| Google Sheets | Available | Same syntax and return value. The Sheets help page describes the test as checking for an even integer. |

## Tips and Best Practices

- Convert text numbers and round decimals before the test so the result matches what you expect.
- Use ISODD for the opposite test instead of wrapping ISEVEN in NOT.
- Use MOD(value, 2) = 0 when the logic might later change to a different divisor.
- Wrap ISEVEN in IF when the result must be a label, not a TRUE or FALSE value.
- Apply SUMPRODUCT around ISEVEN with `*1` to count even values in a range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ISODD](ISODD.md) | Tests the opposite condition for odd integers. |
| [MOD](../Math%20%26%20Trig/MOD.md) | Returns the remainder, so `MOD(A2, 2) = 0` gives the same result and works for other divisors. |
| [ISNUMBER](ISNUMBER.md) | Confirms the value is numeric before testing whether it is even. |
| [IF](../Logical/IF.md) | Turns the TRUE or FALSE result into labels or branching logic. |
| [ROW](../Lookup%20%26%20Reference/ROW.md) | Supplies row numbers for alternating row patterns. |

## Official Documentation

- [Microsoft Support: ISEVEN function](https://support.microsoft.com/en-us/excel/functions/iseven-function)
- [Google Docs Editors Help: ISEVEN](https://support.google.com/docs/answer/3093419)
