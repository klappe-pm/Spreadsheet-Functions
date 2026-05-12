---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- math-trig
subTopics:
- modulo
- remainder
- division
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Modulo
- Remainder
- Mod Function
tags:
- modulo
- remainder
- division
- cyclic
- alternating
---

# MOD

## Description

**MOD** returns the remainder after division—the amount left over when one number doesn't divide evenly into another. MOD(10, 3) returns 1 because 10 divided by 3 is 3 with remainder 1 (3 x 3 = 9, leaving 1). It's the spreadsheet implementation of the modulo operation, fundamental to detecting patterns, cycling through values, and determining divisibility.

This function is incredibly versatile despite its simplicity. Use MOD to **alternate row colors** (MOD(ROW(), 2) returns 0 or 1 for even/odd rows), **extract time components** (MOD(SerialTime, 1) gives time portion of datetime), **wrap values in cycles** (MOD(Month + 3, 12) rotates months), and **check divisibility** (MOD(A1, 5) = 0 means A1 is divisible by 5).

**Critical behavior with negative numbers:** MOD always returns a result with the same sign as the divisor. MOD(-10, 3) = 2, not -1. This matches mathematical convention where the result is always in the range [0, divisor) for positive divisors. Some programming languages use different conventions—spreadsheet MOD follows the mathematically consistent "floored division" approach.

The formula MOD uses internally is: `MOD(n, d) = n - d * INT(n/d)`. This explains the sign behavior and helps predict results. Note that MOD(n, 0) returns #DIV/0! error—division by zero is undefined.

## Syntax

> [!f(x)] MOD Syntax
>
> ```
> =MOD(number, divisor)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `number` | Yes | The dividend—the number to be divided. Can be positive, negative, or a decimal. Also called the numerator in division context. |
| `divisor` | Yes | The number to divide by. Also called the denominator. Cannot be zero (returns #DIV/0!). Can be positive or negative. The result has the same sign as the divisor. |

### Return Value

Returns the remainder after dividing number by divisor. Result is always in the range [0, divisor) for positive divisors, or (divisor, 0] for negative divisors. Returns #DIV/0! if divisor is zero.

## Examples

> [!f(x)] MOD Examples

### Example 1: Basic Remainder
```
=MOD(10, 3)
```
**Result:** 1

**Explanation:** 10 divided by 3 is 3 with remainder 1 (3 x 3 = 9, and 10 - 9 = 1). The classic modulo operation.

---

### Example 2: Evenly Divisible
```
=MOD(15, 5)
```
**Result:** 0

**Explanation:** 15 divides evenly by 5 (15 = 5 x 3), leaving no remainder. MOD returning 0 means the number is divisible by the divisor.

---

### Example 3: Check If Even or Odd
```
=MOD(A1, 2)
```
**Result:** 0 for even, 1 for odd

**Explanation:** Dividing by 2 gives remainder 0 for even numbers, 1 for odd. `=IF(MOD(A1, 2) = 0, "Even", "Odd")` provides labels.

---

### Example 4: Alternate Row Formatting
```
=MOD(ROW(), 2)
```
**Result:** Alternates 0, 1, 0, 1... by row

**Explanation:** Row 1 gives 1, row 2 gives 0, row 3 gives 1, etc. Use in conditional formatting: format when MOD(ROW(), 2) = 0 for striped rows.

---

### Example 5: Every Nth Row
```
=MOD(ROW(), 5) = 0
```
**Result:** TRUE for rows 5, 10, 15, 20...

**Explanation:** Identifies every 5th row. Useful for sampling, periodic formatting, or selecting every Nth record.

---

### Example 6: Negative Number MOD Positive Divisor
```
=MOD(-10, 3)
```
**Result:** 2

**Explanation:** This surprises many users. MOD(-10, 3) = 2, not -1. The result takes the sign of the divisor (positive 3). Mathematically: -10 = 3 x (-4) + 2.

---

### Example 7: Positive Number MOD Negative Divisor
```
=MOD(10, -3)
```
**Result:** -2

**Explanation:** Result takes the sign of divisor (-3). So the remainder is negative: 10 = (-3) x (-4) + (-2).

---

### Example 8: Extract Minutes from Total Minutes
```
=MOD(TotalMinutes, 60)
```
**Result:** Minutes portion (0-59)

**Explanation:** If total is 185 minutes, MOD(185, 60) = 5. Combine with INT for hours: INT(185/60) = 3 hours, MOD(185, 60) = 5 minutes.

---

### Example 9: Extract Time from DateTime
```
=MOD(DateTimeValue, 1)
```
**Result:** Time as decimal (0 to 0.999...)

**Explanation:** Excel stores dates as integers, times as decimals. A datetime like 45000.75 has date 45000 and time 0.75 (6:00 PM). MOD extracts the fractional time.

---

### Example 10: Cycle Through Months
```
=MOD(Month + Offset - 1, 12) + 1
```
**Result:** Month number wrapped to 1-12

**Explanation:** Adding months that wrap around December. Month 11 + 3 offset = month 2 (February). The -1 and +1 adjust for 1-based month numbering.

---

### Example 11: Check Divisibility
```
=IF(MOD(A1, 7) = 0, "Divisible by 7", "Not divisible")
```
**Result:** Divisibility check

**Explanation:** When MOD returns 0, the number is evenly divisible. Check for multiples of any number using this pattern.

---

### Example 12: Decimal MOD
```
=MOD(5.5, 1.5)
```
**Result:** 1

**Explanation:** MOD works with decimals. 5.5 / 1.5 = 3.666..., which is 3 complete portions (3 x 1.5 = 4.5) plus remainder 1.

---

### Example 13: Luhn Algorithm Check Digit
```
=MOD(10 - MOD(SumOfDigits, 10), 10)
```
**Result:** Check digit for credit card validation

**Explanation:** The Luhn algorithm uses MOD 10 to calculate check digits. Nested MOD handles the edge case where the sum is already a multiple of 10.

---

### Example 14: Week Number in Month
```
=INT((DAY(A1) - 1 + MOD(WEEKDAY(EOMONTH(A1, -1)) + 5, 7)) / 7) + 1
```
**Result:** Week number within the month (1-5)

**Explanation:** Complex date calculations often use MOD for day-of-week cycling. This determines which week of the month a date falls in.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#DIV/0!` | Divisor is zero | MOD(x, 0) is undefined. Check divisor is non-zero before calculating, or use IFERROR. |
| `#VALUE!` | Non-numeric input | Ensure both arguments are numbers. Check for text that looks like numbers. |
| `#NAME?` | Misspelled function name | Verify spelling: MOD, not MODULO or MODULUS. |
| `Unexpected negative` | Sign follows divisor | MOD(-10, 3) = 2, not -1. Result always has same sign as divisor. This is correct behavior. |
| `Unexpected with decimals` | Floating-point precision | MOD(1, 0.1) might not equal exactly 0 due to binary representation. Use ROUND for clean results. |
| `Wrong for negative divisor` | Counterintuitive results | MOD(10, -3) = -2. If you expect 1, use ABS(divisor) or adjust formula logic. |

## Use Cases

### [[Alternating Patterns and Formatting]]

**Scenario:** Create alternating row colors, striped tables, or cycling patterns.

**Implementation:**
```
=MOD(ROW(), 2)                                 → 0/1 alternating
=MOD(ROW() - 1, 3)                             → 0/1/2 three-way cycle
=IF(MOD(ROW(), 2) = 0, "Gray", "White")        → Explicit color assignment
```

**Business Application:** Report formatting, dashboard design, data visualization. Alternating colors improve readability of long tables.

**Technical Details:** In conditional formatting, use formula `=MOD(ROW(), 2) = 0` to format even rows. Adjust for header rows by using `ROW() - HeaderCount`.

---

### [[Time and Date Component Extraction]]

**Scenario:** Extract hours, minutes, or seconds from time values; get time from datetime.

**Implementation:**
```
=MOD(SerialDateTime, 1)                        → Time portion only
=INT(MOD(TotalSeconds, 3600) / 60)             → Minutes from seconds
=MOD(TotalSeconds, 60)                         → Remaining seconds
=MOD(MonthNumber + 3, 12) + 1                  → Quarter-end month
```

**Business Application:** Time tracking, scheduling, duration calculations. Breaking down time into components for display or further calculation.

**Technical Details:** Excel times are decimals from 0 to 0.9999. MOD(datetime, 1) strips the date portion (integer) leaving just the time (decimal). Multiply by 24 for hours.

---

### [[Validation and Check Digits]]

**Scenario:** Validate credit card numbers, ISBN codes, or other check-digit algorithms.

**Implementation:**
```
=MOD(SUM(DigitArray), 10) = 0                  → Luhn validation
=MOD(WeightedSum, 11)                          → ISBN-10 check digit
=MOD(10 - MOD(Total, 10), 10)                  → Generate check digit
```

**Business Application:** Data entry validation, barcode verification, financial transaction validation. Catch typos and transcription errors.

**Technical Details:** Most check digit algorithms use MOD 10 or MOD 11. The nested MOD pattern `MOD(10 - MOD(x, 10), 10)` handles edge cases where the sum is already a multiple of 10.

---

### [[Cyclic Scheduling and Rotation]]

**Scenario:** Create rotating schedules, wrap-around calendars, or cyclic assignments.

**Implementation:**
```
=INDEX(Teams, MOD(WeekNumber - 1, TeamCount) + 1)  → Rotating team assignment
=MOD(Position + Steps - 1, TotalPositions) + 1     → Circular movement
=WEEKDAY(Date) = MOD(SomeValue, 7) + 1            → Match day of week
```

**Business Application:** Staff scheduling, shift rotation, resource allocation, game scheduling. Any repeating cycle benefits from MOD.

**Technical Details:** The -1 and +1 pattern converts between 0-indexed MOD results and 1-indexed lists. MOD returns 0 to n-1; add 1 for 1 to n range.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 1.0
- **Sign behavior:** Result has same sign as divisor (matches mathematical convention)
- **Decimal support:** Full support for non-integer arguments
- **Formula:** Internally uses `n - d * INT(n/d)`

### Google Sheets
- **Availability:** All versions
- **Sign behavior:** Same as Excel—result sign matches divisor
- **Decimal support:** Same as Excel
- **Formula:** Same internal calculation as Excel

### Both Platforms
- Identical behavior for positive numbers
- Same sign convention for mixed signs
- Same #DIV/0! error for zero divisor
- Same floating-point precision considerations

### Important Note on Programming Languages
- Python's `%` operator uses same convention as spreadsheet MOD
- JavaScript's `%` operator preserves dividend sign (different!)
- C/C++ `%` operator preserves dividend sign (different!)
- Be careful when porting formulas to/from code

## Tips and Best Practices

1. **Know the sign rule:** MOD result has the same sign as the divisor, not the dividend. MOD(-10, 3) = 2, MOD(10, -3) = -2. This is mathematically correct but surprises many.

2. **Use MOD for cycling:** The pattern `MOD(index - 1, count) + 1` cycles through values 1 to count. Essential for rotating schedules, circular lists, and wrap-around behavior.

3. **Extract time with MOD(datetime, 1):** DateTime values in Excel are integer (date) plus decimal (time). MOD strips the date, leaving just the time fraction.

4. **Check divisibility with MOD = 0:** `IF(MOD(A1, 5) = 0, ...)` tests if A1 is a multiple of 5. The cleanest divisibility check.

5. **Watch floating-point precision:** MOD(1, 0.1) might return 0.0999... instead of 0 due to binary representation of 0.1. Use ROUND(MOD(...), 10) for clean results with decimals.

6. **Combine with INT for quotient:** MOD gives remainder; INT(A/B) gives quotient. Together: `A = B * INT(A/B) + MOD(A, B)`.

7. **Adjust for 1-based indexing:** MOD returns 0 to n-1. For 1 to n range, use `MOD(x - 1, n) + 1`. The -1 before and +1 after handles the offset.

8. **Use for alternating patterns:** `MOD(ROW(), 2)` in conditional formatting creates striped rows. Adjust ROW() offset to align with your data.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[QUOTIENT]] | Integer quotient of division | When you need the whole number result, not remainder |
| [[INT]] | Round down to integer | Used in MOD's internal formula; also for floor division |
| [[TRUNC]] | Truncate toward zero | Similar to INT for positive numbers |

### Commonly Used Together

**[[INT]]** - Get quotient with remainder

*Complete division breakdown:*
```
Quotient:  =INT(A1/B1)
Remainder: =MOD(A1, B1)
```
Together they decompose division: A1 = B1 * INT(A1/B1) + MOD(A1, B1).

---

**[[ROW]]** - Alternating patterns

*Striped row formatting:*
```
=MOD(ROW(), 2)
=MOD(ROW() - HeaderRows, N)
```
Creates alternating or N-way cycling patterns by row.

---

**[[IF]]** - Conditional based on remainder

*Divisibility checks:*
```
=IF(MOD(A1, 2) = 0, "Even", "Odd")
=IF(MOD(A1, 5) = 0, "Multiple of 5", "")
```
Take action based on remainder value.

---

**[[INDEX]]** - Cycle through list

*Rotating selection:*
```
=INDEX(TeamList, MOD(WeekNum - 1, TeamCount) + 1)
```
MOD creates cycling index for INDEX lookup.

---

**[[ROUND]]** - Handle floating-point

*Clean decimal MOD:*
```
=ROUND(MOD(A1, 0.25), 10)
```
Eliminates floating-point noise in decimal modulo.

## Official Documentation

- **Microsoft Excel:** [MOD function](https://support.microsoft.com/en-us/office/mod-function-9b6cd169-b6ee-406a-a97b-edf2a9dc24f3)
- **Google Sheets:** [MOD function](https://support.google.com/docs/answer/3093497)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 1.0 (1985) | Original function |
| Excel 2007+ | All subsequent | No changes to behavior |
| Google Sheets | Original launch | Identical to Excel |
| LibreOffice Calc | All versions | Compatible implementation |

---

*Last updated: 2026-01-10*
