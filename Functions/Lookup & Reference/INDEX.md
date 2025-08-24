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

# INDEX

## INDEX Description

INDEX returns the value at a specified row and column intersection within a given range or array.

> [!f(x)] INDEX Syntax
>
> ```spreadsheets
> INDEX(array, row_num, [column_num])
> ```
>
> **Parameters:**
> - `array` (required): Range or array to index into
> - `row_num` (required): Row number to retrieve
> - `column_num` (optional): Column number to retrieve (required for 2D ranges)

> [!f(x)] INDEX Examples
>
> ```spreadsheets
> INDEX(A1:A10, 5) → fifth_value // Get 5th item in range
> 
> INDEX(B1:D10, 3, 2) → cell_value // Get value at row 3, column 2
> 
> INDEX(A:A, MATCH("Item", A:A, 0)) → matched_value // Dynamic lookup
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

- [[MATCH]] - Related lookup & reference function for analytical calculations
- [[OFFSET]] - Related lookup & reference function for analytical calculations
- [[INDIRECT]] - Related lookup & reference function for analytical calculations
- [[XLOOKUP]] - Related lookup & reference function for analytical calculations

### Commonly Used With Functions

**[[MATCH]]** - Find position of values for dynamic references

*Use MATCH with INDEX for enhanced analytical workflows:*
```spreadsheets
=MATCH(INDEX(A1:A10))
```
This formula combines MATCH and INDEX for comprehensive data analysis

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with INDEX for conditional logic and decision making:*
```spreadsheets
=IF(INDEX(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies INDEX to a range and compares the result to a threshold, returning different text based on the condition

**[[SMALL]]** - Related function for analytical workflows

*Use SMALL with INDEX for enhanced analytical workflows:*
```spreadsheets
=SMALL(INDEX(A1:A10))
```
This formula combines SMALL and INDEX for comprehensive data analysis
