---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Counting
purpose:
  - Counting
use-case:
  - Distinct Customer Counts
  - Unique Visitor Tracking
  - Warehouse SKU Reconciliation
related:
  - COUNT
  - COUNTA
  - COUNTIF
  - COUNTUNIQUEIFS
  - FILTER
  - SUMPRODUCT
  - UNIQUE
level: 2
source:
  - https://support.google.com/docs/answer/3093405
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Count Unique Values
  - Distinct Count
tags:
  - counting
  - distinct-values
  - sheets
---

# COUNTUNIQUE

## Description

**COUNTUNIQUE** counts the distinct values in one or more ranges or lists. Each value that appears more than once is counted once, so a list of customer names with repeats gives the number of different customers. Use it when a report needs a count of different items rather than a count of rows.

The function accepts several ranges or values separated by commas, and it counts the distinct values across all of them together. A value that appears in two ranges is counted once. The function is available in Google Sheets. Excel does not have a COUNTUNIQUE function, so the closest alternative there is the UNIQUE function combined with ROWS.

COUNTUNIQUE counts values, not rows, so it does not check whether two rows share the same combination of columns. Use a query or a helper column when you need distinct combinations.

## Syntax

```excel
=COUNTUNIQUE(value1, [value2, ...])
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/COUNTUNIQUE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first value or range to consider. Ranges and single values can be mixed. |
| `value2, ...` | No | Additional values or ranges. The distinct values across all arguments are counted together. |

### Return Value

A number: the count of distinct values across all arguments. The function is available only in Google Sheets, and Excel reports `#NAME?` for it.

## Examples

Examples 1, 3 and 4 use this list in `A2:A8` and `B2:B7`.

| Fruit (A) | Score (B) |
| --- | --- |
| Apple | 10 |
| Pear | 20 |
| Apple | 10 |
| Plum | 30 |
| Pear | 20 |
| Fig | 40 |
| Plum | |

### Example 1: Distinct Fruit in a Range

```excel
=COUNTUNIQUE(A2:A8)
```

**Result:** `4`

The fruit names Apple, Pear, Plum and Fig are each counted once.

### Example 2: Distinct Values Typed Into the Formula

```excel
=COUNTUNIQUE(1,1,2,3,5,8,13)
```

**Result:** `6`

The distinct values are 1, 2, 3, 5, 8 and 13.

### Example 3: Range Plus a Value

```excel
=COUNTUNIQUE(A2:A8,"Kiwi")
```

**Result:** `5`

The four fruit names from Example 1 are joined by Kiwi, which is not in the range.

### Example 4: Distinct Scores

```excel
=COUNTUNIQUE(B2:B7)
```

**Result:** `4`

The scores 10, 20, 30 and 40 are the distinct values in the range.

<!-- Image 2: Distinct Values Across Two Ranges. See Images/Math & Trig/COUNTUNIQUE.md -->

### Example 5: Excel Alternative

```excel
=ROWS(UNIQUE(A2:A8))
```

**Result:** `4`

In Excel 365 or Excel 2021, UNIQUE returns the distinct fruit names and ROWS counts them.

## Story Problems

### Problem 1: Distinct Customers

A shop exports one row for each order. The owner wants the number of different customers who placed orders, not the number of orders.

| Order | Customer |
| --- | --- |
| 1001 | Lin |
| 1002 | Okafor |
| 1003 | Lin |
| 1004 | Mendes |
| 1005 | Okafor |
| 1006 | Lin |
| 1007 | Patel |

**Task:** Count the distinct customers in column B.

**Solution:**

```excel
=COUNTUNIQUE(B2:B8)
```

**Answer:** `4`. The customers are Lin, Okafor, Mendes and Patel. Lin and Okafor each placed more than one order, but each is counted once.

### Problem 2: Warehouse SKU Reconciliation

Two warehouses list the product codes they hold. Some codes appear in both warehouses, and the purchasing team wants the number of distinct codes across the two lists.

| Warehouse | SKU |
| --- | --- |
| A | SKU-10 |
| A | SKU-12 |
| A | SKU-10 |
| B | SKU-12 |
| B | SKU-14 |

**Task:** Count the distinct SKU codes in column B.

**Solution:**

```excel
=COUNTUNIQUE(B2:B6)
```

**Answer:** `3`. The distinct codes are SKU-10, SKU-12 and SKU-14. SKU-12 is held in both warehouses but is counted once.

## Use Cases

### Distinct Customer Counts

**Scenario:** A sales log stores one row for each purchase in a sheet named Orders. The monthly report needs the number of different customers who bought during the month.

```excel
=COUNTUNIQUE(Orders!B2:B5000)
```

**Why It Works:** The range covers the full log, so new purchases are included when the range is extended. Repeat buyers are counted once, which gives a true customer count.

### Unique Visitor Tracking

**Scenario:** A site analytics export records one visitor identifier per visit. The team wants the number of different visitors in a campaign period.

```excel
=COUNTUNIQUE(Visits!C2:C10000)
```

**Why It Works:** Each visitor identifier is counted once no matter how many visits it appears in. Check that the identifier column holds a stable value, because a changing identifier counts the same visitor more than once.

### Warehouse SKU Reconciliation

**Scenario:** Purchasing combines the SKU columns from two warehouses in one range and needs the number of distinct codes.

```excel
=COUNTUNIQUE(B2:B6)
```

**Why It Works:** The formula counts each code once even when the code appears in several rows. Compare the count with the item master to find codes that are missing from one of the lists.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` in Excel | Excel has no COUNTUNIQUE function. | Use `=ROWS(UNIQUE(A2:A8))` in Excel 365 or Excel 2021. |
| Count is higher than expected | Spelling or spacing differences create separate values, such as "Lin" and "Lin ". | Clean the values first with TRIM, or standardize them before counting. |
| Count is lower than expected | The range does not include every row. | Extend the range, or use a named range that grows with the data. |
| Count includes a value you did not expect | A value was typed into the formula as well as a range. | Check each argument, and remove any extra values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use `=ROWS(UNIQUE(A2:A8))` in Excel 365 or Excel 2021. UNIQUE returns the distinct values, and ROWS counts them. |
| Google Sheets | Available | Accepts several ranges and values in one call. The page documents a BigQuery variant with a single column argument, which is not the same syntax. |

## Tips and Best Practices

- Use a named range or a table column so that the count includes new rows when they are added.
- Clean spelling and spacing with TRIM before counting, because a small difference creates a separate value.
- Use COUNTUNIQUEIFS when the distinct count must be limited by one or more conditions.
- Use QUERY or FILTER with a helper column when you need to count distinct combinations of columns.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNT](../Statistical/COUNT.md) | Counts numeric cells, including repeats. |
| [COUNTA](../Statistical/COUNTA.md) | Counts non-empty cells, including repeats. |
| [COUNTIF](../Statistical/COUNTIF.md) | Counts cells that meet one condition, including repeats. |
| [COUNTUNIQUEIFS](../Database/COUNTUNIQUEIFS.md) | Counts distinct values that meet one or more conditions. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the matching rows, which you can then count. |
| [SUMPRODUCT](SUMPRODUCT.md) | Builds a distinct count in Excel from a division by a COUNTIF array. |
| [UNIQUE](../Lookup%20%26%20Reference/UNIQUE.md) | Returns the distinct values, which ROWS can count in Excel. |

## Official Documentation

- [Google Docs Editors Help: COUNTUNIQUE](https://support.google.com/docs/answer/3093405)
