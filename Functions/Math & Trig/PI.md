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

# PI

## PI Description

Returns the mathematical constant π (pi) with full precision, approximately 3.14159265358979. This constant represents the ratio of a circle's circumference to its diameter and is essential for geometric calculations, statistical distributions, and engineering applications.

> [!f(x)] PI Syntax
>
> ```spreadsheets
> PI()
> ```
>
> **Parameters:**
> - None required - PI() takes no arguments

> [!f(x)] PI Examples
>
> ```spreadsheets
> // Basic pi value
> PI() → 3.14159265358979
> 
> // Circle area calculation
> PI() * 5^2 → 78.5398 (area of circle with radius 5)
> 
> // Circle circumference
> 2 * PI() * 10 → 62.8318 (circumference with radius 10)
> 
> // Convert degrees to radians
> 90 * PI() / 180 → 1.5708 (90 degrees in radians)
> 
> // Volume of cylinder
> PI() * 3^2 * 8 → 226.195 (cylinder radius=3, height=8)
> ```

## Use Cases

### [[Geometric calculations]]
- **Circle measurements**: Calculate areas, circumferences, and arc lengths for design and engineering projects
- **Cylinder and sphere volumes**: Determine storage capacities, material requirements, and space planning calculations
- **Angular measurements**: Convert between degrees and radians for trigonometric functions and rotation calculations  
- **Ellipse calculations**: Compute approximate areas and perimeters for architectural and design applications

### [[Engineering and physics]]  
- **Wave analysis**: Calculate frequencies, wavelengths, and amplitudes in signal processing and acoustics
- **Mechanical design**: Determine gear ratios, pulley systems, and rotational mechanics for machinery design
- **Electrical calculations**: Compute impedances, resonant frequencies, and AC circuit parameters
- **Heat transfer**: Calculate thermal coefficients and heat distribution in cylindrical and spherical systems

### [[Statistical analysis]]
- **Normal distribution**: Generate probability densities and confidence intervals using the Gaussian constant
- **Monte Carlo simulations**: Create random sampling algorithms requiring π for geometric probability calculations
- **Quality control charts**: Establish control limits and process capabilities using statistical formulas involving π
- **Sampling theory**: Calculate sample sizes and margins of error for circular or cyclical data patterns

## Related

### Similar Functions

- [[E]] - Returns Euler's number (e ≈ 2.718), another fundamental mathematical constant for exponential calculations
- [[RADIANS]] - Converts degrees to radians using π in the conversion formula, complementary to PI()
- [[DEGREES]] - Converts radians to degrees, often used in conjunction with PI() for angle calculations
- [[SQRT]] - Returns square roots, frequently combined with PI() in geometric and statistical formulas
- [[LN]] - Natural logarithm function, often paired with PI() in advanced mathematical and statistical calculations

## Trigonometric Functions

### [[SIN]]
Combined with PI() to calculate sine values for angles expressed in radians or to work with periodic functions and wave calculations.

```spreadsheets
// Sine wave calculation at different phases
=SIN(2*PI()*A1/12)
// Creates sine wave with period of 12 units

// Maximum sine value occurs at π/2 radians
=SIN(PI()/2)
// Returns 1 (maximum sine value)

// Sine of 30 degrees using pi conversion
=SIN(30*PI()/180)
// Converts 30 degrees to radians, then calculates sine (0.5)
```

### [[COS]]
Works with PI() for cosine calculations, phase relationships, and circular motion analysis in engineering and physics applications.

```spreadsheets
// Cosine wave with phase shift
=COS(2*PI()*B1/24 + PI()/4)
// 24-hour cosine cycle with 45-degree phase shift

// Calculate x-coordinate on unit circle
=COS(A2*PI()/180)
// Converts degrees to radians for cosine calculation

// Harmonic analysis with multiple frequencies
=COS(2*PI()*C1) + 0.5*COS(4*PI()*C1)
// Combines fundamental and second harmonic frequencies
```

## Geometric Functions

### [[SQRT]]
Frequently used with PI() in geometric formulas, particularly for circle and sphere calculations requiring square roots of pi-based expressions.

```spreadsheets
// Standard deviation of circular normal distribution
=SQRT(2*PI())*A1
// Calculates normalizing factor for circular statistics

// Radius from area (inverse area formula)
=SQRT(B1/PI())
// Given area B1, calculates radius of circle

// Surface area to volume ratio for sphere
=SQRT(36*PI()*C1^2)/(4*PI()*C1^3/3)
// Calculates surface-to-volume ratio for sphere with radius C1
```

### [[POWER]]
Combined with PI() for complex geometric calculations involving exponents, particularly in volume, surface area, and statistical formulas.

```spreadsheets
// Volume of sphere
=4*PI()*POWER(A1,3)/3
// Complete sphere volume formula with radius A1

// Normal distribution probability density
=1/(B1*SQRT(2*PI()))*EXP(-0.5*POWER((C1-D1)/B1,2))
// Full normal distribution formula with mean D1, std dev B1

// Compound interest with circular time periods
=E1*POWER(1+F1/(2*PI()),2*PI()*G1)
// Interest compounded continuously over circular periods
```

## Commonly Used With Functions Examples

### PI with Geometric Calculations
```spreadsheets
// Complete circle analysis
={"Area: "&PI()*A2^2; "Circumference: "&2*PI()*A2; "Diameter: "&2*A2}
// Creates comprehensive circle measurements for radius A2

// Tank capacity calculation (cylindrical)
=PI()*B2^2*C2*0.264172
// Volume in gallons for tank with radius B2, height C2
```

### PI with Trigonometric Analysis
```spreadsheets
// Seasonal temperature model
=D2+E2*SIN(2*PI()*(F2-G2)/365.25)
// Models temperature with base D2, amplitude E2, day F2, phase G2

// Pendulum period calculation
=2*PI()*SQRT(H2/9.81)
// Period of simple pendulum with length H2 meters
```

### PI with Statistical Applications
```spreadsheets
// Chi-square critical value approximation
=SQRT(2*I2)*NORM.S.INV(J2)+2*I2/3-1/(6*SQRT(2*PI()*I2))
// Approximates chi-square critical values for df=I2, probability=J2

// Circular mean calculation
=ATAN2(SUMPRODUCT(SIN(K2:K10*PI()/180)), SUMPRODUCT(COS(K2:K10*PI()/180)))*180/PI()
// Calculates mean of angular measurements in degrees
```
