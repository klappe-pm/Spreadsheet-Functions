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
# OCT2BIN

## OCT2BIN Description

Converts an octal (base-8) number to binary (base-2) representation. Essential for digital system design, computer architecture analysis, and number system conversions in engineering applications requiring octal to binary transformations.

> [!f(x)] OCT2BIN Syntax
>
> ```spreadsheets
> OCT2BIN(octal_number, [places])
> ```
>
> **Parameters:**
> - `octal_number` (required): Octal number to convert (0-777 for positive, or -400 to 377 for negative)
> - `places` (optional): Number of characters to use for the result (pads with leading zeros)

> [!f(x)] OCT2BIN Examples
>
> ```spreadsheets
> // Basic octal to binary conversion
> OCT2BIN("17") → "1111"
> 
> // Single digit octal
> OCT2BIN("7") → "111"
> 
> // With leading zeros specified
> OCT2BIN("12", 8) → "00001010"
> 
> // Maximum positive octal value
> OCT2BIN("777") → "111111111"
> 
> // Zero conversion
> OCT2BIN("0") → "0"
> ```

## Use Cases

### [[Digital system design]]
- **Address decoding**: Convert octal addresses to binary for memory and I/O decoding circuits
- **Permission systems**: Transform Unix-style octal permissions to binary representations for analysis
- **Microprocessor programming**: Convert octal instruction codes to binary for assembly language programming
- **Data bus analysis**: Analyze octal-encoded data bus signals in binary format for debugging

### [[Number system analysis]]
- **Base conversion verification**: Verify octal to binary conversions in computer science education
- **Digital logic design**: Convert truth table inputs from octal notation to binary for logic gate analysis
- **Error detection**: Analyze bit patterns by converting from compact octal to binary representation
- **Data compression analysis**: Study bit patterns in data compression algorithms using octal-binary conversions

### [[Legacy system integration]]
- **Mainframe data conversion**: Convert legacy octal data formats to binary for modern system integration
- **Historical computer analysis**: Analyze historical computer architectures that used octal numbering
- **Documentation translation**: Convert technical documentation from octal to binary representations
- **System migration**: Transform octal configuration data to binary for system upgrades

## Related

### Similar Functions

- [[OCT2DEC]] - Converts octal to decimal, alternative base conversion
- [[OCT2HEX]] - Converts octal to hexadecimal, another common base conversion
- [[BIN2OCT]] - Converts binary to octal, inverse operation
- [[DEC2BIN]] - Converts decimal to binary, related base conversion
- [[HEX2BIN]] - Converts hexadecimal to binary, parallel conversion function

## Base Conversion Functions

### [[BIN2OCT]]
Inverse operation of OCT2BIN, used for round-trip conversion verification and bidirectional number system transformations.

```spreadsheets
// Verify round-trip conversion
=BIN2OCT(OCT2BIN("17")) = "17"
// Returns: TRUE (verifies conversion accuracy)

// Convert through binary for validation
=OCT2BIN("25") = "10101"
=BIN2OCT("10101") = "25"
// Confirms bidirectional conversion consistency

// Multi-step conversion chain
=BIN2OCT(OCT2BIN(original_octal))
// Should return original_octal value
```

### [[OCT2DEC]]
Used with OCT2BIN for multi-base number system analysis and conversion verification.

```spreadsheets
// Verify conversion consistency through decimal
=OCT2DEC("17") = 15  // Decimal equivalent
=DEC2BIN(15) = OCT2BIN("17")  // Both equal "1111"
// Confirms conversion accuracy across number systems

// Address space calculations
=OCT2DEC(octal_address) & " decimal = " & OCT2BIN(octal_address) & " binary"
// Shows address in multiple formats for debugging

// Permission analysis (Unix octal permissions)
="Permission " & octal_perm & " = " & OCT2DEC(octal_perm) & " decimal = " & OCT2BIN(octal_perm) & " binary"
// Analyzes file permissions in multiple number bases
```

## Data Processing Functions

### [[LEN]]
Used with OCT2BIN to analyze the length of binary representations for data formatting and validation.

```spreadsheets
// Analyze binary length from octal input
=LEN(OCT2BIN(octal_value))
// Returns number of bits in binary representation

// Ensure minimum bit width
=OCT2BIN(octal_data, MAX(LEN(OCT2BIN(octal_data)), required_bits))
// Pads binary result to required minimum width

// Calculate storage requirements
="Octal " & octal_num & " requires " & LEN(OCT2BIN(octal_num)) & " bits"
// Analyzes storage requirements for binary representation
```

### [[RIGHT]] and [[LEFT]]
Used with OCT2BIN to extract specific bit fields from binary representations for digital signal analysis.

```spreadsheets
// Extract least significant bits
=RIGHT(OCT2BIN(octal_data, 8), 4)
// Gets last 4 bits of 8-bit binary representation

// Extract most significant bits
=LEFT(OCT2BIN(octal_data, 8), 4)
// Gets first 4 bits of 8-bit binary representation

// Bit field extraction for register analysis
=MID(OCT2BIN(register_value, 12), start_bit, num_bits)
// Extracts specific bit fields from register values
```

## Commonly Used With Functions Examples

### Digital Logic Analysis
```spreadsheets
// Truth table generation from octal inputs
=OCT2BIN(ROW()-1, 3)  // For rows 1-8, generates 3-bit binary patterns
// Creates truth table inputs: 000, 001, 010, 011, 100, 101, 110, 111

// Logic gate input analysis
=LEFT(OCT2BIN(input_combination, 3), 1) & MID(OCT2BIN(input_combination, 3), 2, 1) & RIGHT(OCT2BIN(input_combination, 3), 1)
// Separates 3-bit binary into individual logic inputs A, B, C

// State machine state encoding
="State " & state_octal & ": " & OCT2BIN(state_octal, state_bits) & " (binary encoding)"
// Documents state machine states in both octal and binary formats
```

### Memory and Addressing Systems
```spreadsheets
// Memory address decoding
=IF(LEFT(OCT2BIN(address_octal, 16), 3)="001", "ROM", IF(LEFT(OCT2BIN(address_octal, 16), 3)="010", "RAM", "I/O"))
// Decodes memory type from octal address using binary representation

// Bit masking operations
=AND(OCT2DEC(data_octal), OCT2DEC(mask_octal)) & " = " & DEC2BIN(AND(OCT2DEC(data_octal), OCT2DEC(mask_octal)))
// Performs bit masking and shows result in binary

// Address bus analysis
="Address " & addr_octal & " drives lines: " & SUBSTITUTE(OCT2BIN(addr_octal, 16), "1", "HIGH ") & SUBSTITUTE(OCT2BIN(addr_octal, 16), "0", "LOW ")
// Shows which address lines are driven high or low
```
