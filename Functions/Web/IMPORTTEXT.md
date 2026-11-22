---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
purpose:
  - Data Import
use-case:
  - Fixed-Width Report Imports
  - Pipe-Delimited Stock Files
  - Tab-Separated Log Files
related:
  - IMPORTCSV
  - IMPORTDATA
  - SPLIT
  - TEXTSPLIT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/importtext-function
  - https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-data-into-excel-with-the-new-import-functions/4485613
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Import Text File
  - Text File Import
tags:
  - dynamic-array
  - excel
  - import
  - text-file
  - windows
---

# IMPORTTEXT

## Description

**IMPORTTEXT** reads a text file from a local path or a URL and places its rows and columns into the sheet as a dynamic array. It handles .txt, .csv and .tsv files, and it gives you control over how the text is split: the delimiter, the rows to skip or return, the file encoding and the locale.

When you omit the delimiter, IMPORTTEXT splits each line at tab characters. Pass a character or string such as `"|"` for another delimiter, use CHAR for special characters, or pass an ascending array of integers such as `{1,3}` to split fixed-width columns.

Like IMPORTCSV, IMPORTTEXT does not refresh on its own, so select Refresh All on the Data tab after the file changes. For a comma-separated file, IMPORTCSV needs fewer arguments. Microsoft announced the import functions on January 15, 2026. IMPORTTEXT is available only to Microsoft 365 subscribers enrolled in the Insiders Beta channel, in Excel for Windows, Version 2502 or later.

## Syntax

```excel
=IMPORTTEXT(path, [delimiter], [skip_rows], [take_rows], [encoding], [locale])
```

<!-- Image 1: Delimiter and Row Arguments. See Images/Web/IMPORTTEXT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `path` | Yes | The local file path or URL of the text file, in quotes, such as `"C:\Exports\stock.txt"`. |
| `delimiter` | No | The character or string that separates columns. When omitted, tab is used. Use CHAR for special characters, or an ascending integer array such as `{1,3}` for fixed-width columns. |
| `skip_rows` | No | The number of rows to skip at the top of the file. A negative value skips rows from the end. Leave it empty when you need to set a later argument, as in `"|",,3`. |
| `take_rows` | No | The number of rows to return. A negative value returns rows from the end of the array. |
| `encoding` | No | The text encoding of the file. UTF-8 is used when omitted. Microsoft does not list the other accepted values. |
| `locale` | No | Regional formatting for dates and numbers. When omitted, the operating system locale is used. |

### Return Value

A dynamic array of the imported rows and columns. The array spills into the cells next to the formula, so those cells must be empty. Microsoft does not list the error values for this function, so when an import fails, check the path, the file and the web permissions first.

## Examples

All examples use this pipe-delimited file, saved as `C:\Exports\stock.txt`.

```text
SKU|Qty|Bin
A-10|25|B1
A-11|14|B2
C-03|8|C1
D-77|31|D4
```

### Example 1: Split Columns on a Pipe

```excel
=IMPORTTEXT("C:\Exports\stock.txt", "|")
```

**Result:** `5 rows by 3 columns`, with the header row `SKU, Qty, Bin` at the top.

The pipe is passed as the delimiter, so each line splits into three columns. No rows are skipped.

### Example 2: Skip the Header Row

```excel
=IMPORTTEXT("C:\Exports\stock.txt", "|", 1)
```

**Result:** `4 rows by 3 columns`, starting with `A-10, 25, B1`.

Skipping one row removes the header, so the first returned row is the A-10 record.

### Example 3: Return the First Rows

```excel
=IMPORTTEXT("C:\Exports\stock.txt", "|",, 3)
```

**Result:** `3 rows`: the header row, then the A-10 and A-11 records.

The empty third argument skips no rows, and take_rows returns the first three rows of the array.

### Example 4: Total One Column

```excel
=SUM(INDEX(IMPORTTEXT("C:\Exports\stock.txt", "|", 1), 0, 2))
```

**Result:** `78`, because 25 + 14 + 8 + 31 = 78.

INDEX with a row argument of 0 returns the whole second column, which holds the Qty values.

<!-- Image 2: Pipe Delimiter Applied to Columns. See Images/Web/IMPORTTEXT.md -->

### Example 5: Use the Tab Default

```excel
=IMPORTTEXT("C:\Exports\tab-list.txt")
```

**Result:** Each tab character in the file starts a new column.

Because the delimiter is omitted, the function splits at tabs, so a tab-separated file needs no delimiter argument.

## Story Problems

### Problem 1: Counting Empty Bins

A warehouse writes its cycle count to `C:\Counts\cycle.txt`. The first line is a title, and the second line is the header. The file holds these records below the header, separated by pipes.

| Bin | Units |
| --- | --- |
| B4 | 12 |
| B7 | 30 |
| C2 | 0 |
| D1 | 45 |

**Task:** Import the count without the title line, then count the bins that hold zero units.

**Solution:**

```excel
=SUMPRODUCT(--(INDEX(IMPORTTEXT("C:\Counts\cycle.txt", "|", 1), 0, 2)=0))
```

**Answer:** `1`, because only bin C2 holds zero units. The header text in the Units column does not equal 0.

<!-- Image 3: Count File Imported With a Title Row. See Images/Web/IMPORTTEXT.md -->

### Problem 2: The Last Two Shifts

A plant saves its scrap report at `C:\Shifts\scrap.txt`. Each line is separated by a pipe, and the first line is the header.

| Shift | Scrap |
| --- | --- |
| Day | 14 |
| Evening | 9 |
| Night | 22 |

**Task:** Total the scrap for the last two shifts, without changing the header row in the file.

**Solution:**

```excel
=SUM(INDEX(IMPORTTEXT("C:\Shifts\scrap.txt", "|",,-2), 0, 2))
```

**Answer:** `31`, because the last two rows are Evening (9) and Night (22), and 9 + 22 = 31.

## Use Cases

### Pipe-Delimited Stock Files

**Scenario:** A warehouse system exports stock counts with a title line above the header and pipes between the fields.

```excel
=IMPORTTEXT("C:\Stock\counts.txt", "|", 1)
```

**Why It Works:** The pipe is the delimiter, and skipping one row removes the title. The header then becomes the first row of the imported array.

### Fixed-Width Report Imports

**Scenario:** A legacy system writes a report where each column starts at a fixed position in every line, with no delimiter characters.

```excel
=IMPORTTEXT("C:\Reports\payroll.txt", {1,9,15})
```

**Why It Works:** The ascending integer array defines the fixed-width column breaks. Check the first few rows of the result to confirm that each break falls in the right place.

### Tab-Separated Log Files

**Scenario:** A server writes its error log as a tab-separated file, and the team needs the last 100 entries.

```excel
=IMPORTTEXT("C:\Logs\errors.tsv",,, -100)
```

**Why It Works:** The tab delimiter is the default, so the function needs no delimiter argument. A negative take_rows value returns the last 100 rows.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The Excel build is older than Version 2502 or is not on the Insiders Beta channel. | Update Excel and join the Insiders Beta channel, or use Data, Get Data to import the file. |
| Wrong columns | The delimiter is omitted, so the file is split at tabs, but the file uses another character. | Pass the file's actual delimiter as the second argument. |
| Garbled characters | The file is not UTF-8 encoded. | Pass the file's encoding in the encoding argument. Test with a small take_rows value first. |
| Not documented | The path is wrong, or the file or web address cannot be reached. | Check the path. For a web address, select Data, Get Data, Data Source Settings, open the Global Permissions tab, select the URL and click Clear Permissions. |
| Old data | Imports do not refresh automatically. | Select Refresh All on the Data tab. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 Insiders Beta channel, Excel for Windows, Version 2502 or later | Announced January 15, 2026. The default encoding is UTF-8 and the default locale is the operating system locale. |
| Google Sheets | Not available | Use IMPORTDATA for a CSV or TSV file at a URL, or SPLIT for text that is already in cells. |

## Tips and Best Practices

- Always pass the delimiter explicitly, because an omitted delimiter means tab.
- Use CHAR(9) as the delimiter when you want to write out the tab character in the formula.
- Use skip_rows to remove report titles above the header row.
- Use a negative take_rows value to return only the end of a long log.
- Test a fixed-width array on a few rows first, and widen or move the breaks until each column lines up.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IMPORTCSV](IMPORTCSV.md) | A shorter function for comma-separated files only. |
| [IMPORTDATA](IMPORTDATA.md) | The Google Sheets function that imports a CSV or TSV file from a URL. |
| [SPLIT](../Text/SPLIT.md) | Splits text already in cells on a delimiter. |
| [TEXTSPLIT](../Text/TEXTSPLIT.md) | Splits text into rows and columns as a dynamic array. |

## Official Documentation

- [Microsoft Support: IMPORTTEXT function](https://support.microsoft.com/en-us/excel/importtext-function)
- [Microsoft 365 Insider Blog: Bring Data Into Excel With the New Import Functions](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-data-into-excel-with-the-new-import-functions/4485613)
