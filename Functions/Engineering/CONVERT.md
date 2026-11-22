---
domain: Spreadsheet Functions
category: Engineering
subcategory: Comparison and Conversion
purpose:
  - Unit Conversion
use-case:
  - Freight Weight Conversion
  - Shelving Length Conversion
related:
  - IFERROR
  - ROUND
  - VLOOKUP
  - XLOOKUP
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/convert-function
  - https://support.google.com/docs/answer/6055540
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Measurement Conversion
  - Unit Conversion
tags:
  - conversion
  - engineering
  - excel
  - sheets
  - units
---

# CONVERT

## Description

**CONVERT** changes a number from one unit of measure to another, such as pounds to kilograms or feet to inches. You name the starting unit and the target unit with text codes, and CONVERT applies the exact conversion factor. It works for weight, distance, time, pressure, force, energy, power, magnetism, temperature, volume, area, information and speed.

Both units must belong to the same category. Converting feet to seconds returns `#N/A` because distance and time do not convert into each other. Unit codes are case-sensitive, so type them exactly as the help page lists them. Metric prefixes such as `k` for kilo or `c` for centi can be added to metric unit codes, for example `"kg"` for kilograms.

Use CONVERT when the unit codes are fixed and known, and use a lookup table of factors when the business keeps its own conversion rates. CONVERT does not round its output, so wrap it in ROUND when a report needs fixed decimal places.

## Syntax

```excel
=CONVERT(number, from_unit, to_unit)
```

<!-- Image 1: Unit Code Pattern. See Images/Engineering/CONVERT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The numeric value to convert, expressed in `from_unit`. Non-numeric input returns `#VALUE!`. |
| `from_unit` | Yes | The text code for the unit of `number`, in quotation marks, such as `"lbm"`. |
| `to_unit` | Yes | The text code for the unit of the result, in quotation marks, such as `"kg"`. |

### Return Value

A numeric value expressed in `to_unit`. The function returns `#N/A` when a unit code does not exist, when the two units belong to different categories, or when a binary prefix is used with a unit that does not support it. It returns `#VALUE!` when `number` is not numeric.

## Examples

### Example 1: Pounds Mass to Kilograms

```excel
=CONVERT(1,"lbm","kg")
```

**Result:** `0.4535924`

One pound mass is exactly 0.45359237 kilograms, shown here to seven significant digits.

### Example 2: Fahrenheit to Celsius

```excel
=CONVERT(68,"F","C")
```

**Result:** `20`

Temperature codes use the same function. 68 degrees Fahrenheit is 20 degrees Celsius.

### Example 3: Feet to Inches

```excel
=CONVERT(1,"ft","in")
```

**Result:** `12`

One foot is 12 inches, so the factor between the two codes is exact.

### Example 4: Units From Different Categories

```excel
=CONVERT(2.5,"ft","sec")
```

**Result:** `#N/A`

Distance and time belong to different categories, so the function returns `#N/A`. Check the category of both codes before you convert.

## Story Problems

### Problem 1: Freight Weights in Pounds

A logistics clerk receives pallet weights in pounds mass (`lbm`) from a supplier. The customs form needs each weight in kilograms, rounded to two decimal places.

| Pallet | Weight (lbm) |
| --- | --- |
| P-1001 | 1200 |
| P-1002 | 845.5 |
| P-1003 | 2310 |

**Task:** Convert each weight in column B to kilograms, rounded to two decimal places, starting at row 2.

**Solution:**

```excel
=ROUND(CONVERT(B2,"lbm","kg"),2)
```

Enter this in C2 and fill it down to C4.

**Answer:** `544.31`, `383.51`, and `1047.8`. The last value is 1047.80 when formatted with two decimal places.

### Problem 2: Shelving Lengths in Inches

A furniture store cuts shelves from lengths recorded in feet. The cutting list needs the same lengths in inches, so the operator can read them on the tape measure.

| Shelf | Length (ft) |
| --- | --- |
| Shelf A | 4.5 |
| Shelf B | 7.25 |
| Shelf C | 10 |

**Task:** Convert each length in column B to inches, starting at row 2.

**Solution:**

```excel
=CONVERT(B2,"ft","in")
```

Enter this in C2 and fill it down to C4.

**Answer:** `54`, `87`, and `120` inches. A foot is 12 inches, so each length is multiplied by 12.

<!-- Image 2: Freight Weight Conversion Table. See Images/Engineering/CONVERT.md -->

## Use Cases

### Freight Weight Conversion

**Scenario:** A shipping report converts pallet weights from pounds to kilograms for every row in a carrier export.

```excel
=ROUND(CONVERT(Pallets[Weight_lbm],"lbm","kg"),2)
```

**Why It Works:** CONVERT applies the factor to each row, and ROUND fixes the display. Check that the source column holds pounds mass, not pounds-force, since those are separate codes.

### Shelving Length Conversion

**Scenario:** A cutting list needs shelf lengths in inches, while the design drawings use feet.

```excel
=CONVERT(B2,"ft","in")
```

**Why It Works:** The formula keeps the original value and returns the converted length, so the drawing and the cutting list can both reference the same source cell.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | A unit code does not exist, or the two codes belong to different categories. | Check the code list and confirm both units measure the same quantity. |
| `#N/A` | A binary prefix is used with a unit that does not support it. | Use a binary prefix only with information units such as `"byte"`. |
| `#VALUE!` | The `number` argument is text that cannot be read as a number. | Clean the source cell or convert it with `VALUE`. |
| Rounding looks wrong | CONVERT returns full precision, and the cell shows more digits than expected. | Wrap the function in ROUND or apply a number format. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 and Excel for the web | Full unit-code table, metric prefixes, and binary prefixes. |
| Google Sheets | Available | Uses the same three arguments. The help page lists the unit codes by category and shows examples, but it does not describe the prefix rules in detail. |

## Tips and Best Practices

- Store the unit codes in a labeled cell and reference it, so a change of unit needs one edit instead of many formulas.
- Use the exact code from the help page, because a near match such as `"kilogram"` is not a valid code.
- Use IFERROR around CONVERT when a mixed column may contain a wrong category, and show a clear message instead of `#N/A`.
- Keep the original value next to the converted value so the conversion can be audited.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IFERROR](../Logical/IFERROR.md) | Replaces `#N/A` from a bad unit code with a readable message. |
| [ROUND](../Math%20%26%20Trig/ROUND.md) | Fixes the number of decimal places in the converted result. |
| [VLOOKUP](../Lookup%20%26%20Reference/VLOOKUP.md) | Finds a conversion factor in a business table when the units are not in CONVERT. |
| [XLOOKUP](../Lookup%20%26%20Reference/XLOOKUP.md) | Returns the matching factor from a table with the same purpose as VLOOKUP. |

## Official Documentation

- [Microsoft Support: CONVERT function](https://support.microsoft.com/en-us/excel/functions/convert-function)
- [Google Docs Editors Help: CONVERT](https://support.google.com/docs/answer/6055540)
