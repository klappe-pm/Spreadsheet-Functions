---
domain: Spreadsheet Functions
category: Web
subcategory: Google Data Services
purpose:
  - Data Import
  - Data Retrieval
use-case:
  - Consolidated Regional Totals
  - Department Data Distribution
  - Monthly Report Pulls
related:
  - FILTER
  - IMPORTDATA
  - IMPORTHTML
  - INDEX
  - QUERY
level: 2
source:
  - https://support.google.com/docs/answer/3093340
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cross Spreadsheet Import
  - Import Range
tags:
  - cross-spreadsheet
  - data-import
  - permissions
  - sheets
---

# IMPORTRANGE

## Description

**IMPORTRANGE** copies a range of cells from another Google Sheets file into the current sheet. The link is live. When the source changes, open destination files reload the imported values, and the function checks for updates about once an hour while the destination is open. Use it to keep a summary sheet current without copying values by hand.

Before a new connection works, access must be granted. The first time a destination pulls from a new source, the formula shows `#REF!` with an Allow Access prompt. If you own the source, click Allow Access. If you do not own it, request access from the owner, who must approve it. Once access is granted, any editor of the destination can import from any part of the source. The access lasts until the person who granted it is removed from the source.

Use IMPORTRANGE for data that lives in Google Sheets. For a CSV or TSV file on the web, use IMPORTDATA. For a web page's table, use IMPORTHTML.

IMPORTRANGE is a Google Sheets function. Excel has no single equivalent formula, as described under Platform Differences.

## Syntax

```excel
=IMPORTRANGE(spreadsheet_url, range_string)
```

<!-- Image 1: Source File, Range String and Destination. See Images/Web/IMPORTRANGE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `spreadsheet_url` | Yes | The URL of the source spreadsheet. Enter it in quotes or as a reference to a cell that holds the URL. |
| `range_string` | Yes | The range to import, in the form `Sheet!Range`, such as `"Sales!A1:D10"`. The sheet name is optional and defaults to the first sheet. The argument also accepts a named range, such as `Sales_total`, or a table column, such as `DeptSales[Sales Amount]`. |

### Return Value

The values and formula results from the source range, placed in the destination starting at the cell that holds the formula. The imported area needs empty cells below and to the right of the formula. Formatting, validation rules and comments are not imported.

## Examples

### Example 1: Basic Import From Another File

```excel
=IMPORTRANGE("https://docs.google.com/spreadsheets/d/example-source-id","Sales!A1:D10")
```

**Result:** A block of 10 rows and 4 columns with the values from `Sales!A1:D10` in the source file.

The first argument is the full address of the source file, and the second names the sheet and range.

### Example 2: Sheet Name Omitted

With `A2` holding the source file's URL:

```excel
=IMPORTRANGE(A2,"B2:F40")
```

**Result:** The range `B2:F40` from the first sheet of the source file.

When the sheet name is left out, the function uses the first sheet, so check that it is the sheet you want.

### Example 3: Open-Ended Range

```excel
=IMPORTRANGE(A2,"Orders!A2:D")
```

**Result:** Every row from row 2 down in columns A to D of the Orders sheet, up to the last row that holds data.

An open-ended range grows as new rows are added to the source.

### Example 4: Named Range

```excel
=IMPORTRANGE(A2,"Sales_total")
```

**Result:** The values in the named range `Sales_total` from the source file.

A named range keeps working if the cells it covers move within the source.

<!-- Image 2: A Filtered Import Using QUERY. See Images/Web/IMPORTRANGE.md -->

### Example 5: Filter the Import With QUERY

```excel
=QUERY(IMPORTRANGE(A2,"Orders!A1:F"),"select Col1, Col4 where Col4 > 1000",1)
```

**Result:** Columns 1 and 4 for the rows where column 4 is above 1000, with the header row kept.

QUERY refers to the imported columns as Col1, Col2 and so on. The final 1 tells QUERY that the first row is a header.

### Example 6: Monthly Sheet Chosen by Date

```excel
=IMPORTRANGE(A2,TEXT(TODAY(),"mmmm yyyy")&"!A1:D50")
```

**Result:** The cells from `A1:D50` on the source sheet named for the current month, such as `November 2026`, when the source has a sheet with that name.

TODAY is allowed in the range string, which lets the formula follow a monthly sheet naming pattern.

## Story Problems

### Problem 1: Rows 2 to 500 From an Orders Sheet

An operations team keeps orders in a source file. Row 1 holds headers, and the data for the first 499 orders is in rows 2 to 500 of columns A to D on the Orders sheet. The source URL is in `B1`.

**Task:** Write a formula that imports exactly those rows and columns, then state how many rows the import returns.

**Solution:**

```excel
=IMPORTRANGE(B1,"Orders!A2:D500")
```

**Answer:** The import returns `499` rows and 4 columns, because `500 - 2 + 1` equals 499.

### Problem 2: Total of Twelve Monthly Values

A finance team imports the twelve monthly values from the `Totals` sheet of a source file. The source cells `B2:B13` hold these values: 1200, 950, 1100, 1300, 1250, 980, 1400, 1150, 1020, 1330, 1275 and 1500. The source URL is in `B1`.

**Task:** Write a formula that returns the annual total of the imported values.

**Solution:**

```excel
=SUM(IMPORTRANGE(B1,"Totals!B2:B13"))
```

**Answer:** `14455`. The twelve values add up to 14,455.

## Use Cases

### Consolidated Regional Totals

**Scenario:** A group finance team keeps one file for each region. Each regional file has a summary total in cell `B10`, and the group needs the combined total in one place.

```excel
=SUM(IMPORTRANGE(A2,"Summary!B10"),IMPORTRANGE(A3,"Summary!B10"),IMPORTRANGE(A4,"Summary!B10"))
```

**Why It Works:** Each IMPORTRANGE reads the same cell from a different regional file, and SUM adds the three values. Each regional file's URL sits in its own cell, so a region can be replaced without rewriting the formula.

### Department Data Distribution

**Scenario:** A central team keeps a master employee list, and each department needs the names and titles of its own staff in its own file.

```excel
=QUERY(IMPORTRANGE(A2,"Employees!A1:M"),"select Col1, Col2, Col5 where Col3 = 'Engineering'",1)
```

**Why It Works:** The formula imports the list, and QUERY keeps only the columns and rows the department needs. Share only the columns needed, because the destination can read every value it imports.

### Monthly Report Pulls

**Scenario:** A sales operations team stores each month in its own sheet of a source file, and the monthly report should always show the current month.

```excel
=IMPORTRANGE(A2,TEXT(TODAY(),"mmmm yyyy")&"!A1:D50")
```

**Why It Works:** The sheet name is built from today's date, so the report points to the current month's sheet without any edits. Check that every month has a sheet with the exact name the formula builds.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#REF!` with an Allow Access prompt | Access to the source has not been granted yet. | Click the cell and choose Allow Access. If you do not own the source, request access and wait for the owner. |
| Permissions message | You do not have access to the source. | Open the source file, request access, and wait for the owner to approve it. |
| `Loading...` that does not finish | Usage limits are reached, which can happen with too many import calls. | Reduce the number of IMPORTRANGE calls, combine them where possible, and import only the rows and columns needed. |
| Error after adding NOW, RAND or RANDBETWEEN | Import functions cannot refer to these functions, directly or through another cell. | Use TODAY instead, or paste the volatile value as a fixed value. |
| New formula cannot export data | The source has the option to disable download, print and copy turned on. | Ask the source owner to change the setting. Existing formulas keep working. |
| Data stops appearing | The source was deleted, or the person who granted access was removed from it. | Confirm the source exists, and ask the source owner to grant access again. |
| Import is too large | Each request is capped at 10MB of received data. | Narrow the range to the rows and columns needed. |
| Slow sheet with chains of imports | Sheets import from each other in a chain or a loop. | Import directly from each source to a single destination. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use an external reference such as `[Book.xlsx]Sheet1!A1` or Power Query to combine workbooks. |
| Google Sheets | Available | Requires access to be granted between the two files before the first import works. Works with Google Sheets files only. |

## Tips and Best Practices

- Import one cell first to confirm access, then expand the range.
- Do not wrap a new IMPORTRANGE in IFERROR while you set it up, because IFERROR hides the Allow Access prompt.
- Store each source URL in a labeled settings cell so that one edit updates every formula that uses it.
- Import only the rows and columns you need, because each request is capped at 10MB.
- Avoid chains where one file imports from another that imports from a third.
- Remember that granted access counts against the source's 600-user share limit.
- Keep an empty area below and to the right of each formula so the imported values have room to fill.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Selects imported rows that match a condition. |
| [IMPORTDATA](IMPORTDATA.md) | Imports CSV or TSV files from a web address. |
| [IMPORTHTML](IMPORTHTML.md) | Imports a table or list from a web page. |
| [INDEX](../Lookup%20%26%20Reference/INDEX.md) | Returns one value from an imported range. |
| [QUERY](../Google-specific/QUERY.md) | Filters, sorts and reshapes imported rows. |

## Official Documentation

- [Google Docs Editors Help: IMPORTRANGE](https://support.google.com/docs/answer/3093340)
