---
domain: Spreadsheet Functions
category: Cube
subcategory: OLAP Sets
purpose:
  - Data Retrieval
  - OLAP Analysis
  - Sorting and Filtering
use-case:
  - Bottom Performer Review
  - Reusable Set Definitions
  - Sorted Member Lists
related:
  - CUBEMEMBER
  - CUBERANKEDMEMBER
  - CUBESETCOUNT
  - CUBEVALUE
  - SORT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/cubeset-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Calculated Set
  - Set Expression
tags:
  - cube
  - excel
  - olap
  - set
  - sorting
---

# CUBESET

## Description

**CUBESET** defines a calculated set of members or tuples by sending a set expression to the OLAP server, which creates the set and returns it to Excel. A set is an ordered list of cube members, such as every region or every sales rep. The function can also sort the set by a measure, alphabetically or in natural order, before it is used.

A CUBESET result is not a single value. Other CUBE functions read it: CUBERANKEDMEMBER returns the nth member of the set, CUBESETCOUNT returns the number of members, and CUBEVALUE uses it as a slicer. Put the CUBESET formula in one cell and reference that cell from several formulas to avoid repeating a long expression.

CUBESET works only with workbook connections to a multidimensional cube. It is an Excel function with no Google Sheets equivalent. While the cube query runs, the cell shows `#GETTING_DATA…`.

## Syntax

```excel
=CUBESET(connection, set_expression, [caption], [sort_order], [sort_by])
```

<!-- Image 1: Set Expression and Sort Arguments. See Images/Cube/CUBESET.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `connection` | Yes | The name of a workbook connection to the cube, as text. It must be a valid connection stored in the workbook. |
| `set_expression` | Yes | A text string with an MDX set expression that returns members or tuples, or a cell reference to a range that holds them. |
| `caption` | No | Text shown in the cell in place of the cube's caption. |
| `sort_order` | No | An integer from 0 to 6. `0` keeps the existing order and ignores `sort_by`. `1` sorts ascending by `sort_by` and `2` sorts descending by `sort_by`; both require `sort_by`. `3` and `4` sort alphabetically ascending and descending, `5` and `6` sort in natural order ascending and descending, and these ignore `sort_by`. For alphabetical sorts of tuples, the last element of each tuple is used. The default is `0`. |
| `sort_by` | No | A text string naming the value to sort by, such as a measure. Required when `sort_order` is `1` or `2`. |

### Return Value

The function returns a set of members or tuples for other CUBE functions to use. The article describes it as a set created on the server and returned to Excel, and it does not describe a single display value.

The function returns `#NAME?` when the connection is not valid or the OLAP server is not running, available or responding. It returns `#N/A` when the `set_expression` syntax is incorrect, or the set contains members from different dimensions. It can also return `#N/A` when a session-based object is referenced after its PivotTable is deleted or converted to formulas. It returns `#VALUE!` when `set_expression` is longer than 255 characters, or when `sort_order` is `1` or `2` and `sort_by` is missing.

## Examples

The examples use a connection named `SalesCube` to a cube with Geography, Product, Rep and Store hierarchies and a Sales Amount measure.

### Example 1: Define a Set of Regions

```excel
=CUBESET("SalesCube", "{[Geography].[Region].children}")
```

**Result:** A set of the region members, held for other CUBE functions. The cell is not read as one number.

Pass the cell to CUBESETCOUNT to count the regions, or to CUBERANKEDMEMBER to return one of them.

### Example 2: Sort Reps by Sales, Highest First

```excel
=CUBESET("SalesCube", "{[Rep].[Name].children}", "Reps by Sales", 2, "[Measures].[Sales Amount]")
```

**Result:** A set of reps ordered from the highest Sales Amount to the lowest, with the caption `Reps by Sales`.

### Example 3: Sort Categories Alphabetically

```excel
=CUBESET("SalesCube", "{[Product].[Category].children}", "Categories", 3)
```

**Result:** A set of product categories in alphabetical order. No `sort_by` is needed for this sort type.

### Example 4: Read a Long Expression From a Cell

```excel
=CUBESET("SalesCube", $A$2, "Custom Set", 1, "[Measures].[Sales Amount]")
```

**Result:** A set built from the expression in `A2`, sorted from the lowest Sales Amount to the highest.

An expression longer than 255 characters cannot be typed into the formula, so it goes in a cell instead. The cell can hold up to 32,767 characters.

<!-- Image 2: Sorted Set Versus Cube Order. See Images/Cube/CUBESET.md -->

## Story Problems

### Problem 1: Lowest Selling Store

A retail manager wants the store with the lowest sales. The cube returns these totals:

| Store | Sales Amount |
| --- | --- |
| Harbor | 8200 |
| Lake | 9100 |
| Summit | 7600 |
| Valley | 6400 |

**Task:** Sort the stores from lowest to highest sales, then return the first store in that order.

**Solution:**

```excel
=CUBERANKEDMEMBER("SalesCube", CUBESET("SalesCube", "{[Store].[Name].children}", "Stores", 1, "[Measures].[Sales Amount]"), 1)
```

**Answer:** `Valley`, with 6400 in sales. Valley is the lowest of the four totals.

<!-- Image 3: Ascending Set Returning the First Member. See Images/Cube/CUBESET.md -->

### Problem 2: First Category Alphabetically

A buyer lists five product categories in the cube: Cables, Accessories, Gadgets, Widgets and Sensors. The buyer wants the category that comes first alphabetically.

| Product Category |
| --- |
| Cables |
| Accessories |
| Gadgets |
| Widgets |
| Sensors |

**Task:** Use an alphabetical CUBESET and return the first member.

**Solution:**

```excel
=CUBERANKEDMEMBER("SalesCube", CUBESET("SalesCube", "{[Product].[Category].children}", "Categories", 3), 1)
```

**Answer:** `Accessories`. Sorted alphabetically, the order is Accessories, Cables, Gadgets, Sensors and Widgets, so Accessories comes first.

## Use Cases

### Bottom Performer Review

**Scenario:** A regional manager reviews the store with the lowest sales first, then works up the list each month.

```excel
=CUBESET("SalesCube", "{[Store].[Name].children}", "Stores", 1, "[Measures].[Sales Amount]")
```

**Why It Works:** An ascending sort on the Sales Amount measure puts the lowest store first, and CUBERANKEDMEMBER can return any position in the list.

### Reusable Set Definitions

**Scenario:** A pack needs the same sorted list of reps in three places: a top seller, a count and a total.

```excel
=CUBESET("SalesCube", "{[Rep].[Name].children}", "Reps", 2, "[Measures].[Sales Amount]")
```

**Why It Works:** The set is defined once in a cell, and each dependent formula refers to that cell, so a change to the sort applies everywhere.

### Sorted Member Lists

**Scenario:** A planning sheet needs product categories in alphabetical order for a list that other people read.

```excel
=CUBESET("SalesCube", "{[Product].[Category].children}", "Categories", 3)
```

**Why It Works:** The alphabetical sort does not need a measure, so the list stays in a predictable order even when the sales figures change.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The connection is not a workbook connection, or the OLAP server is not running or available. | Check the connection name and confirm that the server is available. |
| `#N/A` | The set expression syntax is wrong, or the set contains members from different dimensions. | Correct the MDX and keep every member in the set from one dimension. |
| `#VALUE!` | `sort_order` is `1` or `2` but `sort_by` is missing. | Add the measure name to `sort_by`. |
| `#VALUE!` | `set_expression` is longer than 255 characters. | Place the expression in a cell and reference that cell. |
| `#GETTING_DATA…` | The cube query is still running. | Wait for the query to finish. This message is temporary. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web, and Excel for iPad, iPhone and Android | Requires a multidimensional cube connection. Set expressions use MDX. |
| Google Sheets | Not available | Closest alternative: sort the list in the sheet with SORT, or use SORTN to limit the rows returned. |

## Tips and Best Practices

- Store long set expressions in a cell and reference the cell, so the formula stays short and one definition feeds several formulas.
- Use `sort_order` 0 when you need the cube's own order, because it is the default and the cheapest choice.
- Sort the set before ranking it with CUBERANKEDMEMBER, because rank depends on the order.
- Give each set a caption so the cell is readable on a report.
- Remember that `sort_order` 1 and 2 require `sort_by`, or the formula returns `#VALUE!`.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CUBEMEMBER](CUBEMEMBER.md) | Confirms that a single member exists, where a set holds many. |
| [CUBERANKEDMEMBER](CUBERANKEDMEMBER.md) | Returns one member from the sorted set by position. |
| [CUBESETCOUNT](CUBESETCOUNT.md) | Counts the members in the set. |
| [CUBEVALUE](CUBEVALUE.md) | Uses the set as a slicer to aggregate values. |
| [SORT](../Lookup%20%26%20Reference/SORT.md) | Sorts a list kept in the sheet, as a non-cube alternative. |

## Official Documentation

- [Microsoft Support: CUBESET function](https://support.microsoft.com/en-us/excel/functions/cubeset-function)
