---
domain: Spreadsheet Functions
category: Text
subcategory: Case Conversion
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Catalog Title Formatting
  - Customer Name Cleanup
  - Import Name Standardization
related:
  - CLEAN
  - EXACT
  - LOWER
  - TRIM
  - UPPER
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/proper-function
  - https://support.google.com/docs/answer/3094133
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Capitalize Words
  - Title Case
tags:
  - case-conversion
  - data-cleaning
  - excel
  - sheets
  - text
---

# PROPER

## Description

**PROPER** capitalizes the first letter of each word in a text string and changes the rest of the letters to lowercase. It is designed for names and place names, such as `JOHN SMITH` becoming `John Smith`.

PROPER decides where a word starts by looking at the character before each letter. A letter that follows a space, a hyphen, a digit or any other character that is not a letter is capitalized. This is why `north-east` becomes `North-East`, and it is also why `3rd` becomes `3Rd`. The function does not know about English rules for small words, so `and` becomes `And` in a title.

Use PROPER for display and for standardizing names that come from an all-capitals or all-lowercase source. Use LOWER when the value is used as a key for matching, and use EXACT when you need to check a value against an expected spelling.

## Syntax

```excel
=PROPER(text)
```

<!-- Image 1: PROPER Argument Layout. See Images/Text/PROPER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to convert. It can be text in quotation marks, a formula that returns text, or a reference to a cell that contains text. |

### Return Value

A text string in which each word starts with a capital letter and the remaining letters are lowercase. Characters that are not letters, such as digits, spaces and punctuation, are left in place.

## Examples

### Example 1: Converting a Phrase

```excel
=PROPER("quarterly sales REPORT")
```

**Result:** `Quarterly Sales Report`

Each word starts with a capital letter, and the rest of each word is lowercase.

### Example 2: A Letter After a Hyphen or a Digit

```excel
=PROPER("north-east region 3rd floor")
```

**Result:** `North-East Region 3Rd Floor`

The letter after the hyphen is capitalized because it follows a non-letter. The `r` in `3rd` is also capitalized because it follows the digit 3. Plan for this when the text includes ordinal numbers.

<!-- Image 2: Capitalization After Non-Letter Characters. See Images/Text/PROPER.md -->

### Example 3: Mixed Case Input

```excel
=PROPER("mcLeod")
```

**Result:** `Mcleod`

The `L` is lowercased because it is not the first letter of a word. PROPER cannot keep an internal capital, so use a manual correction for names such as this.

### Example 4: Numbers at the Start

```excel
=PROPER("2025 budget PLAN")
```

**Result:** `2025 Budget Plan`

The leading digits are unchanged, and each word after the space starts with a capital letter.

### Example 5: Converting a Cell Value

Cell `A2` contains `JOHN SMITH`.

```excel
=PROPER(A2)
```

**Result:** `John Smith`

The formula leaves the original text in `A2` unchanged, so the result can be checked against the source.

## Story Problems

### Problem 1: Counting Names That Need Changes

A membership office imports a list of names from a spreadsheet that was typed by several people. Some entries are in capitals, some are in lowercase, and some are already correct.

| Name |
| --- |
| JOHN SMITH |
| mary-jane lee |
| tomas garcia |
| Li Wei |
| ANA DIAZ |

**Task:** Count how many names change when PROPER is applied.

**Solution:**

```excel
=SUMPRODUCT(--NOT(EXACT(A2:A6, PROPER(A2:A6))))
```

**Answer:** `4`. JOHN SMITH, mary-jane lee, tomas garcia and ANA DIAZ change. Li Wei is already in the correct form, so it does not change.

### Problem 2: Cleaning a Department Title

A finance team uses department titles in the form `FINANCE and ACCOUNTING` on reports. The report template needs a cleaner title.

**Task:** Convert the title in `A2` with PROPER and check the result for words that should stay lowercase.

**Solution:**

```excel
=PROPER(A2)
```

**Answer:** `Finance And Accounting`. The formula capitalizes `and` because PROPER treats every word the same way, so a manual edit is needed to show `Finance and Accounting`.

## Use Cases

### Customer Name Cleanup

**Scenario:** A call center export stores customer names in capitals, and the letters must be shown in a letter template.

```excel
=PROPER(TRIM(A2))
```

**Why It Works:** TRIM removes stray spaces, and PROPER applies one name style to the whole column. Check names such as `McDonald` by hand, because PROPER will not keep the internal capital.

### Import Name Standardization

**Scenario:** A product list arrives with mixed capitalization, and the catalog must show one style for every name.

```excel
=PROPER(B2)
```

**Why It Works:** A single formula gives every product name the same capitalization, so the list sorts and displays consistently.

### Catalog Title Formatting

**Scenario:** A catalog needs each product title in title case for the website.

```excel
=PROPER(C2)
```

**Why It Works:** PROPER gives a quick first draft of title case. Review the result for small words, which PROPER capitalizes like every other word.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Internal capital is lost | PROPER lowercases every letter that does not start a word. | Correct the name by hand, or keep the original text for that value. |
| `3Rd` or similar | A letter after a digit is capitalized. | Wrap the result in SUBSTITUTE to change the ordinal, for example from `3Rd` to `3rd`. |
| Small words are capitalized | PROPER capitalizes every word. | Review titles and correct small words by hand. |
| `#SPILL!` | A range is used and cells below the result hold data. | Clear the spill range or enter the formula in one cell. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | Range input spills in Microsoft 365. Behavior on text is the same as Google Sheets. |
| Google Sheets | Available | Capitalizes the first letter of each word and lowercases the rest, the same as Excel. |

## Tips and Best Practices

- Apply TRIM before PROPER when names come from forms or paste operations.
- Keep the source column unchanged so you can check the converted text against it.
- Use PROPER for display, and use LOWER when the value is a lookup key.
- Review names with internal capitals, such as Mc or Mac names, after conversion.
- Remember that PROPER capitalizes the first letter after a digit, which matters for dates and ordinals.

## Related Functions

| Function | Relationship |
| --- | --- |
| [UPPER](UPPER.md) | Converts all letters to uppercase. |
| [LOWER](LOWER.md) | Converts all letters to lowercase, often used for matching. |
| [EXACT](EXACT.md) | Compares two text values case-sensitively, to check a result. |
| [TRIM](TRIM.md) | Removes extra spaces before capitalization. |
| [CLEAN](CLEAN.md) | Removes nonprinting characters from imported text. |

## Official Documentation

- [Microsoft Support: PROPER function](https://support.microsoft.com/en-us/excel/functions/proper-function)
- [Google Docs Editors Help: PROPER](https://support.google.com/docs/answer/3094133)
