---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Investment Analysis
use-case:
  - Discounted Note Payoff
  - Money Market Holdings
  - Short Term Investment Planning
related:
  - DISC
  - PRICEDISC
  - TBILLEQ
  - TBILLPRICE
  - YIELDDISC
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/received-function
  - https://support.google.com/docs/answer/3093244
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Amount Received at Maturity
  - Discounted Security Payoff
tags:
  - bonds
  - day-count
  - discount-security
  - excel
  - sheets
---

# RECEIVED

## Description

**RECEIVED** returns the amount you receive at maturity for a fully invested security that was bought at a discount. Discounted securities, such as some notes and money market instruments, pay their face value at maturity rather than paying interest along the way. The buyer pays less than face value on the settlement date and collects the full face value when the security matures. RECEIVED calculates that face value from the amount invested and the discount rate.

The calculation depends on the day count basis. Each basis defines how many days are in a year and how the days between settlement and maturity are counted. The default basis, 0, uses the US (NASD) 30/360 convention. Choose a different basis when the security's terms say so, because the result changes with the convention.

RECEIVED is related to the discount-security functions DISC, PRICEDISC and YIELDDISC, and to the Treasury bill functions TBILLPRICE, TBILLYIELD and TBILLEQ. Use RECEIVED when you know the amount invested and need the payout. Use PRICEDISC when you know the price and need the discount rate.

Enter settlement and maturity as real dates, using the DATE function or a cell that holds a date. Text that looks like a date can produce `#VALUE!` or the wrong result.

## Syntax

```excel
=RECEIVED(settlement, maturity, investment, discount, [basis])
```

<!-- Image 1: Syntax Anatomy. See Images/Financial/RECEIVED.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the security. Enter it as a date, not as text. Settlement and maturity are truncated to whole days. |
| `maturity` | Yes | The date the security expires and is redeemed at face value. Must fall after settlement. |
| `investment` | Yes | The amount paid for the security. Must be greater than 0. |
| `discount` | Yes | The discount rate of the security. Must be greater than 0. |
| `basis` | No | The day count basis. `0` or omitted is US (NASD) 30/360. `1` is actual/actual. `2` is actual/360. `3` is actual/365. `4` is European 30/360. Any value below 0 or above 4 returns `#NUM!`. |

### Return Value

A number: the amount received at maturity, which is larger than the amount invested. The function returns `#VALUE!` when settlement or maturity is not a valid date, and `#NUM!` when the investment or discount is 0 or less, the basis is outside 0 to 4, or settlement is not before maturity.

## Examples

All examples use a security bought on March 10, 2026 and maturing on September 10, 2026.

### Example 1: Actual/365 Basis

```excel
=RECEIVED(DATE(2026,3,10), DATE(2026,9,10), 500000, 0.048, 3)
```

**Result:** `512,398.64`

There are 184 days from settlement to maturity. With an actual/365 year, the function divides the 500,000 investment by 1 minus the discount rate times 184/365. The payout is above the amount invested because the buyer receives face value at maturity.

### Example 2: Actual/360 Basis

```excel
=RECEIVED(DATE(2026,3,10), DATE(2026,9,10), 500000, 0.048, 2)
```

**Result:** `512,575.18`

The same dates and rate on an actual/360 basis produce a slightly higher payout. A 360-day year makes each day a larger fraction of the year, so the discount is smaller and the payout is higher.

### Example 3: Default 30/360 Basis

```excel
=RECEIVED(DATE(2026,3,10), DATE(2026,9,10), 500000, 0.048)
```

**Result:** `512,295.08`

Omitting basis uses US (NASD) 30/360. Under that convention the period counts as 180 days, which gives a lower payout than the actual-day bases in Examples 1 and 2.

<!-- Image 2: Basis Comparison Table. See Images/Financial/RECEIVED.md -->

Store the dates, amount, rate and basis in separate cells when the same formula must work for many securities, and reference those cells instead of typing the values into the formula.

## Story Problems

### Problem 1: Discounted Note Payoff

A treasurer buys a 250,000 discounted note on January 5, 2026. The note matures on July 5, 2026 and carries a 5% discount rate. The treasurer uses an actual/360 basis, as the note's terms require.

| Item | Value |
| --- | --- |
| Settlement | January 5, 2026 |
| Maturity | July 5, 2026 |
| Investment | 250,000 |
| Discount rate | 5% |
| Basis | 2 (actual/360) |

**Task:** Find the amount the note pays at maturity.

**Solution:**

```excel
=RECEIVED(DATE(2026,1,5), DATE(2026,7,5), 250000, 0.05, 2)
```

**Answer:** `256,446.79`. There are 181 days between settlement and maturity, and the function divides 250,000 by 1 minus 0.05 times 181/360.

<!-- Image 3: Story Problem Result Panel. See Images/Financial/RECEIVED.md -->

### Problem 2: Short Note Held Through One Year

A fund buys an 80,000 discounted note on April 1, 2026 with a 3.6% discount rate. The note matures on April 1, 2027, and the fund's documents use an actual/365 basis.

| Item | Value |
| --- | --- |
| Settlement | April 1, 2026 |
| Maturity | April 1, 2027 |
| Investment | 80,000 |
| Discount rate | 3.6% |
| Basis | 3 (actual/365) |

**Task:** Find the amount the fund receives at maturity.

**Solution:**

```excel
=RECEIVED(DATE(2026,4,1), DATE(2027,4,1), 80000, 0.036, 3)
```

**Answer:** `82,987.55`. The period is 365 days, so the discount term is exactly 0.036, and 80,000 divided by 0.964 gives the payout.

## Use Cases

### Discounted Note Payoff

**Scenario:** A company buys a short-term discounted note and needs to forecast the cash it receives on the maturity date.

```excel
=RECEIVED(DATE(2026,1,5), DATE(2026,7,5), 250000, 0.05, 2)
```

**Why It Works:** The function applies the note's day count basis, so the forecast matches the cash the note pays. Using the wrong basis can change the payout by several hundred dollars on a quarter-million note.

### Money Market Holdings

**Scenario:** A treasury team holds a ladder of discounted securities and wants the maturity value of each one in a single column.

```excel
=RECEIVED(B2, C2, D2, E2, F2)
```

**Why It Works:** Each row carries its own dates, amount, rate and basis. Copying the formula down the column produces the maturity value for every holding, and a total can be added with SUM.

### Short Term Investment Planning

**Scenario:** A planner compares the maturity value of a discounted security with the cash needed on the maturity date.

```excel
=IF(RECEIVED(DATE(2026,4,1), DATE(2027,4,1), 80000, 0.036, 3) >= 82000, "Covers Payment", "Payment Not Covered")
```

**Why It Works:** The comparison runs on the payout, not the investment. The planner sees whether the maturity value covers the planned payment before the cash is committed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | Settlement or maturity is text, not a date. | Enter dates with DATE or reference cells formatted as dates. |
| `#NUM!` | Investment or discount is 0 or less. | Enter a positive investment and a positive discount rate. |
| `#NUM!` | Basis is below 0 or above 4. | Use a whole number from 0 to 4. |
| `#NUM!` | Settlement is on or after maturity. | Check that the maturity date falls after the settlement date. |
| Payout differs from the security's statement | The basis does not match the security's terms. | Compare the basis with the security's documents and change the basis argument. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel versions, including Microsoft 365 and Excel for the web | The fourth argument is named basis. Basis `0` is US (NASD) 30/360 and is the default. |
| Google Sheets | Available | The last argument is named day_count_convention. The codes 0 to 4 match Excel. Enter dates with DATE or another date-parsing function. |

## Tips and Best Practices

- Confirm the day count basis in the security's terms before you build the formula.
- Enter dates with DATE so the function never reads them as text.
- Keep the discount rate as a decimal, such as 0.048, or as a percentage cell.
- Use PRICEDISC or YIELDDISC when the price is known and you need the rate or yield instead of the payout.
- Test the formula with a small, known example before you apply it to a large holding.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DISC](DISC.md) | Calculates the discount rate of a security from its price. |
| [PRICEDISC](PRICEDISC.md) | Calculates the price of a discounted security from its discount rate. |
| [TBILLEQ](TBILLEQ.md) | Calculates the bond-equivalent yield of a Treasury bill. |
| [TBILLPRICE](TBILLPRICE.md) | Calculates the price per 100 of face value of a Treasury bill. |
| [YIELDDISC](YIELDDISC.md) | Calculates the annual yield of a discounted security from its price. |

## Official Documentation

- [Microsoft Support: RECEIVED function](https://support.microsoft.com/en-us/excel/functions/received-function)
- [Google Docs Editors Help: RECEIVED](https://support.google.com/docs/answer/3093244)
