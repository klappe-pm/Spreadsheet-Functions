---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - engineering
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-17
  - - aliases
    - []
  - - tags
    - []
---
# BESSELJ

## BESSELJ Description

Returns the Bessel function of the first kind Jn(x), which provides oscillatory solutions to differential equations in cylindrical coordinates. Essential for vibration analysis, wave propagation, and acoustic problems in circular geometries. Used extensively in mechanical engineering, physics, and signal processing for modeling periodic phenomena with radial symmetry.

> [!f(x)] BESSELJ Syntax
>
> ```spreadsheets
> BESSELJ(x, n)
> ```
>
> **Parameters:**
> - `x` (required): The value at which to evaluate the function (real number)
> - `n` (required): The order of the Bessel function (non-negative integer)

> [!f(x)] BESSELJ Examples
>
> ```spreadsheets
> // Basic Bessel function evaluations
> BESSELJ(1, 0) → 0.765
> 
> // First order evaluation
> BESSELJ(1, 1) → 0.440
> 
> // Higher order functions
> BESSELJ(2, 2) → 0.353
> 
> // Small argument behavior
> BESSELJ(0.1, 0) → 0.998
> 
> // Zeros of Bessel functions
> BESSELJ(2.405, 0) → 0.000
> 
> // Vibration analysis
> BESSELJ(3.832, 1) → 0.000
> 
> // Acoustic applications
> BESSELJ(1.841, 1) → 0.582
> ```

## Use Cases

### [[Vibration analysis]]
- **Circular plate vibrations**: Analyze natural frequencies and mode shapes of circular plates, drums, and membranes
- **Shaft torsional vibration**: Calculate critical speeds and resonance frequencies in rotating machinery
- **Acoustic cavity analysis**: Model sound wave patterns in circular chambers and cylindrical resonators
- **Seismic wave propagation**: Analyze ground motion patterns and structural response in circular foundations

### [[Wave propagation and acoustics]]
- **Circular waveguide analysis**: Calculate propagation constants and field distributions in cylindrical waveguides
- **Antenna radiation patterns**: Design circular and cylindrical antenna elements with specific directivity characteristics
- **Ultrasonic testing**: Model wave scattering and reflection from cylindrical defects in materials
- **Underwater acoustics**: Analyze sonar beam patterns and acoustic scattering from cylindrical targets

### [[Heat transfer and fluid mechanics]]
- **Transient heat conduction**: Solve time-dependent temperature distributions in cylindrical geometries
- **Fluid flow in pipes**: Analyze oscillatory flow patterns and pressure fluctuations in circular ducts
- **Thermal stress analysis**: Calculate temperature-induced stresses in cylindrical pressure vessels
- **Convection heat transfer**: Model heat transfer coefficients and Nusselt numbers in circular configurations

## Related

### Similar Functions

- [[BESSELI]] - Modified Bessel function of the first kind for exponential solutions in cylindrical coordinates
- [[BESSELY]] - Bessel function of the second kind for complete solution sets in boundary value problems
- [[BESSELK]] - Modified Bessel function of the second kind for exponentially decaying solutions
- [[COMPLEX]] - Creates complex arguments for Bessel function applications in AC circuit analysis

## Mathematical Analysis Functions

### [[BESSELI]]
Complements BESSELJ for complete solution sets in modified cylindrical coordinate problems. BESSELI provides exponential solutions while BESSELJ provides oscillatory solutions.

```spreadsheets
// Complete modified equation solution
=BESSELJ(A1, 0) + BESSELI(A1, 0)
// Combines oscillatory and exponential components

// Boundary condition matching
=IF(A1<PI(), BESSELJ(A1, 1), BESSELI(A1, 1))
// Selects appropriate function based on argument

// Engineering design comparison
=MAX(ABS(BESSELJ(B1, 0)), ABS(BESSELI(B1, 0)))
// Finds dominant term in solution
```

### [[BESSELY]]  
Works with BESSELJ to form complete solutions for Bessel differential equations. BESSELY provides the second linearly independent solution for boundary value problems.

```spreadsheets
// General Bessel equation solution
=BESSELJ(A1, 1)*B1 + BESSELY(A1, 1)*C1
// General solution with arbitrary constants

// Vibration mode analysis
=BESSELJ(ωn*R1, n) + BESSELY(ωn*R1, n)*K1
// Complete vibration mode with boundary conditions

// Acoustic resonance calculation
=BESSELJ(A1, 0)/BESSELY(A1, 0)
// Ratio for resonance condition analysis
```

## Engineering Calculation Functions

### [[COS]]
Combined with BESSELJ for complete cylindrical coordinate solutions. COS provides time-harmonic variation while BESSELJ provides spatial distribution in vibration and wave problems.

```spreadsheets
// Vibration mode shape
=BESSELJ(ωn*R1, n)*COS(ωn*T1)
// Complete time-dependent vibration solution

// Acoustic pressure field
=BESSELJ(k*R1, 0)*COS(ω*T1 - k*Z1)
// Sound wave propagation in cylindrical geometry

// Electromagnetic field distribution
=BESSELJ(β*R1, m)*COS(m*θ1)*COS(ω*T1)
// Complete field solution in cylindrical waveguide
```

### [[SIN]]
Works with BESSELJ for angular variations in cylindrical coordinate systems. SIN provides circumferential dependence while BESSELJ provides radial distribution.

```spreadsheets
// Complete cylindrical solution
=BESSELJ(A1*R1, B1)*SIN(B1*θ1)
// Radial-angular separation in cylindrical coordinates

// Membrane vibration mode
=BESSELJ(ωn*R1, n)*SIN(n*θ1)*SIN(ωn*T1)
// Complete vibration mode with angular dependence

// Heat conduction with angular variation
=BESSELJ(A1*R1, n)*SIN(n*θ1)*EXP(-α*A1^2*T1)
// Temperature distribution with angular and time dependence
```

## Validation and Analysis Functions

### [[IF]]
Combined with BESSELJ for conditional evaluation and zero-finding in engineering applications. IF enables appropriate function evaluation and parameter validation.

```spreadsheets
// Zero detection for resonance analysis
=IF(ABS(BESSELJ(A1, B1))<0.001, "Resonance frequency", "Normal operation")
// Identifies Bessel function zeros for resonance conditions

// Argument range validation
=IF(A1>=0, BESSELJ(A1, B1), "Invalid argument")
// Ensures proper argument domain

// Solution branch selection
=IF(C1="oscillatory", BESSELJ(A1, B1), BESSELI(A1, B1))
// Selects oscillatory vs exponential solution
```

### [[ABS]]
Works with BESSELJ for magnitude calculations and zero-finding algorithms. ABS enables proper amplitude analysis and root-finding in engineering applications.

```spreadsheets
// Amplitude calculation
=ABS(BESSELJ(A1, B1))
// Magnitude of oscillatory solution

// Zero-finding for resonance
=MIN(ABS(BESSELJ(A1:A100, B1)))
// Finds approximate zero location

// Error analysis
=ABS(BESSELJ(A1, B1) - BESSELJ(C1, B1))
// Calculates solution differences
```

## Physical Modeling Functions

### [[PI]]
Combined with BESSELJ for proper scaling in circular geometry applications. PI provides geometric scaling factors and natural frequency calculations.

```spreadsheets
// Natural frequency calculation
=BESSELJ(PI()*A1*B1, 0)
// Proper frequency scaling for circular modes

// Circumferential mode analysis
=BESSELJ(A1, B1)*COS(2*PI()*C1*θ1)
// Angular variation with circumferential modes

// Wavelength normalization
=BESSELJ(2*PI()*R1/λ1, n)
// Normalized radial coordinate by wavelength
```

### [[SQRT]]
Works with BESSELJ for dimensional scaling in physical applications. SQRT provides proper argument scaling for frequency and wave number calculations.

```spreadsheets
// Frequency domain scaling
=BESSELJ(SQRT(A1*B1), 0)
// Proper dimensional scaling for vibration analysis

// Wave propagation constant
=BESSELJ(SQRT(ω^2/c^2 - k^2)*R1, 0)
// Propagation constant in cylindrical waveguide

// Heat equation scaling
=BESSELJ(SQRT(A1/α1)*R1, 0)
// Scaled argument for heat conduction problems
```

## Commonly Used With Functions Examples

### Circular Plate Vibration Analysis
```spreadsheets
// Natural frequency and mode shape calculation
=LET(ωn, SQRT(A1*B1)*C1, 
     "Mode (" & D1 & "," & E1 & "): f = " & ROUND(ωn/(2*PI()), 2) & " Hz" & 
     " | Amplitude: " & ROUND(BESSELJ(A1*R1, D1), 3) & " at r=" & R1)
// Complete frequency and amplitude analysis
```

### Acoustic Waveguide Design
```spreadsheets
// Cutoff frequency and field distribution
="Cutoff: " & IF(BESSELJ(2.405, 0)<0.001, "Above", "Below") & 
 " | Field: " & ROUND(BESSELJ(A1*B1, C1), 4) & 
 " | Attenuation: " & ROUND(-20*LOG10(ABS(BESSELJ(A1*B1, C1))), 2) & " dB"
// Complete waveguide analysis with propagation characteristics
```

### Heat Transfer in Cylindrical Geometry
```spreadsheets
// Temperature distribution with time evolution
=LET(T, EXP(-α*A1^2*t)*BESSELJ(A1*r, 0),
     "T(r,t) = " & ROUND(T0*T, 2) & "°C" & 
     " | Center temp: " & ROUND(T0*EXP(-α*A1^2*t), 2) & "°C" &
     " | Rate: " & ROUND(-α*A1^2*T0*EXP(-α*A1^2*t), 3) & "°C/s")
// Complete transient temperature analysis
```

### Structural Resonance Detection
```spreadsheets
// Resonance frequency identification and analysis
=LET(f, A1, Bessel_val, BESSELJ(2*PI()*f*R1/c, 0),
     IF(ABS(Bessel_val)<0.01, 
        "RESONANCE at " & f & " Hz | Amplitude: " & ROUND(1/ABS(Bessel_val), 1),
        "f = " & f & " Hz | Response: " & ROUND(ABS(Bessel_val), 4)))
// Identifies resonance conditions and response amplitudes
```

### Antenna Pattern Analysis
```spreadsheets
// Radiation pattern calculation with beamwidth analysis
="Pattern: " & ROUND(ABS(BESSELJ(A1*SIN(θ1), 0)), 4) & 
 " | 3dB beamwidth: " & ROUND(2*ASIN(1.22/A1)*180/PI(), 1) & "°" &
 " | Sidelobe level: " & ROUND(20*LOG10(ABS(BESSELJ(3.83, 0))), 1) & " dB"
// Complete antenna pattern analysis with key parameters
```
