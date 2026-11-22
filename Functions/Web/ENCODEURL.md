---
domain: Spreadsheet Functions
category: Web
subcategory: URL Tools
purpose:
  - Text Manipulation
use-case:
  - Encoded File Names
  - Filtered Report Links
  - Product Search Links
related:
  - FILTERXML
  - HYPERLINK
  - IMPORTDATA
  - IMPORTHTML
  - WEBSERVICE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/encodeurl-function
  - https://support.google.com/docs/answer/9199778
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Percent Encode Text
  - URL Encode
tags:
  - excel
  - sheets
  - url-encoding
  - web-queries
---

# ENCODEURL

## Description

**ENCODEURL** converts a piece of text into a form that can sit safely inside a web address. Spaces become `%20`, and punctuation and symbols such as commas, ampersands and slashes become a percent sign followed by two hexadecimal digits. Use it when a link or query string is built from cell values, so that a value such as `Oak Desk, 120 cm` does not break the address it sits in.

Encode each value separately, then join the encoded values to the fixed part of the address with `&`. Encoding a whole address does the wrong thing: the colon and slashes in `https://` are encoded too, and the link stops working. ENCODEURL is the step that makes WEBSERVICE (Excel) and IMPORTHTML (Google Sheets) work reliably when a query parameter holds spaces or punctuation.

In Excel, ENCODEURL runs in desktop Excel on Windows only. It is not available in Excel for the web or Excel for Mac. Google Sheets provides it as a standard function, and the encoding of spaces and punctuation is the same as the examples on this page.

## Syntax

```excel
=ENCODEURL(text)
```

<!-- Image 1: Encoding a Value in a Cell. See Images/Web/ENCODEURL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The string to encode, entered as a quoted literal or as a cell reference. Spaces, commas, ampersands, slashes and other punctuation are encoded. |

### Return Value

A text string in which each unsafe character is replaced by a percent sign and two hexadecimal digits. Letters and digits pass through unchanged. The result is text, so it joins to other text with `&`.

## Examples

### Example 1: Basic Encoding

```excel
=ENCODEURL("Spring Sale & Clearance")
```

**Result:** `Spring%20Sale%20%26%20Clearance`

The space becomes `%20` and the ampersand becomes `%26`. Both characters would otherwise be read as separators by a web server.

### Example 2: Encode a Cell Value

With `A2` containing `Hello, World!`:

```excel
=ENCODEURL(A2)
```

**Result:** `Hello%2C%20World%21`

The comma becomes `%2C`, the space becomes `%20`, and the exclamation mark becomes `%21`.

### Example 3: Build a Search Link

With `A3` containing `red shoes`:

```excel
="https://example.com/search?q="&ENCODEURL(A3)
```

**Result:** `https://example.com/search?q=red%20shoes`

Only the search term is encoded. The fixed part of the address stays as typed, so the question mark and equal sign keep their meaning.

<!-- Image 2: Joining an Encoded Value to a Fixed Address. See Images/Web/ENCODEURL.md -->

### Example 4: Encode a Slash and a Colon

```excel
=ENCODEURL("size 10/11")
```

**Result:** `size%2010%2F11`

The slash becomes `%2F`. This is the reason a whole address must not be passed through ENCODEURL: the slashes in `https://` would be encoded the same way.

### Example 5: Clickable Link With HYPERLINK

With `A3` containing `red shoes`:

```excel
=HYPERLINK("https://example.com/search?q="&ENCODEURL(A3), "Search for red shoes")
```

**Result:** A clickable cell labeled `Search for red shoes` that opens the search page.

HYPERLINK shows friendly text while the encoded address does the work behind the label.

## Story Problems

### Problem 1: Product Search Links

A catalog team needs a search link for each product. The product names are in column A, and the link text must be encoded in column B.

| Product | Name (Column A) |
| --- | --- |
| Oak Desk | Oak Desk, 120 cm |
| Mug | Blue Ceramic Mug, Large |

**Task:** Write the formula in `B2` that encodes the name in `A2`, then fill it down to `B3`.

**Solution:**

```excel
=ENCODEURL(A2)
```

**Answer:** `Oak%20Desk%2C%20120%20cm` in `B2`, and `Blue%20Ceramic%20Mug%2C%20Large` in `B3` after filling down. Each space becomes `%20` and each comma becomes `%2C`.

<!-- Image 3: Product Search Links in a Catalog. See Images/Web/ENCODEURL.md -->

### Problem 2: Length of an Encoded File Name

A team stores a report named `Q3 Report & Notes.xlsx` in cell `A2`. A link to the file must be built, and the team wants to know how many characters the encoded name uses.

| File Name (Column A) |
| --- |
| Q3 Report & Notes.xlsx |

**Task:** Count the characters in the encoded version of the file name in `A2`.

**Solution:**

```excel
=LEN(ENCODEURL(A2))
```

**Answer:** `30`. The encoded name is `Q3%20Report%20%26%20Notes.xlsx`, which has 30 characters. The period before `xlsx` is left as it is.

## Use Cases

### Search Links in a Product Catalog

**Scenario:** A purchasing team keeps a list of products and wants a one-click search link for each row on the shop's website.

```excel
="https://shop.example.com/find?term="&ENCODEURL(A2)
```

**Why It Works:** ENCODEURL protects each product name, including its commas and spaces, so the shop receives the full name as one search term. The base address stays in the formula, so changing the shop address means editing one formula.

### Filtered Report Pulls

**Scenario:** A finance analyst pulls a table from a reporting site, filtered by the region name typed in `B2`.

```excel
=IMPORTHTML("https://example.com/report?region="&ENCODEURL(B2), "table", 1)
```

**Why It Works:** A region such as `North East` contains a space that would break the query string. Encoding the region name lets the page receive `North%20East` and return the matching table.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Link opens the wrong page or no results | The value was not encoded, so spaces or symbols changed the meaning of the address. | Wrap the value in ENCODEURL and join it to the address with `&`. |
| Slashes or colons in the address look wrong | The whole address was encoded, including `https://`. | Encode only the value. Keep the fixed address outside the function. |
| Function is missing or does not return a result | The formula is running in Excel for the web or Excel for Mac. | Use desktop Excel on Windows, or build the encoded text in Google Sheets. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 on Windows | Not available in Excel for the web or Excel for Mac. On Mac it can appear in the function list but returns no results. |
| Google Sheets | Available as a standard function | Takes one text argument. Builds query strings for web import functions such as IMPORTHTML. |

## Tips and Best Practices

- Encode each value on its own, then join the values to a fixed base address with `&`.
- Store the base address in a labeled cell so that one edit updates every link.
- Test one generated link in a browser before filling the formula down a column.
- Pair ENCODEURL with HYPERLINK when the link needs friendly text.
- Use ENCODEURL in the query-string part of WEBSERVICE (Excel) or IMPORTHTML (Google Sheets) formulas.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTERXML](FILTERXML.md) | Extracts values from the XML that WEBSERVICE returns for an encoded request. |
| [HYPERLINK](../Lookup%20%26%20Reference/HYPERLINK.md) | Turns an encoded address into a clickable link with friendly text. |
| [IMPORTDATA](IMPORTDATA.md) | Imports CSV or TSV data from a URL that may contain encoded parameters. |
| [IMPORTHTML](IMPORTHTML.md) | Imports a table or list from a page whose address includes encoded parameters. |
| [WEBSERVICE](WEBSERVICE.md) | Fetches raw text from an encoded address in Excel. |

## Official Documentation

- [Microsoft Support: ENCODEURL function](https://support.microsoft.com/en-us/excel/functions/encodeurl-function)
- [Google Docs Editors Help: ENCODEURL](https://support.google.com/docs/answer/9199778)
