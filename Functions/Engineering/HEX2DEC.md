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
# HEX2DEC

## HEX2DEC Description

Converts a hexadecimal (base-16) number to its decimal (base-10) equivalent. Essential for programming, memory address analysis, color code conversion, and debugging applications where hexadecimal representations need conversion to standard decimal format. Handles up to 10 hexadecimal digits.

> [!f(x)] HEX2DEC Syntax
>
> ```spreadsheets
> HEX2DEC(number)
> ```
>
> **Parameters:**
> - `number` (required): Hexadecimal number as text containing digits 0-9 and letters A-F (up to 10 characters)

> [!f(x)] HEX2DEC Examples
>
> ```spreadsheets
> // Basic hexadecimal to decimal conversions
> HEX2DEC("FF") → 255
> 
> // Single digit hex
> HEX2DEC("A") → 10
> HEX2DEC("F") → 15
> 
> // Common programming values
> HEX2DEC("100") → 256
> HEX2DEC("1000") → 4096
> 
> // Memory addresses
> HEX2DEC("FFFF") → 65535
> 
> // Color codes (RGB components)
> HEX2DEC("80") → 128
> 
> // Large hexadecimal numbers
> HEX2DEC("FFFFFFFF") → 4294967295
> ```

## Use Cases

### [[Programming and debugging]]
- **Memory address analysis**: Convert hexadecimal memory addresses to decimal for pointer arithmetic and memory calculations
- **Error code interpretation**: Transform hexadecimal error codes and status registers to decimal for lookup and debugging
- **Assembly language development**: Convert hex machine code instructions and operands to decimal for analysis
- **Checksum validation**: Convert hexadecimal checksums and hash values to decimal for verification algorithms

### [[Color code conversion]]
- **Web design**: Convert hexadecimal color codes (#FF0000) to decimal RGB values for color manipulation
- **Graphics programming**: Transform hex color values to decimal for image processing and color space calculations
- **UI/UX design**: Convert design system hex colors to decimal for mathematical color operations
- **Digital art applications**: Decode hex color palettes to decimal values for color analysis and matching

### [[Data analysis]]
- **Binary file analysis**: Convert hexadecimal file signatures and headers to decimal for format identification
- **Network protocol debugging**: Transform hex packet data and protocol fields to decimal for analysis
- **Embedded systems**: Convert hex configuration values and register settings to decimal for system programming
- **Cryptography**: Decode hexadecimal hash outputs and encryption keys to decimal for mathematical operations

## Related

### Similar Functions

- [[DEC2HEX]] - Converts decimal numbers to hexadecimal representation for programming and color codes
- [[BIN2DEC]] - Converts binary numbers to decimal for digital system analysis
- [[OCT2DEC]] - Converts octal numbers to decimal for legacy systems and file permissions
- [[HEX2BIN]] - Converts hexadecimal directly to binary for bitwise operations
- [[HEX2OCT]] - Converts hexadecimal to octal format for specific system applications

## Number Base Conversion Functions

### [[DEC2HEX]]
Complements HEX2DEC for bidirectional hexadecimal-decimal conversions. DEC2HEX enables round-trip validation and creation of hex patterns from decimal specifications.

```spreadsheets
// Round-trip validation
=HEX2DEC(DEC2HEX(255))
// Returns: 255 (validates conversion accuracy)

// Color code generation and verification
=DEC2HEX(HEX2DEC("FF")) = "FF"
// Returns: TRUE if conversion is lossless

// Memory address calculation
=DEC2HEX(HEX2DEC("1000") + HEX2DEC("FF"))
// Converts hex to decimal, adds, converts back to hex
```

### [[BIN2DEC]]  
Works with HEX2DEC for multi-base number system analysis. BIN2DEC enables comparison and validation across binary, decimal, and hexadecimal representations.

```spreadsheets
// Multi-base comparison
=HEX2DEC("FF") = BIN2DEC("11111111")
// Returns: TRUE (both equal 255)

// Bit manipulation verification
=BIN2DEC(DEC2BIN(HEX2DEC("A0")))
// Converts hex to decimal to binary and back

// Digital system cross-validation
=AND(HEX2DEC("80")=128, BIN2DEC("10000000")=128)
// Validates hex and binary representations match
```

## Programming Analysis Functions

### [[IF]]
Combined with HEX2DEC for conditional processing of hexadecimal data and validation of conversion results. IF enables range checking and error handling for hex input validation.

```spreadsheets
// Hexadecimal input validation
=IF(ISERROR(HEX2DEC(A1)), "Invalid hex", HEX2DEC(A1))
// Handles invalid hexadecimal input gracefully

// Memory address range validation
=IF(HEX2DEC(B1)>65535, "Address too high", "Valid address")
// Validates hex address within 16-bit range

// Color component validation
=IF(HEX2DEC(C1)<=255, "Valid RGB", "Invalid color value")
// Ensures hex color component is valid 8-bit value
```

### [[MID]]
Works with HEX2DEC for parsing hexadecimal strings and extracting specific components. MID enables segmentation of hex data for individual field analysis.

```spreadsheets
// RGB color component extraction
=HEX2DEC(MID(A1,2,2)) & "," & HEX2DEC(MID(A1,4,2)) & "," & HEX2DEC(MID(A1,6,2))
// Converts #RRGGBB to decimal RGB components

// Memory address segmentation
=HEX2DEC(MID(B1,1,4)) & ":" & HEX2DEC(MID(B1,5,4))
// Converts 8-digit hex to segment:offset format

// Protocol field extraction
=HEX2DEC(MID(C1,1,2)) & " type, " & HEX2DEC(MID(C1,3,4)) & " value"
// Extracts type and value fields from hex protocol data
```

## Color Processing Functions

### [[RGB]]
Combined with HEX2DEC for color code conversion and manipulation. RGB creates color values from decimal components extracted from hexadecimal color codes.

```spreadsheets
// Hex to RGB color conversion
=RGB(HEX2DEC(LEFT(A1,2)), HEX2DEC(MID(A1,3,2)), HEX2DEC(RIGHT(A1,2)))
// Converts RRGGBB hex code to RGB color

// Color brightness calculation
=(HEX2DEC(LEFT(B1,2))+HEX2DEC(MID(B1,3,2))+HEX2DEC(RIGHT(B1,2)))/3
// Calculates average brightness from hex color

// Color component analysis
=MAX(HEX2DEC(LEFT(C1,2)), HEX2DEC(MID(C1,3,2)), HEX2DEC(RIGHT(C1,2)))
// Finds dominant color component from hex
```

### [[CONCATENATE]]
Works with HEX2DEC for formatting hex conversion results and creating readable output strings. CONCATENATE enables professional presentation of conversion results.

```spreadsheets
// Memory address formatting
=CONCATENATE("Address: ", HEX2DEC(D1), " (0x", D1, ")")
// Shows both decimal and hex address representations

// Color code description
="RGB(" & HEX2DEC(LEFT(E1,2)) & "," & HEX2DEC(MID(E1,3,2)) & "," & HEX2DEC(RIGHT(E1,2)) & ")"
// Formats hex color as RGB string

// Error code interpretation
=CONCATENATE("Error ", HEX2DEC(F1), ": ", VLOOKUP(HEX2DEC(F1), G:H, 2, FALSE))
// Converts hex error code and looks up description
```

## Mathematical Processing Functions

### [[SUM]]
Combined with HEX2DEC to aggregate hexadecimal values after conversion to decimal. SUM enables statistical analysis of hex datasets and calculation of totals from hex-encoded data.

```spreadsheets
// Hexadecimal data aggregation
=SUM(HEX2DEC(G2:G10))
// Converts hex values to decimal and sums them

// Memory usage calculation
=SUM(HEX2DEC(H2:H20))*1024 & " bytes"
// Converts hex memory blocks to decimal and calculates total bytes

// Color brightness analysis
=SUM(HEX2DEC(LEFT(I2:I50,2)))/COUNT(I2:I50)
// Calculates average red component from hex colors
```

## Commonly Used With Functions Examples

### Color Code Analysis Dashboard
```spreadsheets
// Complete hex color breakdown
="Hex: #" & A1 & " | RGB: " & HEX2DEC(LEFT(A1,2)) & "," & 
 HEX2DEC(MID(A1,3,2)) & "," & HEX2DEC(RIGHT(A1,2)) & 
 " | Brightness: " & ROUND((HEX2DEC(LEFT(A1,2))+HEX2DEC(MID(A1,3,2))+HEX2DEC(RIGHT(A1,2)))/7.65,1) & "%"
// Converts hex color to RGB and calculates brightness percentage
```

### Memory Address Calculator
```spreadsheets
// Memory offset calculation
=IF(HEX2DEC(B2)>HEX2DEC(B1), 
    "Offset: " & (HEX2DEC(B2)-HEX2DEC(B1)) & " bytes (" & 
    DEC2HEX(HEX2DEC(B2)-HEX2DEC(B1)) & " hex)",
    "Invalid range")
// Calculates memory offset between two hex addresses
```

### Network Protocol Decoder
```spreadsheets
// Protocol header analysis
="Type: " & HEX2DEC(LEFT(C1,2)) & " | Length: " & HEX2DEC(MID(C1,3,4)) & 
 " | Checksum: " & HEX2DEC(RIGHT(C1,4)) & 
 IF(MOD(HEX2DEC(RIGHT(C1,4)),256)=0, " (Valid)", " (Invalid)")
// Decodes hex protocol header with validation
```

### Programming Debug Assistant
```spreadsheets
// Multi-base number display
="Dec: " & HEX2DEC(D1) & " | Hex: 0x" & D1 & " | Bin: " & 
 DEC2BIN(HEX2DEC(D1)) & " | Oct: " & DEC2OCT(HEX2DEC(D1))
// Shows number in all common programming bases
```

### Batch Hex Processing
```spreadsheets
// Hex data statistics
="Values: " & COUNT(E2:E100) & " | Total: " & SUM(HEX2DEC(E2:E100)) & 
 " | Average: " & ROUND(AVERAGE(HEX2DEC(E2:E100)),1) & 
 " | Max: " & MAX(HEX2DEC(E2:E100)) & " (0x" & DEC2HEX(MAX(HEX2DEC(E2:E100))) & ")"
// Comprehensive statistics for hex dataset with dual representation
```
