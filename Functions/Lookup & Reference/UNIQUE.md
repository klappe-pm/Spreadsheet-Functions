---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Dynamic Arrays
purpose:
  - Data Cleaning
  - Sorting and Filtering
use-case:
  - Customer Record Matching
  - Dropdown Source Lists
  - Unmatched Record Reconciliation
related:
  - CHOOSECOLS
  - FILTER
  - HSTACK
  - ROWS
  - SORT
  - VSTACK
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/unique-function
  - https://support.google.com/docs/answer/10522653
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Distinct Values
  - Remove Duplicates
  - Dedupe
tags:
  - deduplication
  - dynamic-array
  - excel
  - sheets
---

# UNIQUE

## Description

**UNIQUE** returns the distinct values from a range or array, with repeats removed. The result spills into the cells below the formula and updates when the source changes. Before UNIQUE, a distinct list needed the Remove Duplicates command, which changes the source data, or a complex array formula.

By default, UNIQUE keeps each value that appears one or more times, in the order of first appearance. Set the third argument, `exactly_once`, to TRUE to return only the values that appear a single time and drop any value that repeats. That mode finds items that are missing a match, such as a customer that appears in one system but not the other.

UNIQUE also works across several columns. A multi-column range is compared row by row, so two rows are duplicates only when every column matches. Set `by_col` to TRUE to compare columns instead of rows.

UNIQUE is available in Microsoft 365, Excel 2021 and Excel 2024, and in Google Sheets. Google Sheets calls the arguments `range`, `by_column` and `exactly_once`, and supports the same exactly_once behavior.

## Syntax

```excel
=UNIQUE(array, [by_col], [exactly_once])
```

<!-- Image 1: UNIQUE Arguments. See Images/Lookup & Reference/UNIQUE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array to return unique rows or columns from. A multi-column range is compared across all of its columns together. |
| `by_col` | No | FALSE (the default) compares rows and returns unique rows. TRUE compares columns and returns unique columns. |
| `exactly_once` | No | FALSE (the default) returns every distinct row or value. TRUE returns only the rows or values that occur exactly once. |

### Return Value

An array of unique rows (or columns, when `by_col` is TRUE). It spills into the cells below and to the right of the formula. The spill range resizes automatically to match the number of results.

## Examples

All examples use these regions and products in `A2:B8`.

| Region | Product |
| --- | --- |
| North | Widgets |
| South | Gadgets |
| North | Widgets |
| East | Widgets |
| South | Gadgets |
| South | Gizmos |
| West | Gadgets |

### Example 1: Distinct Regions

```excel
=UNIQUE(A2:A8)
```

**Result:** North, South, East, West

Each region appears once, in the order it first appears in the list.

### Example 2: Distinct Regions, Sorted

```excel
=SORT(UNIQUE(A2:A8))
```

**Result:** East, North, South, West

SORT puts the distinct regions in alphabetical order.

### Example 3: Regions That Appear Exactly Once

```excel
=UNIQUE(A2:A8, FALSE, TRUE)
```

**Result:** East, West

North and South repeat, so they are dropped. East and West each appear one time.

### Example 4: Distinct Region and Product Pairs

```excel
=UNIQUE(A2:B8)
```

**Result:** Five pairs: North and Widgets, South and Gadgets, East and Widgets, South and Gizmos, West and Gadgets

Two rows are duplicates only when both columns match. North and Widgets appears twice, but it is returned once.

### Example 5: Count Distinct Regions

```excel
=ROWS(UNIQUE(A2:A8))
```

**Result:** `4`

ROWS counts the rows in the unique list, which gives the number of distinct regions.

<!-- Image 2: Exactly Once Result. See Images/Lookup & Reference/UNIQUE.md -->

## Story Problems

### Problem 1: Department Count

A staff list in `A2:A13` has twelve entries, with departments repeated. The departments are Sales, Support, Finance, HR and Ops.

**Task:** Count how many different departments appear in the list.

**Solution:**

```excel
=ROWS(UNIQUE(A2:A13))
```

**Answer:** `5`. Sales appears four times, Support, Finance, HR and Ops appear twice each, and every department is counted once.

### Problem 2: Unmatched SKUs

Two lists of product codes are kept side by side, one in `A2:A6` and one in `B2:B6`. Each list has five codes with no repeats inside it.

| List A | List B |
| --- | --- |
| SKU-10 | SKU-12 |
| SKU-11 | SKU-14 |
| SKU-12 | SKU-15 |
| SKU-13 | SKU-16 |
| SKU-14 | SKU-11 |

**Task:** Find the codes that appear in only one of the two lists.

**Solution:**

```excel
=UNIQUE(VSTACK(A2:A6, B2:B6), , TRUE)
```

**Answer:** SKU-10, SKU-13, SKU-15 and SKU-16. SKU-11, SKU-12 and SKU-14 appear in both lists, so they are dropped.

## Use Cases

### Dropdown Source Lists

**Scenario:** A data entry form needs a dropdown of product categories that grows as new categories are added to the product table.

```excel
=SORT(UNIQUE(Products!C2:C1000))
```

**Why It Works:** UNIQUE removes repeats, SORT orders the result, and a named range pointing at this formula stays current as the list changes.

### Customer Record Matching

**Scenario:** A team wants a single list of customers that appear anywhere in two source tables, with each name listed once.

```excel
=UNIQUE(VSTACK(CRM!A2:A500, Billing!A2:A500))
```

**Why It Works:** VSTACK combines the two lists, and UNIQUE returns each customer once, even when the same customer appears in both tables.

### Unmatched Record Reconciliation

**Scenario:** Finance needs the customers who appear in one of two systems but not in both.

```excel
=UNIQUE(VSTACK(CRM!A2:A500, Billing!A2:A500), , TRUE)
```

**Why It Works:** Customers in both systems appear twice in the stacked list and are dropped by `exactly_once`, which leaves only the mismatches.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#SPILL!` | The cells below or beside the formula are not empty. | Clear the spill range, or move the formula. |
| Blank appears in the result | Empty cells in the source are treated as a value. | Use `UNIQUE(FILTER(range, range<>""))`. |
| Rows that look duplicated are still returned | Values differ by hidden characters such as trailing spaces. | Trim the source text, and format numbers consistently. |
| Values disappear from the result | `exactly_once` is TRUE, and a repeated value is dropped completely. | Use the default FALSE when every distinct value is needed. |
| `#NAME?` | The Excel version is 2019 or earlier. | Use Excel 2021 or later, Microsoft 365, or Google Sheets. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2021, Excel 2024 and Excel for the web | Not listed for Excel 2019 or earlier. Includes `by_col` and `exactly_once`. |
| Google Sheets | Available | Arguments are named `range`, `by_column` and `exactly_once`, and the behavior matches Excel. |

## Tips and Best Practices

- Combine UNIQUE with SORT for a list people can read, because UNIQUE keeps the order of first appearance.
- Filter out blank cells before UNIQUE so an empty value does not appear as a result.
- Use multi-column UNIQUE for record-level deduplication, and include every column that defines a duplicate.
- Wrap UNIQUE in ROWS or COUNTA when you need the number of distinct values.
- Leave empty rows below the formula so the result can grow when new distinct values appear.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SORT](SORT.md) | Orders the unique values alphabetically or numerically. |
| [FILTER](FILTER.md) | Removes blanks or other unwanted rows before UNIQUE. |
| [VSTACK](VSTACK.md) | Combines lists before finding the values that appear once. |
| [HSTACK](HSTACK.md) | Places a unique list beside a count of each value. |
| [ROWS](ROWS.md) | Counts the distinct values that UNIQUE returns. |
| [CHOOSECOLS](CHOOSECOLS.md) | Selects the columns that define a duplicate before UNIQUE is applied. |

## Official Documentation

- [Microsoft Support: UNIQUE function](https://support.microsoft.com/en-us/excel/functions/unique-function)
- [Google Docs Editors Help: UNIQUE](https://support.google.com/docs/answer/10522653)
