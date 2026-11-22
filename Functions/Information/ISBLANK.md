---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Data Validation
  - Type Checking
use-case:
  - Required Field Checks
  - Skipping Empty Rows
related:
  - COUNTBLANK
  - ISNONTEXT
  - ISNUMBER
  - ISTEXT
  - LEN
level: 2
source:
  - https://support.microsoft.com/en-us/excel/is-functions
  - https://support.google.com/docs/answer/3093290
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Blank Cell Test
tags:
  - blank-cells
  - data-validation
  - excel
  - sheets
  - type-checks
---

# ISBLANK

## Description

**ISBLANK** tests whether a cell is empty. It returns TRUE when the reference points to a truly empty cell and FALSE when the cell holds anything at all, including a space, a number, a text label or a formula.

Use ISBLANK in required-field checks, to skip empty rows during an import, or to show a prompt next to an input that has not been filled in. It is the simplest way to ask whether a cell has been left empty.

The most common surprise is a formula that returns an empty string. A cell with `=""` looks blank on the screen, but ISBLANK returns FALSE because the formula is content. Microsoft and Google both describe the function as checking for an empty cell, so use LEN or COUNTBLANK when the test must also treat empty text as missing. The function is most often combined with IF, because the test on its own only returns TRUE or FALSE.

## Syntax

```excel
=ISBLANK(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISBLANK.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value to test. In practice this is a reference to a cell, such as `B2`. Microsoft also accepts a blank cell, a value, an error, text or a name that refers to one of these. |

### Return Value

TRUE when the reference points to an empty cell. FALSE for any cell with content, including spaces, numbers, text, error values and formulas that return empty text.

## Examples

### Example 1: Empty Cell

Cell A2 is empty.

```excel
=ISBLANK(A2)
```

**Result:** `TRUE`

### Example 2: Cell With a Value

Cell A1 holds the number 120.

```excel
=ISBLANK(A1)
```

**Result:** `FALSE`

### Example 3: Formula That Returns Empty Text

Cell A3 contains the formula `=""`.

```excel
=ISBLANK(A3)
```

**Result:** `FALSE`

The formula result is empty text, which counts as content, so the test returns FALSE.

<!-- Image 2: Blank Versus Empty Text. See Images/Information/ISBLANK.md -->

### Example 4: Showing a Result Only When Input Exists

Cell A1 holds 120 and cell B1 is empty.

```excel
=IF(ISBLANK(B1), "", A1/B1)
```

**Result:** `""` (empty text, so the cell looks blank)

When B1 is empty, the formula returns empty text instead of a division error.

### Example 5: Spaces Count as Content

Cell A4 contains a single space typed by a user.

```excel
=ISBLANK(A4)
```

**Result:** `FALSE`

The space is content, so the cell is not blank. Use TRIM in a combined test to treat spaces as missing.

## Story Problems

### Problem 1: Missing Hours on a Timesheet

A timesheet lists hours in column B. Ben and Dee have not entered their hours yet.

| Employee | Hours |
| --- | --- |
| Ana | 8 |
| Ben | |
| Cy | 6.5 |
| Dee | |

**Task:** Put a formula in C2 that returns `Missing` when B2 is empty and `Entered` otherwise, then fill it down to row 5.

**Solution:**

```excel
=IF(ISBLANK(B2), "Missing", "Entered")
```

**Answer:** Ana and Cy show `Entered`. Ben and Dee show `Missing`, so two hours cells are still empty.

### Problem 2: Formula Blanks in a Discount Column

A discount column holds three kinds of cells. Row 2 is a true blank. Row 3 holds a formula that returns empty text. Rows 4 and 5 hold percentages.

| Row | Discount |
| --- | --- |
| 2 | (true blank) |
| 3 | (formula returning "") |
| 4 | 10% |
| 5 | 5% |

**Task:** Count the truly empty discount cells in B2:B5 with ISBLANK.

**Solution:**

```excel
=SUMPRODUCT(--ISBLANK(B2:B5))
```

**Answer:** `1`. Only row 2 is truly empty. Row 3 looks blank but contains a formula, so ISBLANK returns FALSE for it.

## Use Cases

### Required Field Checks

**Scenario:** A purchase request sheet needs a quantity before the total is calculated, and the reviewer wants a visible reminder when it is missing.

```excel
=IF(ISBLANK(C2), "Quantity required", C2*D2)
```

**Why It Works:** The reminder appears only for an empty quantity. Once the quantity is entered, the formula returns the line total.

### Skipping Empty Rows During an Import

**Scenario:** A data import brings in rows with empty trailing lines, and the totals should ignore them.

```excel
=IF(ISBLANK(A2), 0, A2*B2)
```

**Why It Works:** Empty rows return 0 and do not add noise to the totals. Confirm that the import does not store formulas that return empty text in the same column, because ISBLANK would not catch them.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| FALSE for a cell that looks empty | The cell holds spaces, empty text from a formula or a hidden character. | Test with `LEN(TRIM(B2))=0` instead. |
| TRUE count is too low | Formulas that return empty text count as content. | Use COUNTBLANK or a LEN-based test for those cells. |
| Single result for a range | ISBLANK returns one result for one reference. | Use SUMPRODUCT with `--ISBLANK(range)` in Excel, or ARRAYFORMULA in Google Sheets. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions, including Excel for the web | Accepts a blank cell, value, error, text, number or reference. Use SUMPRODUCT for counts over a range. |
| Google Sheets | Available | Same result for empty cells and for formulas that return empty text. Use ARRAYFORMULA for ranges. |

## Tips and Best Practices

- Use ISBLANK for true empties and LEN or COUNTBLANK when formulas may return empty text.
- Combine ISBLANK with IF so the test returns a message or a calculation rather than a bare TRUE or FALSE.
- Keep import sheets free of formulas in input columns if you rely on ISBLANK.
- Use TRIM when users may type spaces into input cells.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNTBLANK](../Statistical/COUNTBLANK.md) | Counts empty cells in a range, including formulas that return empty text. |
| [ISNONTEXT](ISNONTEXT.md) | Tests whether a value is not text. Blank cells return TRUE. |
| [ISNUMBER](ISNUMBER.md) | Tests whether a value is a number. |
| [ISTEXT](ISTEXT.md) | Tests whether a value is text. |
| [LEN](../Text/LEN.md) | Counts characters, which helps find empty text and spaces. |

## Official Documentation

- [Microsoft Support: IS functions](https://support.microsoft.com/en-us/excel/is-functions)
- [Google Docs Editors Help: ISBLANK](https://support.google.com/docs/answer/3093290)
