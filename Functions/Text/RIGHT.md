---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Text Manipulation
use-case:
  - File Extension Routing
  - Invoice Number Suffixes
  - Zip Code Extraction
related:
  - FIND
  - LEFT
  - LEN
  - MID
  - RIGHTB
  - TEXTAFTER
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/right-function
  - https://support.google.com/docs/answer/3094087
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Extract Right
  - Right Characters
tags:
  - excel
  - sheets
  - substring
  - text-extraction
---

# RIGHT

## Description

**RIGHT** returns a set number of characters from the end of a text string. Use it when the part you need sits at the end of a value, such as a file extension, a check digit, a zip code at the end of an address, or the last digits of an invoice number.

RIGHT always returns text, even when the extracted characters are digits. A value such as `00457` keeps its leading zeros. Convert it with VALUE when the result must be used in a calculation.

The second argument is optional. When it is omitted, RIGHT returns one character. The count must be zero or greater. If the count is larger than the length of the text, RIGHT returns the whole text without an error. A count of zero returns empty text.

Spaces count as characters. A trailing space in a source cell changes the result, so trim the source with TRIM when the data comes from another system. For a part of text that follows a delimiter, FIND or TEXTAFTER is usually simpler than a count based on LEN.

## Syntax

```excel
=RIGHT(text, [num_chars])
```

<!-- Image 1: Text and Character Count Anatomy. See Images/Text/RIGHT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to extract from. It can be a literal string in quotes, a cell reference, or a formula that returns text. A number is converted to text first. |
| `num_chars` | No | The number of characters to return from the end. Must be zero or greater. The default is 1, and a count larger than the text returns the whole text. |

### Return Value

Text containing the rightmost `num_chars` characters of `text`. The result is always text, even when it looks like a number. Empty text is returned when the count is zero or the source is empty.

## Examples

### Example 1: Extract the Last Five Characters

```excel
=RIGHT("INV-00457", 5)
```

**Result:** `00457`

The last five characters are the sequence number. The leading zeros stay because the result is text.

### Example 2: Return One Character by Default

```excel
=RIGHT("ABCDEF")
```

**Result:** `F`

The second argument is omitted, so RIGHT returns the final character. This suits check characters stored at the end of a code.

### Example 3: Read a File Extension

```excel
=RIGHT("report_2025.xlsx", 4)
```

**Result:** `xlsx`

The four characters at the end are the extension without the dot. Use five characters to include the dot.

### Example 4: Keep the Last Four Digits of a Card Number

```excel
=RIGHT(A2, 4)
```

**Result:** `0366` when A2 contains `4532015112830366`

Only the last four digits are returned. Combine the result with LEFT or a masking formula when a receipt must show a partial number.

### Example 5: Read the UTC Offset From a Timestamp

```excel
=RIGHT("2025-08-17T14:30:00-05:00", 6)
```

**Result:** `-05:00`

The last six characters are the time zone offset. The offset is text and can be compared or displayed directly.

### Example 6: Count Larger Than the Text

```excel
=RIGHT("Hi", 10)
```

**Result:** `Hi`

The count is larger than the text, so the whole text is returned without an error.

<!-- Image 2: Invoice Suffix Extraction. See Images/Text/RIGHT.md -->

## Story Problems

### Problem 1: Read Invoice Suffixes

An accounts payable clerk receives invoice numbers from several vendors. The last five characters of each number are the sequence number used in the payment log. The clerk needs the sequence for each invoice.

| Invoice Number |
| --- |
| INV-00457 |
| ACME-88213 |
| PO-5 |

**Task:** Extract the last five characters from each invoice number, and state the result for the first invoice.

**Solution:**

```excel
=RIGHT(A2, 5)
```

**Answer:** `00457` for the first invoice, `88213` for the second, and `PO-5` for the third because that invoice number has only four characters, so the whole text is returned.

### Problem 2: Route Files by Extension

A file intake sheet sends each uploaded file to a handler based on its extension. The handler for `.pdf` files must receive every PDF, whether the name is long or short.

| File Name |
| --- |
| summary.pdf |
| report_Q1.xlsx |
| export.csv |

**Task:** Return the extension of the first file, without the dot.

**Solution:**

```excel
=RIGHT(A2, 3)
```

**Answer:** `pdf`. The last three characters of `summary.pdf` form the extension, so the handler is chosen from that value.

<!-- Image 3: File Routing Flow. See Images/Text/RIGHT.md -->

## Use Cases

### File Extension Routing

**Scenario:** An automated workflow sends each file to a handler based on its type.

```excel
=IF(RIGHT(A2, 4) = "xlsx", "Spreadsheet Queue", IF(RIGHT(A2, 3) = "pdf", "PDF Queue", "Manual Review"))
```

**Why It Works:** Each extension has its own length, so the formula checks the longer extension first. Filenames with no matching extension go to manual review.

### Invoice Number Suffixes

**Scenario:** A payment log matches payments by the last six digits of each invoice number, which are unique within a vendor.

```excel
=VALUE(RIGHT(TRIM(A2), 6))
```

**Why It Works:** TRIM removes stray spaces, RIGHT takes the last six characters, and VALUE turns them into a number for matching. Use it only where the suffix is always numeric.

### Zip Code Extraction

**Scenario:** Shipping addresses end with a five-digit zip code, and the team needs the code for zone assignment.

```excel
=RIGHT(TRIM(A2), 5)
```

**Why It Works:** Trimming first keeps a trailing space from pushing the zip code out of the last five characters. Check a few addresses that include a four-digit extension before relying on the result.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected characters | The source ends with a space that you cannot see. | Wrap the source in TRIM. |
| Leading zeros lost | The result was converted to a number elsewhere. | Keep the value as text, or format the column as text. |
| Formula fails | `num_chars` is negative, which the function does not allow. | Keep the count at zero or greater, using MAX(0, value) for calculated counts. |
| Calculation returns an error | The extracted text is not numeric. | Check the source value with ISNUMBER before wrapping the result in VALUE. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | The Microsoft page lists RIGHTB as deprecated and says that RIGHT supports Unicode surrogate pairs in Compatibility Version 2. |
| Google Sheets | Available | Same arguments and default. The page gives no separate note on negative counts. RIGHTB is also available in Sheets for byte-based extraction. |

## Tips and Best Practices

- Trim the source with TRIM before extracting, especially for data from exports and forms.
- Use FIND or TEXTAFTER to find the start of a suffix that follows a delimiter, rather than counting characters by hand.
- Convert with VALUE only when the result will be calculated, and keep codes as text otherwise.
- Test with a short value, an empty cell and a value that is shorter than the count.
- Combine RIGHT with LEFT and MID when you need to split a value into fixed parts.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LEFT](LEFT.md) | Returns characters from the start of the text, the mirror of RIGHT. |
| [MID](MID.md) | Returns characters from any position in the text. |
| [TEXTAFTER](TEXTAFTER.md) | Returns the text that follows a delimiter, which is simpler than a count for many suffixes. |
| [FIND](FIND.md) | Locates a delimiter so the count can be calculated from it. |
| [LEN](LEN.md) | Returns the length of the text, used with FIND to size the count. |
| [RIGHTB](RIGHTB.md) | Returns the rightmost bytes, for double-byte text. |

## Official Documentation

- [Microsoft Support: RIGHT function](https://support.microsoft.com/en-us/excel/functions/right-function)
- [Google Docs Editors Help: RIGHT](https://support.google.com/docs/answer/3094087)
