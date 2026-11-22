---
domain: Spreadsheet Functions
category: Web
subcategory: URL Tools
purpose:
  - Data Validation
use-case:
  - Contact List Cleanup
  - Link Checks Before Import
  - Website Field Validation
related:
  - ENCODEURL
  - IMPORTDATA
  - IMPORTXML
  - ISEMAIL
level: 2
source:
  - https://support.google.com/docs/answer/3256501
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Is URL
tags:
  - data-validation
  - sheets
  - url
---

# ISURL

## Description

**ISURL** checks whether a value is a valid web address. It returns `TRUE` when the value is recognized as a URL and `FALSE` when it is not. It tests the text only: it does not open the link or confirm that the page exists.

Use ISURL to clean a column of website addresses before you import them, turn them into links, or send them to another system. A fully qualified address is not always required, because Google notes that `http` and `www` are not needed in every case. Recognized protocols include ftp, http, https, gopher, mailto, news, telnet, and aim.

A value can return `FALSE` even when it looks right if its top-level domain is not on Google's list. Check unexpected `FALSE` results by hand before you delete them.

ISURL is available only in Google Sheets. Excel has no equivalent function.

## Syntax

```excel
=ISURL(value)
```

<!-- Image 1: ISURL Input and Result. See Images/Web/ISURL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value to test as a URL. Usually a cell reference, or a value typed in quotes. |

### Return Value

`TRUE` when the value is recognized as a URL, and `FALSE` when it is not. Ordinary text does not produce an error.

## Examples

### Example 1: Test a Full Address

```excel
=ISURL("https://www.google.com")
```

**Result:** `TRUE`

A complete address with a recognized protocol and a common domain passes the test.

### Example 2: Test Plain Text

```excel
=ISURL("Quarterly report")
```

**Result:** `FALSE`

Plain words with spaces are not web addresses, so the function returns `FALSE`.

### Example 3: Label Each Row

```excel
=IF(ISURL(A2), "Link", "Plain text")
```

**Result:** `Link` when A2 holds `https://www.google.com`, and `Plain text` when A2 holds `Quarterly report`.

Wrapping ISURL in IF turns the test into a label that a filter or a colleague can read at a glance.

<!-- Image 2: Label Column Result. See Images/Web/ISURL.md -->

## Story Problems

### Problem 1: Checking a Contact List

A bookshop keeps a list of partner names and their websites in columns A and B. Some entries are real addresses and some are notes.

| Name | Website |
| --- | --- |
| Harbor Cafe | https://www.google.com |
| Pine Tailors | Pine Tailors website |
| Cedar Books | www.wikipedia.org |
| Maple Studio | Ask at the front desk |

**Task:** Put the ISURL result for each row in column C, then count the rows that hold a valid address.

**Solution:**

```excel
=COUNTIF(C2:C5,TRUE)
```

**Answer:** `2`, because the Harbor Cafe and Cedar Books rows return `TRUE` and the other two rows return `FALSE`. Column C uses `=ISURL(B2)` copied down from C2 to C5.

<!-- Image 3: Contact Check Count. See Images/Web/ISURL.md -->

### Problem 2: Labeling a Partner Link Column

A sales team collects partner links in column B. Some rows are still waiting for a link.

| Partner | Link |
| --- | --- |
| Acme Supply | https://www.google.com |
| Birch Labs | Not yet provided |
| Dune Media | www.wikipedia.org |
| Elm Print | Pending |

**Task:** Label each row `Link` or `Missing` in column C.

**Solution:**

```excel
=IF(ISURL(B2), "Link", "Missing")
```

**Answer:** `Link`, `Missing`, `Link`, `Missing` for rows 2 to 5, because only the first and third rows hold addresses.

## Use Cases

### Contact List Cleanup

**Scenario:** A marketing team imports a mailing list where the website column mixes addresses with notes.

```excel
=IF(ISURL(B2), B2, "Fix this address")
```

**Why It Works:** Valid addresses pass through unchanged, and every other row gets a reminder to fix it. The team can filter on the reminder text to find the rows to correct.

### Link Checks Before Import

**Scenario:** A research analyst imports the title of each source page but wants to skip rows that are not addresses.

```excel
=IF(ISURL(A2), IMPORTXML(A2, "//title"), "Not a URL")
```

**Why It Works:** The import runs only for rows that pass the check, so no import requests go out for notes or blank entries.

### Website Field Validation

**Scenario:** An operations manager receives a form export and needs to know how many website answers need follow-up.

```excel
=COUNTIF(C2:C500,FALSE)
```

**Why It Works:** Column C holds one ISURL result per row, and COUNTIF counts the `FALSE` results. Match the range to the rows that actually contain data.

## Common Errors

| Result | Cause | Fix |
| --- | --- | --- |
| `FALSE` for a valid-looking address | The top-level domain is not on Google's list, or the text has a typo or stray spaces. | Correct the typo, remove the spaces, and test the address in a browser. |
| `FALSE` for an address with an unusual prefix | The protocol is not on Google's recognized list. | Use `https://` or `http://`. |
| `TRUE` for a dead page | ISURL checks the text, not the page. | Pair it with IMPORTXML or IMPORTDATA to confirm that the page responds. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Closest alternative: `=ISNUMBER(SEARCH("://",A2))`, which checks only for a protocol separator and does not validate the domain. |
| Google Sheets | Available | Returns `TRUE` or `FALSE`. Recognized protocols include ftp, http, https, gopher, mailto, news, telnet, and aim. |

## Tips and Best Practices

- Run ISURL before an import function so that no request goes out for a value that is not an address.
- Keep the result in a helper column so you can filter for `FALSE` rows and fix them.
- Use IF with a readable label when other people will use the sheet.
- Confirm a `TRUE` result with IMPORTDATA or IMPORTXML when you need to know the page responds.
- Check the protocol list before you reject a value with an unusual prefix.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ENCODEURL](ENCODEURL.md) | Encodes text so it can be used inside a web address. |
| [IMPORTDATA](IMPORTDATA.md) | Imports a CSV or TSV file from a valid URL. |
| [IMPORTXML](IMPORTXML.md) | Imports elements from a web page after the address passes the check. |
| [ISEMAIL](../Information/ISEMAIL.md) | Checks whether a value is a valid email address. |

## Official Documentation

- [Google Docs Editors Help: ISURL function](https://support.google.com/docs/answer/3256501)
