---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Investment Analysis
use-case:
  - Certificate Yield Comparison
  - Interest at Maturity Notes
  - Short-Term Corporate Paper
related:
  - ACCRINTM
  - PRICEMAT
  - YIELD
  - YIELDDISC
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/yieldmat-function
  - https://support.google.com/docs/answer/9000132
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Yield on Interest at Maturity
  - Maturity Interest Yield
tags:
  - bond-math
  - day-count-basis
  - excel
  - maturity-yield
  - sheets
---

# YIELDMAT

## Description

**YIELDMAT** returns the annual yield of a security that pays all of its interest at maturity instead of through periodic coupons. You supply the settlement date (when the buyer takes ownership), the maturity date, the issue date, the interest rate stated at issue, the price per 100 of face value, and an optional day count basis. YIELDMAT then calculates the annual return that the buyer earns between settlement and maturity.

Use it for short notes and certificates where the buyer receives principal plus interest in one payment. Because the function needs the issue date, it can compare securities issued at different times and bought at different prices.

## Syntax

```excel
=YIELDMAT(settlement, maturity, issue, rate, pr, [basis])
```

<!-- Image 1: Issue, Settlement and Maturity Inputs. See Images/Financial/YIELDMAT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The settlement date, which is the date the buyer takes ownership. It must fall before the maturity date. Enter it with DATE or as a cell reference. |
| `maturity` | Yes | The date the security expires and principal plus interest is paid. |
| `issue` | Yes | The date the security was first issued. |
| `rate` | Yes | The annual interest rate stated at issue, as a decimal such as 0.05 for 5 percent. Negative rates return an error. |
| `pr` | Yes | The price per 100 of face value, such as 100.50. Google Sheets names this argument `price`. |
| `basis` | No | The day count basis: `0` or omitted for US (NASD) 30/360, `1` for actual/actual, `2` for actual/360, `3` for actual/365, and `4` for European 30/360. |

### Return Value

The annual yield as a decimal, such as 0.0343, which displays as 3.43% when the cell is formatted as a percentage. When an argument is invalid, the function returns an error; see Common Errors.

## Examples

All examples use this note. The inputs sit in `B1:B6`, with labels in column A.

| Input | Cell | Value |
| --- | --- | --- |
| Settlement date | B1 | 2025-06-30 |
| Maturity date | B2 | 2026-06-30 |
| Issue date | B3 | 2025-01-31 |
| Interest rate | B4 | 0.04 |
| Price per 100 | B5 | 100.50 |
| Day count basis | B6 | 0 |

### Example 1: Yield at the Quoted Price

```excel
=YIELDMAT(B1, B2, B3, B4, B5, B6)
```

**Result:** `3.43%`

The note costs 100.50 for every 100 of face value, which is above par, so the yield is below the 4 percent interest rate.

### Example 2: Lower Price

```excel
=YIELDMAT(B1, B2, B3, B4, 98, B6)
```

**Result:** `6.02%`

Buying at 98 per 100 adds the discount to the interest, which raises the yield to about 6.02 percent.

<!-- Image 2: Issue to Maturity Timeline. See Images/Financial/YIELDMAT.md -->

### Example 3: Omitting the Basis

```excel
=YIELDMAT(B1, B2, B3, B4, B5)
```

**Result:** `3.43%`

When `basis` is omitted, YIELDMAT uses US (NASD) 30/360, the same result as Example 1.

### Example 4: Guarding Against Bad Dates

```excel
=IFERROR(YIELDMAT(B1, B2, B3, B4, B5, B6), "Check dates")
```

**Result:** `3.43%`

If one of the dates is typed as text, the cell shows `Check dates` instead of `#VALUE!`.

## Story Problems

### Problem 1: Interest at Maturity Note

A business buys a note on March 31, 2025 at 101.25 per 100 of face value. The note was issued on September 30, 2024, pays 5% interest at maturity, and matures on March 31, 2027.

| Input | Value |
| --- | --- |
| Settlement | 2025-03-31 |
| Maturity | 2027-03-31 |
| Issue | 2024-09-30 |
| Interest rate | 0.05 |
| Price | 101.25 |
| Basis | 0 |

**Task:** Find the annual yield the business earns on the note.

**Solution:**

```excel
=YIELDMAT(DATE(2025,3,31), DATE(2027,3,31), DATE(2024,9,30), 0.05, 101.25, 0)
```

**Answer:** `4.22%`. The premium paid above 100 reduces the yield below the 5 percent interest rate.

### Problem 2: Certificate Bought Mid-Term

A saver buys a certificate on October 15, 2025 at 100.30 per 100 of face value. The certificate was issued on April 15, 2025, pays 6% interest at maturity, and matures on April 15, 2026.

| Input | Value |
| --- | --- |
| Settlement | 2025-10-15 |
| Maturity | 2026-04-15 |
| Issue | 2025-04-15 |
| Interest rate | 0.06 |
| Price | 100.30 |
| Basis | 0 |

**Task:** Find the annual yield the saver earns from the purchase date to maturity.

**Solution:**

```excel
=YIELDMAT(DATE(2025,10,15), DATE(2026,4,15), DATE(2025,4,15), 0.06, 100.30, 0)
```

**Answer:** `5.23%`. The saver pays a small premium over 100 and receives 6 percent interest, so the yield lands below the interest rate.

<!-- Image 3: Results Panel for the Story Problems. See Images/Financial/YIELDMAT.md -->

## Use Cases

### Interest at Maturity Notes

**Scenario:** A treasury team compares notes that pay all interest at maturity, each bought at a different price.

```excel
=YIELDMAT(Settle, Maturity, Issue, Rate, Price, 0)
```

**Why It Works:** Each row carries its own issue date, rate and price, so the annual yields are computed from the same inputs and can be ranked directly.

### Certificate Yield Comparison

**Scenario:** A saver weighs a certificate bought today against one bought at issue, and needs the yield for each purchase date.

```excel
=YIELDMAT(PurchaseDate, MaturityDate, IssueDate, CertRate, OfferPrice)
```

**Why It Works:** Changing only the purchase date shows how buying later changes the yield, because the issue date and rate stay fixed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The rate is negative or the price is zero or negative. | Enter a rate of zero or more and a positive price. |
| `#NUM!` | The settlement date is on or after the maturity date. | Check the order of the two dates. |
| `#NUM!` | The basis is less than 0 or greater than 4. | Use a basis code from 0 to 4. |
| `#VALUE!` | The settlement, maturity or issue date is text or is not valid. | Enter dates with DATE or as date values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions, including Excel for the web | The `basis` argument is optional and defaults to 0. |
| Google Sheets | Available | Same argument order. The basis is named `day_count_convention` and uses the same codes 0 to 4. The help page does not list error conditions. |

## Tips and Best Practices

- Enter the issue date for every security, because the yield depends on the time since issue as well as the time to maturity.
- Keep the basis the same across a comparison, since a different basis changes the result.
- Use PRICEMAT to check a yield: pricing the note at that yield should return the original price.
- Use ACCRINTM when you need the dollar interest a security pays at maturity alongside the yield.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PRICEMAT](PRICEMAT.md) | Price per 100 of face value for a given yield on the same kind of security. |
| [ACCRINTM](ACCRINTM.md) | Accrued interest for a security that pays interest at maturity. |
| [YIELD](YIELD.md) | Annual yield for a security that pays periodic coupons. |
| [YIELDDISC](YIELDDISC.md) | Annual yield for a discount security that pays no interest. |

## Official Documentation

- [Microsoft Support: YIELDMAT function](https://support.microsoft.com/en-us/excel/functions/yieldmat-function)
- [Google Docs Editors Help: YIELDMAT](https://support.google.com/docs/answer/9000132)
