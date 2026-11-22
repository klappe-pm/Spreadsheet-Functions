---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
purpose:
  - Data Import
use-case:
  - Blog Publishing Calendar
  - Competitor Press Release Tracker
  - Industry News Monitor
related:
  - FILTER
  - IMPORTDATA
  - IMPORTHTML
  - IMPORTXML
  - QUERY
  - SORT
level: 2
source:
  - https://support.google.com/docs/answer/3093337
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Import Atom
  - Import RSS
tags:
  - atom
  - data-import
  - rss
  - sheets
  - syndication
---

# IMPORTFEED

## Description

**IMPORTFEED** reads an RSS or Atom feed and writes its content into the sheet. Feeds are the standard XML formats that blogs, news sites, podcasts and video channels use to publish new items. The formula fetches the feed at the address you give, so the sheet reflects the items the publisher currently lists.

The `query` argument chooses what comes back: a single attribute of the feed, such as its title, the full table of items, or one attribute of each item, such as its title or link. Choosing one attribute keeps the sheet small when only one column is needed.

Use IMPORTFEED to build a monitor, such as a list of article titles and links from several industry sites. Sort and filter the results with SORT, FILTER or QUERY. Use IMPORTHTML instead when the information is a table on a web page rather than a feed.

IMPORTFEED is a Google Sheets function. Excel has no built-in equivalent, as described under Platform Differences.

## Syntax

```excel
=IMPORTFEED(url, [query], [headers], [num_items])
```

<!-- Image 1: Feed Address and Optional Arguments. See Images/Web/IMPORTFEED.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `url` | Yes | The address of an RSS or Atom feed, including the protocol such as `https://`. Enter it in quotes or as a reference to a cell. |
| `query` | No | What to return. The default is `"items"`. Valid values are `"feed"`, `"feed title"`, `"feed description"`, `"feed author"`, `"feed url"`, `"items"`, `"items title"`, `"items summary"`, `"items url"` and `"items created"`. |
| `headers` | No | `TRUE` adds a header row above the returned values. The default is `FALSE`. |
| `num_items` | No | For item queries, how many items to return, counting from the most recent. If omitted, every item the feed currently publishes is returned. |

### Return Value

A single row for `"feed"`, a table for `"items"`, and a single attribute for the feed and item attribute queries. When `headers` is `TRUE`, one extra row of column labels appears above the result. The official documentation does not state a maximum number of items.

## Examples

### Example 1: Full Item Table

```excel
=IMPORTFEED("https://example.com/news/feed.xml")
```

**Result:** A table of the feed's items, with each item's fields in columns and no header row.

The default query is `"items"`, so this formula is the same as adding `"items"` as the second argument.

### Example 2: Item Table With Headers

```excel
=IMPORTFEED("https://example.com/news/feed.xml","items",TRUE)
```

**Result:** The same item table with one header row above it.

Set `headers` to `TRUE` when the sheet will be shared or when QUERY needs a header row to skip.

### Example 3: Latest Five Items

```excel
=IMPORTFEED("https://example.com/news/feed.xml","items",TRUE,5)
```

**Result:** Six rows: a header row followed by the five most recent items.

The `num_items` argument counts from the most recent item, so the newest five appear first.

### Example 4: Titles of the Latest Twelve Items

```excel
=IMPORTFEED("https://example.com/news/feed.xml","items title",FALSE,12)
```

**Result:** Twelve item titles in a single column, with no header row.

A single-attribute query returns only the column that is asked for, which keeps the sheet tidy.

<!-- Image 2: A Single-Attribute Query. See Images/Web/IMPORTFEED.md -->

### Example 5: Feed Title for a Section Label

With `A2` holding a feed address:

```excel
=IMPORTFEED(A2,"feed title")
```

**Result:** One cell that holds the feed's title.

Use this as a section heading in a multi-source dashboard, so each block is labeled with its source.

### Example 6: Publication Dates

```excel
=IMPORTFEED("https://example.com/news/feed.xml","items created",FALSE,10)
```

**Result:** The publication dates of the ten most recent items, one per row.

Check the values with a date function before doing date arithmetic, because the sheet shows whatever the feed provides.

### Example 7: Keyword Filter Without Assuming Column Order

With `A2` holding a feed address:

```excel
=FILTER(IMPORTFEED(A2,"items url",FALSE,50),ISNUMBER(SEARCH("budget",IMPORTFEED(A2,"items title",FALSE,50))))
```

**Result:** The links of the most recent fifty items whose titles contain the word `budget`.

Two imports of the same feed return rows in the same order, so FILTER can match the title test to the link column. This avoids depending on which column the feed places each field in.

### Example 8: Titles From Two Feeds Stacked

With `A2` and `A3` holding two feed addresses:

```excel
={IMPORTFEED(A2,"items title",FALSE,5);IMPORTFEED(A3,"items title",FALSE,5)}
```

**Result:** Ten titles in one column: the five newest from the first feed, followed by the five newest from the second.

Single-attribute queries keep both results to one column, so they stack cleanly.

## Story Problems

### Problem 1: Six Rows for Five Newest Items

A communications analyst wants the five newest items from a press feed, with a header row, in a sheet that shares the feed address in `B1`.

**Task:** Write the formula that returns the five newest items with headers. Then state how many rows the result has.

**Solution:**

```excel
=IMPORTFEED(B1,"items",TRUE,5)
```

**Answer:** `6` rows. The header row adds one row to the five items.

### Problem 2: Counting Titles From a Feed

A team tracks the twelve newest titles from a blog feed in `B1`. They want the titles in one column with no header, and they need the number of rows to check that the feed returned enough items.

**Task:** Write a formula that returns the number of rows in the list of twelve titles.

**Solution:**

```excel
=ROWS(IMPORTFEED(B1,"items title",FALSE,12))
```

**Answer:** `12`. The query returns one title per item, and `num_items` limits the list to twelve.

## Use Cases

### Industry News Monitor

**Scenario:** A marketing team checks five trade publications each morning for articles that mention their product category.

```excel
=FILTER(IMPORTFEED(A2,"items url",FALSE,30),ISNUMBER(SEARCH("cloud storage",IMPORTFEED(A2,"items title",FALSE,30))))
```

**Why It Works:** The formula keeps the links of recent articles whose titles mention the category. Copy the formula to a row for each publication, with its feed address in column A.

### Competitor Press Release Tracker

**Scenario:** An analyst lists competitor press release feeds and needs the newest title from each one.

```excel
=IMPORTFEED(A2,"items title",FALSE,1)
```

**Why It Works:** `num_items` set to 1 returns the most recent title, which keeps each row small and easy to scan. Fill the formula down the list of feed addresses.

### Blog Publishing Calendar

**Scenario:** A content manager wants to see when a blog published its last ten posts, to plan the next publishing date.

```excel
=IMPORTFEED("https://example.com/blog/feed.xml","items created",FALSE,10)
```

**Why It Works:** The formula lists the post dates for the ten newest items. The content manager can count the gaps between dates to see the publishing pattern.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error or no data | The address is a web page, not a feed. | Find the feed link in the page source, which usually appears as an RSS or Atom link, and use that address. |
| Error from an address that works in a browser | The feed requires a login or blocks automated requests. | Use a public feed address. IMPORTFEED takes only a URL, so it cannot send credentials. |
| Error on a query | The query text is not one of the listed values. | Use an exact query string from the Parameters table, including the space in `"items title"`. |
| More rows than expected | `num_items` was left out, so every item the feed publishes is returned. | Add `num_items` to limit the result to the number you need. |
| New post does not appear | The publisher has not added it to the feed yet. | Open the feed address in a browser and confirm the new item is listed. |
| Date arithmetic fails | The `items created` value is text, not a date. | Check the value type before calculating. Convert text dates with DATEVALUE. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Excel has no feed function. Use Power Query (Data, Get Data, From Web) to read an XML feed, or a tool such as Power Automate. |
| Google Sheets | Available | One formula with optional query, headers and item-count arguments. |

## Tips and Best Practices

- Find the feed address in the page source, not the address shown in the browser bar.
- Limit results with `num_items` so the dashboard stays small and fast.
- Choose a single-attribute query such as `"items title"` when only one column is needed.
- Use FILTER with a second IMPORTFEED call on the same feed to select rows by keyword without assuming the column order.
- Wrap the formula in IFERROR on shared dashboards, for example `=IFERROR(IMPORTFEED(A2,"items",TRUE,10),"Feed unavailable")`.
- Keep feed addresses in one labeled column so each source can be changed in one place.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Selects feed rows that match a condition. |
| [IMPORTDATA](IMPORTDATA.md) | Imports CSV or TSV files instead of feeds. |
| [IMPORTHTML](IMPORTHTML.md) | Imports a table or list from a web page. |
| [IMPORTXML](IMPORTXML.md) | Applies an XPath query to XML or HTML from a URL. |
| [QUERY](../Google-specific/QUERY.md) | Filters, sorts and reshapes imported items. |
| [SORT](../Lookup%20%26%20Reference/SORT.md) | Orders imported items by date or title. |

## Official Documentation

- [Google Docs Editors Help: IMPORTFEED](https://support.google.com/docs/answer/3093337)
