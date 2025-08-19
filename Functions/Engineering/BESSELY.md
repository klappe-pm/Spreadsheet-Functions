---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: engineering
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# BESSELY

## BESSELY Description

Returns the Bessel function of the second kind Yn(x), also known as the Neumann function or Weber function. Provides the second linearly independent solution to Bessel differential equations in cylindrical coordinates. Essential for boundary value problems where both Bessel functions are needed to satisfy boundary conditions, particularly in electromagnetic and acoustic applications.

> [!f(x)] BESSELY Syntax
>
> ```spreadsheets
> BESSELY(x, n)
> ```
>
> **Parameters:**
> - `x` (required): The value at which to evaluate the function (positive real number)
> - `n` (required): The order of the Bessel function (non-negative integer)

> [!f(x)] BESSELY Examples
>
> ```spreadsheets
> // Basic Bessel function of second kind
> BESSELY(1, 0) → 0.088
> 
> // First order evaluation
> BESSELY(1, 1) → -0.781
> 
> // Higher order functions
> BESSELY(2, 2) → -0.617
> 
> // Small argument behavior (singular at origin)
> BESSELY(0.1, 0) → -1.534
> 
> // Large argument asymptotic behavior
> BESSELY(5, 0) → -0.309
> 
> // Electromagnetic applications
> BESSELY(2.405, 0) → 0.520
> 
> // Acoustic resonance analysis
> BESSELY(3.832, 1) → 0.403
> ```

## Use Cases

### [[Electromagnetic waveguide analysis]]
- **Cylindrical waveguide modes**: Calculate complete modal solutions requiring both BESSELJ and BESSELY functions
- **Antenna impedance analysis**: Determine input impedance and radiation characteristics of cylindrical antenna elements
- **Scattering analysis**: Model electromagnetic scattering from cylindrical objects and obstacles
- **Coaxial transmission lines**: Analyze field distributions and characteristic impedance in coaxial cable geometries

### [[Acoustic and vibration problems]]
- **Sound radiation from cylinders**: Calculate acoustic radiation patterns and far-field sound pressure levels
- **Cylindrical cavity resonance**: Analyze resonant frequencies and quality factors in cylindrical acoustic cavities
- **Structural vibration**: Model vibration transmission and isolation in cylindrical mechanical systems
- **Ultrasonic transducers**: Design cylindrical ultrasonic elements with optimized radiation characteristics

### [[Heat transfer boundary value problems]]
- **Multi-layer cylindrical systems**: Solve temperature distributions in composite cylindrical structures
- **Convective boundary conditions**: Model heat transfer with convection at cylindrical boundaries
- **Thermal wave propagation**: Analyze periodic temperature variations and thermal penetration depth
- **Heat exchanger optimization**: Calculate effectiveness and thermal performance in cylindrical heat exchanger configurations

## Related

### Similar Functions

- [[BESSELJ]] - Bessel function of the first kind, paired with BESSELY for complete solutions
- [[BESSELI]] - Modified Bessel function of the first kind for exponential solutions
- [[BESSELK]] - Modified Bessel function of the second kind for decaying solutions
- [[COMPLEX]] - Creates complex numbers for advanced Bessel function applications

## Mathematical Analysis Functions

### [[BESSELJ]]
Essential complement to BESSELY for forming complete solutions to Bessel differential equations. BESSELJ and BESSELY together provide the general solution to boundary value problems.

```spreadsheets
// General Bessel equation solution
=BESSELJ(A1, B1)*C1 + BESSELY(A1, B1)*D1
// Complete solution with arbitrary constants

// Wronskian calculation for linear independence
=BESSELJ(A1, B1)*BESSELY(A1, B1+1) - BESSELJ(A1, B1+1)*BESSELY(A1, B1)
// Verifies linear independence of solutions

// Boundary condition matching
=BESSELJ(A1, 0)*BESSELY(B1, 0) - BESSELJ(B1, 0)*BESSELY(A1, 0)
// Determinant for boundary value problems
```

### [[PI]]
Combined with BESSELY for proper normalization and Green's function calculations. PI provides geometric factors essential for physical interpretations.

```spreadsheets
// Green's function calculation
=BESSELY(A1, 0)/(PI()*BESSELJ(A1, 0))
// Normalized Green's function for cylindrical domains

// Hankel function construction
=BESSELJ(A1, B1) + COMPLEX(0,1)*BESSELY(A1, B1)
// Creates Hankel function from Bessel functions

// Radiation impedance calculation
=PI()*A1*BESSELY(A1, B1)/BESSELJ(A1, B1)
// Acoustic radiation impedance factor
```

## Engineering Calculation Functions

### [[COMPLEX]]
Works with BESSELY to form Hankel functions for radiation and scattering problems. COMPLEX enables advanced electromagnetic and acoustic calculations.

```spreadsheets
// Hankel function of first kind
=BESSELJ(A1, B1) + COMPLEX(0,1)*BESSELY(A1, B1)
// Outward propagating wave solution

// Hankel function of second kind
=BESSELJ(A1, B1) - COMPLEX(0,1)*BESSELY(A1, B1)
// Inward propagating wave solution

// Radiation pattern calculation
=ABS(BESSELJ(A1, 0) + COMPLEX(0,1)*BESSELY(A1, 0))^2
// Far-field radiation intensity
```

### [[ATAN2]]
Combined with BESSELY and BESSELJ for phase calculations in wave problems. ATAN2 provides proper phase angles for complex wave solutions.

```spreadsheets
// Phase angle calculation
=ATAN2(BESSELY(A1, B1), BESSELJ(A1, B1))
// Phase of cylindrical wave solution

// Reflection coefficient phase
=ATAN2(BESSELY(A1, 0)*BESSELJ(B1, 1) - BESSELY(B1, 1)*BESSELJ(A1, 0),
        BESSELJ(A1, 0)*BESSELJ(B1, 1) - BESSELJ(B1, 0)*BESSELJ(A1, 1))
// Phase of reflection coefficient

// Impedance phase calculation
=ATAN2(BESSELY(A1, B1), BESSELJ(A1, B1))*180/PI()
// Phase angle in degrees
```

## Validation and Analysis Functions

### [[IF]]
Combined with BESSELY for singularity handling and conditional evaluation. IF enables proper function evaluation near the origin where BESSELY is singular.

```spreadsheets
// Singularity avoidance at origin
=IF(A1>0.001, BESSELY(A1, B1), "Singular at origin")
// Handles singularity at x=0

// Solution branch selection
=IF(C1="interior", BESSELJ(A1, B1), BESSELJ(A1, B1)*D1 + BESSELY(A1, B1)*E1)
// Interior vs exterior solutions

// Asymptotic approximation switching
=IF(A1>10, SQRT(2/(PI()*A1))*SIN(A1-PI()*B1/2-PI()/4), BESSELY(A1, B1))
// Uses asymptotic form for large arguments
```

### [[ABS]]
Works with BESSELY for magnitude calculations and amplitude analysis. ABS ensures proper handling of the oscillatory and sometimes negative values of BESSELY.

```spreadsheets
// Amplitude calculation
=ABS(BESSELY(A1, B1))
// Magnitude of oscillatory solution

// Maximum amplitude finding
=MAX(ABS(BESSELY(A1:A100, B1)))
// Finds maximum amplitude over range

// Error analysis
=ABS(BESSELY(A1, B1) - BESSELY(C1, B1))
// Calculates differences between function values
```

## Physical Modeling Functions

### [[SIN]]
Combined with BESSELY for complete harmonic solutions in cylindrical coordinates. SIN provides time or angular dependence while BESSELY provides spatial distribution.

```spreadsheets
// Time-harmonic wave solution
=BESSELY(k*R1, 0)*SIN(ω*T1)
// Harmonic wave with cylindrical symmetry

// Angular variation with radial dependence
=BESSELY(A1*R1, n)*SIN(n*θ1)
// Complete cylindrical coordinate solution

// Vibration mode with phase
=BESSELY(ωn*R1, n)*SIN(ωn*T1 + φ1)
// Vibration mode with phase angle
```

### [[COS]]
Works with BESSELY for even harmonic solutions and standing wave patterns. COS provides complementary phase relationships for complete wave descriptions.

```spreadsheets
// Standing wave pattern
=BESSELY(k*R1, 0)*COS(ω*T1)
// Standing wave in cylindrical geometry

// Even angular modes
=BESSELY(A1*R1, n)*COS(n*θ1)
// Even symmetry angular modes

// Reflection interference pattern
=BESSELJ(k*R1, 0)*COS(ω*T1) + BESSELY(k*R1, 0)*SIN(ω*T1)
// Combined incident and reflected waves
```

## Commonly Used With Functions Examples

### Electromagnetic Waveguide Mode Analysis
```spreadsheets
// Complete modal solution with cutoff analysis
=LET(β, SQRT(k^2 - (χ/a)^2), 
     H_field, BESSELJ(χ*r/a, m)*COS(m*φ) + C*BESSELY(χ*r/a, m)*COS(m*φ),
     cutoff, IF(χ/a > k, "Below cutoff", "Propagating"),
     "Mode: TM" & m & n & " | " & cutoff & " | H = " & ROUND(H_field, 4))
// Complete waveguide mode analysis with field and cutoff status
```

### Acoustic Radiation from Cylindrical Source
```spreadsheets
// Far-field sound pressure and directivity calculation
=LET(H1, BESSELJ(ka, 0) + COMPLEX(0,1)*BESSELY(ka, 0),
     p_far, ABS(H1)*p0/(4*PI()*r),
     directivity, 20*LOG10(ABS(H1)/MAX(ABS_range)),
     "Pressure: " & ROUND(p_far, 4) & " Pa | Directivity: " & ROUND(directivity, 1) & " dB")
// Complete acoustic radiation analysis with pressure and directivity
```

### Heat Transfer in Multi-layer Cylinder
```spreadsheets
// Temperature distribution across cylindrical layers
="Layer " & n & ": T = " & ROUND(A*BESSELJ(λ*r, 0) + B*BESSELY(λ*r, 0), 2) & "°C" &
 " | Heat flux: " & ROUND(-k*λ*(A*BESSELJ(λ*r, 1) + B*BESSELY(λ*r, 1)), 1) & " W/m²" &
 " | Interface temp: " & ROUND(T_interface, 2) & "°C"
// Temperature profile and heat flux with interface conditions
```

### Vibration Analysis of Cylindrical Structure
```spreadsheets
// Natural frequency and mode shape calculation
=LET(freq, SQRT(λ^2*E/(ρ*a^2))/(2*PI()),
     mode_shape, BESSELJ(λ*r/a, n)*COS(n*θ) + C*BESSELY(λ*r/a, n)*COS(n*θ),
     "f" & m & n & " = " & ROUND(freq, 2) & " Hz | Mode: " & ROUND(mode_shape, 4) &
     " | Node count: " & n)
// Complete vibration mode analysis with frequency and shape
```

### Electromagnetic Scattering Cross-Section
```spreadsheets
// Scattering cross-section calculation for cylindrical obstacle
=LET(a_n, -BESSELJ(ka, n)/BESSELY(ka, n),
     σ_scat, 4/(ka)*SUM(ABS(a_n)^2),
     efficiency, σ_scat/(2*a),
     "RCS: " & ROUND(σ_scat, 4) & " m² | Efficiency: " & ROUND(efficiency, 3) &
     " | ka: " & ROUND(ka, 2))
// Complete electromagnetic scattering analysis with cross-section and efficiency
```
