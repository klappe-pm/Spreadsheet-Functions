---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
purpose:
  - Counting
  - Data Cleaning
use-case:
  - Field Completeness Review
  - Form Submission Validation
  - Inventory Recount Flags
related:
  - COUNTA
  - COUNTIF
  - ISBLANK
  - LEN
  - SUMPRODUCT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/countblank-function
  - https://support.google.com/docs/answer/3093403
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Count Blank Cells
  - Count Empty Cells
  - Count Missing
tags:
  - blank
  - counting
  - data-quality
  - excel
  - sheets
---

# COUNTBLANK

## Description

**COUNTBLANK** returns how many cells in a range are blank. It answers the question "how many cells are missing data?" It is the counterpart of COUNTA for a single range, and it is the quickest way to measure gaps in a column before an analysis or an import.

A cell counts as blank when it is truly empty or when it holds a formula that returns an empty string (`""`). Both Excel and Google Sheets follow this rule, so the same sheet gives the same result on either platform. A cell that holds zero is not blank, and a cell that holds a space is not blank either, because each one holds a value.

The complement is not exact when formulas return empty strings. COUNTA also counts those cells, so `COUNTBLANK(range) + COUNTA(range)` is greater than the number of cells whenever a formula returns `""`. The sum equals the total only when no cell in the range contains such a formula.

## Syntax

```excel
=COUNTBLANK(range)
```

<!-- Image 1: Blank and Filled Cells in a Range. See Images/Statistical/COUNTBLANK.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `range` | Yes | The cells to check. Excel accepts one contiguous range. Google Sheets lists `value1` and an optional `value2` in its syntax, but its tips say counting across multiple columns is not supported, so test before combining ranges. |

### Return Value

A whole number: the count of blank cells in the range. COUNTBLANK returns 0 when no cell is blank and the total number of cells when every cell is blank.

## Examples

### Example 1: Count Gaps in a Name List

Cells `A1:A10` hold Lia, Ben, a blank cell, Owen, a blank cell, a blank cell, Ada, Ravi, a blank cell and Mei.

```excel
=COUNTBLANK(A1:A10)
```

**Result:** `4`

Four cells are empty. The six names are not counted.

### Example 2: No Gaps

Cells `A1:A5` hold the letters A to E.

```excel
=COUNTBLANK(A1:A5)
```

**Result:** `0`

Every cell has a value, so there are no gaps.

### Example 3: Formula Results Count as Blank

Cell `A1` holds Value, cell `A2` holds `=IF(FALSE, "Yes", "")`, and cell `A3` is empty.

```excel
=COUNTBLANK(A1:A3)
```

**Result:** `2`

Cell `A2` shows nothing because its formula returns an empty string, and both Excel and Google Sheets treat that as blank. Cell `A1` is the only filled cell.

<!-- Image 2: Formula Blanks Counted. See Images/Statistical/COUNTBLANK.md -->

### Example 4: Zero Is Not Blank

Cells `A1:A5` hold 0, a blank cell, 0, a blank cell and 0.

```excel
=COUNTBLANK(A1:A5)
```

**Result:** `2`

The three zeros are values. Only the two truly empty cells count. If zeros mean missing data in your sheet, add a separate COUNTIF for zero.

### Example 5: A Space Is Not Blank

Cell `A1` holds Text, cell `A2` holds a single space, and cell `A3` is empty.

```excel
=COUNTBLANK(A1:A3)
```

**Result:** `1`

The space in `A2` is a character, so the cell is not blank. Use `TRIM` on the data or check the length with `LEN` to find cells like this.

### Example 6: Two-Dimensional Range

The grid `A1:C3` has one blank cell in row 1, two in row 2 and one in row 3.

```excel
=COUNTBLANK(A1:C3)
```

**Result:** `4`

COUNTBLANK counts blanks across the rectangle, so a grid of any shape works as long as it is one contiguous range.

### Example 7: Percentage of Missing Values

Cells `B2:B101` hold 100 rows, and 12 of them are blank.

```excel
=COUNTBLANK(B2:B101)/ROWS(B2:B101)
```

**Result:** `0.12` (display as 12 percent)

Dividing by the number of rows turns the count into a missing rate that can be compared across columns.

## Story Problems

### Problem 1: Customer Email Gaps

A marketing list has six rows in `B2:B7`. Row 4 holds a formula that returns an empty string because no email was found in the source.

| Customer | Email |
| --- | --- |
| Ruth | ruth@example.org |
| Marco | (blank) |
| Hana | hana@example.org |
| Dev | (formula returns "") |
| Iris | iris@example.org |
| Tomas | (blank) |

**Task:** Count how many email cells are missing.

**Solution:**

```excel
=COUNTBLANK(B2:B7)
```

**Answer:** `3`. Marco and Tomas are truly empty, and Dev's formula returns an empty string. Both platforms count all three.

### Problem 2: Inventory Quantities

A count sheet has six items in `B2:B7`. Two items were not counted, and the item with zero stock was counted as zero.

| Item | Quantity |
| --- | --- |
| Bolt | 14 |
| Clamp | (blank) |
| Dowel | 0 |
| Eyelet | (blank) |
| Flange | 8 |
| Grommet | 3 |

**Task:** Count the items that still need a quantity.

**Solution:**

```excel
=COUNTBLANK(B2:B7)
```

**Answer:** `2`. The zero for Dowel is a value, so it is not counted as missing.

## Use Cases

### Field Completeness Review

**Scenario:** Before analysis, an analyst checks how many values are missing in each important column of a customer table.

```excel
=COUNTBLANK(EmailColumn)/ROWS(EmailColumn)
```

**Why It Works:** Each column gets a missing rate. Columns with high rates are the first to clean or to exclude from analysis.

### Form Submission Validation

**Scenario:** An application form has required fields in columns B to G. Forms with gaps go to a follow-up queue.

```excel
=IF(COUNTBLANK(B2:G2)=0, "Ready to Process", "Missing " & COUNTBLANK(B2:G2) & " Fields")
```

**Why It Works:** The formula reads one row of required fields. Fields that a formula fills with an empty string count as missing, which matches what the reviewer sees.

### Inventory Recount Flags

**Scenario:** A warehouse team wants every item without a quantity flagged for recount.

```excel
=IF(COUNTBLANK(C2)>0, "Recount", "OK")
```

**Why It Works:** Each row checks its own cell. Filtering the flags produces the recount list. Zero stock is a valid count, so it stays out of the list.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Count is much higher than expected | The range is a whole column, so empty rows below the data count. | Use a bounded range such as `A1:A500`. |
| Count is lower than expected | Cells hold spaces or other invisible characters. | Clean the data with `TRIM` and `CLEAN`, then count again. |
| Zeros not counted | Zero is a value, not a blank. | Add a COUNTIF for zero when zeros mean missing data. |
| Formula blanks not expected | A formula returns an empty string, which both platforms count as blank. | Keep the rule in mind, or check with `SUMPRODUCT(--(LEN(range)=0))` for the same result. |
| Error with several ranges | Excel accepts one range per call. | Use one COUNTBLANK per range and add the results. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | Counts empty cells and cells with formulas returning `""` as blank. Accepts one range. |
| Google Sheets | Available | The help note states that cells with no content and cells with an empty string count as blank. The syntax lists `value1` and an optional `value2`, but the tips say multi-column counting is not supported. |

## Tips and Best Practices

- Use a bounded range instead of a whole column to avoid counting empty rows far below the data.
- Check for spaces with `LEN` when a cell looks empty but COUNTBLANK does not count it.
- Use COUNTA with COUNTBLANK to check a range, but remember that formula blanks are counted by both.
- Use a missing rate, such as `COUNTBLANK(range)/ROWS(range)`, when readers compare columns of different lengths.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNTA](COUNTA.md) | Counts the non-empty cells, which complements this count for the same range. |
| [COUNTIF](COUNTIF.md) | Counts cells that match a condition, such as zero or a specific text. |
| [ISBLANK](../Information/ISBLANK.md) | Tests one cell for a truly empty value. It returns FALSE for a formula that returns an empty string. |
| [LEN](../Text/LEN.md) | Returns the character count, which separates truly empty cells from cells with spaces. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Counts blanks with custom conditions, including formula blanks. |

## Official Documentation

- [Microsoft Support: COUNTBLANK function](https://support.microsoft.com/en-us/excel/functions/countblank-function)
- [Google Docs Editors Help: COUNTBLANK](https://support.google.com/docs/answer/3093403)
