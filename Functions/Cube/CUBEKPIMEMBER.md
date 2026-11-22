---
domain: Spreadsheet Functions
category: Cube
subcategory: OLAP Members
purpose:
  - Data Retrieval
  - OLAP Analysis
use-case:
  - Executive Scorecards
  - Goal Tracking
  - KPI Dashboard Reporting
related:
  - CUBEMEMBER
  - CUBEMEMBERPROPERTY
  - CUBESET
  - CUBEVALUE
  - IFERROR
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/cubekpimember-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Key Performance Indicator Member
  - KPI Member
tags:
  - cube
  - excel
  - kpi
  - olap
---

# CUBEKPIMEMBER

## Description

**CUBEKPIMEMBER** returns a key performance indicator (KPI) from an OLAP cube and displays the KPI name in the cell. A KPI is a measurement that tracks progress toward a business target, such as monthly gross profit compared with its goal. The cube stores each KPI as a set of components: the value, the goal, the status, the trend, the weight and the current time member. The property argument selects which component the function returns.

Use CUBEKPIMEMBER when a report needs the KPI name, a goal caption or another KPI component. The function identifies the component but does not calculate a number by itself. To use a KPI value in a calculation, place CUBEKPIMEMBER inside CUBEVALUE as its member expression argument.

CUBEKPIMEMBER works only with workbook connections to SQL Server 2005 Analysis Services or later. It is an Excel function. Google Sheets has no equivalent, so a Sheets workbook needs KPI figures that are stored as ordinary values. While the cube query runs, the cell shows the temporary message `#GETTING_DATA…`.

## Syntax

```excel
=CUBEKPIMEMBER(connection, kpi_name, kpi_property, [caption])
```

<!-- Image 1: Connection, KPI Name and Property Arguments. See Images/Cube/CUBEKPIMEMBER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `connection` | Yes | The name of a workbook connection to the cube, as text. The connection must exist in the workbook. |
| `kpi_name` | Yes | The name of the KPI as defined in the cube, as text. |
| `kpi_property` | Yes | The KPI component to return: `1` or `KPIValue` for the actual value, `2` or `KPIGoal` for the target, `3` or `KPIStatus` for the state at a given moment, `4` or `KPITrend` for the value over time, `5` or `KPIWeight` for relative importance, and `6` or `KPICurrentTimeMember` for the temporal context. |
| `caption` | No | Text that appears in the cell instead of the KPI name and property. |

### Return Value

The function returns the requested KPI component and displays the KPI name in the cell. With `KPIValue` (1), only the KPI name appears in the cell. A caption, when given, replaces the name and property text.

The function returns `#NAME?` when the connection is not a valid workbook connection or the OLAP server is not running, available or responding. It returns `#N/A` when `kpi_name` or `kpi_property` is invalid, or when a session-based object is referenced after the PivotTable that uses it has been deleted or converted to formulas.

## Examples

The examples use a connection named `SalesCube` to a cube that defines a KPI named `Gross Profit KPI`.

### Example 1: Show the KPI Name

```excel
=CUBEKPIMEMBER("SalesCube", "Gross Profit KPI", 1)
```

**Result:** `Gross Profit KPI`

With `KPIValue`, the cell shows only the KPI name. This is a simple way to label a KPI on a dashboard without showing its number.

### Example 2: Show the Goal With a Caption

```excel
=CUBEKPIMEMBER("SalesCube", "Gross Profit KPI", KPIGoal, "Gross Profit Goal")
```

**Result:** `Gross Profit Goal`

The caption replaces the KPI name and property, so the cell reads as a label rather than a cube path.

### Example 3: Use the KPI Value in a Calculation

```excel
=CUBEVALUE("SalesCube", CUBEKPIMEMBER("SalesCube", "Gross Profit KPI", KPIValue))
```

**Result:** The actual gross profit value stored in the cube, as a number.

The inner function supplies the KPI component as a member expression, and CUBEVALUE returns the aggregated value for it. This is the pattern the function documentation recommends for calculations.

<!-- Image 2: KPI Value Inside CUBEVALUE. See Images/Cube/CUBEKPIMEMBER.md -->

### Example 4: Read the Arguments From Cells

```excel
=CUBEKPIMEMBER("SalesCube", $A$2, $B$2)
```

**Result:** The KPI name held in `A2`, shown with the property named in `B2`.

Keeping the KPI name and property in cells lets one formula serve several KPIs. Fill the formula down a column to label a whole scorecard.

### Example 5: Show a Readable Message When the KPI Is Missing

```excel
=IFERROR(CUBEKPIMEMBER("SalesCube", "Gross Profit KPI", KPIGoal), "KPI not found")
```

**Result:** The goal caption when the KPI exists, or `KPI not found` when the cube does not return it.

## Story Problems

### Problem 1: Monthly Profit Against Goal

A store manager reads the Monthly Gross Profit KPI from the company cube. For the latest month, the cube holds these components:

| KPI Component | Amount |
| --- | --- |
| Value | 84000 |
| Goal | 90000 |

**Task:** Calculate how far the actual value is from the goal, where a negative number means the store is below goal.

**Solution:**

```excel
=CUBEVALUE("SalesCube", CUBEKPIMEMBER("SalesCube", "Monthly Gross Profit", KPIValue)) - CUBEVALUE("SalesCube", CUBEKPIMEMBER("SalesCube", "Monthly Gross Profit", KPIGoal))
```

**Answer:** `-6000`, because 84000 minus 90000 is -6000. The store is 6000 below its goal.

<!-- Image 3: Monthly Profit Against Goal Worksheet. See Images/Cube/CUBEKPIMEMBER.md -->

### Problem 2: Scorecard Goal Label

A scorecard lists the Customer Retention KPI in a row. The row needs a label that shows the goal, not the name.

| KPI Name | Property Code | Label |
| --- | --- | --- |
| Customer Retention | 2 | Retention Goal |

**Task:** Return the goal for Customer Retention with the label from column C as the caption.

**Solution:**

```excel
=CUBEKPIMEMBER("SalesCube", A2, B2, C2)
```

**Answer:** `Retention Goal`. The caption in `C2` replaces the KPI name and property in the cell.

## Use Cases

### Executive Scorecard Labels

**Scenario:** A monthly scorecard shows each KPI name next to its actual value and goal, and the names must match the cube definitions exactly.

```excel
=CUBEKPIMEMBER("SalesCube", "Gross Profit KPI", KPIGoal, "Gross Profit Goal")
```

**Why It Works:** The KPI name comes from the cube, so the scorecard label cannot drift from the definition. The caption keeps the displayed text readable.

### Goal Tracking With Actual Values

**Scenario:** A regional lead needs the actual value and the goal side by side, plus the gap between them.

```excel
=CUBEVALUE("SalesCube", CUBEKPIMEMBER("SalesCube", "Gross Profit KPI", KPIValue)) - CUBEVALUE("SalesCube", CUBEKPIMEMBER("SalesCube", "Gross Profit KPI", KPIGoal))
```

**Why It Works:** Each KPI component is pulled through CUBEVALUE, so both numbers come from the same cube. A negative gap means the KPI is below goal.

### KPI Dashboard Reporting

**Scenario:** A dashboard sheet holds a list of KPI names in column A and shows each KPI value, but a query may be slow or unavailable.

```excel
=IFERROR(CUBEKPIMEMBER("SalesCube", A2, KPIValue), "Loading or missing")
```

**Why It Works:** `IFERROR` shows a plain message when the query is unavailable, so the dashboard never displays a raw error code.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The connection name is not a workbook connection, or the OLAP server is not running or available. | Check the connection name in the workbook and confirm the server is available. |
| `#N/A` | `kpi_name` does not match a KPI in the cube, or `kpi_property` is not a valid component. | Use the exact KPI name from the cube and a property from 1 to 6 or its name. |
| `#N/A` | A session-based object was referenced after its PivotTable was deleted or converted to formulas. | Rebuild the PivotTable connection and refresh the formulas. |
| `#GETTING_DATA…` | The cube query has not returned data yet. | Wait for the query to finish. This message is temporary and is not an error. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web, and Excel for iPad, iPhone and Android | Requires a connection to SQL Server 2005 Analysis Services or later. |
| Google Sheets | Not available | Closest alternative: keep KPI figures as values in the sheet and summarize them with SUMIFS or a pivot table. |

## Tips and Best Practices

- Use the names `KPIValue`, `KPIGoal` and `KPIStatus` instead of their numbers so the formula is easy to read.
- Wrap the function in CUBEVALUE when you need a number, because the KPI name alone is what appears for `KPIValue`.
- Store the KPI name in a cell and reference it, so a renamed KPI needs one change instead of many formulas.
- Add IFERROR around KPI formulas on dashboards so a missing or unavailable KPI shows a readable message.
- Check the KPI names with the cube owner before you build a report, because a misspelled name returns `#N/A`.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CUBEMEMBER](CUBEMEMBER.md) | Confirms that a member exists in the cube, using the same connection. |
| [CUBEMEMBERPROPERTY](CUBEMEMBERPROPERTY.md) | Returns a named property of a member rather than a KPI component. |
| [CUBESET](CUBESET.md) | Builds a set of members for ranking or counting. |
| [CUBEVALUE](CUBEVALUE.md) | Returns the aggregated value, which is how you calculate with a KPI component. |
| [IFERROR](../Logical/IFERROR.md) | Shows a readable message when the KPI cannot be retrieved. |

## Official Documentation

- [Microsoft Support: CUBEKPIMEMBER function](https://support.microsoft.com/en-us/excel/functions/cubekpimember-function)
