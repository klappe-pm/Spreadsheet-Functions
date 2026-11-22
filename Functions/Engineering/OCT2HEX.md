---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Legacy Register Display
  - Memory Address Translation
related:
  - BIN2HEX
  - DEC2HEX
  - HEX2DEC
  - HEX2OCT
  - OCT2BIN
  - OCT2DEC
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/oct2hex-function
  - https://support.google.com/docs/answer/3093147
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Octal to Hexadecimal
tags:
  - base-conversion
  - excel
  - hexadecimal
  - octal
  - sheets
---

# OCT2HEX

## Description

**OCT2HEX** converts an octal (base 8) number to hexadecimal (base 16). Octal and hexadecimal digits both map exactly onto groups of binary bits, so the conversion is exact for every valid input. The result is text in capital letters, such as `FF` for octal 377.

Use OCT2HEX when a source system reports values in octal, such as a legacy memory map or a register dump, but the people reading the output are used to hexadecimal. The optional second argument sets the minimum number of characters, so addresses and codes can be padded to a fixed width. Use HEX2OCT for the reverse direction, and use OCT2DEC or OCT2BIN when the target is decimal or binary.

OCT2HEX reads signed 30-bit octal values. The most significant bit is the sign bit, and negative inputs use two's-complement notation. A negative input always returns a 10-character hexadecimal result, and any padding argument is ignored for those values.

## Syntax

```excel
=OCT2HEX(number, [places])
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/OCT2HEX.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The octal number to convert. It may not contain more than 10 octal characters (30 bits). Digits must be 0 to 7. Google Sheets calls this argument `signed_octal_number`. |
| `places` | No | The number of characters to use in the result. When omitted, the function uses the fewest characters needed. The result is padded with leading zeros to reach this length. Google Sheets calls this argument `significant_digits`. |

### Return Value

A text string of hexadecimal digits in capital letters. The function returns `#NUM!` when the input is not a valid octal number, when the result needs more characters than `places` allows, or when `places` is negative. In Excel it returns `#VALUE!` when `places` is not a number.

## Examples

### Example 1: Basic Conversion

```excel
=OCT2HEX(377)
```

**Result:** `FF`

Octal 377 is 255 in decimal, which is FF in hexadecimal.

### Example 2: Padding the Result

```excel
=OCT2HEX(20,4)
```

**Result:** `0010`

Octal 20 is 16 in decimal, which is 10 in hexadecimal. The second argument pads the result to four characters.

<!-- Image 2: Padding a Hexadecimal Result to a Fixed Width. See Images/Engineering/OCT2HEX.md -->

### Example 3: Value Near the Positive Limit

```excel
=OCT2HEX(777)
```

**Result:** `1FF`

Octal 777 is 511 in decimal, which is 1FF in hexadecimal.

### Example 4: Negative Value in Two's Complement

```excel
=OCT2HEX(7777777760)
```

**Result:** `FFFFFFFFF0`

The input is the 10-digit octal form of -16. The result is always 10 characters for a negative value, so the padding argument would be ignored here.

## Story Problems

### Problem 1: Memory Block Start Addresses

A legacy controller lists the start addresses of four memory blocks in octal. The team wants each address as a four-character hexadecimal code. The first three addresses are stored in `B2:B4`.

| Block | Octal Address |
| --- | --- |
| Block 1 | 1000 |
| Block 2 | 2777 |
| Block 3 | 377 |

**Task:** Convert each address to hexadecimal with four characters. Enter the formula in `C2` and copy it down to `C4`.

**Solution:**

```excel
=OCT2HEX(B2,4)
```

**Answer:** Block 1 gives `0200`, Block 2 gives `05FF` and Block 3 gives `00FF`. Octal 1000 is 512, octal 2777 is 1535 and octal 377 is 255.

### Problem 2: Negative Offset in a Register

A sensor register stores a signed offset as the octal value `7777777400` in `B2`. The register display needs the hexadecimal form of the stored value.

| Register | Octal Offset |
| --- | --- |
| Offset Register | 7777777400 |

**Task:** Convert the stored offset to hexadecimal.

**Solution:**

```excel
=OCT2HEX(B2)
```

**Answer:** `FFFFFFFF00`. Octal 7777777400 is the 30-bit two's-complement form of -256, and the result has 10 characters.

## Use Cases

### Memory Address Translation

**Scenario:** A systems engineer converts octal addresses from an older memory map into hexadecimal, so they can be compared with a modern debugger.

```excel
=OCT2HEX(B2,8)
```

**Why It Works:** The eight-character width matches the address format the debugger displays, so the values sort and compare correctly.

### Legacy Register Display

**Scenario:** A dashboard shows device registers that the hardware manual documents in octal, but the operators read in hexadecimal.

```excel
=OCT2HEX(RegisterValue,4)
```

**Why It Works:** The fixed width keeps every register code the same length on screen, so the operators can scan the column quickly.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input contains a digit other than 0 to 7, such as 8 or 9. | Check the source data for typing errors. |
| `#NUM!` | The result needs more characters than `places` allows. | Increase `places` or leave it out. |
| `#NUM!` | `places` is negative. | Use a positive whole number for `places`. |
| `#VALUE!` | `places` is text in Excel. | Enter a number for `places`. |
| Unexpected result | A negative value shows 10 characters even though `places` was set. | This is expected for negative inputs. Set `places` only for positive values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Argument names are number and places. For negative numbers, `places` is ignored and the result has 10 characters. |
| Google Sheets | Available | Argument names are signed_octal_number and significant_digits. Positive values go up to 3777777777 (octal) and negative values down to 4000000000 (octal). The padding argument is ignored for negative values. |

## Tips and Best Practices

- Set `places` for every address or code that is displayed in a fixed-width field.
- Check input columns for digits 8 and 9 before converting, since those are the most common errors.
- Use OCT2BIN when the output must be shown as bits instead of hexadecimal digits.
- Keep the source values as text when leading zeros matter, so the spreadsheet does not drop them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2HEX](BIN2HEX.md) | Converts binary to hexadecimal. |
| [DEC2HEX](DEC2HEX.md) | Converts decimal to hexadecimal. |
| [HEX2DEC](HEX2DEC.md) | Converts hexadecimal to decimal. |
| [HEX2OCT](HEX2OCT.md) | Converts hexadecimal to octal, the reverse direction. |
| [OCT2BIN](OCT2BIN.md) | Converts octal to binary. |
| [OCT2DEC](OCT2DEC.md) | Converts octal to decimal. |

## Official Documentation

- [Microsoft Support: OCT2HEX function](https://support.microsoft.com/en-us/excel/functions/oct2hex-function)
- [Google Docs Editors Help: OCT2HEX](https://support.google.com/docs/answer/3093147)
