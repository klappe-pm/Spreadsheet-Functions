---
domain: Spreadsheet Functions
category: Information
subcategory: Error Checks
purpose:
  - Error Handling
  - Type Checking
use-case:
  - Lookup Fallback Values
  - Safe Division in Pricing
related:
  - ERROR.TYPE
  - IFERROR
  - ISERR
  - ISNA
  - VLOOKUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/is-functions
  - https://support.google.com/docs/answer/3093349
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Any Error Test
tags:
  - error-checks
  - error-handling
  - excel
  - sheets
---

# ISERROR

## Description

**ISERROR** tests whether a value is any error value. It returns TRUE for `#N/A`, `#DIV/0!`, `#VALUE!`, `#REF!`, `#NAME?`, `#NUM!` and `#NULL!`, and FALSE for everything else, including numbers, text and blank cells.

Use ISERROR when you want a yes or no answer to the question "did this formula fail?" It is often used to show a fallback value, such as "Not found" when a lookup has no match, or to stop an error from spreading into totals. ISERROR is the broadest test in the IS family, because it includes `#N/A`. If a missing lookup is expected and you want to keep it visible, use ISERR or ISNA instead.

ISERROR is usually combined with IF. Before IFERROR existed, this combination was the standard way to replace an error with a fallback value. IFERROR is simpler when that is the only goal, but ISERROR is still useful when you need the TRUE or FALSE result for counting or for a separate check.

## Syntax

```excel
=ISERROR(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISERROR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value to test. It can be a formula, a cell reference or a constant such as `#N/A`. |

### Return Value

TRUE when the value is any error, including `#N/A`. FALSE when the value is a number, text, a logical value or a blank cell. A range passed directly returns one result, so use SUMPRODUCT or ARRAYFORMULA to test many cells.

## Examples

Cells A1 to A3 hold these values: A1 `=1/0`, A2 `=NA()` and A3 the number 10. Cells D2 to E4 hold a small price list with item codes in D and prices in E: 101 with 1.50, 102 with 3.25 and 103 with 4.00.

### Example 1: Division Error

```excel
=ISERROR(A1)
```

**Result:** `TRUE`

`#DIV/0!` is an error, so the test returns TRUE.

### Example 2: The `#N/A` Case

```excel
=ISERROR(A2)
```

**Result:** `TRUE`

Unlike ISERR, ISERROR counts `#N/A` as an error.

### Example 3: A Normal Number

```excel
=ISERROR(A3)
```

**Result:** `FALSE`

The number 10 is not an error.

### Example 4: Lookup With No Match

```excel
=IF(ISERROR(VLOOKUP(105, D2:E4, 2, FALSE)), "Not found", VLOOKUP(105, D2:E4, 2, FALSE))
```

**Result:** `Not found`

Code 105 is not in the list, so VLOOKUP returns `#N/A`. ISERROR detects that error and the formula shows the fallback text.

<!-- Image 2: Lookup Fallback Result. See Images/Information/ISERROR.md -->

### Example 5: Lookup With a Match

```excel
=IF(ISERROR(VLOOKUP(102, D2:E4, 2, FALSE)), "Not found", VLOOKUP(102, D2:E4, 2, FALSE))
```

**Result:** `3.25`

Code 102 exists, so ISERROR returns FALSE and the formula returns the price.

## Story Problems

### Problem 1: Orders That Failed to Match

An order report looks up the status of each order. Two lookups failed, one with `#N/A` and one with `#REF!`.

| Order | Status |
| --- | --- |
| ORD-1 | Shipped |
| ORD-2 | `#N/A` |
| ORD-3 | `#REF!` |
| ORD-4 | Shipped |

**Task:** Count the rows in B2:B5 that contain any error.

**Solution:**

```excel
=SUMPRODUCT(--ISERROR(B2:B5))
```

**Answer:** `2`. ORD-2 returns `#N/A` and ORD-3 returns `#REF!`. Both count as errors because ISERROR includes `#N/A`.

### Problem 2: Safe Sales per Unit

A sheet divides sales by units sold. The Pad sold nothing, which causes a division error.

| Product | Sales | Units | Sales per Unit |
| --- | --- | --- | --- |
| Pen | 500 | 100 | |
| Pad | 300 | 0 | |
| Marker | 240 | 60 | |

**Task:** Put a formula in D2 that returns sales per unit, or an empty result when the division fails, then fill it down to row 4.

**Solution:**

```excel
=IF(ISERROR(B2/C2), "", B2/C2)
```

**Answer:** Pen shows `5`, Pad shows an empty result, and Marker shows `4`.

## Use Cases

### Lookup Fallback Values

**Scenario:** A customer report pulls the region for each account from a lookup table. New accounts are not in the table yet, and the report should say so instead of showing an error.

```excel
=IF(ISERROR(VLOOKUP(B2, Accounts!A:C, 3, FALSE)), "Add to table", VLOOKUP(B2, Accounts!A:C, 3, FALSE))
```

**Why It Works:** The formula writes the lookup twice, once for the test and once for the result. IFERROR states the same fallback in one place, which is easier to maintain.

### Safe Division in Pricing

**Scenario:** A pricing model calculates cost per unit for dozens of products. Some products have no units yet, and the model should show a blank rather than an error.

```excel
=IF(ISERROR(D2/E2), "", D2/E2)
```

**Why It Works:** The blank result keeps the totals clean. The formula still calculates correctly for every product that has units.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Missing lookup hidden as TRUE | ISERROR includes `#N/A`, so an expected gap looks like an error. | Use ISNA when only `#N/A` should be handled. |
| Slow sheet | The formula repeats an expensive calculation inside ISERROR and again in the result. | Use IFERROR, which evaluates the expression once. |
| One result for a range | ISERROR tests one value when given a single reference. | Use SUMPRODUCT with `--ISERROR(range)`, or ARRAYFORMULA in Google Sheets. |
| Errors still appear | A formula returns an error that the IF does not wrap. | Wrap every formula that can fail, including references to other formulas. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions, including Excel for the web | Returns TRUE for every error type, including `#N/A`. Use SUMPRODUCT for counts over a range. |
| Google Sheets | Available | Same definition: TRUE for any error value. Use ARRAYFORMULA for ranges. |

## Tips and Best Practices

- Use IFERROR for a simple fallback and ISERROR when you need the TRUE or FALSE result.
- Use ISNA or ISERR when `#N/A` must stay visible or must be handled differently from other errors.
- Avoid wrapping large formulas in ISERROR, because the formula is repeated.
- Use ERROR.TYPE when a report needs to name the error that occurred.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ERROR.TYPE](ERROR.TYPE.md) | Returns the number of the error type. |
| [IFERROR](../Logical/IFERROR.md) | Returns a fallback value for any error in one step. |
| [ISERR](ISERR.md) | Tests for any error except `#N/A`. |
| [ISNA](ISNA.md) | Tests only for `#N/A`. |
| [VLOOKUP](../Lookup%20%26%20Reference/VLOOKUP.md) | A common source of `#N/A` that ISERROR detects. |

## Official Documentation

- [Microsoft Support: IS functions](https://support.microsoft.com/en-us/excel/is-functions)
- [Google Docs Editors Help: ISERROR](https://support.google.com/docs/answer/3093349)
