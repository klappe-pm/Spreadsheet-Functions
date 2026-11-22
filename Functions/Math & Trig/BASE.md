---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Roman and Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Base 36 Box Labels
  - Hexadecimal Device Codes
  - Padded Serial Numbers
related:
  - BIN2DEC
  - DEC2BIN
  - DEC2HEX
  - DEC2OCT
  - HEX2DEC
  - TEXT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/base-function
  - https://support.google.com/docs/answer/9084167
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Number To Base Text
  - Radix Conversion
tags:
  - base-conversion
  - excel
  - identifiers
  - sheets
  - text
---

# BASE

## Description

**BASE** converts a whole number into text written in another number base (radix). Use it to turn a decimal value into binary (base 2), octal (base 8), hexadecimal (base 16), or any base up to 36, which uses the digits 0 to 9 followed by the letters A to Z.

BASE can also pad the result with leading zeros. The optional third argument sets the minimum length of the text, which keeps codes such as serial numbers or box labels a fixed width. Leading zeros are added only when that argument is included.

The result is text, not a number. Arithmetic on a BASE result can give misleading answers, so keep the converted value for display, lookup, or printing. Use `DEC2BIN`, `DEC2HEX`, and related functions when you need a fixed bit or hex format with the limits those functions impose. Microsoft Excel and Google Sheets accept the same three arguments in the same order.

## Syntax

```excel
=BASE(number, radix, [min_length])
```

<!-- Image 1: BASE Argument Layout. See Images/Math & Trig/BASE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to convert. It must be an integer of 0 or more and less than 2^53. Decimal parts are truncated. Google Sheets calls this argument `value`. |
| `radix` | Yes | The target base, an integer from 2 to 36. Google Sheets calls this argument `base`. |
| `min_length` | No | The minimum number of characters in the result, from 0 to 255. The result is padded with leading zeros when it is shorter. Omit it to get no padding. |

### Return Value

A text string that shows `number` in the target base, using uppercase letters for digits above 9. The function returns `#NUM!` when `number`, `radix`, or `min_length` is outside its allowed range, and `#VALUE!` when `number` is not numeric.

## Examples

### Example 1: Decimal to Hexadecimal

```excel
=BASE(255, 16)
```

**Result:** `FF`

The decimal value 255 is 15 times 16 plus 15, which is written as FF in base 16.

### Example 2: Binary With Padding

```excel
=BASE(10, 2, 8)
```

**Result:** `00001010`

The value 10 is 1010 in binary. The third argument pads the text to eight characters.

### Example 3: Hexadecimal With Padding

```excel
=BASE(4095, 16, 6)
```

**Result:** `000FFF`

The value 4095 is FFF in hexadecimal. Padding to six characters makes it match a six-character code format.

### Example 4: Converting a Cell Value

```excel
=BASE(A2, 2)
```

**Result:** `10101` when A2 contains 21

This form works well in a column of values. Each row converts its own number without a helper column.

### Example 5: Combined With Text

```excel
="0x" & BASE(255, 16, 2)
```

**Result:** `0xFF`

The ampersand joins a fixed prefix to the converted digits. Use this pattern to build codes that carry a label such as a hexadecimal prefix.

## Story Problems

### Problem 1: Serial Numbers for Test Equipment

A lab writes equipment serial numbers as four-character hexadecimal codes. The inventory list stores each serial as a decimal number.

| Equipment | Decimal Serial | Hex Code |
| --- | --- | --- |
| Oscilloscope | 1024 | |
| Multimeter | 255 | |
| Probe Kit | 16 | |

**Task:** Convert each decimal serial into a four-character hexadecimal code, padded with zeros.

**Solution:**

```excel
=BASE(B2, 16, 4)
```

Copy the formula down to row 4.

**Answer:** The codes are `0400`, `00FF`, and `0010`. Each value is converted to base 16 and padded to four characters.

<!-- Image 2: Padded Hexadecimal Serial Codes. See Images/Math & Trig/BASE.md -->

### Problem 2: Box Labels in Base 36

A warehouse numbers boxes from 1 upward and prints short labels using base 36, which uses digits and letters. Each label must be three characters long.

| Box Number | Label |
| --- | --- |
| 35 | |
| 36 | |
| 1000 | |
| 1295 | |

**Task:** Create a three-character base 36 label for each box number.

**Solution:**

```excel
=BASE(A2, 36, 3)
```

**Answer:** The labels are `00Z`, `010`, `0RS`, and `0ZZ`. Box 1295 converts to `ZZ`, which has two characters, so the padding adds one leading zero.

<!-- Image 3: Base 36 Label Table. See Images/Math & Trig/BASE.md -->

## Use Cases

### Hexadecimal Device Codes

**Scenario:** A manufacturer stores device counts as decimal numbers, but the field technicians read hexadecimal codes printed on the labels.

```excel
=BASE(Devices[Count], 16, 4)
```

**Why It Works:** The padding argument keeps every code the same width, so technicians can scan the labels quickly. Each row is converted by the same formula, so the column stays consistent when rows are added.

### Base 36 Box Labels

**Scenario:** A distribution center prints compact box labels that use letters and digits to fit a small sticker.

```excel
=BASE(A2, 36, 3)
```

**Why It Works:** Base 36 packs many numbers into few characters. Keeping the label length fixed prevents the sticker printer from misaligning the text.

### Padded Serial Numbers

**Scenario:** An asset register stores serial numbers as decimal values, and a barcode scanner expects exactly six characters.

```excel
=BASE(B2, 16, 6)
```

**Why It Works:** The third argument adds leading zeros until the code reaches six characters. Without the argument, short codes would not match the scanner format.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The radix is outside 2 to 36, the number is negative, or `min_length` is outside 0 to 255. | Check each argument against its allowed range. |
| `#VALUE!` | The number argument is text or an empty cell. | Convert the value to a number or use `IF(A2="", "", BASE(A2, 16))`. |
| Padding missing | The third argument was left out. | Add the minimum length argument to pad the result. |
| Wrong sum | Arithmetic is applied to the text result. | Convert the result back with a function such as `DEC2BIN` or keep the decimal value in a separate column. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions and Excel for the web | Argument names are `Number`, `Radix`, and `Min_length`. Errors follow the `#NUM!` and `#VALUE!` rules listed above. |
| Google Sheets | Available | Argument names are `value`, `base`, and `min_length`. Sheets converts the text result silently when you use it in arithmetic, which can produce wrong totals. |

## Tips and Best Practices

- Use the third argument whenever a code must have a fixed width.
- Keep decimal source values in one column and text codes in another, so the numbers stay available for calculations.
- Round or truncate the input first if it may contain decimals, because the function drops the decimal part.
- Use `DEC2HEX` or `DEC2BIN` for codes that must be checked by range, since those functions limit the values they accept.
- Test one converted value by hand before you fill a column of labels.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DEC2BIN](../Engineering/DEC2BIN.md) | Converts decimal to binary with a fixed bit range. |
| [DEC2HEX](../Engineering/DEC2HEX.md) | Converts decimal to hexadecimal with a fixed bit range. |
| [DEC2OCT](../Engineering/DEC2OCT.md) | Converts decimal to octal with a fixed bit range. |
| [BIN2DEC](../Engineering/BIN2DEC.md) | Converts binary text back to a decimal number. |
| [HEX2DEC](../Engineering/HEX2DEC.md) | Converts hexadecimal text back to a decimal number. |
| [TEXT](../Text/TEXT.md) | Formats a number as text, but cannot change its base. |

## Official Documentation

- [Microsoft Support: BASE function](https://support.microsoft.com/en-us/excel/functions/base-function)
- [Google Docs Editors Help: BASE](https://support.google.com/docs/answer/9084167)
