---
domain: Spreadsheet Functions
category: Cube
subcategory: OLAP Values
purpose:
  - Aggregation
  - Data Retrieval
  - OLAP Analysis
use-case:
  - Budget Variance Reporting
  - Cube Totals in Summary Tables
  - Regional Sales Totals
related:
  - CUBEKPIMEMBER
  - CUBEMEMBER
  - CUBESET
  - CUBESETCOUNT
  - IFERROR
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/cubevalue-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cube Aggregate
  - Cube Total
tags:
  - aggregation
  - cube
  - excel
  - olap
  - slicer
---

# CUBEVALUE

## Description

**CUBEVALUE** returns an aggregated value from an OLAP cube. You supply the connection, then one or more member expressions that act as slicers. A slicer narrows the part of the cube that is summed, such as the East region or the year 2025. If you do not name a measure, the cube's default measure is used. The member expressions can be a member, a tuple, a set created with CUBESET, or a KPI component from CUBEKPIMEMBER.

Use CUBEVALUE for totals and comparisons that come straight from the cube: regional sales, budget against actual, or a KPI value. The function does not calculate on the sheet, so the number reflects the cube's own definitions. For a report, keep each slicer in its own cell and fill the formula down or across.

CUBEVALUE works only with workbook connections to a multidimensional cube. It is an Excel function with no Google Sheets equivalent. When a cube returns no value for a combination, CUBEVALUE returns a zero-length string, which can break later arithmetic. While the query runs, the cell shows `#GETTING_DATA…`.

## Syntax

```excel
=CUBEVALUE(connection, [member_expression1], [member_expression2], ...)
```

<!-- Image 1: Connection and Slicer Arguments. See Images/Cube/CUBEVALUE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `connection` | Yes | The name of a workbook connection to the cube, as text. |
| `member_expression1` | No | An MDX expression that returns a member or tuple, or a set created with CUBESET, used as a slicer. If no measure appears among the expressions, the cube's default measure is used. |
| `member_expression2` and later | No | More slicers, such as a year or a product category, that narrow the aggregate. Each one is a text string, a cell reference or a CUBE function. |

### Return Value

The function returns the aggregated value for the slicers you give. A null result from the cube is returned as a zero-length string, and arithmetic on that string returns `#VALUE!`.

The function returns `#NAME?` when the connection is not valid or the OLAP server is not running, available or responding. It returns `#VALUE!` when a tuple element is invalid. It returns `#N/A` when the MDX syntax is incorrect, the member does not exist, a tuple has no intersection for its values, a set mixes dimensions, or a session-based object was referenced after its PivotTable was deleted or converted to formulas.

## Examples

The examples use a connection named `SalesCube` to a cube with a Geography hierarchy, a Product hierarchy, a Date hierarchy and the measures Sales Amount and Budget Sales.

### Example 1: Total Sales for One Region

```excel
=CUBEVALUE("SalesCube", "[Measures].[Sales Amount]", "[Geography].[Region].&[East]")
```

**Result:** The aggregated Sales Amount for the East region, as a number.

The measure is the first slicer and the region is the second. The result is whatever the cube aggregates for that combination.

### Example 2: Fill a Region Column From Cells

Cell `B1` holds the measure expression `[Measures].[Sales Amount]`, and column A holds region expressions such as `[Geography].[Region].&[East]` in `A2`.

```excel
=CUBEVALUE("SalesCube", $B$1, A2)
```

**Result:** The Sales Amount for the region in `A2`. Filling the formula down gives one total for each region in column A.

### Example 3: Replace a Zero-Length Result With Zero

```excel
=IF(CUBEVALUE("SalesCube", "[Measures].[Sales Amount]", A2)="", 0, CUBEVALUE("SalesCube", "[Measures].[Sales Amount]", A2))
```

**Result:** The Sales Amount for the region in `A2`, or `0` when the cube returns no value for it.

The article recommends this test when the value will be used in arithmetic, because a zero-length string breaks calculations.

### Example 4: Show a Message When the Member Is Missing

```excel
=IFERROR(CUBEVALUE("SalesCube", "[Measures].[Sales Amount]", A2), "Not in cube")
```

**Result:** The Sales Amount for the member in `A2`, or `Not in cube` when the member cannot be read.

<!-- Image 2: Region Totals Filled Down a Column. See Images/Cube/CUBEVALUE.md -->

## Story Problems

### Problem 1: East Region Total and Share

A sales analyst needs the East region total from the cube. The cube holds these totals by region:

| Region | Sales Amount |
| --- | --- |
| East | 14200 |
| West | 9800 |
| North | 6400 |

**Task:** Use CUBEVALUE to return the East total, then state the East share of the three regions combined.

**Solution:**

```excel
=CUBEVALUE("SalesCube", "[Measures].[Sales Amount]", "[Geography].[Region].&[East]")
```

**Answer:** `14200` for East. The three regions total 30400, so East is about 46.7 percent of the combined sales.

<!-- Image 3: Region Total and Share Summary. See Images/Cube/CUBEVALUE.md -->

### Problem 2: Actual Sales Against Budget

A regional controller compares actual sales with the budget for 2025. The cube holds these values for the year:

| Measure | Value for 2025 |
| --- | --- |
| Actual Sales | 52000 |
| Budget Sales | 58000 |

**Task:** Use two CUBEVALUE formulas to calculate actual minus budget, where a negative result means sales are below budget.

**Solution:**

```excel
=CUBEVALUE("SalesCube", "[Measures].[Actual Sales]", "[Date].[Year].&[2025]") - CUBEVALUE("SalesCube", "[Measures].[Budget Sales]", "[Date].[Year].&[2025]")
```

**Answer:** `-6000`, because 52000 minus 58000 is -6000. Sales are 6000 below budget for 2025.

## Use Cases

### Regional Sales Totals

**Scenario:** A monthly pack shows the sales total for each region, and the totals must match the cube exactly.

```excel
=CUBEVALUE("SalesCube", "[Measures].[Sales Amount]", "[Geography].[Region].&[West]")
```

**Why It Works:** The total is aggregated by the cube, so the pack agrees with the cube's own figures without a separate sum on the sheet.

### Budget Variance Reporting

**Scenario:** A finance team reviews actual sales against budget for each region each quarter.

```excel
=CUBEVALUE("SalesCube", "[Measures].[Actual Sales]", A2) - CUBEVALUE("SalesCube", "[Measures].[Budget Sales]", A2)
```

**Why It Works:** Both values use the same slicer in `A2`, so the difference compares like with like. A negative result flags a shortfall.

### Cube Totals in Summary Tables

**Scenario:** A summary table lists several regions with their totals, and the table must not show errors when a region has no data.

```excel
=IF(CUBEVALUE("SalesCube", "[Measures].[Sales Amount]", A2)="", 0, CUBEVALUE("SalesCube", "[Measures].[Sales Amount]", A2))
```

**Why It Works:** The zero-length test turns a missing value into `0`, so the column can be summed without `#VALUE!` errors.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The connection is not a workbook connection, or the OLAP server is not running or available. | Check the connection name and confirm that the server is available. |
| `#VALUE!` | A tuple element is invalid, or a zero-length result was used in arithmetic. | Check the tuple, and guard the formula with an IF test on the empty string. |
| `#N/A` | The MDX syntax is wrong, the member does not exist, or the tuple has no intersection. | Copy the exact unique member name and check the hierarchy levels. |
| Blank or zero-length result | The cube returns no value for that slicer combination. | Guard with an IF test, or confirm that the combination holds data in the cube. |
| `#GETTING_DATA…` | The cube query is still running. | Wait for the query to finish. This message is temporary. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web, and Excel for iPad, iPhone and Android | Requires a multidimensional cube connection. SUM ignores zero-length strings in a range. |
| Google Sheets | Not available | Closest alternative: summarize the figures in the sheet with SUMIFS or a pivot table on imported values. |

## Tips and Best Practices

- Put each slicer in a cell and reference the cell, so one formula fills down a report and each row changes only its slicer.
- Test for the empty string before doing arithmetic on a single CUBEVALUE result.
- Use CUBEMEMBER or CUBEKPIMEMBER as a slicer when the member or KPI component must be confirmed first.
- Name the measure explicitly, because a formula with no measure uses the cube's default measure, which may not be the one you intended.
- Use IFERROR to label missing members, so a summary table reads clearly when a slicer is wrong.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CUBEKPIMEMBER](CUBEKPIMEMBER.md) | Supplies a KPI component as a slicer, so the value can be used in a calculation. |
| [CUBEMEMBER](CUBEMEMBER.md) | Supplies a confirmed member as a slicer. |
| [CUBESET](CUBESET.md) | Supplies a set of members as a slicer. |
| [CUBESETCOUNT](CUBESETCOUNT.md) | Counts the members in a set used as a slicer. |
| [IFERROR](../Logical/IFERROR.md) | Replaces an error from a missing member with a readable message. |

## Official Documentation

- [Microsoft Support: CUBEVALUE function](https://support.microsoft.com/en-us/excel/functions/cubevalue-function)
