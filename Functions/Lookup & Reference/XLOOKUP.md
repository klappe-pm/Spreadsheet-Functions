---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Modern Lookup
purpose:
  - Data Retrieval
use-case:
  - Left Side Lookup
  - Price Lookup With Default
  - Volume Discount Tiers
related:
  - FILTER
  - INDEX
  - MATCH
  - VLOOKUP
  - XMATCH
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/xlookup-function
  - https://support.google.com/docs/answer/12405947
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Lookup Left
  - Modern Lookup
tags:
  - dynamic-array
  - excel
  - lookup
  - sheets
  - wildcard-match
---

# XLOOKUP

## Description

**XLOOKUP** searches for a value in one range and returns the matching item from another range of the same size. It covers the cases of [VLOOKUP](VLOOKUP.md) and of [INDEX](INDEX.md) with [MATCH](MATCH.md). The lookup range can be a column or a row, the return range can be on either side of it, and the function needs no column number.

The function is built for the common cases that older lookups handled poorly. Its fourth argument supplies text to show when nothing matches, so [IFERROR](../Logical/IFERROR.md) is not needed. Its match mode can require an exact match, an exact or nearest smaller or larger value, or a wildcard pattern. Its search mode can search from the bottom up, and it can run a faster binary search on sorted data.

When the return range covers several columns or rows, XLOOKUP returns the entire matching row or column, which can spill into the cells around the formula. It returns the first match it finds, so use search mode -1 when the last match is the one you need.

XLOOKUP is available in Excel for Microsoft 365, Excel 2024 and Excel 2021. It is not available in Excel 2016 or Excel 2019. Google Sheets supports it under the same name, with slightly different argument names.

## Syntax

```excel
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```

<!-- Image 1: XLOOKUP Syntax Anatomy. See Images/Lookup & Reference/XLOOKUP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `lookup_value` | Yes | The value to find. If it is left blank, XLOOKUP returns the blank cells found in `lookup_array`. |
| `lookup_array` | Yes | The range or array to search. It can be a single column or a single row. |
| `return_array` | Yes | The range or array that holds the results. It should be the same size as `lookup_array`. |
| `if_not_found` | No | The text or value to return when no match is found. When omitted, the result is `#N/A`. |
| `match_mode` | No | `0` for an exact match (the default). `-1` for an exact match or the next smaller item. `1` for an exact match or the next larger item. `2` for a wildcard match in which `*`, `?` and `~` have special meaning. |
| `search_mode` | No | `1` searches from first to last (the default). `-1` searches from last to first. `2` runs a binary search on data sorted in ascending order. `-2` runs a binary search on data sorted in descending order. |

### Return Value

The item in `return_array` that lines up with the first match in `lookup_array`. If `return_array` spans several columns or rows, the whole matching row or column is returned. When no match exists, the function returns `if_not_found` if it was supplied, the nearest value when `match_mode` is -1 or 1, or `#N/A`.

## Examples

All examples use this product list in `A1:D6`.

| Product Code | Product | Unit Price | Stock |
| --- | --- | --- | --- |
| P-100 | Desk Lamp | 34 | 12 |
| P-200 | Office Chair | 189 | 4 |
| P-300 | Filing Cabinet | 145 | 0 |
| P-400 | Whiteboard | 62 | 9 |
| P-500 | Paper Ream | 8 | 120 |

### Example 1: Basic Exact Match

```excel
=XLOOKUP("P-300", A2:A6, C2:C6)
```

**Result:** `145`

The search finds P-300 in the code column and returns the price from the same position in the price column. No column number is needed.

### Example 2: Looking Left

```excel
=XLOOKUP("Office Chair", B2:B6, A2:A6)
```

**Result:** `P-200`

The lookup column is to the right of the result column. [VLOOKUP](VLOOKUP.md) cannot do this, but XLOOKUP reads either direction.

### Example 3: Custom Text When Nothing Matches

```excel
=XLOOKUP("P-999", A2:A6, C2:C6, "Not listed")
```

**Result:** `Not listed`

The code P-999 does not exist, so the fourth argument supplies the text. The formula stays clean without a wrapping `IFERROR`.

### Example 4: Returning a Whole Row

```excel
=XLOOKUP("P-400", A2:A6, B2:D6)
```

**Result:** `Whiteboard`, `62` and `9` across three cells

When `return_array` spans several columns, the matching row spills across them. The product name, price and stock for P-400 appear in one step.

### Example 5: Nearest Smaller Price

```excel
=XLOOKUP(100, C2:C6, A2:A6, "None", -1)
```

**Result:** `P-400`

No price equals 100, so the function uses the next smaller price, which is 62 for the Whiteboard. Match mode -1 is what makes that choice possible.

### Example 6: Wildcard Search

```excel
=XLOOKUP("*Lamp*", B2:B6, A2:A6, "No match", 2)
```

**Result:** `P-100`

Match mode 2 turns on wildcards. The asterisk matches any text before and after `Lamp`, so the Desk Lamp row is found.

<!-- Image 2: Match Modes Compared. See Images/Lookup & Reference/XLOOKUP.md -->

## Story Problems

### Problem 1: Stock Value for Two Products

A store keeps the product list above in `A1:D6`. The owner wants the stock value of the chair, which is the unit price multiplied by the units in stock.

**Task:** Multiply the unit price of P-200 by its stock, using XLOOKUP for both values.

**Solution:**

```excel
=XLOOKUP("P-200", A2:A6, C2:C6) * XLOOKUP("P-200", A2:A6, D2:D6)
```

**Answer:** `756`, because 189 multiplied by 4 is 756.

### Problem 2: Discount Tier for an Order

A wholesaler gives discounts by order quantity. The tiers in `F2:G5` start at 1, 10, 50 and 100 units, and each tier has its own discount rate.

| Minimum Units | Discount |
| --- | --- |
| 1 | 0% |
| 10 | 5% |
| 50 | 10% |
| 100 | 15% |

**Task:** Find the discount for an order of 68 units. The order does not match any tier exactly, so the tier below it applies.

**Solution:**

```excel
=XLOOKUP(68, F2:F5, G2:G5, 0, -1)
```

**Answer:** `10%`. The largest tier at or below 68 units is 50, and its discount is 10%.

<!-- Image 3: Discount Tier Lookup Result. See Images/Lookup & Reference/XLOOKUP.md -->

## Use Cases

### Left Side Lookup

**Scenario:** A payroll sheet has employee names in column B and IDs in column A. A time sheet has names but needs the IDs.

```excel
=XLOOKUP(B2, Employees!B:B, Employees!A:A, "Unknown")
```

**Why It Works:** The ID column sits to the left of the names, so VLOOKUP cannot be used directly. XLOOKUP reads the names in one column and returns the ID from the other, and `Unknown` flags any name that is missing from the master list.

### Price Lookup With Default

**Scenario:** A quote tool pulls prices from a master list, but some new products do not have a price yet.

```excel
=XLOOKUP(A2, Prices!A:A, Prices!C:C, "Price missing")
```

**Why It Works:** The fourth argument marks missing prices in place, so the quote can show a clear note instead of an error.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | No match exists and `if_not_found` was not supplied. | Add an `if_not_found` value, or check the spelling and spaces in the lookup value. |
| `#NAME?` | The workbook is opened in Excel 2016 or Excel 2019, where XLOOKUP does not exist. | Use INDEX with MATCH, or open the file in a supported version. |
| Wrong result | A wildcard character is used without `match_mode` 2. | Set `match_mode` to 2 when the lookup value contains `*` or `?`. |
| Wrong result | Binary search (`search_mode` 2 or -2) is used on unsorted data. | Sort the lookup range, or use search mode 1. |
| Wrong result | Only the first match is returned. | Use `search_mode` -1 to search from the bottom when the last match is needed. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel 2024 and Excel 2021. | Arguments are named `lookup_value`, `lookup_array`, `return_array`, `if_not_found`, `match_mode` and `search_mode`. Not available in Excel 2016 or Excel 2019. |
| Google Sheets | Available. | Arguments are named `search_key`, `lookup_range`, `result_range`, `missing_value`, `match_mode` and `search_mode`. The lookup range must be a single row or column. The match modes 0, 1, -1 and 2 have the same meanings. |

## Tips and Best Practices

- Use `if_not_found` for every user-facing lookup so readers see a clear message instead of `#N/A`.
- Pass explicit arguments in order rather than relying on defaults when sharing a workbook.
- Use absolute references such as `$A$2:$A$500` when copying the formula down a column.
- Prefer full-column references only for tables that grow, because they slow large workbooks.
- Use [FILTER](FILTER.md) when you need every match instead of the first one.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTER](FILTER.md) | Returns every matching row, not only the first match. |
| [INDEX](INDEX.md) | Returns a value at a given position, which XLOOKUP does internally. |
| [MATCH](MATCH.md) | Finds a position in a range, the older building block for INDEX lookups. |
| [VLOOKUP](VLOOKUP.md) | The older vertical lookup that XLOOKUP replaces in most cases. |
| [XMATCH](XMATCH.md) | Returns the position of a match instead of the value at that position. |

## Official Documentation

- [Microsoft Support: XLOOKUP function](https://support.microsoft.com/en-us/excel/functions/xlookup-function)
- [Google Docs Editors Help: XLOOKUP](https://support.google.com/docs/answer/12405947)
