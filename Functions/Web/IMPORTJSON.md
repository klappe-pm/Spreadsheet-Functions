---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
purpose:
  - Data Import
use-case:
  - API Price Feeds
  - Catalog Title Lists
  - Exchange Rate Snapshots
related:
  - ENCODEURL
  - IMPORTDATA
  - IMPORTHTML
  - IMPORTXML
  - WEBSERVICE
level: 4
source:
  - https://developers.google.com/apps-script/guides/sheets/functions
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Import JSON
tags:
  - apps-script
  - community-script
  - json
  - web-api
---

# IMPORTJSON

## Description

**IMPORTJSON** is not a built-in Google Sheets function. It is a community custom function written in Google Apps Script, the JavaScript environment attached to Google Sheets. Someone adds the script to a spreadsheet's script project, and the function then works in cells like any built-in function. It reads a JSON response from a web address and returns the values found at a path you specify.

Google's Apps Script guide on custom functions explains how a script function is written, called from a cell, and limited. The guide does not document this particular function. The widely shared version of the script is an open-source project that its author archived in February 2023 and no longer maintains, so check the copy you install before relying on it in a shared report.

Because the function is not built in, its arguments and options depend on the script version installed. The version described here takes a web address and a slash-separated path. Use it for public JSON endpoints. Use IMPORTDATA for CSV files, IMPORTHTML for tables on a web page, and IMPORTXML for XPath queries.

## Syntax

```excel
=IMPORTJSON(url, query)
```

<!-- Image 1: The URL and the Path Argument. See Images/Web/IMPORTJSON.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `url` | Yes | The address of a JSON response, entered in quotes or as a cell reference. Any query parameters in the address belong to the web service, not to the function. |
| `query` | Yes | A slash-separated path into the JSON, such as `/title`. The path names the field to return from each record. |

### Return Value

The values found at the path, placed in the sheet. The shape of the result depends on the structure of the JSON response, and the script's project page does not describe it. Confirm the layout on a real response before you build formulas on it.

## Examples

### Example 1: Titles From a Public List

```excel
=IMPORTJSON("https://api.example.com/books?limit=20","/title")
```

**Result:** A column of titles, one for each record in the response.

The address returns a list, and the path `/title` picks the title field from each record.

### Example 2: Prices From a Product Feed

```excel
=IMPORTJSON("https://api.example.com/products","/price")
```

**Result:** A column of prices, one for each product in the feed.

### Example 3: Address From a Cell

With `A2` holding a JSON address:

```excel
=IMPORTJSON(A2,"/name")
```

**Result:** The names found at the path in the response at the address in `A2`.

Keeping the address in a cell lets one edit change the source for every formula that refers to it.

### Example 4: Total of the Returned Values

```excel
=SUM(IMPORTJSON(A2,"/price"))
```

**Result:** The total of the numeric values returned at the path.

SUM adds numbers only, so check the imported values for text before you rely on the total.

<!-- Image 2: Imported Values Summed in a Column. See Images/Web/IMPORTJSON.md -->

### Example 5: Show a Message When the Source Fails

```excel
=IFERROR(IMPORTJSON(A2,"/name"),"Feed unavailable")
```

**Result:** The imported names, or the text `Feed unavailable` if the function returns an error.

## Story Problems

### Problem 1: Prices for One Product Category

A buyer needs the price of every tea product in a public catalog. The JSON address for the tea category is in `B1`.

| Field | Value |
| --- | --- |
| Catalog address (`B1`) | `https://api.example.com/products?category=tea` |
| Path to price | `/price` |

**Task:** Write the formula that returns the price of each product in the response.

**Solution:**

```excel
=IMPORTJSON(B1,"/price")
```

**Answer:** A column with one price for each tea product in the response. The formula returns the values as they appear in the JSON, so the count matches the number of records in the response.

### Problem 2: Total of Imported Prices

Three prices have already been imported into `A2:A4`: 19.50, 4.25 and 8.00.

**Task:** Write a formula that totals the three imported prices.

**Solution:**

```excel
=SUM(A2:A4)
```

**Answer:** `31.75`, because 19.50 + 4.25 + 8.00 = 31.75.

## Use Cases

### API Price Feeds

**Scenario:** A supplier publishes current prices through a public JSON endpoint, and the purchasing team wants the prices in a sheet to compare with their budget.

```excel
=IMPORTJSON(A2,"/price")
```

**Why It Works:** The formula returns the price values for each record in the feed. Place the budget figures beside the imported column so the comparison updates when the feed is reloaded.

### Catalog Title Lists

**Scenario:** A librarian keeps a list of recently added titles from a public catalog service.

```excel
=IMPORTJSON("https://api.example.com/books?limit=20","/title")
```

**Why It Works:** The `limit` parameter belongs to the service, and it keeps the list to twenty records. The path `/title` returns only the title column.

### Exchange Rate Snapshots

**Scenario:** A finance team copies a daily exchange rate into a log, and the rate comes from a public endpoint.

```excel
=IMPORTJSON("https://api.example.com/rates/latest","/rate")
```

**Why It Works:** The formula gives the current rate, and the team pastes that value into the log as a fixed number each day. The history then stays the same even when the feed changes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Formula name is not recognized | The script is not added to the spreadsheet's Apps Script project. | Open Extensions, then Apps Script, add the script file, save it, and reload the sheet. |
| `#ERROR!` after a delay | A custom function must return within 30 seconds, and the request took longer. | Request less data, or store a snapshot of the values in the sheet. |
| `Loading...` never finishes | A volatile function such as NOW or RAND was used as an argument. | Pass a cell reference instead, and put the volatile function in a separate cell. |
| Empty or unexpected values | The path does not match the JSON structure. | Open the address in a browser, find the exact field name, and correct the path. |
| Permission error | Custom functions cannot request permission from the user, so the service needs a sign-in. | Use a public endpoint that does not require authorization. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use Power Query (Data, Get Data, From Web) to read a JSON response and expand its fields. |
| Google Sheets | Not built in. A community custom function written in Apps Script | Works only after the script is added through Extensions, then Apps Script. The function is not documented by Google, and the widely shared version is no longer maintained. |

## Tips and Best Practices

- Open the JSON address in a browser first and find the exact field names before writing the path.
- Store the address in a labeled cell so that one edit changes the source.
- Each cell that uses a custom function makes a separate call to the web service, so keep the number of calls small.
- Read the installed script's source code to confirm its arguments and options, because they vary between versions.
- Wrap formulas in IFERROR on shared sheets.
- Test the script again after changes to Google Sheets, because an unmaintained script may stop working.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ENCODEURL](ENCODEURL.md) | Encodes values placed in the JSON address. |
| [IMPORTDATA](IMPORTDATA.md) | Imports CSV or TSV files, which are simpler than JSON. |
| [IMPORTHTML](IMPORTHTML.md) | Imports tables and lists from a web page. |
| [IMPORTXML](IMPORTXML.md) | Applies XPath queries to XML or HTML. |
| [WEBSERVICE](WEBSERVICE.md) | Fetches raw text from a web address in Excel. |

## Official Documentation

- [Google Apps Script: Custom functions in Google Sheets](https://developers.google.com/apps-script/guides/sheets/functions)
