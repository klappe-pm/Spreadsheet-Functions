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
- position
- reference
dateCreated: '2025-08-17'
dateRevised: '2026-09-09'
aliases:
- Extended Match
- Modern MATCH
tags:
- lookup
- position
- dynamic-arrays
- match
---

# XMATCH

## Description

**XMATCH** returns the relative position of an item within an array or range. Where XLOOKUP hands you the value sitting at the matched position, XMATCH hands you the position number itself. If "Chicago" is the fourth entry in a list of cities, XMATCH returns `4`. That number is only useful in combination with something else, which is exactly the point: XMATCH is the addressing half of a lookup, designed to be fed into INDEX, OFFSET, CHOOSE, or any formula that needs an index rather than a value.

You use XMATCH when the position is the answer, or when a single lookup key has to drive several different retrievals. Ranking a value inside a sorted band table, finding which column of a wide report a given month occupies, checking whether a value exists in a list at all, and locating the last non-empty row of a growing column are all position problems. In a two-dimensional lookup, computing the row index and the column index separately with two XMATCH calls and passing both to INDEX is still the clearest and fastest pattern available.

XMATCH is the successor to MATCH and improves on it in three concrete ways. It defaults to exact match, whereas MATCH defaults to `1`, an approximate mode that silently returns wrong positions on unsorted data. It offers both an "exact or next larger" mode and an "exact or next smaller" mode, where MATCH only had the smaller variant without re-sorting the data descending. And it supports reverse search, so finding the last occurrence of a value no longer needs the `LOOKUP(2,1/(range=x),...)` trick that generations of spreadsheet users have copied without fully understanding.

XMATCH shipped with XLOOKUP in Excel 365 in 2019, reached Excel 2021, and came to Google Sheets in 2022. Like XLOOKUP it is unavailable in Excel 2019 and earlier, where MATCH remains the compatible choice.

## Syntax

> [!f(x)] XMATCH Syntax
>
> ```
> =XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `lookup_value` | Yes | The value whose position you want. Number, text, date, Boolean, or a reference to one. Text matching is case-insensitive. |
| `lookup_array` | Yes | A single row or single column to search. A two-dimensional range returns `#VALUE!`. |
| `match_mode` | No | `0` (default) exact match; `-1` exact match or next smaller item; `1` exact match or next larger item; `2` wildcard match honoring `*`, `?`, and `~`. |
| `search_mode` | No | `1` (default) first to last; `-1` last to first; `2` binary search ascending; `-2` binary search descending. Binary modes assume the array is sorted and do not check. |

### Return Value

Returns a positive integer giving the position of the match relative to the start of `lookup_array`, counting from 1. Returns `#N/A` when no match is found. Note that the position is relative to the array you passed, not to the worksheet, so `XMATCH(x, A5:A20)` returning `1` means row 5.

## Examples

> [!f(x)] XMATCH Examples

### Example 1: Basic Position Lookup
```
=XMATCH("Chicago", A2:A20)
```
**Result:** `4`

**Explanation:** "Chicago" is the fourth entry in the range starting at A2, so it sits in row 5 of the sheet. Exact match is the default, so no third argument is needed.

---

### Example 2: Two-Dimensional Lookup with INDEX
```
=INDEX(B2:M50, XMATCH(P1, A2:A50), XMATCH(P2, B1:M1))
```
**Result:** The value at the intersection of the named row and named column

**Explanation:** The classic cross-tab lookup. One XMATCH finds the product row, the other finds the month column, and INDEX reads the cell where they meet. This handles inserted rows and columns gracefully because nothing is hard-coded.

---

### Example 3: Existence Check
```
=IF(ISNUMBER(XMATCH(A2, ApprovedList!B:B)), "Approved", "Not on list")
```
**Result:** `"Approved"` or `"Not on list"`

**Explanation:** You do not care where the value is, only whether it is there. XMATCH returns a number on a hit and `#N/A` on a miss, so ISNUMBER converts that into a clean Boolean test.

---

### Example 4: Finding the Last Occurrence
```
=XMATCH(A2, Log!B:B, 0, -1)
```
**Result:** The position of the final matching row rather than the first

**Explanation:** Search mode `-1` scans bottom-up. Combined with INDEX this retrieves the most recent record for a key from an append-only table.

---

### Example 5: Banding a Value into a Tier
```
=XMATCH(B2, {0;1000;5000;25000}, -1)
```
**Result:** `3` for a value of 8,000

**Explanation:** Match mode `-1` returns the position of the largest threshold not exceeding the input, which is the tier index. Feed that into CHOOSE or INDEX to get the tier's label or rate.

---

### Example 6: Locating the Last Filled Row
```
=XMATCH(TRUE, A:A<>"", 0, -1)
```
**Result:** The row number of the last non-empty cell in column A

**Explanation:** `A:A<>""` produces an array of TRUE and FALSE values; searching for TRUE from the bottom gives the last populated row. This is a robust dynamic range boundary that survives blanks in the middle of the data.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#N/A` | The value is genuinely absent, or differs by whitespace, data type, or invisible characters. | Wrap in IFNA for a friendly result, and normalize both sides with `TRIM` and `VALUE` when keys come from exports. |
| `#VALUE!` | `lookup_array` spans multiple rows and multiple columns. | Pass a single row or single column; for a grid, use two XMATCH calls and INDEX. |
| `#NAME?` | Opened in Excel 2019 or earlier where XMATCH does not exist. | Substitute `MATCH(value, array, 0)` for exact matching. |
| Wrong position returned | A binary search mode was used on unsorted data. | Use search mode `1` or `-1`, or sort the array to match the declared mode. |
| Off-by-one row references | The position is relative to the array, not the sheet. | Add the offset of the array's first row, or pass the same range to INDEX so the two stay aligned. |

## Use Cases

### [[Two-Dimensional Report Lookup]]

**Scenario:** A budget grid has products down the side and months across the top, and users pick a product and a month from dropdowns.

**Implementation:**
```
=INDEX($B$2:$M$200, XMATCH($P$1,$A$2:$A$200), XMATCH($P$2,$B$1:$M$1))
```

**Business Application:** Analysts get an interactive cell-level query over the plan without building a pivot table or restructuring the source into a long format.

**Technical Details:** Both XMATCH calls default to exact match, so a mistyped or renamed header surfaces as `#N/A` rather than quietly returning a neighboring month.

---

### [[Dynamic Column Mapping for Imports]]

**Scenario:** A vendor CSV puts the same fields in a different column order every month, breaking any formula that assumes a fixed column index.

**Implementation:**
```
=INDEX(Import!$A:$Z, ROW(), XMATCH("Invoice Total", Import!$A$1:$Z$1))
```

**Business Application:** The mapping layer adapts to each file automatically, eliminating the manual re-pointing step that made monthly close a source of errors.

**Technical Details:** Resolving the column index once in a helper cell and referencing that cell everywhere is faster than recomputing XMATCH in every row of a large sheet.

---

### [[Latest Record Retrieval]]

**Scenario:** A price history table appends a new row each time a price changes; the current price is the last row for that SKU.

**Implementation:**
```
=INDEX(History!$C:$C, XMATCH($A2, History!$B:$B, 0, -1))
```

**Business Application:** Pricing dashboards read current values directly from the immutable history table, so there is no separate "current price" table to fall out of sync.

**Technical Details:** Reverse search depends on insertion order reflecting chronology. If rows can arrive late, sort by effective date or match on the maximum date instead.

## Platform Differences

### Microsoft Excel
- **Availability:** Excel 365, Excel 2021, Excel 2024, Excel for the web.
- **Specific Behavior:** All four search modes are supported. XMATCH accepts array expressions such as `A:A<>""` directly without requiring Ctrl+Shift+Enter.

### Google Sheets
- **Availability:** Added August 2022.
- **Specific Behavior:** Feature parity with Excel. Sheets tolerates whole-column arrays comfortably, though bounded ranges recalculate faster in large documents.

## Tips and Best Practices

1. **Compute the index once, reuse it many times:** When several columns are pulled for the same key, put XMATCH in one helper cell and feed that number to multiple INDEX calls instead of repeating the search.
2. **Pair XMATCH with INDEX rather than OFFSET:** INDEX is non-volatile; OFFSET recalculates on every change anywhere in the workbook and will slow a large model noticeably.
3. **Remember positions are array-relative:** `XMATCH(x, A5:A100)` returning `1` means sheet row 5. Passing the identical range to INDEX keeps the arithmetic implicit and correct.
4. **Use ISNUMBER for existence tests, not IFERROR:** ISNUMBER states the intent clearly and does not swallow unrelated errors that indicate a real problem.
5. **Reach for XLOOKUP when you only want the value:** XMATCH earns its place when the position matters or when one search drives several retrievals; otherwise XLOOKUP is shorter and clearer.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[MATCH]] | Legacy position lookup | When the workbook must open in Excel 2019 or earlier |
| [[XLOOKUP]] | Returns the matched value directly | When you want the value and not the position, which is the more common case |
| [[INDEX]] | Returns the value at a given position | Always, as XMATCH's natural partner |
| [[FILTER]] | Returns all rows meeting a condition | When multiple matches are expected and all of them matter |

### Commonly Used Together

**[[INDEX]]** - Returns the item at a given position in a range

*Combined with XMATCH for flexible lookups in any direction:*
```
=INDEX(C2:C500, XMATCH(A2, B2:B500))
```
The canonical replacement for VLOOKUP when the return column sits left of the key.

---

**[[CHOOSE]]** - Selects one item from a list by index number

*Combined with XMATCH for turning a band position into a label:*
```
=CHOOSE(XMATCH(B2,{0;1000;5000;25000},-1), "Bronze","Silver","Gold","Platinum")
```
XMATCH converts the amount to a tier number and CHOOSE converts the tier number to its name.

---

**[[ISNUMBER]]** - Tests whether a value is a number

*Combined with XMATCH for membership testing:*
```
=IF(ISNUMBER(XMATCH(A2, Blocklist!A:A)), "Blocked", "Allowed")
```
Turns a position-or-error result into a clean two-state decision.

## Official Documentation

- **Microsoft Excel:** [XMATCH function](https://support.microsoft.com/en-us/office/xmatch-function-d966da31-7a6b-4a13-a1c6-5a33ed6a0312)
- **Google Sheets:** [XMATCH](https://support.google.com/docs/answer/12594061)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel 365 | August 2019 | Released alongside XLOOKUP |
| Excel | Excel 2021 | First perpetual release including it |
| Google Sheets | August 2022 | Full match and search mode parity |

---

*Last updated: 2026-09-09*
