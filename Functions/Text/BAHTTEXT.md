---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Number Formatting
use-case:
  - Bilingual Price Quotes
  - Thai Cheque Amounts
  - Thai Invoice Totals
related:
  - DOLLAR
  - FIXED
  - NUMBERVALUE
  - TEXT
  - VALUE
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/bahttext-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Baht Text
  - Thai Baht Text
tags:
  - baht
  - currency
  - excel
  - number-to-text
---

# BAHTTEXT

## Description

**BAHTTEXT** converts a number into Thai text and adds the Thai word for the baht currency. The result spells out the amount in Thai script, so an invoice or cheque can show the total in words next to the numeric total. It is an Excel function with no Google Sheets equivalent.

Use BAHTTEXT on Thai invoices, quotes and payment documents where the law or the customer expects the amount written in words. The function takes one number, so combine it with SUM or a cell reference when the total comes from several lines.

The output uses Thai characters, so the cell and any printed copy need a font that includes Thai glyphs. Microsoft notes that the Baht format can be changed in the Windows Regional and Language Options, which affects how the currency is displayed on that computer.

<!-- Image 1: Amount in Words Beside the Numeric Total. See Images/Text/BAHTTEXT.md -->

## Syntax

```excel
=BAHTTEXT(number)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A number, a cell reference that contains a number, or a formula that returns a number. |

### Return Value

A Thai text string that spells out the number and ends with the baht word. Text that cannot be read as a number produces an error.

## Examples

### Example 1: Spelling Out a Whole Amount

```excel
=BAHTTEXT(A2)
```

Where `A2` contains `560`.

**Result:** Thai text that reads five hundred sixty baht.

The function returns the Thai words for the amount and the baht suffix.

### Example 2: Combining Text With the Amount in Words

```excel
="Amount due: " & BAHTTEXT(B2)
```

Where `B2` contains `2400`.

**Result:** The label `Amount due:` followed by Thai text that reads two thousand four hundred baht.

The ampersand joins a fixed label to the spelled-out amount.

### Example 3: Spelling Out a Total From Several Lines

```excel
=BAHTTEXT(SUM(C2:C4))
```

Where `C2:C4` contain `120`, `230` and `50`.

**Result:** Thai text that reads four hundred baht.

The three values add up to 400, and the function spells out that total.

<!-- Image 2: Amount in Words in an Invoice Layout. See Images/Text/BAHTTEXT.md -->

## Story Problems

### Problem 1: Thai Invoice Total in Words

A small office invoice lists three lines in `A1:B4`.

| Line | Amount |
| --- | --- |
| Notebook | 300 |
| Pen box | 135 |
| Folder | 100 |

**Task:** Write the invoice total in Thai words in cell `D2`.

**Solution:**

```excel
=BAHTTEXT(SUM(B2:B4))
```

**Answer:** Thai text that reads five hundred thirty five baht, because 300 + 135 + 100 = 535.

### Problem 2: Bilingual Quote Total

A consultant quotes two services in `A1:B3`.

| Service | Fee |
| --- | --- |
| Setup | 2000 |
| Support | 1500 |

**Task:** Show the quote total in Thai words in cell `D2`.

**Solution:**

```excel
=BAHTTEXT(SUM(B2:B3))
```

**Answer:** Thai text that reads three thousand five hundred baht, because 2000 + 1500 = 3500.

## Use Cases

### Thai Invoice Totals

**Scenario:** A supplier in Thailand must print the invoice total in words under the line items.

```excel
=BAHTTEXT(SUM(Invoice[Line Total]))
```

**Why It Works:** The words update whenever a line changes, so the written total and the numeric total cannot drift apart. Check the printed output with a Thai font before sending.

### Thai Cheque Amounts

**Scenario:** An accounts team writes the payment amount in words on a cheque template.

```excel
=BAHTTEXT(Payments!C2)
```

**Why It Works:** The formula reads the approved payment amount from the register, so the cheque text always matches the register entry. Print one test copy to confirm the layout.

### Bilingual Price Quotes

**Scenario:** A quote shows the amount in English and in Thai words for a client in Bangkok.

```excel
="Total: " & TEXT(B5, "#,##0") & " baht (" & BAHTTEXT(B5) & ")"
```

**Why It Works:** TEXT shows the numeric amount with separators, and BAHTTEXT adds the spelled-out version, so both forms come from one cell.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text that cannot be read as a number. | Convert the value with VALUE or NUMBERVALUE first. |
| Boxes or question marks instead of Thai letters | The font does not include Thai characters. | Use a font with Thai glyphs in the cell and in the printed copy. |
| Baht wording looks different on another computer | The Baht format is set in the Windows Regional and Language Options. | Set the same regional format on each computer that prints the output. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019, Excel 2016 and Microsoft Office | Spells out the number in Thai text with the baht suffix. |
| Google Sheets | Not available | Closest alternative: TEXT with a currency format, which shows the number as currency but not in words. |

## Tips and Best Practices

- Build the total in a single cell first, then point BAHTTEXT at it so the words follow one source.
- Test the output with a Thai-capable font before you print a batch of documents.
- Check the regional setting on every machine that prints the same document.
- Keep the numeric total beside the words so readers can compare them.
- Round or check decimals with the finance team before printing an amount that includes satang.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DOLLAR](DOLLAR.md) | Formats a number as currency text, but keeps the digits. |
| [FIXED](FIXED.md) | Formats a number with a fixed number of decimals as text. |
| [NUMBERVALUE](NUMBERVALUE.md) | Converts locale-formatted text back into a number before spelling it out. |
| [TEXT](TEXT.md) | Formats a number with a format code, such as thousands separators. |
| [VALUE](VALUE.md) | Converts text that looks like a number into a number. |

## Official Documentation

- [Microsoft Support: BAHTTEXT function](https://support.microsoft.com/en-us/excel/functions/bahttext-function)
