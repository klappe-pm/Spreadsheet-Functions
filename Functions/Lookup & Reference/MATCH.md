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
---

# MATCH

## MATCH Description

MATCH searches for a value in a range and returns the relative position of that item.

> [!f(x)] MATCH Syntax
>
> ```spreadsheets
> MATCH(lookup_value, lookup_array, [match_type])
> ```
>
> **Parameters:**
> - `lookup_value` (required): Value to search for
> - `lookup_array` (required): Range to search in
> - `match_type` (optional): 0=exact, 1=less than, -1=greater than

> [!f(x)] MATCH Examples
>
> ```spreadsheets
> MATCH("Apple", A1:A10, 0) → position // Find exact position
> 
> MATCH(100, B:B, 1) → largest_less_equal // Find largest value ≤100
> 
> MATCH(MAX(C:C), C:C, 0) → max_position // Find position of maximum
> ```

## Use Cases

### [[Data Retrieval]]
- **Implementation**: Retrieve related data from reference tables and databases for comprehensive analysis
- **Business Application**: Look up prices, specifications, and related information to support business operations
- **Technical Details**: Optimize lookup performance, handle missing values, and implement proper error handling

### [[Data Integration]]
- **Implementation**: Combine data from multiple sources using lookup functions for unified reporting and analysis
- **Business Application**: Integrate customer, product, and operational data for comprehensive business intelligence
- **Technical Details**: Design efficient lookup structures, handle data relationships, and ensure referential integrity

### [[Dynamic References]]
- **Implementation**: Create flexible formulas that adapt to changing data structures and requirements
- **Business Application**: Build scalable reporting systems that accommodate growth and changing business needs
- **Technical Details**: Implement dynamic range references, optimize calculation performance, and maintain formula flexibility

## Related

### Similar Functions

- [[INDEX]] - Related lookup & reference function for analytical calculations
- [[FIND]] - Related lookup & reference function for analytical calculations
- [[SEARCH]] - Related lookup & reference function for analytical calculations
- [[XLOOKUP]] - Related lookup & reference function for analytical calculations

### Commonly Used With Functions

**[[INDEX]]** - Retrieve values by position for flexible lookups

*Use INDEX with MATCH for enhanced analytical workflows:*
```spreadsheets
=INDEX(MATCH(A1:A10))
```
This formula combines INDEX and MATCH for comprehensive data analysis

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with MATCH for conditional logic and decision making:*
```spreadsheets
=IF(MATCH(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies MATCH to a range and compares the result to a threshold, returning different text based on the condition

**[[MAX]]** - Find maximum values for range analysis

*Use MAX with MATCH for enhanced analytical workflows:*
```spreadsheets
=MAX(MATCH(A1:A10))
```
This formula combines MAX and MATCH for comprehensive data analysis
