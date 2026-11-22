---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Text Manipulation
use-case:
  - Catalog Localization
  - Multilingual Support Queue
  - Supplier Note Review
related:
  - CLEAN
  - IFERROR
  - ISTEXT
  - LEN
  - TRIM
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/translate-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Translate Cell Text
  - Translate Text
tags:
  - excel
  - localization
  - translation
---

# TRANSLATE

## Description

**TRANSLATE** returns the translation of a text string into another language. The translation comes from Microsoft Translation Services, so the function reaches a remote service rather than calculating the result in the sheet. You give it the text, an optional source language and an optional target language, and the translated text appears in the cell.

Use TRANSLATE for a first draft of a translation that a person will review: a product description, a support message or a supplier note. It saves time when a list mixes languages, because the source language can be left out and detected automatically. It is not a substitute for certified translation of legal, medical or regulated text.

The wording of a translation depends on the service and can change as the supported languages are updated. Check results before they are published, and keep the original text in its own column.

## Syntax

```excel
=TRANSLATE(text, [source_language], [target_language])
```

<!-- Image 1: Syntax Anatomy. See Images/Text/TRANSLATE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to translate. Type it in double quotes or refer to a cell that holds it. |
| `source_language` | No | The language code of the source text, such as `"en"` for English or `"es"` for Spanish. When omitted, the language is detected automatically. Specify it for short texts, where detection is less reliable. |
| `target_language` | No | The language code for the translation. When omitted, the system language is used. |

### Return Value

The translated text, shown in the cell that holds the formula. If the translation cannot be produced, the cell shows an error message, such as one of the messages listed under Common Errors.

## Examples

The examples use `A2` for an English product sentence, `A3` for a Spanish customer note, `A4` for an English shipping note, `A5` for an English greeting and `A6` for a German confirmation.

### Example 1: English to Spanish With Both Languages Named

```excel
=TRANSLATE(A2,"en","es")
```

**Result:** a Spanish version of the English sentence in `A2`

Naming both languages skips detection, which gives a more reliable result for short text.

### Example 2: Detect the Source Language

```excel
=TRANSLATE(A3,,"en")
```

**Result:** an English version of the Spanish note in `A3`

The empty second argument tells the function to detect the source language, and the target is English.

### Example 3: English to French

```excel
=TRANSLATE(A4,"en","fr")
```

**Result:** a French version of the shipping note in `A4`

The same pattern works for any supported language code. Change the target code to produce another language.

### Example 4: Fall Back When Translation Fails

```excel
=IFERROR(TRANSLATE(A5,"en","ja"),"Translation unavailable")
```

**Result:** a Japanese version of the greeting, or the text `Translation unavailable` when the service returns an error

IFERROR keeps the sheet readable when the service is unavailable or a language code is rejected.

### Example 5: Use the System Language as the Target

```excel
=TRANSLATE(A6)
```

**Result:** the German confirmation in the language set as the system language

When no target language is given, the function uses the system language. Set the target explicitly in shared sheets so every reader gets the same language.

## Story Problems

### Problem 1: Localize a Product Catalog

A catalog has an English description for each product in column B, and the Spanish storefront needs the same text in column C.

| Product | Description |
| --- | --- |
| Steel water bottle | Keeps drinks cold for a full day. |
| Canvas tote | Folds flat and holds a laptop. |
| Cork coaster set | Protects tables from heat and moisture. |

**Task:** Enter a formula in `C2` that translates the description in `B2` from English to Spanish, then fill it down the column.

**Solution:**

```excel
=TRANSLATE(B2,"en","es")
```

**Answer:** Column C holds a Spanish version of each description. Each row returns a different translation, and the exact wording depends on the service, so a Spanish reviewer should read each row before the catalog is published.

<!-- Image 2: English and Translated Columns. See Images/Text/TRANSLATE.md -->

### Problem 2: Read a Mixed-Language Support Inbox

A support inbox holds messages in German, French and Spanish, and the team reads everything in English. The source language is not recorded.

**Task:** Translate each message in column A to English without naming the source language, then mark any row whose result is an error.

**Solution:**

```excel
=IFERROR(TRANSLATE(A2,,"en"),"Check the message")
```

**Answer:** Column B holds an English version of each message, with the source language detected per row. A message that cannot be translated shows the words `Check the message`, so it can be read in its original language.

## Use Cases

### Catalog Localization

**Scenario:** A small retailer adds Spanish descriptions to each product, and a native speaker reviews every row before the storefront goes live.

```excel
=TRANSLATE(B2,"en","es")
```

**Why It Works:** The target language is fixed, so every row is translated the same way. Keeping the English text in column B means a reviewer can compare both versions.

### Multilingual Support Queue

**Scenario:** A support lead needs to see the subject of each incoming message in English before assigning it.

```excel
=TRANSLATE(A2,,"en")
```

**Why It Works:** Leaving the source language out lets the function detect German, French or Spanish automatically. The English version is enough to route the ticket, and the original text remains in column A for the agent who replies.

### Supplier Note Review

**Scenario:** An operations team receives delivery notes from overseas suppliers and needs to check quantities and dates quickly.

```excel
=TRANSLATE(C2,,"en")
```

**Why It Works:** The translated note supports a quick check. Any figure that matters, such as a quantity or a date, should be confirmed against the original document.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Text Too Long | The text is longer than the cell limit. | Split the text into shorter pieces across several cells, and translate each piece. |
| Error in Value | The cell holds a number, a date or another value that is not text. | Translate only text cells, or convert the value to text with TEXT first. |
| Invalid Language | The language code is not supported. | Use a supported code such as `en`, `es`, `fr`, `de` or `ja`, and check the supported list. |
| Request Throttled | The daily quota for the function has been used. | Wait until the quota resets, or copy the finished translations as values so they are not requested again. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows and Mac), Excel for the web and Excel Mobile | Uses Microsoft Translation Services, so results and supported languages can change over time. |
| Google Sheets | Not available | The closest alternative is GOOGLETRANSLATE, a separate Google Sheets function that takes the text and optional source and target language codes. |

## Tips and Best Practices

- Name the source language for short texts, because detection is less reliable on a few words.
- Keep the original text in a separate column so a reviewer can compare both versions.
- Copy finished translations as values once they are approved, so the sheet does not request them again.
- Wrap the formula in IFERROR so a failed request leaves a clear message.
- Clean the input first with TRIM or CLEAN when it was copied from a web page or a document.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CLEAN](../Text/CLEAN.md) | Removes non-printing characters before the text is translated. |
| [IFERROR](../Logical/IFERROR.md) | Returns a fallback message when the translation fails. |
| [ISTEXT](../Information/ISTEXT.md) | Confirms that a cell holds text before it is sent for translation. |
| [LEN](../Text/LEN.md) | Counts characters, which helps check text against the length limit. |
| [TRIM](../Text/TRIM.md) | Removes extra spaces from the text before it is translated. |

## Official Documentation

- [Microsoft Support: TRANSLATE function](https://support.microsoft.com/en-us/excel/functions/translate-function)
