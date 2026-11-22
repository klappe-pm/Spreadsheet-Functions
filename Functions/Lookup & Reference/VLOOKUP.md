---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Classic Lookup
purpose:
  - Data Retrieval
  - Reference Building
use-case:
  - Employee Records Lookup
  - Grade Band Lookup
  - Price List Lookup
related:
  - HLOOKUP
  - IFNA
  - INDEX
  - MATCH
  - XLOOKUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/vlookup-function
  - https://support.google.com/docs/answer/3093318
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Table Lookup
  - V Lookup
  - Vertical Lookup
tags:
  - approximate-match
  - exact-match
  - excel
  - lookup
  - sheets
---

# VLOOKUP

## Description

**VLOOKUP** searches for a value in the first column of a range and returns a value from another column in the same row. Give it an employee ID and it returns the name. Give it a product code and it returns the price. The "V" stands for vertical because the function moves down a column to find the key.

The lookup column must be the leftmost column of the range. VLOOKUP can only return values from columns to the right of that key column. When the answer sits to the left of the key, use [XLOOKUP](XLOOKUP.md) or [INDEX](INDEX.md) with [MATCH](MATCH.md) instead.

The fourth argument chooses the match type. `FALSE` (or `0`) requests an exact match, which suits IDs, codes and names. `TRUE` (or `1`) requests an approximate match, which assumes the first column is sorted in ascending order and returns the largest key that does not go past the search value. Omitting the argument is the same as `TRUE`, so pass `FALSE` explicitly whenever you need an exact match.

XLOOKUP is the modern replacement. It is available in Excel 2021, Excel 2024 and Microsoft 365, but not in Excel 2016 or Excel 2019. Google Sheets supports both functions. VLOOKUP remains common in existing workbooks, so it is still worth knowing.

## Syntax

```excel
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```

<!-- Image 1: VLOOKUP Syntax Anatomy. See Images/Lookup & Reference/VLOOKUP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `lookup_value` | Yes | The value to find in the first column of `table_array`. It can be a number, a text string in quotes, or a cell reference. |
| `table_array` | Yes | The range or table to search. It must include the lookup column and the column that holds the result. |
| `col_index_num` | Yes | The position of the return column, counted from 1 at the leftmost column of `table_array`. The value 1 returns the lookup column itself. |
| `range_lookup` | No | `FALSE` or `0` for an exact match. `TRUE` or `1` for an approximate match. Omitting it is the same as `TRUE`. |

### Return Value

The value in the `col_index_num` column of the first row that matches. When the key appears more than once, only the first row is used.

The function returns `#N/A` when an exact match is not found, or when an approximate lookup value is smaller than the smallest value in the first column. It returns `#REF!` when `col_index_num` is larger than the number of columns in `table_array`, and `#VALUE!` when `col_index_num` is less than 1.

## Examples

All examples use this employee list in `A1:D6`.

| Employee ID | Name | Department | Hourly Rate |
| --- | --- | --- | --- |
| E101 | Maya Reyes | Finance | 38 |
| E102 | Owen Park | Sales | 27 |
| E103 | Lena Brooks | Support | 24 |
| E104 | Tomas Vidal | Sales | 31 |
| E105 | Priya Nair | Operations | 35 |

### Example 1: Basic Exact Match

```excel
=VLOOKUP("E103", A2:D6, 2, FALSE)
```

**Result:** `Lena Brooks`

The search finds E103 in column A and returns the value from column 2 of the same row. `FALSE` guarantees that only an identical ID matches.

### Example 2: Cell Reference With a Fixed Table

With `E104` typed in cell `F2`:

```excel
=VLOOKUP(F2, $A$2:$D$6, 4, FALSE)
```

**Result:** `31`

The dollar signs lock the table so the formula still points at the same range when it is copied down. Column 4 is the hourly rate.

### Example 3: Approximate Match for Grade Bands

A band table sits in `H1:I5` with the header row `Minimum Score` and `Band`, followed by the rows `0` and `Developing`, `60` and `Proficient`, `80` and `Advanced`, and `90` and `Expert`.

```excel
=VLOOKUP(85, $H$2:$I$5, 2, TRUE)
```

**Result:** `Advanced`

The score 85 is larger than 80 but smaller than 90, so the function returns the band that starts at 80. The minimum scores must be sorted in ascending order for this to work.

<!-- Image 2: Exact Versus Approximate Match. See Images/Lookup & Reference/VLOOKUP.md -->

### Example 4: Column Chosen by Header Name

With `E102` in `F2` and `Department` in `F3`:

```excel
=VLOOKUP(F2, $A$2:$D$6, MATCH(F3, $A$1:$D$1, 0), FALSE)
```

**Result:** `Sales`

`MATCH` finds that `Department` is in position 3, so the outer function returns column 3 for the row of E102. If someone inserts a column, the header still leads to the right position.

### Example 5: Fallback When the Key Is Missing

```excel
=IFERROR(VLOOKUP("E999", $A$2:$D$6, 2, FALSE), "Not Found")
```

**Result:** `Not Found`

No row has the ID E999, so the exact match fails and `IFERROR` returns the text. [IFNA](../Logical/IFNA.md) is a narrower choice because it only catches `#N/A`.

### Example 6: Wildcard Match on the Key

```excel
=VLOOKUP("E10?", $A$2:$D$6, 2, FALSE)
```

**Result:** `Maya Reyes`

The question mark matches any single character, so every ID that starts with E10 and has one more character qualifies. The function returns the first match, E101. Wildcards work only with `FALSE` and text keys.

## Story Problems

### Problem 1: Parcel Shipping Rate

A courier charges a rate that depends on the weight band of the parcel. The band table in `E1:F5` lists the minimum weight of each band in ascending order.

| Minimum Weight (kg) | Rate |
| --- | --- |
| 0 | 4.00 |
| 5 | 6.50 |
| 10 | 9.00 |
| 20 | 14.00 |

**Task:** Find the rate for a parcel weighing 12 kg, which is typed in cell `B2`.

**Solution:**

```excel
=VLOOKUP(B2, $E$2:$F$5, 2, TRUE)
```

**Answer:** `9.00`. The largest minimum weight that does not exceed 12 is 10, and its rate is 9.00.

<!-- Image 3: Shipping Rate Lookup Result. See Images/Lookup & Reference/VLOOKUP.md -->

### Problem 2: Client Behind an Invoice

A small studio keeps invoices in `A1:C5` with the invoice number in column A, the client in column B and the amount in column C.

| Invoice | Client | Amount |
| --- | --- | --- |
| INV-2041 | Birch Studio | 1250 |
| INV-2042 | Cedar Labs | 480 |
| INV-2048 | Acme Retail | 3975 |
| INV-2050 | Dune Foods | 610 |

**Task:** Return the client name for invoice INV-2048.

**Solution:**

```excel
=VLOOKUP("INV-2048", $A$1:$C$5, 2, FALSE)
```

**Answer:** `Acme Retail`. The exact match finds the row for INV-2048, and column 2 holds the client.

## Use Cases

### Employee Records Lookup

**Scenario:** A timesheet lists employee IDs. The payroll sheet needs the name and hourly rate for each row.

```excel
=VLOOKUP($A2, Employees!$A:$F, 2, FALSE)
```

**Why It Works:** The `$A2` reference keeps the key column fixed while the formula is copied across. Full-column references keep the range current as the master list grows. Each extra field needs its own formula with a different column number.

### Grade Band Lookup

**Scenario:** A training team converts numeric assessment scores to bands such as Developing, Proficient and Advanced.

```excel
=VLOOKUP(B2, GradeBands, 2, TRUE)
```

**Why It Works:** `GradeBands` is a named range whose first column holds the minimum score for each band, sorted in ascending order. The approximate match returns the band that a score falls into, so a score of 85 does not need its own row in the table.

### Price List Integration

**Scenario:** Sales orders contain product codes. The quoting sheet needs the current unit price for each code.

```excel
=VLOOKUP(B2, PriceList!$A:$D, MATCH("Unit Price", PriceList!$1:$1, 0), FALSE)
```

**Why It Works:** `MATCH` finds the price column by its header, so inserting a column in the price list does not break the quote. The product code must be in the leftmost column of the price list.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The key is not in the first column, or an exact match finds no row. | Check spelling and spaces, and use `TRIM` on text keys. |
| `#N/A` | An approximate lookup value is smaller than the smallest key. | Add a lower band or start the table at 0. |
| `#REF!` | `col_index_num` is larger than the number of columns in `table_array`. | Widen the range or lower the column number. |
| `#VALUE!` | `col_index_num` is less than 1. | Use a column number of 1 or higher. |
| `#NAME?` | A text key is typed without quotation marks. | Wrap literal text in double quotes. |
| Wrong value | `TRUE` or a missing `range_lookup` returns the nearest smaller key. | Pass `FALSE` for exact matches. |
| Wrong value | The first column is not sorted when approximate matching is used. | Sort the key column in ascending order, or use exact matching. |
| Wrong value | Numbers or dates are stored as text. | Convert the key or the table column so both use the same type. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions. | Arguments are named `lookup_value`, `table_array`, `col_index_num` and `range_lookup`. Wildcards work only with `FALSE` and text keys. |
| Google Sheets | Available. | Arguments are named `search_key`, `range`, `index` and `is_sorted`. The default for `is_sorted` is `TRUE`, the same as Excel's default. |

## Tips and Best Practices

- Pass `FALSE` on every exact lookup so the formula never falls back to an approximate match.
- Anchor the table with dollar signs or a named range so the reference does not shift when the formula is copied.
- Use `MATCH` for the column number when headers may move.
- Clean text keys with `TRIM` when the source data may contain stray spaces.
- Keep the key column leftmost, and when that is not possible, switch to XLOOKUP or INDEX with MATCH.
- Check for duplicate keys before relying on the first match.
- VLOOKUP does not distinguish uppercase from lowercase, so `abc` and `ABC` match the same row. For a case-sensitive match, use `=INDEX(B2:B10, MATCH(TRUE, EXACT(A2:A10, E2), 0))`, where EXACT compares each key with the lookup value in `E2`. In Excel versions without dynamic arrays, confirm it with Ctrl+Shift+Enter; in Google Sheets, wrap the formula in ARRAYFORMULA.

## Related Functions

| Function | Relationship |
| --- | --- |
| [HLOOKUP](HLOOKUP.md) | Performs the same search across the first row instead of the first column. |
| [IFNA](../Logical/IFNA.md) | Supplies a fallback value only when the lookup returns `#N/A`. |
| [INDEX](INDEX.md) | Returns a value from any column, including columns to the left of the key. |
| [MATCH](MATCH.md) | Finds the position of a header or key, often used to set `col_index_num`. |
| [XLOOKUP](XLOOKUP.md) | Modern replacement that can look left, returns a fallback value and needs no column number. |

## Official Documentation

- [Microsoft Support: VLOOKUP function](https://support.microsoft.com/en-us/excel/functions/vlookup-function)
- [Google Docs Editors Help: VLOOKUP](https://support.google.com/docs/answer/3093318)
