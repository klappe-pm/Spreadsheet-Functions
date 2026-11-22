---
domain: Spreadsheet Functions
category: Cube
subcategory: OLAP Members
purpose:
  - Data Retrieval
  - OLAP Analysis
  - Ranking
use-case:
  - Bottom Performer Review
  - Ranked Customer Reports
  - Top Performer Lists
related:
  - CUBEMEMBER
  - CUBESET
  - CUBESETCOUNT
  - CUBEVALUE
  - SORT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/cuberankedmember-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Nth Member
  - Ranked Set Member
tags:
  - cube
  - excel
  - olap
  - ranking
  - set
---

# CUBERANKEDMEMBER

## Description

**CUBERANKEDMEMBER** returns the nth member of a set from an OLAP cube, where n is the rank you supply. Rank 1 returns the first member in the set's order, rank 2 the second, and so on. A set is a list of members, such as every sales rep or every store, and the order of that list decides which member is ranked first. To return the top seller, sort the set by sales first, then ask for rank 1.

Use CUBERANKEDMEMBER for top and bottom lists, such as the three best stores or the five largest customers. To build a top five, fill the formula down and change the rank in each row. To return the lowest values, reverse the sort order in CUBESET rather than changing the rank.

CUBERANKEDMEMBER works only with workbook connections to a multidimensional cube. It is an Excel function with no Google Sheets equivalent. While the cube query runs, the cell shows `#GETTING_DATA…`.

## Syntax

```excel
=CUBERANKEDMEMBER(connection, set_expression, rank, [caption])
```

<!-- Image 1: Connection, Set, Rank and Caption Arguments. See Images/Cube/CUBERANKEDMEMBER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `connection` | Yes | The name of a workbook connection to the cube, as text. |
| `set_expression` | Yes | A text string with a set expression, such as `{[Rep].[Name].children}`. It can also be a CUBESET function or a cell reference to one. |
| `rank` | Yes | An integer position in the set. `1` returns the top member in the set's order, `2` returns the second, and so on. |
| `caption` | No | Text to show in the cell instead of the cube's caption. |

### Return Value

The function returns the member at the requested position in the set, displayed by its caption. The article does not separate the return value from the description, so the result is the nth member of the set as ordered.

The function returns `#NAME?` when the connection is not valid or the OLAP server is not running, available or responding. It returns `#N/A` when the `set_expression` syntax is incorrect or the set contains a member from a different dimension than the others.

## Examples

The examples use a connection named `SalesCube` to a cube with a Rep hierarchy and a Sales Amount measure.

### Example 1: Return the First Member of an Unsorted Set

```excel
=CUBERANKEDMEMBER("SalesCube", "{[Rep].[Name].children}", 1)
```

**Result:** The first rep in the cube's order, which is not necessarily the top seller.

This formula ranks by position only. Sort the set first, as in Example 2, when the rank must reflect sales.

### Example 2: Rank a Sorted Set

Cell `B2` holds this CUBESET formula, which sorts the reps by sales from highest to lowest:

```excel
=CUBESET("SalesCube", "{[Rep].[Name].children}", "Reps", 2, "[Measures].[Sales Amount]")
```

```excel
=CUBERANKEDMEMBER("SalesCube", B2, 1)
```

**Result:** The rep with the highest Sales Amount.

Because `B2` is sorted descending, rank 1 is the top seller.

### Example 3: Add a Caption

```excel
=CUBERANKEDMEMBER("SalesCube", B2, 2, "Second Place")
```

**Result:** `Second Place`

The caption replaces the rep name in the cell, which is useful for a podium layout.

### Example 4: Build a Top Five List

Enter this formula in `D2` and fill it down to `D6`:

```excel
=CUBERANKEDMEMBER("SalesCube", $B$2, ROWS($D$2:D2))
```

**Result:** The five highest-selling reps in order, one per row, from rank 1 in `D2` to rank 5 in `D6`.

`ROWS` supplies the rank for each row, so the formula changes its rank as it is filled down.

<!-- Image 2: Top Five Ranks Filled Down a Column. See Images/Cube/CUBERANKEDMEMBER.md -->

## Story Problems

### Problem 1: Second Highest Seller

A sales manager has five reps with these totals from the cube:

| Rep | Sales Amount |
| --- | --- |
| Avery | 4200 |
| Blake | 3100 |
| Casey | 5100 |
| Drew | 2750 |
| Emery | 3900 |

**Task:** Name the rep with the second highest sales, using a sorted CUBESET inside CUBERANKEDMEMBER.

**Solution:**

```excel
=CUBERANKEDMEMBER("SalesCube", CUBESET("SalesCube", "{[Rep].[Name].children}", "Reps", 2, "[Measures].[Sales Amount]"), 2)
```

**Answer:** `Avery`, with 4200 in sales. Sorted from highest to lowest, the order is Casey (5100), Avery (4200), Emery (3900), Blake (3100) and Drew (2750), so Avery is second.

<!-- Image 3: Sorted Set Ranking Result. See Images/Cube/CUBERANKEDMEMBER.md -->

### Problem 2: Third Busiest Store

A retail chain wants the store that ranks third by sales. The cube returns these totals:

| Store | Sales Amount |
| --- | --- |
| Harbor | 8200 |
| Lake | 9100 |
| Summit | 7600 |
| Valley | 6400 |

**Task:** Return the store in third place by sales.

**Solution:**

```excel
=CUBERANKEDMEMBER("SalesCube", CUBESET("SalesCube", "{[Store].[Name].children}", "Stores", 2, "[Measures].[Sales Amount]"), 3)
```

**Answer:** `Summit`, with 7600 in sales. Sorted from highest to lowest, the order is Lake, Harbor, Summit and Valley, so Summit holds third place.

## Use Cases

### Top Performer Lists

**Scenario:** A monthly bulletin lists the top three reps by sales, with the names updated from the cube each month.

```excel
=CUBERANKEDMEMBER("SalesCube", B2, 1, "Top Seller")
```

**Why It Works:** The set in `B2` is sorted once, and each rank returns the matching rep, so the bulletin stays accurate without manual sorting.

### Ranked Customer Reports

**Scenario:** An account team reviews its five largest customers each quarter, and the list must follow the cube's current sales figures.

```excel
=CUBERANKEDMEMBER("SalesCube", $B$2, ROWS($D$2:D2))
```

**Why It Works:** Filling the formula down builds the list in rank order, and the sorted set in `B2` decides which customers appear.

### Bottom Performer Review

**Scenario:** A regional manager wants the lowest-selling store to review first, so the set is sorted from lowest to highest.

```excel
=CUBERANKEDMEMBER("SalesCube", CUBESET("SalesCube", "{[Store].[Name].children}", "Stores", 1, "[Measures].[Sales Amount]"), 1)
```

**Why It Works:** An ascending sort puts the lowest sales first, so rank 1 returns the bottom member without a separate formula.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The connection is not a workbook connection, or the OLAP server is not running or available. | Check the connection name and confirm that the server is available. |
| `#N/A` | The set expression syntax is wrong, or the set mixes members from different dimensions. | Keep every member in the set from one dimension, such as Rep Name. |
| `#N/A` | A session-based object was referenced after its PivotTable was deleted or converted to formulas. | Recreate the PivotTable connection and refresh the formulas. |
| Wrong member | The set was not sorted, so rank 1 is the first member in cube order, not the top value. | Sort the set with CUBESET using `sort_order` and `sort_by` before ranking. |
| `#GETTING_DATA…` | The cube query is still running. | Wait for the query to finish. This message is temporary. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web, and Excel for iPad, iPhone and Android | Requires a multidimensional cube connection. Use CUBESET to sort the set before ranking. |
| Google Sheets | Not available | Closest alternative: sort the values in the sheet with SORT and return the nth row with INDEX. |

## Tips and Best Practices

- Sort the set before ranking, because rank depends on the order of the set and not on the values themselves.
- Fill the rank down with `ROWS` to build a top list without typing each rank.
- Use CUBESETCOUNT to check how many members the set holds before you ask for a high rank.
- Use a caption to show a label in place of the member name in a ranked table.
- Reverse the sort order in CUBESET to return bottom values, rather than trying to count from the end.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CUBEMEMBER](CUBEMEMBER.md) | Confirms that a ranked member exists in the cube. |
| [CUBESET](CUBESET.md) | Builds the sorted set that this function ranks. |
| [CUBESETCOUNT](CUBESETCOUNT.md) | Counts the members in the set, which tells you the highest rank you can request. |
| [CUBEVALUE](CUBEVALUE.md) | Returns the sales figure for the ranked member. |
| [SORT](../Lookup%20%26%20Reference/SORT.md) | Sorts a range kept in the sheet, as a non-cube alternative. |

## Official Documentation

- [Microsoft Support: CUBERANKEDMEMBER function](https://support.microsoft.com/en-us/excel/functions/cuberankedmember-function)
