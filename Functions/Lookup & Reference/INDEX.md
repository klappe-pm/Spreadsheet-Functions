---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Classic Lookup
purpose:
  - Data Retrieval
use-case:
  - Latest Entry Lookup
  - Price List Lookup
  - Regional Sales Matrix
related:
  - CHOOSE
  - FILTER
  - MATCH
  - OFFSET
  - VLOOKUP
  - XLOOKUP
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/index-function
  - https://support.google.com/docs/answer/3098242
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Array Index
  - Cell Index
  - Range Index
tags:
  - excel
  - index-match
  - lookup
  - reference
  - sheets
---

# INDEX

## Description

**INDEX** returns the value at a position you specify inside a range. You give it the range, a row number and, for a table, a column number, and it returns whatever sits at that intersection. Use it when you know where a value is in a table but do not need to search for it, or when you want a whole row or column returned as an array.

INDEX is most useful paired with MATCH. MATCH finds the position of a lookup value, and INDEX returns the value at that position from any column, including columns to the left of the lookup column. VLOOKUP cannot do that. For a one-off lookup, XLOOKUP or VLOOKUP may read more easily, but INDEX with MATCH keeps working when columns are inserted or moved because it does not depend on a fixed column number.

Microsoft documents two forms. The array form, shown in the syntax below, reads from one range and returns a value. This is the form used in almost every formula. The reference form accepts several ranges in parentheses, uses `area_num` to choose one, and returns a reference to the cell instead of its value. Google Sheets documents only the array form, with `reference`, `row` and `column` arguments.

## Syntax

```excel
=INDEX(array, row_num, [column_num])
```

```excel
=INDEX(reference, row_num, [column_num], [area_num])
```

<!-- Image 1: INDEX Argument Anatomy. See Images/Lookup & Reference/INDEX.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array constant to read from. If it has only one row or one column, `row_num` or `column_num` can be omitted. |
| `row_num` | Yes, unless `column_num` is given | The row within the range to return from. The first row is 1. A value of `0` returns the entire column as an array. |
| `column_num` | No | The column within the range to return from. The first column is 1. A value of `0` returns the entire row as an array. |
| `reference` | Yes (reference form) | One range, or several ranges in parentheses separated by commas, to read from. |
| `area_num` | No (reference form) | Which range in `reference` to use. The first range is 1. Defaults to 1 when omitted. |

### Return Value

The value at the intersection of `row_num` and `column_num`. When `row_num` or `column_num` is `0`, or one of them is left out on a multi-row, multi-column range, INDEX returns the whole column or row as an array. The reference form returns a reference to the cell instead of its value.

INDEX returns `#REF!` when `row_num`, `column_num` or `area_num` points outside the range. In the reference form, `#VALUE!` appears when the areas are on different sheets.

## Examples

All examples use this product list in `A1:D6`.

| Item | Category | Price | Stock |
| --- | --- | --- | --- |
| Pens | Office | 2.50 | 120 |
| Staplers | Office | 9.00 | 35 |
| Mugs | Kitchen | 6.25 | 60 |
| Kettles | Kitchen | 24.00 | 12 |
| Notebooks | Office | 4.75 | 80 |

### Example 1: Value by Position in One Column

```excel
=INDEX(C2:C6, 3)
```

**Result:** `6.25`

A single-column range needs only a row number. Position 3 in `C2:C6` is `C4`, the price of Mugs.

### Example 2: Value by Row and Column

```excel
=INDEX(A2:D6, 2, 4)
```

**Result:** `35`

Row 2 of the range is the Staplers row, and column 4 of the range is Stock. The positions are counted inside `A2:D6`, not from the top of the sheet.

### Example 3: Price for a Named Item

```excel
=INDEX(C2:C6, MATCH("Mugs", A2:A6, 0))
```

**Result:** `6.25`

MATCH returns 3 because Mugs is the third item in `A2:A6`. INDEX then returns the third value from `C2:C6`.

### Example 4: Two-Way Lookup

```excel
=INDEX(A2:D6, MATCH("Mugs", A2:A6, 0), MATCH("Stock", A1:D1, 0))
```

**Result:** `60`

The first MATCH finds the row for Mugs. The second MATCH finds the Stock column in the header row. INDEX returns the cell where they meet.

<!-- Image 2: Two-Way Lookup Grid. See Images/Lookup & Reference/INDEX.md -->

### Example 5: Returning a Whole Row

```excel
=INDEX(A2:D6, 4, 0)
```

**Result:** `Kettles`, `Kitchen`, `24.00`, `12` (spills across four cells in Microsoft 365 and Google Sheets)

A column number of `0` returns every column in row 4 of the range. In legacy Excel, enter this as an array formula, or use it inside a function that accepts arrays.

### Example 6: Reverse Lookup to the Left

```excel
=INDEX(A2:A6, MATCH(24, C2:C6, 0))
```

**Result:** `Kettles`

The lookup value is in column C, and the returned value is in column A, to its left. VLOOKUP cannot read a column to the left of its lookup column, so this pattern is a common reason to use INDEX with MATCH.

## Story Problems

### Problem 1: Quarterly Bonus Lookup

A manager keeps bonus amounts in `A1:B6`. Each row holds one employee name and one bonus.

| Name | Bonus |
| --- | --- |
| Ana | 1200 |
| Ben | 850 |
| Cy | 1500 |
| Dee | 990 |
| Eli | 700 |

**Task:** Type a name in `D2` and return that person's bonus with INDEX and MATCH.

**Solution:**

```excel
=INDEX(B2:B6, MATCH(D2, A2:A6, 0))
```

**Answer:** `1500`, because Cy is the third name in the list and Cy's bonus is 1500.

### Problem 2: Largest Order

A shop lists order totals in `A1:B5`.

| Order | Total |
| --- | --- |
| O-101 | 240 |
| O-102 | 515 |
| O-103 | 98 |
| O-104 | 310 |

**Task:** Return the order number with the largest total.

**Solution:**

```excel
=INDEX(A2:A5, MATCH(MAX(B2:B5), B2:B5, 0))
```

**Answer:** `O-102`, because its total of 515 is the largest value in `B2:B5`.

<!-- Image 3: Problem 2 Result Panel. See Images/Lookup & Reference/INDEX.md -->

## Use Cases

### Regional Sales Matrix

**Scenario:** A sales report has products down the rows and regions across the columns. A manager picks a product and a region from two drop-down lists, and the report shows the matching sales figure.

```excel
=INDEX(SalesMatrix, MATCH(ProductPick, ProductList, 0), MATCH(RegionPick, RegionList, 0))
```

**Why It Works:** Each MATCH converts a text choice into a position, and INDEX reads the cell at that row and column. Changing a drop-down changes the output without rewriting the formula. The named ranges must list products and regions in the same order as the rows and columns of `SalesMatrix`.

### Latest Entry Lookup

**Scenario:** A log sheet receives one new entry per day in column A, starting in row 2. A dashboard needs to show the most recent entry without someone updating a cell reference each day.

```excel
=INDEX(A:A, COUNTA(A:A))
```

**Why It Works:** COUNTA counts the filled cells in column A, including the header in row 1, so the count equals the row number of the last entry. This works only when the column has no blank cells. If blanks can appear, use a formula based on `LOOKUP(2, 1/(A:A<>""), A:A)` instead.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#REF!` | `row_num` or `column_num` is larger than the range, or is negative. | Check the size of the range, or count positions from the start of the range rather than the sheet. |
| `#REF!` | `area_num` refers to an area that does not exist in the reference form. | Check how many ranges are listed in parentheses. |
| `#N/A` | A MATCH inside INDEX cannot find the lookup value. | Check spelling, spaces and data types, or wrap the MATCH in IFERROR. |
| `#VALUE!` | The reference form uses areas on different sheets. | Use the array form with CHOOSE, or move the data to one sheet. |
| Wrong value | The row or column number counts from the start of the range, not the sheet. | Use the position inside the range, or compute it with MATCH. |
| Array spills or is blank in older Excel | `0` returns a whole row or column, which older Excel shows as a single value unless entered as an array formula. | Confirm the formula as an array formula, or wrap it in a function that takes arrays. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Supports the array and reference forms. In Microsoft 365 a `0` row or column spills automatically. Earlier versions need Ctrl+Shift+Enter for whole-row or whole-column results. |
| Google Sheets | Available | Documents `reference`, `row` and `column`. A `row` or `column` of `0` returns the whole column or row, and both default to 0 when omitted. No `area_num` argument is documented. |

## Tips and Best Practices

- Pair INDEX with MATCH for lookups that may need columns on either side of the lookup column.
- Use absolute references such as `$B$2:$B$100` for the ranges so they stay fixed when the formula is copied, and leave the lookup value relative.
- Store the MATCH result in a helper cell when several INDEX formulas read different columns with the same row.
- Count positions from the first row or column of the range, not from the top of the sheet.
- Wrap the formula in IFERROR when a missing lookup value should show a message instead of `#N/A`.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MATCH](MATCH.md) | Returns the position that INDEX needs. |
| [CHOOSE](CHOOSE.md) | Returns one value from a short list of values by position. |
| [FILTER](FILTER.md) | Returns every matching row instead of one value. |
| [OFFSET](OFFSET.md) | Returns a range by moving from a starting cell. It is volatile, so INDEX is usually the better choice for dynamic ranges. |
| [VLOOKUP](VLOOKUP.md) | Searches the first column and returns a value to its right. |
| [XLOOKUP](XLOOKUP.md) | Searches and returns in one function, in either direction. |

## Official Documentation

- [Microsoft Support: INDEX function](https://support.microsoft.com/en-us/excel/functions/index-function)
- [Google Docs Editors Help: INDEX](https://support.google.com/docs/answer/3098242)
