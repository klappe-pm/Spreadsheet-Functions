---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Conditional Logic
  - Type Checking
use-case:
  - Odd Floor Rent Totals
  - Odd Row Shading
  - Two Crew Schedule
related:
  - IF
  - ISEVEN
  - ISNUMBER
  - MOD
  - ROW
  - SUMPRODUCT
level: 1
source:
  - https://support.microsoft.com/en-us/excel/is-functions
  - https://support.google.com/docs/answer/3093491
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Odd Number Test
tags:
  - excel
  - information
  - sheets
  - type-checking
---

# ISODD

## Description

**ISODD** returns TRUE when a number is an odd integer and FALSE for everything else, including even integers, decimals and text. Use it to flag odd-numbered items, to shade alternate rows, or to split a list into two groups.

ISODD is the mirror of ISEVEN. Both platforms define the test for integers, so round or truncate decimals before testing them. A decimal such as 3.5 does not count as an odd integer.

For a test that works with any divisor, use MOD(value, 2) = 1 instead. For the opposite condition on whole numbers, ISEVEN gives the same answer with the logic reversed.

## Syntax

```excel
=ISODD(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISODD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The number or cell reference to test. Text is not converted, so convert a number stored as text with VALUE first. |

### Return Value

TRUE when `value` is an odd integer, or a reference to a cell that holds one. FALSE when the value is even, is a decimal, or is text. An invalid argument such as a misspelled name returns an error.

## Examples

### Example 1: Basic Usage

Cell A2 holds `9`.

```excel
=ISODD(A2)
```

**Result:** `TRUE`

Nine leaves a remainder of 1 when divided by 2, so the function returns TRUE.

### Example 2: Flagging Odd Invoice Numbers

Cell B2 holds `1043`.

```excel
=IF(ISODD(B2),"Review","Pass")
```

**Result:** `Review`

Odd invoice numbers go to a review queue and even numbers pass straight through.

### Example 3: Alternating Pattern by Row Number

```excel
=ISODD(ROW(A2))
```

**Result:** `FALSE` in row 2, `TRUE` in row 3, `FALSE` in row 4

ROW returns the row number of each formula cell. The pattern repeats down the column.

### Example 4: Summing Only Odd Values

Column C holds the values 3, 8, 15, 20, 7 and 12 in `C2:C7`.

```excel
=SUMPRODUCT(ISODD(C2:C7)*C2:C7)
```

**Result:** `25`

Only 3, 15 and 7 are odd, and their total is 25.

<!-- Image 2: Two Crew Pattern. See Images/Information/ISODD.md -->

## Story Problems

### Problem 1: Rent for Odd-Numbered Floors

A small office building lists the monthly rent for each floor. The owner wants the total rent for odd-numbered floors only.

| Floor | Monthly Rent |
| --- | --- |
| 2 | 1800 |
| 3 | 1650 |
| 5 | 2100 |
| 8 | 1950 |
| 11 | 2400 |
| 14 | 2250 |

**Task:** Total the rent for the odd floors in `A2:B7`.

**Solution:**

```excel
=SUMPRODUCT(ISODD(A2:A7)*B2:B7)
```

**Answer:** `6150`. Floors 3, 5 and 11 pay 1650, 2100 and 2400.

<!-- Image 3: Odd Floor Rent Result. See Images/Information/ISODD.md -->

### Problem 2: Odd Tank Batches

A brewery labels its fermentation tanks with ID numbers. The quality team inspects only the tanks with odd IDs this week.

| Tank | Litres |
| --- | --- |
| 4 | 150 |
| 7 | 210 |
| 9 | 95 |
| 12 | 300 |
| 15 | 180 |

**Task:** Count the tanks with an odd ID in `A2:A6`.

**Solution:**

```excel
=SUMPRODUCT(ISODD(A2:A6)*1)
```

**Answer:** `3`. Tanks 7, 9 and 15 have odd IDs.

## Use Cases

### Odd Row Shading

**Scenario:** A long price list is easier to scan when alternate rows have a light background.

```excel
=ISODD(ROW())
```

**Why It Works:** Apply this formula as a conditional formatting rule to the table. Rows where the formula returns TRUE get the shade, and the rule updates as rows are inserted.

### Two Crew Schedule

**Scenario:** A maintenance supervisor rotates two crews through a list of jobs, one job per row.

```excel
=IF(ISODD(ROW(A2)),"Crew 1","Crew 2")
```

**Why It Works:** Odd-numbered rows go to Crew 1 and even-numbered rows go to Crew 2. The assignment stays fixed even if the list is sorted by another column, because it depends on the row position.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for a number that looks odd | The value is stored as text, such as a number pasted from a web page. | Convert it with `=ISODD(VALUE(A2))` or change the cell format to Number. |
| `FALSE` for a decimal | The value is 3.5 or another non-integer. | Round or truncate first with ROUND or TRUNC. |
| `#NAME?` | The function name is misspelled. | Correct the spelling to ISODD. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Excel 2024, Excel 2021, Excel 2019, Excel 2016 and Excel for the web. | Returns TRUE only for odd integers. Works in conditional formatting and array formulas. |
| Google Sheets | Available | Same syntax and return value. The Sheets help page describes the test as checking for an odd integer. |

## Tips and Best Practices

- Convert text numbers and round decimals before the test so the result matches what you expect.
- Use ISEVEN for the opposite test on whole numbers.
- Use MOD(value, 2) = 1 when the divisor might change later.
- Wrap ISODD in IF when the result must be a label, not a TRUE or FALSE value.
- Use SUMPRODUCT with ISODD to total only the odd values in a range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ISEVEN](ISEVEN.md) | Tests the opposite condition for even integers. |
| [IF](../Logical/IF.md) | Turns the TRUE or FALSE result into labels or branching logic. |
| [ISNUMBER](ISNUMBER.md) | Confirms the value is numeric before testing whether it is odd. |
| [MOD](../Math%20%26%20Trig/MOD.md) | Returns the remainder, so `MOD(A2, 2) = 1` gives the same result for whole numbers. |
| [ROW](../Lookup%20%26%20Reference/ROW.md) | Supplies row numbers for alternating row patterns. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Totals or counts the values that pass the ISODD test. |

## Official Documentation

- [Microsoft Support: IS functions](https://support.microsoft.com/en-us/excel/is-functions)
- [Google Docs Editors Help: ISODD](https://support.google.com/docs/answer/3093491)
