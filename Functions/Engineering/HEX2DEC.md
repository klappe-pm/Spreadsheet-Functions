---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Register Value Decoding
  - Serial Number Conversion
related:
  - BIN2DEC
  - DEC2HEX
  - HEX2BIN
  - HEX2OCT
  - OCT2DEC
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/hex2dec-function
  - https://support.google.com/docs/answer/3093192
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Hex to Decimal
tags:
  - excel
  - number-base
  - sheets
---

# HEX2DEC

## Description

**HEX2DEC** converts a hexadecimal number (base 16) to its decimal (base 10) equivalent. Hexadecimal is common in memory addresses, color codes, device registers and log files, and HEX2DEC turns those values into numbers that can be sorted, compared or added.

The input can be at most 10 characters, which is a 40-bit value. The most significant bit is the sign bit, so negative values use two's-complement notation. For example, `FFFFFFFF5B` is -165 in decimal. Google Sheets documents the limits as a maximum positive value of `7fffffffff` and a minimum negative value of `8000000000`.

Hex digits are not case-sensitive, so `a5` and `A5` return the same result. Any character other than 0 to 9 or A to F makes the function return an error.

## Syntax

```excel
=HEX2DEC(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/HEX2DEC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The hexadecimal value to convert, as text in quotes (`"A5"`), a cell reference or a valid hex number entered without quotes. It cannot contain more than 10 characters, and the sign is taken from the most significant bit. |

### Return Value

The decimal equivalent of the hexadecimal input, as a number. The function returns `#NUM!` when the input contains a character that is not a hex digit.

## Examples

### Example 1: Two-Digit Hex Value

```excel
=HEX2DEC("A5")
```

**Result:** `165`

Hex A5 equals 10 times 16 plus 5, which is 165.

### Example 2: Negative Value in Two's Complement

```excel
=HEX2DEC("FFFFFFFF5B")
```

**Result:** `-165`

The leading digits show a negative 40-bit value. The result is the negative of 165, the same magnitude as Example 1.

### Example 3: Large Hex Value

```excel
=HEX2DEC("3DA408B9")
```

**Result:** `1034160313`

Excel may display this result in scientific notation (1.034E+09). Widen the column or format the cell as a number to see every digit.

### Example 4: Converting a Cell Reference

Cell `A2` holds the text `1F`.

```excel
=HEX2DEC(A2)
```

**Result:** `31`

Hex 1F equals 16 plus 15, which is 31.

<!-- Image 2: Register Sum Worksheet. See Images/Engineering/HEX2DEC.md -->

## Story Problems

### Problem 1: Summing Register Readings

A technician reads three hex register values from a controller and needs their decimal total for a calibration report.

| Register | Value (Hex) |
| --- | --- |
| R1 | 1A |
| R2 | FF |
| R3 | 10 |

**Task:** Convert each value to decimal in column C, then total the three decimal values in `C5`.

**Solution:**

```excel
=HEX2DEC(B2)
```

Fill the formula down to `C4`, then use `=SUM(C2:C4)` in `C5`.

**Answer:** `297`. The three decimal values are 26, 255 and 16, and 26 + 255 + 16 = 297.

### Problem 2: Decoding a Serial Number

A warehouse labels crates with hex serial numbers. The team wants the decimal crate number to look up in an older system.

**Task:** Convert the serial `2A` in cell `B2` to decimal.

**Solution:**

```excel
=HEX2DEC(B2)
```

**Answer:** `42`. Hex 2A is 2 times 16 plus 10, which is 42.

## Use Cases

### Register Value Decoding

**Scenario:** An engineer logs hex register values from a sensor and needs decimal values to compare against a datasheet limit.

```excel
=IF(HEX2DEC(RegisterLog[Value])>MaxReading,"Over Limit","OK")
```

**Why It Works:** HEX2DEC converts each log entry before the comparison, so the limit can be a plain decimal number.

### Serial Number Conversion

**Scenario:** A logistics team maps hex serial numbers to decimal IDs used in a legacy database.

```excel
=HEX2DEC(TRIM(A2))
```

**Why It Works:** TRIM removes stray spaces copied from scanners, which would otherwise cause `#NUM!` errors.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input contains a character other than 0 to 9 or A to F, such as `G1` or `0x1F`. | Remove the prefix or correct the character. |
| `#NUM!` | Extra spaces or punctuation are inside the text. | Clean the value with TRIM or SUBSTITUTE. |
| Error | The input has more than 10 characters. | Check the source; the value is outside the 40-bit range. |
| Unexpected negative value | The top hex digit is 8 or higher, so the sign bit is set. | Confirm that the source uses signed 40-bit values before reading the result. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Excel for Microsoft 365 and Excel for the web | Accepts up to 10 characters in two's-complement form. |
| Google Sheets | Available | Accepts the same signed 40-bit range, with a maximum positive value of `7fffffffff`. |

## Tips and Best Practices

- Enter hex values as text, for example `"A5"`, so that the spreadsheet does not try to read them as a number first.
- Use TRIM to remove spaces before conversion when the values come from a scanner or a copied report.
- Use HEX2DEC with IFERROR when a column may contain blanks or invalid codes.
- Compare the decimal result with a known value from the datasheet to confirm that the sign convention matches.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2DEC](BIN2DEC.md) | Converts a binary value to decimal. |
| [DEC2HEX](DEC2HEX.md) | Converts a decimal value back to hexadecimal. |
| [HEX2BIN](HEX2BIN.md) | Converts a hex value to binary for bit-level reading. |
| [HEX2OCT](HEX2OCT.md) | Converts a hex value to octal. |
| [OCT2DEC](OCT2DEC.md) | Converts an octal value to decimal. |

## Official Documentation

- [Microsoft Support: HEX2DEC function](https://support.microsoft.com/en-us/excel/functions/hex2dec-function)
- [Google Docs Editors Help: HEX2DEC](https://support.google.com/docs/answer/3093192)
