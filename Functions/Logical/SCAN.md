---
domain: Spreadsheet Functions
category: Logical
subcategory: Lambda Helpers
purpose:
  - Aggregation
  - Array Shaping
use-case:
  - Cumulative Sales Targets
  - Running Account Balance
  - Running Peak Temperature
related:
  - LAMBDA
  - MAKEARRAY
  - MAP
  - REDUCE
  - SUM
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/scan-function
  - https://support.google.com/docs/answer/12569094
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Intermediate Results
  - Running Total
tags:
  - cumulative-totals
  - dynamic-array
  - excel
  - lambda
  - sheets
---

# SCAN

## Description

**SCAN** works like REDUCE, but it keeps every intermediate step. It starts with an initial value, calls a LAMBDA for each item with the running result and the current item, and returns an array of all the running results. The last value in the output equals what REDUCE would return for the same inputs.

Use SCAN when the running history matters: a cumulative total, a running account balance, or the point at which a target is first passed. Use REDUCE when only the final result is needed.

Always supply the initial value. It sets the first running result and must match the operation: 0 for sums, 1 for products and an empty string for text. Google Sheets requires it, and the Microsoft syntax treats it as optional, so writing it out keeps a formula clear in both products.

## Syntax

```excel
=SCAN([initial_value], array, LAMBDA(accumulator, value, calculation))
```

Google Sheets uses `SCAN(initial_value, array_or_range, LAMBDA)`, with the initial value required.

<!-- Image 1: Syntax Anatomy. See Images/Logical/SCAN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `initial_value` | Required in Sheets, optional in Excel | The starting value of the accumulator, which becomes the first running result after the first item. |
| `array` | Yes | The array or range to scan. Items are read row by row. |
| `LAMBDA` | Yes | A LAMBDA with an accumulator name, a value name and a calculation. The calculation must return one value for each step. |

### Return Value

An array with one running result for each item in the input. For a single column of input, the result is a single column that spills into the cells below the formula. A LAMBDA with the wrong number of arguments returns an error, and Google Sheets returns `#N/A` in that case.

## Examples

### Example 1: Running Total

```excel
=SCAN(0,A2:A5,LAMBDA(acc,v,acc+v))
```

**Result:** `5`, `8`, `16` and `18` when A2:A5 hold 5, 3, 8 and 2.

Each step adds the next item to the running total. The last result, 18, is the same value SUM would return for the range.

### Example 2: Running Product

```excel
=SCAN(1,A2:A4,LAMBDA(acc,v,acc*v))
```

**Result:** `2`, `6` and `24` when A2:A4 hold 2, 3 and 4.

The starting value is 1 so the first multiplication does not change the first item. The steps are 2, then 2 × 3 = 6, then 6 × 4 = 24.

<!-- Image 2: Running Steps Versus Final Total. See Images/Logical/SCAN.md -->

### Example 3: Building Text Step by Step

```excel
=SCAN("",A2:A4,LAMBDA(acc,v,acc&v))
```

**Result:** `a`, `ab` and `abc` when A2:A4 hold a, b and c.

The starting value is an empty string, which is the correct starting point for text. Each step shows the text joined so far.

### Example 4: Running Account Balance

```excel
=SCAN(500,B2:B5,LAMBDA(bal,t,bal+t))
```

**Result:** `750`, `630`, `550` and `850` when B2:B5 hold 250, -120, -80 and 300.

The opening balance of 500 is the starting value. Deposits add to the balance and withdrawals subtract from it, and each step shows the balance after that transaction.

### Example 5: Running Maximum

```excel
=SCAN(0,A2:A5,LAMBDA(hi,v,MAX(hi,v)))
```

**Result:** `4`, `9`, `9` and `11` when A2:A5 hold 4, 9, 2 and 11.

Each step keeps the higher of the highest value so far and the current item. The starting value of 0 works because all the readings are positive.

## Story Problems

### Problem 1: Running Balance After Transactions

A checking account starts the week with 1200. The transactions in B2:B5 are a deposit of 300, a bill of 450, a fee of 200 and a deposit of 150.

| Transaction | Amount |
| --- | --- |
| Deposit | 300 |
| Bill | -450 |
| Fee | -200 |
| Deposit | 150 |

**Task:** Show the balance after each transaction in one formula, then state the final balance.

**Solution:**

```excel
=SCAN(1200,B2:B5,LAMBDA(bal,t,bal+t))
```

**Answer:** The balances are `1500`, `1050`, `850` and `1000`. The final balance is `1000`.

<!-- Image 3: Running Balance Worksheet. See Images/Logical/SCAN.md -->

### Problem 2: Week When the Sales Target Is Passed

A team has a target of 90 units over four weeks. Weekly sales are 18, 22, 25 and 30.

| Week | Sales |
| --- | --- |
| 1 | 18 |
| 2 | 22 |
| 3 | 25 |
| 4 | 30 |

**Task:** Show the cumulative sales for each week, then find the first week in which the total reaches the target.

**Solution:**

```excel
=SCAN(0,B2:B5,LAMBDA(a,v,a+v))
```

**Answer:** The cumulative totals are `18`, `40`, `65` and `95`. The target is first passed in week 4, when the total reaches 95.

## Use Cases

### Cumulative Sales Targets

**Scenario:** A sales manager tracks the running total of weekly sales against a quarterly target.

```excel
=SCAN(0,WeeklySales,LAMBDA(a,v,a+v))
```

**Why It Works:** Each week's running total is shown next to the target, so the manager sees how close the team is at every step.

### Running Account Balance

**Scenario:** A bank export lists transactions for a month, and a report needs the balance after each line.

```excel
=SCAN(OpeningBalance,Transactions,LAMBDA(bal,t,bal+t))
```

**Why It Works:** The opening balance is the starting value, so the report starts from the figure on the statement and the formula adds each transaction in order.

### Running Peak Temperature

**Scenario:** A weather station logs temperatures through the day, and an operator needs the highest reading so far at each time.

```excel
=SCAN(MIN(Readings),Readings,LAMBDA(peak,r,MAX(peak,r)))
```

**Why It Works:** Starting from the lowest reading makes the first running peak correct for any set of values, including negative ones.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` (Incorrect Parameters) | The LAMBDA does not use an accumulator, a value and a calculation in the expected form. | Write the LAMBDA with the accumulator and value names followed by the calculation. |
| `#N/A` in Sheets | The LAMBDA has the wrong number of arguments. | Use exactly two names before the calculation. |
| Single value expected | A step returns an array instead of one value. | Return one value per step. |
| Argument must be a LAMBDA | The last argument is not a LAMBDA. | Put the LAMBDA last. |
| Text comes out wrong | The initial value is 0 when text is expected. | Use `""` as the starting value for text. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024 (Windows and Mac), Microsoft Office and Office for iPhone | The Microsoft page does not list Excel 2021. The initial value is shown as optional in the syntax. |
| Google Sheets | Available | The initial value is required. The LAMBDA takes exactly two names, and a named function can be passed without parentheses. |

## Tips and Best Practices

- Supply the initial value in every formula, so the first result is clear to the next reader.
- Choose the starting value that matches the operation: 0 for a sum, 1 for a product and "" for text.
- Use REDUCE when only the final value is needed, because it is easier to read.
- Pair SCAN with MATCH to find the first step that reaches a target.
- Keep the LAMBDA short, and move a long rule into a named LAMBDA of its own.

## Related Functions

| Function | Relationship |
| --- | --- |
| [REDUCE](REDUCE.md) | Returns only the final value of the same accumulator pattern. |
| [LAMBDA](LAMBDA.md) | Defines the accumulator-and-value calculation that SCAN calls. |
| [MAP](MAP.md) | Transforms each item separately, without a running result. |
| [MAKEARRAY](MAKEARRAY.md) | Builds an array from row and column numbers rather than from running results. |
| [SUM](../Math%20%26%20Trig/SUM.md) | Gives the final total of a range. The last SCAN step matches it for a running sum. |

## Official Documentation

- [Microsoft Support: SCAN function](https://support.microsoft.com/en-us/excel/functions/scan-function)
- [Google Docs Editors Help: SCAN](https://support.google.com/docs/answer/12569094)
