---
domain: Spreadsheet Functions
category: Add-in & Automation
subcategory: Add-in Functions
purpose:
  - Unit Conversion
use-case:
  - Cross-Border Invoice Conversion
  - Euro Transition Ledgers
  - Legacy Currency Reports
related:
  - CONVERT
  - GOOGLEFINANCE
  - IFERROR
  - ROUND
  - VLOOKUP
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/euroconvert-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Currency Triangulation
  - Euro Conversion
tags:
  - add-in
  - currency
  - euro
  - excel
  - triangulation
---

# EUROCONVERT

## Description

**EUROCONVERT** converts an amount between the euro and the national currencies of the euro member states, or between two member currencies. It uses the official euro conversion rates, so each conversion is a fixed calculation rather than a market quote.

When both currencies are euro member currencies, such as French francs and Deutsche marks, EUROCONVERT goes through the euro as an intermediary. This step is called triangulation. The optional `triangulation_precision` argument controls how many significant digits the intermediate euro value keeps.

Use EUROCONVERT when a workbook holds figures in a former euro member currency and you need them in euros or in another member currency. The function needs Microsoft's Euro Currency Tools add-in. Without it, the formula returns `#NAME?`. It cannot be used in array formulas.

## Syntax

```excel
=EUROCONVERT(number, source, target, [full_precision], [triangulation_precision])
```

<!-- Image 1: Add-in Activation Steps. See Images/Add-in & Automation/EUROCONVERT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The amount to convert, or a cell that holds it. |
| `source` | Yes | The three-letter code of the currency the amount is in, as text or a cell reference. Accepted codes: BEF, LUF, DEM, ESP, FRF, IEP, ITL, NLG, ATS, PTE, FIM, GRD, SIT and EUR. |
| `target` | Yes | The three-letter code of the currency to convert to, from the same list. |
| `full_precision` | No | `TRUE` shows all significant digits from the calculation. `FALSE` applies each currency's rounding rules. The default is `FALSE`. |
| `triangulation_precision` | No | An integer of 3 or greater that sets the significant digits of the intermediate euro value in a conversion between two member currencies. When it is omitted, Excel does not round the intermediate value. |

Microsoft's parameter table marks the last two arguments as required, but its text gives defaults for both, so they are optional here.

### Return Value

The converted number, without a number format, so format the result cell yourself. When `source` and `target` are the same code, the function returns the original number. An invalid argument returns `#VALUE!`. Microsoft's rounding rules by currency group are:

| Currencies | Calculation Decimals | Display Decimals |
| --- | --- | --- |
| BEF, LUF, ESP, ITL | 0 | 0 |
| PTE, GRD | 0 | 2 |
| DEM, FRF, IEP, NLG, ATS, FIM, SIT, EUR | 2 | 2 |

## Examples

### Example 1: Deutsche Marks to Euros

In `A2`, `B2` and `C2`, enter `500`, `DEM` and `EUR`.

```excel
=EUROCONVERT(A2, B2, C2)
```

**Result:** `255.65`

One euro equals 1.95583 Deutsche marks, so 500 marks is 255.65 euros when rounded to the two decimal places that both currencies use.

### Example 2: French Francs to Euros With Default Precision

```excel
=EUROCONVERT(1200, "FRF", "EUR")
```

**Result:** `182.94`

One euro equals 6.55957 French francs, so 1200 francs is 182.94 euros at two decimals.

### Example 3: Euros to a Member Currency

```excel
=EUROCONVERT(100, "EUR", "DEM")
```

**Result:** `195.58`

100 euros is 195.583 marks, which rounds to 195.58 at two decimals.

### Example 4: Triangulation Between Member Currencies

```excel
=EUROCONVERT(800, "FRF", "DEM", TRUE, 3)
```

**Result:** `238.61126`

800 francs is about 121.96 euros. Keeping three significant digits makes the intermediate value 122 euros, and 122 euros at 1.95583 marks per euro is 238.61126 marks.

<!-- Image 2: Triangulation Worksheet. See Images/Add-in & Automation/EUROCONVERT.md -->

## Story Problems

### Problem 1: Converting a Legacy Payroll

A small firm paid three staff in Deutsche marks. The payroll sheet lists each monthly amount in column B, and the team wants each amount in euros in column C. The data sits in `A1:B4`.

| Employee | Monthly Pay (DEM) |
| --- | --- |
| Ayla | 2400 |
| Ben | 3150 |
| Chen | 875.50 |

**Task:** Convert each amount to euros and total the three results. EUROCONVERT cannot run in an array formula, so write the conversion in each row.

**Solution:**

Enter this in `C2`, then fill it down to `C4`:

```excel
=EUROCONVERT(B2, "DEM", "EUR")
```

Total the column in `C5`:

```excel
=SUM(C2:C4)
```

**Answer:** `3285.31`. The three euro amounts are 1227.10, 1610.57 and 447.64.

<!-- Image 3: Results Panel for the Story Problems. See Images/Add-in & Automation/EUROCONVERT.md -->

### Problem 2: Triangulating an Invoice

A buyer in Germany receives an invoice in French francs and needs the amount in Deutsche marks. The buyer's accounting rules keep the intermediate euro value to three significant digits and show all digits in the result. The invoice sits in `A1:C2`.

| Invoice | Amount | Currency |
| --- | --- | --- |
| INV-017 | 800 | FRF |

**Task:** Convert the amount in `B2` to Deutsche marks using full precision and a triangulation precision of 3.

**Solution:**

```excel
=EUROCONVERT(B2, C2, "DEM", TRUE, 3)
```

**Answer:** `238.61126` marks, the same result as Example 4.

## Use Cases

### Cross-Border Invoice Conversion

**Scenario:** A purchasing team holds supplier invoices in several euro member currencies and reports every line in euros.

```excel
=EUROCONVERT(B2, C2, "EUR")
```

**Why It Works:** Each row holds its own amount and currency code, so one formula fills down the column. Because EUROCONVERT cannot run in an array formula, avoid passing whole ranges. The cell format sets the displayed decimals.

### Euro Transition Ledgers

**Scenario:** A finance team restates ledger entries kept in Italian lira as euros for a consolidated report.

```excel
=EUROCONVERT(D2, "ITL", "EUR", TRUE)
```

**Why It Works:** Microsoft's rounding rules give lira amounts zero decimals in the calculation. Setting `full_precision` to `TRUE` keeps all significant digits from the calculation, so the total is not rounded row by row before it is summed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The Euro Currency Tools add-in is not loaded. | Open File > Options > Add-Ins, choose Excel Add-ins in the Manage list, click Go, and select Euro Currency Tools. |
| `#VALUE!` | A currency code is not on the accepted list, the triangulation precision is below 3, or a range was passed in an array formula. | Use an accepted code, an integer of 3 or more, and one cell per row. |
| Total differs from a manual calculation | Currency rounding removed decimals before the values were summed. | Set `full_precision` to `TRUE` when the report must keep all digits. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed for Excel for Microsoft 365, Excel 2024, Excel 2021, Excel 2019, Excel 2016 and Excel on mobile devices. | Requires the Euro Currency Tools add-in. Cannot be used in array formulas. |
| Google Sheets | Not available | The closest alternative is [GOOGLEFINANCE](../Google-specific/GOOGLEFINANCE.md) for live exchange rates, or a rate cell that the formula multiplies by. |

## Tips and Best Practices

- Load the Euro Currency Tools add-in on every computer that opens the workbook, or the formulas show `#NAME?`.
- Keep currency codes in their own column so each row names its currency.
- Fill the formula down one row at a time rather than passing ranges.
- Format the result cell, because the function does not apply a number format.
- Use `TRUE` for `full_precision` only when a report needs unrounded values.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CONVERT](../Engineering/CONVERT.md) | Converts units of measure. It does not convert currencies. |
| [GOOGLEFINANCE](../Google-specific/GOOGLEFINANCE.md) | Looks up live exchange rates in Google Sheets. |
| [IFERROR](../Logical/IFERROR.md) | Shows a fallback when the add-in is missing or a code is wrong. |
| [ROUND](../Math%20%26%20Trig/ROUND.md) | Rounds a converted value to a set number of decimals. |
| [VLOOKUP](../Lookup%20%26%20Reference/VLOOKUP.md) | Pulls a rate from a rate table kept on the sheet. |

## Official Documentation

- [Microsoft Support: EUROCONVERT function](https://support.microsoft.com/en-us/excel/functions/euroconvert-function)
