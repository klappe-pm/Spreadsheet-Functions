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
# BESSELI

## BESSELI Description

Returns the modified Bessel function of the first kind In(x), also known as the hyperbolic Bessel function. Essential for solving heat conduction, vibration, and wave propagation problems in cylindrical coordinates. Used extensively in physics, mechanical engineering, and signal processing for modeling exponential growth/decay phenomena in circular geometries.

> [!f(x)] BESSELI Syntax
>
> ```spreadsheets
> BESSELI(x, n)
> ```
>
> **Parameters:**
> - `x` (required): The value at which to evaluate the function (real number)
> - `n` (required): The order of the Bessel function (non-negative integer)

> [!f(x)] BESSELI Examples
>
> ```spreadsheets
> // Basic modified Bessel function evaluations
> BESSELI(1, 0) → 1.266
> 
> // First order evaluation
> BESSELI(1, 1) → 0.565
> 
> // Higher order functions
> BESSELI(2, 2) → 0.688
> 
> // Small argument approximation
> BESSELI(0.1, 0) → 1.003
> 
> // Engineering applications
> BESSELI(5, 0) → 27.24
> 
> // Heat transfer analysis
> BESSELI(3.83, 1) → 9.759
> 
> // Vibration analysis
> BESSELI(2.405, 0) → 2.279
> ```

## Use Cases

### [[Heat transfer analysis]]
- **Cylindrical heat conduction**: Model temperature distribution in pipes, rods, and cylindrical vessels with internal heat generation
- **Transient heat transfer**: Analyze time-dependent temperature profiles in circular geometries during heating/cooling processes  
- **Heat exchanger design**: Calculate temperature profiles and heat transfer coefficients in tubular heat exchangers
- **Thermal stress analysis**: Determine temperature-induced stresses in cylindrical components and pressure vessels

### [[Vibration and acoustics]]
- **Circular membrane vibration**: Analyze natural frequencies and mode shapes of circular plates, drums, and diaphragms
- **Cylindrical cavity acoustics**: Model sound wave propagation and resonance in cylindrical enclosures and pipes
- **Structural dynamics**: Calculate dynamic response of circular structures to harmonic and transient loading
- **Wave propagation**: Analyze acoustic and elastic wave transmission in cylindrical waveguides and ducts

### [[Signal processing and electromagnetics]]
- **Antenna design**: Calculate radiation patterns and impedance characteristics of cylindrical antenna elements
- **Electromagnetic wave propagation**: Model field distributions in cylindrical waveguides and coaxial cables
- **Beamforming applications**: Design circular antenna arrays with optimized directivity patterns
- **Radar signal processing**: Analyze target scattering from cylindrical objects and clutter suppression

## Related

### Similar Functions

- [[BESSELJ]] - Regular Bessel function of the first kind for oscillatory solutions in cylindrical coordinates
- [[BESSELY]] - Bessel function of the second kind for boundary value problems in cylindrical geometry
- [[BESSELK]] - Modified Bessel function of the second kind for exponentially decaying solutions
- [[COMPLEX]] - Creates complex arguments for Bessel function applications in AC analysis

## Mathematical Analysis Functions

### [[BESSELJ]]
Complements BESSELI for complete solution sets in cylindrical coordinate problems. BESSELJ provides oscillatory solutions while BESSELI provides exponential solutions for modified equations.

```spreadsheets
// Complete cylindrical solution
=BESSELI(A1, 0) + BESSELJ(A1, 0)
// Combines modified and regular Bessel functions

// Boundary condition matching
=IF(A1<1, BESSELJ(A1, 1), BESSELI(A1, 1))
// Selects appropriate function based on argument

// Engineering design comparison
=MAX(BESSELI(B1, 0), BESSELJ(B1, 0))
// Finds dominant term in solution
```

### [[BESSELK]]
Works with BESSELI to form complete solutions for modified Bessel differential equations. BESSELK provides the linearly independent solution for exponentially decaying phenomena.

```spreadsheets
// Modified Bessel equation general solution
=BESSELI(A1, 1)*B1 + BESSELK(A1, 1)*C1
// General solution with arbitrary constants

// Heat conduction solution
=BESSELI(SQRT(A1), 0) + BESSELK(SQRT(A1), 0)
// Temperature profile in cylindrical geometry

// Engineering boundary matching
=BESSELI(A1, 2)/BESSELK(A1, 2)
// Ratio for boundary condition analysis
```

## Engineering Calculation Functions

### [[EXP]]
Combined with BESSELI for modeling exponential growth/decay with cylindrical geometry corrections. EXP provides the exponential component while BESSELI adds geometric effects.

```spreadsheets
// Heat generation with geometry
=EXP(-A1*B1)*BESSELI(C1*SQRT(A1), 0)
// Temperature with time decay and radial distribution

// Signal decay in cylindrical waveguide
=EXP(-A1*L1)*BESSELI(B1*R1, 1)
// Amplitude decay with radial variation

// Stress concentration factor
=EXP(A1)*BESSELI(B1, 0)
// Stress amplification in cylindrical notch
```

### [[SQRT]]
Works with BESSELI for scaling arguments in engineering applications. SQRT provides proper dimensional scaling for Bessel function arguments in physical problems.

```spreadsheets
// Heat equation scaling
=BESSELI(SQRT(A1*B1), 0)
// Proper dimensional argument for heat transfer

// Vibration frequency scaling
=BESSELI(SQRT(ω*L1), 1)
// Scaled frequency parameter for dynamics

// Electromagnetic field scaling
=BESSELI(SQRT(A1/B1), 0)
// Scaled propagation constant
```

## Validation and Analysis Functions

### [[IF]]
Combined with BESSELI for conditional evaluation based on argument ranges and engineering limits. IF enables appropriate function selection and parameter validation.

```spreadsheets
// Argument range validation
=IF(A1>=0, BESSELI(A1, B1), "Invalid argument")
// Ensures non-negative arguments

// Engineering approximation
=IF(A1<0.1, 1+A1^2/(4*(B1+1)), BESSELI(A1, B1))
// Uses small argument approximation when appropriate

// Solution branch selection
=IF(C1="growing", BESSELI(A1, B1), BESSELK(A1, B1))
// Selects growing or decaying solution
```

### [[ABS]]
Works with BESSELI for magnitude calculations and ensuring positive arguments. ABS enables proper function evaluation and error handling in engineering applications.

```spreadsheets
// Magnitude calculation
=ABS(BESSELI(A1, B1))
// Ensures positive result for physical quantities

// Symmetric evaluation
=BESSELI(ABS(A1), B1)
// Handles negative arguments properly

// Error magnitude
=ABS(BESSELI(A1, B1) - BESSELI(C1, B1))
// Calculates solution differences
```

## Physical Modeling Functions

### [[PI]]
Combined with BESSELI for proper scaling in circular geometry applications. PI provides geometric scaling factors for radial coordinates and angular frequencies.

```spreadsheets
// Circular frequency scaling
=BESSELI(2*PI()*A1*B1, 0)
// Proper frequency scaling for circular geometry

// Radial coordinate normalization
=BESSELI(PI()*R1/R0, 1)
// Normalized radial coordinate

// Circumferential analysis
=BESSELI(A1, 0)*COS(PI()*B1)
// Angular variation with radial Bessel function
```

### [[SIN]]
Works with BESSELI for complete cylindrical coordinate solutions combining radial and angular components. SIN provides angular variation while BESSELI provides radial distribution.

```spreadsheets
// Complete cylindrical solution
=BESSELI(A1*R1, B1)*SIN(B1*θ1)
// Radial-angular separation in cylindrical coordinates

// Vibration mode shape
=BESSELI(ωn*R1, n)*SIN(n*θ1)*COS(ωn*t)
// Complete vibration mode in cylindrical geometry

// Heat distribution
=BESSELI(A1*R1, 0)*SIN(PI()*Z1/L1)
// Temperature distribution in cylinder
```

## Commonly Used With Functions Examples

### Cylindrical Heat Conduction Analysis
```spreadsheets
// Temperature profile in heated cylinder
=LET(α, A1, r, B1, t, C1, 
     "T(r,t) = " & ROUND(100*EXP(-α*t)*BESSELI(r/SQRT(α*t), 0), 2) & "°C" & 
     " | Max at center: " & ROUND(100*EXP(-α*t), 2) & "°C")
// Complete temperature solution with maximum value
```

### Vibration Analysis of Circular Membrane
```spreadsheets
// Natural frequency calculation
=LET(ωn, SQRT(A1*B1)*C1, 
     "Mode (" & D1 & "," & E1 & "): f = " & ROUND(ωn/(2*PI()), 2) & " Hz" & 
     " | Shape: " & ROUND(BESSELI(A1*R1, D1), 3) & " at r=" & R1)
// Frequency and mode shape evaluation
```

### Electromagnetic Waveguide Design
```spreadsheets
// Field distribution in cylindrical waveguide
="Field strength: " & ROUND(BESSELI(A1*B1, C1), 4) & " | Cutoff: " & 
 IF(BESSELI(2.405, 0)>1, "Above cutoff", "Below cutoff") & 
 " | Loss: " & ROUND(EXP(-D1*L1)*100, 1) & "%"
// Complete field analysis with propagation characteristics
```

### Thermal Stress in Pressure Vessel
```spreadsheets
// Stress concentration at cylindrical discontinuity
=LET(K, BESSELI(A1, 0)/BESSELI(A1, 1),
     "Stress factor: " & ROUND(K, 2) & " | Max stress: " & 
     ROUND(B1*K, 0) & " MPa | Safety factor: " & ROUND(C1/(B1*K), 1))
// Stress concentration analysis with safety assessment
```

### Signal Processing Filter Response
```spreadsheets
// Modified Bessel filter characteristics  
="Response: " & ROUND(BESSELI(A1, B1), 4) & " | -3dB freq: " & 
 ROUND(C1*SQRT(LN(2)), 2) & " Hz | Ripple: " & 
 ROUND(20*LOG10(ABS(BESSELI(A1, B1))), 2) & " dB"
// Complete filter response analysis with key parameters
```
