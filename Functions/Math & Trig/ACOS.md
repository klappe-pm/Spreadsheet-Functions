---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: math & trig
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-19
aliases: []
tags: []
---

# ACOS

## ACOS Description

Calculates the arccosine (inverse cosine) of a number, returning the result in radians. The arccosine is the angle whose cosine is the specified number. Input must be between -1 and 1 inclusive, and the result will be between 0 and π radians.

> [!f(x)] ACOS Syntax
>
> ```spreadsheets
> ACOS(number)
> ```
>
> **Parameters:**
> - `number` (required): A numeric value between -1 and 1 for which you want the arccosine

> [!f(x)] ACOS Examples
>
> ```spreadsheets
> // Basic arccosine calculations
> ACOS(1) → 0 (cosine of 0 radians is 1)
> 
> // Common angle calculations
> ACOS(0) → 1.570796327 (π/2 radians = 90 degrees)
> 
> // Negative value calculation
> ACOS(-1) → 3.141592654 (π radians = 180 degrees)
> 
> // Converting to degrees
> ACOS(0.5)*180/PI() → 60 (degrees)
> 
> // Using with cell references
> ACOS(A1) → arccosine of value in cell A1
> ```

## Use Cases

### [[Engineering calculations]]
- **Structural analysis**: Calculate support angles in bridge construction based on load distribution ratios
- **Mechanical design**: Determine gear tooth angles from contact ratios in precision machinery applications
- **Electrical engineering**: Find phase angles in AC circuit analysis from power factor measurements
- **Aerospace applications**: Calculate flight path angles from lift-to-weight ratios in aircraft design

### [[Physics simulations]]  
- **Wave analysis**: Determine phase relationships in interference patterns from amplitude ratios
- **Optics calculations**: Calculate critical angles for total internal reflection in fiber optic design
- **Pendulum motion**: Find maximum deflection angles from energy conservation ratios
- **Oscillatory systems**: Calculate phase angles in damped harmonic oscillators from amplitude decay

### [[Navigation systems]]
- **GPS positioning**: Calculate bearing angles from coordinate differences in location-based services
- **Marine navigation**: Determine compass headings from position vectors in route planning
- **Aviation systems**: Calculate approach angles from altitude-to-distance ratios in landing procedures
- **Survey calculations**: Find elevation angles from horizontal and vertical distance measurements

## Related

### Similar Functions

- [[ASIN]] - Calculates arcsine, complementary to ACOS for right triangle calculations
- [[ATAN]] - Calculates arctangent, useful when working with slopes and ratios rather than adjacent/hypotenuse
- [[COS]] - Calculates cosine, the inverse operation of ACOS
- [[DEGREES]] - Converts radians to degrees, essential for readable angle measurements
- [[RADIANS]] - Converts degrees to radians for trigonometric calculations

## Trigonometric Functions

### [[COS]]
ACOS and COS are inverse functions, making them essential for angle-finding calculations. COS converts angles to ratios, while ACOS converts ratios back to angles.

```spreadsheets
// Verify inverse relationship
=COS(ACOS(0.5)) → 0.5 (confirms inverse operations)

// Find original angle from cosine value
=ACOS(COS(RADIANS(60))) → 1.047197551 (π/3 radians = 60 degrees)

// Engineering stress analysis
=ACOS(B2/C2)*180/PI() & " degrees" 
// Calculates angle from adjacent/hypotenuse ratio
```

### [[DEGREES]]
ACOS returns values in radians, so DEGREES is frequently used to convert results to more intuitive degree measurements for practical applications.

```spreadsheets
// Convert arccosine result to degrees
=DEGREES(ACOS(0.866)) → 30 (degrees)

// Navigation bearing calculation
="Bearing: " & DEGREES(ACOS(A1/B1)) & "°"
// Shows bearing angle in degrees from coordinate ratios

// Quality control angle measurement
=IF(DEGREES(ACOS(D2))>45, "Reject", "Accept")
// Quality check based on angle threshold
```

## Mathematical Functions

### [[PI]]
Used with ACOS for angle calculations and conversions, particularly when working with angle relationships and circular measurements.

```spreadsheets
// Express angle as fraction of π
=ACOS(-0.5)/PI() & "π radians"
// Result: "0.666666667π radians" (2π/3)

// Calculate complementary angle
=PI()/2 - ACOS(0.7)
// Finds complementary angle in radians

// Circular sector calculations
=ACOS(0.8) * 2 * PI() * A1
// Arc length calculation using arccosine
```

### [[SQRT]]
Often combined with ACOS in geometric calculations, especially when working with distance ratios and Pythagorean relationships.

```spreadsheets
// Calculate angle from sides of triangle
=ACOS((A1^2+B1^2-C1^2)/(2*A1*B1))
// Law of cosines angle calculation

// Distance-based angle calculation
=DEGREES(ACOS(A2/SQRT(A2^2+B2^2)))
// Angle from horizontal using distance components

// 3D vector angle calculation
=ACOS(D1/SQRT(D1^2+E1^2+F1^2))
// Angle between vector and axis
```

## Conditional Logic Functions

### [[IF]]
Essential for validating ACOS inputs since the function only accepts values between -1 and 1, and for handling edge cases in angle calculations.

```spreadsheets
// Input validation for ACOS
=IF(AND(A1>=-1,A1<=1), DEGREES(ACOS(A1)), "Invalid input")
// Prevents #NUM! error from invalid inputs

// Conditional angle calculation
=IF(B1>0, DEGREES(ACOS(B1)), "Negative ratio not allowed")
// Only calculates for positive ratios

// Engineering tolerance check
=IF(ABS(DEGREES(ACOS(C1))-90)<5, "Within tolerance", "Adjust angle")
// Checks if calculated angle is within 5 degrees of perpendicular
```

## Commonly Used With Functions Examples

### Angle Measurement and Validation
```spreadsheets
// Complete angle validation system
=IF(AND(A1>=-1,A1<=1), DEGREES(ACOS(A1)) & "°", "Error: Input must be -1 to 1")

// Multi-angle comparison
=DEGREES(ACOS(B1)) & "° vs target " & C1 & "° (diff: " & ABS(DEGREES(ACOS(B1))-C1) & "°)"

// Quality control with statistical analysis
=IF(DEGREES(ACOS(D1))>AVERAGE(E:E)+2*STDEV(E:E), "Outlier detected", "Normal")
```

### Engineering Calculations
```spreadsheets
// Structural load analysis
="Load angle: " & DEGREES(ACOS(F1/G1)) & "° (Factor: " & ROUND(COS(ACOS(F1/G1)),3) & ")"

// Precision machinery alignment
=IF(ABS(DEGREES(ACOS(H1))-90)<0.1, "Aligned", "Adjust by " & (90-DEGREES(ACOS(H1))) & "°")

// Vector analysis with magnitude
="Angle: " & DEGREES(ACOS(I1/SQRT(I1^2+J1^2+K1^2))) & "° (Magnitude: " & SQRT(I1^2+J1^2+K1^2) & ")"
```

### Navigation and Positioning
```spreadsheets
// GPS bearing calculation with distance
="Bearing: " & DEGREES(ACOS(L1/M1)) & "° (Distance: " & M1 & " km)"

// Navigation error checking
=IF(DEGREES(ACOS(N1))>180, "Error: Check coordinates", DEGREES(ACOS(N1)) & "° heading")

// Multi-point navigation analysis
="From point A: " & DEGREES(ACOS(O1)) & "° to point B: " & DEGREES(ACOS(P1)) & "° (Turn: " & ABS(DEGREES(ACOS(O1))-DEGREES(ACOS(P1))) & "°)"
```
