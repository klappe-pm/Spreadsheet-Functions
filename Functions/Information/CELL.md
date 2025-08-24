---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - information
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
# CELL

## CELL Description

Returns specific information about the formatting, location, or contents of a cell based on the info_type parameter. Essential for dynamic formatting analysis, location tracking, and conditional processing based on cell properties and attributes.

> [!f(x)] CELL Syntax
>
> ```spreadsheets
> CELL(info_type, [reference])
> CELL(info_type, cell_reference)
> ```
>
> **Parameters:**
> - `info_type` (required): Text string specifying the type of information to return
> - `reference` (optional): Cell reference to analyze; defaults to last changed cell if omitted

> [!f(x)] CELL Examples
>
> ```spreadsheets
> // Get cell address
> CELL("address", A5) → "$A$5" (absolute reference)
> 
> // Check cell formatting
> CELL("format", B10) → "F2" (number format with 2 decimals)
> 
> // Get cell contents
> CELL("contents", C15) → actual value in cell C15
> 
> // Find column number
> CELL("col", D20) → 4 (column D is 4th column)
> 
> // Check if cell is protected
> CELL("protect", E25) → 1 (if protected) or 0 (if unprotected)
> ```

## Use Cases

### [[Dynamic cell analysis]]
- **Format detection**: Identify number formats, currency symbols, and decimal places applied to cells for consistent reporting
- **Location tracking**: Determine cell addresses and coordinates for dynamic range generation and formula construction
- **Protection status**: Check cell protection settings before allowing data entry or modification operations
- **Content analysis**: Examine cell values and types for validation and processing decisions

### [[Conditional formatting]]
- **Format-based logic**: Apply different processing based on existing cell formatting and display properties
- **Style consistency**: Ensure formatting consistency across worksheets and workbooks through programmatic checking
- **Template validation**: Verify that template cells have correct formatting before data entry or distribution
- **Report standardization**: Maintain formatting standards across multiple reports and data presentations

### [[Automation workflows]]
- **Dynamic range building**: Construct cell ranges and references based on current cell positions and properties
- **Worksheet navigation**: Track and manage current cell positions for interactive applications and user interfaces
- **Data validation**: Verify cell properties meet requirements before processing or calculations
- **Quality assurance**: Ensure cells meet formatting and protection standards in automated workflows

## Related

### Similar Functions

- [[TYPE]] - Returns numeric data type codes, complementing CELL's detailed formatting information
- [[ISBLANK]] - Checks for empty cells, used with CELL for comprehensive cell state analysis
- [[INFO]] - Returns system and environment information, broader scope than CELL's specific cell properties
- [[ROW]] - Returns row number, simpler alternative to CELL("row") for basic positioning
- [[COLUMN]] - Returns column number, simpler alternative to CELL("col") for basic positioning

## Cell Property Functions

### [[ADDRESS]]
CELL can return cell addresses, working with ADDRESS function for dynamic reference creation and cell coordinate management.

```spreadsheets
// Dynamic address generation
=CELL("address", A1) → "$A$1"
// Returns absolute address of specified cell

// Compare with ADDRESS function
=ADDRESS(CELL("row", B5), CELL("col", B5)) → "$B$5"
// Reconstructs address using CELL-derived coordinates

// Dynamic range construction
=CELL("address", A1) & ":" & CELL("address", INDEX(A:A, COUNTA(A:A)))
// Creates range from A1 to last non-empty cell in column A
```

### [[ROW]]
CELL("row") provides row numbers, complementing ROW function for position analysis and dynamic formula construction.

```spreadsheets
// Row position analysis
=CELL("row", C10) → 10
// Returns row number of specified cell

// Dynamic row calculations
=IF(CELL("row", INDIRECT("A" & ROW()))<10, "Header area", "Data area")
// Categorizes cells based on row position

// Row-based conditional formatting
=IF(CELL("row", A1)=1, "Title formatting", "Data formatting")
// Applies different formatting based on row position
```

## Formatting Functions

### [[TEXT]]
CELL provides format information that can guide TEXT function formatting decisions and ensure consistent number presentation.

```spreadsheets
// Format-aware text conversion
=IF(CELL("format", A2)="C2", TEXT(A2, "$#,##0.00"), TEXT(A2, "0.00"))
// Applies currency or number formatting based on cell format

// Dynamic format preservation
=TEXT(B3, IF(CELL("format", B3)="P2", "0.00%", "#,##0.00"))
// Preserves percentage or number formatting in text conversion

// Format consistency checking
=IF(CELL("format", C4)=CELL("format", C3), "Consistent", "Format mismatch")
// Validates formatting consistency between cells
```

### [[IF]]
CELL properties enable sophisticated conditional logic based on cell formatting, protection status, and location properties.

```spreadsheets
// Protection-based logic
=IF(CELL("protect", D5)=1, "Cannot edit", "Editable cell")
// Different actions based on cell protection status

// Format-based processing
=IF(CELL("format", E6)="C2", E6*1.08, "Not currency format")
// Applies tax calculation only to currency-formatted cells

// Location-based logic
=IF(CELL("col", F7)>10, "Extended range", "Standard range")
// Different processing based on column position
```

## Data Validation Functions

### [[INDIRECT]]
CELL addresses work with INDIRECT for dynamic cell referencing and flexible formula construction based on cell properties.

```spreadsheets
// Dynamic cell referencing
=INDIRECT(CELL("address", A8))
// References cell using address from CELL function

// Dynamic range references
=SUM(INDIRECT("A1:" & CELL("address", A10)))
// Creates sum range dynamically based on cell position

// Conditional cell referencing
=IF(CELL("contents", B9)>100, INDIRECT("C" & CELL("row", B9)), 0)
// References related cell based on current cell value
```

### [[OFFSET]]
Combines with CELL for dynamic range creation and cell navigation based on current position and properties.

```spreadsheets
// Dynamic offset based on position
=OFFSET(C10, CELL("row", D11)-CELL("row", C10), 0)
// Creates offset reference based on row difference

// Format-based range selection
=IF(CELL("format", E12)="C2", OFFSET(E12, 0, 1), E12)
// Selects different cells based on formatting

// Protection-aware navigation
=IF(CELL("protect", F13)=0, F13, OFFSET(F13, 1, 0))
// Moves to next row if current cell is protected
```

## Position Analysis Functions

### [[INDEX]]
CELL coordinates work with INDEX for dynamic data retrieval based on cell positions and properties.

```spreadsheets
// Position-based lookup
=INDEX(A:A, CELL("row", B14))
// Returns value from column A at same row as B14

// Dynamic table lookup
=INDEX(DataTable, CELL("row", C15)-1, CELL("col", C15))
// Looks up value in table based on current cell position

// Conditional index based on format
=IF(CELL("format", D16)="G", INDEX(GeneralData, CELL("row", D16)), "Not general format")
// Uses different data source based on cell format
```

### [[MATCH]]
Combines with CELL for position finding and dynamic searching based on cell properties and locations.

```spreadsheets
// Position-based matching
=MATCH(CELL("contents", E17), F:F, 0)
// Finds position of current cell value in column F

// Format-based matching
=IF(CELL("format", G18)="D1", MATCH(G18, DateRange, 0), "Not date format")
// Matches only if cell contains date format

// Dynamic search based on position
=MATCH(CELL("address", H19), AddressRange, 0)
// Searches for cell address in range of addresses
```

## Commonly Used With Functions Examples

### Dynamic Worksheet Management
```spreadsheets
// Comprehensive cell analysis
="Cell " & CELL("address", I20) & ": " &
 "Value=" & CELL("contents", I20) & ", " &
 "Format=" & CELL("format", I20) & ", " &
 "Protected=" & IF(CELL("protect", I20), "Yes", "No") & ", " &
 "Position=R" & CELL("row", I20) & "C" & CELL("col", I20)
// Complete cell property summary

// Dynamic navigation system
=IF(CELL("col", J21)<5, 
   "Move to " & ADDRESS(CELL("row", J21), CELL("col", J21)+1), 
   "End of range")
// Provides navigation guidance based on current position
```

### Template Validation and Quality Control
```spreadsheets
// Format consistency validation
=IF(AND(CELL("format", K22)="C2", CELL("format", L22)="C2", CELL("format", M22)="C2"),
   "✓ All currency formatted correctly",
   "✗ Inconsistent formatting detected")
// Validates multiple cells have consistent currency formatting

// Protection status audit
="Protection audit: " &
 SUMPRODUCT(--(CELL("protect", N22:N30)=1)) & " protected, " &
 SUMPRODUCT(--(CELL("protect", N22:N30)=0)) & " unprotected cells"
// Analyzes protection status across range (Note: Requires array formula support)
```

### Data Quality Assessment
```spreadsheets
// Content and format validation
=IF(AND(NOT(ISBLANK(CELL("contents", O23))), CELL("format", O23)<>"G"),
   "✓ Formatted data present",
   IF(ISBLANK(CELL("contents", O23)), "✗ Missing data", "✗ General format detected"))
// Validates both content presence and proper formatting

// Location-based data rules
=IF(CELL("row", P24)<=5,
   IF(CELL("format", P24)="@", "✓ Header text format", "✗ Headers should be text"),
   IF(CELL("format", P24)="F2", "✓ Data number format", "✗ Data should be formatted"))
// Applies different format rules based on row position
```