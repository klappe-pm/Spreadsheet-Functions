---
domain: Spreadsheet Functions
category: Logical
subcategory: Boolean Values
purpose:
  - Conditional Logic
use-case:
  - Data Quality Alerts
  - Priority Routing
  - Threshold Monitoring
related:
  - AND
  - COUNTIF
  - IF
  - IFS
  - NOT
  - XOR
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/or-function
  - https://support.google.com/docs/answer/3093306
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Any Condition True
  - Boolean Or
tags:
  - boolean
  - conditional-logic
  - excel
  - logical
  - sheets
---

# OR

## Description

**OR** returns TRUE when at least one of its tests is TRUE and FALSE only when every test is FALSE. Use it for rules that accept any of several conditions, such as "urgent or VIP," or for alerts that fire when any one measurement is out of range.

OR is most often placed inside IF as the test. `=IF(OR(A2="Red",A2="Amber"),"Stop","Go")` is easier to read than two nested IF functions, and it keeps working when another color is added to the list.

The most common mistake is using OR where AND is meant. A value cannot be both below 10 and above 0 at once, so `OR(A2>0,A2<10)` is TRUE for every number. For a value that must fall between two limits, use `AND(A2>0,A2<10)`.

## Syntax

```excel
=OR(logical1, [logical2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/OR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `logical1` | Yes | The first test. It can be a comparison such as `A2="Active"`, a logical function such as `ISERROR(B2)`, or a cell that holds TRUE or FALSE. |
| `logical2, ...` | No | Further tests. Microsoft Excel accepts up to 255 arguments in total. Google Sheets help does not state a limit. |

### Return Value

TRUE if any argument is TRUE, and FALSE if all arguments are FALSE. In a range or array argument, text and empty cells are ignored. If a range holds no logical values, OR returns `#VALUE!`.

## Examples

### Example 1: Matching One of Two Spellings

```excel
=OR(A2="Yes",A2="Y")
```

**Result:** `TRUE` when A2 holds `Y`.

The first test is FALSE because "Y" is not "Yes", but the second test is TRUE, so OR returns TRUE. A single TRUE is enough.

### Example 2: Grouping Departments Inside IF

```excel
=IF(OR(B2="Sales",B2="Marketing"),"Revenue Team","Support Team")
```

**Result:** `Support Team` when B2 holds `Support`.

Neither test is TRUE for "Support," so OR returns FALSE and IF returns the second branch. Adding a department means adding one more test inside OR.

### Example 3: Flagging Any Error in a Row

```excel
=IF(OR(ISERROR(A2),ISERROR(B2),ISERROR(C2)),"Check Data","OK")
```

**Result:** `Check Data` when B2 shows `#N/A`.

ISERROR returns TRUE for any error value. Because B2 is an error, its test is TRUE, and OR passes that result up to IF. Only a row with three error-free cells shows "OK."

<!-- Image 2: Either-Side Test Layout for OR. See Images/Logical/OR.md -->

### Example 4: Alerting on Either Limit

```excel
=IF(OR(B2<LowLimit,B2>HighLimit),"Alert","Normal")
```

**Result:** `Alert` when B2 holds 105 and HighLimit holds 100.

The reading is above the high limit, so the second test is TRUE. Named limits keep the formula readable and let the limits change without editing the formula.

### Example 5: Matching a Long List With COUNTIF

```excel
=IF(COUNTIF(RegionList,C2)>0,"Listed","Not Listed")
```

**Result:** `Not Listed` when C2 holds `Central` and RegionList holds North, South, East and West.

Writing 12 or 20 separate tests inside OR is hard to maintain. COUNTIF counts the matches in the list, and any match above zero means the value is listed.

### Example 6: Checking a Whole Range

```excel
=OR(A2:A10="Error")
```

**Result:** `TRUE` when any cell in A2:A10 contains `Error`.

Microsoft 365 evaluates the comparison across the range and OR returns one result. Older Excel versions need the formula entered as an array formula with Ctrl+Shift+Enter.

## Story Problems

### Problem 1: Which Orders Need a Surcharge

A shipping desk adds a surcharge when an order weighs more than 30 kg, goes to a remote destination, or is marked fragile.

| Order | Weight (kg) | Destination | Fragile |
| --- | --- | --- | --- |
| A101 | 12 | Local | No |
| A102 | 35 | Local | No |
| A103 | 8 | Remote | No |
| A104 | 9 | Local | Yes |
| A105 | 5 | Local | No |

**Task:** Mark each order `Surcharge` or `None` in column E, then count the surcharged orders.

**Solution:**

```excel
=IF(OR(B2>30,C2="Remote",D2="Yes"),"Surcharge","None")
```

```excel
=COUNTIF(E2:E6,"Surcharge")
```

**Answer:** `3`. A102 is heavy, A103 is remote and A104 is fragile. A101 and A105 get no surcharge.

<!-- Image 3: Surcharge Worksheet. See Images/Logical/OR.md -->

### Problem 2: Expense Lines to Review

A finance team reviews an expense line when the amount is missing, the receipt is missing, or the amount is above 500.

| Expense | Amount | Receipt |
| --- | --- | --- |
| Lunch | 42 | Yes |
| Hotel | 610 | Yes |
| Taxi | 25 | Missing |
| Software |  | Yes |
| Books | 80 | Yes |

**Task:** Mark each line `Review` or `OK` in column D, then count the lines to review.

**Solution:**

```excel
=IF(OR(B2="",C2="Missing",B2>500),"Review","OK")
```

```excel
=COUNTIF(D2:D6,"Review")
```

**Answer:** `3`. Hotel is above 500, Taxi has no receipt and Software has no amount. Lunch and Books pass.

## Use Cases

### Priority Routing

**Scenario:** A support queue sends a ticket to the priority team when the customer is a VIP, the ticket is marked urgent, or the account value is above $50,000.

```excel
=IF(OR(B2="VIP",C2="Urgent",D2>50000),"Priority Queue","Standard Queue")
```

**Why It Works:** Any one of the three triggers is enough, so OR matches the business rule exactly. A separate test for each trigger keeps the reason for a decision visible.

### Data Quality Alerts

**Scenario:** An import sheet must flag any row where the invoice date is blank, the amount is not a number, or the status is unknown.

```excel
=IF(OR(A2="",NOT(ISNUMBER(C2)),COUNTIF(StatusList,D2)=0),"Check Row","OK")
```

**Why It Works:** Each problem is a separate test, and a single failed test is enough to flag the row. The status check uses COUNTIF so the valid statuses can live in a named list.

### Threshold Monitoring

**Scenario:** A plant records two temperature sensors. Either sensor going outside its range should trigger an alert.

```excel
=IF(OR(B2<MinTemp,B2>MaxTemp,C2<MinTemp,C2>MaxTemp),"ALERT","Normal")
```

**Why It Works:** The formula tests both readings against the same limits. Changing the limits in two named cells updates every row.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A test is not logical, or a range holds no TRUE or FALSE values. | Pass comparisons or logical functions, or compare the range first, such as `OR(A2:A10="Error")`. |
| Always TRUE | The tests cover every value, such as `OR(A1>0,A1<10)`. | Use AND for a range check, such as `AND(A1>0,A1<10)`. |
| Missed matches | Text and empty cells inside a range are ignored, so a range of text never returns TRUE. | Compare each cell with the value you want before passing the range to OR. |
| Argument limit | A formula passes more than 255 tests in Excel. | Put the values in a list and use COUNTIF against it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All listed versions: Excel 2016, 2019, 2021, 2024 and Microsoft 365 | Accepts up to 255 arguments. Works directly with arrays in Microsoft 365, while older versions need Ctrl+Shift+Enter. |
| Google Sheets | Available | Accepts range references such as `OR(A1:A10,B1:B10)`. Zero is FALSE and every other number is TRUE. The help page does not state an argument limit. |

## Tips and Best Practices

- Wrap OR in IF when the result should be a label instead of TRUE or FALSE.
- Use AND for "between" checks, and OR for "either side" checks.
- Put long lists of alternatives in a range and test them with COUNTIF.
- Trace each test with one value that passes, one that fails, and one at the boundary before you copy the formula down.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AND](AND.md) | Returns TRUE only when every test is TRUE. Use it for range checks. |
| [COUNTIF](../Statistical/COUNTIF.md) | Counts matches in a list. Use it when many alternatives would make OR long. |
| [IF](IF.md) | Chooses a result from OR's TRUE or FALSE output. |
| [IFS](IFS.md) | Returns a different value for each condition. Use it when each OR group should give its own result. |
| [NOT](NOT.md) | Reverses a test. NOT(OR()) builds an exclusion rule. |
| [XOR](XOR.md) | Returns TRUE when an odd number of tests are TRUE. Use it when exactly one of two conditions should hold. |

## Official Documentation

- [Microsoft Support: OR function](https://support.microsoft.com/en-us/excel/functions/or-function)
- [Google Docs Editors Help: OR](https://support.google.com/docs/answer/3093306)
