---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - lookup-reference
  - - subTopics
    - []
  - - dateCreated
    - 2025-08-17
  - - dateRevised
    - 2025-08-17
  - - aliases
    - []
  - - tags
    - []
---
# XLOOKUP

## XLOOKUP Description

A modern, powerful replacement for VLOOKUP and HLOOKUP that searches in any direction, supports multiple return values, has built-in error handling, and offers superior performance. Available in Excel 365 and Excel 2021, representing the evolution of lookup functions with enhanced flexibility and user-friendly features.

> [!f(x)] XLOOKUP Syntax
>
> ```spreadsheets
> XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
> ```
>
> **Parameters:**
> - `lookup_value` (required): The value to search for
> - `lookup_array` (required): Range or array to search within
> - `return_array` (required): Range or array to return values from
> - `if_not_found` (optional): Value to return if no match found (default: #N/A)
> - `match_mode` (optional): 0 = exact (default), -1 = exact or next smallest, 1 = exact or next largest, 2 = wildcard
> - `search_mode` (optional): 1 = first to last (default), -1 = last to first, 2 = binary (sorted asc), -2 = binary (sorted desc)

> [!f(x)] XLOOKUP Examples
>
> ```spreadsheets
> // Basic exact match lookup
> XLOOKUP("Product A", Products, Prices) → returns price for Product A
> 
> // Lookup with custom error message
> XLOOKUP(B2, EmployeeIDs, Salaries, "Employee not found") → friendly error handling
> 
> // Return multiple columns at once
> XLOOKUP(C1, StudentIDs, GradeTable) → returns entire row of grades
> 
> // Approximate match for tax brackets
> XLOOKUP(Income, TaxBrackets, TaxRates, , 1) → finds next largest bracket
> 
> // Reverse search (last occurrence)
> XLOOKUP("Q4", Quarters, Sales, , , -1) → finds last Q4 entry
> ```

## Use Cases

### [[Data analysis]]
- **Multi-dimensional analysis**: Return entire rows or columns of related data with a single lookup, eliminating need for multiple VLOOKUP formulas
- **Time series analysis**: Find specific dates or periods and return associated metrics, with built-in handling for missing periods
- **Customer analytics**: Look up customer information and return comprehensive profiles including demographics, purchase history, and preferences
- **Performance dashboards**: Create dynamic reports that automatically handle missing data with custom messages instead of error codes

### [[Calculations]]  
- **Pricing models**: Implement complex pricing structures with approximate matches for volume discounts and tier-based pricing
- **Financial calculations**: Look up interest rates, exchange rates, or tax rates with built-in interpolation capabilities
- **Inventory management**: Calculate reorder points, lead times, and supplier information with error-resistant lookups
- **Commission calculations**: Determine sales commission rates based on performance tiers with automatic fallback values

### [[Report generation]]
- **Automated reporting**: Generate reports that handle missing data gracefully without displaying error values to end users
- **Cross-reference verification**: Validate data across multiple sources with comprehensive error messaging
- **Dashboard creation**: Build interactive dashboards with lookups that return multiple related values simultaneously
- **Data consolidation**: Merge information from multiple tables with robust error handling and custom not-found messages

## Related

### Similar Functions

- [[VLOOKUP]] - Predecessor with vertical-only search and less flexibility
- [[HLOOKUP]] - Horizontal lookup function replaced by XLOOKUP's bidirectional capability
- [[INDEX]] - Combined with MATCH provides similar flexibility but requires more complex formulas
- [[MATCH]] - Position-finding function that XLOOKUP incorporates internally
- [[FILTER]] - Returns multiple matching rows rather than single values

## Array Functions

### [[FILTER]]
Complementary to XLOOKUP - while XLOOKUP returns single matches or rows, FILTER returns all matching records. Together they provide complete lookup and filtering capabilities.

```spreadsheets
// XLOOKUP for single match
=XLOOKUP("Sales", Departments, ManagerNames)
// Returns single manager name for Sales department

// FILTER for multiple matches
=FILTER(EmployeeData, DepartmentColumn="Sales")
// Returns all employees in Sales department

// Combined usage for comprehensive analysis
=XLOOKUP("Q1", Quarters, FILTER(SalesData, ProductColumn="Widget"))
// Filter by product, then lookup by quarter
```

### [[UNIQUE]]
Works with XLOOKUP to handle duplicate scenarios and create clean lookup tables from messy data sources.

```spreadsheets
// Lookup from deduplicated list
=XLOOKUP(SearchValue, UNIQUE(DuplicateList), UNIQUE(ResultList))
// Ensures clean lookup without duplicate confusion

// Find unique categories then lookup details
=XLOOKUP(Category, UNIQUE(CategoryList), UNIQUE(DescriptionList))
// Works with unique values for consistent results

// Create lookup table from raw data
=XLOOKUP(Product, UNIQUE(ProductLog), UNIQUE(PriceLog))
// Builds lookup from transaction history
```

## Text Functions

### [[TRIM]]
Prepares lookup values by removing extra spaces that could prevent matches, essential for reliable XLOOKUP operations with user input.

```spreadsheets
// Clean lookup values
=XLOOKUP(TRIM(UserInput), CleanedList, Results)
// Removes spaces that might prevent matches

// Robust text matching
=XLOOKUP(TRIM(UPPER(A1)), TRIM(UPPER(SearchList)), ReturnValues)
// Combines trimming with case normalization

// Data cleaning integration
=XLOOKUP(TRIM(B1), ProductCodes, TRIM(ProductNames))
// Cleans both input and output values
```

### [[CONCATENATE]]
Builds composite lookup keys when XLOOKUP needs to match multiple criteria simultaneously.

```spreadsheets
// Multi-criteria lookup with concatenated key
=XLOOKUP(A1&"-"&B1, ProductCode&"-"&Region, Pricing)
// Searches for product-region combinations

// Dynamic key construction
=XLOOKUP(CONCATENATE(Customer, "_", YEAR(OrderDate)), CustomerYearKey, AnnualSpend)
// Creates temporal customer keys

// Complex business rule matching
=XLOOKUP(CONCATENATE(Category, "|", Subcategory, "|", Size), RuleKeys, Discounts)
// Matches three-part business rules
```

## Logical Functions

### [[IF]]
Controlls XLOOKUP execution and provides additional conditional logic around lookup operations.

```spreadsheets
// Conditional lookup tables
=IF(CustomerTier="Premium", 
   XLOOKUP(Product, PremiumProducts, PremiumPrices), 
   XLOOKUP(Product, StandardProducts, StandardPrices))
// Different lookup tables based on customer status

// Conditional error handling
=IF(SearchValue="", "No selection", XLOOKUP(SearchValue, LookupList, Results, "Not found"))
// Handles empty inputs before lookup

// Performance optimization
=IF(EXACT(A1, PreviousLookup), PreviousResult, XLOOKUP(A1, LookupArray, ResultArray))
// Avoids repeated lookups for same value
```

### [[SWITCH]]
Provides multi-condition logic that can work alongside XLOOKUP for complex decision trees.

```spreadsheets
// Multi-table lookup selection
=XLOOKUP(Item, 
         SWITCH(Category, 
                "Electronics", ElectronicsProducts, 
                "Clothing", ClothingProducts, 
                "Books", BookProducts), 
         SWITCH(Category, 
                "Electronics", ElectronicsPrices, 
                "Clothing", ClothingPrices, 
                "Books", BookPrices))
// Dynamic table selection based on category
```

## Date Functions

### [[TODAY]]
Enables time-sensitive lookups and dynamic date-based filtering with XLOOKUP.

```spreadsheets
// Current period lookup
=XLOOKUP(TODAY(), DateRanges, CurrentRates, "Rate not available")
// Finds current applicable rate based on date

// Age-based calculations
=XLOOKUP(TODAY()-BirthDate, AgeRanges, InsuranceRates)
// Calculates insurance rates based on current age

// Seasonal pricing
=XLOOKUP(MONTH(TODAY()), MonthNumbers, SeasonalPrices)
// Applies seasonal pricing based on current month
```

## Commonly Used With Functions Examples

### Advanced Customer Lookup System
```spreadsheets
// Comprehensive customer information retrieval
=IF(TRIM(CustomerID)="", 
   "Enter Customer ID", 
   XLOOKUP(TRIM(UPPER(CustomerID)), 
          CustomerDatabase[ID], 
          CustomerDatabase[Name]:CustomerDatabase[Phone], 
          "Customer not found - Please verify ID"))
// Returns multiple customer fields with robust error handling
```

### Dynamic Pricing Calculator
```spreadsheets
// Multi-tier pricing with volume discounts
=XLOOKUP(Quantity, 
         QuantityBreaks, 
         XLOOKUP(ProductCode, 
                Products, 
                BasePrices) * DiscountMultipliers, 
         "Invalid quantity", 
         1) // Next largest quantity break
// Nested XLOOKUP for product price with quantity-based discounts
```

### Comprehensive Reporting System
```spreadsheets
// Multi-dimensional report data
=XLOOKUP(ReportDate, 
         DateList, 
         FILTER(SalesData, 
               (RegionColumn=SelectedRegion) * 
               (ProductColumn=SelectedProduct)), 
         "No data for selected date")
// Combines date lookup with filtered multi-criteria data
```

### Inventory Management with Fallbacks
```spreadsheets
// Stock lookup with supplier alternatives
=IF(XLOOKUP(PartNumber, PrimaryInventory, StockLevels, 0)>MinimumStock, 
   "In Stock", 
   "Order from: " & XLOOKUP(PartNumber, SupplierCatalog, SupplierNames, "No supplier found"))
// Checks primary stock then suggests supplier if needed
```

### Performance Dashboard with Error Recovery
```spreadsheets
// Robust performance metrics lookup
=CONCATENATE(
   "Current: ", XLOOKUP(Employee, CurrentMonth, Performance, "No data"), 
   " | Trend: ", 
   IF(XLOOKUP(Employee, CurrentMonth, Performance, 0) > 
      XLOOKUP(Employee, PreviousMonth, Performance, 0), "↑", "↓"))
// Creates performance summary with trend indicators and error handling
```
