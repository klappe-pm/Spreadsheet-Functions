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

# RIGHT

## RIGHT Description

RIGHT extracts a specified number of characters from the end (right side) of a text string.

> [!f(x)] RIGHT Syntax
>
> ```spreadsheets
> RIGHT(text, [num_chars])
> ```
>
> **Parameters:**
> - `text` (required): The text string from which to extract characters
> - `num_chars` (optional): Number of characters to extract (default is 1)

> [!f(x)] RIGHT Examples
>
> ```spreadsheets
> RIGHT("Hello", 3) → "llo" // Last 3 characters
> 
> RIGHT(A1, 4) → last_four // Extract from cell
> 
> RIGHT("Product123", 3) → "123" // Extract number suffix
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

- [[LEFT]] - Related text function for analytical calculations
- [[MID]] - Related text function for analytical calculations
- [[LEN]] - Related text function for analytical calculations
- [[FIND]] - Related text function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with RIGHT for conditional logic and decision making:*
```spreadsheets
=IF(RIGHT(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies RIGHT to a range and compares the result to a threshold, returning different text based on the condition

**[[LEN]]** - Related function for analytical workflows

*Use LEN with RIGHT for enhanced analytical workflows:*
```spreadsheets
=LEN(RIGHT(A1:A10))
```
This formula combines LEN and RIGHT for comprehensive data analysis

**[[FIND]]** - Related function for analytical workflows

*Use FIND with RIGHT for enhanced analytical workflows:*
```spreadsheets
=FIND(RIGHT(A1:A10))
```
This formula combines FIND and RIGHT for comprehensive data analysis
