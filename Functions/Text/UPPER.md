---
domain: Spreadsheet Functions
category: Text
subcategory: Case Conversion
purpose:
  - Text Manipulation
use-case:
  - Customer Name Cleanup
  - Product Code Formatting
  - Report Heading Formatting
related:
  - CONCAT
  - EXACT
  - LOWER
  - PROPER
  - TRIM
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/upper-function
  - https://support.google.com/docs/answer/3094219
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Convert To Uppercase
  - Uppercase Text
tags:
  - case-conversion
  - excel
  - sheets
  - text
---

# UPPER

## Description

**UPPER** converts every letter in a text string to capital letters. Numbers, spaces and punctuation stay as they are, so `sku-4417b` becomes `SKU-4417B`. Use it to standardize codes, names and labels that people type in mixed case.

UPPER changes only the display text it returns. The original cell keeps its contents. To change the case of the first letter of each word instead of every letter, use PROPER. To change every letter to lowercase, use LOWER.

Comparisons in Excel and Google Sheets already ignore case, so `="yes"="YES"` returns TRUE. UPPER is useful for building a standard key or a heading, not for making a comparison work. When a case-sensitive test is needed, use EXACT.

## Syntax

```excel
=UPPER(text)
```

<!-- Image 1: Input and Output Cells. See Images/Text/UPPER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to convert. It can be a cell reference or a text string in quotation marks. A number is converted to text and returned unchanged. |

### Return Value

A text string with every letter in capitals. The function does not return an error for ordinary text. An empty cell returns an empty string.

## Examples

### Example 1: Convert a Text String

```excel
=UPPER("quarterly budget")
```

**Result:** `QUARTERLY BUDGET`

The text in quotation marks is converted letter by letter.

### Example 2: Convert a Cell Reference

Cell `A2` contains `sku-4417b`.

```excel
=UPPER(A2)
```

**Result:** `SKU-4417B`

The hyphen and the digits stay the same; only the letter `b` changes.

### Example 3: Capitalize Only the First Letter

Cell `A2` contains `mARCH`.

```excel
=UPPER(LEFT(A2,1))&LOWER(MID(A2,2,100))
```

**Result:** `March`

LEFT takes the first character and UPPER capitalizes it. MID takes the rest of the text, and LOWER makes it lowercase. The 100 is a length large enough for most text; it can be any number at least as long as the text.

<!-- Image 2: Chained Case Functions. See Images/Text/UPPER.md -->

### Example 4: Case-Sensitive Check After Conversion

Cell `A2` contains `yes`, and the test needs a standard uppercase value.

```excel
=EXACT(UPPER(A2),"YES")
```

**Result:** `TRUE`

UPPER makes the value `YES`, and EXACT then compares it with `YES` case-sensitively.

## Story Problems

### Problem 1: Warehouse Bin Codes

A warehouse export lists bin codes in mixed case. The codes must be uppercase before they are printed on shelf labels.

| Bin Code |
| --- |
| ab-102 |
| Kx-7 |
| mn-330 |
| qp-18 |
| Zt-045 |

**Task:** Convert each bin code in column A to uppercase in column B.

**Solution:**

```excel
=UPPER(A2)
```

Fill the formula down from `B2` to `B6`.

**Answer:** `AB-102`, `KX-7`, `MN-330`, `QP-18` and `ZT-045`. Each code keeps its hyphen and digits and only the letters change.

### Problem 2: Matching Customer Names

A sales list records the same customer with different spacing and capitalization. Counting the rows for `ACME LTD` requires a standard key.

| Customer |
| --- |
| acme ltd |
| Acme Ltd |
| ACME LTD |
| Birch Co |
| acme LTD |

**Task:** Count the rows that refer to `ACME LTD`, ignoring extra spaces and capitalization.

**Solution:**

```excel
=SUMPRODUCT(--(UPPER(TRIM(A2:A6))="ACME LTD"))
```

**Answer:** `4`. TRIM removes the leading and trailing spaces, UPPER standardizes the capitalization, and rows 2, 3, 4 and 6 match. The Birch Co row does not match.

## Use Cases

### Product Code Formatting

**Scenario:** A purchasing team receives product codes from several suppliers, and some use lowercase letters. Every code must match the uppercase format in the inventory system.

```excel
=UPPER(TRIM(B2))
```

**Why It Works:** TRIM removes stray spaces first, then UPPER gives every code the same format before it is pasted into the inventory import.

### Customer Name Cleanup

**Scenario:** A contact list was typed by hand, so names appear in capitals, lowercase or mixed case. A mailing label needs the last name in capitals for sorting.

```excel
=UPPER(C2)&", "&B2
```

**Why It Works:** The last name in column C is capitalized and joined with the first name in column B. The original cells stay unchanged.

### Report Heading Formatting

**Scenario:** A monthly report title is built from a region name in cell `B1`, and the heading must appear in capitals.

```excel
="SALES REPORT: "&UPPER(B1)
```

**Why It Works:** The fixed text is already in capitals, and UPPER converts only the region name, so the heading updates when the region changes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Numbers look unchanged | UPPER changes only letters. Digits and symbols are returned as they are. | This is expected. Check the letters only. |
| Result is still mixed case | The formula refers to an empty or different cell, or the cell was not filled down. | Check the reference and copy the formula to every row. |
| Extra spaces remain | UPPER does not remove spaces. | Wrap the text in TRIM: `=UPPER(TRIM(A2))`. |
| Case test gives an unexpected result | UPPER changes display text only, and comparisons already ignore case. | Use EXACT for a case-sensitive comparison. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions, including Excel for the web | Works the same way in Windows and Mac versions. |
| Google Sheets | Available | Same syntax and behavior as Excel. |

## Tips and Best Practices

- Wrap the input in TRIM when the source comes from a manual entry or an export, so extra spaces do not affect the result.
- Keep the original column and write the uppercase version in a helper column, so the source data stays available.
- Use UPPER only for display or for a standard key; use EXACT when the case of the text must match exactly.
- Fill the formula down with a table or a named range so new rows are converted automatically.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LOWER](../Text/LOWER.md) | Converts every letter to lowercase. |
| [PROPER](../Text/PROPER.md) | Capitalizes the first letter of each word. |
| [EXACT](../Text/EXACT.md) | Compares two texts case-sensitively. |
| [TRIM](../Text/TRIM.md) | Removes extra spaces before or after conversion. |
| [CONCAT](../Text/CONCAT.md) | Joins converted text with other text. |

## Official Documentation

- [Microsoft Support: UPPER function](https://support.microsoft.com/en-us/excel/functions/upper-function)
- [Google Docs Editors Help: UPPER](https://support.google.com/docs/answer/3094219)
