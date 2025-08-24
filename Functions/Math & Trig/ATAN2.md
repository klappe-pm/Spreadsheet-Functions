---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- math-trig
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- math trig
- excel
- sheets
---
# ATAN2

## ATAN2 Description

Returns the arctangent of the specified x and y coordinates, providing the angle in radians from the x-axis to a point. ATAN2 handles all quadrants correctly and avoids division by zero.

> [!f(x)] ATAN2 Syntax
>
> ```spreadsheets
> ATAN2(x_num, y_num)
> ```
>
> **Parameters:**
> - `x_num` (required): X-coordinate of the point
> - `y_num` (required): Y-coordinate of the point

> [!f(x)] ATAN2 Examples
>
> ```spreadsheets
> ATAN2(1, 1) → π/4 (0.785 radians)
> // 45-degree angle
> 
> ATAN2(1, 0) → 0
> // Angle along positive x-axis
> 
> ATAN2(0, 1) → π/2
> // Angle along positive y-axis
> 
> ATAN2(-1, -1) → -3π/4
> // Third quadrant angle
>
> ```

## Use Cases

### [[Geometric calculations]]
- **Implementation**: Calculate angles, bearings, and directions in coordinate systems

### [[Engineering analysis]]
- **Implementation**: Determine phase angles in electrical circuits and mechanical systems

### [[Navigation systems]]
- **Implementation**: Calculate headings and bearings for GPS and mapping applications

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
