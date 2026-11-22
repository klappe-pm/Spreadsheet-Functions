---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
related:
  - FILTERXML
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - web
  - xml-parsing
---

# FILTERXML Image Guide

Images planned for [FILTERXML](../../Functions/Web/FILTERXML.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: XML Input and XPath Expression

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a worksheet cell and a formula. |
| Content | Cell `A1` holds a short XML text with two `order` elements. The formula `=FILTERXML(A1, "//order[1]/customer")` sits in an adjacent cell. Arrows connect the `xml` argument to the XML text and the `xpath` argument to the highlighted `customer` element inside the first `order`. |
| Alt Text | A diagram of a FILTERXML formula with its XML input and XPath argument linked to the matching parts of the XML text. |
| File Name | FILTERXML XML Input XPath.png |

## Image 2: Selecting a Node by Attribute

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 2. |
| Format | Two-panel diagram. |
| Content | Left panel shows the XML with the second `order` element highlighted, labeled as position `[2]`. Right panel shows the same XML with the element whose `id` attribute equals `1002` highlighted, labeled `[@id='1002']`. A caption reads: a position changes when records move, an attribute value does not. |
| Alt Text | Two panels comparing selection by position and selection by attribute in an XML document. |
| File Name | FILTERXML Position Versus Attribute.png |

## Image 3: Shipment Status Records in Column B

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, directly below the Problem 2 answer. |
| Format | Screenshot of a worksheet with two rows of XML text in column B. |
| Content | Rows 2 and 3 hold the two shipment records. Row 3 is highlighted because its status is `Delayed`. A callout points to the formula `=FILTERXML(B3,"//carrier")` with the output `RiverFreight` in a result cell. |
| Alt Text | A worksheet with two XML shipment records in one column, the delayed record highlighted, and a FILTERXML result showing the carrier name. |
| File Name | FILTERXML Shipment Records.png |
