---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Google Data Services
purpose:
  - Data Import
use-case:
  - Logo Placement
  - Product Catalog Thumbnails
related:
  - ARRAYFORMULA
  - ENCODEURL
  - HYPERLINK
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/image-function
  - https://support.google.com/docs/answer/3093333
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cell Image
  - Insert Image
tags:
  - excel
  - images
  - sheets
---

# IMAGE

## Description

**IMAGE** places a picture from a web address into a cell. The picture scales to the cell, or to a size you set, and it updates when the address in the source cell changes. Use it for product thumbnails, logos, status icons or photo lists that should stay in sync with a data table.

The sizing argument is the part that differs most between platforms. In Google Sheets, `mode` 1 fits the image inside the cell, 2 stretches it to fill the cell, 3 keeps the original size and 4 uses the height and width you give. In Excel, `sizing` 0 fits the image, 1 fills the cell, 2 keeps the original size and 3 uses your height and width. The same number therefore means different things in each program, so check the mode before you copy a formula between them.

The address must be a full web address that uses `https`, and the image must be in a supported format such as PNG, JPG or GIF. Google Sheets does not accept SVG files or links to drive.google.com, and it does not allow a volatile function such as RAND in the address. Excel also supports WEBP, except on the web and Android, where it is unsupported.

## Syntax

Google Sheets:

```text
IMAGE(url, [mode], [height], [width])
```

Excel:

```excel
=IMAGE(source, [alt_text], [sizing], [height], [width])
```

<!-- Image 1: Sizing Modes by Platform. See Images/Lookup & Reference/IMAGE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `url` or `source` | Yes | The image address, including the protocol, in quotes or as a cell reference. Excel requires `https`. |
| `mode` or `alt_text` | No | Google Sheets `mode` sets the sizing from 1 to 4. Excel `alt_text` is a description for screen readers. |
| `sizing` | No | Excel only. `0` fits the image, `1` fills the cell, `2` keeps the original size and `3` uses the height and width. |
| `height` and `width` | No | Pixel values. Google Sheets needs `mode` set to 4, and Excel needs `sizing` set to 3. |

### Return Value

The image shown inside the cell. If the source cannot be read, the cell shows an error rather than the image, so wrap the call in IFERROR when a blank or text fallback is better.

## Examples

### Example 1: Show an Image Fitted to the Cell (Google Sheets)

```excel
=IMAGE("https://example.com/images/logo.png")
```

**Result:** The logo appears inside the cell at its proportions. Google Sheets uses mode 1 when no mode is given.

The default fits the image so that the whole picture is visible.

### Example 2: Set a Custom Size (Google Sheets)

Cell `B2` holds the image address.

```excel
=IMAGE(B2, 4, 60, 120)
```

**Result:** The image appears 60 pixels high and 120 pixels wide.

Mode 4 tells Sheets to use the height and width that follow. Height comes before width in this argument order.

### Example 3: Set a Custom Size With Alt Text (Excel)

```excel
=IMAGE("https://example.com/images/logo.png", "Company logo", 3, 60, 120)
```

**Result:** The logo appears 60 pixels high and 120 pixels wide, with the alt text `Company logo` for screen readers.

In Excel, sizing 3 uses the height and width, and the second argument provides the description.

### Example 4: Fit the Image in Excel

Cell `B2` holds the image address.

```excel
=IMAGE(B2, "Product photo", 0)
```

**Result:** The product photo fits inside the cell and keeps its proportions.

Sizing 0 scales the picture to fit without distorting it.

### Example 5: Show Text When the Image Fails

Cell `B2` holds the image address.

```excel
=IFERROR(IMAGE(B2, 2), "Image not available")
```

**Result:** The image stretched to fill the cell, or the text `Image not available` if the address cannot be loaded.

IFERROR gives the reader a clear message when the source is missing or blocked.

## Story Problems

### Problem 1: Thumbnails for a Product List

A store lists each product's photo address in column B of a sheet, with the SKU in column A. The thumbnails must be 80 by 80 pixels in Google Sheets.

| SKU | Photo Address |
| --- | --- |
| LMP-01 | https://example.com/photos/lmp-01.jpg |
| DSK-07 | https://example.com/photos/dsk-07.jpg |

**Task:** Write the formula for row 2 that places the photo at 80 by 80 pixels.

**Solution:**

```excel
=IMAGE(B2, 4, 80, 80)
```

**Answer:** The photo appears at 80 pixels high and 80 pixels wide. Copying the formula down places a thumbnail in each row.

### Problem 2: Original Size Sign Image

A shop keeps a sign image at a fixed size and shows it in Excel without scaling.

| Sign | Address |
| --- | --- |
| Open | https://example.com/signs/open.png |

**Task:** Write the Excel formula for cell `B2` that shows the sign at its original size, with the alt text `Open sign`.

**Solution:**

```excel
=IMAGE("https://example.com/signs/open.png", "Open sign", 2)
```

**Answer:** The image appears at its original pixel size. Sizing 2 keeps that size, so the picture may extend beyond the cell boundary.

<!-- Image 2: Thumbnail Grid. See Images/Lookup & Reference/IMAGE.md -->

## Use Cases

### Logo Placement

**Scenario:** A monthly report must carry the company logo at a fixed size in its header cell.

```excel
=IMAGE("https://example.com/brand/logo.png", "Company logo", 3, 40, 120)
```

**Why It Works:** Sizing 3 fixes the height and width, so the logo keeps the same footprint whatever the column widths are.

### Product Catalog Thumbnails

**Scenario:** A catalog sheet shows a thumbnail for each product, pulled from the photo address in a column that the team keeps updated.

```excel
=IMAGE(Products!D2, 4, 80, 80)
```

**Why It Works:** The photo address lives in the product table, so changing the link in the table changes the thumbnail. The fixed size keeps the rows evenly spaced.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Image does not appear | The address is not a full web address or uses an unsupported protocol. | Include `https://` in the address and test it in a browser. |
| Image does not appear (Google Sheets) | The address points to drive.google.com or to an SVG file. | Host the image at a direct image address, in a supported format. |
| Error in a formula that uses RAND or NOW | A volatile function is inside the image address. | Build the address from fixed text and a cell value. |
| Image is distorted | The height and width do not match the image's proportions. | Use mode 1 or sizing 0 to keep the aspect ratio. |
| Size ignored | The mode or sizing value is not set to the custom option. | Set Google Sheets mode to 4 or Excel sizing to 3. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2024 and Excel for the web, plus mobile versions | Syntax is `IMAGE(source, [alt_text], [sizing], [height], [width])`. Sizing 0 fits, 1 fills, 2 keeps the original size and 3 sets a custom size. The address must use `https`. |
| Google Sheets | Available | Syntax is `IMAGE(url, [mode], [height], [width])`. Mode 1 fits, 2 stretches, 3 keeps the original size and 4 sets a custom size. SVG files and drive.google.com links are not supported. |

## Tips and Best Practices

- Check the mode or sizing number on each platform, because the same number means a different size setting in Excel and in Sheets.
- Use mode 4 or sizing 3 with a height and width when a table needs even rows.
- Keep image addresses in a column of the source table so the picture updates when the address changes.
- Wrap the call in IFERROR to show a clear message when an image cannot be loaded.
- Use short, meaningful alt text in Excel so screen readers can describe the picture.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ARRAYFORMULA](../Google-specific/ARRAYFORMULA.md) | Applies IMAGE to every row of a range in Google Sheets at once. |
| [ENCODEURL](../Web/ENCODEURL.md) | Encodes text so it can be placed safely inside a web address. |
| [HYPERLINK](HYPERLINK.md) | Creates a clickable link, which can accompany an image in the same row. |

## Official Documentation

- [Microsoft Support: IMAGE function](https://support.microsoft.com/en-us/excel/functions/image-function)
- [Google Docs Editors Help: IMAGE](https://support.google.com/docs/answer/3093333)
