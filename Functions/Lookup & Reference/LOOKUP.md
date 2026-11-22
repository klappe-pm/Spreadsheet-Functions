---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Classic Lookup
purpose:
  - Data Retrieval
use-case:
  - Effective Date Rate Schedule
  - Grade Band Lookup
  - Shipping Weight Bands
related:
  - HLOOKUP
  - IFERROR
  - INDEX
  - MATCH
  - VLOOKUP
  - XLOOKUP
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/lookup-function
  - https://support.google.com/docs/answer/3256570
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Approximate Lookup
  - Sorted Lookup
  - Vector Lookup
tags:
  - approximate-match
  - excel
  - lookup
  - reference
  - sheets
---

# LOOKUP

## Description

**LOOKUP** searches a single row or column for a value and returns the matching value from a second row or column. It is an approximate lookup. When the exact value is not in the list, LOOKUP uses the largest value that is less than or equal to the lookup value. This makes it a good fit for bands, such as grade boundaries, weight brackets or rate schedules, where each lower limit applies until the next one starts.

LOOKUP requires the search list to be sorted in ascending order. If the data is not sorted, LOOKUP can return a wrong value without any warning. For exact matches on unsorted data, use [MATCH](MATCH.md) with a `0` match type, [VLOOKUP](VLOOKUP.md) with `FALSE`, or [XLOOKUP](XLOOKUP.md). Microsoft recommends VLOOKUP, HLOOKUP or XLOOKUP for most new work and describes the array form of LOOKUP as included mainly for compatibility with other spreadsheet programs.

LOOKUP has two forms. The vector form takes a search range and a separate result range of the same size. The array form takes one range that holds both columns or both rows, searches its first row or column, and returns a value from its last row or column. Google Sheets documents the same two forms as the two-argument and one-argument versions.

## Syntax

```excel
=LOOKUP(lookup_value, lookup_vector, [result_vector])
```

```excel
=LOOKUP(lookup_value, array)
```

<!-- Image 1: Vector and Array Forms. See Images/Lookup & Reference/LOOKUP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `lookup_value` | Yes | The value to find. It can be a number, text, a logical value or a cell reference. |
| `lookup_vector` | Yes (vector form) | A single row or single column of values sorted in ascending order. Text, numbers and logical values can all be used. |
| `result_vector` | No | A single row or column with the same number of cells as `lookup_vector`. The value at the matching position is returned. |
| `array` | Yes (array form) | A range whose first row or column holds the search values and whose last row or column holds the results. |

### Return Value

The value from `result_vector` at the position of the largest search value that is less than or equal to `lookup_value`. In the array form, the value comes from the last row or column of the array. LOOKUP returns `#N/A` when `lookup_value` is smaller than the smallest value in the list.

## Examples

All examples use a grade band table in `A2:B6`. The thresholds are in ascending order in column A, and the letter grades are in column B. A second table in `D1:E6` lists names with their extension numbers, sorted by name.

| Minimum Score | Grade | | Name | Extension |
| --- | --- | --- | --- | --- |
| 0 | F | | Ana | 4101 |
| 60 | D | | Ben | 4102 |
| 70 | C | | Cy | 4105 |
| 80 | B | | Dee | 4110 |
| 90 | A | | Eli | 4120 |

### Example 1: Grade for a Score Between Bands

```excel
=LOOKUP(87, A2:A6, B2:B6)
```

**Result:** `B`

The largest minimum score that is not above 87 is 80, which carries the grade B. The score falls in the 80 band, not the 90 band.

### Example 2: Score Exactly on a Boundary

```excel
=LOOKUP(60, A2:A6, B2:B6)
```

**Result:** `D`

An exact match on 60 returns its own row. The boundary belongs to the band that starts at that value.

<!-- Image 2: Grade Band Table. See Images/Lookup & Reference/LOOKUP.md -->

### Example 3: Score Below the Lowest Band

```excel
=LOOKUP(59, A2:A6, B2:B6)
```

**Result:** `F`

The largest threshold not above 59 is 0, so the grade is F. Had the first threshold been 60, this formula would return `#N/A`.

### Example 4: Array Form

```excel
=LOOKUP(87, A2:B6)
```

**Result:** `B`

The array has five rows and two columns, so LOOKUP searches the first column and returns from the last column. The result is the same as Example 1 without a separate result range.

### Example 5: Text Lookup in a Sorted Name List

```excel
=LOOKUP("Dana", D2:D6, E2:E6)
```

**Result:** `4105`

Dana is not in the list. Alphabetically, Dana falls after Cy and before Dee, so LOOKUP returns the extension for Cy. This is useful for bands, but it can mislead when a name is simply missing. Check for an exact match first when accuracy matters.

### Example 6: Exact Text Match With a Safer Formula

```excel
=INDEX(E2:E6, MATCH("Dana", D2:D6, 0))
```

**Result:** `#N/A`

An exact MATCH makes the missing name visible as `#N/A` instead of silently returning Cy's extension. Wrap the formula in IFERROR to show a message.

## Story Problems

### Problem 1: Shipping Weight Bands

A courier charges a fee that depends on the weight of a parcel. The bands are in `A1:B5`, and each band applies from its minimum weight up to the next band.

| Minimum Weight (kg) | Fee |
| --- | --- |
| 0 | 4.00 |
| 1 | 7.50 |
| 5 | 12.00 |
| 10 | 20.00 |

**Task:** Enter a parcel weight of 6.4 kg in `D2`, then return the fee for that weight.

**Solution:**

```excel
=LOOKUP(D2, A2:A5, B2:B5)
```

**Answer:** `12.00`. The largest minimum weight not above 6.4 is 5 kg, which carries a fee of 12.00.

### Problem 2: Finding an Extension

An office keeps a sorted list of names and phone extensions in `A1:B6`. Before calling a colleague, a staff member looks up the extension for Dee.

| Name | Extension |
| --- | --- |
| Ana | 4101 |
| Ben | 4102 |
| Cy | 4105 |
| Dee | 4110 |
| Eli | 4120 |

**Task:** Return Dee's extension from the list in `A2:B6`.

**Solution:**

```excel
=LOOKUP("Dee", A2:A6, B2:B6)
```

**Answer:** `4110`. Dee is an exact match, so LOOKUP returns the extension in the same row. The same formula would return the wrong extension for a name that is missing, which is why an exact method is better for names.

## Use Cases

### Grade Band Lookup

**Scenario:** A school report sheet converts each numeric score into a letter grade using the same boundaries every term. The boundaries are kept in a table that teachers can edit.

```excel
=LOOKUP(B2, $A$2:$A$6, $B$2:$B$6)
```

**Why It Works:** Each score is compared with the lower limit of each band. The formula returns the grade for the highest limit the score has reached. Keep the limits in ascending order, because the formula depends on that order.

### Effective Date Rate Schedule

**Scenario:** A utility changes its unit price on several dates. Each invoice must use the rate that was in force on the date of the usage.

```excel
=LOOKUP(A2, EffectiveDates, RatesPerUnit)
```

**Why It Works:** EffectiveDates is a list of change dates in ascending order, and RatesPerUnit holds the rate that starts on each date. A usage date that falls between two change dates returns the earlier rate. Dates are stored as numbers, so the comparison is correct when the cells are true date values.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | `lookup_value` is smaller than the smallest value in the list. | Add a row with a lower starting value, such as 0, or wrap the formula in IFERROR. |
| Wrong result | The search list is not sorted in ascending order. | Sort the list from smallest to largest, or use MATCH with `0` or XLOOKUP for exact matches. |
| Wrong result | A missing exact value returns the nearest smaller entry. | Use INDEX with MATCH and a match type of `0` when the value must exist. |
| Error or wrong result | The result range is not the same size as the search range. | Select ranges of equal length in the vector form. |
| `#N/A` | The number is stored as text while the list holds numbers, or the reverse. | Convert the value with VALUE, or re-enter the list as numbers. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions from Excel 2016 through Microsoft 365, including Excel for the web | Vector and array forms are both supported. Microsoft recommends VLOOKUP, HLOOKUP or XLOOKUP for most work, and XLOOKUP in Microsoft 365. |
| Google Sheets | Available | Documents the search key, the search range or search result array, and an optional result range. Uses the next smaller value when the key is not found, and recommends VLOOKUP or HLOOKUP for unsorted data. |

## Tips and Best Practices

- Use LOOKUP only for approximate matches on sorted lists, such as bands and schedules.
- Keep bands in ascending order and review the order whenever the table is edited.
- Start the first band at the lowest possible value, such as 0, so every input has a band.
- Use MATCH with `0`, VLOOKUP with `FALSE` or XLOOKUP for exact matches, because they report a missing value.
- Name the bands and rates with defined names so the formula is easier to read and copy.

## Related Functions

| Function | Relationship |
| --- | --- |
| [INDEX](INDEX.md) | Returns a value by position and pairs with MATCH for exact or approximate lookups. |
| [MATCH](MATCH.md) | Finds the position of a value, with match type `1` for bands on sorted data. |
| [VLOOKUP](VLOOKUP.md) | Reads a value to the right of the lookup column, with approximate or exact matching. |
| [HLOOKUP](HLOOKUP.md) | The horizontal version of VLOOKUP for data laid out in rows. |
| [XLOOKUP](XLOOKUP.md) | A modern lookup that searches in either direction and handles missing values. |
| [IFERROR](../Logical/IFERROR.md) | Shows a message when LOOKUP returns `#N/A`. |

## Official Documentation

- [Microsoft Support: LOOKUP function](https://support.microsoft.com/en-us/excel/functions/lookup-function)
- [Google Docs Editors Help: LOOKUP](https://support.google.com/docs/answer/3256570)
