---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
purpose:
  - Data Import
use-case:
  - Bank Statement Imports
  - Monthly Sales Exports
  - Refreshable Data Feeds
related:
  - IMPORTDATA
  - IMPORTTEXT
  - IMPORTXML
  - SPLIT
  - TEXTSPLIT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/importcsv-function
  - https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-data-into-excel-with-the-new-import-functions/4485613
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - CSV Import Function
  - Import CSV
tags:
  - csv
  - dynamic-array
  - excel
  - import
  - windows
---

# IMPORTCSV

## Description

**IMPORTCSV** reads a comma-separated file from a local path or a URL and places its rows and columns into the sheet as a dynamic array. One formula replaces a manual copy and paste, and the imported block fills the empty cells below and to the right of the formula.

Imported data does not refresh on its own. Select Refresh All on the Data tab to bring in the latest contents of the file.

IMPORTCSV is a shorter form of IMPORTTEXT for comma-separated files only. It expects a comma delimiter and UTF-8 encoding, so use IMPORTTEXT for files that use semicolons, tabs, fixed-width columns or another encoding. Microsoft announced the import functions on January 15, 2026. The function is available only to Microsoft 365 subscribers enrolled in the Insiders Beta channel, in Excel for Windows, Version 2502 or later.

## Syntax

```excel
=IMPORTCSV(path, [skip_rows], [take_rows], [locale])
```

<!-- Image 1: Import Formula Anatomy. See Images/Web/IMPORTCSV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `path` | Yes | The local file path or URL of the CSV file, in quotes, such as `"C:\Exports\orders.csv"`. |
| `skip_rows` | No | The number of rows to skip at the top of the file. A negative value skips rows from the end of the array. Leave it empty when you need to set a later argument, as in `,,3`. |
| `take_rows` | No | The number of rows to return. A negative value returns rows from the end of the array. |
| `locale` | No | Regional formatting for dates and numbers. When omitted, the operating system locale is used. |

### Return Value

A dynamic array of the imported rows and columns. The array spills into the cells next to the formula, so those cells must be empty. Microsoft does not list the error values for this function, so when an import fails, check the path, the file and the web permissions first.

## Examples

All examples use this file, saved as `C:\Exports\orders.csv`.

```text
Order,Customer,Amount
1001,Harbor Cafe,240
1002,Pine Books,180
1003,Lake Tools,95
1004,Oak Studio,310
1005,Mesa Print,150
```

### Example 1: Import the Whole File

```excel
=IMPORTCSV("C:\Exports\orders.csv")
```

**Result:** `6 rows by 3 columns`, with the header row `Order, Customer, Amount` at the top.

No rows are skipped, so the header row is imported as the first row.

### Example 2: Skip the Header Row

```excel
=IMPORTCSV("C:\Exports\orders.csv", 1)
```

**Result:** `5 rows by 3 columns`, starting with `1001, Harbor Cafe, 240`.

Skipping the first row removes the header, so the first returned row is order 1001.

### Example 3: Return the First Two Rows

```excel
=IMPORTCSV("C:\Exports\orders.csv",,2)
```

**Result:** `2 rows`: the header row and order 1001.

The empty second argument skips no rows, and take_rows returns only the first two rows of the array.

### Example 4: Total the Amount Column

```excel
=SUM(INDEX(IMPORTCSV("C:\Exports\orders.csv", 1), 0, 3))
```

**Result:** `975`, because 240 + 180 + 95 + 310 + 150 = 975.

Skipping the header keeps the Amount column numeric. INDEX with a row argument of 0 returns the whole third column, and SUM adds it.

<!-- Image 2: Spilled Array Beside the Formula. See Images/Web/IMPORTCSV.md -->

### Example 5: Return the Last Two Rows

```excel
=IMPORTCSV("C:\Exports\orders.csv",,-2)
```

**Result:** `2 rows`: order 1004 (Oak Studio, 310) and order 1005 (Mesa Print, 150).

A negative take_rows value counts from the end of the array, so the header is not returned.

## Story Problems

### Problem 1: Skipping a Report Title

A finance clerk receives a bank export at `C:\Exports\bank.csv`. The first line is a report title, and the second line is the header. The file contains these rows below the header.

| Payee | Amount |
| --- | --- |
| Fuel | 62 |
| Printer Paper | 38 |
| Courier | 115 |
| Software | 240 |

**Task:** Import the export without the title line, then total the Amount column.

**Solution:**

```excel
=SUM(INDEX(IMPORTCSV("C:\Exports\bank.csv", 1), 0, 2))
```

**Answer:** `455`, because 62 + 38 + 115 + 240 = 455. The header text in the first returned row is ignored by SUM.

### Problem 2: Taking the Last Three Days

A website team exports daily visits to `C:\Exports\visits.csv`. The file holds six days, and the team wants the total for the last three days only.

| Day | Visits |
| --- | --- |
| Mon | 120 |
| Tue | 135 |
| Wed | 98 |
| Thu | 142 |
| Fri | 160 |
| Sat | 75 |

**Task:** Total the visits for the last three days, skipping the header row.

**Solution:**

```excel
=SUM(INDEX(IMPORTCSV("C:\Exports\visits.csv", 1, -3), 0, 2))
```

**Answer:** `377`, because Thu (142), Fri (160) and Sat (75) are the last three rows, and 142 + 160 + 75 = 377.

<!-- Image 3: Last Three Rows Highlighted. See Images/Web/IMPORTCSV.md -->

## Use Cases

### Bank Statement Imports

**Scenario:** A bookkeeper receives a CSV from the bank with two lines of report title above the header, and needs the last 30 rows of the file.

```excel
=IMPORTCSV("C:\Exports\bank.csv", 2, -30)
```

**Why It Works:** Skipping two rows removes the title and the blank line. A negative take_rows value returns the last 30 rows of the remaining array.

### Monthly Sales Exports

**Scenario:** A regional manager receives a sales export at the same path every month, and the summary sheet must show the new month after each update.

```excel
=IMPORTCSV("C:\Exports\sales.csv", 1)
```

**Why It Works:** The formula reads the file again whenever Refresh All runs, so the summary picks up the new export without changing the formula.

### Refreshable Data Feeds

**Scenario:** A team publishes a price list as a CSV file at a web address that is updated every night.

```excel
=IMPORTCSV("https://example.com/feeds/prices.csv")
```

**Why It Works:** The URL is read the same way as a local path. Imports do not refresh automatically, so select Refresh All after the nightly update. Files on the web can require sign-in, as described in Common Errors.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The Excel build is older than Version 2502 or is not on the Insiders Beta channel. | Update Excel and join the Insiders Beta channel, or use Data, Get Data to import the file. |
| Not documented | The path is wrong, or the file or web address cannot be reached. | Check the path. For a web address, select Data, Get Data, Data Source Settings, open the Global Permissions tab, select the URL and click Clear Permissions. |
| Columns are wrong | The file does not use commas or does not use UTF-8. | Use IMPORTTEXT and set the delimiter and encoding. |
| Old data | Imports do not refresh automatically. | Select Refresh All on the Data tab. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 Insiders Beta channel, Excel for Windows, Version 2502 or later | Announced January 15, 2026. The locale argument defaults to the operating system locale. |
| Google Sheets | Not available | Use IMPORTDATA to import a CSV or TSV file from a URL. |

## Tips and Best Practices

- Use skip_rows to remove report titles above the header, so the header becomes the first returned row.
- Wrap the imported array in INDEX with a row argument of 0 to pull one column out for SUM, AVERAGE or a lookup.
- Keep the cells below and to the right of the formula empty, because a blocked spill range returns an error.
- Select Refresh All on the Data tab after the source file changes.
- Switch to IMPORTTEXT when the file uses semicolons, tabs, another encoding or fixed-width columns.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IMPORTDATA](IMPORTDATA.md) | The Google Sheets function that imports a CSV or TSV file from a URL. |
| [IMPORTTEXT](IMPORTTEXT.md) | Imports delimited text with a choice of delimiter, encoding and column layout. |
| [IMPORTXML](IMPORTXML.md) | Imports structured data from web pages in Google Sheets. |
| [SPLIT](../Text/SPLIT.md) | Splits text already in cells into columns. |
| [TEXTSPLIT](../Text/TEXTSPLIT.md) | Splits text into rows and columns as a dynamic array. |

## Official Documentation

- [Microsoft Support: IMPORTCSV function](https://support.microsoft.com/en-us/excel/importcsv-function)
- [Microsoft 365 Insider Blog: Bring Data Into Excel With the New Import Functions](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-data-into-excel-with-the-new-import-functions/4485613)
