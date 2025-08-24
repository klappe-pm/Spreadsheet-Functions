---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - engineering
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
# OCT2DEC

## OCT2DEC Description

Converts an octal (base-8) number to decimal (base-10) representation. Essential for Unix/Linux permission calculations, legacy system data conversion, and numerical computations requiring octal to decimal transformations in engineering applications.

> [!f(x)] OCT2DEC Syntax
>
> ```spreadsheets
> OCT2DEC(octal_number)
> ```
>
> **Parameters:**
> - `octal_number` (required): Octal number to convert (valid octal digits 0-7)

> [!f(x)] OCT2DEC Examples
>
> ```spreadsheets
> // Basic octal to decimal conversion
> OCT2DEC("17") → 15
> 
> // Single digit octal
> OCT2DEC("7") → 7
> 
> // Three-digit octal (common in permissions)
> OCT2DEC("755") → 493
> 
> // Maximum single byte octal
> OCT2DEC("377") → 255
> 
> // Zero conversion
> OCT2DEC("0") → 0
> ```

## Use Cases

### [[Unix/Linux permissions]]
- **File permission analysis**: Convert octal permission codes to decimal for mathematical operations
- **Access control calculations**: Analyze permission combinations using decimal arithmetic
- **System administration**: Calculate permission masks and access levels numerically
- **Security auditing**: Evaluate permission settings using decimal comparison operations

### [[Legacy system integration]]
- **Mainframe data conversion**: Convert octal data from legacy systems to decimal for modern processing
- **Historical data analysis**: Process archival data stored in octal format
- **Migration planning**: Calculate storage requirements and data ranges during system migrations
- **Compatibility analysis**: Evaluate numeric ranges and limits between octal and decimal systems

### [[Numerical computations]]
- **Address calculations**: Convert octal memory addresses to decimal for offset calculations
- **Data structure indexing**: Transform octal indices to decimal for array and table operations
- **Mathematical modeling**: Use decimal equivalents of octal values in engineering calculations
- **Range analysis**: Determine valid ranges and bounds using decimal arithmetic on octal inputs

## Related

### Similar Functions

- [[DEC2OCT]] - Converts decimal to octal, inverse operation
- [[OCT2BIN]] - Converts octal to binary, parallel base conversion
- [[OCT2HEX]] - Converts octal to hexadecimal, another base conversion
- [[HEX2DEC]] - Converts hexadecimal to decimal, similar base conversion
- [[BIN2DEC]] - Converts binary to decimal, related conversion function

## Commonly Used With Functions Examples

### Unix Permission Analysis
```spreadsheets
// Extract individual permission levels
=INT(OCT2DEC("755")/100) & " (owner), " & INT(MOD(OCT2DEC("755"), 100)/10) & " (group), " & MOD(OCT2DEC("755"), 10) & " (others)"
// Returns: "7 (owner), 5 (group), 5 (others)"

// Calculate total permission combinations
=OCT2DEC(owner_octal)*64 + OCT2DEC(group_octal)*8 + OCT2DEC(other_octal)
// Calculates total permission value in decimal

// Permission comparison and validation
=IF(OCT2DEC(current_perms) >= OCT2DEC(minimum_perms), "Access Granted", "Access Denied")
// Compares permissions using decimal arithmetic
```

### Mathematical Operations
```spreadsheets
// Arithmetic operations on octal inputs
=OCT2DEC(octal_value1) + OCT2DEC(octal_value2)
// Adds two octal numbers in decimal space

// Range and bounds checking
=IF(AND(OCT2DEC(input_octal) >= OCT2DEC(min_octal), OCT2DEC(input_octal) <= OCT2DEC(max_octal)), "Valid Range", "Out of Range")
// Validates octal input against decimal range

// Statistical analysis of octal data
=AVERAGE(OCT2DEC(A1:A10))
// Calculates average of octal values in decimal space
```
