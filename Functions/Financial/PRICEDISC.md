---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Cash Management Planning
  - Discount Note Valuation
  - Treasury Bill Pricing
related:
  - DISC
  - PRICE
  - PRICEMAT
  - TBILLPRICE
  - YIELDDISC
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/pricedisc-function
  - https://support.google.com/docs/answer/3093240
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Discount Security Price
tags:
  - bond-pricing
  - discount-securities
  - excel
  - sheets
---

# PRICEDISC

## Description

**PRICEDISC** returns the price per $100 face value of a discount security, which is sold below its redemption value and repays the full face value at maturity. It pays no periodic interest. The buyer earns the difference between the purchase price and the face value, and the discount is earned over the days from settlement to maturity.

Enter the settlement date, the maturity date, the discount rate and the redemption value. The function returns the price, so a rate of 4.8% on a 90 day security produces a price that is 1.2% below the redemption value under the actual/360 basis.

Use PRICEDISC for securities such as short-term Treasury bills and commercial paper that are quoted by discount rate. For securities that pay interest at maturity, use PRICEMAT. For bonds with periodic coupons, use PRICE. To find the discount rate from a known price, use DISC.

## Syntax

```excel
=PRICEDISC(settlement, maturity, discount, redemption, [basis])
```

<!-- Image 1: Discount Security Timeline. See Images/Financial/PRICEDISC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the security. It must fall before the maturity date. |
| `maturity` | Yes | The date the security expires and the redemption value is paid. |
| `discount` | Yes | The annual discount rate of the security. It must be greater than 0. |
| `redemption` | Yes | The amount repaid at maturity per $100 of face value. It must be greater than 0. |
| `basis` | No | The day count basis: `0` or omitted for US (NASD) 30/360, `1` for actual/actual, `2` for actual/360, `3` for actual/365, or `4` for European 30/360. |

### Return Value

A number: the price per $100 face value. The function returns `#VALUE!` when the settlement or maturity is not a valid date. It returns `#NUM!` when the discount or redemption value is 0 or less, the basis is outside 0 to 4, or the settlement date is on or after the maturity date.

## Examples

### Example 1: Price a 90 Day Discount Security

```excel
=PRICEDISC(DATE(2026,1,10), DATE(2026,4,10), 4.8%, 100, 2)
```

**Result:** `98.80`

The security has 90 days to maturity. The discount is 4.8% of 100 multiplied by 90 divided by 360, which is 1.20 points.

### Example 2: Price Per 1,000 of Face Value

```excel
=PRICEDISC(DATE(2026,1,10), DATE(2026,4,10), 4.8%, 1000, 2)
```

**Result:** `988.00`

Changing the redemption value to 1,000 scales the price by the same ratio, so the discount is 12.00 per 1,000 of face value.

<!-- Image 2: Price Per 100 and Per 1,000. See Images/Financial/PRICEDISC.md -->

### Example 3: Wrap the Price in IFERROR

With the settlement date in `B2`, the maturity date in `B3` and the discount rate in `B4`:

```excel
=IFERROR(PRICEDISC(B2, B3, B4, 100, 2), "Check dates")
```

**Result:** `98.80`

If the settlement is on or after the maturity, the cell shows "Check dates" instead of an error code.

## Story Problems

### Problem 1: Buying a 91 Day Bill

A business buys a 91 day discount security for its cash reserves. It settles on May 4, 2026, matures on August 3, 2026, and carries a discount rate of 4.35%. The business wants to know the cost of 10,000 in face value.

| Term | Value |
| --- | --- |
| Settlement | 5/4/2026 |
| Maturity | 8/3/2026 |
| Discount | 4.35% |
| Face value | 10000 |

**Task:** Find the amount the business pays for 10,000 of face value, using actual/360 day counting.

**Solution:**

```excel
=PRICEDISC(B2, B3, B4, 100, 2) * B5 / 100
```

**Answer:** `9890.04`. The price per 100 is 98.90, and 10,000 of face value costs 9,890.04.

### Problem 2: A Discount Note With 30/360 Counting

A treasurer buys a discount note with 250,000 of face value. It settles on March 2, 2026, matures on June 30, 2026 and carries a discount rate of 3.90%. The note's terms use 30/360 day counting.

**Task:** Find the amount the treasurer pays for 250,000 of face value.

**Solution:**

```excel
=PRICEDISC(DATE(2026,3,2), DATE(2026,6,30), 3.9%, 100, 0) * 250000 / 100
```

**Answer:** `246804.17`. The price per 100 is 98.72, and the discount over 118 days of 30/360 time is 1.28 points.

<!-- Image 3: Story Problem Inputs and Output. See Images/Financial/PRICEDISC.md -->

## Use Cases

### Treasury Bill Pricing

**Scenario:** A cash manager compares the cost of several short Treasury bills before buying.

```excel
=PRICEDISC(SettlementDate, MaturityDate, BillDiscount, 100, 2) * FaceValue / 100
```

**Why It Works:** Each bill uses its own dates and discount rate, and multiplying by the face value gives the cash needed for the purchase.

### Cash Management Planning

**Scenario:** A business plans to receive face value from a discount note on a known date and wants the purchase cost now.

```excel
=PRICEDISC(TodayDate, MaturityDate, NoteDiscount, 100, 0) * FaceValue / 100
```

**Why It Works:** The formula gives the cash outlay today, which can be compared with the face value received at maturity.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The settlement date is on or after the maturity date. | Enter a settlement date earlier than maturity. |
| `#NUM!` | The discount or redemption value is 0 or less. | Enter a positive discount rate and redemption value. |
| `#NUM!` | The basis is outside 0 to 4. | Use `0`, `1`, `2`, `3` or `4`. |
| `#VALUE!` | A date argument is text instead of a date. | Enter dates with `DATE` or as true date values. |
| Price per 100 mistaken for total cost | The result is per 100 of face value, not the full face amount. | Multiply by the face value and divide by 100. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | The optional argument is named `basis`. |
| Google Sheets | Available | The optional argument is named `day_count_convention` and uses the same codes 0 to 4. |

## Tips and Best Practices

- Read the result as a price per 100 of face value, then scale it to the amount you hold.
- Use the day count basis of the security, because actual/360 and 30/360 give different prices for the same dates.
- Use `DATE` for every date so the function does not depend on regional date formats.
- Use DISC with a known price to recover the discount rate and confirm that the inputs are consistent.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DISC](DISC.md) | Returns the discount rate for a given price, the reverse of this function. |
| [TBILLPRICE](TBILLPRICE.md) | Prices a Treasury bill with its own argument layout. |
| [YIELDDISC](YIELDDISC.md) | Returns the yield of a discount security from its price. |
| [PRICEMAT](PRICEMAT.md) | Prices a security that pays interest at maturity. |
| [PRICE](PRICE.md) | Prices a bond that pays periodic coupons. |

## Official Documentation

- [Microsoft Support: PRICEDISC function](https://support.microsoft.com/en-us/excel/functions/pricedisc-function)
- [Google Docs Editors Help: PRICEDISC](https://support.google.com/docs/answer/3093240)
