---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
purpose:
  - Data Import
  - Data Retrieval
use-case:
  - Competitor Price Monitoring
  - Page Metadata Audits
  - Public Data Feeds
related:
  - IFERROR
  - IMPORTDATA
  - IMPORTFEED
  - IMPORTHTML
  - QUERY
  - WEBSERVICE
level: 3
source:
  - https://support.google.com/docs/answer/3093342
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Import XML
  - XPath Import
tags:
  - sheets
  - web-import
  - web-scraping
  - xpath
---

# IMPORTXML

## Description

**IMPORTXML** pulls data from a web page or XML feed into a sheet. You give it a URL and an XPath query, which is a path that points to specific elements in the document, such as the page title, every link, or one value inside a particular element. The function returns the matching text or attribute values, and when several elements match, each value fills the next cell down.

Use IMPORTXML when the data you need is not in a clean table or list. IMPORTHTML reads only tables and lists, and IMPORTFEED reads only RSS and Atom feeds, so IMPORTXML is the choice when you need one heading, a meta tag, or a value buried inside a specific element. Google documents support for XML, HTML, CSV, TSV, and RSS and ATOM feeds.

The function sees only the HTML the server sends. Content that JavaScript adds after the page loads, pages behind a login, and sites that block automated requests will not return the data you expect. Google also stores imported results for a while, so a change on the source page can take time to appear in the sheet.

IMPORTXML is available only in Google Sheets. Excel has no matching function.

## Syntax

```excel
=IMPORTXML(url, xpath_query, [locale])
```

<!-- Image 1: XPath Query Anatomy. See Images/Web/IMPORTXML.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `url` | Yes | The full address of the page or feed, including `https://` or `http://`. Type it in quotes or reference a cell that holds it. |
| `xpath_query` | Yes | The XPath expression that selects the elements to return. Type it in quotes or reference a cell that holds it. |
| `locale` | No | A language and region code that controls how the imported numbers and dates are read. When omitted, the document locale is used. |

### Return Value

The text or attribute values of the matching elements, placed in the cell that holds the formula and the cells below it. A query that matches nothing, a page that cannot be fetched, or an invalid XPath returns an error instead.

## Examples

### Example 1: Pull the Page Title

```excel
=IMPORTXML("https://www.wikipedia.org", "//title")
```

**Result:** The text inside the page's `<title>` element.

Every HTML page has a title element in its head section, so this query is a reliable first test that the URL and the query both work. `//` tells XPath to search the whole document, not only one branch of it.

### Example 2: Read a Meta Description

```excel
=IMPORTXML(A2, "//meta[@name='description']/@content")
```

**Result:** The description the page offers to search engines, or an error if the page has no description tag.

The `/@content` part returns the attribute value instead of element text. Put the page address in A2 so you can copy this formula down a list of pages. To find the XPath for any element, use the browser developer tools, as shown in the image guide.

<!-- Image 2: Copy XPath From Browser Developer Tools. See Images/Web/IMPORTXML.md -->

### Example 3: Return Every Link Address

```excel
=IMPORTXML("https://www.wikipedia.org", "//a/@href")
```

**Result:** One link address per cell, filling downward, for every anchor element on the page.

`//a` selects each anchor element and `/@href` reads its address. Relative addresses such as `/wiki/Main_Page` come back exactly as the page wrote them, so you may need to add the site address in front of them.

### Example 4: Select One Element by Position

```excel
=IMPORTXML(A2, "(//div[@class='product'])[1]//h2")
```

**Result:** The heading text from the first product block on the page.

The parentheses apply the position `[1]` to the whole set of product blocks. Without them, `//div[@class='product'][1]` would take the first product block inside each parent element, which usually returns more than you want.

### Example 5: Trim Stray Spaces From Imported Text

```excel
=TRIM(IMPORTXML(A2, "//h1"))
```

**Result:** The main heading text with leading and trailing spaces removed.

Imported text often carries line breaks or spacing from the page layout. Wrapping the import in TRIM makes the value safe for lookups and comparisons.

### Example 6: Show a Message When a Pull Fails

```excel
=IFERROR(IMPORTXML(A2, "//span[@class='price']"), "Price not found")
```

**Result:** The price text, or "Price not found" when the query returns an error.

Pages change, elements disappear, and sites sometimes refuse requests. IFERROR keeps the sheet readable and stops errors from spreading into formulas that depend on this cell.

## Story Problems

### Problem 1: Summing Imported Prices

A buyer imports three competitor prices into column B. The site shows each price with a dollar sign and thousands separators, so the imported values are text.

| Product | Imported Text |
| --- | --- |
| Floor Lamp | $1,249.00 |
| Desk | $89.50 |
| Office Chair | $1,099.99 |

**Task:** Convert the three texts to numbers and add them together.

**Solution:**

```excel
=SUMPRODUCT(VALUE(SUBSTITUTE(SUBSTITUTE(B2:B4,"$",""),",","")))
```

**Answer:** `2438.49`, because 1249.00 + 89.50 + 1099.99 = 2438.49. The inner SUBSTITUTE removes the dollar signs, the outer SUBSTITUTE removes the commas, and VALUE turns each clean text into a number.

<!-- Image 3: Imported Price Total. See Images/Web/IMPORTXML.md -->

### Problem 2: Counting Sale Pages

A marketer imports the title of four product pages into column B and wants to know how many titles mention a sale.

| Page | Imported Title |
| --- | --- |
| Lamps | Spring Sale: Lamps |
| Desks | Desk Clearance |
| Chairs | Summer Sale Chairs |
| Gift Cards | Gift Cards |

**Task:** Count the titles that contain the word Sale.

**Solution:**

```excel
=COUNTIF(B2:B5,"*Sale*")
```

**Answer:** `2`, because "Spring Sale: Lamps" and "Summer Sale Chairs" contain the word, and the other two titles do not.

## Use Cases

### Competitor Price Monitoring

**Scenario:** A procurement analyst keeps a list of competitor product page addresses in column A and wants the current price next to each one.

```excel
=IMPORTXML(A2, "//span[@class='price']")
```

**Why It Works:** Each row reads its own address, so one formula copied down the list covers every product. Prices that a script loads after the page opens will not appear, so check a few rows by hand.

### Page Metadata Audits

**Scenario:** A content team checks that every page has a title that fits the length limit the team has set for search results.

```excel
=LEN(IMPORTXML(A2, "//title"))
```

**Why It Works:** IMPORTXML returns the title, and LEN counts its characters. Add a column with IF to flag rows that exceed the limit, so the team can rewrite those titles.

### Public Data Feeds

**Scenario:** An analyst follows a public XML news feed and wants the headline of each item without reading the raw file.

```excel
=IMPORTXML("https://www.example.org/news.xml", "//*[local-name()='item']/*[local-name()='title']")
```

**Why It Works:** The `local-name()` test matches elements by name and ignores any namespace prefix, which many feeds use. Without it, a plain `//item/title` query can fail even though the elements exist.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error in the cell | The XPath matches nothing, often because the element is added by JavaScript. | Confirm the element appears in the page source (Ctrl+U) and adjust the query. |
| Error in the cell | The page cannot be fetched, needs a login, or blocks Google. | Open the address in a private browser window. Choose a different source if the site blocks it. |
| Error in the cell | The XPath has a syntax error, such as an unmatched quote or a misspelled function. | Test the query in the browser console with `$x("//your/xpath")` before using it. |
| Empty cells | The matched element holds its text in child elements. | Select the child element or add `/text()` to the query. |
| Old values | Google stores imported results for a time. | Wait for the stored result to refresh, and avoid building formulas that rely on instant updates. |
| Garbled characters | The page uses an unusual encoding or HTML entities. | Replace the leftover entities with SUBSTITUTE, for example `=SUBSTITUTE(A2,"&amp;","&")`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Closest alternatives: Power Query with the From Web connector for HTML, or WEBSERVICE with FILTERXML for well-formed XML on Windows. |
| Google Sheets | Available | Reads XML, HTML, CSV, TSV, RSS and ATOM sources, and takes an optional locale argument. |

## Tips and Best Practices

- Build and test the XPath in the browser console with `$x("//your/xpath")` before you paste it into a sheet.
- Prefer id attributes over class names or positions, because ids change less often than page layout.
- Use the page source (Ctrl+U) rather than the inspected page to confirm the data is in the HTML that IMPORTXML reads.
- Wrap every import in IFERROR so one failed page does not break the reports that depend on it.
- Limit long results with a position test such as `(//a)[position()<=20]`.
- Store page addresses in cells so one formula can be copied down a list and the source can change without editing the formula.
- Check the site's terms of service before you import many pages, and keep the request volume modest.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IFERROR](../Logical/IFERROR.md) | Replaces import errors with a fallback message. |
| [IMPORTDATA](IMPORTDATA.md) | Imports CSV or TSV files without an XPath query. |
| [IMPORTFEED](IMPORTFEED.md) | Imports RSS or Atom feed items directly. |
| [IMPORTHTML](IMPORTHTML.md) | Imports tables and lists from a web page. |
| [QUERY](../Google-specific/QUERY.md) | Filters and sorts the results that IMPORTXML returns. |
| [WEBSERVICE](WEBSERVICE.md) | The Excel function for fetching data from a web service. |

## Official Documentation

- [Google Docs Editors Help: IMPORTXML function](https://support.google.com/docs/answer/3093342)
