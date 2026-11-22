---
domain: Spreadsheet Functions
category: Cube
subcategory: OLAP Members
purpose:
  - Data Retrieval
  - Data Validation
  - OLAP Analysis
use-case:
  - Attribute Driven Labels
  - Member Attribute Lookup
  - Product Owner Directory
related:
  - CUBEKPIMEMBER
  - CUBEMEMBER
  - CUBEVALUE
  - IFERROR
  - XLOOKUP
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/cubememberproperty-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Member Property Lookup
  - Member Attribute
tags:
  - attribute
  - cube
  - excel
  - member
  - olap
---

# CUBEMEMBERPROPERTY

## Description

**CUBEMEMBERPROPERTY** returns the value of a named property of a member in an OLAP cube. A property describes a member beyond its name, such as the manager, color or owner that the cube stores for a product. Use it to pull that attribute into a report, and to confirm that a member name exists in the cube, because the function returns an error when the member is missing.

The member is given as an MDX expression in text or as a reference to a cell that holds one. The property is also text, or a cell reference that contains the property name. Use a property name that the cube defines. Each formula returns one property for one member, so a report with many members fills the formula down a column.

CUBEMEMBERPROPERTY works only with workbook connections to a multidimensional cube. It does not work with Excel Data Models edited in Power Pivot, because those are not multidimensional cubes. It is an Excel function with no Google Sheets equivalent. While the cube query runs, the cell shows `#GETTING_DATA…`.

## Syntax

```excel
=CUBEMEMBERPROPERTY(connection, member_expression, property)
```

<!-- Image 1: Connection, Member and Property Arguments. See Images/Cube/CUBEMEMBERPROPERTY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `connection` | Yes | The name of a workbook connection to the cube, as text. |
| `member_expression` | Yes | A text string with an MDX expression for one member in the cube, or a reference to a cell that holds it. |
| `property` | Yes | The name of the property to return, as text or as a reference to a cell that contains the name. |

### Return Value

The function returns the value of the requested member property from the cube. The article describes the return value only briefly, so the data type and format depend on how the cube defines that property.

The function returns `#NAME?` when the connection is not a valid workbook connection or the OLAP server is not running, available or responding. It returns `#N/A` when the `member_expression` syntax is incorrect, the member does not exist in the cube, or a session-based object such as a calculated member or named set was referenced after its PivotTable was deleted or converted to formulas.

## Examples

The examples use a connection named `SalesCube` to a cube with a Product hierarchy that has a Category level, and members that carry an `Owner` property.

### Example 1: Return a Property for One Member

```excel
=CUBEMEMBERPROPERTY("SalesCube", "[Product].[Category].&[Gadgets]", "Owner")
```

**Result:** The Owner value that the cube stores for the Gadgets category, such as a person's name.

The property name must match the cube definition. A property name that the cube does not define returns an error instead of a blank value.

### Example 2: Read the Member and Property From Cells

```excel
=CUBEMEMBERPROPERTY("SalesCube", A2, B2)
```

**Result:** The property named in `B2` for the member expression in `A2`.

Keeping the member and property in cells lets one formula serve a whole table of members and attributes.

### Example 3: Show a Readable Message When the Member Is Missing

```excel
=IFERROR(CUBEMEMBERPROPERTY("SalesCube", A2, "Owner"), "Member not found")
```

**Result:** The Owner value for the member in `A2`, or `Member not found` when the cube does not return one.

### Example 4: Check That the Member Exists

```excel
=IF(ISERROR(CUBEMEMBERPROPERTY("SalesCube", A2, "Owner")), "Check member", "OK")
```

**Result:** `OK` when the property returns a value, or `Check member` when it returns an error.

This pattern turns the property lookup into a yes or no check that a validation column can show.

<!-- Image 2: Property Lookup Filled Down a Column. See Images/Cube/CUBEMEMBERPROPERTY.md -->

## Story Problems

### Problem 1: Product Owners for a Stock List

A product team keeps product members in column A of a sheet. Each product's owner is stored in the cube as the Owner property. The cube holds owners for Gadgets, Widgets and Cables, but not for Sensors.

| Product Member | Owner Held in Cube |
| --- | --- |
| Gadgets | Blake |
| Widgets | Avery |
| Cables | Casey |

**Task:** Fill column B with each product's owner, or `Not found` when the cube has no owner for that product.

**Solution:**

```excel
=IFERROR(CUBEMEMBERPROPERTY("SalesCube", "[Product].[Category].&["&A2&"]", "Owner"), "Not found")
```

Column A holds Gadgets, Widgets, Cables and Sensors in `A2` to `A5`, so fill the formula down from `B2` to `B5`.

**Answer:** Gadgets shows `Blake`, Widgets shows `Avery`, Cables shows `Casey`, and Sensors shows `Not found`, because the cube holds no owner for it.

<!-- Image 3: Owner Lookup Column. See Images/Cube/CUBEMEMBERPROPERTY.md -->

### Problem 2: Owner Changes Between Reports

A planner keeps the property name in cell `D1` so that the same formula can read either `Owner` or `Region Lead` from the cube. Cell `D2` holds the member expression `[Product].[Category].&[Widgets]`.

| Property Name in D1 | Value Held in Cube for Widgets |
| --- | --- |
| Owner | Avery |
| Region Lead | Emery |

**Task:** Return the value for the property named in `D1`, first with `Owner` and then with `Region Lead`.

**Solution:**

```excel
=CUBEMEMBERPROPERTY("SalesCube", $D$2, $D$1)
```

**Answer:** With `Owner` in `D1`, the result is `Avery`. Changing `D1` to `Region Lead` returns `Emery`, with no change to the formula.

## Use Cases

### Product Owner Directory

**Scenario:** A directory sheet lists product categories and must show the accountable owner for each one, pulled from the cube so it stays current.

```excel
=CUBEMEMBERPROPERTY("SalesCube", "[Product].[Category].&[Gadgets]", "Owner")
```

**Why It Works:** The owner is read from the cube's property, so a change made in the cube reaches the directory without retyping names.

### Attribute Driven Report Labels

**Scenario:** A regional report shows a manager name under each region heading, and the names change every quarter.

```excel
=IFERROR(CUBEMEMBERPROPERTY("SalesCube", "[Geography].[Region].&[East]", "Manager"), "Manager not set")
```

**Why It Works:** The label is driven by the cube, and the fallback text shows a clear gap when the cube does not hold a manager for that region.

### Membership Check Before a Pivot Summary

**Scenario:** A reviewer must confirm that every product in a pivot summary still exists in the cube before the summary is shared.

```excel
=IF(ISERROR(CUBEMEMBERPROPERTY("SalesCube", A2, "Owner")), "Remove from summary", "Keep")
```

**Why It Works:** An error from a missing member becomes a clear action for the reviewer, and the check reuses the same property the summary reads.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The connection is not a workbook connection, or the OLAP server is not running or available. | Check the connection name and confirm that the server is available. |
| `#N/A` | The MDX syntax is wrong, the member does not exist, or a session-based object was deleted. | Copy the exact unique member name, and recreate the PivotTable connection if a session object was deleted. |
| `#N/A` | The property name is not defined for that member in the cube. | Confirm the property name with the cube definition and correct its spelling. |
| `#GETTING_DATA…` | The cube query is still running. | Wait for the query to finish. This message is temporary. |
| No result | The workbook uses an Excel Data Model edited in Power Pivot, which is not a multidimensional cube. | Connect to a multidimensional cube, such as SQL Server Analysis Services. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web, and Excel for iPad, iPhone and Android | Requires a multidimensional cube connection. Power Pivot data models are not supported. |
| Google Sheets | Not available | Closest alternative: store the attribute in a column next to the member name and retrieve it with XLOOKUP. |

## Tips and Best Practices

- Put the property name in a cell so one formula can switch between attributes without editing it.
- Wrap the function in IFERROR or an ISERROR check so a missing member does not break a report.
- Confirm property names with the cube definition, because a misspelled property returns an error rather than a blank.
- Use CUBEMEMBER first when you only need to confirm that a member exists, since it is simpler than reading a property.
- Keep the member expression in a cell when it is long, because formulas with very long text are harder to audit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CUBEKPIMEMBER](CUBEKPIMEMBER.md) | Returns a KPI component, a different kind of cube attribute. |
| [CUBEMEMBER](CUBEMEMBER.md) | Confirms that a member exists before you read its property. |
| [CUBEVALUE](CUBEVALUE.md) | Aggregates a measure for the same member used as a slicer. |
| [IFERROR](../Logical/IFERROR.md) | Replaces an error from a missing member with a readable message. |
| [XLOOKUP](../Lookup%20%26%20Reference/XLOOKUP.md) | Looks up an attribute from a list kept in the sheet, as a non-cube alternative. |

## Official Documentation

- [Microsoft Support: CUBEMEMBERPROPERTY function](https://support.microsoft.com/en-us/excel/functions/cubememberproperty-function)
