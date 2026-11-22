---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Data Cleaning
  - Type Checking
use-case:
  - Checkbox Flag Totals
  - Date Serial Comparisons
  - Shipping Surcharge Flags
related:
  - ISLOGICAL
  - ISNUMBER
  - ISTEXT
  - TYPE
  - VALUE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/n-function
  - https://support.google.com/docs/answer/3093357
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Convert To Number
  - Logical To Number
tags:
  - compatibility
  - conversion
  - data-cleaning
  - excel
  - sheets
---

# N

## Description

**N** converts a value to a number. A number comes back unchanged, TRUE becomes 1, FALSE becomes 0, and a date returns its serial number. Text and blank cells return 0, and an error value passes through unchanged. Use N when a formula needs a numeric result from a cell that holds a logical flag or a date, and you want the conversion to be explicit.

N is a narrow tool. It does not read numbers out of text: the text "7" returns 0 because it is text, not a number. Use VALUE for numeric text. Excel converts most values automatically during arithmetic, so most workbooks never need N. The function exists mainly for compatibility with other spreadsheet programs, and it is most useful when a reader or an export expects a plain number.

Google Sheets follows the same return rules, with one difference in how it counts dates: its serial numbers start from December 30, 1899, so they match Excel serials for dates on or after March 1, 1900.

## Syntax

```excel
=N(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/N.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value to convert: a number, a date, TRUE or FALSE, text, an error value, or a reference to any of these. |

### Return Value

A number. The result depends on the type of `value`: a number returns itself, TRUE returns 1, FALSE returns 0, a date returns its serial number, and text or a blank cell returns 0. An error value returns the same error.

## Examples

All examples use this sample data:

| Cell | Value |
| --- | --- |
| A2 | 12.5 |
| A3 | Pending |
| A4 | TRUE |
| A5 | FALSE |
| A6 | 3/1/2024 |
| A7 | `#DIV/0!` error |

### Example 1: Converting a Number

```excel
=N(A2)
```

**Result:** `12.5`

The number is returned unchanged, so N has no effect on it.

### Example 2: Converting Text

```excel
=N(A3)
```

**Result:** `0`

The text "Pending" is not a number, so N returns 0.

### Example 3: Converting Logical Values

```excel
=N(A4)+N(A5)
```

**Result:** `1`

TRUE becomes 1 and FALSE becomes 0, so the sum is 1. This is the pattern used to count flags.

<!-- Image 2: TRUE and FALSE Converted to 1 and 0. See Images/Information/N.md -->

### Example 4: Converting a Date

```excel
=N(A6)
```

**Result:** `45352`

March 1, 2024 is the 45,352nd day after December 30, 1899, so N returns that serial number. Format the cell as a date only when a date display is needed.

### Example 5: Passing Through an Error

```excel
=N(A7)
```

**Result:** `#DIV/0!`

N does not hide errors. The error value returns unchanged, so the next formula in the chain receives it.

### Example 6: Replacing an Error With a Default

```excel
=IFERROR(N(A7), 0)
```

**Result:** `0`

Wrapping N in IFERROR turns the error into a default value that downstream totals can add safely.

## Story Problems

### Problem 1: Express Shipping Surcharge

A shop marks express orders with TRUE in column C. Each express order pays a 5.00 surcharge on top of the base fee in column B.

| Order | Base Fee | Express |
| --- | --- | --- |
| A-101 | 12 | TRUE |
| A-102 | 12 | FALSE |
| A-103 | 18 | TRUE |

**Task:** In `D2`, calculate the total fee for each order, then fill the formula down to row 4.

**Solution:**

```excel
=B2+N(C2)*5
```

**Answer:** A-101 costs `17` (12 + 5), A-102 costs `12` because it is not express, and A-103 costs `23` (18 + 5).

<!-- Image 3: Surcharge Table Result. See Images/Information/N.md -->

### Problem 2: Checking an Invoice Date Against a Cutoff

An accounts clerk stores invoice dates as real dates. An export tool needs the serial number of each date, and the clerk needs to know the serial for March 15, 2026 in cell `B2`.

| Invoice | Date |
| --- | --- |
| INV-884 | 3/15/2026 |

**Task:** Return the serial number of the date in `B2`.

**Solution:**

```excel
=N(B2)
```

**Answer:** `46096`. Counting from December 30, 1899, March 15, 2026 is 46,096 days later. This assumes the default 1900 date system.

## Use Cases

### Checkbox Flag Totals

**Scenario:** A project tracker has TRUE and FALSE checkboxes in column C. The team wants a count of completed tasks in the first three rows.

```excel
=N(C2)+N(C3)+N(C4)
```

**Why It Works:** Each checkbox returns TRUE or FALSE, and N turns each one into 1 or 0. The sum is the number of checked boxes. For longer lists, use SUMPRODUCT on the full column instead.

### Date Serial Comparisons

**Scenario:** A system export compares dates as serial numbers, and the analyst needs to find rows on or after March 1, 2024.

```excel
=N(B2)>=45352
```

**Why It Works:** N returns the serial number of the date in `B2`, so the comparison uses the same numeric scale as the export. The result is TRUE for rows on or after that date.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` or another error | N returns an error value unchanged, so the error reaches the next formula. | Wrap the call in IFERROR, or correct the source cell. |
| `0` | The cell holds a number stored as text, such as "7". | Convert the text with VALUE before using N. |
| `0` | The cell holds a text label or is blank. | Check the source cell, and use IF to handle blanks explicitly. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available; the Microsoft page lists no version restriction | Dates return serial numbers in the active date system (1900 by default, 1904 optionally). |
| Google Sheets | Available | Same return rules. Date serials count from December 30, 1899, which matches Excel for dates on or after March 1, 1900. |

## Tips and Best Practices

- Use N to turn TRUE and FALSE flags into 1 and 0 without writing a comparison.
- Use VALUE for numeric text, because N returns 0 for any text.
- Check the 1904 date system setting in Excel before comparing serial numbers from workbooks created on a Mac.
- Use N only when a reader or export needs a plain number, since Excel converts most values automatically.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ISLOGICAL](ISLOGICAL.md) | Tests whether a value is TRUE or FALSE before you convert it. |
| [ISNUMBER](ISNUMBER.md) | Tests whether a value is a number, without converting it. |
| [ISTEXT](ISTEXT.md) | Tests whether a value is text, which N converts to 0. |
| [TYPE](TYPE.md) | Returns a code for the value type, useful for diagnosing why N returns 0. |
| [VALUE](../Text/VALUE.md) | Converts numeric text to a number, which N cannot do. |

## Official Documentation

- [Microsoft Support: N function](https://support.microsoft.com/en-us/excel/functions/n-function)
- [Google Docs Editors Help: N](https://support.google.com/docs/answer/3093357)
