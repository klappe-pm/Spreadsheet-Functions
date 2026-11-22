---
domain: Spreadsheet Functions
category: Engineering
subcategory: Comparison and Conversion
purpose:
  - Conditional Logic
  - Data Validation
use-case:
  - Batch Target Checks
  - Inventory Count Matching
related:
  - GESTEP
  - IF
  - IFERROR
  - SUM
  - SUMPRODUCT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/delta-function
  - https://support.google.com/docs/answer/3401147
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Equality Test
  - Kronecker Delta
tags:
  - comparison
  - equality
  - excel
  - sheets
---

# DELTA

## Description

**DELTA** tests whether two numbers are equal. It returns 1 when they match and 0 when they do not. Because the result is a number rather than TRUE or FALSE, you can add the results with SUM to count how many rows match a target, which makes DELTA useful for reconciliation and count checks. The function is also called the Kronecker delta in mathematics.

The optional second number defaults to 0. When you omit it, DELTA tests whether the first number is zero, so `DELTA(0)` returns 1 and `DELTA(0.5)` returns 0. A blank cell is treated as zero. DELTA compares numbers only, and both arguments must be numeric or the function returns `#VALUE!`.

For text, dates compared as text, or other mixed types, use an IF test instead. Google Sheets points to its EQ function for other value types. DELTA is a good fit when you want a numeric flag that other formulas can sum.

## Syntax

```excel
=DELTA(number1, [number2])
```

<!-- Image 1: Equal and Unequal Comparisons. See Images/Engineering/DELTA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number to compare. Non-numeric input returns `#VALUE!`. |
| `number2` | No | The second number to compare. The default is 0, so omitting it compares `number1` with zero. |

### Return Value

The number 1 when the two numbers are equal and 0 otherwise. The function returns `#VALUE!` when either argument is not numeric.

## Examples

### Example 1: Unequal Values

```excel
=DELTA(5,4)
```

**Result:** `0`

5 and 4 are different, so the comparison returns 0.

### Example 2: Equal Values

```excel
=DELTA(5,5)
```

**Result:** `1`

The two numbers match, so the function returns 1.

### Example 3: Omitted Second Number

```excel
=DELTA(0.5)
```

**Result:** `0`

With no second number, DELTA compares 0.5 with 0. They are not equal, so the result is 0.

### Example 4: Compare Two Cells

```excel
=DELTA(B2,C2)
```

**Result:** `1` when B2 and C2 both hold 48

Both cells hold the same number, so the function returns 1. To total many such flags, fill the formula down a helper column and sum that column, as the first story problem shows.

## Story Problems

### Problem 1: Batch Target Checks

A bottling line aims for 48 bottles per batch. Each batch count is recorded beside its target, and the supervisor needs a flag for each batch and a total of batches that hit the target exactly.

| Batch | Bottles Filled | Target |
| --- | --- | --- |
| Batch A | 48 | 48 |
| Batch B | 47 | 48 |
| Batch C | 50 | 50 |

**Task:** Flag each batch that matches its target in column D, starting at row 2, and total the flags.

**Solution:**

```excel
=DELTA(B2,C2)
```

Enter this in D2 and fill it down to D4. Then enter `=SUM(D2:D4)` in D5.

**Answer:** `1`, `0`, and `1` for the three flags, and a total of `2`. Batch A and Batch C hit their targets, and Batch B is one bottle short.

### Problem 2: Empty Bin Count

A warehouse counts the units in each bin. An empty bin has a count of 0, and the cycle count needs the number of empty bins so the replenishment team can plan a restock.

| Bin | Units |
| --- | --- |
| B-01 | 0 |
| B-02 | 12 |
| B-03 | 0 |
| B-04 | 3 |

**Task:** Flag each empty bin in column C, starting at row 2, and total the flags.

**Solution:**

```excel
=DELTA(B2)
```

Enter this in C2 and fill it down to C5. Then enter `=SUM(C2:C5)` in C6.

**Answer:** `1`, `0`, `1`, `0`, and a total of `2`. Bins B-01 and B-03 are empty.

<!-- Image 2: Batch Flags Table. See Images/Engineering/DELTA.md -->

## Use Cases

### Batch Target Checks

**Scenario:** A production report marks each batch that met its count target and shows the share that did.

```excel
=DELTA(B2,C2)
```

**Why It Works:** Fill the formula down the table so each row returns 1 or 0, and a SUM or AVERAGE over the flag column gives the count or share of batches that matched. Confirm that both columns hold numbers, because text returns `#VALUE!`.

### Inventory Count Matching

**Scenario:** A stock check compares the system quantity with the counted quantity to find rows that agree.

```excel
=IF(DELTA(C2,D2)=1,"Matched","Recount")
```

**Why It Works:** DELTA gives a clean numeric test, and IF turns the flag into a readable status. Rows that return "Recount" go back to the floor for a second count.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | One argument is text or a date stored as text. | Convert the value to a number or use an IF test for text. |
| Unexpected 1 | The second argument is blank, so the first is compared with zero. | Enter the target in the second argument, or confirm the blank is intended. |
| Unexpected 0 | Values look equal but differ in decimal places. | Round both values to the same precision before comparing. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions, including Microsoft 365 and Excel for the web | Returns 1 or 0 for numeric arguments. |
| Google Sheets | Available | Compares numbers only, and a blank cell is treated as zero. For other value types, the help page points to EQ. |

## Tips and Best Practices

- Put the DELTA flag in its own column so the totals stay visible in the sheet.
- Round values before comparing when they come from calculations, since tiny differences make a match fail.
- Leave `number2` out only when you mean to test against zero.
- Use SUM over the flag column to count matches, and COUNTIF with 0 to count mismatches.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GESTEP](GESTEP.md) | Returns 1 when a number is at or above a threshold, a related numeric test. |
| [IF](../Logical/IF.md) | Turns the 1 or 0 flag into a text status such as Matched. |
| [IFERROR](../Logical/IFERROR.md) | Handles `#VALUE!` from text inputs without breaking a column. |
| [SUM](../Math%20%26%20Trig/SUM.md) | Totals the flags to count matching rows. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Totals flags across several conditions in one formula. |

## Official Documentation

- [Microsoft Support: DELTA function](https://support.microsoft.com/en-us/excel/functions/delta-function)
- [Google Docs Editors Help: DELTA](https://support.google.com/docs/answer/3401147)
