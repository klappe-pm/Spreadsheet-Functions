---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Roman and Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Binary Flag Decoding
  - Hex Part Code Lookup
  - Legacy System Imports
related:
  - BASE
  - BIN2DEC
  - DEC2BIN
  - DEC2HEX
  - HEX2DEC
  - OCT2DEC
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/decimal-function
  - https://support.google.com/docs/answer/9116090
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Convert Base to Decimal
tags:
  - base-conversion
  - excel
  - number-systems
  - sheets
---

# DECIMAL

## Description

**DECIMAL** converts a text representation of a whole number written in another base into an ordinary base 10 (decimal) number. Use it when codes arrive as text in hexadecimal, binary, octal or any base from 2 to 36, such as part codes, bit patterns or values exported from older systems.

The base is called the radix in Excel and base in Google Sheets. Bases above 10 use the letters A to Z for digits 10 to 35, and Microsoft notes that the input is not case sensitive. The text can be at most 255 characters long, and the value must be 0 or greater and less than 2^53. Larger values can lose precision.

DECIMAL works in one direction only. To convert a decimal number into another base, use BASE. For the most common bases, the specific converters BIN2DEC, HEX2DEC and OCT2DEC do the same job with fewer arguments.

## Syntax

```excel
=DECIMAL(text, radix)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/DECIMAL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The number to convert, entered as text, for example `"FF"` or `"1010"`. Only characters valid for the base are allowed. Google Sheets names this argument `value`. |
| `radix` | Yes | The base of the number, an integer from 2 to 36. Google Sheets names this argument `base`. |

### Return Value

A decimal (base 10) number. The function may return `#NUM!` or `#VALUE!` when an argument is outside its limits, such as a character that does not belong to the base or a radix outside 2 to 36.

## Examples

### Example 1: Hexadecimal Value

```excel
=DECIMAL("FF",16)
```

**Result:** `255`

Each F in base 16 stands for 15, so the value is (15 times 16) plus 15.

### Example 2: Binary Value From a Cell

Cell A2 holds the text `1010`.

```excel
=DECIMAL(A2,2)
```

**Result:** `10`

The binary digits 1010 stand for 8 plus 2, which is 10.

### Example 3: Base 36 Value

```excel
=DECIMAL("zap",36)
```

**Result:** `45745`

The letters are digits in base 36: z is 35, a is 10 and p is 25. The value is (35 times 36 squared) plus (10 times 36) plus 25.

<!-- Image 2: Letter Digits in Base 36. See Images/Math & Trig/DECIMAL.md -->

### Example 4: Case Does Not Matter

```excel
=DECIMAL("ff",16)
```

**Result:** `255`

Lowercase letters give the same result as uppercase letters in Excel.

### Example 5: Binary Value Written as a Number

```excel
=DECIMAL(111,2)
```

**Result:** `7`

The digits 111 in base 2 stand for 4 plus 2 plus 1, which is 7. Enclosing the digits in quotation marks is safer when a cell might convert them to a number.

## Story Problems

### Problem 1: Hex Part Codes

A warehouse export stores three part codes as hexadecimal text in column B. The inventory team needs each code as a decimal number in column C.

| Part | Hex Code |
| --- | --- |
| P-100 | 3F |
| P-200 | A0 |
| P-300 | 7E |

**Task:** Enter `=DECIMAL(B2,16)` in C2 and fill it down to C4.

**Solution:**

```excel
=DECIMAL(B2,16)
```

**Answer:** `63`, `160` and `126` in C2, C3 and C4. The codes 3F, A0 and 7E are 63, 160 and 126 in base 10.

### Problem 2: Binary Flag Settings

A sensor reports its flag settings as four-bit binary text. The technician needs the decimal value of the Flag 2 pattern in B3 to compare it with a threshold.

| Flag | Bit Pattern |
| --- | --- |
| Flag 1 | 1010 |
| Flag 2 | 1111 |

**Task:** Convert the Flag 2 bit pattern to decimal.

**Solution:**

```excel
=DECIMAL(B3,2)
```

**Answer:** `15`, because 1111 in base 2 is 8 plus 4 plus 2 plus 1.

## Use Cases

### Hex Part Code Lookup

**Scenario:** A parts list from a legacy system stores each code as hexadecimal text. Staff need the decimal index for each code to join the list to a numeric table.

```excel
=DECIMAL(B2,16)
```

**Why It Works:** The formula reads the text code and the base, then returns a number that a lookup can match. Fill it down the column to convert every row.

### Binary Flag Decoding

**Scenario:** A monitoring report records device status as binary text, and a summary sheet needs the decimal value for each device.

```excel
=DECIMAL(C2,2)
```

**Why It Works:** Each binary digit represents a power of two, so the decimal result can be compared with thresholds. Store the pattern as text so that leading zeros are kept.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The radix is outside 2 to 36, or the value is outside the allowed range. | Check the radix, and keep the value between 0 and less than 2^53. |
| `#VALUE!` | The text contains a character that is not valid for the base. | Check the source text for letters beyond the base, such as G in base 16. |
| Wrong value | The digits were stored as a number that lost leading zeros. | Store the code as text, and enclose it in quotation marks in the formula. |
| Imprecise result | The value is very large. | Keep the value below 2^53 or split it into smaller parts. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Arguments are `text` and `radix`. Input is not case sensitive. |
| Google Sheets | Available | Arguments are `value` and `base`. The page describes a base from 2 to 36 and conversion to positive integers. |

## Tips and Best Practices

- Enter codes as text, with quotation marks in the formula, so leading zeros are not lost.
- Use BIN2DEC, HEX2DEC or OCT2DEC for the three common bases when you want a shorter formula.
- Check the code for letters beyond the base before converting a long column.
- Use BASE to convert a decimal result back into text in another base.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BASE](BASE.md) | Converts a decimal number into text in another base, the reverse direction. |
| [BIN2DEC](../Engineering/BIN2DEC.md) | Converts a binary code to decimal with a fixed base. |
| [DEC2BIN](../Engineering/DEC2BIN.md) | Converts a decimal number to binary text. |
| [DEC2HEX](../Engineering/DEC2HEX.md) | Converts a decimal number to hexadecimal text. |
| [HEX2DEC](../Engineering/HEX2DEC.md) | Converts a hexadecimal code to decimal with a fixed base. |
| [OCT2DEC](../Engineering/OCT2DEC.md) | Converts an octal code to decimal with a fixed base. |

## Official Documentation

- [Microsoft Support: DECIMAL function](https://support.microsoft.com/en-us/excel/functions/decimal-function)
- [Google Docs Editors Help: DECIMAL](https://support.google.com/docs/answer/9116090)
