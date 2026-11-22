---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Modern Lookup
purpose:
  - Data Retrieval
use-case:
  - Conditional Data Type Checks
  - Country Facts Reporting
  - Stock Field Lookups
related:
  - FILTER
  - IFERROR
  - INDEX
  - XLOOKUP
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/fieldvalue-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Data Type Field
  - Linked Field Value
tags:
  - excel
  - linked-data-types
  - lookup
---

# FIELDVALUE

## Description

**FIELDVALUE** returns one field from a linked data type in Microsoft Excel. A linked data type is a cell that holds a record from an online source, such as a stock or a geographic place, and that record has named fields such as Price or Population. FIELDVALUE takes the cell and the field name and returns the field's value.

The field name must match the data type's field name exactly. The page warns that `"Prices"` fails where the field is named `"Price"`. Putting the field name in a header cell, and pointing FIELDVALUE at that cell, lets one formula serve several fields. To list the field names for a record, select its cell and press Alt+Shift+F10.

Excel also offers a simpler way to pick fields from a linked cell. Use FIELDVALUE when the field name must come from another cell or a formula, or when the value is needed inside a condition.

## Syntax

```excel
=FIELDVALUE(value, field_name)
```

<!-- Image 1: Linked Cell and Field Name. See Images/Lookup & Reference/FIELDVALUE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The cell that holds the linked data type. |
| `field_name` | Yes | The field to return, typed in quotes such as `"Price"` or taken from a cell. It must match the data type's field name exactly. |

### Return Value

The matching field value from the linked data type. The page says the function returns all matching fields, but it does not describe how more than one field would display. If the field name does not exist, the formula returns `#FIELD!`. If the cell does not hold a linked data type, the formula returns an error.

## Examples

The results below depend on live data from the data provider, so each one describes the value rather than a fixed number.

### Example 1: A Field Named in Quotes

```excel
=FIELDVALUE(A2, "Price")
```

**Result:** the current price stored in the linked record in A2

The field name is typed in quotes, so the same formula returns the value for that field only.

### Example 2: A Field Named in a Header Cell

```excel
=FIELDVALUE(A2, B$1)
```

**Result:** the field named in B1 for the record in A2

Changing the header in B1 changes the field returned, so one formula fits every column of a table.

### Example 3: Blank Instead of an Error

```excel
=IFERROR(FIELDVALUE(A2, "Volume"), "")
```

**Result:** the volume for the record in A2, or a blank cell when the field is missing or A2 holds no linked data type

IFERROR shows a blank instead of an error, which keeps a summary table tidy when some rows are not linked.

### Example 4: Condition Based on a Field

```excel
=IF(FIELDVALUE(A2, "Price") > 100, "Review", "Hold")
```

**Result:** "Review" when the price in A2 is above 100, otherwise "Hold"

The field value feeds a condition directly, without copying the value into another cell first.

<!-- Image 2: Field Names in the Field List. See Images/Lookup & Reference/FIELDVALUE.md -->

## Story Problems

### Problem 1: Portfolio Value From Linked Prices

A small investor keeps three holdings. Each holding is a linked stock in column A, and the number of shares is in column B. The price column is filled with FIELDVALUE, and the snapshot below shows the prices at the time the sheet was written.

| Holding | Shares | Price |
| --- | --- | --- |
| Stock A | 10 | 150 |
| Stock B | 25 | 40 |
| Stock C | 4 | 300 |

**Task:** Find the total value of the three holdings using the prices in column C.

**Solution:**

```excel
=SUMPRODUCT(B2:B4, C2:C4)
```

**Answer:** `3700`. The holdings are worth 1500, 1000 and 1200, which add to 3700. The price cells would be filled with `=FIELDVALUE(A2, "Price")`, copied down, so the total updates when the data refreshes.

### Problem 2: Counting Prices Above a Limit

A watch list holds five linked stocks, and their prices are shown in column C after FIELDVALUE fills them.

| Stock | Price |
| --- | --- |
| Stock 1 | 80 |
| Stock 2 | 120 |
| Stock 3 | 95 |
| Stock 4 | 210 |
| Stock 5 | 150 |

**Task:** Count how many stocks have a price above 100.

**Solution:**

```excel
=COUNTIF(C2:C6, ">100")
```

**Answer:** `3`. Stock 2 (120), Stock 4 (210) and Stock 5 (150) are above 100.

## Use Cases

### Stock Field Lookups

**Scenario:** A portfolio sheet needs the price of each linked stock in its own column, and the header row names the field to show.

```excel
=FIELDVALUE(A2, B$1)
```

**Why It Works:** The header cell in B1 names the field, so the formula is copied across the sheet and each column returns a different field of the same record.

### Country Facts Reporting

**Scenario:** A report lists countries as linked geography cells and shows one fact per row. The formula must show a blank when a country has no value for the fact.

```excel
=IFERROR(FIELDVALUE(B2, "Population"), "Not listed")
```

**Why It Works:** The formula returns the population field when the data type has it and a clear label when it does not, so the report stays readable.

### Conditional Data Type Checks

**Scenario:** A watch sheet flags a stock for review when its price rises above a set limit.

```excel
=IF(FIELDVALUE(A2, "Price") > $F$1, "Review", "Hold")
```

**Why It Works:** The limit sits in one cell, so changing it updates every flag. The field value is used directly inside the condition.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#FIELD!` | The field name does not match the data type's field. | Press Alt+Shift+F10 on the cell, and copy the field name exactly. |
| Error on a plain cell | The referenced cell does not hold a linked data type. | Link the cell to a data type, or wrap the formula in IFERROR. |
| `#VALUE!` or no match | The field name has a typo, such as `"Prices"` for `"Price"`. | Correct the name, or point the formula at a header cell with the correct name. |
| Blank result | IFERROR returned its blank value. | Check the source cell and field name if the blank is not expected. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), and Excel Web App | Works with linked data types such as Stocks and Geography. Data types were released to Windows Microsoft 365 subscribers on March 28, 2019. |
| Google Sheets | Not available | Use INDEX with MATCH on a list you maintain, or a lookup over the values you need. |

## Tips and Best Practices

- Copy the field name from the Alt+Shift+F10 list instead of typing it, to avoid spelling errors.
- Put field names in a header row and point FIELDVALUE at those cells, so one formula serves many columns.
- Wrap FIELDVALUE in IFERROR for cells that might not be linked.
- Keep the source data type updated, because linked values change as the provider refreshes them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns rows that meet a condition, which can include linked fields once they are in cells. |
| [IFERROR](../Logical/IFERROR.md) | Replaces an error with a blank or a label, useful when some cells are not linked. |
| [INDEX](INDEX.md) | Returns a value by position from a list you maintain, a common alternative in Google Sheets. |
| [XLOOKUP](XLOOKUP.md) | Finds a value by key in a table, a different approach for records held in ranges. |

## Official Documentation

- [Microsoft Support: FIELDVALUE function](https://support.microsoft.com/en-us/excel/functions/fieldvalue-function)
