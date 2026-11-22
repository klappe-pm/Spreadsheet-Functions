---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
purpose:
  - Data Import
  - Data Retrieval
use-case:
  - Competitor Price Tables
  - Public Statistics Tables
  - Sports Standings Tables
related:
  - ENCODEURL
  - IMPORTDATA
  - IMPORTFEED
  - IMPORTXML
  - INDEX
  - QUERY
level: 2
source:
  - https://support.google.com/docs/answer/3093339
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Import HTML
  - Import Table
tags:
  - data-import
  - html-parsing
  - sheets
  - tables
  - web-scraping
---

# IMPORTHTML

## Description

**IMPORTHTML** pulls a table or a list out of a web page and places it in the sheet. A table is an HTML table element, and a list is a bulleted or numbered list. The second argument chooses the kind of element, and the third argument chooses which one, counting from the top of the page.

Tables and lists are counted separately. A page can have a list and a table that are both index 1, so the index always depends on the query type. Pages often contain navigation tables or information boxes before the main data, so the correct index is found by trying values until the right table appears.

Use IMPORTHTML when the data is shown as a table or list in the page's HTML. Use IMPORTDATA for a CSV or TSV file, IMPORTFEED for an RSS or Atom feed, and IMPORTXML for an XPath query against XML or HTML.

The official documentation does not describe the exact layout of the returned data, the refresh timing, or any size limits. Check the result on the live page before building formulas on it, and confirm that the site allows the use.

IMPORTHTML is a Google Sheets function. Excel uses Power Query for the same job, as described under Platform Differences.

## Syntax

```excel
=IMPORTHTML(url, query, index)
```

<!-- Image 1: Address, Query Type and Index. See Images/Web/IMPORTHTML.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `url` | Yes | The address of the web page, including the protocol such as `https://`. Enter it in quotes or as a reference to a cell. |
| `query` | Yes | `"table"` to import a table element, or `"list"` to import a bulleted or numbered list. |
| `index` | Yes | The position of the table or list on the page, starting at 1. Tables and lists are counted separately. |

### Return Value

The rows and columns of the selected table, or the items of the selected list, placed starting at the cell that holds the formula. A list returns one item per row. The official documentation does not describe a fixed layout, so confirm the shape of the result on the page.

## Examples

### Example 1: The First Table on a Page

```excel
=IMPORTHTML("https://example.com/rankings/cities","table",1)
```

**Result:** The first table on the page, with each table row in a sheet row and each cell in its own column.

If the first table is a navigation or information box, try index 2 next.

### Example 2: A Later Table on the Same Page

```excel
=IMPORTHTML("https://example.com/rankings/cities","table",2)
```

**Result:** The second table on the page.

Change only the index to move through the page's tables. The address and query type stay the same.

### Example 3: The First List on a Page

```excel
=IMPORTHTML("https://example.com/guides/tools","list",1)
```

**Result:** Each item in the first bulleted or numbered list appears in its own row.

Lists return one column, which makes them easy to count with ROWS.

<!-- Image 2: A List Imported as One Column. See Images/Web/IMPORTHTML.md -->

### Example 4: Address From a Cell

With `A2` holding `https://example.com/rankings/cities`:

```excel
=IMPORTHTML(A2,"table",1)
```

**Result:** The same table as Example 1.

Keeping the address in a cell lets one edit switch the source for every formula that refers to it.

### Example 5: Read One Cell From a Table

```excel
=INDEX(IMPORTHTML("https://example.com/prices","table",1),2,3)
```

**Result:** The value in row 2, column 3 of the imported table.

INDEX with a row and column number returns one cell. Row 1 is the first row of the imported table.

### Example 6: Filter and Sort a Table With QUERY

```excel
=QUERY(IMPORTHTML("https://example.com/prices","table",1),"select Col1, Col2 where Col2 > 20 order by Col2 desc",0)
```

**Result:** The first two columns for rows where `Col2` is above 20, sorted from highest to lowest.

QUERY refers to imported columns as Col1, Col2 and so on. The final 0 means that the import has no header row to skip.

## Story Problems

### Problem 1: Highest Daily High

A weather page publishes a table of daily highs. The imported table has a header row and five days, with the High values in column 3. The imported table is shown below for reference.

| Day | City | High |
| --- | --- | --- |
| Monday | Lisbon | 18 |
| Tuesday | Lisbon | 21 |
| Wednesday | Lisbon | 19 |
| Thursday | Lisbon | 24 |
| Friday | Lisbon | 22 |

**Task:** Write a formula that returns the highest value in the High column of the first table on the page.

**Solution:**

```excel
=MAX(INDEX(IMPORTHTML("https://example.com/weather","table",1),0,3))
```

**Answer:** `24`, the Thursday high. MAX ignores the header text in the High column, so only the five numbers are compared.

### Problem 2: Counting Items in a List

A guide page has a bulleted list of tools. The first list on the page has seven bullets.

**Task:** Write a formula that returns the number of items in the first list on the page.

**Solution:**

```excel
=ROWS(IMPORTHTML("https://example.com/guides/tools","list",1))
```

**Answer:** `7`. Each bullet becomes one row, so ROWS counts seven.

## Use Cases

### Competitor Price Tables

**Scenario:** A retail buyer watches a competitor's price table for a set of products and wants only the rows for one product family.

```excel
=QUERY(IMPORTHTML(A2,"table",1),"select Col1, Col2 where Col1 contains 'Pro'",0)
```

**Why It Works:** IMPORTHTML brings in the table, and QUERY keeps the product rows that match the name. Check the site's terms before collecting prices this way.

### Public Statistics Tables

**Scenario:** A researcher needs a population figure from a statistics agency page, which publishes several tables.

```excel
=INDEX(IMPORTHTML("https://example.gov/statistics/population","table",2),3,2)
```

**Why It Works:** The index picks the table that holds the figures, and INDEX picks the row and column. Confirm the table number by viewing the page before relying on the formula.

### Sports Standings Tables

**Scenario:** A fan site lists league standings, and the editor wants the table sorted by points.

```excel
=QUERY(IMPORTHTML(A2,"table",1),"select * order by Col3 desc",1)
```

**Why It Works:** The header row is kept with the argument 1, and the rows are sorted by the third column from highest to lowest. Confirm which column holds points before using the formula.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error result | The index is higher than the number of tables or lists on the page. | Lower the index, starting at 1, and remember that tables and lists are counted separately. |
| Error result | The address is wrong, or the page is not publicly available. | Open the address in a browser or a private window. Correct the address or use a public page. |
| Table is visible in the browser but does not import | The table is added to the page by a script after it loads, so the function does not see it. | View the page source to confirm the table is in the HTML. Use a different source if it is not. |
| Wrong table is returned | The index counts a navigation or information table. | Try the next index, and count tables and lists separately. |
| Error result | The query is not `"table"` or `"list"`. | Enter one of the two exact values. |
| Garbled or shifted values | The page uses merged cells or nested tables. | Clean the text with TRIM and CLEAN, or choose a simpler source. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use Power Query (Data, Get Data, From Web). Its navigator lets you pick a table from the page. |
| Google Sheets | Available | Takes a URL, a query of `"table"` or `"list"`, and an index. |

## Tips and Best Practices

- Count tables and lists from the top of the page, and remember that each type has its own count.
- Confirm the index in a browser's view-source before you build formulas on the table.
- Store the page address in a labeled cell so one edit updates every formula.
- Wrap formulas in IFERROR on shared sheets, for example `=IFERROR(IMPORTHTML(A2,"table",1),"Data unavailable")`.
- Use TRIM and CLEAN on text that comes from a web page.
- Read the site's terms of use before you import its data on a regular schedule.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ENCODEURL](ENCODEURL.md) | Encodes query values placed in the page address. |
| [IMPORTDATA](IMPORTDATA.md) | Imports CSV or TSV files rather than tables on a page. |
| [IMPORTFEED](IMPORTFEED.md) | Imports RSS or Atom feed items. |
| [IMPORTXML](IMPORTXML.md) | Uses an XPath query for more precise selection from a page. |
| [INDEX](../Lookup%20%26%20Reference/INDEX.md) | Returns one row, column or cell from the imported table. |
| [QUERY](../Google-specific/QUERY.md) | Filters, sorts and selects columns from the imported table. |

## Official Documentation

- [Google Docs Editors Help: IMPORTHTML](https://support.google.com/docs/answer/3093339)
