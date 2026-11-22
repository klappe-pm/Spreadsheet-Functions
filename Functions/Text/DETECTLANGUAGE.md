---
domain: Spreadsheet Functions
category: Text
subcategory: Google Data Services
purpose:
  - AI Assistance
  - Text Manipulation
use-case:
  - Multilingual Support Tickets
  - Routing Customer Messages
  - Tagging Product Descriptions
related:
  - AI
  - GOOGLETRANSLATE
  - IF
  - LEN
  - TRIM
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/detectlanguage-function
  - https://support.google.com/docs/answer/3093278
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Detect Language
tags:
  - excel
  - google-ai
  - language-detection
  - sheets
---

# DETECTLANGUAGE

## Description

**DETECTLANGUAGE** returns the language code of a piece of text, such as `en` for English or `es` for Spanish. It is useful for sorting messages, routing requests and tagging content by language before another step, such as translation, runs on the text.

In Excel, DETECTLANGUAGE is a service-backed function that uses Microsoft Translation Services. The supported languages and results can change as languages are added or removed. Excel reads one text value, which must be a text cell or a text string. Heavy use can reach a daily quota, and Excel returns an error when the quota is exceeded.

In Google Sheets, DETECTLANGUAGE identifies the language used in the text, and accepts either one text value or a one-dimensional column range. When the range holds several languages, only the first text found is evaluated. Use GOOGLETRANSLATE when you need the translated text rather than the language code.

<!-- Image 1: Detected Codes in a Ticket List. See Images/Text/DETECTLANGUAGE.md -->

## Syntax

```excel
=DETECTLANGUAGE(text)
```

Google Sheets uses the argument name `text_or_range` and accepts a one-dimensional column range.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to evaluate, or a reference to a cell that contains text. In Google Sheets, a column range is also accepted. |

### Return Value

A language code, such as `es` for Spanish. Excel returns an error when the text is too long, when the input is not text, or when the daily quota is exceeded.

## Examples

### Example 1: Detecting the Language of One Cell

```excel
=DETECTLANGUAGE(A2)
```

Where `A2` contains a sentence written in German.

**Result:** `de`, the code for German.

The function returns the code for the language of the sentence.

### Example 2: Detecting a Column in Google Sheets

```excel
=DETECTLANGUAGE(A2:A7)
```

**Result:** The code for the first language found in the range.

In Google Sheets, only the first text found in a multi-language range is evaluated, so split mixed columns into separate ranges before detection.

### Example 3: Routing Messages That Are Not in English

```excel
=IF(DETECTLANGUAGE(A2)<>"en", "Translation Queue", "Standard Queue")
```

**Result:** `Translation Queue` for a German message, `Standard Queue` for an English message.

The formula sends only messages in other languages to the translation step.

### Example 4: Skipping Blank Cells

```excel
=IF(LEN(TRIM(A2))=0, "", DETECTLANGUAGE(A2))
```

**Result:** An empty cell for a blank row, and the language code for a filled row.

Checking for blank text first avoids errors when the column has gaps.

<!-- Image 2: Routing Table With Language Codes. See Images/Text/DETECTLANGUAGE.md -->

## Story Problems

### Problem 1: Language Tags for Support Tickets

A help desk logs three messages in `A1:B4`.

| Ticket | Message |
| --- | --- |
| 101 | Ich kann mich nicht anmelden. |
| 102 | My invoice is wrong. |
| 103 | Mi pedido llegó dañado. |

**Task:** Return the detected language code for each message in column C.

**Solution:**

```excel
=DETECTLANGUAGE(B2)
```

Fill this formula down to `C4`.

**Answer:** The expected codes are `de`, `en` and `es`, for German, English and Spanish. Detection can vary with short text, so confirm the codes in your own copy before relying on them.

### Problem 2: Routing by Language

The codes from Problem 1 are in column C.

**Task:** Send every message that is not English to the translation queue, and every English message to the standard queue.

**Solution:**

```excel
=IF(C2<>"en", "Translation Queue", "Standard Queue")
```

Fill this formula down to `D4`.

**Answer:** Tickets 101 and 103 go to the translation queue, and ticket 102 goes to the standard queue.

## Use Cases

### Multilingual Support Tickets

**Scenario:** A help desk receives messages in many languages and sends the non-English ones to a translation team.

```excel
=IF(DETECTLANGUAGE(B2)<>"en", "Translation Queue", "Standard Queue")
```

**Why It Works:** The formula reads the language code and compares it with English. The queue label then drives the routing, so the team sees the right tickets without reading each message.

### Tagging Product Descriptions

**Scenario:** A product catalog must record the language of every description, and some rows are empty.

```excel
=IF(LEN(TRIM(A2))=0, "", DETECTLANGUAGE(A2))
```

**Why It Works:** The blank check prevents an error on empty rows, and the language code fills the tag column for the rest. Copy the results as values once they are reviewed, to avoid repeated calls against the quota.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `Error in Value` | The input is not text. | Check the source, and convert numbers or dates to text before detection. |
| `Text Too Long` | The cell contains more characters than the function accepts. | Detect the language on a shorter sample, such as the first sentence with LEFT. |
| `Request Throttled` | The daily quota for the function has been exceeded. | Wait for the quota to reset, or reduce repeated calls. |
| Unexpected code | The text is very short or mixes languages. | Test with a longer sample of the message. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel Mobile and Office for iPhone | Service-backed, with a daily quota. Supported languages may change. |
| Google Sheets | Available | Accepts one text value or a one-dimensional column range. Only the first text found in a multi-language range is evaluated. |

## Tips and Best Practices

- Blank out empty rows with a LEN and TRIM check before calling the function.
- Sample long text with LEFT to stay within the length limit.
- Replace formulas with their results once the codes are checked, to save quota.
- Use GOOGLETRANSLATE after detection when the translated text is needed.
- Split mixed-language columns in Google Sheets so each range has one language.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AI](../Google-specific/AI.md) | Runs a prompt on a cell, which can also classify text by language. |
| [GOOGLETRANSLATE](../Google-specific/GOOGLETRANSLATE.md) | Translates text after its language has been detected. |
| [IF](../Logical/IF.md) | Routes or tags rows based on the detected code. |
| [LEN](LEN.md) | Checks whether a cell is empty before detection runs. |
| [TRIM](TRIM.md) | Removes spaces so blank cells are detected correctly. |

## Official Documentation

- [Microsoft Support: DETECTLANGUAGE function](https://support.microsoft.com/en-us/excel/functions/detectlanguage-function)
- [Google Docs Editors Help: DETECTLANGUAGE](https://support.google.com/docs/answer/3093278)
