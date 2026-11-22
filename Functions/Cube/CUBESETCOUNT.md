---
domain: Spreadsheet Functions
category: Cube
subcategory: OLAP Sets
purpose:
  - Counting
  - OLAP Analysis
use-case:
  - Dropdown Source Sizes
  - Set Size Checks
  - Store Count Reporting
related:
  - COUNTA
  - CUBERANKEDMEMBER
  - CUBESET
  - CUBEVALUE
  - IFERROR
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/cubesetcount-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Count Set Items
  - Set Count
tags:
  - count
  - cube
  - excel
  - olap
  - set
---

# CUBESETCOUNT

## Description

**CUBESETCOUNT** returns the number of items in a set. The set comes from a CUBESET formula, either typed directly into CUBESETCOUNT or held in a cell that CUBESETCOUNT refers to. Use it to find out how many stores, reps or categories a set contains before a report depends on that count, or to confirm that a set is the size you expected.

The count depends on the members the set returns, not on the order they are sorted in. A sorted CUBESET and an unsorted one of the same members return the same count. Check the count before ranking with CUBERANKEDMEMBER, because a rank above the number of items has no member to return.

CUBESETCOUNT works only with sets created from a multidimensional cube. It is an Excel function with no Google Sheets equivalent. While the set loads, the cell shows the temporary message `#GETTING_DATA…`.

## Syntax

```excel
=CUBESETCOUNT(set)
```

<!-- Image 1: Set Argument as a Cell Reference. See Images/Cube/CUBESETCOUNT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `set` | Yes | A text Microsoft Excel expression that evaluates to a set, the CUBESET function itself, or a reference to a cell that contains a CUBESET formula. |

### Return Value

The function returns a number: the count of items in the set. The article states that the function returns the number of items in a set, and it lists no separate error values for this function.

A set is created by CUBESET, so if CUBESET cannot create the set, the errors that CUBESET returns, such as `#NAME?` or `#N/A`, appear in place of a count.

## Examples

The examples use a connection named `SalesCube` to a cube with Geography, Product and Rep hierarchies.

### Example 1: Count Regions in a Set Held in a Cell

Cell `A3` holds this CUBESET formula:

```excel
=CUBESET("SalesCube", "{[Geography].[Region].children}")
```

```excel
=CUBESETCOUNT(A3)
```

**Result:** The number of regions in the set held in `A3`.

Referring to the cell keeps the set definition in one place, so the count and the set always agree.

### Example 2: Count Categories With the Set Inline

```excel
=CUBESETCOUNT(CUBESET("SalesCube", "{[Product].[Category].children}"))
```

**Result:** The number of product categories in the cube.

### Example 3: Show a Readable Message When the Set Fails

```excel
=IFERROR(CUBESETCOUNT(B2), "Set unavailable")
```

**Result:** The count when the set in `B2` is valid, or `Set unavailable` when the set cannot be created.

### Example 4: Count a Sorted Set

```excel
=CUBESETCOUNT(CUBESET("SalesCube", "{[Rep].[Name].children}", "Reps", 2, "[Measures].[Sales Amount]"))
```

**Result:** The number of reps in the set. Sorting by sales changes the order of the reps but not the count.

<!-- Image 2: Count Compared With an Expected Size. See Images/Cube/CUBESETCOUNT.md -->

## Story Problems

### Problem 1: Stores in the West Region

A chain's planning sheet needs the number of stores in the West region. Cell `B2` holds a CUBESET formula that returns the West stores, which are Pine, Oak, Cedar and Birch.

| Store in West Region |
| --- |
| Pine |
| Oak |
| Cedar |
| Birch |

**Task:** Count the stores in the set held in `B2`.

**Solution:**

```excel
=CUBESETCOUNT(B2)
```

**Answer:** `4`. The West set holds four stores, one for each name in the list.

<!-- Image 3: Planned Count Compared With the Set. See Images/Cube/CUBESETCOUNT.md -->

### Problem 2: Checking a Planned Store Count

The same planning sheet expects five West stores in cell `E2`, with the planned count entered there. The set from Problem 1 has four members.

**Task:** Compare the count from the set with the planned count in `E2`, and show `Matches` when they agree or `Check set` when they differ.

**Solution:**

```excel
=IF(CUBESETCOUNT(B2)=E2,"Matches","Check set")
```

**Answer:** `Check set`. The set holds 4 stores but 5 are planned, so the set or the plan needs review.

## Use Cases

### Set Size Checks Before Ranking

**Scenario:** A top-five report should only rank a set that has at least five members, and the check must happen before the ranking formulas run.

```excel
=IF(CUBESETCOUNT(B2)>=5, "Ready", "Fewer than five members")
```

**Why It Works:** The count guards the ranking step, so the report shows a clear message instead of a rank that has no member to return.

### Store Count Reporting

**Scenario:** A monthly summary shows how many stores are open in each region, with the count coming from the cube.

```excel
=CUBESETCOUNT(CUBESET("SalesCube", "{[Store].[Region].&[West].children}"))
```

**Why It Works:** The count follows the cube's store list, so a new store appears in the summary without a manual update.

### Dropdown Source Sizes

**Scenario:** A dropdown should list only the members that a set contains, and the sheet must warn when the list grows past a limit.

```excel
=IF(CUBESETCOUNT(B2)>50, "Too many items for a dropdown", "OK")
```

**Why It Works:** The count tells the sheet how many items the dropdown would show, so the warning appears before users face a long list.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The set was created with a connection that is not a workbook connection, or the OLAP server is not running or available. | Check the connection name in the CUBESET formula and confirm that the server is available. |
| `#N/A` | The set expression was invalid, so CUBESET could not create the set. | Correct the set expression in the CUBESET formula. |
| Unexpected count | The set expression returns a different level of the hierarchy than intended. | Check the hierarchy level in the set expression, and use `.children` or the named level on purpose. |
| `#GETTING_DATA…` | The set is still loading. | Wait for the query to finish. This message is temporary. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web, and Excel for iPad, iPhone and Android | Works with sets created by CUBESET from a multidimensional cube. |
| Google Sheets | Not available | Closest alternative: count the rows of a list kept in the sheet with COUNTA. |

## Tips and Best Practices

- Keep the CUBESET formula in one cell and count that cell, so the count and the set always describe the same members.
- Sorting does not change the count, so you can sort the set for ranking without recounting.
- Compare the count with an expected size before a report relies on it, because a surprise count often means the expression targets the wrong level.
- Wrap the count in IFERROR when a set can fail while a report is open.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNTA](../Statistical/COUNTA.md) | Counts non-empty cells in a list kept in the sheet, not in the cube. |
| [CUBERANKEDMEMBER](CUBERANKEDMEMBER.md) | Returns a member at a given rank, which the count should cover. |
| [CUBESET](CUBESET.md) | Creates the set that this function counts. |
| [CUBEVALUE](CUBEVALUE.md) | Aggregates values for a set used as a slicer. |
| [IFERROR](../Logical/IFERROR.md) | Replaces a failed set with a readable message. |

## Official Documentation

- [Microsoft Support: CUBESETCOUNT function](https://support.microsoft.com/en-us/excel/functions/cubesetcount-function)
