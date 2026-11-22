---
domain: Spreadsheet Functions
category: Financial
subcategory: Depreciation
purpose:
  - Depreciation
use-case:
  - Fixed Asset Register Reviews
  - French Accounting Asset Ledgers
related:
  - AMORDEGRC
  - DB
  - DDB
  - SLN
  - SYD
  - VDB
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/amorlinc-function
  - https://support.google.com/docs/answer/9083932
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - French Linear Depreciation
  - Straight Line French Depreciation
tags:
  - depreciation
  - excel
  - french-accounting
  - sheets
---

# AMORLINC

## Description

**AMORLINC** returns the depreciation of an asset for one accounting period under the French accounting system. The method is linear: each full period carries the same charge, which is the cost multiplied by the depreciation rate. The function also takes a first period that often runs from a mid-year purchase date to a period end date, so the first charge can differ from the rest.

Use AMORLINC for asset ledgers that follow French rules and need a flat charge each year. For a charge that falls each year, use AMORDEGRC, which applies a degressive coefficient. For other methods, such as the standard straight line or declining balance charges, use SLN, DB or DDB.

Both Microsoft and Google describe AMORLINC as a function for the French accounting system. Microsoft's article states that the first period is prorated when an asset is bought in the middle of a period, but its own worked example returns the full annual charge. Check the first period against your asset records before you rely on it in a schedule.

## Syntax

```excel
=AMORLINC(cost, purchase_date, first_period_end, salvage, period, rate, [basis])
```

<!-- Image 1: Linear Depreciation Inputs. See Images/Financial/AMORLINC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `cost` | Yes | The purchase cost of the asset. |
| `purchase_date` | Yes | The date the asset was bought. Enter it with `DATE` or as a date value. |
| `first_period_end` | Yes | The date the first accounting period ends. |
| `salvage` | Yes | The value of the asset at the end of its life. |
| `period` | Yes | The period to calculate. `1` is the first period. Google Sheets requires a non-negative value, rounds fractions below 1 up to 1 and rounds fractions above 1 down. |
| `rate` | Yes | The annual depreciation rate, for example `0.1` for 10%. Enter it as a decimal. |
| `basis` | No | The year basis. `0` or omitted uses 360 days (NASD method). `1` uses actual days, `3` uses 365 days per year and `4` uses 360 days per year (European method). |

### Return Value

A number: the depreciation charge for the requested period, in the same currency unit as `cost`. The function returns `#VALUE!` when a date is not valid. Google's article does not list specific error conditions, and Microsoft's article does not list any either.

## Examples

All examples use an asset costing 8,000 that was bought on February 10, 2026, with a first period that ends on December 31, 2026, a salvage value of 500 and a rate of 0.1.

### Example 1: First Period Charge

```excel
=AMORLINC(8000,DATE(2026,2,10),DATE(2026,12,31),500,1,0.1,1)
```

**Result:** `800`

With a rate of 10% on a cost of 8,000, the annual charge is 800. This result is the full annual charge, not a partial charge for the months after the purchase, which is the point to verify against your asset records.

### Example 2: A Later Period Using a 360-Day Basis

```excel
=AMORLINC(15000,DATE(2026,4,1),DATE(2026,12,31),1500,2,0.12,0)
```

**Result:** `1800`

A cost of 15,000 at 12% gives a charge of 1,800 in each period, and the salvage value of 1,500 is not reached in this period.

### Example 3: Remaining Book Value

```excel
=8000-AMORLINC(8000,DATE(2026,2,10),DATE(2026,12,31),500,1,0.1,1)
```

**Result:** `7200`

Subtracting the first period charge from the cost gives the book value at the end of that period.

<!-- Image 2: Straight Line Schedule Over Periods. See Images/Financial/AMORLINC.md -->

### Example 4: Charge for the Second Period

```excel
=AMORLINC(4200,DATE(2026,3,1),DATE(2026,12,31),300,2,0.25,0)
```

**Result:** `1050`

A cost of 4,200 at 25% gives a flat charge of 1,050 per period. Because the charge does not change from period to period, the second period result matches the annual charge.

## Story Problems

### Problem 1: Printing Press Schedule

A printing company buys a laser engraver for 15,000 on April 1, 2026. The company expects a salvage value of 1,500 and depreciates the equipment at 12% a year under the French linear method. It uses a 360-day year, and the first period ends on December 31, 2026.

| Item | Value |
| --- | --- |
| Cost | 15000 |
| Purchase date | 2026-04-01 |
| First period end | 2026-12-31 |
| Salvage value | 1500 |
| Period | 3 |
| Rate | 0.12 |
| Basis | 0 |

**Task:** Calculate the depreciation charge for period 3.

**Solution:**

```excel
=AMORLINC(B2,B3,B4,B5,B6,B7,B8)
```

**Answer:** `1800`. A rate of 12% on a cost of 15,000 gives a flat charge of 1,800 for each period, and the book value stays above the salvage value in period 3.

### Problem 2: Office Scanners

An office buys a scanner for 4,200 on March 1, 2026. The salvage value is 300, and the rate is 25% a year. The first period ends on December 31, 2026, and the accountant uses the 360-day basis.

| Item | Value |
| --- | --- |
| Cost | 4200 |
| Purchase date | 2026-03-01 |
| First period end | 2026-12-31 |
| Salvage value | 300 |
| Period | 2 |
| Rate | 0.25 |
| Basis | 0 |

**Task:** Calculate the charge for period 2 and state whether it is the same as the annual charge.

**Solution:**

```excel
=AMORLINC(B2,B3,B4,B5,B6,B7,B8)
```

**Answer:** `1050`, which is the same as the annual charge of 25% of 4,200, because a linear schedule carries the same charge in each full period.

## Use Cases

### French Accounting Asset Ledgers

**Scenario:** A subsidiary in France maintains a ledger of equipment that uses the French linear method for each asset.

```excel
=AMORLINC(Cost,PurchaseDate,FirstPeriodEnd,Salvage,Period,Rate,Basis)
```

**Why It Works:** One row holds one asset, so the same formula can be copied down the ledger for each period. Confirm the first period result on a sample of assets before you post the schedule.

### Fixed Asset Register Reviews

**Scenario:** An internal auditor compares the register's depreciation charges with a recalculated schedule for a sample of assets.

```excel
=ROUND(AMORLINC(Cost,PurchaseDate,FirstPeriodEnd,Salvage,Period,Rate,0),2)
```

**Why It Works:** Rounding to cents matches the register's presentation, and a fixed basis keeps the review consistent across assets.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A date is stored as text. | Enter the dates with `DATE` or convert the text to date values. |
| `#NUM!` | `period` is negative. | Use a period of 0 or greater, as Google Sheets requires. |
| Same charge in every period | The linear method gives the same charge in each full period. | This is expected. Use AMORDEGRC for a schedule that falls each year. |
| Charge does not match the register | The first period was prorated differently from the register. | Compare the first period against a hand calculation and the register's policy. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365 and Excel for the web | Described as a French accounting system function. Uses the same argument order as Sheets. |
| Google Sheets | Available | The article states that the function is available only for users of the French accounting system. Same argument order. |

## Tips and Best Practices

- Enter the rate as a decimal, so `0.1` means 10% and not 10.
- Verify the first period result for each asset before you rely on the schedule, because the official article and its own example describe the first period differently.
- Keep the basis in one cell across the ledger so every row uses the same year basis.
- Use AMORLINC for flat charges and AMORDEGRC for degressive charges, and do not mix the two in one schedule.
- Round only in the final presentation cell.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AMORDEGRC](AMORDEGRC.md) | The degressive French method, with a charge that falls each period. |
| [DB](DB.md) | Fixed declining balance depreciation, the closest alternative in Google Sheets to a degressive method. |
| [DDB](DDB.md) | Double declining balance depreciation, a declining balance method with a faster early charge. |
| [SLN](SLN.md) | Straight line depreciation, which uses the same flat charge for every period. |
| [SYD](SYD.md) | Sum of years digits depreciation, a degressive method for a different schedule. |
| [VDB](VDB.md) | Variable declining balance depreciation over any period. |

## Official Documentation

- [Microsoft Support: AMORLINC function](https://support.microsoft.com/en-us/excel/functions/amorlinc-function)
- [Google Docs Editors Help: AMORLINC](https://support.google.com/docs/answer/9083932)
