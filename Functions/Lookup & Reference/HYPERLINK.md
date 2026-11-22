---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
purpose:
  - Reference Building
use-case:
  - Policy Document Links
  - Project File Index
related:
  - ADDRESS
  - ENCODEURL
  - IMAGE
  - INDIRECT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/hyperlink-function
  - https://support.google.com/docs/answer/3093313
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Clickable Link
  - Web Link
tags:
  - excel
  - links
  - sheets
---

# HYPERLINK

## Description

**HYPERLINK** turns a cell into a clickable link. The first argument is the destination, which can be a web address, an email address, a file path or a location inside the same workbook. The optional second argument is the text that the cell shows. Use it to build an index of documents, add a link that opens a related sheet, or create a mailto link that starts a message.

The destination can come from another cell, so a list of URLs can become a column of clickable labels. Keep the link text short and descriptive, because users see the text, not the address. When you leave out the label, the cell shows the destination itself.

Excel and Google Sheets accept the same basic syntax, with a few differences. Excel can point to a cell or named range inside the workbook by starting the destination with `#`, and it can open local files. Google Sheets accepts web, mail and a few other protocols, and it adds `http://` to any address that has no protocol. In Excel for the web, only URLs work as destinations.

## Syntax

```excel
=HYPERLINK(link_location, [friendly_name])
```

<!-- Image 1: Link Cell and Display Text. See Images/Lookup & Reference/HYPERLINK.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `link_location` | Yes | The destination: a URL in quotes, a cell that holds one, a file path, or a location in the workbook that starts with `#`. |
| `friendly_name` | No | The text the cell shows, which can be typed text, a number or a cell reference. Leave it out to show the destination. |

Google Sheets uses the same idea with the names `HYPERLINK(url, [link_label])`. Its destination must include a supported protocol, such as `https://` or `mailto:`, or Sheets adds `http://` for you.

### Return Value

The text or number shown in the cell, displayed as a link that opens the destination when clicked. The function returns the friendly name, or the destination if no name is given. If the friendly name refers to an error, the cell shows that error.

## Examples

### Example 1: A Link With Display Text

```excel
=HYPERLINK("https://example.com/policies/travel", "Travel Policy")
```

**Result:** `Travel Policy` (a clickable link to the travel policy page)

The destination is the web address in quotes. The second argument makes the cell read Travel Policy instead of the full address.

### Example 2: Build a Mail Link From a Cell

Cell `B2` holds the address `dana@example.com`.

```excel
=HYPERLINK("mailto:" & B2, "Email Dana")
```

**Result:** `Email Dana` (opens a new message to dana@example.com when clicked)

The ampersand joins the mailto prefix to the address, so the link stays correct when the address changes.

### Example 3: Link to a Location in the Same Workbook

```excel
=HYPERLINK("#Summary!A1", "Go to Summary")
```

**Result:** `Go to Summary` (jumps to cell A1 on the Summary sheet)

In Excel, a destination that begins with `#` refers to a location inside the current workbook. Google Sheets links to a sheet differently, so use this form in Excel workbooks.

### Example 4: Use a Cell for the Label

Cell `A2` holds the text `Q2 Budget` and cell `B2` holds `https://example.com/budget/q2`.

```excel
=HYPERLINK(B2, A2)
```

**Result:** `Q2 Budget` (a clickable link to the budget page)

Because both arguments come from cells, the list can grow without rewriting the formula.

### Example 5: Show the Address When No Label Is Given

```excel
=HYPERLINK("https://example.com/help")
```

**Result:** `https://example.com/help` (a clickable link that shows the address)

Omitting the second argument makes the address itself the visible text.

### Example 6: Make an Invisible Hotspot

Cell `C5` holds the address `https://example.com/archive` and `D5` holds the text `Archive`.

```excel
=HYPERLINK(C5, "")
```

**Result:** A blank-looking cell that opens the archive page when clicked.

An empty label hides the text but keeps the link working. Use this sparingly, because readers cannot see where the cell leads.

## Story Problems

### Problem 1: Policy Document Index

An HR coordinator keeps the policy titles and web addresses in `A2:B4`.

| Policy | Address |
| --- | --- |
| Leave Policy | https://example.com/hr/leave |
| Expense Policy | https://example.com/hr/expenses |
| Remote Work | https://example.com/hr/remote |

**Task:** In `C2`, create a clickable link for the first policy that shows the policy title as its label.

**Solution:**

```excel
=HYPERLINK(B2, A2)
```

**Answer:** The cell shows `Leave Policy` as a link to https://example.com/hr/leave. Copying the formula down to `C4` produces the other two links.

### Problem 2: Email Links for a Contact List

A sales team keeps contact names and email addresses in `A2:B4`.

| Name | Email |
| --- | --- |
| Priya Nair | priya@example.com |
| Lee Brooks | lee@example.com |
| Sam Ortiz | sam@example.com |

**Task:** In `C2`, create a link that opens a new email to the contact, with the label `Email Priya Nair` built from the name cell.

**Solution:**

```excel
=HYPERLINK("mailto:" & B2, "Email " & A2)
```

**Answer:** The cell shows `Email Priya Nair`. Clicking it opens a message addressed to priya@example.com.

<!-- Image 2: Policy and Email Links. See Images/Lookup & Reference/HYPERLINK.md -->

## Use Cases

### Policy Document Links

**Scenario:** A company intranet index lists every policy with a clickable title, so staff can open a document from a single sheet.

```excel
=HYPERLINK(Policies!C2, Policies!A2)
```

**Why It Works:** The address and title come from the source list, so editing the list updates every link without touching the index formula.

### Project File Index

**Scenario:** A project lead keeps a folder index in which each row links to the document's location and shows its name.

```excel
=HYPERLINK(Files!B2, Files!A2)
```

**Why It Works:** The label comes from the file name and the destination from the path, so the index stays readable and accurate when files are renamed in the list.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Link does not open | The destination is missing a protocol or contains a typo. | Include `https://` or `mailto:`, and test the address in a browser. |
| Link does not open (Excel) | The destination points to a location that no longer exists. | Update the cell or range reference after the sheet is renamed. |
| Error shown instead of text | The friendly name refers to a cell that contains an error. | Check the referenced cell, or wrap the label in IFERROR. |
| Formula returns a plain address | The destination is not a supported link format in Google Sheets. | Use a supported protocol such as `https://`, `http://`, or `mailto:`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Microsoft 365 and Excel for the web | Destinations can be URLs, file paths or `#` references inside the workbook. In Excel for the web, only URLs work. |
| Google Sheets | Available | Supports `http://`, `https://`, `mailto:` and a few other protocols. Adds `http://` to addresses without a protocol. An empty label keeps the link working in an empty-looking cell. |

## Tips and Best Practices

- Build the destination from a cell so one list drives every link in a column.
- Use short, descriptive labels, because readers scan the text and rarely see the full address.
- Use a leading `#` in Excel to link to a cell or named range in the same workbook.
- Include the protocol in every address in Google Sheets so the link is never treated as plain text.
- Avoid empty labels for links that readers need to find, because the cell gives no clue about its destination.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ADDRESS](../Lookup%20%26%20Reference/ADDRESS.md) | Builds a cell address as text, which can be used in a `#` link destination. |
| [ENCODEURL](../Web/ENCODEURL.md) | Encodes text so it can be placed safely inside a web address. |
| [IMAGE](IMAGE.md) | Shows a picture in a cell, which can be combined with a link. |
| [INDIRECT](../Lookup%20%26%20Reference/INDIRECT.md) | Converts text into a reference, the way a dynamic link target can be built. |

## Official Documentation

- [Microsoft Support: HYPERLINK function](https://support.microsoft.com/en-us/excel/functions/hyperlink-function)
- [Google Docs Editors Help: HYPERLINK](https://support.google.com/docs/answer/3093313)
