---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - File Permission Codes
  - Legacy Code Conversion
related:
  - BIN2OCT
  - DEC2OCT
  - HEX2BIN
  - HEX2DEC
  - OCT2HEX
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/hex2oct-function
  - https://support.google.com/docs/answer/3093142
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Hex to Octal
tags:
  - excel
  - number-base
  - sheets
---

# HEX2OCT

## Description

**HEX2OCT** converts a hexadecimal number (base 16) to an octal number (base 8). Octal is still used for Unix file permissions and for some older hardware and software codes, so HEX2OCT is the direct route when a source system reports hex and the target system expects octal.

The input can be at most 10 characters and uses a 40-bit two's-complement format with the most significant bit as the sign bit. Positive values cannot be greater than `1FFFFFFF` (536,870,911 in decimal), and negative values cannot be less than `FFE0000000`. Negative results are always 10 octal digits long.

The optional `places` argument pads the result with leading zeros to a fixed width. Google Sheets calls it `significant_digits` and converts the output to a number, so arithmetic on the result can produce values that are not valid octal numbers.

## Syntax

```excel
=HEX2OCT(number, [places])
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/HEX2OCT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The hexadecimal value to convert, as text in quotes (`"1ED"`), a cell reference or a valid hex number entered without quotes. It cannot exceed 10 characters. |
| `places` | No | The number of characters in the result. If omitted, the function uses the fewest characters needed. The result is padded with leading zeros. Negative results always have 10 characters and ignore `places`. |

### Return Value

The octal equivalent of the hexadecimal input, as digits 0 to 7. The function returns `#NUM!` when `number` is not valid hex, when the result needs more characters than `places` allows, or when `places` is negative. It returns `#VALUE!` when `places` is nonnumeric.

## Examples

### Example 1: Padding a Short Result

```excel
=HEX2OCT("F", 3)
```

**Result:** `017`

Hex F equals 15 in decimal, which is 17 in octal. The `places` value pads the result to three characters.

### Example 2: Converting a Four-Digit Value

```excel
=HEX2OCT("3B4E")
```

**Result:** `35516`

Hex 3B4E equals 15182 in decimal, which is 35516 in octal.

### Example 3: Negative Value

```excel
=HEX2OCT("FFFFFFFF00")
```

**Result:** `7777777400`

The sign bit is set, so the result is a negative 40-bit value written as a 10-digit octal number.

### Example 4: Converting a Cell Reference

Cell `A2` holds the text `199`.

```excel
=HEX2OCT(A2)
```

**Result:** `631`

Hex 199 equals 409 in decimal, which is 631 in octal.

<!-- Image 2: Permission Mode Table. See Images/Engineering/HEX2OCT.md -->

## Story Problems

### Problem 1: Unix Permission Codes

A systems administrator stores permission values as hex in a configuration file. The target tool expects a four-digit octal mode, such as `0755`.

| File | Permission (Hex) |
| --- | --- |
| deploy.sh | 1ED |
| config.env | 1A4 |
| backup.tar | 1FF |

**Task:** Convert each permission to a four-digit octal string in column C, then read the value for `config.env` in `C3`.

**Solution:**

```excel
=HEX2OCT(B2, 4)
```

Fill the formula down to `C4`.

**Answer:** `0644` for `config.env`. The other two files return `0755` and `0777`.

### Problem 2: Legacy Equipment Code

A plant system stores a machine code as the hex value `3B4E`. A legacy controller expects the octal form.

**Task:** Convert `3B4E` in cell `B2` to octal.

**Solution:**

```excel
=HEX2OCT(B2)
```

**Answer:** `35516`, which is the same value as Example 2.

## Use Cases

### File Permission Codes

**Scenario:** An administrator generates a deployment script that sets permissions from a hex table exported by an audit tool.

```excel
=HEX2OCT(PermissionTable[HexMode], 4)
```

**Why It Works:** The four-digit padding gives the familiar mode format, so the output can be pasted into a script without manual edits.

### Legacy Code Conversion

**Scenario:** A data team migrates hex product codes from a modern database to an older system that stores octal identifiers.

```excel
=HEX2OCT(TRIM(A2), 10)
```

**Why It Works:** TRIM removes stray spaces, and the ten-digit padding keeps every code the same width in the legacy file.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input contains a character other than 0 to 9 or A to F. | Correct the source value. |
| `#NUM!` | The octal result needs more digits than `places`, for example `HEX2OCT("1FF", 2)` where the result is `777`. | Increase `places` to at least 3. |
| `#NUM!` | `places` is negative. | Use a positive whole number for `places`. |
| `#VALUE!` | `places` contains text. | Enter a number or remove the argument. |
| Wrong arithmetic | Google Sheets converts the octal result to a number, so adding to it does not follow octal rules. | Convert the result with OCT2DEC before doing arithmetic. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Excel for Microsoft 365 and Excel for the web | The padding argument is named `places`. Positive values are limited to `1FFFFFFF`. |
| Google Sheets | Available | The padding argument is named `significant_digits`, and the result is silently converted to a number. |

## Tips and Best Practices

- Enter hex values as text, for example `"1ED"`, to keep them from being read as numbers.
- Use `places` set to 4 for Unix permission modes and to 10 for fixed-width legacy codes.
- Check the source value against the limits in the Description before converting large values.
- Convert octal results back with OCT2DEC or OCT2HEX before doing any arithmetic.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DEC2OCT](DEC2OCT.md) | Converts a decimal value directly to octal. |
| [HEX2BIN](HEX2BIN.md) | Converts a hex value to binary for bit-level reading. |
| [HEX2DEC](HEX2DEC.md) | Converts a hex value to decimal for arithmetic. |
| [OCT2HEX](OCT2HEX.md) | Converts an octal value back to hexadecimal. |
| [OCT2DEC](OCT2DEC.md) | Converts an octal value to decimal. |

## Official Documentation

- [Microsoft Support: HEX2OCT function](https://support.microsoft.com/en-us/excel/functions/hex2oct-function)
- [Google Docs Editors Help: HEX2OCT](https://support.google.com/docs/answer/3093142)
