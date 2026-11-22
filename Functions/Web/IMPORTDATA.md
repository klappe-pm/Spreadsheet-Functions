---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
purpose:
  - Data Import
use-case:
  - Daily Export Links
  - Imported Row Counts
  - Published Dataset Snapshots
related:
  - IMPORTFEED
  - IMPORTHTML
  - IMPORTRANGE
  - IMPORTXML
  - QUERY
level: 2
source:
  - https://support.google.com/docs/answer/3093335
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Import CSV
  - Import TSV
tags:
  - csv
  - data-import
  - external-data
  - sheets
  - tsv
---

# IMPORTDATA

## Description

**IMPORTDATA** fetches a file from a web address and places its rows and columns into the sheet. The file must be in CSV (comma-separated values) or TSV (tab-separated values) format. The result fills the cells below and to the right of the formula, so the data stays linked to its source rather than being copied by hand.

Use IMPORTDATA when a data provider publishes a plain CSV or TSV file at a stable address. For a table inside a web page, use IMPORTHTML. For an XML or HTML query, use IMPORTXML. For an RSS or Atom feed, use IMPORTFEED.

The official documentation does not state how often the data refreshes, the maximum file size, or the error messages the function can return. Test each source with a real file before relying on it in a shared report.

IMPORTDATA is a Google Sheets function. Excel has no equivalent formula; the closest approach is Power Query, described under Platform Differences.

## Syntax

```excel
=IMPORTDATA(url)
```

<!-- Image 1: The URL Argument and the Imported Grid. See Images/Web/IMPORTDATA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `url` | Yes | The address of a CSV or TSV file, including the protocol such as `https://`. Enter it in quotes or as a reference to a cell that holds the address. It must point to the file itself, not to a web page that displays the file. |

### Return Value

An array of the file's rows and columns, placed starting at the cell that holds the formula. Only CSV and TSV files are supported. Any other format does not produce the data.

## Examples

### Example 1: Import a CSV File

```excel
=IMPORTDATA("https://example.com/data/stores.csv")
```

**Result:** One row for each line in `stores.csv`, with each comma-separated field in its own column.

The first line of the file usually holds the column headers, so it appears in the first row of the result.

### Example 2: Import From a Cell Address

With `A2` holding `https://example.com/data/stores.csv`:

```excel
=IMPORTDATA(A2)
```

**Result:** The same rows as Example 1.

Storing the address in a cell means the source can change by editing one cell, without touching the formula.

<!-- Image 2: Imported CSV Rows in the Sheet. See Images/Web/IMPORTDATA.md -->

### Example 3: Import a TSV File

```excel
=IMPORTDATA("https://example.com/data/readings.tsv")
```

**Result:** Each tab-separated field appears in its own column.

Use this form for TSV files. IMPORTDATA supports tab and comma separators.

### Example 4: Count the Data Rows

With `A2` holding the address of a file whose first line is a header:

```excel
=ROWS(IMPORTDATA(A2))-1
```

**Result:** The number of data rows, without the header line.

ROWS counts every imported row, and subtracting 1 removes the header.

### Example 5: Build Today's Address

```excel
=IMPORTDATA("https://example.com/exports/daily.csv?day="&TEXT(TODAY(),"yyyy-mm-dd"))
```

**Result:** The rows of the file for the current date, if the provider publishes a file at that address.

The TEXT function formats today's date so it matches the date pattern in the address, which lets one formula follow a daily export.

### Example 6: Filter Imported Rows With QUERY

With `A2` holding the address of a CSV file:

```excel
=QUERY(IMPORTDATA(A2),"select Col1, Col3 where Col3 > 1000",1)
```

**Result:** The `Col1` and `Col3` values for rows where `Col3` is above 1000, with the header row kept.

QUERY refers to imported columns as Col1, Col2 and so on. The final 1 tells QUERY that the first row is a header.

## Story Problems

### Problem 1: Daily Store Export Address

A store manager receives a daily CSV export. The store number is in `B1`, and the export date is in `B2`. The provider publishes each export at a fixed address pattern.

| Field | Value |
| --- | --- |
| Store number (`B1`) | 12 |
| Export date (`B2`) | 2026-11-21 |

**Task:** Write a formula that imports the export for store 12 on 2026-11-21. The address pattern is `https://example.com/exports/daily.csv?store=STORE&day=DATE`.

**Solution:**

```excel
=IMPORTDATA("https://example.com/exports/daily.csv?store="&B1&"&day="&TEXT(B2,"yyyy-mm-dd"))
```

**Answer:** The address the formula requests is `https://example.com/exports/daily.csv?store=12&day=2026-11-21`. The TEXT function turns the date into `2026-11-21`, which matches the pattern.

<!-- Image 3: Daily Export Address in the Story Problem. See Images/Web/IMPORTDATA.md -->

### Problem 2: Counting Data Rows

A CSV file has one header line and 14 lines of data. The address is in `A2`.

**Task:** Write a formula that returns the number of data rows, not counting the header.

**Solution:**

```excel
=ROWS(IMPORTDATA(A2))-1
```

**Answer:** `14`. The import returns 15 rows, including the header, and subtracting 1 gives 14.

## Use Cases

### Daily Export Links

**Scenario:** A point-of-sale system publishes a sales file each day, and the manager wants a total by product group without downloading the file.

```excel
=QUERY(IMPORTDATA(A2),"select Col2, sum(Col4) group by Col2",1)
```

**Why It Works:** IMPORTDATA brings in the day's rows, and QUERY totals the fourth column for each group in the second column. Update the address in `A2` when the provider changes the pattern.

### Imported Row Counts

**Scenario:** A researcher records how many rows a public dataset contains each month, to check that the source is still growing.

```excel
=ROWS(IMPORTDATA(B2))-1
```

**Why It Works:** The formula counts rows in the current file. Pasting its value into a log each month creates a history, because the function only shows the current count.

### Published Dataset Snapshots

**Scenario:** A team links a published spreadsheet to a CSV export and needs a fixed copy for an audit.

**Why It Works:** IMPORTDATA keeps the data current, so the audit copy must be made separately. Copy the imported range and paste it as values into an archive sheet on each audit date.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error or blank result | The address points to a web page, a zipped file, or a format other than CSV or TSV. | Open the address in a browser. It should show plain comma- or tab-separated text. Find the direct CSV or TSV link. |
| Error result | The address is missing `https://` or is misspelled. | Include the protocol and copy the address exactly. |
| All data in one column | The file uses a separator other than a comma or tab, such as a semicolon. | Import the lines as one column and split them with SPLIT, using the file's separator. |
| Source is not reachable | The address requires a login or is not publicly available. | Use a public address. IMPORTDATA takes only a URL, so it cannot send credentials. |
| Data does not change after the source changes | The source has not been updated, or the sheet has not refreshed yet. | Confirm the source changed in a browser, then recalculate the sheet and compare again. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use Power Query (Data, Get Data, From Web) to load a web file. Get Data, From Text/CSV loads a file already on your computer. |
| Google Sheets | Available | One URL argument. Supports CSV and TSV files only. |

## Tips and Best Practices

- Open the address in a browser before you enter the formula, and confirm that it shows plain text rows.
- Store each source address in a labeled cell so that one edit updates every formula that uses it.
- Leave empty cells below and to the right of the formula, because the imported rows fill them.
- Wrap the formula in IFERROR on shared sheets, for example `=IFERROR(IMPORTDATA(A2),"Source unavailable")`.
- Use QUERY to select columns, filter rows and sort the imported data in one step.
- Paste imported values into an archive sheet when a fixed copy is needed.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IMPORTFEED](IMPORTFEED.md) | Imports RSS or Atom feed items rather than CSV or TSV files. |
| [IMPORTHTML](IMPORTHTML.md) | Imports a table or list from a web page. |
| [IMPORTRANGE](IMPORTRANGE.md) | Imports cells from another Google Sheets file. |
| [IMPORTXML](IMPORTXML.md) | Applies an XPath query to XML or HTML from a URL. |
| [QUERY](../Google-specific/QUERY.md) | Filters, sorts and reshapes imported rows. |

## Official Documentation

- [Google Docs Editors Help: IMPORTDATA](https://support.google.com/docs/answer/3093335)
