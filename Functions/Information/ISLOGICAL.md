---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Data Validation
  - Type Checking
use-case:
  - Checkbox Column Audit
  - Mixed Entry Check
  - Status Routing
related:
  - IF
  - ISNONTEXT
  - ISNUMBER
  - ISTEXT
  - SUMPRODUCT
level: 1
source:
  - https://support.microsoft.com/en-us/excel/is-functions
  - https://support.google.com/docs/answer/3093351
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - data-validation
  - excel
  - information
  - sheets
  - type-checking
---

# ISLOGICAL

## Description

**ISLOGICAL** returns TRUE when a value is a logical value, meaning the Boolean TRUE or FALSE. A logical value can be typed directly, come from a checkbox, or be the result of a comparison such as `5>3`. Text that reads "TRUE" is not a logical value, and neither is the number 1.

Use ISLOGICAL to check that a column of yes or no answers really holds TRUE and FALSE, or to route each row differently depending on whether its entry is a logical value or something else.

ISLOGICAL pairs with IF in most formulas. Both Microsoft Excel and Google Sheets document it as a test for a value that is already logical, so it does not convert text or numbers.

## Syntax

```excel
=ISLOGICAL(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISLOGICAL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value or cell reference to test. It can be a literal TRUE or FALSE, a comparison, or a cell that holds a logical value. |

### Return Value

TRUE when `value` is a logical value, or a reference to a cell that holds one. FALSE for any other value, including text, numbers and blank cells.

## Examples

### Example 1: Testing a Checkbox Cell

Cell A2 holds a checkbox that is ticked, so it contains `TRUE`.

```excel
=ISLOGICAL(A2)
```

**Result:** `TRUE`

The cell holds a logical value, so the function returns TRUE.

### Example 2: Testing a Comparison

```excel
=ISLOGICAL(5>3)
```

**Result:** `TRUE`

The comparison returns the logical value TRUE, so the function returns TRUE.

### Example 3: Text That Looks Like a Logical Value

Cell A3 holds the text string `TRUE`, which looks like a logical value but is stored as text.

```excel
=ISLOGICAL(A3)
```

**Result:** `FALSE`

The function does not convert text, so the text "TRUE" is not a logical value.

### Example 4: Routing Each Row

Cell B2 holds the checkbox value `TRUE`.

```excel
=IF(ISLOGICAL(B2),IF(B2,"Met","Missed"),"Check")
```

**Result:** `Met`

The outer IF sends logical values to the inner test and everything else to the "Check" label.

## Story Problems

### Problem 1: Counting Completed Checkboxes

A project checklist uses checkboxes in column B. Some rows were filled in by a team member who typed "Yes" instead of ticking the box. The manager wants to count rows that hold a real checkbox value.

| Task | Done |
| --- | --- |
| Order parts | TRUE |
| Schedule visit | FALSE |
| Send invoice | Yes |
| Close file | TRUE |

**Task:** Count the logical values in `B2:B5`.

**Solution:**

```excel
=SUMPRODUCT(ISLOGICAL(B2:B5)*1)
```

**Answer:** `3`. The "Yes" entry is text, so only the three checkbox values count.

### Problem 2: Routing Checklist Results

The same checklist needs a status column. A logical TRUE means "Met", a logical FALSE means "Missed", and anything else needs a manual check.

| Task | Done | Status |
| --- | --- | --- |
| Order parts | TRUE | |
| Schedule visit | FALSE | |
| Send invoice | Pending | |
| Close file | TRUE | |

**Task:** Fill the Status column in `C2:C5` so each row shows the correct label.

**Solution:**

```excel
=IF(ISLOGICAL(B2),IF(B2,"Met","Missed"),"Check")
```

**Answer:** Met, Missed, Check, Met. The Pending entry is text, so it gets the "Check" label.

<!-- Image 2: Checkbox Routing Results. See Images/Information/ISLOGICAL.md -->

## Use Cases

### Checkbox Column Audit

**Scenario:** A tracker imports checkbox states from another system, and some values arrive as text after the import.

```excel
=COUNTA(B2:B100)-SUMPRODUCT(ISLOGICAL(B2:B100)*1)
```

**Why It Works:** The formula counts the non-blank entries and subtracts the logical values. What remains is the number of rows that arrived as text and need to be reconnected to real checkboxes.

### Mixed Entry Check

**Scenario:** A form collects approval answers that should always be TRUE or FALSE, but people sometimes type a word.

```excel
=IF(ISLOGICAL(C2),"Valid","Fix entry")
```

**Why It Works:** Each entry is checked as it is recorded. A reviewer sees "Fix entry" beside any row that needs attention before the approvals are counted.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for a value that displays TRUE | The value is the text "TRUE", often from a pasted or imported file. | Reinsert the checkbox or compare the text with `=B2="TRUE"`. |
| `FALSE` for a 1 or 0 | Numbers are not logical values. | Test the number directly, such as `=B2=1`. |
| Checkboxes return FALSE after a paste | The paste brought in the displayed text, not the logical value. | Paste as values only or rebuild the checkbox column. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Excel 2024, Excel 2021, Excel 2019, Excel 2016 and Excel for the web. | Works with checkbox columns and comparison results. Text is not converted. |
| Google Sheets | Available | Same syntax and return value. Works with checkbox columns and comparison results. |

## Tips and Best Practices

- Use ISLOGICAL in data checks before totals or routing logic depends on TRUE and FALSE values.
- Pair with IF to give each non-logical entry a clear label instead of an error.
- Use ISNUMBER and ISTEXT for other data types, because ISLOGICAL only identifies Boolean values.
- Use SUMPRODUCT with `*1` to count logical values in a range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IF](../Logical/IF.md) | Routes each row based on the ISLOGICAL result. |
| [ISNUMBER](ISNUMBER.md) | Tests for numeric values, the counterpart to logical checks. |
| [ISTEXT](ISTEXT.md) | Tests for text values, including the text "TRUE". |
| [ISNONTEXT](ISNONTEXT.md) | Tests for anything that is not text, including logical values. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Counts or totals the values that pass the ISLOGICAL test. |

## Official Documentation

- [Microsoft Support: IS functions](https://support.microsoft.com/en-us/excel/is-functions)
- [Google Docs Editors Help: ISLOGICAL](https://support.google.com/docs/answer/3093351)
