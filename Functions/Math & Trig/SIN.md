---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: math & trig
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# SIN

## SIN Description

Returns the sine of an angle in radians. The sine function represents the y-coordinate of a point on the unit circle and is fundamental for wave analysis, circular motion, and periodic modeling in engineering and scientific applications.

> [!f(x)] SIN Syntax
>
> ```spreadsheets
> SIN(number)
> ```
>
> **Parameters:**
> - `number` (required): The angle in radians for which you want the sine

> [!f(x)] SIN Examples
>
> ```spreadsheets
> // Sine of π/6 radians (30 degrees)
> SIN(PI()/6) → 0.5
> 
> // Sine of π/2 radians (90 degrees) 
> SIN(PI()/2) → 1
> 
> // Sine with degree conversion
> SIN(RADIANS(45)) → 0.7071 (sin of 45 degrees)
> 
> // Sine wave generation
> SIN(2*PI()*A1/12) → monthly sine wave pattern
> 
> // Zero crossing
> SIN(PI()) → 0 (approximately)
> ```

## Use Cases

### [[Wave and oscillation modeling]]
- **Signal processing**: Generate sine waves for audio processing, telecommunications, and frequency analysis
- **Seasonal analysis**: Model cyclical business patterns, temperature variations, and periodic trends
- **Vibration analysis**: Calculate harmonic motion in mechanical systems and structural engineering
- **AC circuit analysis**: Determine voltage and current waveforms in electrical engineering applications

### [[Geometric calculations]]  
- **Coordinate transformations**: Convert between polar and rectangular coordinates for mapping and navigation
- **Triangle geometry**: Calculate side lengths and areas in surveying and architectural applications
- **Projectile motion**: Determine vertical components of velocity and displacement in physics simulations
- **Circular motion**: Analyze position and velocity components in rotational mechanics

### [[Engineering applications]]
- **Structural analysis**: Calculate stress components and load distributions in beam and frame analysis
- **Optics and waves**: Model light propagation, interference patterns, and diffraction phenomena
- **Control systems**: Design feedback loops and analyze system stability in automation engineering
- **Robotics**: Calculate joint positions and end-effector coordinates in robotic arm control

## Related

### Similar Functions

- [[COS]] - Cosine function, complementary to SIN with 90-degree phase shift for complete trigonometric analysis
- [[TAN]] - Tangent function equal to SIN/COS, useful for slope and angle calculations
- [[ASIN]] - Arcsine (inverse sine), converts sine values back to angles for reverse calculations
- [[SINH]] - Hyperbolic sine, related to exponential functions for advanced mathematical modeling
- [[PI]] - Provides π constant essential for radian-based sine calculations and periodic functions

## Trigonometric Functions

### [[COS]]
Complementary to SIN with 90-degree phase relationship, essential for complete harmonic analysis and coordinate transformations.

```spreadsheets
// Unit circle coordinates (x, y)
=COS(A1) & ", " & SIN(A1)
// Generates (x, y) coordinates for angle A1 radians

// Phase relationship verification
=SIN(B1) - COS(B1-PI()/2)
// Should equal zero (sine leads cosine by π/2)

// Vector component calculations
=C1*COS(D1) & " (horizontal), " & C1*SIN(D1) & " (vertical)"
// Breaks vector C1 into components at angle D1
```

### [[TAN]]
Related to SIN through TAN = SIN/COS relationship, useful for slope calculations and complementary trigonometric analysis.

```spreadsheets
// Verify trigonometric identity
=TAN(A1) - SIN(A1)/COS(A1)
// Should equal zero (fundamental trig identity)

// Slope from sine and cosine
=SIN(B1)/COS(B1) & " slope = " & TAN(B1)
// Shows slope calculation using sine and cosine

// Projectile trajectory analysis
=C1*SIN(D1)/(9.81*COS(D1)^2)*E1
// Uses sine for trajectory calculations
```

## Conversion Functions

### [[RADIANS]]
Essential for converting degree measurements to radians for SIN function input, since SIN requires radian angles.

```spreadsheets
// Convert degrees to sine value
=SIN(RADIANS(30))
// Sine of 30 degrees (converted to radians)

// Sine wave with degree-based period
=SIN(RADIANS(A1*360/365))
// Daily sine wave over yearly cycle

// Angular analysis with degree inputs
=SIN(RADIANS(B1)) & " at " & B1 & " degrees"
// Shows sine value with degree reference
```

### [[PI]]
Fundamental constant for radian-based sine calculations, essential for periodic functions and wave generation.

```spreadsheets
// Standard sine wave generation
=SIN(2*PI()*C1/D1)
// Creates sine wave with period D1 at position C1

// Harmonic frequency analysis
=SIN(2*PI()*E1*F1)
// Sine wave with frequency E1 at time F1

// Phase-shifted sine waves
=SIN(2*PI()*G1 + H1)
// Sine wave with phase shift H1 radians
```

## Commonly Used With Functions Examples

### SIN with Wave Generation
```spreadsheets
// Monthly seasonal pattern
=50 + 20*SIN(2*PI()*(A1-1)/12)
// Creates seasonal variation around baseline 50

// Damped oscillation
=B1*EXP(-C1)*SIN(2*PI()*D1)
// Exponentially decaying sine wave
```

### SIN with Engineering Calculations
```spreadsheets
// Vertical force component
=E1*SIN(RADIANS(F1)) & " N vertical force"
// Calculates vertical component of angled force

// AC voltage calculation
=G1*SIN(2*PI()*60*H1) & " V instantaneous"
// 60 Hz AC voltage at time H1 seconds
```

### SIN with Coordinate Geometry
```spreadsheets
// Polar to rectangular conversion
=I1*COS(J1) & ", " & I1*SIN(J1)
// Converts polar coordinates (radius I1, angle J1) to (x,y)

// Circular motion position
=K1 + L1*SIN(2*PI()*M1/N1)
// Position on circle with center K1, radius L1, period N1
```
