---
domain: Spreadsheet Functions
category: Logical
subcategory: Lambda Helpers
purpose:
  - Array Shaping
  - Financial Modeling
use-case:
  - Custom Discount Formula
  - Reusable Tax Calculation
  - Rounded Price Rule
related:
  - BYCOL
  - BYROW
  - LET
  - MAKEARRAY
  - MAP
  - REDUCE
  - SCAN
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/lambda-function
  - https://support.google.com/docs/answer/12508718
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Custom Function
  - Reusable Formula
tags:
  - custom-functions
  - excel
  - lambda
  - reusable-formulas
  - sheets
---

# LAMBDA

## Description

**LAMBDA** packages a calculation with a list of parameters and returns a function. Calling that function with values runs the calculation. This lets you write a rule once and reuse it, either inline in a single formula or as a named function that any cell can call by name.

LAMBDA is also the tool that the array helpers need. MAP, REDUCE, SCAN, MAKEARRAY, BYROW and BYCOL each take a LAMBDA that describes what to do with each item. A LAMBDA on its own is not a value, so it must be called, saved under a name, or passed to a helper function.

LAMBDA is an advanced function. For a calculation used once, a plain formula is easier to audit. Reach for LAMBDA when the same rule appears in many formulas or when you need a helper such as MAP that expects a function.

## Syntax

```excel
=LAMBDA([parameter1, parameter2, ...,] calculation)
```

```text
Google Sheets: LAMBDA(name1, [name2, ...,] formula_expression)
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/LAMBDA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `parameter1`, `parameter2` | No | Names for the values passed when the function is called. Microsoft Excel allows up to 253 parameters. Each name must be a valid identifier, not a cell reference. |
| `calculation` | Yes | The formula that uses the parameter names and returns a result. It must be the last argument. |

### Return Value

The result of the calculation for the values supplied. A LAMBDA that is not called returns a function rather than a value, which Excel shows as `#CALC!` in a cell.

## Examples

### Example 1: Calling a LAMBDA Inline

```excel
=LAMBDA(price,price*0.9)(B2)
```

**Result:** `45` when B2 holds 50.

The function takes one value, `price`, and applies a 10% reduction. The value in parentheses after the LAMBDA is the argument, so the formula returns 50 × 0.9 = 45.

### Example 2: Calling a Named Function

Define the name `DiscountPrice` as `=LAMBDA(price,rate,price*(1-rate))` in Name Manager in Excel, or as a named function in Google Sheets.

```excel
=DiscountPrice(B2,0.1)
```

**Result:** `72` when B2 holds 80.

Once named, the function is called like a built-in function. Changing the definition updates every cell that uses it, which is the main reason to name a LAMBDA.

<!-- Image 2: Inline Versus Named LAMBDA Calls. See Images/Logical/LAMBDA.md -->

### Example 3: Passing a LAMBDA to MAP

```excel
=MAP(A2:A4,LAMBDA(x,x*2))
```

**Result:** `6`, `10` and `14` when A2:A4 hold 3, 5 and 7.

MAP calls the LAMBDA once for each item and returns the results as an array, which spills into the cells below. The LAMBDA is not called directly, because MAP does the calling.

### Example 4: Two Parameters With LET Inside

```excel
=LAMBDA(a,b,LET(total,a+b,total*1.08))(100,50)
```

**Result:** `162`

The function adds its two arguments, names the sum with LET, and applies an 8% charge. 150 × 1.08 = 162. LET keeps the intermediate step readable inside the LAMBDA.

### Example 5: Calling With the Wrong Number of Values

```excel
=LAMBDA(a,b,a+b)(5)
```

**Result:** `#VALUE!`

The function expects two arguments and receives one. Microsoft Excel returns `#VALUE!` when the number of arguments does not match the parameter list.

## Story Problems

### Problem 1: Shipping Cost With a Weight Cap

A courier charges a base fee of 5 plus 1.5 per kilogram. Billed weight stops at 20 kg, so heavier parcels pay the same weight charge as a 20 kg parcel. Define the name `ShipCost` as `=LAMBDA(w,5+1.5*MIN(w,20))`.

| Parcel | Weight (kg) |
| --- | --- |
| P1 | 4 |
| P2 | 12 |
| P3 | 25 |

**Task:** Fill column C with each parcel's cost using `ShipCost`, then total the costs in C5.

**Solution:**

```excel
=ShipCost(B2)
```

```excel
=SUM(C2:C4)
```

**Answer:** P1 costs `11`, P2 costs `23` and P3 costs `35`, because its billed weight is capped at 20. The total is `69`.

<!-- Image 3: Shipping Cost Worksheet. See Images/Logical/LAMBDA.md -->

### Problem 2: Rounded Discounts on a Cart

A cart has three items, and each receives a 10% discount rounded to the nearest cent. Define the name `NetPrice` as `=LAMBDA(p,r,ROUND(p*(1-r),2))`.

| Item | Price |
| --- | --- |
| Notebook | 19.99 |
| Backpack | 42.50 |
| Pen | 7.00 |

**Task:** Calculate the discounted price of each item in column C, then total the three prices.

**Solution:**

```excel
=NetPrice(B2,0.1)
```

```excel
=SUM(C2:C4)
```

**Answer:** The discounted prices are `17.99`, `38.25` and `6.30`. The total is `62.54`.

## Use Cases

### Custom Discount Formula

**Scenario:** A sales team applies the same discount rule across several sheets and wants one definition to maintain.

```excel
=DiscountPrice(B2,C2)
```

**Why It Works:** The discount logic lives in the named LAMBDA. Each sheet calls it with a price and a rate, so a change to the rule is made once.

### Rounded Price Rule

**Scenario:** A price list must round every discounted price to the cent, and the rounding must match across all tabs.

```excel
=NetPrice(B2,C2)
```

**Why It Works:** The ROUND step is inside the named function, so no tab can forget it.

### Reusable Tax Calculation

**Scenario:** An invoice template calculates tax on net amounts and rounds the total to two decimals.

```excel
=LAMBDA(net,rate,LET(tax,net*rate,ROUND(net+tax,2)))(B2,0.0825)
```

**Why It Works:** LET names the tax step inside the LAMBDA, so the rule reads as a sequence of named steps. The same pattern can be saved under a name for repeated use.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The call has the wrong number of arguments, or the LAMBDA has more than 253 parameters. | Match each call to the parameter list. |
| `#CALC!` | A LAMBDA is placed in a cell and not called. | Append the arguments, such as `(B2)`, or save the LAMBDA under a name. |
| `#NUM!` | Recursive calls go too deep. | Replace recursion with SCAN or REDUCE, which handle repeated steps without recursion. |
| Invalid name | A parameter name matches a cell reference, such as `A1`. | Use a descriptive name such as `price` or `rate`. |
| LAMBDA not called | In Google Sheets, a LAMBDA is used as a value instead of being called. | Add the call with arguments after the LAMBDA, or pass it to a helper function. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024 (Windows and Mac) | Accepts up to 253 parameters. Named LAMBDAs can be scoped to a workbook, or to one sheet except in Excel for the web. Not listed for Excel 2021. |
| Google Sheets | Available | Parameter names can contain dots and underscores. A named function is defined once and called by name in any cell of the spreadsheet. |

## Tips and Best Practices

- Test each LAMBDA inline with sample values before you give it a name.
- Choose parameter names such as `price` and `rate`, and avoid names that look like cell references.
- Use LET inside a LAMBDA to label the steps when the calculation has more than one stage.
- Add a short comment in Excel when you define a named LAMBDA, so others know what it does (the comment field holds up to 255 characters).
- Keep a LAMBDA small. A long LAMBDA is harder to test than several named helpers.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MAP](MAP.md) | Calls a LAMBDA for each item in one or more arrays. |
| [REDUCE](REDUCE.md) | Combines array items into one value using a LAMBDA with an accumulator. |
| [SCAN](SCAN.md) | Returns each running step of a REDUCE-style calculation. |
| [MAKEARRAY](MAKEARRAY.md) | Builds an array of set size, calling a LAMBDA with row and column numbers. |
| [BYROW](BYROW.md) | Applies a LAMBDA to each row of an array. |
| [BYCOL](BYCOL.md) | Applies a LAMBDA to each column of an array. |
| [LET](LET.md) | Names intermediate values inside a calculation, often inside a LAMBDA. |

## Official Documentation

- [Microsoft Support: LAMBDA function](https://support.microsoft.com/en-us/excel/functions/lambda-function)
- [Google Docs Editors Help: LAMBDA](https://support.google.com/docs/answer/12508718)
