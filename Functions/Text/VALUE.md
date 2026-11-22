---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Bank Export Amounts
  - Survey Scores Stored as Text
  - Text Dates From Exports
related:
  - IFERROR
  - ISNUMBER
  - NUMBERVALUE
  - TEXT
  - VALUETOTEXT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/value-function
  - https://support.google.com/docs/answer/3094220
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Convert Text To Number
  - Text To Number
tags:
  - conversion
  - data-cleaning
  - excel
  - sheets
  - text
---

# VALUE

## Description

**VALUE** converts a text string that looks like a number, date or time into a real number. Exported files often store amounts such as `$1,250.00` or dates such as `14-Mar-2024` as text, which means sums, averages and date math ignore them. VALUE returns the number so those calculations work.

VALUE accepts any number, date or time format that the spreadsheet recognizes for the current locale. A date becomes a serial number, the count of days since the base date of the spreadsheet, so `14-Mar-2024` returns `45365`. Format the result as a date to display it. A time becomes a fraction of a day, so 12:00 returns `0.5`.

Excel and Google Sheets usually convert text to numbers on their own when you calculate with it. VALUE is most useful when you need a clear, explicit conversion in a helper column, or when a formula must return a number instead of text. When the text is not in a recognized format, VALUE returns `#VALUE!`. Wrap it in IFERROR to supply a fallback.

## Syntax

```excel
=VALUE(text)
```

<!-- Image 1: Text Input and Number Output. See Images/Text/VALUE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to convert, either typed in quotation marks or a reference to a cell that holds the text. The text must be in a number, date or time format the spreadsheet recognizes. |

### Return Value

A number. Dates and times return serial numbers, so format the result to display them as dates or times. The function returns `#VALUE!` when the text is not in a recognized format.

## Examples

### Example 1: Amount With a Thousands Separator

```excel
=VALUE("1,250.75")
```

**Result:** `1250.75`

In a locale that uses a period as the decimal separator and a comma for thousands, the text is read as a number. In a locale that reverses those symbols, the same text can produce a different number or an error.

### Example 2: Time Difference

```excel
=VALUE("18:30:00")-VALUE("09:45:00")
```

**Result:** `0.364583`

The two times become fractions of a day, and the difference is 8 hours and 45 minutes. Format the result as a time (`h:mm`) to display `8:45`.

### Example 3: Date Text as a Serial Number

```excel
=VALUE("14-Mar-2024")
```

**Result:** `45365`

The serial number counts days from the spreadsheet base date. Format the cell as a date to display `3/14/2024` in US locales.

### Example 4: Fallback for Text Values

Cell `A2` contains `n/a`.

```excel
=IFERROR(VALUE(A2),0)
```

**Result:** `0`

VALUE returns `#VALUE!` for `n/a`, and IFERROR replaces that error with 0.

### Example 5: Unrecognized Text

```excel
=VALUE("twelve")
```

**Result:** `#VALUE!`

The word is not a number, date or time format, so VALUE cannot convert it.

## Story Problems

### Problem 1: Bank Export Amounts

A bank export lists the payments of a small office, and each amount is stored as text with a currency symbol.

| Payee | Amount |
| --- | --- |
| Hotel deposit | $1,250.00 |
| Client lunch | $87.50 |
| Software license | $3,410.25 |
| Printer paper | $560.00 |
| Parking | $12.99 |

**Task:** Convert each amount in column B to a number in column C, then total the payments.

**Solution:**

```excel
=VALUE(B2)
```

Fill the formula down from `C2` to `C6`, then total the column with `=SUM(C2:C6)`.

**Answer:** `5320.74`. The five amounts add up to 1250.00 + 87.50 + 3410.25 + 560.00 + 12.99. Without VALUE, SUM would ignore the text and return 0.

<!-- Image 2: Bank Export Totals. See Images/Text/VALUE.md -->

### Problem 2: Survey Scores Stored as Text

A survey export stores each score as text, and one respondent skipped the question and entered `n/a`.

| Respondent | Score |
| --- | --- |
| R01 | 4 |
| R02 | 5 |
| R03 | n/a |
| R04 | 3 |
| R05 | 2 |

**Task:** Convert the scores to numbers, leaving the skipped answer blank, then find the average score.

**Solution:**

```excel
=IFERROR(VALUE(B2),"")
```

Fill the formula down from `C2` to `C6`, then find the average with `=AVERAGE(C2:C6)`.

**Answer:** `3.5`. The four valid scores are 4, 5, 3 and 2, and their average is 14 divided by 4. AVERAGE ignores the blank text result in row 4.

## Use Cases

### Bank Export Amounts

**Scenario:** A bookkeeper imports a bank file where every amount has a currency symbol and a thousands separator, so the amounts arrive as text.

```excel
=SUM(VALUE(Export[Amount]))
```

**Why It Works:** VALUE converts each amount to a number. Test the formula on a small sample first, because array handling differs between Excel versions.

### Survey Scores Stored as Text

**Scenario:** A research team pastes responses from a web form, and some scores are text. The team needs an average that skips skipped answers.

```excel
=AVERAGE(IFERROR(VALUE(C2:C50),""))
```

**Why It Works:** IFERROR turns each unrecognized entry into a blank text value, and AVERAGE ignores it. In Excel 365 this works directly; in older versions, enter it as an array formula.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The text is not a recognized number, date or time format. | Clean the text first, or wrap the formula in IFERROR. |
| Date shows as `45365` | VALUE returns a serial number for dates. | Format the result cell as a date. |
| Wrong date or number | A regional setting reads the text in a different order or with different separators. | Convert the text in a locale that matches the source file, or rebuild the date with DATE. |
| Sum is 0 | The amounts are still text, so SUM ignores them. | Convert each cell with VALUE in a helper column. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions, including Excel for the web | Dates and times return serial numbers, and text is read using the regional settings. |
| Google Sheets | Available | Converts any date, time or number format Sheets understands. For example, `01/01/2012` returns `40909`. |

## Tips and Best Practices

- Convert text in a helper column so the original export stays unchanged and any error is easy to find.
- Test one or two values before filling the formula down, especially for dates, because regional settings change how text is read.
- Use IFERROR with VALUE when some entries are expected to be blank or invalid, so one bad row does not break a total.
- Use ISNUMBER to check that a converted cell really holds a number before relying on it in a total.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IFERROR](../Logical/IFERROR.md) | Supplies a fallback value when VALUE cannot convert the text. |
| [ISNUMBER](../Information/ISNUMBER.md) | Confirms that a converted cell holds a number. |
| [NUMBERVALUE](../Text/NUMBERVALUE.md) | Converts text to a number with explicit decimal and group separators. |
| [TEXT](../Text/TEXT.md) | Converts a number to text using a display format; the reverse direction. |
| [VALUETOTEXT](../Text/VALUETOTEXT.md) | Converts any value to text, with an option for a strict format. |

## Official Documentation

- [Microsoft Support: VALUE function](https://support.microsoft.com/en-us/excel/functions/value-function)
- [Google Docs Editors Help: VALUE](https://support.google.com/docs/answer/3094220)
