---
domain: Spreadsheet Functions
category: Financial
subcategory: Depreciation
purpose:
  - Depreciation
use-case:
  - Equipment Depreciation Schedules
  - Fixed Asset Register Reviews
related:
  - AMORLINC
  - DB
  - DDB
  - SLN
  - SYD
  - VDB
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/amordegrc-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Degressive Asset Depreciation
  - French Degressive Depreciation
tags:
  - asset-life
  - degressive
  - depreciation
  - excel
---

# AMORDEGRC

## Description

**AMORDEGRC** returns the depreciation of an asset for one accounting period, using a degressive method. Under this method an asset loses more value in its early years and less later on. The function follows the French accounting system. It sets a depreciation rate from the asset's life, then applies that rate to the remaining book value each period.

The function works out the asset life as 1 divided by `rate`, then picks a coefficient for that life. The coefficient is 1.5 for a life of 3 to 4 years, 2 for 5 to 6 years, and 2.5 for more than 6 years. The depreciation rate is the coefficient times `rate`. Microsoft states that the rate rises to 50% for the period before the last one and to 100% for the final period, and that depreciation stops once cumulative depreciation reaches the cost less the salvage value.

Microsoft states that this function is deprecated and should no longer be used. It remains in Excel only so older workbooks keep calculating. For a new schedule, choose a method that your accounting policy allows, such as DB, DDB or VDB. Google Sheets does not offer AMORDEGRC.

## Syntax

```excel
=AMORDEGRC(cost, date_purchased, first_period, salvage, period, rate, [basis])
```

<!-- Image 1: Degressive Depreciation Inputs. See Images/Financial/AMORDEGRC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `cost` | Yes | The purchase cost of the asset. |
| `date_purchased` | Yes | The date the asset was bought. Enter it with `DATE` or as a date value. |
| `first_period` | Yes | The date the first accounting period ends. |
| `salvage` | Yes | The value of the asset at the end of its life. |
| `period` | Yes | The period to calculate. `1` is the first period, which starts at the purchase date. |
| `rate` | Yes | The depreciation rate before the coefficient is applied, for example `0.3`. The asset life is `1 / rate`, so the rate must lead to a life the function accepts. |
| `basis` | No | The year basis. `0` or omitted uses 360 days (NASD method). `1` uses actual days, `3` uses 365 days per year and `4` uses 360 days per year (European method). The Microsoft article does not list basis `2`. |

### Return Value

A number: the depreciation charge for the requested period, in the same currency unit as `cost`. The function returns `#NUM!` when the asset life falls between 0 and 1 years, 1 and 2 years, 2 and 3 years, or 4 and 5 years, and `#VALUE!` when a date is not valid.

## Examples

All examples use an asset costing 8,000 that was bought on February 10, 2026, with a first period that ends on December 31, 2026, a salvage value of 500 and a rate of 0.3 (an asset life of 3.33 years).

### Example 1: First Period Depreciation on Actual Days

```excel
=AMORDEGRC(8000,DATE(2026,2,10),DATE(2026,12,31),500,1,0.3,1)
```

**Result:** `2162`

The 3.33-year life gives a coefficient of 1.5, so the rate applied is 0.45. The first period covers the time from the purchase date to the period end, counted on an actual basis.

### Example 2: The Same Asset on a 360-Day Basis

```excel
=AMORDEGRC(8000,DATE(2026,2,10),DATE(2026,12,31),500,1,0.3,0)
```

**Result:** `2156`

Changing only the basis from 1 to 0 gives a slightly smaller first charge, because the 360-day year treats the same period differently.

<!-- Image 2: Basis Effect on the First Period. See Images/Financial/AMORDEGRC.md -->

### Example 3: Remaining Book Value

```excel
=8000-AMORDEGRC(8000,DATE(2026,2,10),DATE(2026,12,31),500,1,0.3,1)
```

**Result:** `5838`

Subtracting the first period charge from the cost gives the book value at the end of the first period.

### Example 4: Checking the Asset Life First

```excel
=1/0.3
```

**Result:** `3.3333`

The asset life of 3.33 years sits inside the 3 to 4 year band, so the coefficient is 1.5. If the life fell between 4 and 5 years, the function would return `#NUM!` instead of a value, so check the life before you build a long schedule.

## Story Problems

### Problem 1: Printing Equipment Purchased in July

A print shop buys a large press for 12,000 on July 1, 2026. The accountant expects a salvage value of 1,000 and uses a rate of 0.18 (a life of about 5.56 years). The shop's year ends on December 31, and the accountant uses actual days.

| Item | Value |
| --- | --- |
| Cost | 12000 |
| Purchase date | 2026-07-01 |
| First period end | 2026-12-31 |
| Salvage value | 1000 |
| Period | 1 |
| Rate | 0.18 |
| Basis | 1 |

**Task:** Calculate the depreciation for the first period.

**Solution:**

```excel
=AMORDEGRC(B2,B3,B4,B5,B6,B7,B8)
```

**Answer:** `3540`. The 5.56-year life falls in the 5 to 6 year band, so the coefficient is 2 and the depreciation rate is 0.36.

### Problem 2: Delivery Van Bought in May

A courier buys a van for 6,400 on May 15, 2026. The salvage value is 400, and the rate is 0.28 (a life of about 3.57 years). The first period ends on December 31, 2026, and the company uses actual days.

| Item | Value |
| --- | --- |
| Cost | 6400 |
| Purchase date | 2026-05-15 |
| First period end | 2026-12-31 |
| Salvage value | 400 |
| Period | 1 |
| Rate | 0.28 |
| Basis | 1 |

**Task:** Calculate the first period depreciation to the nearest whole currency unit.

**Solution:**

```excel
=ROUND(AMORDEGRC(B2,B3,B4,B5,B6,B7,B8),0)
```

**Answer:** `1977`, because the 3.57-year life falls in the 3 to 4 year band, giving a coefficient of 1.5 and a rate of 0.42.

## Use Cases

### Equipment Depreciation Schedules

**Scenario:** A manufacturer maintains an older workbook that depreciates machines with the French degressive method.

```excel
=AMORDEGRC(Cost,PurchaseDate,FirstPeriodEnd,Salvage,Period,Rate,1)
```

**Why It Works:** Named ranges keep each machine's inputs in one row, so the same formula can be copied down the register. Because the function is deprecated, plan a separate review of the method for new machines.

### Fixed Asset Register Reviews

**Scenario:** An auditor checks the first period charge on a sample of assets in a French subsidiary's register.

```excel
=ROUND(AMORDEGRC(Cost,PurchaseDate,FirstPeriodEnd,Salvage,1,Rate,Basis),0)
```

**Why It Works:** Rounding to whole units matches the register's presentation. Recalculate a sample of rows by hand before accepting the register as correct.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The asset life, 1 divided by `rate`, falls between 0 and 1, 1 and 2, 2 and 3, or 4 and 5 years. | Change the rate so the life lands in an accepted range, or use a different method. |
| `#VALUE!` | A date is stored as text. | Enter the dates with `DATE` or convert the text to date values. |
| `#NAME?` in Google Sheets | The function is not available in Sheets. | Use DB or DDB in Sheets, or calculate the schedule in Excel. |
| `#NUM!` | The rate was entered as a whole number such as `30` instead of `0.3`, which makes the asset life less than 1 year. | Enter the rate as a decimal. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365 and Excel for the web | Deprecated. Kept for compatibility with older workbooks. |
| Google Sheets | Not available | Use DB or DDB for declining balance depreciation, or VDB for a variable declining balance. |

## Tips and Best Practices

- Check the asset life, 1 divided by `rate`, before you build a schedule, because several ranges return `#NUM!`.
- Enter every date with `DATE` so the first period uses the correct number of days.
- Keep the basis in one cell in the register so every row uses the same year basis.
- Use AMORDEGRC only in workbooks that already rely on it, and choose a current method for new assets.
- Compare the first period result with a hand calculation for one asset before you trust the whole register.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AMORLINC](AMORLINC.md) | The linear version of the French depreciation method, with a flat charge for each period. |
| [DB](DB.md) | Fixed declining balance depreciation, the closest alternative in Google Sheets. |
| [DDB](DDB.md) | Double declining balance depreciation, a declining balance method with a faster early charge. |
| [SLN](SLN.md) | Straight line depreciation, which gives an even charge each year. |
| [SYD](SYD.md) | Sum of years digits depreciation, a degressive method that does not use the French coefficients. |
| [VDB](VDB.md) | Variable declining balance depreciation over any period. |

## Official Documentation

- [Microsoft Support: AMORDEGRC function](https://support.microsoft.com/en-us/excel/functions/amordegrc-function)
