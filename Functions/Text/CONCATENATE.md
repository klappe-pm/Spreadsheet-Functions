---
domain: Spreadsheet Functions
category: Text
subcategory: Text Joining and Splitting
purpose:
  - Text Manipulation
use-case:
  - Customer Name Formatting
  - Product Code Assembly
  - Report Titles
related:
  - CONCAT
  - JOIN
  - TEXT
  - TEXTJOIN
  - TRIM
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/concatenate-function
  - https://support.google.com/docs/answer/3094123
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Join Text
tags:
  - compatibility
  - concatenation
  - excel
  - sheets
  - text-joining
---

# CONCATENATE

## Description

**CONCATENATE** joins several text items, cell references or numbers into one string, in the order they are given. It adds no separator, so spaces and punctuation must be supplied as arguments. Excel allows up to 255 items and a combined total of 8,192 characters.

Microsoft has replaced CONCATENATE with CONCAT in Excel. Excel 2016 and later keep the function for compatibility, and Microsoft notes that it may not be available in future versions. In new Excel work, use CONCAT to join cells and ranges, or TEXTJOIN when you need a delimiter or want blanks skipped. Google Sheets still supports CONCATENATE fully, and there it accepts ranges as well.

The ampersand operator (`&`) does the same job with less typing. Use CONCATENATE when a formula must be read by someone who prefers function syntax, or when an existing workbook already depends on it.

<!-- Image 1: Joining Cells With Explicit Separators. See Images/Text/CONCATENATE.md -->

## Syntax

```excel
=CONCATENATE(text1, [text2], ...)
```

Google Sheets uses the form `=CONCATENATE(string1, [string2, ...])`.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text1` | Yes | The first item to join. It can be text, a number or a cell reference. In Google Sheets this argument is `string1`. |
| `text2`, ... | No | Additional items, joined in order. Excel allows up to 255 items. In Google Sheets the arguments are `string2` and onward. |

### Return Value

A single text string that combines the items in the order supplied. In Excel the combined text can be up to 8,192 characters.

## Examples

### Example 1: Joining Two Literal Strings

```excel
=CONCATENATE("Hello", " ", "World")
```

**Result:** `Hello World`

The middle argument is a space, so the words are separated.

### Example 2: Full Name From Two Cells

```excel
=CONCATENATE(A2, " ", B2)
```

Where `A2` contains `Jane` and `B2` contains `Doe`.

**Result:** `Jane Doe`

### Example 3: Address Fragments With Mixed Separators

```excel
=CONCATENATE(A2, ", ", B2, ", ", C2, " ", D2)
```

Where `A2` contains `Austin`, `B2` contains `TX`, `C2` contains `78701`, and `D2` is empty.

**Result:** `Austin, TX, 78701 ` (with a trailing space, because `D2` is empty)

The empty cell adds nothing, but the separator before it still appears. This is the reason to use TEXTJOIN with blanks skipped for optional fields.

### Example 4: Formatting a Number Inside the Text

```excel
=CONCATENATE("Total: ", TEXT(B2, "$#,##0.00"))
```

Where `B2` contains `1249.5`.

**Result:** `Total: $1,249.50`

TEXT applies the currency format before the value is joined. Without it, the number would appear as 1249.5.

<!-- Image 2: Legacy Formula Versus Modern Replacement. See Images/Text/CONCATENATE.md -->

## Story Problems

### Problem 1: Badge IDs From Department, Number and Site

A staff list in `A1:C4` holds the department, a badge number and the site code.

| Dept | Number | Site |
| --- | --- | --- |
| OPS | 7 | NYC |
| HR | 42 | LAX |
| FIN | 118 | CHI |

**Task:** Build a badge ID in column D with the number padded to three digits, for example `OPS-007-NYC`.

**Solution:**

```excel
=CONCATENATE(A2, "-", TEXT(B2, "000"), "-", C2)
```

Fill this formula down to `D4`.

**Answer:** `OPS-007-NYC`, `HR-042-LAX` and `FIN-118-CHI`, because TEXT pads 7 to `007`, 42 to `042` and 118 stays `118`.

### Problem 2: Email Address From a Name

A contact list has a first name in `A2` and a last name in `B2`: Maya and Ortiz.

**Task:** Build a lowercase email address in `C2` with the first initial and the full last name, followed by `@example.com`.

**Solution:**

```excel
=CONCATENATE(LOWER(LEFT(A2,1)), LOWER(B2), "@example.com")
```

**Answer:** `mortiz@example.com`, because the first letter of Maya is `m` and the last name is `ortiz` in lowercase.

## Use Cases

### Customer Name Formatting

**Scenario:** A letter template needs a name in the form `Title First Last`, but the title column is often blank.

```excel
=TRIM(CONCATENATE(A2, " ", B2, " ", C2))
```

**Why It Works:** Column A holds the title, B the first name and C the last name. When the title is blank, the joined text starts with a space, and TRIM removes it along with any doubled spaces.

### Report Titles From a Date

**Scenario:** A monthly report title must show the reporting month, which is stored in a date cell.

```excel
=CONCATENATE("Sales Report, ", TEXT(B1, "mmmm yyyy"))
```

**Why It Works:** TEXT turns the date into the month name and year before the join. Without TEXT, the title would show the underlying serial number.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Words run together | No separator argument was supplied. | Add `" "` or another separator as an argument. |
| Numbers or dates look wrong | The value is converted to text in general format. | Wrap the value in TEXT with a format code. |
| `#VALUE!` | The combined text is longer than 8,192 characters in Excel. | Split the text across cells, or use CONCAT, which allows 32,767 characters. |
| `#NAME?` | The function name is misspelled, or literal text lacks quotation marks. | Check the spelling and quote all literal text. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Microsoft 365 and Excel for the web | Compatibility only. Up to 255 items and 8,192 combined characters. Ranges are not accepted, so use CONCAT. |
| Google Sheets | Available | Fully supported. A range argument is read row by row. |

## Tips and Best Practices

- Include every separator as its own argument, because the function adds none.
- Use TEXT for dates and formatted numbers before joining them.
- Use CONCAT or TEXTJOIN in new Excel workbooks, since CONCATENATE is kept only for compatibility.
- Use the `&` operator for short, simple joins.
- Wrap the result in TRIM when optional cells can leave extra spaces.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CONCAT](CONCAT.md) | The modern replacement in Excel. It accepts ranges. |
| [JOIN](JOIN.md) | Joins an array with a delimiter in Google Sheets. |
| [TEXT](TEXT.md) | Formats numbers and dates before they are joined. |
| [TEXTJOIN](TEXTJOIN.md) | Joins with a delimiter and can skip empty values. |
| [TRIM](TRIM.md) | Removes extra spaces left by empty cells or separators. |

## Official Documentation

- [Microsoft Support: CONCATENATE function](https://support.microsoft.com/en-us/excel/functions/concatenate-function)
- [Google Docs Editors Help: CONCATENATE](https://support.google.com/docs/answer/3094123)
