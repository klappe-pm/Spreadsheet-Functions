---
domain: Spreadsheet Functions
category: Logical
subcategory: Named Calculations
purpose:
  - Conditional Logic
  - Financial Modeling
use-case:
  - Commission Calculation
  - Invoice Totals With Tax
  - Reusable Lookup Results
related:
  - IF
  - IFS
  - LAMBDA
  - MAP
  - REDUCE
  - XLOOKUP
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/let-function
  - https://support.google.com/docs/answer/13190535
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Local Variables
  - Named Calculations
tags:
  - excel
  - formula-simplification
  - named-values
  - sheets
---

# LET

## Description

**LET** gives names to intermediate results inside a single formula, then uses those names in the final calculation. The names exist only inside that LET, so they do not clash with named ranges elsewhere in the workbook.

LET serves two purposes. It makes long formulas readable, because `TaxRate` explains a number better than `0.0825` does. It also avoids repeated work, because each value expression is calculated once, even when its name is used many times. Before LET, the same subexpression often appeared two or three times in one formula.

LET is an advanced function. Use it when a formula repeats a long expression or mixes several steps that deserve labels. For a one-step calculation, a plain formula is shorter and easier to share with people who do not use LET.

## Syntax

```excel
=LET(name1, name_value1, [name2, name_value2], ..., calculation)
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/LET.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `name1` | Yes | The first name. It must start with a letter and must not look like a cell reference. |
| `name_value1` | Yes | The value or expression assigned to `name1`. It is calculated once. |
| `name2`, `name_value2` | No | Further name and value pairs. Each value can use the names declared before it. |
| `calculation` | Yes | The final formula. It must be the last argument and must use the names to return a result. |

### Return Value

The result of the final calculation. The value depends on the calculation, so a LET that ends in a range can return an array. Excel allows up to 126 name and value pairs.

## Examples

### Example 1: Two Named Inputs

```excel
=LET(price,20,qty,3,price*qty)
```

**Result:** `60`

Each name is assigned a value, and the last argument multiplies them. The same result could be written as `20*3`, but the names make the formula self-explanatory when the inputs come from cells.

### Example 2: Applying a Named Tax Rate

```excel
=LET(net,B2,rate,0.0825,net*(1+rate))
```

**Result:** `259.8` when B2 holds 240.

The net amount is 240 and the rate is 8.25%. 240 × 1.0825 = 259.8. A later edit to the rate changes one value, and the rest of the formula reads the same.

### Example 3: Reusing a Value

```excel
=LET(total,SUM(B2:B6),total/COUNT(B2:B6))
```

**Result:** `32` when B2:B6 hold 10, 20, 30, 40 and 60.

The sum 160 is calculated once and used as the numerator. The count of 5 is taken from the same range, so the result is the mean, 160 ÷ 5 = 32. For a plain average, AVERAGE is shorter.

### Example 4: Building Text From a Named Value

```excel
=LET(name,"Ava",UPPER(name)&" ("&LEN(name)&")")
```

**Result:** `AVA (3)`

The name `name` holds the text once, and the calculation uses it twice without repeating the string. Replace `"Ava"` with a cell reference to use the same formula on a list.

### Example 5: Classifying a Score

```excel
=LET(score,B2,IF(score>=90,"A",IF(score>=80,"B","C")))
```

**Result:** `B` when B2 holds 84.

The score is named once, so the nested IF tests read as `score>=90` and `score>=80`. The score cell is referenced only in the assignment, which makes the test easy to change.

<!-- Image 2: Repeated Expression Versus Named Value. See Images/Logical/LET.md -->

## Story Problems

### Problem 1: Commission on Sales Above Target

A sales team earns 8% commission only on the sales above each rep's target.

| Rep | Sales | Target |
| --- | --- | --- |
| Ava | 12000 | 10000 |
| Ben | 9000 | 10000 |
| Chloe | 15500 | 12000 |

**Task:** In column D, calculate each rep's commission, then total the commissions in D5.

**Solution:**

```excel
=LET(over,MAX(0,B2-C2),over*0.08)
```

```excel
=SUM(D2:D4)
```

**Answer:** Ava earns `160`, Ben earns `0` and Chloe earns `280`. The total is `440`. Ava is 2000 over target and Chloe is 3500 over.

<!-- Image 3: Commission Worksheet. See Images/Logical/LET.md -->

### Problem 2: Final Price After Discount and Tax

An invoice of 200 receives a 10% discount, and tax of 8% applies after the discount.

| Subtotal | Discount | Tax |
| --- | --- | --- |
| 200 | 0.10 | 0.08 |

**Task:** Calculate the final amount in D2 using names for the net amount and the taxed amount.

**Solution:**

```excel
=LET(net,B2*(1-C2),net*(1+D2))
```

**Answer:** `194.4`. The net amount is 200 × 0.90 = 180, and 180 × 1.08 = 194.4.

## Use Cases

### Commission Calculation

**Scenario:** A payroll sheet pays a base rate on all sales and an extra rate when a target is met.

```excel
=LET(base,Sales*0.05,bonus,IF(Sales>=Target,Sales*0.02,0),base+bonus)
```

**Why It Works:** Each part of the pay rule has a name, so an auditor can check the base and the bonus separately. The sales figure is referenced only in the two steps that need it.

### Invoice Totals With Tax

**Scenario:** An accounts team applies a flat discount, then tax, to each invoice in a batch.

```excel
=LET(net,Amount-Discount,net*(1+TaxRate))
```

**Why It Works:** The discounted amount is named before tax is applied, which matches how the invoice is presented to the customer.

### Reusable Lookup Results

**Scenario:** A price sheet finds a product code in a list and returns its price, with a label when the code is missing.

```excel
=LET(row,MATCH(A2,Codes,0),IF(ISNA(row),"Unknown Code",INDEX(Prices,row)))
```

**Why It Works:** MATCH runs once and its position is reused by INDEX. Without the name, the lookup would repeat inside the IF test and again in the result.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | A name is misspelled, or it is used before the pair that declares it. | Check the spelling and declare each name before its first use. |
| Invalid name | The name looks like a cell reference or starts with a number. Names such as `c` and `r` are rejected because they conflict with R1C1 references. | Choose a descriptive name such as `Rate` or `TaxRate`. |
| Formula does not calculate | The last argument is a name instead of a calculation. | End the formula with the calculation that uses the names. |
| Too many names | A formula passes more than 126 name and value pairs in Excel. | Split the work across helper cells, or nest LET calls. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024 (Windows and Mac), Excel 2021 (Windows and Mac) | Requires at least one name and value pair. Accepts up to 126 pairs. The function is not listed for Excel 2019. |
| Google Sheets | Available | Each value expression is evaluated once even when its name is used later. Names cannot contain spaces or special characters, and a name used before its declaration causes an error. |

## Tips and Best Practices

- Choose names that describe the value, such as `NetAmount` rather than `x`.
- Use LET whenever the same expression appears two or more times in one formula.
- Declare names in the order they are needed, because each value can use only the names declared before it.
- Wrap a LET in IFERROR or IF(ISNA()) when a lookup can fail inside it.
- For a calculation that you reuse across many formulas, define it with LAMBDA instead.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LAMBDA](LAMBDA.md) | Stores a calculation with parameters so it can be called repeatedly. |
| [IF](IF.md) | Often used inside LET to test a named value. |
| [IFS](IFS.md) | Tests several named values in order when each branch needs its own result. |
| [MAP](MAP.md) | Applies a calculation to each item in an array, where LET names the steps. |
| [REDUCE](REDUCE.md) | Combines array items into one result, with names defined in its LAMBDA. |
| [XLOOKUP](../Lookup%20%26%20Reference/XLOOKUP.md) | Returns a looked-up value. LET can store its match result for reuse. |

## Official Documentation

- [Microsoft Support: LET function](https://support.microsoft.com/en-us/excel/functions/let-function)
- [Google Docs Editors Help: LET](https://support.google.com/docs/answer/13190535)
