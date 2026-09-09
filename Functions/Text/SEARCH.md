---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- text
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
---

# SEARCH-

## SEARCH- Description

SEARCH- manipulates and analyzes text strings for data processing and formatting.

> [!f(x)] SEARCH- Syntax
>
> ```spreadsheets
> SEARCH-(input_value, [options])
> ```
>
> **Parameters:**
> - `input_value` (required): Primary input for the calculation
> - `options` (optional): Additional parameters or settings

> [!f(x)] SEARCH- Examples
>
> ```spreadsheets
> SEARCH-(A1) → result // Basic calculation
> 
> SEARCH-(A1:A10) → range_result // Process entire range
> ```

## Use Cases

### [[Text Processing]]
- **Implementation**: Parse, manipulate, and analyze text data for information extraction and data cleaning
- **Business Application**: Process customer data, product information, and communication content for business insights
- **Technical Details**: Handle various text formats, implement string validation, and ensure data quality

### [[Data Cleaning]]
- **Implementation**: Clean and standardize text data by removing unwanted characters, formatting, and inconsistencies
- **Business Application**: Prepare data for analysis, standardize naming conventions, and improve data quality
- **Technical Details**: Implement validation rules, handle special characters, and maintain data integrity

### [[Report Formatting]]
- **Implementation**: Format text output for reports, labels, and user interfaces with consistent presentation
- **Business Application**: Create professional reports, generate labels, and format data for stakeholder communication
- **Technical Details**: Ensure consistent formatting, handle different text lengths, and implement proper alignment

## Related

### Similar Functions

- [[IF]] - Related text function for analytical calculations
- [[IFERROR]] - Related text function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with SEARCH- for conditional logic and decision making:*
```spreadsheets
=IF(SEARCH-(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies SEARCH- to a range and compares the result to a threshold, returning different text based on the condition

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with SEARCH- for aggregate calculations across multiple results:*
```spreadsheets
=SUM(SEARCH-(A1:A5),SEARCH-(B1:B5),SEARCH-(C1:C5))
```
This formula calculates SEARCH- for multiple ranges and sums the results together

**[[AVERAGE]]** - Calculate arithmetic mean for central tendency analysis

*Use AVERAGE with SEARCH- for enhanced analytical workflows:*
```spreadsheets
=AVERAGE(SEARCH-(A1:A10))
```
This formula combines AVERAGE and SEARCH- for comprehensive data analysis
