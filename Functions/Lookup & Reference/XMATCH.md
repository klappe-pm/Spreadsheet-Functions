---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Modern Lookup
purpose:
  - Data Retrieval
use-case:
  - Last Status Check
  - Row Locator for Dynamic Ranges
related:
  - FILTER
  - INDEX
  - MATCH
  - VLOOKUP
  - XLOOKUP
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/xmatch-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Modern Match
  - Position Lookup
tags:
  - dynamic-array
  - excel
  - lookup
  - position
  - wildcard-match
---

# XMATCH

## Description

**XMATCH** returns the relative position of an item in a range or array. It answers the question "where is this value?" rather than "what is in the row for this value?". Its result is usually passed to [INDEX](INDEX.md) or to another formula that needs a position.

XMATCH is the newer version of [MATCH](MATCH.md). It adds the match modes and search modes that MATCH lacks, including a search from the last item to the first. That option returns the last occurrence of a repeated value, which MATCH cannot find directly. Like MATCH, it counts positions from 1 at the first item of the lookup range, not from the top of the sheet.

Use XMATCH when you need a position for a row number, when the value you need is the most recent entry in a log, or when you want the nearest smaller or larger value. For a complete lookup that returns a value from another column, [XLOOKUP](XLOOKUP.md) is usually the simpler choice.

XMATCH is available in Excel for Microsoft 365, Excel 2024 and Excel 2021. It is not available in Excel 2016 or Excel 2019. Google Sheets does not provide this function, so use [MATCH](MATCH.md) there instead.

## Syntax

```excel
=XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])
```

<!-- Image 1: XMATCH Syntax Anatomy. See Images/Lookup & Reference/XMATCH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `lookup_value` | Yes | The value to find in `lookup_array`. |
| `lookup_array` | Yes | The one-dimensional range or array to search. |
| `match_mode` | No | `0` for an exact match (the default). `-1` for an exact match or the next smaller item. `1` for an exact match or the next larger item. `2` for a wildcard match in which `*`, `?` and `~` have special meaning. |
| `search_mode` | No | `1` searches from first to last (the default). `-1` searches from last to first. `2` runs a binary search on data sorted in ascending order. `-2` runs a binary search on data sorted in descending order. |

### Return Value

The position of the match within `lookup_array`, counted from 1 at the first item. A position of 1 means the first item. The function returns `#N/A` when no match exists and the match mode does not allow a nearest value.

## Examples

All examples use this product list in `A1:D6`. The examples refer to the codes in `A2:A6` and the prices in `C2:C6`.

| Product Code | Product | Unit Price | Stock |
| --- | --- | --- | --- |
| P-100 | Desk Lamp | 34 | 12 |
| P-200 | Office Chair | 189 | 4 |
| P-300 | Filing Cabinet | 145 | 0 |
| P-400 | Whiteboard | 62 | 9 |
| P-500 | Paper Ream | 8 | 120 |

### Example 1: Position of an Exact Match

```excel
=XMATCH("P-300", A2:A6)
```

**Result:** `3`

P-300 is the third item in the code column, so the function returns 3.

### Example 2: Missing Value With a Fallback

```excel
=IFERROR(XMATCH("P-999", A2:A6), "Not listed")
```

**Result:** `Not listed`

No code matches P-999, so XMATCH returns `#N/A`, and `IFERROR` converts it to the text.

### Example 3: Last Occurrence of a Repeated Value

With the statuses `Ready`, `Busy`, `Ready`, `Idle` and `Ready` in `F2:F6`:

```excel
=XMATCH("Ready", F2:F6, 0, -1)
```

**Result:** `5`

Ready appears in positions 1, 3 and 5. Searching from the last item to the first finds position 5 first, which is the most recent entry.

### Example 4: Nearest Smaller Price

```excel
=XMATCH(100, C2:C6, -1)
```

**Result:** `4`

No price equals 100, so the function uses the next smaller price, 62, which is the fourth item in the price column.

### Example 5: Wildcard Position

```excel
=XMATCH("*Chair*", B2:B6, 2)
```

**Result:** `2`

The asterisk matches any text around `Chair`, so Office Chair is found in the second item of the product column.

<!-- Image 2: Position Versus Value Returned. See Images/Lookup & Reference/XMATCH.md -->

## Story Problems

### Problem 1: Last Late Shipment

A logistics clerk records each shipment as `On time` or `Late` in `B2:B9`, in the order the shipments left the warehouse. The manager wants the position of the most recent late shipment.

| Shipment | Status |
| --- | --- |
| 1 | On time |
| 2 | Late |
| 3 | On time |
| 4 | Late |
| 5 | On time |
| 6 | On time |
| 7 | Late |
| 8 | On time |

**Task:** Find the position of the last `Late` status, searching from the bottom of the list.

**Solution:**

```excel
=XMATCH("Late", B2:B9, 0, -1)
```

**Answer:** `7`. Late appears at shipments 2, 4 and 7, and the search from the bottom stops at 7.

<!-- Image 3: Last Match Search Direction. See Images/Lookup & Reference/XMATCH.md -->

### Problem 2: Threshold Band for a Reading

A lab uses the thresholds 10, 25, 50 and 100 in `A2:A5`, sorted in ascending order. A reading of 60 falls between two thresholds, and the lab wants the position of the threshold that sits just below it.

**Task:** Find the position of the threshold that applies to a reading of 60.

**Solution:**

```excel
=XMATCH(60, A2:A5, -1)
```

**Answer:** `3`. The next smaller threshold to 60 is 50, which is the third item in the list.

## Use Cases

### Last Status Check

**Scenario:** A maintenance log records a status for each machine check. A supervisor wants the row number of the most recent failed check.

```excel
=XMATCH("Failed", Log!B:B, 0, -1)
```

**Why It Works:** Searching from the bottom returns the newest failure. The position can be passed to INDEX to show the date and machine name in the same row.

### Row Locator for Dynamic Ranges

**Scenario:** A sales report needs the amount for an invoice number, and the list grows every week.

```excel
=INDEX(Sales!C:C, XMATCH(A2, Sales!A:A))
```

**Why It Works:** XMATCH returns the row number of the invoice in the whole column, and INDEX uses that number to return the amount from the same row. The formula keeps working as rows are added.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The value is not in the lookup array and no match mode allows a nearest value. | Check the spelling and spaces, or wrap the formula in `IFERROR`. |
| `#NAME?` | The workbook is opened in Excel 2016 or Excel 2019. | Use MATCH, which works in every version. |
| Wrong result | The lookup value contains `*` or `?` but `match_mode` is 0. | Set `match_mode` to 2 to treat the characters as wildcards. |
| Wrong result | Binary search is used on unsorted data. | Sort the array, or use search mode 1 or -1. |
| Confusion | The position is used as a value. | Pass the position to INDEX to return the value from another column. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel 2024 and Excel 2021. | Arguments are named `lookup_value`, `lookup_array`, `match_mode` and `search_mode`. Not available in Excel 2016 or Excel 2019. |
| Google Sheets | Not available. | Use MATCH for an exact position. Use XLOOKUP when the result must come from a different column. |

## Tips and Best Practices

- Use `search_mode` -1 to find the last occurrence of a repeated value.
- Keep `lookup_array` to one row or one column so the position is easy to interpret.
- Pass the result to INDEX when you need the value, not the position.
- Wrap the formula in `IFERROR` when a missing value is an expected outcome.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTER](FILTER.md) | Returns every matching row rather than one position. |
| [INDEX](INDEX.md) | Returns the value at the position that XMATCH finds. |
| [MATCH](MATCH.md) | The older position function, which lacks search from the bottom. |
| [VLOOKUP](VLOOKUP.md) | Returns a value from a column by a key, without returning a position. |
| [XLOOKUP](XLOOKUP.md) | Returns the value directly and can take a fallback argument. |

## Official Documentation

- [Microsoft Support: XMATCH function](https://support.microsoft.com/en-us/excel/functions/xmatch-function)
