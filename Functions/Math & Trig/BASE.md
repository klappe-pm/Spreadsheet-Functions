---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - math & trig
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-19
  - - aliases
    - []
  - - tags
    - []
---
# BASE

## BASE Description

Converts a decimal number to a text representation in any base from 2 to 36. Supports binary, octal, hexadecimal, and custom bases with optional minimum length padding. Uses digits 0-9 and letters A-Z for bases greater than 10.

> [!f(x)] BASE Syntax
>
> ```spreadsheets
> BASE(number, radix, [min_length])
> ```
>
> **Parameters:**
> - `number` (required): Decimal number to convert (must be ≥ 0 and < 2^53)
> - `radix` (required): Base to convert to (integer from 2 to 36)
> - `min_length` (optional): Minimum length of result, padded with leading zeros

> [!f(x)] BASE Examples
>
> ```spreadsheets
> // Binary conversion
> BASE(10, 2) → "1010"
> 
> // Hexadecimal conversion
> BASE(255, 16) → "FF"
> 
> // Octal conversion
> BASE(64, 8) → "100"
> 
> // With minimum length padding
> BASE(10, 2, 8) → "00001010"
> 
> // Custom base conversion
> BASE(100, 36) → "2S"
> ```

## Use Cases

### [[Programming and development]]
- **Binary data analysis**: Convert decimal values to binary for bit manipulation and debugging
- **Memory address formatting**: Convert decimal addresses to hexadecimal for system programming
- **Color code generation**: Convert RGB values to hexadecimal for web development
- **Version number encoding**: Convert version numbers to custom bases for compact storage

### [[Data encoding and storage]]  
- **Compact identifiers**: Convert large decimal IDs to higher bases for shorter string representations
- **Hash generation**: Convert numeric hashes to alphanumeric strings for database keys
- **File naming**: Generate base-36 filenames from sequential numbers for filesystem organization
- **URL shortening**: Convert long numeric IDs to compact alphanumeric codes

### [[Mathematical analysis]]
- **Number theory**: Analyze number properties across different base representations
- **Cryptographic applications**: Convert numbers to different bases for encryption algorithms
- **Pattern recognition**: Identify patterns in number sequences across various bases
- **Educational demonstrations**: Show number system concepts and base conversion principles

## Related

### Similar Functions

- [[DECIMAL]] - Converts text in any base back to decimal number, inverse of BASE
- [[HEX2DEC]] - Converts hexadecimal to decimal (limited to base 16 only)
- [[BIN2DEC]] - Converts binary to decimal (limited to base 2 only)
- [[OCT2DEC]] - Converts octal to decimal (limited to base 8 only)
- [[TEXT]] - Formats numbers as text, but doesn't handle base conversion

## Number System Functions

### [[DECIMAL]]
BASE and DECIMAL are inverse functions, essential for bidirectional conversion between decimal and any base system.

```spreadsheets
// Verify round-trip conversion
=DECIMAL(BASE(42, 16), 16) → 42

// Data validation
=IF(DECIMAL(BASE(A1, B1), B1)=A1, "Valid conversion", "Error")

// Base conversion workflow
=A1 & " (base 10) = " & BASE(A1, 16) & " (base 16)"
```

### [[HEX2DEC]]
BASE provides more flexibility than HEX2DEC by supporting custom padding and working with the broader base conversion system.

```spreadsheets
// Enhanced hexadecimal formatting
=BASE(255, 16, 4)  // "00FF" with padding
=HEX2DEC("FF")     // 255 (limited functionality)

// Color code processing
=BASE(A1, 16, 2) & BASE(B1, 16, 2) & BASE(C1, 16, 2)
// Creates 6-digit hex color code from RGB values

// Memory address formatting
="0x" & BASE(C1, 16, 8)
// Creates standard memory address format
```

## Text Processing Functions

### [[LEN]]
Used with BASE to analyze and validate converted string lengths, particularly important for fixed-width encodings.

```spreadsheets
// Ensure minimum bit width
=BASE(D1, 2, MAX(8, LEN(BASE(D1, 2))))
// Ensures at least 8-bit representation

// Analyze conversion efficiency
="Original: " & D1 & " chars, Base36: " & LEN(BASE(D1, 36)) & " chars"

// Padding validation
=IF(LEN(BASE(E1, 16, 4))=4, "Formatted correctly", "Check padding")
```

### [[UPPER]]
Often combined with BASE since hexadecimal and higher bases use uppercase letters by default, ensuring consistent formatting.

```spreadsheets
// Consistent uppercase formatting
=UPPER(BASE(F1, 16))  // Ensures uppercase hex

// Case standardization
=UPPER(BASE(G1, 36))  // Uppercase base-36 encoding

// Format comparison
="Std: " & BASE(H1, 16) & " | Upper: " & UPPER(BASE(H1, 16))
```

## Conditional Logic Functions

### [[IF]]
Essential for validating inputs and implementing conditional base conversion logic based on data ranges or types.

```spreadsheets
// Input validation
=IF(AND(I1>=0, I1<2^53), BASE(I1, J1), "Number out of range")

// Conditional base selection
=IF(I1<256, BASE(I1, 16), BASE(I1, 36))
// Use hex for small numbers, base-36 for larger

// Format selection based on magnitude
=IF(K1<1000, BASE(K1, 10), BASE(K1, 36))
```

## Commonly Used With Functions Examples

### Programming and Development
```spreadsheets
// Complete color code generator
="Color: #" & BASE(L1, 16, 2) & BASE(M1, 16, 2) & BASE(N1, 16, 2) & " (R:" & L1 & ", G:" & M1 & ", B:" & N1 & ")"

// Memory address with validation
=IF(O1>=0, "Address: 0x" & BASE(O1, 16, 8), "Invalid address")

// Binary analysis with bit count
="Binary: " & BASE(P1, 2) & " (" & LEN(BASE(P1, 2)) & " bits, value: " & P1 & ")"
```

### Data Encoding and Identifiers
```spreadsheets
// Compact ID generation
="ID: " & BASE(Q1, 36, 4) & " (from " & Q1 & ")"

// Multi-base representation
=Q1 & " = " & BASE(Q1, 2) & "₂ = " & BASE(Q1, 8) & "₈ = " & BASE(Q1, 16) & "₁₆"

// URL-safe encoding
="Code: " & SUBSTITUTE(BASE(R1, 36), "0", "O") & " (original: " & R1 & ")"
```

### Educational and Analysis
```spreadsheets
// Number system comparison
="Decimal " & S1 & " in different bases: Bin=" & BASE(S1, 2) & ", Oct=" & BASE(S1, 8) & ", Hex=" & BASE(S1, 16)

// Pattern analysis
="Base " & T1 & ": " & BASE(U1, T1) & " (length: " & LEN(BASE(U1, T1)) & ", efficiency: " & ROUND(LEN(TEXT(U1, "0"))/LEN(BASE(U1, T1)), 2) & ")"

// Conversion verification
="Round-trip test: " & V1 & " → " & BASE(V1, W1) & " → " & DECIMAL(BASE(V1, W1), W1) & " (Match: " & IF(V1=DECIMAL(BASE(V1, W1), W1), "✓", "✗") & ")"
```
