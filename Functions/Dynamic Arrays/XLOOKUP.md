---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- dynamic-arrays
subTopics:
- lookup
- reference
- modern-lookup
dateCreated: '2025-08-17'
dateRevised: '2026-09-09'
aliases:
- Extended Lookup
- Modern VLOOKUP
tags:
- lookup
- dynamic-arrays
- vlookup-replacement
- reference
---

# XLOOKUP

## Description

**XLOOKUP** searches a range or array for a value and returns the corresponding item from a second range or array. It is the modern replacement for VLOOKUP, HLOOKUP, and the INDEX/MATCH combination, and it removes nearly every limitation those older functions carried. You give it three things at minimum: what you are looking for, where to look for it, and where to pull the answer from. The lookup range and the return range are separate arguments, so the two do not need to sit next to each other, and the return column can be to the left of the lookup column.

You reach for XLOOKUP whenever you need to join two sets of data by a shared key: pulling a product price from a catalog into an order line, attaching an employee's department to a payroll row, matching a customer ID to a region, or looking up a tax rate by income band. Because the fourth argument lets you specify what to return when nothing matches, you can drop the IFERROR wrapper that VLOOKUP formulas almost always needed. The fifth and sixth arguments give you approximate matching, wildcard matching, and reverse (last-to-first) search order, all without changing the shape of the formula.

The advantages over VLOOKUP are worth spelling out because they explain why XLOOKUP is now the default recommendation. VLOOKUP requires the lookup value to be in the first column of the table and takes a column index number, which silently breaks the moment someone inserts a column. XLOOKUP takes ranges, so inserting a column shifts the reference along with it. VLOOKUP defaults to approximate match, a design decision that has produced an enormous amount of quietly wrong data over the years. XLOOKUP defaults to exact match. VLOOKUP can only search left to right and top to bottom. XLOOKUP can search in either direction, and with a binary search mode it handles very large sorted datasets far faster than a linear scan.

XLOOKUP arrived in Excel 365 in 2019 and later reached Excel 2021 and Excel for the web. Google Sheets added it in 2022. It is not available in Excel 2019 or earlier perpetual releases, so if your workbook has to open on an older installation you still need INDEX/MATCH. A file saved with XLOOKUP and opened in an older Excel shows `_xlfn.XLOOKUP` and a `#NAME?` error rather than the computed value.

## Syntax

> [!f(x)] XLOOKUP Syntax
>
> ```
> =XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `lookup_value` | Yes | The value to search for. Can be a number, text, date, Boolean, cell reference, or expression. Text comparison is case-insensitive in both Excel and Google Sheets. |
| `lookup_array` | Yes | The single row or single column to search in. Must be one-dimensional; a multi-column range produces `#VALUE!`. |
| `return_array` | Yes | The range to return a result from. Must have the same number of rows (for a vertical lookup) or columns (for a horizontal lookup) as `lookup_array`. Can be multiple columns wide, in which case XLOOKUP returns a spilled row of values. |
| `if_not_found` | No | What to return when no match is found. If omitted, XLOOKUP returns `#N/A`. This replaces the common `IFERROR(VLOOKUP(...),"")` wrapper. |
| `match_mode` | No | `0` (default) exact match; `-1` exact match or next smaller item; `1` exact match or next larger item; `2` wildcard match where `*`, `?`, and `~` are treated as wildcards. |
| `search_mode` | No | `1` (default) search first to last; `-1` search last to first; `2` binary search on an ascending-sorted array; `-2` binary search on a descending-sorted array. Binary modes return unpredictable results if the data is not actually sorted. |

### Return Value

Returns the value or values from `return_array` at the position of the match. If `return_array` spans multiple columns (or rows), the result spills into adjacent cells. Returns `#N/A` when no match is found and `if_not_found` was omitted, or `#VALUE!` when the lookup and return arrays are incompatible in size.

## Examples

> [!f(x)] XLOOKUP Examples

### Example 1: Basic Exact Lookup
```
=XLOOKUP("Widget-A", B2:B500, D2:D500)
```
**Result:** `24.99`

**Explanation:** Finds "Widget-A" in the product code column B and returns the matching price from column D. No column index number, no sorting requirement, and exact match is the default. This is the formula that replaces `=VLOOKUP("Widget-A",B2:D500,3,FALSE)`.

---

### Example 2: Supplying a Friendly Not-Found Message
```
=XLOOKUP(A2, Catalog!B:B, Catalog!D:D, "Not in catalog")
```
**Result:** `"Not in catalog"` when A2 has no match

**Explanation:** The fourth argument handles the miss case inline. A downstream SUM over these results still works if you return `0` instead of text, which is often the better choice for numeric columns.

---

### Example 3: Left-Ward Lookup (Impossible in VLOOKUP)
```
=XLOOKUP(F2, D2:D500, A2:A500)
```
**Result:** The value in column A on the row where column D matches F2

**Explanation:** The return range sits to the left of the lookup range. VLOOKUP cannot do this at all; INDEX/MATCH can, but needs two nested functions. XLOOKUP treats direction as irrelevant.

---

### Example 4: Returning an Entire Record
```
=XLOOKUP(A2, Employees!A:A, Employees!B:F)
```
**Result:** Five cells spill horizontally with name, department, hire date, manager, and location

**Explanation:** When `return_array` is more than one column wide, XLOOKUP returns the whole slice as a dynamic array. One formula replaces five separate lookups and stays consistent if the source columns are reordered.

---

### Example 5: Approximate Match for a Tiered Rate Table
```
=XLOOKUP(B2, {0;10000;50000;100000}, {0.1;0.15;0.22;0.28}, , -1)
```
**Result:** `0.22` for an income of 75,000

**Explanation:** Match mode `-1` returns the row for the largest bracket floor that does not exceed the lookup value. This is the commission and tax-band pattern that VLOOKUP's TRUE mode handled, but here approximate behavior is explicit rather than the silent default.

---

### Example 6: Finding the Most Recent Entry with Reverse Search
```
=XLOOKUP(A2, Log!B:B, Log!D:D, "No entries", 0, -1)
```
**Result:** The status from the last matching log row rather than the first

**Explanation:** Search mode `-1` scans from the bottom up. In an append-only log where each ID appears many times, this returns the latest record without sorting or filtering the source.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#N/A` | No match was found and `if_not_found` was omitted. Often caused by trailing spaces, numbers stored as text, or a genuine gap in the source data. | Supply the fourth argument, or clean the key with `TRIM()` / `VALUE()` on both sides before comparing. |
| `#VALUE!` | `lookup_array` and `return_array` have mismatched dimensions, or `lookup_array` is more than one row and one column. | Make both arrays the same length along the search axis, and search a single row or column. |
| `#REF!` | The return array spills into cells that do not exist, typically a multi-column return at the right edge of the sheet. | Move the formula left, or narrow the return range. |
| `#SPILL!` | A multi-cell result is blocked by existing content in the spill range. | Clear the cells below or to the right of the formula. |
| `#NAME?` | The workbook was opened in Excel 2019 or earlier, which does not have XLOOKUP. | Rewrite as `INDEX(return,MATCH(lookup,array,0))` for backward compatibility. |

## Use Cases

### [[Order Line Enrichment]]

**Scenario:** A sales export contains product codes and quantities but no prices or product names, and the catalog lives in a separate sheet whose column order changes between exports.

**Implementation:**
```
=XLOOKUP($A2, Catalog!$A:$A, Catalog!$C:$E, "Unknown SKU")
```

**Business Application:** Finance can calculate revenue per line without waiting for IT to reshape the export, and a reordered catalog does not silently corrupt the numbers the way a hard-coded VLOOKUP column index would.

**Technical Details:** Anchoring the lookup value column with `$A2` lets the formula be dragged across without drifting. Returning `C:E` as a range spills name, price, and category in one pass, keeping the three fields row-aligned by construction.

---

### [[Effective-Dated Rate Lookup]]

**Scenario:** A currency or commission rate table stores one row per effective date, and each transaction needs the rate that was in force on the day it occurred.

**Implementation:**
```
=XLOOKUP(B2, Rates!$A$2:$A$500, Rates!$B$2:$B$500, "No rate on file", -1, 2)
```

**Business Application:** Restatements and audits reproduce historical figures exactly, because the formula reads the same effective-dated table the accounting team maintains rather than a snapshot pasted into the model.

**Technical Details:** Match mode `-1` picks the latest effective date at or before the transaction date. Search mode `2` uses binary search, which requires the date column to be sorted ascending but makes the lookup dramatically faster across tens of thousands of rows.

---

### [[Latest Status from an Append-Only Log]]

**Scenario:** A ticketing system writes one row per status change. A dashboard needs each ticket's current status without pre-aggregating the log.

**Implementation:**
```
=XLOOKUP($A2, Log!$B:$B, Log!$E:$E, "No activity", 0, -1)
```

**Business Application:** Support leads get a live current-state view straight off the raw event feed, avoiding a nightly rollup job that would otherwise need building and maintaining.

**Technical Details:** Reverse search mode assumes the log is in chronological insertion order. If rows can be inserted out of order, sort by timestamp first or the "latest" result will be whichever matching row happens to sit lowest.

## Platform Differences

### Microsoft Excel
- **Availability:** Excel 365, Excel 2021, Excel 2024, Excel for the web. Not available in Excel 2019 or earlier.
- **Specific Behavior:** Supports all four search modes including both binary variants. Multi-column return arrays spill natively. Files containing XLOOKUP open in older Excel versions as `_xlfn.XLOOKUP` with `#NAME?`.

### Google Sheets
- **Availability:** Added August 2022, all accounts.
- **Specific Behavior:** Behaves the same as Excel including wildcard and binary search modes. Sheets is generally more forgiving about whole-column references such as `B:B` in the lookup array, though limiting the range still improves recalculation time on large files.

## Tips and Best Practices

1. **Always supply `if_not_found`:** It documents the intended behavior at the point of use and removes the need for an IFERROR wrapper, which would also mask genuine `#VALUE!` and `#REF!` problems you actually want to see.
2. **Prefer table or named ranges over whole columns:** `B:B` is convenient but forces the engine to consider a million rows on every recalculation. Structured references such as `Catalog[SKU]` grow automatically and stay fast.
3. **Use binary search only on genuinely sorted data:** Modes `2` and `-2` do not verify the sort. On unsorted data they return a wrong answer silently rather than an error, which is far worse than being slow.
4. **Return a range, not a single cell, when you need several fields:** One spilled XLOOKUP is cheaper to compute and easier to audit than five parallel lookups on the same key.
5. **Normalize keys before comparing:** Most `#N/A` results are data problems, not formula problems. Trailing spaces and numbers stored as text are the usual culprits; `TRIM` and `VALUE` on both sides resolve the majority of them.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[VLOOKUP]] | Vertical lookup using a column index number | When the file must open in Excel 2019 or earlier, or when maintaining an existing model whose conventions you should not break |
| [[INDEX]] | Returns a value at a given row and column position | With MATCH, when you need backward compatibility or a two-dimensional lookup by both row and column key |
| [[MATCH]] | Returns the position of a value in a range | When you need the position itself rather than the associated value, for example to feed OFFSET |
| [[XMATCH]] | Modern position lookup with the same match and search modes | When you want XLOOKUP's flexible matching but need the index number rather than the value |
| [[FILTER]] | Returns every row meeting a condition | When a key can legitimately match many rows and you want all of them, not just one |

### Commonly Used Together

**[[IFERROR]]** - Catches errors and substitutes a fallback value

*Combined with XLOOKUP for defensive nesting of chained lookups:*
```
=IFERROR(XLOOKUP(A2,B:B,C:C), XLOOKUP(A2,E:E,F:F,"Not found anywhere"))
```
Tries the primary table first and falls back to a secondary table, which is useful when a key may live in either of two sources.

---

**[[SUM]]** - Adds numeric values

*Combined with XLOOKUP for totaling a returned record:*
```
=SUM(XLOOKUP(A2, Budget!A:A, Budget!C:N, 0))
```
XLOOKUP returns twelve monthly columns for the matched row and SUM collapses them into an annual total in a single formula.

---

**[[FILTER]]** - Returns rows matching a condition

*Combined with XLOOKUP for two-stage narrowing:*
```
=FILTER(A2:D100, C2:C100 = XLOOKUP(F1, Regions!A:A, Regions!B:B))
```
Resolves a region code to its canonical name, then filters the detail table by that name, keeping the mapping in one maintained place.

## Official Documentation

- **Microsoft Excel:** [XLOOKUP function](https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929)
- **Google Sheets:** [XLOOKUP](https://support.google.com/docs/answer/12061245)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel 365 | August 2019 | Rolled out to Insiders first, then general availability |
| Excel | Excel 2021 | First perpetual release to include it |
| Google Sheets | August 2022 | Shipped alongside XMATCH with full match and search mode parity |

---

*Last updated: 2026-09-09*
