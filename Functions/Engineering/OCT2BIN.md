---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Bit Pattern Reporting
  - Legacy Fault Code Decoding
related:
  - BIN2DEC
  - BIN2OCT
  - DEC2BIN
  - HEX2BIN
  - OCT2DEC
  - OCT2HEX
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/oct2bin-function
  - https://support.google.com/docs/answer/3093144
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Octal to Binary
tags:
  - base-conversion
  - binary
  - excel
  - octal
  - sheets
---

# OCT2BIN

## Description

**OCT2BIN** converts an octal (base 8) number to binary (base 2). Octal digits run from 0 to 7, and each octal digit stands for three binary digits, so the conversion is exact for every valid octal value. The result is text, such as `1010` for octal 12.

Use OCT2BIN when a legacy device, an older log file or a protocol document reports values in octal, but a person needs to read the individual bits. The optional second argument pads the result with leading zeros, which keeps a fixed-width bit field aligned. Use DEC2BIN instead when the input is a decimal number, and use OCT2DEC or OCT2HEX when the target is a decimal or hexadecimal value.

Negative values use two's-complement notation. Excel and Google Sheets both treat the most significant bit of a 10-digit octal value as the sign bit. A negative input always returns a 10-character binary result, and the padding argument is ignored for those values.

## Syntax

```excel
=OCT2BIN(number, [places])
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/OCT2BIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The octal number to convert. It may not contain more than 10 characters. Positive values can be at most 777 (octal), and negative values can be no lower than 7777777000 (octal). Google Sheets calls this argument `signed_octal_number`. |
| `places` | No | The number of characters in the result. When omitted, the function uses the fewest characters needed. Use it to pad the result with leading zeros. Google Sheets calls this argument `significant_digits`. |

### Return Value

A text string of binary digits. The function returns `#NUM!` when the input is not a valid octal number, when the result needs more characters than `places` allows, or when `places` is negative. In Excel it returns `#VALUE!` when `places` is not a number.

## Examples

### Example 1: Basic Conversion

```excel
=OCT2BIN(12)
```

**Result:** `1010`

Octal 12 is 1 times 8 plus 2, which is 10 in decimal. Ten in binary is 1010.

### Example 2: Padding the Result

```excel
=OCT2BIN(17,8)
```

**Result:** `00001111`

Octal 17 is 15 in decimal, which is 1111 in binary. The second argument pads the result to eight characters with leading zeros.

<!-- Image 2: Padding a Binary Result to a Fixed Width. See Images/Engineering/OCT2BIN.md -->

### Example 3: Negative Value in Two's Complement

```excel
=OCT2BIN(7777777760)
```

**Result:** `1111110000`

The input is the 10-digit octal form of -16. Negative results always have 10 characters, so the 10-bit pattern for -16 is returned without padding.

### Example 4: Octal Value at the Positive Limit

```excel
=OCT2BIN(777)
```

**Result:** `111111111`

Octal 777 is 511 in decimal, the largest positive value the function accepts. Its binary form has nine ones.

### Example 5: Padding From a Cell Reference

```excel
=OCT2BIN(B2,6)
```

**Result:** `000111` (with B2 holding `7`)

Pointing to a cell with a fixed `places` value keeps the output width the same down a column, even when the input values have different lengths.

## Story Problems

### Problem 1: Fault Flags on Three Presses

A factory's older press controllers report fault flags as octal codes. Each code is stored as a number in `B2:B4`. Each fault flag is a six-bit pattern, so the bits must be padded to six characters.

| Press | Octal Code |
| --- | --- |
| Press 1 | 7 |
| Press 2 | 12 |
| Press 3 | 30 |

**Task:** Convert each octal code to a six-bit binary pattern so a technician can read the flags.

**Solution:**

Enter this formula in `C2` and copy it down to `C4`.

```excel
=OCT2BIN(B2,6)
```

**Answer:** Press 1 gives `000111`, Press 2 gives `001010` and Press 3 gives `011000`.

### Problem 2: Negative Calibration Offset

A temperature logger stores a signed calibration offset as the octal value `7777777500` in `B2`. The offset is negative, and the logger's manual requires the binary form for its register.

| Sensor | Octal Offset |
| --- | --- |
| Logger 7 | 7777777500 |

**Task:** Convert the stored offset to binary.

**Solution:**

```excel
=OCT2BIN(B2)
```

**Answer:** `1101000000`. Octal 7777777500 is -192 in two's complement, and its 10-bit form is 1101000000.

## Use Cases

### Fault Flag Decoding

**Scenario:** A maintenance team decodes octal fault codes from a legacy controller so each flag can be matched to a bit position in the manual.

```excel
=OCT2BIN(FaultCode, 6)
```

**Why It Works:** The six-character padding keeps every flag in the same column width, so bit positions line up when the codes are compared.

### Bit Pattern Reporting

**Scenario:** A reporting sheet lists device status words that are documented in octal but reviewed in binary.

```excel
=OCT2BIN(StatusWord, 8)
```

**Why It Works:** A fixed eight-character width makes each status word easy to compare with the bit table in the device manual.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input contains a digit other than 0 to 7, such as 18. | Check that every digit is between 0 and 7. |
| `#NUM!` | The result needs more characters than `places` allows. | Increase `places` or leave it out. |
| `#NUM!` | `places` is negative. | Use a positive whole number for `places`. |
| `#VALUE!` | `places` is text in Excel. | Enter a number for `places` or refer to a cell that holds one. |
| Unexpected result | A decimal value was entered where an octal value was meant. | Confirm the source format, or use DEC2BIN for decimal input. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Argument names are number and places. For negative numbers, `places` is ignored and the result has 10 characters. |
| Google Sheets | Available | Argument names are signed_octal_number and significant_digits. When the input is 4000000000 (octal) or greater, significant_digits is ignored. |

## Tips and Best Practices

- Always pass `places` when the output feeds a fixed-width field, so every result has the same length.
- Check the input for digits 8 and 9, which are common typing errors in octal data.
- Use a cell reference for `places` when several conversions need the same width.
- Convert with OCT2DEC first when a result must be read as a number rather than a bit pattern.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2DEC](BIN2DEC.md) | Converts a binary result back to decimal. |
| [BIN2OCT](BIN2OCT.md) | Converts binary directly to octal, the reverse direction. |
| [DEC2BIN](DEC2BIN.md) | Converts a decimal number to binary. |
| [HEX2BIN](HEX2BIN.md) | Converts hexadecimal to binary. |
| [OCT2DEC](OCT2DEC.md) | Converts octal to decimal when the target is a number. |
| [OCT2HEX](OCT2HEX.md) | Converts octal to hexadecimal. |

## Official Documentation

- [Microsoft Support: OCT2BIN function](https://support.microsoft.com/en-us/excel/functions/oct2bin-function)
- [Google Docs Editors Help: OCT2BIN](https://support.google.com/docs/answer/3093144)
