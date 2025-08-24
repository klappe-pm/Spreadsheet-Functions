---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- dynamic-arrays
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- dynamic arrays
- excel
- sheets
---
# XMATCH

## XMATCH Description

Performs a lookup in an array and returns the relative position of the first match, offering enhanced functionality over MATCH with exact, approximate, and wildcard matching options.

> [!f(x)] XMATCH Syntax
>
> ```spreadsheets
> XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])
> ```
>
> **Parameters:**
> - `lookup_value` (required): The value to search for in the array
> - `lookup_array` (required): The array to search within
> - `match_mode` (optional): Matching behavior: 0=exact, -1=exact or next smallest, 1=exact or next largest, 2=wildcard
> - `search_mode` (optional): Search direction: 1=first to last, -1=last to first, 2=binary ascending, -2=binary descending

> [!f(x)] XMATCH Examples
>
> ```spreadsheets
> XMATCH("Apple", A1:A10) → position of Apple in the range
> // Exact text match
> 
> XMATCH(100, B1:B10, 1) → position of 100 or next largest value
> // Approximate numeric match
> 
> XMATCH("A*e", C1:C10, 2) → position of text matching wildcard pattern
> // Wildcard matching
> 
> XMATCH(50, D1:D10, 0, -1) → last occurrence of exact match
> // Reverse search
>
> ```

## Use Cases

### [[Advanced lookup operations]]
- **Implementation**: Perform sophisticated lookups with flexible matching criteria and search directions

### [[Data validation]]
- **Implementation**: Verify data existence and position within datasets using various matching algorithms

### [[Dynamic indexing]]
- **Implementation**: Create dynamic references to data based on complex search criteria and patterns

## Related

### Similar Functions

- [[RELATED1]] - Description of relationship
- [[RELATED2]] - Description of relationship
- [[RELATED3]] - Description of relationship

### Commonly Used With Functions

- [[IF]] - Conditional logic and error handling
- [[IFERROR]] - Error handling and validation
- [[INDEX]] - Data retrieval and reference operations
- [[MATCH]] - Lookup and positioning functions
