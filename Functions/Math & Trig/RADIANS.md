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
# RADIANS

## RADIANS Description

Converts angle measurements from degrees to radians using the formula: radians = degrees × π/180. Essential for trigonometric calculations since most mathematical functions require radian input for accurate results.

> [!f(x)] RADIANS Syntax
>
> ```spreadsheets
> RADIANS(angle)
> ```
>
> **Parameters:**
> - `angle` (required): The angle in degrees to convert to radians

> [!f(x)] RADIANS Examples
>
> ```spreadsheets
> // Common angle conversions
> RADIANS(90) → 1.5708 (90 degrees = π/2 radians)
> 
> // Full circle conversion
> RADIANS(360) → 6.2832 (360 degrees = 2π radians)
> 
> // Half circle conversion
> RADIANS(180) → 3.1416 (180 degrees = π radians)
> 
> // 30-degree conversion for trigonometry
> RADIANS(30) → 0.5236 (30 degrees = π/6 radians)
> 
> // Negative angle conversion
> RADIANS(-45) → -0.7854 (-45 degrees = -π/4 radians)
> ```

## Use Cases

### [[Trigonometric calculations]]
- **Sine and cosine functions**: Convert degree inputs to radians for accurate SIN, COS, and TAN calculations in mathematical modeling
- **Wave analysis**: Transform degree-based frequency measurements to radians for signal processing and harmonic analysis
- **Circular motion**: Calculate angular velocities and positions in engineering and physics applications
- **Navigation systems**: Convert compass bearings and heading angles for GPS and mapping calculations

### [[Engineering applications]]  
- **Mechanical design**: Calculate gear ratios, pulley systems, and rotational mechanics using radian-based formulas
- **Electrical engineering**: Analyze AC circuits, phase relationships, and frequency responses requiring radian inputs
- **Structural analysis**: Determine beam deflections, joint rotations, and stability factors in construction projects
- **Robotics programming**: Convert joint angles and movement commands from degrees to radians for servo control

### [[Scientific modeling]]
- **Physics simulations**: Model pendulum motion, orbital mechanics, and wave propagation using radian-based equations
- **Statistical analysis**: Calculate circular statistics, directional data analysis, and periodic trend modeling
- **Astronomy calculations**: Convert celestial coordinates, orbital elements, and observational angles for space science
- **Weather modeling**: Analyze cyclonic motion, wind directions, and atmospheric circulation patterns

## Related

### Similar Functions

- [[DEGREES]] - Converts radians back to degrees, inverse operation of RADIANS for angle measurement conversion
- [[PI]] - Provides the pi constant used in degree-to-radian conversions, essential for manual calculations
- [[SIN]] - Calculates sine values, requires radian input from RADIANS for degree-based angle calculations
- [[COS]] - Computes cosine values, works with RADIANS output for trigonometric analysis of degree measurements
- [[TAN]] - Determines tangent values, uses RADIANS conversion for accurate degree-based trigonometric calculations

## Trigonometric Functions

### [[SIN]]
Must use RADIANS to convert degree inputs before calculating sine values, as SIN function expects radian measurements for mathematical accuracy.

```spreadsheets
// Sine of 30 degrees (should equal 0.5)
=SIN(RADIANS(30))
// Converts 30 degrees to radians, then calculates sine

// Sine wave generation with degree inputs
=SIN(RADIANS(A1*360/12))
// Creates sine wave where A1 represents months (0-12)

// Vertical component of angled force
=B1*SIN(RADIANS(C1))
// Force B1 at angle C1 degrees, calculates vertical component
```

### [[COS]]
Requires RADIANS conversion for degree-based inputs to ensure accurate cosine calculations in engineering and mathematical applications.

```spreadsheets
// Cosine of 60 degrees (should equal 0.5)
=COS(RADIANS(60))
// Converts 60 degrees to radians for accurate cosine calculation

// Horizontal displacement in circular motion
=D1*COS(RADIANS(E1))
// Radius D1 with angle E1 degrees, calculates x-coordinate

// Phase relationship analysis
=COS(RADIANS(F1+G1))
// Combines base angle F1 with phase shift G1 in degrees
```

## Angle Functions

### [[DEGREES]]
Inverse function of RADIANS, converting radian measurements back to degrees for human-readable angle representations.

```spreadsheets
// Verify conversion accuracy
=DEGREES(RADIANS(A1))
// Should return original degree value A1

// Convert calculated radian result to degrees
=DEGREES(ATAN2(B1,C1))
// ATAN2 returns radians, converts to degrees for display

// Full angle conversion workflow
=DEGREES(ASIN(D1)) & "°"
// Arcsine returns radians, converts to degrees with symbol
```

### [[PI]]
Foundational constant in RADIANS conversion formula, often used together for manual angle conversions and mathematical relationships.

```spreadsheets
// Manual radian conversion (equivalent to RADIANS function)
=A1*PI()/180
// Converts degrees A1 to radians using PI constant

// Angle proportion calculations
=RADIANS(B1)/(2*PI())
// Calculates what fraction of full circle angle B1 represents

// Multiple angle conversions
=C1*PI()/180 + D1*PI()/180
// Combines two degree angles in radian form
```

## Commonly Used With Functions Examples

### RADIANS with Trigonometric Analysis
```spreadsheets
// Complete trigonometric analysis of degree angle
={SIN(RADIANS(A1)), COS(RADIANS(A1)), TAN(RADIANS(A1))}
// Returns sine, cosine, and tangent of angle A1 in degrees

// Polar to rectangular coordinate conversion
=B1*COS(RADIANS(C1)) & ", " & B1*SIN(RADIANS(C1))
// Converts polar coordinates (radius B1, angle C1°) to x,y
```

### RADIANS with Engineering Calculations
```spreadsheets
// Pendulum period calculation with degree amplitude
=2*PI()*SQRT(D1/(9.81*COS(RADIANS(E1/2))))
// Calculates period for pendulum length D1, amplitude E1 degrees

// Projectile motion with launch angle in degrees
=F1*SIN(2*RADIANS(G1))/9.81
// Maximum range for initial velocity F1, angle G1 degrees
```

### RADIANS with Circular Calculations
```spreadsheets
// Arc length calculation with central angle in degrees
=H1*RADIANS(I1)
// Arc length for radius H1, central angle I1 degrees

// Sector area with degree angle
=0.5*J1^2*RADIANS(K1)
// Sector area for radius J1, central angle K1 degrees
```
