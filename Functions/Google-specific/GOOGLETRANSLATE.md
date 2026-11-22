---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Google Data Services
purpose:
  - Text Manipulation
use-case:
  - Customer Message Translation
  - Multilingual Product Labels
  - Support Ticket Review
related:
  - AI
  - DETECTLANGUAGE
  - IFERROR
  - TRIM
level: 2
source:
  - https://support.google.com/docs/answer/3093331
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Google Translate
tags:
  - language
  - sheets
  - text
  - translation
---

# GOOGLETRANSLATE

## Description

**GOOGLETRANSLATE** translates text from one language into another and returns the result in the cell. It is useful for a first pass at translating customer messages, product labels or short notes so that a team can read them without leaving the sheet.

The function takes the text and two optional language codes. When you omit the source language, it detects the language automatically, using the value `"auto"`. When you omit the target language, it uses the system language of the sheet. Language codes are two letters, such as `"en"` for English, `"es"` for Spanish, `"ja"` for Japanese and `"ko"` for Korean.

The official help page states one rule about the arguments: if you omit the source language, you must also omit the target language. The page does not state character, cell or request limits. For critical translations, such as legal or medical text, have a qualified translator review the output, because machine translation can change meaning. For checking which language a cell is in before translating it, use DETECTLANGUAGE. GOOGLETRANSLATE is available only in Google Sheets.

<!-- Image 1: GOOGLETRANSLATE Language Codes. See Images/Google-specific/GOOGLETRANSLATE.md -->

## Syntax

```excel
=GOOGLETRANSLATE(text, [source_language], [target_language])
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to translate. Put it in quotation marks, or refer to a cell such as `A2`. |
| `source_language` | No | The two-letter code of the language the text is written in, or `"auto"` to detect it. It defaults to `"auto"`. |
| `target_language` | No | The two-letter code of the language to translate into. It defaults to the sheet's system language. |

### Return Value

Text: the translated version of `text`. The official page does not describe an error value for unsupported input, so check the output for blanks or unexpected wording.

## Examples

### Example 1: Translating a Typed Phrase

```excel
=GOOGLETRANSLATE("Hello World", "en", "es")
```

**Result:** A Spanish translation of the phrase. The usual result is `Hola Mundo`, but the wording can vary.

Both language codes are given, so the function does not need to detect the source language.

### Example 2: Translating From a Cell With Automatic Detection

```excel
=GOOGLETRANSLATE(A2)
```

**Result:** The text in A2 translated into the sheet's system language. The source language is detected automatically.

With only the text argument, the function uses the defaults for both languages.

### Example 3: Using Language Codes From Cells

```excel
=GOOGLETRANSLATE(A2, B2, C2)
```

**Result:** The text in A2 translated from the language code in B2 into the code in C2. When B2 holds `"auto"`, the source language is detected.

Putting the codes in cells lets one formula handle messages in several languages across the same sheet.

### Example 4: Translating a List

```excel
=ARRAYFORMULA(GOOGLETRANSLATE(A2:A5, "auto", "en"))
```

**Result:** One English translation for each cell in A2:A5, placed down the column.

Wrap the formula in ARRAYFORMULA to process the whole list from a single cell.

<!-- Image 2: GOOGLETRANSLATE Translated List. See Images/Google-specific/GOOGLETRANSLATE.md -->

## Story Problems

### Problem 1: Translating Support Messages

A help desk received four messages in different languages in `A2:A5`. The team wants English versions in column C.

| Message |
| --- |
| Mi pedido llegó dañado. |
| Le paquet n'est pas arrivé. |
| Die Rechnung ist falsch. |
| Gracias por la rápida respuesta. |

**Task:** Translate each message into English in `C2:C5`, then count how many translations are filled in.

**Solution:**

```excel
=GOOGLETRANSLATE(A2, "auto", "en")
```

Fill this formula down `C2:C5`, then count the filled cells with `=COUNTA(C2:C5)` in a separate cell.

**Answer:** `4`, one English translation for each message. The wording of each translation depends on the service, so a team member should read them before replying.

### Problem 2: Checking for Untranslated Labels

A product catalog has five labels in `A2:A6`, and two of them are still blank. The team wants a count of the labels that have a translation in column B.

| Label | Translation |
| --- | --- |
| Red mug | Taza roja |
| Blue bowl | |
| Green plate | Plato verde |
| Yellow vase | |
| White cup | Taza blanca |

**Task:** Count how many translations are filled in, so the team knows how many labels still need work.

**Solution:**

```excel
=COUNTA(B2:B6)
```

**Answer:** `3`, because the Spanish labels for the red mug, the green plate and the white cup are filled in. The blue bowl and the yellow vase still need a translation.

## Use Cases

### Customer Message Translation

**Scenario:** A customer service team receives messages in several languages and needs an English copy beside each one.

```excel
=IFERROR(GOOGLETRANSLATE(A2, "auto", "en"), "Translate manually")
```

**Why It Works:** Setting the source to auto lets the function handle mixed languages in one column. IFERROR shows a reminder when a message cannot be translated, so no row is left silent.

### Multilingual Product Labels

**Scenario:** An online shop keeps product names in English and needs Spanish and French labels for its catalog.

```excel
=GOOGLETRANSLATE(A2, "en", "es")
```

**Why It Works:** The source language is fixed because the catalog is written in English. A second column with `"fr"` in place of `"es"` produces French labels with the same pattern.

### Support Ticket Review

**Scenario:** A support lead reviews tickets written in several languages and wants a quick English version to decide which team should handle each one.

```excel
=GOOGLETRANSLATE(TRIM(A2), "auto", "en")
```

**Why It Works:** TRIM removes extra spaces before the text is translated, so stray spaces do not affect the output. The English text helps the lead route the ticket.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Blank result | The text cell is empty, or a language code is not valid. | Check that the cell has text and that the codes are two-letter codes such as `en` or `es`. |
| Wrong language | The source language was set to a code that does not match the text. | Use `"auto"` for the source language when the text is mixed or unknown. |
| Argument error | The source language was omitted while the target language was given. | Give both codes, or omit both as the official page requires. |
| Meaning lost | Machine translation changed the sense of an idiom or a technical term. | Have a qualified person review important translations. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available. Excel has no built-in translation function, so an add-in or an external flow is the closest alternative. | Excel users typically translate with a separate tool and paste the results. |
| Google Sheets | Available | Uses two-letter language codes, detects the source language when set to `"auto"`, and defaults the target to the sheet's system language. |

## Tips and Best Practices

- Use `"auto"` for the source language when the input mixes languages.
- Store language codes in cells so the same formula works for every language in the list.
- Wrap GOOGLETRANSLATE in IFERROR for production sheets, so a failed row shows a clear message.
- Clean the text with TRIM first, which keeps spacing differences from changing the output.
- Use DETECTLANGUAGE to check which language a cell is written in before you rely on the translation.
- Review translations of legal, medical or safety text with a qualified translator before they are used.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AI](AI.md) | Generates text from a prompt, which can also rewrite or summarize content in another language. |
| [DETECTLANGUAGE](../Text/DETECTLANGUAGE.md) | Identifies the language of text, so you can check the source before translating. |
| [IFERROR](../Logical/IFERROR.md) | Shows a fallback message when a translation cannot be produced. |
| [TRIM](../Text/TRIM.md) | Removes extra spaces from the text before it is translated. |

## Official Documentation

- [Google Docs Editors Help: GOOGLETRANSLATE](https://support.google.com/docs/answer/3093331)
