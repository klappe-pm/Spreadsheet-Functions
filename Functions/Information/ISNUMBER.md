---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Data Validation
  - Type Checking
use-case:
  - Guarded Arithmetic
  - Lookup Found Check
  - Numeric Entry Totals
related:
  - IF
  - ISLOGICAL
  - ISNONTEXT
  - ISTEXT
  - MATCH
  - SUMPRODUCT
level: 1
source:
  - https://support.microsoft.com/en-us/excel/is-functions
  - https://support.google.com/docs/answer/3093296
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Is Numeric
tags:
  - data-validation
  - excel
  - information
  - sheets
  - type-checking
---

# ISNUMBER

## Description

**ISNUMBER** returns TRUE when a value is a number and FALSE for everything else, including text, logical values and errors. A number typed in quotation marks, such as `"123"`, is text, so it returns FALSE. Dates and times are stored as numbers in both platforms, so they return TRUE.

Use ISNUMBER to guard arithmetic against text entries, to check that an input is usable before a calculation runs, and to total only the numeric values in a mixed column. It is the most common type test in spreadsheet models.

ISNUMBER does not convert anything. To test whether text holds a valid number, convert it first with VALUE, and wrap the conversion in IFERROR if the text may not be numeric.

## Syntax

```excel
=ISNUMBER(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISNUMBER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value or cell reference to test. Numbers, dates and times return TRUE. Text and logical values return FALSE. |

### Return Value

TRUE when `value` is a number, or a reference to a cell that holds one. FALSE for text, logical values, errors and blank cells.

## Examples

### Example 1: A Number in a Cell

Cell A2 holds `450`.

```excel
=ISNUMBER(A2)
```

**Result:** `TRUE`

The cell holds a number, so the function returns TRUE.

### Example 2: A Number Typed as Text

```excel
=ISNUMBER("450")
```

**Result:** `FALSE`

The quotation marks make this a text string, so the function returns FALSE.

### Example 3: A Date

```excel
=ISNUMBER(DATE(2026,11,22))
```

**Result:** `TRUE`

DATE returns a date serial number, which is a number. The test returns TRUE.

### Example 4: Guarding a Calculation

Cell B2 holds `n/a`, and cell C2 holds `1.08`.

```excel
=IF(ISNUMBER(B2),B2*C2,"Enter a price")
```

**Result:** `Enter a price`

The multiplication runs only when B2 holds a number, which prevents a `#VALUE!` error.

## Story Problems

### Problem 1: Totaling Invoice Amounts

An accounts clerk keeps invoice amounts in column B. Some rows contain status words such as "pending" or "void" instead of amounts. The clerk needs the total of the real amounts.

| Invoice | Amount |
| --- | --- |
| INV-01 | 120 |
| INV-02 | pending |
| INV-03 | 85 |
| INV-04 | 240 |
| INV-05 | 60 |
| INV-06 | void |

**Task:** Total only the numeric amounts in `B2:B7`.

**Solution:**

```excel
=SUMPRODUCT(ISNUMBER(B2:B7)*1,B2:B7)
```

**Answer:** `505`. The four real amounts are 120, 85, 240 and 60, and the two status words add nothing.

<!-- Image 2: Invoice Total Result. See Images/Information/ISNUMBER.md -->

### Problem 2: Counting Usable Quantities

A stock count sheet holds quantities that were typed by several people. The manager wants to know how many entries are usable numbers.

| Item | Quantity |
| --- | --- |
| Bolts | 5 |
| Nuts | five |
| Washers | 8 |
| Springs | 12 units |
| Clips | 0 |

**Task:** Count the numeric quantities in `B2:B6`.

**Solution:**

```excel
=SUMPRODUCT(ISNUMBER(B2:B6)*1)
```

**Answer:** `3`. The entries 5, 8 and 0 are numbers. "five" and "12 units" are text.

## Use Cases

### Guarded Arithmetic

**Scenario:** A pricing sheet multiplies unit prices by quantities, but some prices are missing or typed as text.

```excel
=IF(ISNUMBER(B2),B2*C2,"Check input")
```

**Why It Works:** The formula multiplies only when the price is a number. Rows with bad input get a clear message instead of an error that spreads into the totals.

### Lookup Found Check

**Scenario:** A roster needs to show whether each employee ID appears in the training list.

```excel
=IF(ISNUMBER(MATCH(D2,A2:A50,0)),"Found","Missing")
```

**Why It Works:** MATCH returns a position number when it finds the value and an error when it does not. ISNUMBER turns that result into a simple test, and IF turns the test into a label.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for a number that looks correct | The number was imported as text, often with a leading apostrophe or a stray space. | Convert it with VALUE or remove the space with TRIM. |
| `FALSE` for a number with a thousands separator | The value was imported as text, such as "1,250". | Remove the comma with SUBSTITUTE or convert the column with the Text to Columns tool on the Data tab. |
| `TRUE` for a date | Dates are stored as numbers. | This is expected. Use ISTEXT or a format check if only plain numbers should count. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Microsoft 365 for Mac, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016. | Dates and times return TRUE. Numbers in quotation marks return FALSE. |
| Google Sheets | Available | Same syntax and return value. The Sheets help page notes that a number in quotes returns FALSE. |

## Tips and Best Practices

- Use ISNUMBER before any calculation that depends on user input.
- Pair with IF to show a message instead of an error when the input is not numeric.
- Use SUMPRODUCT with ISNUMBER and a comma between arrays to total only the numeric entries.
- Convert imported numbers to real numbers early so every later formula works.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IF](../Logical/IF.md) | Chooses a calculation or message based on the ISNUMBER result. |
| [ISTEXT](ISTEXT.md) | Tests for text, the counterpart to ISNUMBER for mixed columns. |
| [ISNONTEXT](ISNONTEXT.md) | Tests for every non-text value, including numbers and logical values. |
| [ISLOGICAL](ISLOGICAL.md) | Tests for TRUE and FALSE values. |
| [MATCH](../Lookup%20%26%20Reference/MATCH.md) | Returns a position number when a value is found, which ISNUMBER can test. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Totals or counts only the entries that pass the ISNUMBER test. |

## Official Documentation

- [Microsoft Support: IS functions](https://support.microsoft.com/en-us/excel/is-functions)
- [Google Docs Editors Help: ISNUMBER](https://support.google.com/docs/answer/3093296)
