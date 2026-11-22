---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Device Status Flags
  - Register Value Decoding
related:
  - BIN2DEC
  - BIN2HEX
  - DEC2BIN
  - HEX2DEC
  - HEX2OCT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/hex2bin-function
  - https://support.google.com/docs/answer/3093139
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Hex to Binary
tags:
  - excel
  - number-base
  - sheets
---

# HEX2BIN

## Description

**HEX2BIN** converts a hexadecimal number (base 16) to a binary number (base 2). It is useful when a device, log file or register reports status bits in hex and a person needs to read the individual bits.

The function works on 10-character hexadecimal values that use a 40-bit two's-complement format. The most significant bit is the sign bit, so positive values can be at most `1FF` (511 in decimal) and negative values can be as low as `FFFFFFFE00` (-512). Negative results always have 10 binary digits.

Use the optional `places` argument to pad short results with leading zeros, which is useful for byte-aligned or fixed-width status displays. Google Sheets calls the same argument `significant_digits` and returns the result as a number, so arithmetic on that result can go wrong because the spreadsheet treats the binary digits as a decimal number.

## Syntax

```excel
=HEX2BIN(number, [places])
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/HEX2BIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The hexadecimal value to convert, as text in quotes (`"1F"`), a cell reference or a valid hex number entered without quotes. It cannot exceed 10 characters, and positive values cannot be greater than `1FF`. |
| `places` | No | The number of characters in the result. If omitted, the function uses the fewest characters needed. The result is padded with zeros to reach this length. Negative results ignore `places`. |

### Return Value

A binary number with up to 10 digits. The function returns `#NUM!` for an invalid hex value, a result that needs more characters than `places` allows, or a negative `places` value. It returns `#VALUE!` when `places` is nonnumeric.

## Examples

### Example 1: Padding With Leading Zeros

```excel
=HEX2BIN("F", 8)
```

**Result:** `00001111`

Hex F is 1111 in binary. The `places` argument pads the result to eight characters.

### Example 2: Converting a Two-Digit Value

```excel
=HEX2BIN("B7")
```

**Result:** `10110111`

Hex B7 equals 183 in decimal, which is 10110111 in binary.

### Example 3: Negative Value

```excel
=HEX2BIN("FFFFFFFFFF")
```

**Result:** `1111111111`

The value FFFFFFFFFF is -1 in 40-bit two's complement, so every bit of the 10-digit result is 1.

### Example 4: Largest Positive Value

Cell `A2` holds the text `1FF`.

```excel
=HEX2BIN(A2)
```

**Result:** `111111111`

Hex 1FF is 511, the largest positive value the function accepts. A larger positive value such as `200` returns `#NUM!`.

<!-- Image 2: Padded Status Worksheet. See Images/Engineering/HEX2BIN.md -->

## Story Problems

### Problem 1: Reading Status Flags

A pump controller reports its status as a hex byte. Each bit is a flag: for example, bit 0 might mean "running" and bit 1 might mean "door open". The status codes are in column B.

| Pump | Status (Hex) |
| --- | --- |
| P-1 | 1F |
| P-2 | A0 |
| P-3 | 07 |

**Task:** Convert each status to eight binary digits in column C, then read the result for pump P-2 in `C3`.

**Solution:**

```excel
=HEX2BIN(B3, 8)
```

Fill the formula down to `C4`.

**Answer:** `10100000` for pump P-2, which shows bits 5 and 7 set. The other two pumps return `00011111` and `00000111`.

### Problem 2: Fixed-Width Address Display

A sensor address is written as the hex value `3F`. A display panel must show exactly six binary digits.

**Task:** Convert `3F` to a six-digit binary string in `B2`.

**Solution:**

```excel
=HEX2BIN(B2, 6)
```

**Answer:** `111111`. Hex 3F equals 63 in decimal, and the six binary digits are all 1.

## Use Cases

### Device Status Flags

**Scenario:** A maintenance team decodes hex status bytes from equipment logs and wants a readable binary column next to each code.

```excel
=HEX2BIN(LogStatus[Code], 8)
```

**Why It Works:** The `places` value keeps every result at eight digits, so the bit positions line up across rows.

### Register Value Decoding

**Scenario:** An embedded systems engineer copies register values from a datasheet and checks which bits are set.

```excel
=HEX2BIN(A2, 10)
```

**Why It Works:** Ten digits show the full width of a 40-bit value. Negative results are always ten digits, so the padding has no effect on them.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input contains characters that are not hex digits, such as `G1`. | Correct the source value. |
| `#NUM!` | The result needs more characters than `places` allows, for example `HEX2BIN("FF", 4)`. | Increase `places` to at least 8. |
| `#NUM!` | A positive value greater than `1FF` was entered, such as `200`. | Split the value into smaller parts or use BIN2HEX for other ranges. |
| `#VALUE!` | `places` contains text. | Enter a number for `places` or remove it. |
| Wrong arithmetic | Google Sheets converts the binary result to a number, so adding to it treats the digits as decimal. | Convert the result back with BIN2DEC before doing arithmetic. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Excel for Microsoft 365 and Excel for the web | The padding argument is named `places`. |
| Google Sheets | Available | The padding argument is named `significant_digits`, and the result is silently converted to a number, so later arithmetic can be wrong. |

## Tips and Best Practices

- Enter hex values as text, for example `"1F"`, so that Excel does not read them as numbers.
- Use a fixed `places` value such as 8 for bytes or 10 for a full 40-bit field so that columns align.
- Convert binary results back with BIN2DEC or HEX2DEC before doing arithmetic on them.
- Keep the source hex in one column and the binary output in another so reviewers can check each conversion.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2DEC](BIN2DEC.md) | Converts a binary number back to decimal. |
| [BIN2HEX](BIN2HEX.md) | Converts a binary number to hexadecimal. |
| [DEC2BIN](DEC2BIN.md) | Converts a decimal number directly to binary. |
| [HEX2DEC](HEX2DEC.md) | Converts a hexadecimal number to decimal for arithmetic. |
| [HEX2OCT](HEX2OCT.md) | Converts a hexadecimal number to octal. |

## Official Documentation

- [Microsoft Support: HEX2BIN function](https://support.microsoft.com/en-us/excel/functions/hex2bin-function)
- [Google Docs Editors Help: HEX2BIN](https://support.google.com/docs/answer/3093139)
