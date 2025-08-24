---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - logical
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-17
  - - aliases
    - []
  - - tags
    - []
---
# XOR

## XOR Description

Exclusive OR function that returns TRUE if an odd number of arguments are TRUE, FALSE if an even number (including zero) are TRUE. Used for mutually exclusive conditions where exactly one or an odd number of conditions should be true.

> [!f(x)] XOR Syntax
>
> ```spreadsheets
> XOR(logical1, logical2, [logical3], ...)
> ```
>
> **Parameters:**
> - `logical1` (required): First logical value or expression
> - `logical2` (required): Second logical value or expression
> - `logical3, ...` (optional): Additional logical values (up to 255 arguments)

> [!f(x)] XOR Examples
>
> ```spreadsheets
> // Basic exclusive OR
> XOR(A1>10, B1<5) → TRUE if exactly one condition is true, FALSE if both or neither
> 
> // Mutually exclusive options
> XOR(C2="Cash", D2="Credit", E2="Check") → TRUE if exactly one payment method selected
> 
> // Toggle validation
> XOR(F3, G3) → TRUE if exactly one of two boolean values is TRUE
> 
> // Multi-condition exclusivity
> XOR(H4="A", I4="B", J4="C", K4="D") → TRUE if odd number of conditions are TRUE
> 
> // Status conflict detection
> XOR(L5="Active", M5="Inactive", N5="Pending") → TRUE if exactly one or three statuses are true
> ```

## Use Cases

### [[Exclusive conditions]]
- **Mutually exclusive selections**: Ensure only one option is selected from multiple choices
- **Toggle states**: Validate that exactly one of two opposite states is active
- **Conflict detection**: Identify when multiple mutually exclusive conditions are simultaneously true
- **Single-choice validation**: Verify that users select exactly one option from a set of alternatives

### [[Data validation]]
- **Input consistency**: Check that related fields don't contain contradictory information
- **Business rule enforcement**: Ensure mutually exclusive business conditions are properly maintained
- **Quality control**: Flag records where multiple exclusive flags are incorrectly set to true
- **Form validation**: Validate that users make exactly one selection from exclusive options

## Related

### Similar Functions

- [[OR]] - Returns TRUE if any condition is true, inclusive logic
- [[AND]] - Returns TRUE only if all conditions are true
- [[NOT]] - Reverses logical values, often combined with XOR
- [[IF]] - Uses XOR results for exclusive conditional logic
- [[CHOOSE]] - Alternative for exclusive selection scenarios

## Commonly Used With Functions Examples

### XOR with Conditional Logic
Uses exclusive OR results to control mutually exclusive processing paths.

```spreadsheets
// Exclusive payment processing
=IF(XOR(O2="Cash", P2="Credit", Q2="Check"), "Valid Payment", "Payment Method Error")
// Ensures exactly one payment method is selected

// Toggle state management
=IF(XOR(R3, S3), "Valid Toggle", "Toggle Conflict")
// Validates that exactly one of two boolean states is active

// Mutually exclusive category assignment
=IF(XOR(T4="Premium", U4="Standard", V4="Basic"), "Category OK", "Category Conflict")
// Ensures exactly one category is assigned
```

### XOR with Validation Functions
Combines exclusive logic with data validation for comprehensive input checking.

```spreadsheets
// Form validation with exclusive options
=AND(NOT(ISBLANK(W5)), XOR(X5="Option A", Y5="Option B", Z5="Option C"))
// Requires input and exactly one option selected

// Status consistency validation
=XOR(AA6="Active", BB6="Inactive") AND NOT(OR(ISBLANK(AA6), ISBLANK(BB6)))
// Ensures exactly one status is selected and neither field is blank

// Exclusive flag validation
=IF(XOR(CC7, DD7, EE7), "Flags Valid", "Flag Configuration Error")
// Validates exclusive flag settings
```

### XOR with Mathematical Operations
Applies exclusive logic to numerical calculations and conditional mathematics.

```spreadsheets
// Exclusive bonus calculation
=IF(XOR(FF8>1000, GG8="VIP"), HH8*0.1, 0)
// Bonus only if high sales XOR VIP status, not both

// Mutually exclusive discount logic
=II9 * (1 - IF(XOR(JJ9>100, KK9="Member", LL9="Promo"), 0.1, 0))
// Applies 10% discount if exactly one condition is met

// Exclusive rate application
=MM10 * SWITCH(SUMPRODUCT(--(XOR(NN10="A", OO10="B", PP10="C"))), 1, 1.2, 0, 1.0)
// Different rate if exactly one category is selected
```
