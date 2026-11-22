---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Classic Lookup
purpose:
  - Data Retrieval
  - Data Validation
use-case:
  - Discount Tier Lookup
  - Duplicate ID Check
  - Dynamic Column Selection
related:
  - COUNTIF
  - INDEX
  - ISNA
  - LOOKUP
  - VLOOKUP
  - XMATCH
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/match-function
  - https://support.google.com/docs/answer/3093378
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Array Position
  - Find Position
  - Position Lookup
tags:
  - excel
  - index-match
  - lookup
  - position
  - sheets
---

# MATCH

## Description

**MATCH** searches a single row or column for a value and returns the position of that value within the range. It answers "where is this value?" rather than "what is the value?" If "Drew" is the fourth name in a list, MATCH returns 4. The position is then passed to INDEX, or to a function such as OFFSET, to return the data that sits beside it.

MATCH has three match types. The match type is the third argument and controls how the search works. Type `0` finds an exact match. Type `1`, the default when the argument is left out, finds the largest value that is less than or equal to the lookup value and requires the data to be sorted in ascending order. Type `-1` finds the smallest value that is greater than or equal to the lookup value and requires descending order. Because omitting the argument triggers approximate matching, write `0` explicitly whenever you need an exact match.

MATCH is the first half of the INDEX and MATCH pattern. It finds the row or column, and INDEX returns the value from any column in that row. This pattern can look in either direction, and it does not break when columns are inserted. The search is not case sensitive in either Microsoft Excel or Google Sheets. Microsoft also supports wildcards in exact matches. XMATCH is a newer Microsoft function that adds search modes; see the [XMATCH](XMATCH.md) page for that function.

## Syntax

```excel
=MATCH(lookup_value, lookup_array, [match_type])
```

<!-- Image 1: Match Type Anatomy. See Images/Lookup & Reference/MATCH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `lookup_value` | Yes | The value to find. It can be a number, text, a logical value or a cell reference. |
| `lookup_array` | Yes | The single row or single column to search. A range with more than one row and more than one column is not accepted. |
| `match_type` | No | `1` (or omitted) finds the largest value less than or equal to `lookup_value` and needs ascending data. `0` finds the first exact match and does not need sorted data. `-1` finds the smallest value greater than or equal to `lookup_value` and needs descending data. |

### Return Value

The position of the match within `lookup_array`, counted from 1 at the first cell. It is a position, not the matched value. MATCH returns `#N/A` when no value matches. For exact matches this means no equal value exists. For approximate matches it means `lookup_value` falls outside the range, for example below the smallest value in an ascending list.

## Examples

All examples use this data. Names and scores are in `A1:B7`. A tier table is in `D1:E6`, and a descending list is in `G1:G6`.

| Name | Score | | Sales Threshold | Rate | | Descending Score |
| --- | --- | --- | --- | --- | --- | --- |
| Avery | 72 | | 0 | 5% | | 100 |
| Blake | 88 | | 10000 | 7% | | 90 |
| Casey | 65 | | 25000 | 10% | | 85 |
| Drew | 91 | | 50000 | 12% | | 70 |
| Emery | 78 | | 100000 | 15% | | 60 |
| Finley | 84 | | | | | |

### Example 1: Exact Match for a Name

```excel
=MATCH("Drew", A2:A7, 0)
```

**Result:** `4`

Drew is the fourth name in `A2:A7`. The `0` forces an exact match, so the names must be equal, not just similar.

### Example 2: Exact Match for a Score

```excel
=MATCH(88, B2:B7, 0)
```

**Result:** `2`

The score 88 belongs to Blake, the second row of the range.

### Example 3: Approximate Match for a Sales Tier

```excel
=MATCH(67500, D2:D6, 1)
```

**Result:** `4`

The thresholds in `D2:D6` are in ascending order. The largest threshold not above 67500 is 50000, which is in position 4.

<!-- Image 2: Approximate Match Tier Ladder. See Images/Lookup & Reference/MATCH.md -->

### Example 4: Smallest Value at or Above a Target

```excel
=MATCH(80, G2:G6, -1)
```

**Result:** `3`

The values in `G2:G6` are in descending order. The smallest value that is at least 80 is 85, which is in position 3.

### Example 5: Wildcard Match on Text

```excel
=MATCH("Fi*", A2:A7, 0)
```

**Result:** `6`

The asterisk matches any run of characters, so the search finds Finley. Wildcards work only with exact matches and text lookup values.

### Example 6: Tier Rate Through INDEX

```excel
=INDEX(E2:E6, MATCH(67500, D2:D6, 1))
```

**Result:** `12%`

MATCH returns position 4, and INDEX returns the fourth rate in `E2:E6`. This is the standard way to apply a tiered rate without nested IF functions.

## Story Problems

### Problem 1: Bulk Discount Tier

A supplier offers discounts based on order size. The tier table in `A1:B5` lists the minimum quantity for each tier and its discount.

| Minimum Quantity | Discount |
| --- | --- |
| 1 | 0% |
| 10 | 5% |
| 50 | 10% |
| 100 | 15% |

**Task:** Type an order quantity of 75 in `D2`, then return the discount that applies.

**Solution:**

```excel
=INDEX(B2:B5, MATCH(D2, A2:A5, 1))
```

**Answer:** `10%`. The largest minimum quantity not above 75 is 50, which is in position 3, and that tier's discount is 10%.

<!-- Image 3: Discount Tier Result. See Images/Lookup & Reference/MATCH.md -->

### Problem 2: Locating an Invoice

A billing clerk keeps invoice numbers in `A1:A6`, sorted in no particular order. The list is headed "Invoice" in `A1`.

| Invoice |
| --- |
| INV-1038 |
| INV-1042 |
| INV-1047 |
| INV-1051 |
| INV-1059 |

**Task:** Find the position of INV-1047 within the list of invoices.

**Solution:**

```excel
=MATCH("INV-1047", A2:A6, 0)
```

**Answer:** `3`, because INV-1047 is the third invoice below the header. An exact match is required because the list is not sorted.

## Use Cases

### Dynamic Column Selection

**Scenario:** A report has a drop-down in `G1` that lists the column headers of a data table in `A1:F1`. When a manager chooses a header, the report shows that whole column, without the formula being edited.

```excel
=INDEX($A$2:$F$100, 0, MATCH($G$1, $A$1:$F$1, 0))
```

**Why It Works:** MATCH converts the chosen header into a column position. INDEX with a row of `0` returns the entire column at that position. In Microsoft 365 the result spills into the cells below. Other platforms need the result placed in a function that accepts arrays.

### Duplicate ID Check

**Scenario:** A data entry form checks new customer IDs against a list of existing IDs in `A2:A5000` before the new record is saved.

```excel
=IF(ISNUMBER(MATCH(E2, $A$2:$A$5000, 0)), "ID already exists", "OK to add")
```

**Why It Works:** An exact MATCH returns a number when the ID is found and `#N/A` when it is not. ISNUMBER turns that result into TRUE or FALSE, which the IF function converts into a message. Use the same pattern on a column of existing records to catch duplicates before they are saved.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | An exact match cannot find the value. | Check spelling, extra spaces and data types. Use TRIM on text if the data has stray spaces. |
| `#N/A` | With match type `1`, the lookup value is smaller than every value in the list. | Make sure the list starts with the smallest threshold, or handle the case with IFERROR. |
| `#N/A` | With match type `-1`, the lookup value is larger than every value in the list. | Check the order of the list and the size of the lookup value. |
| `#N/A` | A number is stored as text, or the reverse. | Convert both sides to the same type with VALUE or TEXT. |
| Wrong position | Approximate matching was used on unsorted data. | Sort the list in the order the match type expects, or use match type `0`. |
| Wrong position | The third argument was left out, so match type `1` was used. | Write `0` explicitly for exact matches. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Matches are not case sensitive. Wildcards `*` and `?` work only with match type `0` and text lookup values. Use `~` before a literal asterisk or question mark. |
| Google Sheets | Available | Documents `search_key`, `range` and `search_type`, with `search_type` values `1`, `0` and `-1` that match Excel. A two-dimensional range returns `#N/A`. The documentation does not describe wildcard support, so test it before relying on it. |

## Tips and Best Practices

- Write `0` as the third argument for every exact match, because the default behaves as an approximate match.
- Use approximate matching only on sorted data, such as tier tables, and check the sort order whenever the table changes.
- Keep the lookup range one row or one column wide, and anchor it with `$` signs when the formula is copied.
- Use ISNUMBER with MATCH to test whether a value exists, which is clearer than comparing the result to `#N/A`.
- Store the MATCH result in a helper cell when several INDEX formulas need the same position.
- MATCH does not distinguish uppercase from lowercase text. For a case-sensitive position, use `=MATCH(TRUE, EXACT(A2:A10, E2), 0)`, where EXACT compares each item with the lookup value in `E2`. In Excel versions without dynamic arrays, confirm it with Ctrl+Shift+Enter; in Google Sheets, wrap the formula in ARRAYFORMULA.

## Related Functions

| Function | Relationship |
| --- | --- |
| [INDEX](INDEX.md) | Returns the value at the position that MATCH finds. |
| [XMATCH](XMATCH.md) | A newer position function with search modes and a not-found argument. |
| [VLOOKUP](VLOOKUP.md) | Returns a value from a table in one step, but reads only to the right of the lookup column. |
| [LOOKUP](LOOKUP.md) | An older approximate lookup that depends on sorted data. |
| [COUNTIF](../Statistical/COUNTIF.md) | Counts matching cells instead of returning a position. Use it for simple existence checks that do not need a position. |
| [ISNA](../Information/ISNA.md) | Tests whether a formula returned `#N/A`, which MATCH uses to signal a missing value. |

## Official Documentation

- [Microsoft Support: MATCH function](https://support.microsoft.com/en-us/excel/functions/match-function)
- [Google Docs Editors Help: MATCH](https://support.google.com/docs/answer/3093378)
