---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- logical
subTopics:
- conditional-logic
- boolean-operations
- negation
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Logical Not
- Boolean Negation
- Inverse Boolean
tags:
- logical
- conditional
- boolean
- negation
- invert
---

# NOT

## Description

**NOT** is the simplest of the logical functions, yet surprisingly powerful. It takes a single logical value and flips it: TRUE becomes FALSE, and FALSE becomes TRUE. Think of NOT as a logical toggle switch or a "reverse" button. While AND and OR combine multiple conditions, NOT transforms a single condition into its opposite. This inversion capability is essential when your logic is more naturally expressed as "everything except X" rather than listing all the things you want.

The real utility of NOT emerges when combined with IF, AND, and OR. Consider checking if a cell is NOT empty: `=IF(NOT(ISBLANK(A1)), "Has Data", "Empty")`. Or ensuring a record is NOT in an exclusion list: `=IF(NOT(OR(A1="Cancelled", A1="Deleted", A1="Archived")), "Active", "Inactive")`. Sometimes it's far easier to define what you want to exclude than to enumerate everything you want to include. NOT lets you express that exclusion elegantly.

**NOT's truth table is trivial but fundamental:** NOT(TRUE) = FALSE. NOT(FALSE) = TRUE. That's it. But this simple inversion combines with AND and OR to create De Morgan's Laws: NOT(AND(A,B)) equals OR(NOT(A), NOT(B)), and NOT(OR(A,B)) equals AND(NOT(A), NOT(B)). Understanding these equivalences helps you restructure complex conditions. If your formula using NOT and AND seems convoluted, there's likely a cleaner OR formulation (or vice versa).

**Type coercion matters:** NOT interprets numbers as Boolean before inverting. Zero (0) is FALSE, so NOT(0) returns TRUE. Any non-zero number is TRUE, so NOT(1), NOT(-5), and NOT(100) all return FALSE. Empty cells are also treated as FALSE (so NOT of empty = TRUE), which can cause unexpected results. Always be explicit about what you're testing: use NOT(A1=0) rather than NOT(A1) if you specifically want to check for zero.

## Syntax

> [!f(x)] NOT Syntax
>
> ```
> =NOT(logical)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `logical` | Yes | Any value or expression that evaluates to TRUE or FALSE. Can be a comparison (A1>10), a logical function (ISBLANK(A1)), a cell containing TRUE/FALSE, or a number (0=FALSE, non-zero=TRUE). |

### Return Value

Returns FALSE if the argument is TRUE. Returns TRUE if the argument is FALSE. If the argument cannot be interpreted as a logical value, returns a #VALUE! error.

### NOT Truth Table

| Input | NOT Result |
|-------|------------|
| TRUE | **FALSE** |
| FALSE | **TRUE** |
| 0 | **TRUE** (0 = FALSE, so NOT gives TRUE) |
| 1 (or any non-zero) | **FALSE** (non-zero = TRUE, so NOT gives FALSE) |
| Empty cell | **TRUE** (empty = FALSE, so NOT gives TRUE) |

## Examples

> [!f(x)] NOT Examples

### Example 1: Basic Boolean Inversion
```
=NOT(TRUE)
```
**Result:** FALSE

**Explanation:** The most basic NOT operation. TRUE becomes FALSE. Rarely used with a literal TRUE, but foundational for understanding the function.

---

### Example 2: NOT with Comparison
```
=NOT(A1>100)
```
**Result:** TRUE if A1 is 100 or less

**Explanation:** Instead of writing A1<=100, you can invert A1>100. Both are equivalent. NOT can make complex comparisons more readable when the positive condition is simpler to express.

---

### Example 3: NOT with IF for Non-Empty Check
```
=IF(NOT(ISBLANK(A1)), "Has Value", "Empty")
```
**Result:** "Has Value" if A1 contains anything

**Explanation:** ISBLANK returns TRUE for empty cells. NOT inverts it to TRUE for non-empty cells. While you could write IF(ISBLANK(A1), "Empty", "Has Value"), NOT makes the "has value" case the primary focus.

---

### Example 4: Exclusion Logic with NOT and OR
```
=IF(NOT(OR(B2="Inactive", B2="Suspended", B2="Terminated")), "Active User", "Inactive User")
```
**Result:** "Active User" unless status is one of the excluded values

**Explanation:** Rather than listing all possible active statuses, list the inactive ones and negate the whole group. If status is NOT any of the excluded values, the user is active. This pattern scales well when there are many valid values but few invalid ones.

---

### Example 5: NOT with AND for Incomplete Check
```
=IF(NOT(AND(A2<>"", B2<>"", C2<>"")), "Missing Fields", "Complete")
```
**Result:** "Missing Fields" if ANY field is empty

**Explanation:** AND returns TRUE only if all fields are non-empty. NOT inverts this: if NOT all fields are filled, something is missing. Equivalent to OR(A2="", B2="", C2="") but reads more naturally as "not complete".

---

### Example 6: Double Negation (Identity)
```
=NOT(NOT(A1))
```
**Result:** Same as A1 (when A1 is TRUE/FALSE)

**Explanation:** Two NOTs cancel out. NOT(NOT(TRUE))=TRUE, NOT(NOT(FALSE))=FALSE. While seemingly useless, this pattern can coerce values to Boolean: NOT(NOT(A1)) forces A1 to TRUE/FALSE even if it contains a number.

---

### Example 7: NOT with ISERROR for Success Check
```
=IF(NOT(ISERROR(VLOOKUP(A1, Data, 2, 0))), VLOOKUP(A1, Data, 2, 0), "Not Found")
```
**Result:** The looked-up value if found, "Not Found" otherwise

**Explanation:** ISERROR returns TRUE if VLOOKUP fails. NOT inverts this to TRUE on success. This pattern checks if an operation succeeded before using its result. Note: IFERROR is cleaner for this specific case.

---

### Example 8: Boolean Algebra - De Morgan's Law
```
=NOT(AND(A1, B1))
```
is equivalent to:
```
=OR(NOT(A1), NOT(B1))
```
**Result:** Both return TRUE if either A1 or B1 is FALSE

**Explanation:** De Morgan's Law: the negation of an AND equals the OR of negations. This helps restructure complex conditions. If your NOT(AND(...)) is hard to read, convert to OR(NOT(...), NOT(...)) or vice versa.

---

### Example 9: NOT with ISNUMBER for Text Detection
```
=IF(NOT(ISNUMBER(A1)), "Text or Empty", "Number")
```
**Result:** "Text or Empty" if A1 is not a number

**Explanation:** ISNUMBER returns TRUE only for numeric values. NOT inverts this to identify text, Booleans, errors, or empty cells. Useful for data validation before calculations.

---

### Example 10: Inverting Error States
```
=NOT(ISNA(MATCH(A1, ValidList, 0)))
```
**Result:** TRUE if A1 is found in ValidList

**Explanation:** MATCH returns #N/A if not found; ISNA detects this. NOT inverts: TRUE means found, FALSE means not found. This converts MATCH's error behavior into a clean Boolean for use in other logic.

---

### Example 11: NOT with Date Comparisons
```
=IF(NOT(A1>TODAY()), "Past or Present", "Future")
```
**Result:** "Past or Present" for today or earlier dates

**Explanation:** A1>TODAY() is TRUE for future dates. NOT inverts to TRUE for today or past dates. Equivalent to A1<=TODAY() but may read more naturally in certain contexts.

---

### Example 12: Checkbox/Boolean Toggle
```
=NOT(A1)
```
**Result:** The opposite of whatever Boolean A1 contains

**Explanation:** When A1 contains TRUE or FALSE (from a checkbox or logical formula), NOT flips it. Useful in toggle scenarios or when one cell should always be the opposite of another.

---

### Example 13: Conditional Formatting Logic
```
=NOT(MOD(ROW(),2)=0)
```
**Result:** TRUE for odd rows, FALSE for even rows

**Explanation:** MOD(ROW(),2)=0 identifies even rows. NOT inverts to identify odd rows. Use in conditional formatting to alternate row colors or in formulas to process every other row.

---

### Example 14: NOT with Nested Logical Functions
```
=IF(AND(NOT(A1=""), NOT(B1=""), OR(C1>0, D1>0)), "Valid", "Invalid")
```
**Result:** "Valid" if A1 and B1 are non-empty AND either C1 or D1 is positive

**Explanation:** Complex validation combining NOT, AND, and OR. Both required fields (A1, B1) must be non-empty AND at least one of the optional numeric fields must be positive.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Passing text that cannot be interpreted as Boolean | NOT requires a logical value. Pass a comparison (A1="text") instead of just text ("text"). |
| `Unexpected TRUE` | Empty cells or zeros being treated as FALSE | NOT(empty) = TRUE, NOT(0) = TRUE. Be explicit: NOT(A1="") for text, NOT(A1=0) for numbers. |
| `Unexpected FALSE` | Non-zero numbers treated as TRUE | NOT(any non-zero) = FALSE. NOT(5) = FALSE. Check if you meant NOT(A1=5) instead of NOT(A1). |
| `Logical confusion` | Misunderstanding De Morgan's Laws | NOT(AND(A,B)) = OR(NOT(A), NOT(B)). NOT(OR(A,B)) = AND(NOT(A), NOT(B)). Test with concrete values. |
| `Redundant nesting` | Using NOT when simpler comparison exists | NOT(A1>5) is just A1<=5. NOT(A1=B1) is just A1<>B1. Use NOT for readability, not complexity. |

## Use Cases

### [[Access Control Exclusion]]

**Scenario:** A system grants access by default but needs to deny it to users who are on a blacklist, suspended, or from restricted regions.

**Implementation:**
```
=IF(NOT(OR(COUNTIF(Blacklist, A2)>0, B2="Suspended", COUNTIF(RestrictedRegions, C2)>0)), "Access Granted", "Access Denied")
```

**Business Application:** Security systems often work by exclusion rather than inclusion. It's easier to maintain a list of who CANNOT access than to update permissions for every legitimate user. The NOT pattern inverts the exclusion check into an access decision.

**Technical Details:** Uses COUNTIF to check against named ranges (Blacklist, RestrictedRegions). The OR combines multiple exclusion criteria. NOT inverts the combined result so TRUE means access is allowed. Easy to add new exclusion criteria without restructuring the formula.

---

### [[Data Validation Inversion]]

**Scenario:** A data import process should flag records that do NOT meet all quality criteria: non-empty required fields, valid date format, and numeric values within range.

**Implementation:**
```
=IF(NOT(AND(A2<>"", ISNUMBER(DATEVALUE(B2)), C2>=0, C2<=100)), "Flagged for Review", "Valid")
```

**Business Application:** Quality control often focuses on finding problems. By defining what "valid" looks like and negating it, you efficiently identify records needing attention. This approach ensures completeness: anything not meeting the strict valid criteria gets flagged.

**Technical Details:** AND inside NOT means failure of ANY criterion triggers the flag. DATEVALUE converts text to date (errors if invalid format). Range check for C2 ensures values are 0-100. Add IFERROR if DATEVALUE might fail.

---

### [[Toggle State Management]]

**Scenario:** A project tracking sheet has a "Complete" checkbox. A separate column should automatically show the opposite ("Incomplete" when unchecked, "Complete" when checked) for reporting purposes.

**Implementation:**
```
=IF(A2, "Complete", "In Progress")
```
Alternative toggling formula:
```
=NOT(A2)
```
Where A2 contains TRUE/FALSE from a checkbox.

**Business Application:** Checkboxes in modern spreadsheets return TRUE/FALSE. NOT provides a simple way to create inverse states. One checkbox can drive multiple display variations: the original state, its inverse, or conditional text based on either.

**Technical Details:** Google Sheets checkboxes return TRUE (checked) or FALSE (unchecked). Excel linked checkboxes work similarly. NOT(A2) in the adjacent column always shows the opposite state. Useful for "Show Incomplete Only" filters.

---

### [[Availability Window Detection]]

**Scenario:** A scheduling system needs to identify time slots that are NOT during standard business hours (9 AM - 5 PM) or NOT on weekdays.

**Implementation:**
```
=IF(NOT(AND(HOUR(A2)>=9, HOUR(A2)<17, WEEKDAY(A2,2)<=5)), "After Hours", "Business Hours")
```

**Business Application:** Identifying after-hours slots for special pricing, overtime calculation, or scheduling restrictions. The NOT pattern clearly expresses "everything outside normal hours" without listing all the after-hours possibilities.

**Technical Details:** AND requires all conditions (hour in range AND weekday). NOT inverts: if NOT all conditions are met, it's after hours. WEEKDAY mode 2 returns 1-5 for Monday-Friday. Adjust hour boundaries for different business hours.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 97 onward)
- **Numeric handling:** 0 = FALSE, non-zero = TRUE before NOT inverts
- **Empty cells:** Treated as FALSE, so NOT(empty) = TRUE
- **Array behavior:** In Excel 365, can use NOT with arrays: `=NOT(A1:A10>0)` returns array of inverted values
- **Case sensitivity:** When used with text comparisons, inherits Excel's case-insensitivity

### Google Sheets
- **Availability:** All versions
- **Numeric handling:** Same as Excel: 0 = FALSE, non-zero = TRUE
- **Empty cells:** Treated as FALSE, so NOT(empty) = TRUE
- **Array behavior:** Native array support: `=NOT(A1:A10>0)` returns array of inverted values
- **Case sensitivity:** When used with text comparisons, inherits Sheets' case-sensitivity

### Key Difference Alert
NOT behavior is nearly identical between platforms. The main difference is inherited from the comparison operators used within NOT: text comparisons like NOT(A1="Yes") follow each platform's case-sensitivity rules. Use UPPER() or LOWER() in cross-platform spreadsheets.

## Tips and Best Practices

1. **Use NOT for cleaner negation:** Instead of A1<=5, sometimes NOT(A1>5) reads more naturally, especially when the positive condition is what you're focusing on. Choose whichever is clearer in context.

2. **Combine NOT with OR for exclusion lists:** When you have a few values to exclude from many valid values, use NOT(OR(A1="Bad1", A1="Bad2")) instead of listing all good values.

3. **Watch for empty cell surprises:** NOT(empty cell) = TRUE because empty is treated as FALSE. If blanks should be treated as "unknown" rather than FALSE, add explicit handling: AND(A1<>"", NOT(A1=0)).

4. **Remember De Morgan's Laws:** NOT(AND(A,B)) = OR(NOT(A), NOT(B)). If your NOT(AND(...)) is confusing, rewrite using OR with individual NOTs, or vice versa.

5. **Avoid double negatives when possible:** NOT(NOT(A1)) equals A1 for Boolean values. Double negatives are valid but confusing. Simplify when you can.

6. **Use NOT(ISERROR()) carefully:** While common, IFERROR is usually cleaner for error handling. NOT(ISERROR(formula)) tests for success, but IFERROR(formula, alternate) handles errors in one step.

7. **Type coercion with double NOT:** NOT(NOT(A1)) forces any value to TRUE or FALSE. Useful when you need a guaranteed Boolean from a cell that might contain numbers, text, or be empty.

8. **Test edge cases explicitly:** NOT's behavior with 0, empty, and non-zero values can surprise. Before deploying, test with: empty cell, 0, 1, -1, text, TRUE, FALSE, and error values.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[AND]] | Returns TRUE if ALL conditions are TRUE | When combining conditions, not inverting a single one |
| [[OR]] | Returns TRUE if ANY condition is TRUE | When checking alternatives, not negation |
| [[XOR]] | Returns TRUE if ODD number of conditions are TRUE | For exclusive-or logic requiring specific TRUE count |
| [[IF]] | Returns one value for TRUE, another for FALSE | NOT typically works inside IF's logical_test |

### Commonly Used Together

**[[IF]]** - Returns different values based on condition

*Inverting a condition for clearer logic:*
```
=IF(NOT(ISBLANK(A1)), A1*2, 0)
```
Calculate only if cell is NOT blank. NOT makes the "action" case the TRUE branch.

---

**[[AND]]** - Returns TRUE if all conditions are TRUE

*Negating a combined condition:*
```
=IF(NOT(AND(A1>0, B1>0, C1>0)), "Has Non-Positive", "All Positive")
```
If NOT all are positive, at least one is zero or negative. De Morgan's equivalent: OR(A1<=0, B1<=0, C1<=0).

---

**[[OR]]** - Returns TRUE if any condition is TRUE

*Negating an alternative set:*
```
=IF(NOT(OR(Status="Closed", Status="Cancelled")), "Open", "Ended")
```
If status is NOT Closed or Cancelled, it's still open. Cleaner than listing all open statuses.

---

**[[ISBLANK]]** - Returns TRUE if cell is empty

*Checking for non-empty cells:*
```
=NOT(ISBLANK(A1))
```
TRUE if A1 contains any value. Common pattern for required field validation.

---

**[[ISERROR]]** - Returns TRUE if value is any error

*Checking for successful operations:*
```
=IF(NOT(ISERROR(VLOOKUP(A1, Range, 2, 0))), "Found", "Not Found")
```
If VLOOKUP did NOT error, the value was found. Consider IFERROR as a cleaner alternative.

---

**[[ISNUMBER]]** - Returns TRUE if value is numeric

*Checking for non-numeric values:*
```
=NOT(ISNUMBER(A1))
```
TRUE if A1 contains text, Boolean, error, or is empty. Useful for data type validation.

## Official Documentation

- **Microsoft Excel:** [NOT function](https://support.microsoft.com/en-us/office/not-function-9cfc6011-a054-40c7-a140-cd4ba2d87d77)
- **Google Sheets:** [NOT function](https://support.google.com/docs/answer/3093305)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 2.0 (1987) | One of the original logical functions |
| Excel 2007+ | All subsequent | No changes to basic function |
| Excel 365 | Dynamic arrays | Native array support without CSE |
| Google Sheets | Original launch | Identical core functionality |

---

*Last updated: 2026-01-10*
