---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Network Packet Headers
  - Signed Register Values
related:
  - BIN2DEC
  - BIN2OCT
  - DEC2HEX
  - HEX2BIN
  - HEX2DEC
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/bin2hex-function
  - https://support.google.com/docs/answer/3093133
date-created: 2025-06-20
date-revised: 2026-11-22
aliases:
  - Binary To Hexadecimal
tags:
  - binary
  - excel
  - hexadecimal
  - number-base
  - sheets
---

# BIN2HEX

## Description

**BIN2HEX** converts a binary number to hexadecimal text. Like the other binary conversion functions, it works on values of up to 10 characters, where the leftmost bit is the sign bit and negative values use two's complement notation.
A negative input always returns a 10-character hexadecimal result, so the optional places argument has no effect on negative values.

Use BIN2HEX when a source system writes values in binary and a report, a memory map or a protocol note needs the shorter hexadecimal form. Each hex digit stands for four bits, so the result is easier to read than a long binary string.

The optional places argument pads the result with leading zeros to a fixed width. Leave it out to get the fewest digits needed. Only the digits 0 and 1 are valid, and a result that needs more digits than places allows returns `#NUM!`.

BIN2HEX is available in Microsoft Excel and Google Sheets. Google calls the second argument `significant_digits`.

## Syntax

```excel
=BIN2HEX(number, [places])
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/BIN2HEX.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The binary value to convert, up to 10 characters. Values with a leading 1 in a 10-character string are negative. |
| `places` | No | The number of characters in the result. Shorter results are padded with leading zeros. Ignored for negative values. A non-integer is truncated, and a negative value returns `#NUM!`. |

### Return Value

A hexadecimal value as text, using the digits 0 to 9 and the letters A to F. The function returns `#NUM!` for invalid binary input or when the result is wider than `places` allows, and `#VALUE!` when `places` is not numeric.

## Examples

### Example 1: Padding to Four Characters

```excel
=BIN2HEX(10110101, 4)
```

**Result:** `00B5`

The binary value is 181, which is B5 in hexadecimal. The places argument pads it to four characters.

### Example 2: Without Padding

```excel
=BIN2HEX(1010)
```

**Result:** `A`

Without the places argument, the function returns only the digits needed, which is a single character here.

### Example 3: Filled Down a Column

Codes in `A2:A4` are `1111`, `100000` and `1000000`.

```excel
=BIN2HEX(A2)
```

Fill the formula down to `B4`.

**Result:** `F` (A2), `20` (A3), `40` (A4)

Each row converts independently, so the same formula handles a list of mixed-length codes.

<!-- Image 2: Four-Bit Groups to Hex Digits. See Images/Engineering/BIN2HEX.md -->

### Example 4: Negative Input

```excel
=BIN2HEX(1000000000)
```

**Result:** `FFFFFFFE00`

The input is -512 in 10-bit two's complement. The result is always 10 characters for a negative value, so the places argument would be ignored here.

## Story Problems

### Problem 1: Packet Header Bytes

A network log stores four header fields as binary text. The team needs each value in two-digit hexadecimal for a protocol note.

| Field | Binary |
| --- | --- |
| Flags | 01111111 |
| Length | 00010010 |
| Type | 01000001 |

**Task:** Put `=BIN2HEX(B2, 2)` in `C2`, fill it down to `C4`, and record the three results.

**Solution:**

```excel
=BIN2HEX(B2, 2)
```

**Answer:** Flags `7F`, Length `12` and Type `41`.

<!-- Image 3: Results Panel for the Story Problems. See Images/Engineering/BIN2HEX.md -->

### Problem 2: Reading a Negative Register

A controller holds a signed register value of `1111110110`. The engineer must record its hexadecimal form for the register map.

| Item | Value |
| --- | --- |
| Register | 1111110110 |
| Places | 10 |

**Task:** Convert the register value to hexadecimal, using 10 characters.

**Solution:**

```excel
=BIN2HEX("1111110110", 10)
```

**Answer:** `FFFFFFFFF6`. The value is -10, and the 10-character result is the two's complement form.

## Use Cases

### Network Packet Headers

**Scenario:** A capture export lists header flags in binary, and an analyst needs a two-digit hexadecimal value for each row.

```excel
=BIN2HEX(Table1[FlagBits], 2)
```

**Why It Works:** Each binary code converts to a fixed-width hex value, which keeps a table of flags aligned.
Dynamic array versions of Excel return the full column from one formula.

### Signed Register Values

**Scenario:** A device manual lists signed register settings in binary, and a technician builds a lookup table of hexadecimal values for a configuration tool.

```excel
=BIN2HEX(B2, 4)
```

**Why It Works:** Four characters keep positive values aligned in the table.
Negative values always return 10 characters, so check the column width before printing.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input contains a digit other than 0 or 1, or has more than 10 characters. | Clean the source text and remove any spaces or letters. |
| `#NUM!` | The result needs more characters than `places` allows. | Increase `places` or remove it. |
| `#VALUE!` | `places` is text. | Enter a number for the places argument. |
| Wrong type in Sheets | A result with only digits is stored as a number. | Format the cell as plain text before combining results with arithmetic. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365 and current Excel versions | Arguments are `number` and `places`. Check the Microsoft Support page for the exact version list. |
| Google Sheets | Available | Arguments are `signed_binary_number` and `significant_digits`. Results that contain only digits can be converted to numbers, so keep the output as text. |

## Tips and Best Practices

- Pad results with `places` when the values feed a fixed-width field such as a register map or a packet layout.
- Keep binary inputs as text so leading zeros are not lost.
- Use DEC2HEX when the source is decimal and HEX2BIN when the target is binary.
- Remember that hexadecimal results with no letters, such as `120`, look like decimal numbers to Sheets and may be treated as numbers.
- Convert to decimal with HEX2DEC when a later formula needs arithmetic on the value.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2DEC](BIN2DEC.md) | Converts the same binary value to decimal. |
| [BIN2OCT](BIN2OCT.md) | Converts the same binary value to octal. |
| [DEC2HEX](DEC2HEX.md) | Converts a decimal number to hexadecimal. |
| [HEX2BIN](HEX2BIN.md) | Converts hexadecimal text back to binary. |
| [HEX2DEC](HEX2DEC.md) | Converts hexadecimal text to decimal for arithmetic. |

## Official Documentation

- [Microsoft Support: BIN2HEX function](https://support.microsoft.com/en-us/excel/functions/bin2hex-function)
- [Google Docs Editors Help: BIN2HEX](https://support.google.com/docs/answer/3093133)
