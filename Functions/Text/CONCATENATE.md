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

# CONCATENATE

## CONCATENATE Description

CONCATENATE joins multiple text strings into one string. This function has been largely replaced by the & operator and CONCAT function.

> [!f(x)] CONCATENATE Syntax
>
> ```spreadsheets
> CONCATENATE(text1, [text2], ...)
> ```
>
> **Parameters:**
> - `text1` (required): First text string to join
> - `text2` (optional): Additional text strings to join

> [!f(x)] CONCATENATE Examples
>
> ```spreadsheets
> CONCATENATE("Hello", " ", "World") → "Hello World" // Join with space
> 
> CONCATENATE(A1, B1) → combined_text // Join cell values
> 
> CONCATENATE("Product: ", C1) → labeled_value // Add label
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

- [[CONCAT]] - Related text function for analytical calculations
- [[TEXTJOIN]] - Related text function for analytical calculations
- [[AMPERSAND(&)]] - Related text function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with CONCATENATE for conditional logic and decision making:*
```spreadsheets
=IF(CONCATENATE(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies CONCATENATE to a range and compares the result to a threshold, returning different text based on the condition

**[[LEFT]]** - Related function for analytical workflows

*Use LEFT with CONCATENATE for enhanced analytical workflows:*
```spreadsheets
=LEFT(CONCATENATE(A1:A10))
```
This formula combines LEFT and CONCATENATE for comprehensive data analysis

**[[RIGHT]]** - Related function for analytical workflows

*Use RIGHT with CONCATENATE for enhanced analytical workflows:*
```spreadsheets
=RIGHT(CONCATENATE(A1:A10))
```
This formula combines RIGHT and CONCATENATE for comprehensive data analysis
