---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Bin Label Formatting
  - Packed Color Values
related:
  - BIN2HEX
  - DEC2BIN
  - DEC2OCT
  - HEX2BIN
  - HEX2DEC
  - HEX2OCT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/dec2hex-function
  - https://support.google.com/docs/answer/3093137
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Decimal to Hex
  - Decimal to Hexadecimal
tags:
  - conversion
  - excel
  - hexadecimal
  - number-base
  - sheets
---

# DEC2HEX

## Description

**DEC2HEX** converts a whole decimal number into hexadecimal text, which uses the digits 0 to 9 and the letters A to F. Hexadecimal is compact, so it appears in color codes, memory addresses, product labels and device logs. The result is text, so it can be displayed or stored, but arithmetic on it should be done after converting back with HEX2DEC.

Excel accepts decimal values from -549,755,813,888 to 549,755,813,887. A positive value uses only as many digits as it needs, unless the optional `places` argument pads it with leading zeros. A negative value is written as a 10-character, 40-bit two's complement number, and the `places` argument is ignored for it.

Use DEC2HEX when the output must be short and readable. For binary or octal output, use DEC2BIN or DEC2OCT, which have smaller ranges.

## Syntax

```excel
=DEC2HEX(number, [places])
```

<!-- Image 1: Decimal to Hexadecimal Digits. See Images/Engineering/DEC2HEX.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A whole decimal number from -549,755,813,888 to 549,755,813,887. Values outside the range return `#NUM!`. |
| `places` | No | The number of characters in the result. Shorter results are padded with leading zeros. Non-integer values are truncated, and negative values return `#NUM!`. |

### Return Value

A text string of hexadecimal digits in uppercase. The function returns `#NUM!` when `number` is outside its range, when `places` is negative, or when the result needs more characters than `places` allows. It returns `#VALUE!` when either argument is not numeric.

## Examples

### Example 1: Pad to Four Characters

```excel
=DEC2HEX(100,4)
```

**Result:** `0064`

100 is 64 in hexadecimal, and the `places` argument pads it to four characters.

### Example 2: Two's Complement for a Negative Value

```excel
=DEC2HEX(-54)
```

**Result:** `FFFFFFFFCA`

A negative value is written as a 10-character, 40-bit two's complement number, so the leftmost F characters are the sign extension.

### Example 3: Short Result

```excel
=DEC2HEX(28)
```

**Result:** `1C`

28 is 16 plus 12, and 12 is C in hexadecimal, so the result is 1C.

### Example 4: Result Too Long for Places

```excel
=DEC2HEX(64,1)
```

**Result:** `#NUM!`

64 is 40 in hexadecimal, which needs two characters. Setting `places` to 1 is too short, so the function returns `#NUM!`.

## Story Problems

### Problem 1: Warehouse Bin Labels

A warehouse numbers its bins in decimal, but the scanner labels show four hexadecimal characters so staff can match them to the printed map. Each bin number must be padded to four characters.

| Bin Number |
| --- |
| 255 |
| 4096 |
| 4660 |

**Task:** Convert each bin number in column A to a four-character hexadecimal label, starting at A2.

**Solution:**

```excel
=DEC2HEX(A2,4)
```

Enter this in B2 and fill it down to B4.

**Answer:** `00FF`, `1000`, and `1234`. Bin 4660 has the label 1234, which is 1 times 4096 plus 2 times 256 plus 3 times 16 plus 4.

### Problem 2: Packed Color Values

A design team stores three colors as packed decimal values. Each value must become a six-character hexadecimal code for the style sheet, with leading zeros kept.

| Color | Decimal Value |
| --- | --- |
| Red | 16711680 |
| Green | 65280 |
| Blue | 255 |

**Task:** Convert each decimal value in column B to a six-character hexadecimal code, starting at B2.

**Solution:**

```excel
=DEC2HEX(B2,6)
```

Enter this in C2 and fill it down to C4.

**Answer:** `FF0000`, `00FF00`, and `0000FF`. Each code has six characters, so the leading zeros keep the colors in the same position in the style sheet.

<!-- Image 2: Bin Labels Table. See Images/Engineering/DEC2HEX.md -->

## Use Cases

### Bin Label Formatting

**Scenario:** A label printing job needs a fixed-width hexadecimal code for every bin in the inventory list.

```excel
=DEC2HEX(Bins[Number],4)
```

**Why It Works:** Padding to four characters gives every label the same length, so the printed codes line up. Bins numbered above 65535 need more characters, so raise `places` for those rows.

### Packed Color Values

**Scenario:** A style export stores each color as a decimal value, and the web team needs the six-character hexadecimal form.

```excel
=DEC2HEX(B2,6)
```

**Why It Works:** Six characters match the standard RGB code width, and the padding keeps dark colors with leading zeros readable.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The number is outside the Excel range, or `places` is negative. | Check the input range and use a positive `places` value. |
| `#NUM!` | The result needs more characters than `places` allows. | Increase `places` to the length of the hexadecimal value. |
| `#VALUE!` | An argument is text that cannot be read as a number. | Clean the source cell or convert it with `VALUE`. |
| Wrong result in later math | The hexadecimal text is used in arithmetic. | Convert it back with HEX2DEC before calculating. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 and Excel for the web | Range from -549,755,813,888 to 549,755,813,887. The `places` argument pads the result. |
| Google Sheets | Available | Uses `significant_digits` for padding. The help page warns that Sheets can convert the hexadecimal text in later calculations, so results can be misleading. |

## Tips and Best Practices

- Use a fixed `places` value for every label or code, so the output width stays the same as the data grows.
- Keep the result as text, and use HEX2DEC before doing any arithmetic on it.
- Uppercase letters are the standard output in Excel, so match that case in lookups.
- Wrap the formula in IFERROR when a column may contain values that are out of range, and mark those rows for review.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2HEX](BIN2HEX.md) | Converts a binary string directly to hexadecimal. |
| [DEC2BIN](DEC2BIN.md) | Converts the same decimal value to binary. |
| [DEC2OCT](DEC2OCT.md) | Converts the same decimal value to octal. |
| [HEX2BIN](HEX2BIN.md) | Converts a hexadecimal string to binary. |
| [HEX2DEC](HEX2DEC.md) | Converts a hexadecimal string back to decimal before arithmetic. |
| [HEX2OCT](HEX2OCT.md) | Converts a hexadecimal string to octal. |

## Official Documentation

- [Microsoft Support: DEC2HEX function](https://support.microsoft.com/en-us/excel/functions/dec2hex-function)
- [Google Docs Editors Help: DEC2HEX](https://support.google.com/docs/answer/3093137)
