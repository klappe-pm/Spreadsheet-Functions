---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- lookup-reference
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- lookup reference
- excel
- sheets
---
# MATCH

## MATCH Description

Returns the relative position (row or column number) of a specified value within a range. Essential partner to INDEX function for creating flexible two-way lookups that overcome VLOOKUP limitations. Supports exact matches and approximate matches for sorted data.

> [!f(x)] MATCH Syntax
>
> ```spreadsheets
> MATCH(lookup_value, lookup_array, [match_type])
> ```
>
> **Parameters:**
> - `lookup_value` (required): The value to search for
> - `lookup_array` (required): One-dimensional range to search within
> - `match_type` (optional): 0 = exact match, 1 = less than (default), -1 = greater than

> [!f(x)] MATCH Examples
>
> ```spreadsheets
> // Find exact position of employee name
> MATCH("Sarah Johnson", A2:A100, 0) → returns row position of Sarah
> 
> // Find column position of header
> MATCH("Total Sales", Headers, 0) → returns column number for Total Sales
> 
> // Approximate match for tax brackets (sorted ascending)
> MATCH(75000, TaxBrackets, 1) → finds highest bracket ≤ 75000
> 
> // Find position in descending sorted list
> MATCH(85, ScoresDescending, -1) → finds lowest score ≥ 85
> 
> // Multi-criteria search with array formula
> MATCH(1, (Region="West")*(Product="Widget"), 0) → finds first matching row
> ```

## Use Cases

### [[Position finding]]
- **Dynamic column references**: Find column positions for headers that might move, making formulas adaptable to changing layouts
- **Row identification**: Locate specific records in large datasets without knowing exact row numbers
- **Rank determination**: Find position of values within sorted lists for percentile and ranking calculations
- **Data validation**: Verify that lookup values exist before performing expensive operations

### [[Lookup enhancement]]  
- **Two-way lookups**: Combine with INDEX to create flexible lookups that can search in any direction
- **Multi-criteria matching**: Use array formulas to find positions based on multiple conditions
- **Approximate matching**: Find closest values in sorted ranges for interpolation and classification
- **Dynamic range navigation**: Calculate positions for moving through datasets programmatically

### [[Data validation]]
- **Existence checking**: Verify that values exist in reference lists before processing
- **Duplicate detection**: Find first occurrence of values to identify and handle duplicates
- **Range validation**: Confirm that lookup values fall within acceptable parameter ranges
- **Data completeness**: Check for missing values in required data sequences

## Related

### Similar Functions

- [[INDEX]] - Returns value at specific position, perfect complement for two-way lookups
- [[FIND]] - Finds position of text within strings, similar concept but for text searching
- [[SEARCH]] - Case-insensitive text position finding with wildcard support
- [[XMATCH]] - Modern replacement with additional features and better error handling
- [[LOOKUP]] - Simplified position-based lookup for sorted data only

## Array Functions

### [[INDEX]]
The most important partner function for MATCH. Together they create the most powerful and flexible lookup system, replacing VLOOKUP limitations with bidirectional searching.

```spreadsheets
// Two-way lookup system
=INDEX(DataTable, MATCH("John", Names, 0), MATCH("Salary", Headers, 0))
// Finds John's salary by locating both row and column positions

// Dynamic last value extraction
=INDEX(Values, MATCH(9E+99, Values, 1))
// Finds last value in ascending sorted list

// First non-zero value
=INDEX(Numbers, MATCH(TRUE, Numbers<>0, 0))
// Locates first non-zero entry in range
```

### [[SMALL]]
Combined with MATCH to find positions of ranked values, enabling extraction of multiple results rather than just the first match.

```spreadsheets
// Find all positions of specific value
=MATCH(SearchValue, Range, 0)
// Returns first occurrence only

=SMALL(IF(Range=SearchValue, ROW(Range)-ROW(Range)+1), 1)
// Array formula returning first occurrence position

// Extract multiple matching positions
=SMALL(IF(Criteria=CriteriaRange, ROW(CriteriaRange)), ROW(A1))
// Copy down to get all matching positions
```

## Logical Functions

### [[ISERROR]]
Validates MATCH operations to prevent errors when lookup values don't exist, essential for robust formula construction.

```spreadsheets
// Safe position finding
=IF(ISERROR(MATCH(LookupValue, SearchRange, 0)), "Not found", MATCH(LookupValue, SearchRange, 0))
// Returns position or friendly message

// Conditional processing based on match success
=IF(ISERROR(MATCH(Product, ProductList, 0)), "Add new product", "Update existing")
// Different workflows for new vs existing items

// Robust lookup chain
=IF(ISERROR(MATCH(Item, PrimaryList, 0)), MATCH(Item, BackupList, 0), MATCH(Item, PrimaryList, 0))
// Falls back to secondary list if primary match fails
```

### [[IF]]
Controls MATCH execution based on conditions and provides conditional logic for different matching scenarios.

```spreadsheets
// Conditional match type
=MATCH(Value, Range, IF(IsSorted, 1, 0))
// Uses approximate match for sorted data, exact for unsorted

// Multi-criteria decision
=IF(Category="A", MATCH(Item, ListA, 0), MATCH(Item, ListB, 0))
// Searches different lists based on category

// Range-based matching
=IF(Value>1000, MATCH(Value, HighValueRange, 0), MATCH(Value, StandardRange, 0))
// Different lookup ranges based on value size
```

## Error Handling Functions

### [[IFERROR]]
Provides graceful error handling when MATCH can't find the lookup value, essential for user-friendly formulas.

```spreadsheets
// User-friendly position finding
=IFERROR(MATCH(UserInput, ValidOptions, 0), "Please select from dropdown")
// Guides users when invalid selections are made

// Default position handling
=IFERROR(MATCH(Month, MonthList, 0), 1)
// Defaults to first position if month not found

// Comprehensive error messages
=IFERROR(MATCH(ID, IDList, 0), "ID " & ID & " not found in system")
// Provides specific error information
```

### [[ISNA]]
Specifically tests for #N/A errors from MATCH, allowing targeted handling of "not found" scenarios.

```spreadsheets
// Specific handling for not found
=IF(ISNA(MATCH(Code, CodeList, 0)), "New code - add to database", "Code exists")
// Different action for missing vs existing codes

// Count missing items
=SUMPRODUCT(--(ISNA(MATCH(CheckList, MasterList, 0))))
// Counts how many items from CheckList are missing

// Validation status
=IF(ISNA(MATCH(Entry, ValidEntries, 0)), "❌ Invalid", "✅ Valid")
// Visual validation feedback
```

## Commonly Used With Functions Examples

### Dynamic Two-Way Lookup System
```spreadsheets
// Complete flexible lookup replacing VLOOKUP
=IFERROR(
   INDEX(DataTable, 
         MATCH(RowCriteria, RowHeaders, 0), 
         MATCH(ColumnCriteria, ColumnHeaders, 0)), 
   "Data not found")
// Finds intersection of any row and column with error handling
```

### Multi-Criteria Lookup with Array Formula
```spreadsheets
// Complex matching with multiple conditions
=INDEX(Results, 
       MATCH(1, (Criteria1=Range1)*(Criteria2=Range2)*(Criteria3=Range3), 0))
// Array formula finding first row matching all conditions
```

### Approximate Match for Grading System
```spreadsheets
// Grade assignment using sorted thresholds
=INDEX(GradeLetters, 
       MATCH(StudentScore, GradeThresholds, 1))
// Finds appropriate grade based on score ranges
```

### Data Validation with Position Tracking
```spreadsheets
// Validate and track positions simultaneously
=IF(ISERROR(MATCH(InputValue, ValidList, 0)), 
   "Invalid entry", 
   "Valid - Position: " & MATCH(InputValue, ValidList, 0))
// Provides both validation and position information
```

### Dynamic Range Processing
```spreadsheets
// Process data until specific condition met
=IF(MATCH("END", ProcessList, 0)>ROW(), 
   INDEX(ProcessList, ROW()), 
   "")
// Processes list until "END" marker found
```
