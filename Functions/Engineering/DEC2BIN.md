---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Relay Status Strings
  - Signed Offset Encoding
related:
  - BIN2DEC
  - BIN2HEX
  - BIN2OCT
  - DEC2HEX
  - DEC2OCT
  - HEX2BIN
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/dec2bin-function
  - https://support.google.com/docs/answer/3092997
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Decimal to Binary
  - Signed Binary Conversion
tags:
  - binary
  - conversion
  - excel
  - number-base
  - sheets
---

# DEC2BIN

## Description

**DEC2BIN** converts a whole decimal number into its binary text form, using only the digits 0 and 1. It is useful wherever a device, log or specification shows status as a row of bits, such as a relay board where each digit represents one channel. The result is text, so it can be displayed or stored, but it should not be used in arithmetic.

Excel accepts decimal numbers from -512 to 511. A positive value uses as few digits as it needs unless you set the optional `places` argument to pad it with leading zeros. A negative value is written in 10-bit two's complement form, so `DEC2BIN(-100)` returns `1110011100`, and `places` is not applied to it in the same way.

Use DEC2BIN with BIN2DEC when you need to move a value back and forth between bases. For hexadecimal or octal output, use DEC2HEX or DEC2OCT, which accept larger ranges.

## Syntax

```excel
=DEC2BIN(number, [places])
```

<!-- Image 1: Decimal, Binary and Padding. See Images/Engineering/DEC2BIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A whole decimal number from -512 to 511. Values outside the range return `#NUM!`. |
| `places` | No | The number of characters in the result. Shorter results are padded with leading zeros. If the result needs more characters than `places` allows, the function returns `#NUM!`. |

### Return Value

A text string of binary digits. The function returns `#NUM!` when `number` is outside -512 to 511, when `places` is zero or negative, or when the result needs more characters than `places` allows. It returns `#VALUE!` when either argument is not numeric.

## Examples

### Example 1: Pad to Four Characters

```excel
=DEC2BIN(9,4)
```

**Result:** `1001`

9 needs four binary digits, so the padding has no effect. A value such as 1 with `places` of 4 would return `0001`.

### Example 2: Negative Value in Ten Bits

```excel
=DEC2BIN(-100)
```

**Result:** `1110011100`

Negative numbers use 10-bit two's complement, where the leftmost bit is the sign bit. The 10-bit value of -100 is 1024 minus 100, which is 924, or 1110011100 in binary.

### Example 3: Value at the Upper Limit

```excel
=DEC2BIN(511)
```

**Result:** `111111111`

511 is the largest positive value Excel accepts, and it needs nine binary digits. The value 512 returns `#NUM!` because it is outside the range.

### Example 4: Convert a Cell Value

```excel
=DEC2BIN(A2,8)
```

**Result:** `00000101` when cell A2 holds 5

The formula pads the result to eight characters. Problem 1 below applies it to a full list.

## Story Problems

### Problem 1: Relay Channel Status

A control board turns relays on and off with a channel number. The technician needs each channel number shown as an eight-digit binary string so the board's status row can be read against the wiring diagram.

| Channel Number |
| --- |
| 5 |
| 18 |
| 200 |

**Task:** Convert each channel number in column A to an eight-digit binary string, starting at A2.

**Solution:**

```excel
=DEC2BIN(A2,8)
```

Enter this in B2 and fill it down to B4.

**Answer:** `00000101`, `00010010`, and `11001000`. Each string has one digit per relay position, read from right to left.

<!-- Image 2: Relay Channel Status Table. See Images/Engineering/DEC2BIN.md -->

### Problem 2: Signed Offsets in Ten Bits

A sensor stores three signed offsets as 10-bit values. Negative offsets use two's complement, and the technician needs the binary form of each offset to load into the register.

| Offset |
| --- |
| -100 |
| -1 |
| 12 |

**Task:** Convert each offset in column A to its binary form, starting at A2.

**Solution:**

```excel
=DEC2BIN(A2)
```

Enter this in B2 and fill it down to B4.

**Answer:** `1110011100`, `1111111111`, and `1100`. The two negative values use all ten bits, and the positive value needs only four.

## Use Cases

### Relay Status Strings

**Scenario:** A maintenance log shows which relay channels are active, and the report needs a readable binary pattern for each board.

```excel
=DEC2BIN(Relays[Channel],8)
```

**Why It Works:** Padding to eight characters keeps every string the same width, so the columns line up when the report is printed.

### Signed Offset Encoding

**Scenario:** A configuration sheet lists signed offsets that must be written to a device as 10-bit values.

```excel
=DEC2BIN(B2)
```

**Why It Works:** Negative offsets are converted automatically to two's complement, and no separate sign handling is needed. Check that each value stays between -512 and 511 first.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The number is outside -512 to 511. | Check the input range or split the value across two fields. |
| `#NUM!` | The result needs more characters than `places` allows. | Increase `places` to the length of the binary value. |
| `#VALUE!` | `number` or `places` is text that cannot be read as a number. | Clean the source cell or convert it with `VALUE`. |
| Wrong length | `places` was omitted, so the result has no leading zeros. | Set `places` to the width the device expects. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 and Excel for the web | Range -512 to 511. The optional `places` argument pads the result. |
| Google Sheets | Available | Uses `significant_digits` for padding. Positive values go up to 511 and negative values down to -512. The help page warns that the text result can be converted silently in later calculations. |

## Tips and Best Practices

- Pad every binary output to the width the device expects, so the strings align.
- Keep the result as text. A binary string used in arithmetic can give a misleading number, so convert it back with BIN2DEC first.
- Check the input range before you convert large values, because values above 511 return `#NUM!` in Excel.
- Use IFERROR around the formula in reports that must not show error codes, and flag the row for review instead.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2DEC](BIN2DEC.md) | Converts a binary string back to decimal. |
| [BIN2HEX](BIN2HEX.md) | Converts a binary string directly to hexadecimal. |
| [BIN2OCT](BIN2OCT.md) | Converts a binary string directly to octal. |
| [DEC2HEX](DEC2HEX.md) | Converts a decimal number to hexadecimal, with a wider range. |
| [DEC2OCT](DEC2OCT.md) | Converts a decimal number to octal. |
| [HEX2BIN](HEX2BIN.md) | Converts a hexadecimal string to binary. |

## Official Documentation

- [Microsoft Support: DEC2BIN function](https://support.microsoft.com/en-us/excel/functions/dec2bin-function)
- [Google Docs Editors Help: DEC2BIN](https://support.google.com/docs/answer/3092997)
