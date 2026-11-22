---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Aggregation
use-case:
  - Defect Share Reporting
  - Product Mix Shares
  - Regional Revenue Share
related:
  - ROUND
  - SUM
  - SUMIFS
  - SUMPRODUCT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/percentof-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Percent Of Total
tags:
  - excel
  - percentage
  - share-of-total
---

# PERCENTOF

## Description

**PERCENTOF** returns the share that a subset of values makes up of the full set. It adds the values in the subset, divides by the sum of all the values, and returns the result as a proportion. For example, if a subset adds up to 250 and the full set adds up to 540, PERCENTOF returns about 0.4630, which displays as 46.3% when the cell is formatted as a percentage.

Use PERCENTOF when you want the share of a total in one formula without writing the sum twice. Microsoft describes the function as logically equivalent to SUM(subset) / SUM(all), so the two formulas give the same answer. PERCENTOF reads more clearly when a report asks "what part of the whole is this?"

PERCENTOF is available only in Excel for Microsoft 365, according to the Microsoft Applies To list. The Google Sheets help does not list it. In workbooks that must work in older Excel versions or in Sheets, use SUM with division instead.

## Syntax

```excel
=PERCENTOF(data_subset, data_all)
```

<!-- Image 1: Subset and Full Set Ranges. See Images/Math & Trig/PERCENTOF.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `data_subset` | Yes | The values that form the part you want to measure. It can be a range, a single cell, or an array. |
| `data_all` | Yes | The values that form the whole. It should include every value in `data_subset`, or the share can exceed 100%. |

### Return Value

A proportion: the sum of `data_subset` divided by the sum of `data_all`. Microsoft does not state a display format, so format the cell as a percentage when you want to show 46.3% rather than 0.463. Microsoft's help page does not list specific error conditions.

## Examples

Each example uses the product sales in `B2:B7`: 120, 80, 50, 150, 100, and 40. The full set adds to 540.

### Example 1: Share of Three Products

```excel
=PERCENTOF(B2:B4, B2:B7)
```

**Result:** `0.4630`

The subset `B2:B4` adds to 250, and 250 / 540 = 0.4630. Format the cell as a percentage to show 46.3%.

### Example 2: Share of One Cell

```excel
=PERCENTOF(B5, B2:B7)
```

**Result:** `0.2778`

The single value 150 is 27.8% of the full set of 540.

<!-- Image 2: Subset Within the Full Set. See Images/Math & Trig/PERCENTOF.md -->

### Example 3: Same Result With SUM

```excel
=SUM(B2:B4) / SUM(B2:B7)
```

**Result:** `0.4630`

This version matches Example 1 and works in any version of Excel and in Google Sheets.

## Story Problems

### Problem 1: Furniture Mix in a Quarter

A furniture store records quarterly sales by product in `B2:B7`. The chairs, desks, and lamps are listed first, followed by the tables, shelves, and stools.

| Product | Sales (Units) |
| --- | --- |
| Chairs | 120 |
| Desks | 80 |
| Lamps | 50 |
| Tables | 150 |
| Shelves | 100 |
| Stools | 40 |

**Task:** Calculate the share of total units sold that came from chairs, desks, and lamps.

**Solution:**

```excel
=PERCENTOF(B2:B4, B2:B7)
```

**Answer:** `0.4630`, or 46.3% when formatted as a percentage. Chairs, desks, and lamps sold 250 units out of 540 in total.

### Problem 2: Defect Share on a Production Line

A plant records defects by line in `B2:B5`: Line A had 4, Line B had 2, Line C had 3, and Line D had 1. Lines A and B run the same product, and the manager wants their share of all defects.

| Line | Defects |
| --- | --- |
| Line A | 4 |
| Line B | 2 |
| Line C | 3 |
| Line D | 1 |

**Task:** Calculate the share of defects that came from Lines A and B.

**Solution:**

```excel
=PERCENTOF(B2:B3, B2:B5)
```

**Answer:** `0.6`, or 60%. Lines A and B logged 6 of the 10 defects.

<!-- Image 3: Defect Share Results Panel. See Images/Math & Trig/PERCENTOF.md -->

## Use Cases

### Defect Share Reporting

**Scenario:** A quality team reports what share of defects comes from one shift or one line each week.

```excel
=PERCENTOF(ShiftDefects, AllDefects)
```

**Why It Works:** The formula keeps the share tied to the source ranges, so it updates when new defect counts are entered.

### Product Mix Shares

**Scenario:** A sales manager wants to show each product family's share of total units.

```excel
=PERCENTOF(FamilyUnits, TotalUnits)
```

**Why It Works:** Each family's share is calculated against the same total, so the shares add up to 100% when every family is included.

### Regional Revenue Share

**Scenario:** A finance team reports the share of revenue that comes from a subset of regions.

```excel
=PERCENTOF(RegionRevenue, AllRevenue)
```

**Why It Works:** The denominator includes every region, so the result is the share of the whole company. Confirm that the subset range is contained within the full range.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Share greater than 100% | `data_subset` includes values that are not in `data_all`. | Make sure the full range contains every value in the subset. |
| Shows 0.463 instead of 46.3% | The cell has a number format rather than a percentage format. | Format the cell as a percentage. |
| `#NAME?` | The formula is used in a version of Excel that does not include PERCENTOF. | Use SUM(subset) / SUM(all) instead. |
| Unexpected value | A subset or total range includes text or blank cells. | Check the source ranges and correct the entries. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 only, according to the Applies To list | Returns a proportion. Format the cell as a percentage to display the share. |
| Google Sheets | Not available | Use `=SUM(subset) / SUM(all)` for the same result. |

## Tips and Best Practices

- Use the full range for `data_all`, and make sure the subset is a part of that range.
- Format the result as a percentage, and round it with ROUND only when the report needs fewer decimals.
- Use SUMIFS inside the subset argument when the subset depends on a condition, such as a region name.
- Keep the calculation in its own column so the share can be checked against the total.
- Use the SUM form when the workbook must open in Google Sheets or in an older Excel version.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SUM](SUM.md) | The method PERCENTOF follows; SUM(subset) / SUM(all) gives the same answer in any version. |
| [SUMIFS](SUMIFS.md) | Builds a conditional subset total that can feed a share calculation. |
| [SUMPRODUCT](SUMPRODUCT.md) | Calculates weighted totals when each value needs its own weight. |
| [ROUND](ROUND.md) | Rounds the share to a set number of decimal places for display. |

## Official Documentation

- [Microsoft Support: PERCENTOF function](https://support.microsoft.com/en-us/excel/functions/percentof-function)
