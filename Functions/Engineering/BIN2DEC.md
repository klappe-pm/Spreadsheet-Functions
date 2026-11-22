---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Sensor Code Decoding
  - Signed Offset Conversion
related:
  - BIN2HEX
  - BIN2OCT
  - BITAND
  - DEC2BIN
  - HEX2DEC
  - OCT2DEC
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/bin2dec-function
  - https://support.google.com/docs/answer/3092991
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Binary To Decimal
  - Signed Binary To Decimal
tags:
  - binary
  - excel
  - number-base
  - sheets
  - two-complement
---

# BIN2DEC

## Description

**BIN2DEC** converts a binary number to its decimal equivalent. Binary numbers in Excel and Google Sheets are limited to 10 characters, which is 10 bits. The leftmost bit is the sign bit, and the other nine bits hold the magnitude. Negative values use two's complement notation, so the range runs from `1000000000` (-512) to `0111111111` (511).

Use BIN2DEC when a device, log or export reports values as binary text and a calculation needs the decimal number. It is the reverse of DEC2BIN, and it pairs well with BITAND, BITOR and other bitwise functions when a model reads individual bits.

Only the digits 0 and 1 are accepted. Any other character returns `#NUM!`, and so does a value with more than 10 characters.
Enter binary values as text in cells that have a leading zero, such as `0001010`, so the zeros are not dropped when the value is typed.

BIN2DEC is available in both Microsoft Excel and Google Sheets with the same behavior.

## Syntax

```excel
=BIN2DEC(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/BIN2DEC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The binary value to convert, up to 10 characters. The first character is the sign bit for 10-digit values. A plain number such as `1011001` or a text value such as `"0110"` both work. |

### Return Value

A decimal number. The function returns `#NUM!` when the input contains a character other than 0 or 1 or has more than 10 characters.

## Examples

### Example 1: Converting a Seven-Digit Code

```excel
=BIN2DEC(1011001)
```

**Result:** `89`

The bits 1011001 stand for 64 + 16 + 8 + 1, which equals 89.

### Example 2: Sign Bit Alone

```excel
=BIN2DEC(1000000000)
```

**Result:** `-512`

In 10-bit two's complement, a leading 1 followed by nine zeros is the lowest value the function accepts.

### Example 3: Filled Down a Column

Codes in `A2:A4` are `110`, `1001` and `1111111111`.

```excel
=BIN2DEC(A2)
```

Fill the formula down to `B4`.

**Result:** `6` (A2), `9` (A3), `-1` (A4)

Shorter codes are read as positive values, and a full 10-digit code with a leading 1 is read as negative.

<!-- Image 2: Sign Bit Layout. See Images/Engineering/BIN2DEC.md -->

### Example 4: Largest Positive Value

```excel
=BIN2DEC("0111111111")
```

**Result:** `511`

The quoted text and the unquoted number produce the same result, so either form works in a formula.

## Story Problems

### Problem 1: Shelf Sensor Codes

A warehouse shelf sensor reports a count in binary. The codes are typed as text in column A, and the team needs the total of the four decoded counts.

| Sensor | Code |
| --- | --- |
| S1 | 0001010 |
| S2 | 0010100 |
| S3 | 0011110 |
| S4 | 0000111 |

**Task:** Put `=BIN2DEC(B2)` in `C2`, fill it down to `C5`, then add the four results.

**Solution:**

```excel
=SUM(C2:C5)
```

**Answer:** `67`, from 10 + 20 + 30 + 7.

<!-- Image 3: Results Panel for the Story Problems. See Images/Engineering/BIN2DEC.md -->

### Problem 2: A Negative Temperature Offset

A controller stores a calibration offset as a 10-bit signed binary value. The value is `1111110110`, and the engineer needs its decimal form to apply the correction.

| Item | Value |
| --- | --- |
| Stored offset | 1111110110 |

**Task:** Convert the stored offset to decimal and state whether the correction adds or subtracts.

**Solution:**

```excel
=BIN2DEC("1111110110")
```

**Answer:** `-10`. The offset is negative, so the correction subtracts 10 from the reading.

## Use Cases

### Sensor Code Decoding

**Scenario:** A monitoring export stores each sensor state as a binary string, and a dashboard needs the decimal count for each row.

```excel
=BIN2DEC(Table1[StatusCode])
```

**Why It Works:** Excel returns one decimal value per row when the workbook supports dynamic arrays, so the conversion covers the whole column.
Store the codes as text so leading zeros are kept.

### Signed Offset Conversion

**Scenario:** An imported register lists signed offsets in binary, and the analyst needs the decimal value to check each adjustment.

```excel
=IF(AND(LEN(B2)=10, LEFT(B2,1)="1"), "Negative", "Positive") & ": " & BIN2DEC(B2)
```

**Why It Works:** For a 10-character code, the first character is the sign bit, so the test checks the length before reading that bit.
This tells a reviewer the direction of an adjustment before they read the number.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The code contains a digit other than 0 or 1. | Clean the source text, or check for a stray space or a letter. |
| `#NUM!` | The code has more than 10 characters. | Split the value or use a wider conversion method for longer bit strings. |
| Wrong value | A leading zero was lost when the code was typed as a number. | Format the cell as text or enter the code in quotes. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Argument is named `number`. Input is limited to 10 characters. |
| Google Sheets | Available | Argument is named `signed_binary_number`. Plain binary numbers without quotes are accepted, and the 10-bit limits are the same. |

## Tips and Best Practices

- Store binary codes as text so leading zeros survive copy and paste.
- Validate codes with a check for characters other than 0 and 1 before converting a long list.
- Use BIN2DEC on the way in and DEC2BIN on the way out when a model moves between bit patterns and numbers.
- Remember that a 10-digit code beginning with 1 is negative, even if the code looks like a large positive number.
- Pair the result with BITAND when a single bit inside the code needs to be tested.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2HEX](BIN2HEX.md) | Converts the same binary code to hexadecimal. |
| [BIN2OCT](BIN2OCT.md) | Converts the same binary code to octal. |
| [BITAND](BITAND.md) | Tests individual bits once the code is in decimal form. |
| [DEC2BIN](DEC2BIN.md) | Reverses the conversion, from decimal to binary. |
| [HEX2DEC](HEX2DEC.md) | Converts hexadecimal text to decimal, for the other common base. |
| [OCT2DEC](OCT2DEC.md) | Converts octal text to decimal. |

## Official Documentation

- [Microsoft Support: BIN2DEC function](https://support.microsoft.com/en-us/excel/functions/bin2dec-function)
- [Google Docs Editors Help: BIN2DEC](https://support.google.com/docs/answer/3092991)
