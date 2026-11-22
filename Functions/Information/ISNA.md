---
domain: Spreadsheet Functions
category: Information
subcategory: Error Checks
purpose:
  - Error Handling
  - Type Checking
use-case:
  - Lookup Fallback
  - Missing Match Count
  - Vendor Quote Check
related:
  - IFERROR
  - IFNA
  - ISERR
  - ISERROR
  - MATCH
  - NA
  - XLOOKUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/is-functions
  - https://support.google.com/docs/answer/3093293
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - error-handling
  - excel
  - information
  - lookup
  - sheets
---

# ISNA

## Description

**ISNA** returns TRUE only when a value is the `#N/A` error, which usually means a lookup did not find a match. It returns FALSE for every other value, including other errors such as `#VALUE!`, `#REF!` and `#DIV/0!`.

Use ISNA when a missing lookup result should trigger a different action, such as a default value, a "not found" label or a count of unmatched items. Because ISNA ignores other errors, a real problem in the formula still shows up instead of being hidden.

ISNA is the narrow test. ISERROR catches every error type, and IFNA or IFERROR replace errors directly without a separate test. Use ISNA when you need to know that the error was specifically `#N/A`.

## Syntax

```excel
=ISNA(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISNA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value, expression or cell reference to test. A formula that returns `#N/A`, such as a MATCH with no match, is the usual input. |

### Return Value

TRUE when `value` is the `#N/A` error, or refers to a cell that displays it. FALSE for any other value, including other error types.

## Examples

### Example 1: Detecting a Missing Match

The list in `A2:A6` holds Apple, Banana, Cherry, Date and Elderberry.

```excel
=ISNA(MATCH("Kiwi",A2:A6,0))
```

**Result:** `TRUE`

Kiwi is not in the list, so MATCH returns `#N/A`, and ISNA returns TRUE.

### Example 2: Detecting a Found Match

```excel
=ISNA(MATCH("Banana",A2:A6,0))
```

**Result:** `FALSE`

Banana is in position 2, so MATCH returns a number and ISNA returns FALSE.

### Example 3: Labeling Lookup Results

Cell D2 holds `Date`.

```excel
=IF(ISNA(MATCH(D2,A2:A6,0)),"Not in list","In list")
```

**Result:** `In list`

The formula reports the result in plain words instead of showing an error.

### Example 4: Other Errors Do Not Match

```excel
=ISNA(1/0)
```

**Result:** `FALSE`

Dividing by zero returns `#DIV/0!`, which is a different error, so ISNA returns FALSE.

## Story Problems

### Problem 1: Requested Items Not in the Catalog

A distributor keeps a catalog of four product codes in `A2:A5`. A customer sends a request list in `D2:D5`. The sales team wants the count of requested codes that are not in the catalog.

| Catalog Code | Requested Code |
| --- | --- |
| SKU-10 | SKU-20 |
| SKU-20 | SKU-35 |
| SKU-30 | SKU-40 |
| SKU-40 | SKU-50 |

**Task:** Count the requested codes in `D2:D5` that MATCH cannot find in `A2:A5`.

**Solution:**

```excel
=SUMPRODUCT(ISNA(MATCH(D2:D5,A2:A5,0))*1)
```

**Answer:** `2`. SKU-35 and SKU-50 are not in the catalog.

### Problem 2: Vendor Quotes With Missing Prices

A purchasing clerk gathers quotes from a vendor. The vendor's system returns `#N/A` for items it does not stock. The clerk needs the number of missing quotes.

| Item | Price |
| --- | --- |
| Pens | 2.40 |
| Paper | `#N/A` |
| Stapler | 6.75 |
| Markers | `#N/A` |

**Task:** Count the `#N/A` results in `B2:B5`.

**Solution:**

```excel
=SUMPRODUCT(ISNA(B2:B5)*1)
```

**Answer:** `2`. Paper and Markers have no quoted price.

<!-- Image 2: Vendor Quote Results. See Images/Information/ISNA.md -->

## Use Cases

### Lookup Fallback

**Scenario:** A price sheet should show "Not stocked" for any product code that has no match in the price list.

```excel
=IF(ISNA(XLOOKUP(B2,SKU,Price)),"Not stocked",XLOOKUP(B2,SKU,Price))
```

**Why It Works:** ISNA catches only the missing-match case. A different error from the lookup range would still appear, so a broken range is not hidden as "Not stocked". The named ranges `SKU` and `Price` keep the formula readable.

### Vendor Quote Check

**Scenario:** A buyer needs to send a follow-up email only for the items that a vendor did not quote.

```excel
=IF(ISNA(C2),"Request quote","Quoted")
```

**Why It Works:** The label drives a filter. Rows marked "Request quote" are the only ones that need follow-up, and the quoted rows stay out of the email list.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for a `#REF!` or `#VALUE!` | ISNA tests only for `#N/A`. | Use ISERROR to catch all error types. |
| `#N/A` from a match that looks correct | The lookup value has extra spaces or different capitalization. | Clean the value with TRIM and compare it with the list. |
| `#N/A` from an approximate match | The match type is 1 or omitted, and the list is not sorted. | Use match type 0 for an exact match. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Microsoft 365 for Mac, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016. | Returns TRUE only for `#N/A`. Use with MATCH, XLOOKUP and VLOOKUP. |
| Google Sheets | Available | Same syntax and return value. Works with lookup functions such as MATCH and XLOOKUP. |

## Tips and Best Practices

- Use IFNA when you only need a replacement value and do not need the TRUE or FALSE result.
- Use ISNA in a separate check column when a count of missing matches is the goal.
- Use exact match (match type 0) in lookups so `#N/A` means the value is truly missing.
- Clean lookup keys with TRIM before matching to avoid false `#N/A` results.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IFNA](../Logical/IFNA.md) | Replaces only `#N/A` with a value, in one step. |
| [IFERROR](../Logical/IFERROR.md) | Replaces any error with a value, in one step. |
| [ISERROR](ISERROR.md) | Tests for any error type, not only `#N/A`. |
| [ISERR](ISERR.md) | Tests for every error except `#N/A`. |
| [NA](NA.md) | Returns the `#N/A` error on purpose, such as to mark missing data. |
| [MATCH](../Lookup%20%26%20Reference/MATCH.md) | Produces the `#N/A` error when a value is not found. |
| [XLOOKUP](../Lookup%20%26%20Reference/XLOOKUP.md) | Returns `#N/A` when no match exists unless an if_not_found value is given. |

## Official Documentation

- [Microsoft Support: IS functions](https://support.microsoft.com/en-us/excel/is-functions)
- [Google Docs Editors Help: ISNA](https://support.google.com/docs/answer/3093293)
