---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
purpose:
  - Data Import
  - Data Retrieval
use-case:
  - Order Lookup From Web Service
  - Shipment Status Tables
  - XML Status Responses
related:
  - ENCODEURL
  - IFERROR
  - IMPORTXML
  - WEBSERVICE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/filterxml-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - XML Filter
  - XPath Extract
tags:
  - excel
  - web-queries
  - xml-parsing
  - xpath
---

# FILTERXML

## Description

**FILTERXML** reads a block of XML text and returns the single value that an XPath expression points to. XPath is a path language for XML: `//order/customer` means every `customer` element inside an `order` element, and a bracket such as `[1]` picks one element from a list. FILTERXML gives Excel a way to pull one field out of an XML document without any macros or manual copying.

The most common use is with WEBSERVICE. WEBSERVICE fetches raw text from a web address, and FILTERXML reads the XML inside that text. Build the address with ENCODEURL when a parameter contains spaces or punctuation.

FILTERXML is an Excel function only. It is available in Microsoft 365, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 on Windows, and it is not available in Excel for the web or Excel for Mac. Google Sheets has no FILTERXML; the closest equivalent is IMPORTXML.

## Syntax

```excel
=FILTERXML(xml, xpath)
```

<!-- Image 1: XML Input and XPath Expression. See Images/Web/FILTERXML.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `xml` | Yes | A text string in valid XML format, entered as a quoted literal or as a cell reference. A web response from WEBSERVICE is passed here directly. |
| `xpath` | Yes | A standard XPath expression that identifies the element or attribute to return. Positions in brackets start at 1. |

### Return Value

The value of the element or attribute that the XPath selects. Numeric values can be used in arithmetic, such as `=FILTERXML(...)*2`. If `xml` is not valid XML, the function returns `#VALUE!`.

## Examples

Every example below uses this XML in cell `A1`:

```text
<orders><order id="1001"><customer>Harbor Cafe</customer><total>248.50</total></order><order id="1002"><customer>Pine Books</customer><total>73.25</total></order></orders>
```

### Example 1: Select by Position

```excel
=FILTERXML(A1, "//order[1]/customer")
```

**Result:** `Harbor Cafe`

The path finds every `order` element, takes the first one, and returns its `customer` text. XPath positions start at 1, not 0.

### Example 2: Select by Attribute Value

```excel
=FILTERXML(A1, "//order[@id='1002']/total")
```

**Result:** `73.25`

The predicate `[@id='1002']` finds the order whose `id` attribute is `1002`, regardless of its position. This is safer than a position when records may be added or sorted.

<!-- Image 2: Selecting a Node by Attribute. See Images/Web/FILTERXML.md -->

### Example 3: Return an Attribute

```excel
=FILTERXML(A1, "//order[2]/@id")
```

**Result:** `1002`

The `@` sign selects an attribute instead of an element. Use it when the value you need is stored in an attribute such as `id`.

### Example 4: Calculate With an Extracted Value

```excel
=FILTERXML(A1, "//order[1]/total")*2
```

**Result:** `497`

The first order total is `248.50`, and doubling it gives 497.

### Example 5: Handle Invalid XML

```excel
=IFERROR(FILTERXML("<order><total>", "//total"), "Invalid XML")
```

**Result:** `Invalid XML`

The text is missing its closing tags, so it is not valid XML and FILTERXML returns `#VALUE!`. IFERROR replaces that error with a readable message.

## Story Problems

### Problem 1: Total Weight of Two Shipments

A logistics clerk receives one XML status record per shipment. Each record is stored as text in column B, and the weight is in the `weight_kg` element.

| Shipment | XML Status Record (Column B) |
| --- | --- |
| Shipment 1 | `<shipment><status>Delivered</status><weight_kg>12.4</weight_kg><carrier>NorthWay</carrier></shipment>` |
| Shipment 2 | `<shipment><status>Delayed</status><weight_kg>8.75</weight_kg><carrier>RiverFreight</carrier></shipment>` |

**Task:** Find the combined weight of both shipments in kilograms.

**Solution:**

```excel
=FILTERXML(B2,"//weight_kg")+FILTERXML(B3,"//weight_kg")
```

**Answer:** `21.15`, because 12.4 + 8.75 = 21.15.

### Problem 2: Carrier for a Delayed Shipment

The same clerk needs the carrier for the shipment whose status is `Delayed`, which is the record in `B3`.

**Task:** Return the carrier name for the delayed shipment.

**Solution:**

```excel
=FILTERXML(B3,"//carrier")
```

**Answer:** `RiverFreight`. The status in `B3` is `Delayed`, and its `carrier` element holds `RiverFreight`.

<!-- Image 3: Shipment Status Records in Column B. See Images/Web/FILTERXML.md -->

## Use Cases

### Order Lookup From Web Service

**Scenario:** A logistics system returns an XML record for any order number, and the team wants the customer name in a sheet without copying it by hand.

```excel
=FILTERXML(WEBSERVICE("https://api.example.com/orders?number="&ENCODEURL(A2)),"//order/customer")
```

**Why It Works:** WEBSERVICE returns the XML as text, FILTERXML reads the customer element, and ENCODEURL protects the order number in the address. Confirm the XML structure in a browser first, because the XPath must match the service's element names.

### Shipment Status Tables

**Scenario:** Each row holds the XML status record for one shipment, and the team wants the status in its own column.

```excel
=FILTERXML($B2,"//status")
```

**Why It Works:** The column reference is anchored with `$`, so the formula can be filled down to read every row. Each row returns its own status, such as `Delivered` or `Delayed`.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The `xml` argument is not valid XML, or it contains a namespace prefix that is not valid. | Check that every tag is closed, there is one root element, and any namespace prefix is declared. |
| Wrong value returned | The XPath selects a different element than intended, or the position is off by one. | Test the path on a small sample. Remember that positions start at 1, or use an attribute predicate such as `[@id='1002']`. |
| Formula returns no usable result in Excel for the web | FILTERXML is not available in Excel for the web. | Open the workbook in desktop Excel on Windows to calculate the formula. |
| Formula returns no usable result on Mac | FILTERXML relies on Windows features and does not return results on Mac. | Use desktop Excel on Windows for the calculation. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel 2024, Excel 2021, Excel 2019 and Excel 2016, and Microsoft Office and My Office for iPhone | Not available in Excel for the web or Excel for Mac. Returns the value as stored in the XML, so check the result type before doing arithmetic on it. |
| Google Sheets | Not available | Use IMPORTXML, which applies an XPath query to XML or HTML fetched from a URL. |

## Tips and Best Practices

- Test each XPath on a short sample of XML before connecting it to a web service.
- Prefer attribute predicates such as `[@id='1002']` to positions when records can move.
- Remember that XPath positions start at 1.
- Use WEBSERVICE to fetch the XML and FILTERXML to read it, and keep both in one formula only when the result is stable.
- Wrap formulas that depend on a web service in IFERROR so the sheet shows a message instead of an error.
- Build query parameters with ENCODEURL, so spaces and punctuation do not change the request.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ENCODEURL](ENCODEURL.md) | Encodes a parameter that is placed in the address WEBSERVICE fetches. |
| [IFERROR](../Logical/IFERROR.md) | Replaces `#VALUE!` from invalid XML with a readable message. |
| [IMPORTXML](IMPORTXML.md) | Google Sheets counterpart that applies an XPath query to a URL. |
| [WEBSERVICE](WEBSERVICE.md) | Fetches the raw XML text that FILTERXML reads. |

## Official Documentation

- [Microsoft Support: FILTERXML function](https://support.microsoft.com/en-us/excel/functions/filterxml-function)
