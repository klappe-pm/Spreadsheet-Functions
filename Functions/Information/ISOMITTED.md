---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Conditional Logic
  - Type Checking
use-case:
  - Default Discount Rate
  - Default Shipping Fee
  - Optional LAMBDA Argument
related:
  - IF
  - ISBLANK
  - ISREF
  - LAMBDA
  - LET
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/isomitted-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - excel
  - lambda
  - optional-arguments
  - type-checking
---

# ISOMITTED

## Description

**ISOMITTED** returns TRUE when a parameter of a LAMBDA function was left out of the call and FALSE when a value was supplied. It lets a custom function give an optional parameter a default value without requiring the caller to type one.

ISOMITTED works only inside a LAMBDA definition, because it tests LAMBDA parameters. Pass an empty argument, written as a trailing comma such as `(100,)`, to leave a parameter out. Passing 0 or any other value counts as supplying the parameter, so ISOMITTED returns FALSE.

Use ISOMITTED with IF to choose between a default calculation and one that uses the caller's value. For a named LAMBDA, define the function in Name Manager and call it by its name in a formula.

## Syntax

```excel
=ISOMITTED(argument)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISOMITTED.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `argument` | Yes | The LAMBDA parameter to test. It must be a parameter name defined in the LAMBDA, not a cell reference. |

### Return Value

TRUE when the parameter was omitted from the call. FALSE when a value was supplied. The function is meaningful only inside a LAMBDA.

## Examples

### Example 1: Default Markup When the Rate Is Left Out

```excel
=LAMBDA(price,rate,IF(ISOMITTED(rate),price*1.1,price*(1+rate)))(100,)
```

**Result:** `110`

The empty second argument is omitted, so ISOMITTED returns TRUE and the default 10 percent markup applies.

### Example 2: A Supplied Rate

```excel
=LAMBDA(price,rate,IF(ISOMITTED(rate),price*1.1,price*(1+rate)))(100,0.2)
```

**Result:** `120`

A rate is supplied, so ISOMITTED returns FALSE and the formula uses 0.2 instead of the default.

### Example 3: Last Argument Omitted

```excel
=LAMBDA(a,b,c,IF(ISOMITTED(c),a+b,a+b+c))(2,3,)
```

**Result:** `5`

The third argument is omitted, so the formula adds only the first two values. Calling the same LAMBDA with `(2,3,4)` returns 9.

## Story Problems

### Problem 1: Parcel Fee With an Optional Zone Surcharge

A courier charges 2 per kilogram of parcel weight. A zone surcharge of 1.5 per zone number is added only when a zone is entered. The dispatcher calls the fee function with a weight of 4 and a zone of 3.

**Task:** Calculate the fee for a 4 kilogram parcel in zone 3.

**Solution:**

```excel
=LAMBDA(w,z,w*2+IF(ISOMITTED(z),0,z*1.5))(4,3)
```

**Answer:** `12.5`. The base fee is 4 times 2, or 8, and the surcharge is 3 times 1.5, or 4.5.

### Problem 2: Discount Default for Quick Quotes

A shop gives a default discount of 10 percent when the sales clerk leaves the rate blank. The function takes an order amount and an optional rate.

**Task:** Price an order of 200 with the rate left blank.

**Solution:**

```excel
=LAMBDA(amount,rate,IF(ISOMITTED(rate),amount*0.9,amount*(1-rate)))(200,)
```

**Answer:** `180`. With the rate omitted, the default 10 percent discount applies to 200.

<!-- Image 2: Optional Argument Pattern. See Images/Information/ISOMITTED.md -->

## Use Cases

### Default Discount Rate

**Scenario:** A quoting tool applies a standard 10 percent discount unless the salesperson enters a negotiated rate in column C.

```excel
=IF(ISBLANK(C2),B2*0.9,B2*(1-C2))
```

**Why It Works:** On a worksheet, a blank cell is a supplied reference, so ISOMITTED cannot test it. ISBLANK is the worksheet test that does the same job here. Entering a rate in C2 overrides the default for that quote.

### Default Shipping Fee

**Scenario:** A logistics team estimates shipping fees, and most estimates do not need a zone surcharge.

```excel
=LAMBDA(w,z,w*2+IF(ISOMITTED(z),0,z*1.5))(A2,)
```

**Why It Works:** The trailing comma leaves the zone out, so the surcharge is skipped. Calling the same LAMBDA with a zone, such as `(A2,B2)`, adds the surcharge. Define the LAMBDA in Name Manager to reuse it across the workbook.

### Optional LAMBDA Argument

**Scenario:** A team wants one reusable function that accepts an optional tax rate, with the rate defaulting to 8 percent when it is omitted.

```excel
=LAMBDA(price,r,LET(rate,IF(ISOMITTED(r),0.08,r),price*(1+rate)))(B2,)
```

**Why It Works:** The LET step holds the default in one place, and the rest of the formula reads cleanly. The trailing comma omits the rate, so the default applies.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error or unexpected result | ISOMITTED is used outside a LAMBDA, so there is no parameter to test. | Move the test inside a LAMBDA definition. |
| `FALSE` when the argument was left blank | A 0 or other value was passed instead of leaving the argument empty. | Use a trailing comma, such as `(100,)`, to omit the argument. |
| `FALSE` for a blank cell passed as an argument | A reference to an empty cell counts as a supplied argument. | Test the cell with ISBLANK in the calling formula, or leave the argument out of the call. |
| `#NAME?` in an older version | ISOMITTED is not available in Excel 2021 or earlier. | Use Microsoft 365, Excel 2024 or Excel for the web. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Microsoft 365 for Mac, Excel for the web and Excel 2024. | Works only inside a LAMBDA definition. Not listed for Excel 2021 or earlier. |
| Google Sheets | Not available | The closest alternative is to test the cell that holds the optional input with ISBLANK, such as `=IF(ISBLANK(B2),0.08,B2)`. |

## Tips and Best Practices

- Put optional parameters last so callers can omit them without confusion.
- Use LET to store the default value once, then use the result in the rest of the formula.
- Use a clear parameter name, such as rate, so the default reads well in the LAMBDA body.
- Test each path, with and without the optional argument, before you share the function.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LAMBDA](../Logical/LAMBDA.md) | Defines the reusable function whose parameters ISOMITTED tests. |
| [LET](../Logical/LET.md) | Stores the default value or intermediate result in a named step. |
| [IF](../Logical/IF.md) | Chooses the default calculation or the supplied-value calculation. |
| [ISBLANK](ISBLANK.md) | Tests a cell for emptiness, the closest alternative in Google Sheets. |
| [ISREF](ISREF.md) | Tests whether a value is a cell reference rather than a parameter state. |

## Official Documentation

- [Microsoft Support: ISOMITTED function](https://support.microsoft.com/en-us/excel/functions/isomitted-function)
