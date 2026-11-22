---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
purpose:
  - Data Retrieval
use-case:
  - Currency Rate Lookups
  - Intranet Status Checks
  - Public API Data Pulls
related:
  - ENCODEURL
  - FILTERXML
  - IFERROR
  - IMPORTDATA
  - IMPORTXML
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/webservice-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Web Service Call
tags:
  - api
  - excel
  - web-import
  - web-service
---

# WEBSERVICE

## Description

**WEBSERVICE** calls a web service and returns the data the service sends back into one cell. Use it when a public or intranet service provides the data and the formula should fetch it on demand. The function returns the raw response, so you usually wrap it in another function such as FILTERXML, which reads XML, or in text functions that pull out the value you need.

Microsoft says the address should be URL-encoded before the call and recommends the ENCODEURL function for that step. The service must be reachable from the computer that runs Excel, so the function works with public services and with intranet services on the same network.

WEBSERVICE works in Windows versions of Excel, including Excel 2016, 2019, 2021, 2024, and Microsoft 365. It relies on Windows features, so it does not return results on Mac, and Excel for the web does not support it. Google Sheets has no WEBSERVICE function; the closest alternatives are IMPORTDATA, IMPORTXML, and IMPORTHTML.

## Syntax

```excel
=WEBSERVICE(url)
```

<!-- Image 1: WEBSERVICE Call Flow. See Images/Web/WEBSERVICE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `url` | Yes | The address of the web service call, including `https://`. Encode the address first and keep it to 2,048 characters or fewer. Reference a cell when the address is built from other values. |

### Return Value

The data that the web service returns. The function returns `#VALUE!` when it cannot retrieve data, when the result is invalid or exceeds the 32,767-character cell limit, when the address is longer than 2,048 characters, or when the protocol is unsupported, such as `ftp://` or `file://`.

## Examples

### Example 1: Call a Service From a Cell Address

```excel
=WEBSERVICE(A2)
```

**Result:** The raw response from the address in A2, such as a block of XML text.

Keeping the address in one cell lets you change the endpoint without editing the formula. Each row can call a different address.

### Example 2: Extract One Value From an XML Response

```excel
=FILTERXML(WEBSERVICE(A2), "//rate")
```

**Result:** The text of the first `rate` element in the response, when the response is well-formed XML and contains that element.

FILTERXML needs valid XML, so this pattern works only with services that return XML. Check the response format in a browser before you build the formula.

### Example 3: Show a Fallback When the Call Fails

```excel
=IFERROR(WEBSERVICE(A2), "Service unavailable")
```

**Result:** The service response, or "Service unavailable" when the call returns an error.

A failed call should not break the cells that depend on it. The fallback text makes the failure visible to readers.

<!-- Image 2: Error Results Panel. See Images/Web/WEBSERVICE.md -->

### Example 4: Check the Address Length First

```excel
=IF(LEN(A2)<=2048, WEBSERVICE(A2), "URL too long")
```

**Result:** The service response when the address fits within 2,048 characters, and "URL too long" when it does not.

Long addresses often come from many filter values joined together. Checking the length first avoids a `#VALUE!` error and tells the user what went wrong.

## Story Problems

### Problem 1: Long Request Addresses

A reporting team builds request addresses from many filter values. Column B holds the length of each address, calculated with LEN.

| Request | Address Length |
| --- | --- |
| Regional Sales | 1820 |
| Product Stock | 2105 |
| Monthly Refunds | 2048 |
| Store Hours | 980 |

**Task:** Count the requests that WEBSERVICE can send.

**Solution:**

```excel
=COUNTIF(B2:B5,"<=2048")
```

**Answer:** `3`, because 1820, 2048, and 980 are at or under the limit. The 2105-character address is too long.

<!-- Image 3: Length Check Table. See Images/Web/WEBSERVICE.md -->

### Problem 2: Counting Failed Price Pulls

A parts clerk pulls a price for each item with IFERROR, so a failed call shows the word Unavailable.

| Item | Price Pull |
| --- | --- |
| Filter | 19.42 |
| Hose | Unavailable |
| Gasket | 18.90 |
| Valve | Unavailable |

**Task:** Count the items whose price pull failed.

**Solution:**

```excel
=COUNTIF(B2:B5,"Unavailable")
```

**Answer:** `2`, for the Hose and Valve rows.

## Use Cases

### Currency Rate Lookups

**Scenario:** A finance team pulls a daily exchange rate from a public service that returns XML, one cell per currency pair.

```excel
=FILTERXML(WEBSERVICE("https://www.example.org/rates.xml"), "//rate")
```

**Why It Works:** FILTERXML reads the rate element from the raw response. Replace the placeholder address with the service's real address, and encode any values that change.

### Intranet Status Checks

**Scenario:** An IT team checks a status page on the internal network and wants a simple Up or Down label for each system.

```excel
=IFERROR(IF(ISNUMBER(SEARCH("OK",WEBSERVICE(C2))),"Up","Down"),"Down")
```

**Why It Works:** The search looks for the word OK in the response. If the call fails, the outer IFERROR returns Down, so an unreachable system is not reported as healthy.

### Public API Data Pulls

**Scenario:** A research analyst pulls a regional total from a public API and needs a clear message when the service does not respond.

```excel
=IFERROR(FILTERXML(WEBSERVICE(B2), "//total"), "Check service")
```

**Why It Works:** The address in B2 can change by row, and the message tells the analyst to look at the service rather than trusting a blank cell.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The call cannot retrieve data, the response is too large, the address is longer than 2,048 characters, or the protocol is unsupported. | Check the address length, use `https://`, and confirm the service responds in a browser. |
| No result on Mac | WEBSERVICE relies on Windows features. | Run the formula in Excel on Windows, or use Power Query. |
| Call fails with special characters | Spaces or symbols in the address were not encoded. | Encode the address with ENCODEURL before the call. |
| Raw text in the cell | WEBSERVICE returns the response as-is. | Wrap the call in FILTERXML or text functions to extract the value. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Windows versions of Excel 2016, 2019, 2021, 2024, and Microsoft 365 | Returns the raw response. Not available in Excel for the web, and no results on Mac. |
| Google Sheets | Not available | Closest alternatives: IMPORTDATA for CSV or TSV, IMPORTXML for XML and HTML with XPath, and IMPORTHTML for tables. |

## Tips and Best Practices

- Encode the address with ENCODEURL before the call, as Microsoft recommends.
- Keep each address under 2,048 characters, the limit Microsoft gives for a GET request.
- Parse XML responses with FILTERXML and other formats with text functions.
- Wrap each call in IFERROR so one failed service does not break a whole report.
- Test the address in a browser first to confirm the service responds and returns the data you expect.
- Do not place secret keys in the address, because anyone who opens the sheet can read the formula.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ENCODEURL](ENCODEURL.md) | Encodes the address before the call. |
| [FILTERXML](FILTERXML.md) | Extracts values from the XML that WEBSERVICE returns. |
| [IFERROR](../Logical/IFERROR.md) | Provides a fallback when the call fails. |
| [IMPORTDATA](IMPORTDATA.md) | Google Sheets alternative for CSV or TSV data. |
| [IMPORTXML](IMPORTXML.md) | Google Sheets alternative for XML and HTML with XPath. |

## Official Documentation

- [Microsoft Support: WEBSERVICE function](https://support.microsoft.com/en-us/excel/functions/webservice-function)
