---
domain: Spreadsheet Functions
category: Cube
subcategory: OLAP Members
purpose:
  - Data Retrieval
  - Data Validation
  - OLAP Analysis
use-case:
  - Cube Member Validation
  - Report Input Checks
  - Slicer Member Lookup
related:
  - CUBEKPIMEMBER
  - CUBEMEMBERPROPERTY
  - CUBESET
  - CUBEVALUE
  - IFERROR
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/cubemember-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cube Member Check
  - Member Lookup
tags:
  - cube
  - excel
  - member
  - olap
  - validation
---

# CUBEMEMBER

## Description

**CUBEMEMBER** returns a member or a tuple from an OLAP cube. A member is a single item in a cube hierarchy, such as the East region or the Gadgets product category. A tuple is a combination of members from different hierarchies, such as East and Gadgets together. Use CUBEMEMBER to confirm that a member or tuple exists in the cube before a report depends on it, or to pass a member into another CUBE function as its argument.

The member expression is a text string written in MDX, the query language for cubes, or a cell range or array constant for a tuple. The function displays the member caption in the cell. When CUBEMEMBER appears as an argument to another CUBE function, that function uses the MDX expression, not the text shown in the CUBEMEMBER cell.

CUBEMEMBER works only with workbook connections to a multidimensional cube. It does not work with Excel Data Models edited in Power Pivot, because those are not multidimensional cubes. Google Sheets has no equivalent function. While the cube query runs, the cell shows `#GETTING_DATA…`.

## Syntax

```excel
=CUBEMEMBER(connection, member_expression, [caption])
```

<!-- Image 1: Connection, Member Expression and Caption Arguments. See Images/Cube/CUBEMEMBER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `connection` | Yes | The name of a workbook connection to the cube, as text. |
| `member_expression` | Yes | A text string with an MDX expression that returns one unique member, or a tuple given as a cell range or array constant. An expression longer than 255 characters returns `#VALUE!`, so place long text in a cell and reference that cell. |
| `caption` | No | Text to show in the cell instead of the cube's caption. For a tuple, the caption comes from the last member in the tuple. |

### Return Value

The function returns the member or tuple from the cube, displayed by its caption. Use the result to check that the member exists, or pass the function into another CUBE function.

The function returns `#NAME?` when the connection is not valid or the OLAP server is not running, available or responding. It returns `#VALUE!` when a tuple element is invalid or the expression is longer than 255 characters. It returns `#N/A` when the MDX syntax is wrong, the member does not exist, a tuple has no intersection for its values, or a set mixes members from different dimensions.

## Examples

The examples use a connection named `SalesCube` to a cube with a Geography hierarchy that has a Region level, a Product hierarchy with a Category level, and a Sales Amount measure.

### Example 1: Confirm a Region Exists

```excel
=CUBEMEMBER("SalesCube", "[Geography].[Region].&[East]")
```

**Result:** The caption of the East member, usually `East`, when the member exists in the cube.

The `&[East]` part is the member key that the cube uses. Copy the exact unique name from the cube definition, because a display name alone often does not match.

### Example 2: Set a Caption for Display

```excel
=CUBEMEMBER("SalesCube", "[Geography].[Region].&[East]", "East Region")
```

**Result:** `East Region`

The caption replaces the cube's caption in the cell, which helps when the cube uses codes or long names.

### Example 3: Show a Message When the Member Is Missing

```excel
=IFERROR(CUBEMEMBER("SalesCube", A2), "Not in cube")
```

**Result:** The member caption when `A2` holds a valid member expression, or `Not in cube` when it does not.

`IFERROR` catches both `#N/A` for a missing member and `#NAME?` for a connection problem, so the report shows one plain message.

### Example 4: Pass the Member Into CUBEVALUE

```excel
=CUBEVALUE("SalesCube", "[Measures].[Sales Amount]", CUBEMEMBER("SalesCube", "[Geography].[Region].&[East]"))
```

**Result:** The aggregated Sales Amount for the East region, as a number.

CUBEVALUE uses the MDX expression inside CUBEMEMBER, so the East slicer applies even though the cell shows only the caption.

<!-- Image 2: Member Passed Into CUBEVALUE. See Images/Cube/CUBEMEMBER.md -->

## Story Problems

### Problem 1: Checking a Region List Before a Report

A sales planner types four region names into column A of a sheet. The cube holds the members East, West, North and South, so any name outside that list will fail.

| Region in Sheet |
| --- |
| East |
| West |
| Central |
| North |

**Task:** Return each region's cube caption in column B, or the text `Not in cube` when the cube has no matching member.

**Solution:**

```excel
=IFERROR(CUBEMEMBER("SalesCube", "[Geography].[Region].&["&A2&"]"), "Not in cube")
```

Fill the formula down from B2 to B5.

**Answer:** `East`, `West`, `Not in cube`, `North`. Three of the four names match, so `Central` must be corrected before the report runs.

<!-- Image 3: Region Check Column. See Images/Cube/CUBEMEMBER.md -->

### Problem 2: Confirming a Single Product Member

A buyer types `Gadgets` into cell `E1` and wants to confirm that the product category exists before building a filter that depends on it.

| Product Category | Status |
| --- | --- |
| Accessories | Listed |
| Gadgets | Listed |
| Widgets | Listed |

**Task:** Use CUBEMEMBER with the product category in `E1` and show the caption, or `Not in cube` if it is missing.

**Solution:**

```excel
=IFERROR(CUBEMEMBER("SalesCube", "[Product].[Category].&["&E1&"]"), "Not in cube")
```

**Answer:** `Gadgets`. The category is listed in the cube, so the formula returns its caption, and the filter can use it.

## Use Cases

### Dropdown Validation for Cube Reports

**Scenario:** A report reads a region name from a dropdown in cell B2, and the report must stop with a clear message when the name is not in the cube.

```excel
=IFERROR(CUBEMEMBER("SalesCube", "[Geography].[Region].&["&B2&"]"), "Pick a valid region")
```

**Why It Works:** The dropdown value becomes part of the MDX string, and a missing region falls through to the readable message instead of an error code.

### Cube Member Captions for Labels

**Scenario:** A summary table needs friendly labels for cube codes such as region keys, without typing the labels by hand.

```excel
=CUBEMEMBER("SalesCube", "[Geography].[Region].&[N01]", "North Region")
```

**Why It Works:** The caption argument supplies the label, and the member expression still confirms the code exists, so the label cannot appear for a code that the cube does not hold.

### Feeding a Member Into a Value Lookup

**Scenario:** A monthly pack shows sales for a chosen region, where the region is confirmed once and then reused in several CUBEVALUE formulas.

```excel
=CUBEVALUE("SalesCube", "[Measures].[Sales Amount]", CUBEMEMBER("SalesCube", "[Geography].[Region].&[West]"))
```

**Why It Works:** Passing CUBEMEMBER into CUBEVALUE uses the member's MDX expression, which keeps the slicer exact even when the displayed caption differs from the key.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The connection is not a workbook connection, or the OLAP server is not running or available. | Check the connection name in the workbook and confirm that the server is available. |
| `#VALUE!` | A tuple element is invalid, or `member_expression` is longer than 255 characters. | Check the tuple, or put the long expression in a cell and reference it. |
| `#N/A` | The MDX syntax is wrong, the member does not exist, or a tuple has no intersection. | Copy the exact unique member name, including the brackets and the `&[ ]` key syntax. |
| `#GETTING_DATA…` | The cube query is still running. | Wait for the query to finish. This message is temporary. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web, and Excel for iPad, iPhone and Android | Requires a multidimensional cube connection. Power Pivot data models are not supported. |
| Google Sheets | Not available | Closest alternative: check membership with `COUNTIF` or `MATCH` against a list of valid names kept in the sheet. |

## Tips and Best Practices

- Build the member expression in a cell with `&` joins when the member comes from a dropdown, so one formula fills down a whole column.
- Store long MDX text in a cell, because a member expression longer than 255 characters returns `#VALUE!` when typed into the formula.
- Use the caption argument to shorten member names in reports without changing the member used for calculation.
- Remember that another CUBE function reads the MDX inside CUBEMEMBER, not the caption shown in its cell.
- Wrap CUBEMEMBER in IFERROR when the report must keep running while a member is missing.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CUBEKPIMEMBER](CUBEKPIMEMBER.md) | Returns a KPI component using the same connection and naming rules. |
| [CUBEMEMBERPROPERTY](CUBEMEMBERPROPERTY.md) | Returns a named property of a member, once the member is confirmed. |
| [CUBESET](CUBESET.md) | Builds a set of members that other CUBE functions can read. |
| [CUBEVALUE](CUBEVALUE.md) | Aggregates values for a member used as a slicer. |
| [IFERROR](../Logical/IFERROR.md) | Replaces a missing-member error with a readable message. |

## Official Documentation

- [Microsoft Support: CUBEMEMBER function](https://support.microsoft.com/en-us/excel/functions/cubemember-function)
