---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Text Manipulation
use-case:
  - Bullet Points In Cells
  - Currency Symbols In Labels
  - Status Check Marks
related:
  - CHAR
  - CODE
  - CONCATENATE
  - TEXT
  - UNICODE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/unichar-function
  - https://support.google.com/docs/answer/9369024
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Character From Code Point
  - Unicode Character
tags:
  - character-codes
  - excel
  - sheets
  - unicode
---

# UNICHAR

## Description

**UNICHAR** returns the character that matches a Unicode number (also called a code point). Unicode covers letters, symbols and punctuation from almost every writing system, so UNICHAR can insert a euro sign, a bullet, a check mark or an accented letter into a formula result without typing the character itself.

Use UNICHAR when a label needs a symbol that is not on the keyboard, or when a list of code points is kept in a table and the symbols are generated from it. For code numbers from 1 to 255, CHAR is the older option. For the reverse operation, which returns the number for a character, use UNICODE.

Not every code point has a visible glyph in every font. If a symbol displays as a box or as blank space, change the font of the cell to one that includes the character. The Unicode character set is also refined over time, so Google Sheets warns that output for some numbers may change.

## Syntax

```excel
=UNICHAR(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Text/UNICHAR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The Unicode number (code point) of the character, such as 8364 for the euro sign. It must be a positive whole number within the Unicode range. |

### Return Value

A single character. The function returns `#VALUE!` when the number is 0, negative or outside the Unicode range. Excel also returns `#N/A` for a partial surrogate or a value of the wrong data type.

## Examples

### Example 1: A Letter From a Code Point

```excel
=UNICHAR(67)
```

**Result:** `C`

Code point 67 is the uppercase letter C, which is the same character CHAR would return for that number.

### Example 2: Euro Label With a Formatted Amount

```excel
=UNICHAR(8364)&TEXT(A2,"#,##0.00")
```

**Result:** `€1,250.00` when `A2` holds 1250

The euro sign is code point 8364. TEXT adds the separators and two decimals to the amount.

### Example 3: Check Mark

```excel
=UNICHAR(10003)
```

**Result:** `✓`

Code point 10003 is a check mark, which suits a pass indicator in a status column.

### Example 4: Bullet Character

```excel
=UNICHAR(8226)&" "&A2
```

**Result:** `• Oil change` when `A2` holds `Oil change`

The bullet is code point 8226. The space after it separates the bullet from the item text.

### Example 5: Invalid Code Point

```excel
=UNICHAR(0)
```

**Result:** `#VALUE!`

Code point 0 is not a valid character in Excel, so the formula returns an error. Wrap the formula in IFERROR when the number comes from an input cell that may be blank.

## Story Problems

### Problem 1: Price Labels With Currency Symbols

A price list stores a currency code point in column A and an amount in column B.

| Code | Amount |
| --- | --- |
| 36 | 45 |
| 163 | 80 |
| 165 | 9000 |

**Task:** Build a label in column C that starts with the currency symbol and shows the amount with two decimals and separators.

**Solution:**

```excel
=UNICHAR(A2)&TEXT(B2,"#,##0.00")
```

**Answer:** `$45.00`, `£80.00` and `¥9,000.00`. Code point 36 is the dollar sign, 163 is the pound sign and 165 is the yen sign.

<!-- Image 2: Symbols in a Label. See Images/Text/UNICHAR.md -->

### Problem 2: Bullets for a Task List

Column A holds three tasks: `Oil change`, `Tire check` and `Brake pads`. The notes column needs each task on its own line with a bullet in front.

**Task:** Put a bullet and a space in front of the task in `A2`, then fill the formula down.

**Solution:**

```excel
=UNICHAR(8226)&" "&A2
```

**Answer:** `• Oil change`, `• Tire check` and `• Brake pads`, one per row. The bullet is code point 8226.

## Use Cases

### Bullet Points in Cells

**Scenario:** A maintenance report needs a bulleted list inside one cell, and the cell is exported to a system that keeps the characters as they are.

```excel
=UNICHAR(8226)&" "&A2
```

**Why It Works:** The bullet is generated from its code point, so the formula produces the same character on every machine. Use CHAR(10) between items when the list needs line breaks, and turn on wrap text.

### Currency Symbols in Labels

**Scenario:** A dashboard shows amounts in euros, and the symbol must follow the same currency code column as the amounts.

```excel
=UNICHAR(8364)&TEXT(A2,"#,##0.00")
```

**Why It Works:** The symbol and the formatted amount are built in one step, so a change to the amount updates the label without any manual edit.

### Status Check Marks

**Scenario:** A checklist shows a check mark for each completed item and a cross for each open item.

```excel
=IF(B2="Done",UNICHAR(10003),UNICHAR(10007))
```

**Why It Works:** Code point 10003 is a check mark and 10007 is a cross. The IF test chooses between them, and the symbols can be formatted with a font color as well.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The number is 0, negative, or outside the Unicode range. | Check the code point, and wrap the formula in IFERROR when the input may be blank. |
| `#N/A` | The number is a partial surrogate or is not a number. | Use a complete code point, and make sure the input is a number. |
| Box or blank symbol | The font in the cell does not include the character. | Change the cell font to one that includes the symbol. |
| Wrong symbol | The code page number from CHAR was used with UNICHAR. | Use CHAR for numbers 1 to 255 and UNICHAR for larger code points, or check the number with UNICODE. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Returns `#VALUE!` for 0 or an out-of-range number, and `#N/A` for a partial surrogate. |
| Google Sheets | Available | Returns the character for the number, with UTF-8 and UTF-16 support. Output for some numbers may change as the Unicode set is refined. |

## Tips and Best Practices

- Keep code points in a small lookup table, so the symbols can be changed without editing formulas.
- Use UNICODE to check the code point of a symbol already in a cell before you reuse it.
- Test the symbol in the font that the report or export will use.
- Use CHAR only for code numbers from 1 to 255, and UNICHAR for everything above that.
- Combine UNICHAR with TEXT when a symbol must sit in front of a formatted number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHAR](../Text/CHAR.md) | Returns the character for a code number from 1 to 255 in the system code page. |
| [CODE](../Text/CODE.md) | Returns the code number of the first character in the system code page. |
| [CONCATENATE](../Text/CONCATENATE.md) | Joins a symbol with other text in a label. |
| [TEXT](../Text/TEXT.md) | Formats the amount that follows a currency symbol. |
| [UNICODE](../Text/UNICODE.md) | Returns the Unicode number of the first character, the reverse of UNICHAR. |

## Official Documentation

- [Microsoft Support: UNICHAR function](https://support.microsoft.com/en-us/excel/functions/unichar-function)
- [Google Docs Editors Help: UNICHAR](https://support.google.com/docs/answer/9369024)
