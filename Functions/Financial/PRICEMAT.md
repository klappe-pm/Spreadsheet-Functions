---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Investment Portfolio Valuation
  - Money Market Investment
  - Short Term Note Pricing
related:
  - ACCRINTM
  - DISC
  - PRICE
  - PRICEDISC
  - YIELDMAT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/pricemat-function
  - https://support.google.com/docs/answer/3093191
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Price at Maturity Bond
tags:
  - bond-pricing
  - excel
  - sheets
---

# PRICEMAT

## Description

**PRICEMAT** returns the price per $100 face value of a security that pays its interest in one payment at maturity, rather than through periodic coupons. Short-term notes and bills of this type are often issued with a single interest payment, and the buyer receives the principal plus all accumulated interest on the maturity date.

Enter the settlement date, the maturity date, the issue date, the interest rate and the yield. The function returns the price that makes the expected yield equal the required return. The result is a clean price, with the interest accrued from the issue date to settlement removed.

Use PRICEMAT when the security has one payment at maturity. For bonds with periodic coupons, use PRICE. For discount securities that are sold below face value and pay face value at maturity, use PRICEDISC. To find the yield from a known price, use YIELDMAT.

## Syntax

```excel
=PRICEMAT(settlement, maturity, issue, rate, yld, [basis])
```

<!-- Image 1: Issue, Settlement and Maturity Dates. See Images/Financial/PRICEMAT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the security. It must fall after the issue date and before maturity. |
| `maturity` | Yes | The date the security expires and the interest and principal are paid. |
| `issue` | Yes | The date the security was issued. |
| `rate` | Yes | The annual interest rate on the issue date. It cannot be negative. |
| `yld` | Yes | The annual yield the buyer requires. It cannot be negative. |
| `basis` | No | The day count basis: `0` or omitted for US (NASD) 30/360, `1` for actual/actual, `2` for actual/360, `3` for actual/365, or `4` for European 30/360. |

### Return Value

A number: the price per $100 face value. The function returns `#VALUE!` when the settlement, maturity or issue is not a valid date. It returns `#NUM!` when the rate or yield is negative, the basis is outside 0 to 4, or the settlement date is on or after the maturity date.

## Examples

### Example 1: Price a Note With Interest at Maturity

```excel
=PRICEMAT(DATE(2026,2,1), DATE(2026,8,1), DATE(2025,11,1), 6%, 5.5%, 2)
```

**Result:** `100.20`

The 5.5% yield is below the 6% interest rate, so the price is above par. The buyer receives 6% interest on the face value at maturity.

### Example 2: Yield Above the Interest Rate

```excel
=PRICEMAT(DATE(2026,2,1), DATE(2026,8,1), DATE(2025,11,1), 6%, 6.5%, 2)
```

**Result:** `99.71`

With a 6.5% yield, the same note sells below par because the buyer requires more than the interest the note pays.

<!-- Image 2: Premium and Discount Results. See Images/Financial/PRICEMAT.md -->

### Example 3: Wrap the Price in IFERROR

With the terms in `B2:B6`, where `B2` is settlement, `B3` is maturity, `B4` is issue, `B5` is the rate and `B6` is the yield:

```excel
=IFERROR(PRICEMAT(B2, B3, B4, B5, B6, 2), "Check dates")
```

**Result:** `100.20` when `B6` holds 5.5%.

If the dates are out of order, the cell shows "Check dates" instead of an error code.

## Story Problems

### Problem 1: Pricing a Short Note for a Cash Fund

A cash management fund considers a note issued on January 15, 2026 that pays 5.5% interest at maturity on January 15, 2027. The fund settles on April 15, 2026 and requires a yield of 5.0%.

| Term | Value |
| --- | --- |
| Settlement | 4/15/2026 |
| Maturity | 1/15/2027 |
| Issue | 1/15/2026 |
| Rate | 5.50% |
| Yield | 5.00% |
| Basis | 0 |

**Task:** Find the price per $100 face value the fund should pay.

**Solution:**

```excel
=PRICEMAT(B2, B3, B4, B5, B6, B7)
```

**Answer:** `100.31`, rounded to the cent. The interest rate is higher than the required yield, so the note sells above par.

### Problem 2: Pricing a Note Bought Mid Term

A treasurer buys a second note issued on February 1, 2026 and maturing on December 1, 2026. The note pays 4.8% at maturity. The treasurer settles on June 1, 2026 and requires a yield of 5.2%, using 30/360 day counting.

**Task:** Find the price per $100 face value the treasurer should pay.

**Solution:**

```excel
=PRICEMAT(DATE(2026,6,1), DATE(2026,12,1), DATE(2026,2,1), 4.8%, 5.2%, 0)
```

**Answer:** `99.76`, rounded to the cent. The required yield is above the interest rate, so the note sells below par.

<!-- Image 3: Story Problem Inputs and Output. See Images/Financial/PRICEMAT.md -->

## Use Cases

### Short Term Note Pricing

**Scenario:** A corporate treasury team prices short notes that pay interest and principal together at maturity.

```excel
=PRICEMAT(SettlementDate, MaturityDate, IssueDate, NoteRate, RequiredYield, 2)
```

**Why It Works:** The function uses the issue date to account for interest already earned before settlement, so the price reflects the accrued amount.

### Money Market Investment

**Scenario:** A fund manager compares several short instruments that all pay interest at maturity.

```excel
=PRICEMAT(SettlementDate, MaturityDate, IssueDate, NoteRate, MarketYield, 3)
```

**Why It Works:** Using the same basis for every instrument keeps the comparison consistent. Changing only the rate or yield shows which instrument offers the better price.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The settlement date is on or after the maturity date. | Enter a settlement date earlier than maturity. |
| `#NUM!` | The rate or yield is negative. | Enter both as zero or positive decimals. |
| `#NUM!` | The basis is outside 0 to 4. | Use `0`, `1`, `2`, `3` or `4`. |
| `#VALUE!` | A date argument is text instead of a date. | Enter dates with `DATE` or as true date values. |
| Price looks too low | The rate was entered as `6` instead of `6%`. | Enter the rate as a percentage or a decimal such as `0.06`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | The optional argument is named `basis`. |
| Google Sheets | Available | The optional argument is named `day_count_convention` and uses the same codes 0 to 4. |

## Tips and Best Practices

- Use the issue date from the note's documents, because interest accrues from issue, not from the previous coupon.
- Use the same basis as the note's terms so the day counts and the price match the documents.
- Use `DATE` for every date so the function does not depend on regional date formats.
- Use YIELDMAT with the price from this function to confirm that the yield you entered is recovered.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PRICE](PRICE.md) | Prices a bond that pays periodic coupons. |
| [PRICEDISC](PRICEDISC.md) | Prices a discount security that pays face value at maturity. |
| [YIELDMAT](YIELDMAT.md) | Returns the yield for a security that pays interest at maturity, the reverse of this function. |
| [ACCRINTM](ACCRINTM.md) | Calculates the interest a security pays at maturity. |
| [DISC](DISC.md) | Returns the discount rate for a discount security. |

## Official Documentation

- [Microsoft Support: PRICEMAT function](https://support.microsoft.com/en-us/excel/functions/pricemat-function)
- [Google Docs Editors Help: PRICEMAT](https://support.google.com/docs/answer/3093191)
