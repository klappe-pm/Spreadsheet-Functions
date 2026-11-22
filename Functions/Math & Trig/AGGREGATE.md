---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Aggregation
  - Error Handling
use-case:
  - Error Tolerant Totals
  - Filtered Sales Totals
  - Percentile Benchmarks
related:
  - FILTER
  - IFERROR
  - LARGE
  - MEDIAN
  - PERCENTILE.INC
  - SUBTOTAL
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/aggregate-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Aggregate With Options
  - Ignore Hidden Rows
tags:
  - aggregation
  - error-handling
  - excel
  - hidden-rows
---

# AGGREGATE

## Description

**AGGREGATE** applies one of 19 summary functions, such as SUM, AVERAGE, MEDIAN or a percentile, and lets you choose which values to skip. You can skip hidden rows, error values, nested SUBTOTAL and AGGREGATE results, or any combination. A plain `SUM` returns an error when a range contains one and counts hidden rows, so AGGREGATE is the function to reach for when a range contains errors or when users filter a list.

The function has two forms. The reference form accepts one or more ranges, for example `AGGREGATE(9, 6, A2:A20, C2:C20)`, and works with function numbers 1 to 13. The array form accepts one array or range and an optional `k` value. Function numbers 14 to 19 (LARGE, SMALL, and the percentile and quartile functions) use the array form.

AGGREGATE is available in Microsoft Excel only. Google Sheets does not offer it, so workbooks that use it need a different approach there. The Microsoft page also notes that hidden columns in a horizontal range do not change a sum, so AGGREGATE is designed for vertical ranges.

## Syntax

```excel
=AGGREGATE(function_num, options, ref1, [ref2], ...)
=AGGREGATE(function_num, options, array, [k])
```

<!-- Image 1: Function Number and Options Map. See Images/Math & Trig/AGGREGATE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `function_num` | Yes | A number from 1 to 19 that selects the summary function. 1 is AVERAGE, 2 is COUNT, 3 is COUNTA, 4 is MAX, 5 is MIN, 6 is PRODUCT, 7 is STDEV.S, 8 is STDEV.P, 9 is SUM, 10 is VAR.S, 11 is VAR.P, 12 is MEDIAN, 13 is MODE.SNGL, 14 is LARGE, 15 is SMALL, 16 is PERCENTILE.INC, 17 is QUARTILE.INC, 18 is PERCENTILE.EXC and 19 is QUARTILE.EXC. |
| `options` | Yes | A number from 0 to 7 that sets what is ignored. 0 or omitted ignores nested SUBTOTAL and AGGREGATE. 1 adds hidden rows. 2 adds error values. 3 adds both hidden rows and errors. 4 ignores nothing. 5 ignores hidden rows. 6 ignores error values. 7 ignores hidden rows and error values. Each option also ignores nested SUBTOTAL and AGGREGATE except 4 to 7, which do not. |
| `ref1` | Yes (reference form) | The first range or reference to aggregate. |
| `ref2` | No (reference form) | Additional ranges or references. Up to 253 arguments can be supplied in total. |
| `array` | Yes (array form) | A single range, array or array formula to aggregate. |
| `k` | Depends on function | The position or percentile required by LARGE, SMALL, PERCENTILE and QUARTILE functions. Omitting it for those functions returns `#VALUE!`. |

### Return Value

The summary value calculated over the values that remain after the options are applied. Errors that are not ignored are returned. A 3-D reference returns `#VALUE!`.

## Examples

These examples use the sales list in `B2:B7`. Cell `B4` contains an error (`#DIV/0!`). The values are 40, 55, error, 70, 25 and 90.

### Example 1: Sum While Skipping Errors

```excel
=AGGREGATE(9,6,B2:B7)
```

**Result:** `280`

Option 6 ignores the error in `B4`. A plain `SUM` would return the error instead.

### Example 2: Median Ignoring Errors

```excel
=AGGREGATE(12,6,B2:B7)
```

**Result:** `55`

The median of the five valid values, 25, 40, 55, 70 and 90, is 55.

### Example 3: Largest Value

```excel
=AGGREGATE(14,6,B2:B7,1)
```

**Result:** `90`

Function 14 is LARGE, and the final argument `1` asks for the first largest value. The array form is required because LARGE takes a `k` value.

### Example 4: Percentile Interpolation

```excel
=AGGREGATE(16,6,B2:B7,0.9)
```

**Result:** `82`

PERCENTILE.INC with `k` of 0.9 interpolates between 70 and 90 across the five valid values.

### Example 5: Sum Without Hidden Rows

Values are 10, 20 and 30 in `D2:D4`, and row 3 is hidden.

```excel
=AGGREGATE(9,5,D2:D4)
```

**Result:** `40`

Option 5 skips the hidden row, so the visible values 10 and 30 are added. A plain `SUM` returns 60.

## Story Problems

### Problem 1: Store Sales With a Hidden Closed Store

A regional report lists sales by store. One lookup failed, and a closed store has been hidden with a row filter.

| Store | Sales |
| --- | --- |
| North | 500 |
| East | 320 |
| South | #N/A |
| Closed Store (hidden) | 150 |
| West | 410 |

**Task:** Total the visible sales and skip the lookup error.

**Solution:**

```excel
=AGGREGATE(9,7,B2:B6)
```

**Answer:** `1230`, because 500 + 320 + 410 = 1230. Option 7 skips both the hidden row and the `#N/A` error, which a plain `SUM` could not do.

<!-- Image 2: Filtered Store Table. See Images/Math & Trig/AGGREGATE.md -->

### Problem 2: Response Time Percentile

A support team logged response times in seconds for seven requests. One record is missing its timestamp and shows an error.

| Request | Seconds |
| --- | --- |
| R-1 | 2.1 |
| R-2 | 3.4 |
| R-3 | 1.8 |
| R-4 | 5.0 |
| R-5 | #N/A |
| R-6 | 2.9 |
| R-7 | 4.2 |

**Task:** Find the 75th percentile of the response times, skipping the error.

**Solution:**

```excel
=AGGREGATE(16,6,B2:B8,0.75)
```

**Answer:** `4`. Six valid values remain, and the 75th percentile falls at 4.0 seconds using inclusive interpolation between 3.4 and 4.2.

## Use Cases

### Error Tolerant Totals

**Scenario:** A monthly ledger pulls values from another workbook, and some lookups return errors that should not stop the total.

```excel
=AGGREGATE(9,6,LedgerAmounts)
```

**Why It Works:** Option 6 skips the error values, so the total reflects every valid amount. Review the skipped errors separately with `COUNTIF` or a filter.

### Filtered Sales Totals

**Scenario:** A sales manager filters a list by region, and the total on the report should reflect only the visible rows.

```excel
=AGGREGATE(9,5,SalesColumn)
```

**Why It Works:** Option 5 skips rows hidden by the filter, so the total changes when the filter changes.

### Percentile Benchmarks

**Scenario:** A support lead wants the 90th percentile of handling times for the current view of a service log, excluding failed records.

```excel
=AGGREGATE(16,7,HandlingTimes,0.9)
```

**Why It Works:** Option 7 skips both hidden rows and errors before the percentile is calculated.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `k` is missing for LARGE, SMALL or a percentile or quartile function. | Supply `k`, or use the array form with the required argument. |
| Error appears in the result | Option 0, 1, 4 or 5 is used and the range contains errors. | Use option 2, 3, 6 or 7 to skip errors. |
| Total includes hidden rows | Option 0, 2, 4 or 6 is used. | Use option 1, 3, 5 or 7 to skip hidden rows. |
| Hidden rows still counted | The range is an array calculation such as `A1:A100*(A1:A100>0)`. | Use a plain range in AGGREGATE and move the condition into a helper column. |
| `#NAME?` | The function is used in Google Sheets, which does not support it. | Use SUBTOTAL with FILTER and IFERROR in Google Sheets. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Supports 19 functions, the reference and array forms, and options 0 to 7. Ignores hidden rows and errors as set by the options. |
| Google Sheets | Not available | Use SUBTOTAL for hidden-row totals and FILTER with IFERROR to remove error values. |

## Tips and Best Practices

- Use option 6 for totals over imported data that may contain errors, and check the error count separately so problems are not hidden.
- Use option 5 or 7 when users filter a list, so totals follow the visible rows.
- Use the array form for LARGE, SMALL and percentile or quartile results, because those functions need `k`.
- Keep the ranges vertical. The Microsoft page notes that hidden columns in a horizontal range do not change a sum.
- Do not rely on option 1, 3, 5 or 7 to skip hidden rows inside a calculated array. Put the calculation in a helper column first.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SUBTOTAL](SUBTOTAL.md) | Hidden-row-aware totals with fewer options. Use it when only filtering matters. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns matching rows, which can be aggregated in Google Sheets. |
| [IFERROR](../Logical/IFERROR.md) | Replaces errors with another value before a calculation. |
| [LARGE](../Statistical/LARGE.md) | Returns the k-th largest value. AGGREGATE can do the same with option 6. |
| [MEDIAN](../Statistical/MEDIAN.md) | Returns the median. AGGREGATE function 12 adds option control. |
| [PERCENTILE.INC](../Statistical/PERCENTILE.INC.md) | Returns a percentile. AGGREGATE function 16 adds option control. |

## Official Documentation

- [Microsoft Support: AGGREGATE function](https://support.microsoft.com/en-us/excel/functions/aggregate-function)
