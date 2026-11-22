---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Classic Lookup
purpose:
  - Data Retrieval
use-case:
  - Commission Tier Rates
  - Monthly KPI Panel
  - Quarterly Target Check
related:
  - FILTER
  - INDEX
  - LOOKUP
  - MATCH
  - VLOOKUP
  - XLOOKUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/hlookup-function
  - https://support.google.com/docs/answer/3093375
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Horizontal Lookup
  - Row Lookup
tags:
  - excel
  - horizontal-lookup
  - lookup
  - sheets
---

# HLOOKUP

## Description

**HLOOKUP** (horizontal lookup) searches for a value in the first row of a table and returns a value from a row you choose, in the same column. It is the horizontal counterpart of VLOOKUP. Use it when labels run across the top of a table, such as months, quarters or product codes, and the data you need sits in the rows below.

The first row of `table_array` must contain the search values, and the lookup can only return values from rows at or below that first row. To return a value from a row above the header, or to search by a column that is not the first one, use INDEX with MATCH instead.

The fourth argument controls the match type. Set it to FALSE for an exact match, which is the right choice for codes, labels and dates. Leave it TRUE, or omit it, for an approximate match on sorted values such as commission tiers. An approximate match needs the first row sorted in ascending order, and an unsorted row returns wrong results without an error.

HLOOKUP returns the first matching column when a value appears more than once in the header row. Excel also accepts wildcards in exact match mode, while Google Sheets does not support wildcards in HLOOKUP. In Excel 2021 and Microsoft 365, XLOOKUP can search in either direction, but HLOOKUP still works in every version.

## Syntax

```excel
=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])
```

<!-- Image 1: HLOOKUP Argument Layout. See Images/Lookup & Reference/HLOOKUP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `lookup_value` | Yes | The value to find in the first row of `table_array`. It can be a number, text in quotes, or a cell reference. |
| `table_array` | Yes | The range or named range to search. Its first row holds the search values. |
| `row_index_num` | Yes | The row number to return, counting the first row of `table_array` as 1. A value below 1 returns an error. |
| `range_lookup` | No | TRUE or omitted for an approximate match on sorted data. FALSE for an exact match. |

### Return Value

The value in the `row_index_num` row of the column where the match was found. With FALSE, it returns `#N/A` when no exact match exists. With TRUE, it returns `#N/A` when the lookup value is smaller than the first value in the header row. Excel returns `#VALUE!` when `row_index_num` is less than 1 and `#REF!` when it is larger than the number of rows in `table_array`. Google Sheets returns `#VALUE!` for either out-of-range row number.

## Examples

The examples use this quarterly table in `A1:G4`. Row 1 holds the months and rows 2 to 4 hold the metrics.

| Metric | Jan | Feb | Mar | Apr | May | Jun |
| --- | --- | --- | --- | --- | --- | --- |
| Units | 120 | 135 | 150 | 128 | 142 | 160 |
| Returns | 4 | 6 | 3 | 7 | 5 | 2 |
| Price | 25 | 25 | 26 | 26 | 27 | 27 |

### Example 1: Exact Match on a Month

```excel
=HLOOKUP("Mar", A1:G4, 2, FALSE)
```

**Result:** `150`

The function finds `Mar` in row 1, column D, then returns the value in row 2 of that column, which is the March units figure.

### Example 2: Return a Different Metric

```excel
=HLOOKUP("Apr", A1:G4, 3, FALSE)
```

**Result:** `7`

Changing the row index to 3 returns the April value from the Returns row.

### Example 3: Choose the Row With MATCH

```excel
=HLOOKUP("May", A1:G4, MATCH("Price", A1:A4, 0), FALSE)
```

**Result:** `27`

MATCH finds that `Price` sits in row 4, so HLOOKUP returns the May price. If a row is inserted above Price, the formula still finds the right row.

### Example 4: Approximate Match on Sorted Tiers

This table sits in `I1:L2`. Row 1 holds the sales thresholds in ascending order, and row 2 holds the tier names.

| Threshold | 0 | 500 | 1000 | 2500 |
| --- | --- | --- | --- | --- |
| Tier | Basic | Silver | Gold | Platinum |

```excel
=HLOOKUP(750, I1:L2, 2, TRUE)
```

**Result:** `Silver`

The largest threshold that does not exceed 750 is 500, which is in the Silver column. The threshold row must be sorted in ascending order for this match to work.

<!-- Image 3: Exact Versus Approximate Match. See Images/Lookup & Reference/HLOOKUP.md -->

### Example 5: Wildcard Match in Excel

```excel
=HLOOKUP("Ma*", A1:G4, 2, FALSE)
```

**Result:** `150`

In Excel, the wildcard `*` matches any text, and the first header that starts with `Ma` is March. Google Sheets does not support wildcards in HLOOKUP.

### Example 6: Show a Message When the Lookup Fails

```excel
=IFERROR(HLOOKUP("Sep", A1:G4, 2, FALSE), "No data for that month")
```

**Result:** `No data for that month`

The table has no September column, so the exact match fails. IFERROR returns the message instead of `#N/A`.

## Story Problems

### Problem 1: Quarterly Sales Target Check

A regional sales team tracks its target and actual revenue by quarter in `A1:E3`.

| Measure | Q1 | Q2 | Q3 | Q4 |
| --- | --- | --- | --- | --- |
| Target | 5000 | 5500 | 6000 | 6500 |
| Actual | 5200 | 5100 | 6400 | 6300 |

**Task:** Return the actual revenue for Q3.

**Solution:**

```excel
=HLOOKUP("Q3", A1:E3, 2, FALSE)
```

**Answer:** `6400`. The Q3 column holds 6000 as the target and 6400 as the actual, and row 2 holds the actual values.

### Problem 2: Commission Rate by Sales Tier

A sales representative earns a commission rate that depends on monthly sales. The tier thresholds sit in ascending order in `B1:E1`, and the rates sit beneath them in `B2:E2`.

| Threshold | 0 | 1000 | 2000 | 3000 |
| --- | --- | --- | --- | --- |
| Rate | 2% | 4% | 6% | 8% |

**Task:** Find the commission rate for monthly sales of 1240.

**Solution:**

```excel
=HLOOKUP(1240, B1:E2, 2, TRUE)
```

**Answer:** `4%`. Sales of 1240 fall between the 1000 and 2000 thresholds, so the 1000 tier applies.

<!-- Image 2: Commission Tier Lookup. See Images/Lookup & Reference/HLOOKUP.md -->

## Use Cases

### Monthly KPI Panel

**Scenario:** An executive picks a month from a drop-down, and a summary panel shows each metric for that month.

```excel
=HLOOKUP($B$2, Finance!$B$1:$M$20, MATCH("Revenue", Finance!$A$1:$A$20, 0), FALSE)
```

**Why It Works:** `B2` holds the selected month, and MATCH finds the metric's row, so the same formula works for every line of the panel. Absolute references keep the table fixed when the formula is copied.

### Commission Tier Rates

**Scenario:** A sales operations team stores commission tiers across a row and looks up the rate for each rep's monthly total.

```excel
=HLOOKUP(E5, $B$1:$E$2, 2, TRUE)
```

**Why It Works:** The approximate match returns the highest tier that the sales figure reaches. The threshold row must stay in ascending order.

### Quarterly Target Check

**Scenario:** A manager compares actual results with the target for a chosen quarter.

```excel
=HLOOKUP($H$1, Plan!$B$1:$E$3, 3, FALSE)
```

**Why It Works:** `H1` holds the quarter, and row 3 holds the actual results. Changing `H1` updates the comparison without editing the formula.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The lookup value is not in the first row, or the text and numbers do not match. | Check spelling and data type, and use TRIM on the lookup value. |
| `#REF!` (Excel) | `row_index_num` is larger than the number of rows in `table_array`. | Extend the table range or reduce the row number. |
| `#VALUE!` | `row_index_num` is less than 1. | Use a row number of 1 or more. |
| Wrong value with TRUE | The first row is not sorted in ascending order. | Sort the header row or switch to FALSE for an exact match. |
| Wrong value with duplicates | The header row contains the lookup value more than once. | HLOOKUP returns the leftmost match, so reorganize the headers or use FILTER. |
| `#N/A` for a date | The header holds dates as text rather than date values. | Convert the headers with DATEVALUE or enter them as real dates. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Excel 2019, Excel 2021, Excel 2024, Microsoft 365 and Excel for the web | Wildcards work with FALSE and text lookup values. Returns `#VALUE!` for a row index below 1 and `#REF!` for one that is too large. XLOOKUP is available in Excel 2021 and Microsoft 365 as a newer alternative. |
| Google Sheets | Available | Syntax is `HLOOKUP(search_key, range, index, [is_sorted])`. Returns `#VALUE!` for an index outside the range. Wildcards are not supported, so use QUERY or INDEX with MATCH for pattern matching. |

## Tips and Best Practices

- Use FALSE for identifier lookups and TRUE only for sorted thresholds such as tax brackets or commission tiers.
- Anchor the table with absolute references, such as `$A$1:$Z$20`, or use a named range, so copying the formula does not shift the table.
- Use MATCH for the row number instead of a typed number, so the formula survives inserted rows.
- Wrap the formula in IFERROR when a missing value should show a message or a blank instead of an error.
- Keep the lookup row at the top of the range, because HLOOKUP cannot look above it.
- Store headers as real dates or numbers, not text, so they match the lookup value.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns every matching column or row instead of the first match only. |
| [INDEX](../Lookup%20%26%20Reference/INDEX.md) | Returns a value by row and column position, and can look above the search row. |
| [LOOKUP](../Lookup%20%26%20Reference/LOOKUP.md) | A simpler approximate lookup that works on one sorted vector. |
| [MATCH](../Lookup%20%26%20Reference/MATCH.md) | Returns the position of a value, which HLOOKUP uses for its row index. |
| [VLOOKUP](../Lookup%20%26%20Reference/VLOOKUP.md) | The vertical counterpart, which searches the first column and returns from a column to its right. |
| [XLOOKUP](../Lookup%20%26%20Reference/XLOOKUP.md) | A newer lookup that searches in either direction and returns exact matches by default. |

## Official Documentation

- [Microsoft Support: HLOOKUP function](https://support.microsoft.com/en-us/excel/functions/hlookup-function)
- [Google Docs Editors Help: HLOOKUP](https://support.google.com/docs/answer/3093375)
