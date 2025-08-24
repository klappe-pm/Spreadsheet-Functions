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
    - 2025-08-19
  - - aliases
    - []
  - - tags
    - []
---
# COMPLEX

## COMPLEX Description

Creates a complex number from real and imaginary coefficients. Essential for electrical engineering, signal processing, control systems, and advanced mathematical analysis where complex number operations are required. Returns complex numbers in standard a+bi format for use with other complex number functions.

> [!f(x)] COMPLEX Syntax
>
> ```spreadsheets
> COMPLEX(real_num, i_num, [suffix])
> ```
>
> **Parameters:**
> - `real_num` (required): The real coefficient of the complex number
> - `i_num` (required): The imaginary coefficient of the complex number  
> - `suffix` (optional): "i" (default) or "j" to specify imaginary unit notation

> [!f(x)] COMPLEX Examples
>
> ```spreadsheets
> // Basic complex number creation
> COMPLEX(3, 4) → "3+4i"
> 
> // Negative imaginary part
> COMPLEX(5, -2) → "5-2i"
> 
> // Pure imaginary number
> COMPLEX(0, 3) → "3i"
> 
> // Pure real number
> COMPLEX(7, 0) → "7"
> 
> // Engineering notation with j
> COMPLEX(2, 5, "j") → "2+5j"
> 
> // Electrical impedance
> COMPLEX(50, 30) → "50+30i"
> 
> // Signal processing
> COMPLEX(-1, 1.732) → "-1+1.732i"
> ```

## Use Cases

### [[Electrical engineering]]
- **AC circuit analysis**: Create complex impedances combining resistance and reactance for power system analysis
- **Phasor representation**: Model sinusoidal voltages and currents as complex exponentials for circuit calculations
- **Filter design**: Represent poles and zeros in s-domain for analog filter design and stability analysis
- **Power system analysis**: Calculate complex power (P+jQ) for load flow studies and power factor correction

### [[Signal processing]]
- **Fourier transform analysis**: Create frequency domain representations of signals for spectral analysis
- **Digital filter design**: Define complex coefficients for IIR and FIR filter implementations
- **Modulation analysis**: Model complex baseband signals for QAM, PSK, and OFDM communication systems
- **Control system design**: Represent transfer function poles and zeros for stability and performance analysis

### [[Mathematical modeling]]
- **Quantum mechanics**: Create wave function representations and probability amplitude calculations
- **Fluid dynamics**: Model potential flow and complex velocity fields in aerodynamics
- **Vibration analysis**: Represent oscillatory systems with complex eigenvalues and mode shapes
- **Optimization**: Use complex variables in gradient descent and optimization algorithms

## Related

### Similar Functions

- [[IMREAL]] - Extracts the real part of a complex number for component analysis
- [[IMAGINARY]] - Extracts the imaginary part of a complex number for component analysis  
- [[IMABS]] - Calculates the absolute value (magnitude) of a complex number
- [[IMARGUMENT]] - Returns the argument (phase angle) of a complex number in radians
- [[IMCONJUGATE]] - Returns the complex conjugate for impedance and frequency response calculations

## Complex Number Analysis Functions

### [[IMREAL]]
Extracts the real coefficient from complex numbers created by COMPLEX. IMREAL enables separation of real and imaginary components for analysis and validation.

```spreadsheets
// Component extraction
=IMREAL(COMPLEX(3, 4))
// Returns: 3 (real part of 3+4i)

// Validation of complex creation
=IMREAL(COMPLEX(A1, B1)) = A1
// Returns: TRUE if COMPLEX correctly stores real part

// Impedance resistance calculation
=IMREAL(COMPLEX(50, 30))
// Returns: 50 (resistance component of impedance)
```

### [[IMAGINARY]]
Extracts the imaginary coefficient from complex numbers created by COMPLEX. IMAGINARY enables analysis of reactive components in electrical systems and phase relationships.

```spreadsheets
// Imaginary component extraction
=IMAGINARY(COMPLEX(3, 4))
// Returns: 4 (imaginary part of 3+4i)

// Reactance calculation
=IMAGINARY(COMPLEX(R1, X1))
// Returns: X1 (reactive component)

// Phase component analysis
=IMAGINARY(COMPLEX(0, SIN(RADIANS(45))))
// Returns: sine component for 45-degree phase
```

## Complex Arithmetic Functions

### [[IMSUM]]
Works with COMPLEX for adding multiple complex numbers in circuit analysis and signal processing. IMSUM enables parallel impedance calculations and signal combination.

```spreadsheets
// Complex impedance addition
=IMSUM(COMPLEX(50, 30), COMPLEX(25, -40))
// Adds two complex impedances

// Signal combination
=IMSUM(COMPLEX(A1, B1), COMPLEX(C1, D1), COMPLEX(E1, F1))
// Combines multiple complex signals

// AC circuit analysis
=IMSUM(COMPLEX(R1, X1), COMPLEX(R2, X2))
// Series impedance calculation
```

### [[IMPRODUCT]]
Combined with COMPLEX for multiplication of complex numbers in frequency domain analysis and power calculations. IMPRODUCT enables transfer function evaluation and modulation analysis.

```spreadsheets
// Transfer function evaluation
=IMPRODUCT(COMPLEX(H_real, H_imag), COMPLEX(X_real, X_imag))
// Multiplies transfer function by input

// Power calculation
=IMPRODUCT(COMPLEX(V_real, V_imag), IMCONJUGATE(COMPLEX(I_real, I_imag)))
// Calculates complex power S = V × I*

// Filter response
=IMPRODUCT(COMPLEX(1, 0), COMPLEX(1, -1))
// Evaluates filter at specific frequency
```

## Engineering Analysis Functions

### [[IMABS]]
Works with COMPLEX to calculate magnitudes of complex numbers for amplitude analysis and distance calculations. IMABS provides the modulus for polar form conversion.

```spreadsheets
// Complex magnitude calculation
=IMABS(COMPLEX(3, 4))
// Returns: 5 (magnitude of 3+4i)

// Impedance magnitude
=IMABS(COMPLEX(R1, X1))
// Calculates total impedance magnitude

// Signal amplitude
=IMABS(COMPLEX(A1*COS(B1), A1*SIN(B1)))
// Returns: A1 (signal amplitude)
```

### [[IMARGUMENT]]
Combined with COMPLEX to determine phase angles of complex numbers for frequency response and phasor analysis. IMARGUMENT provides the argument for polar form representation.

```spreadsheets
// Phase angle calculation
=DEGREES(IMARGUMENT(COMPLEX(3, 4)))
// Returns: 53.13° (angle of 3+4i)

// Impedance phase
=DEGREES(IMARGUMENT(COMPLEX(R1, X1)))
// Calculates impedance phase angle

// Transfer function phase
=DEGREES(IMARGUMENT(COMPLEX(H_real, H_imag)))
// Returns phase response in degrees
```

## Validation and Formatting Functions

### [[IF]]
Works with COMPLEX for conditional complex number creation and validation of input parameters. IF enables error checking and parameter validation for complex calculations.

```spreadsheets
// Input validation
=IF(AND(ISNUMBER(A1), ISNUMBER(B1)), COMPLEX(A1, B1), "Invalid input")
// Creates complex number only with valid inputs

// Engineering unit selection
=IF(C1="electrical", COMPLEX(R1, X1, "j"), COMPLEX(R1, X1, "i"))
// Uses j notation for electrical engineering

// Conditional complex creation
=IF(X1<>0, COMPLEX(R1, X1), R1)
// Creates complex only if imaginary part exists
```

### [[TEXT]]
Combined with COMPLEX for formatting complex number display and creating custom representations. TEXT enables professional presentation of complex calculation results.

```spreadsheets
// Formatted complex display
=TEXT(IMREAL(COMPLEX(A1, B1)), "0.000") & 
 IF(IMAGINARY(COMPLEX(A1, B1))>=0, "+", "") & 
 TEXT(IMAGINARY(COMPLEX(A1, B1)), "0.000") & "j"
// Custom engineering format display

// Polar form conversion
="Magnitude: " & TEXT(IMABS(COMPLEX(A1, B1)), "0.00") & 
 ", Phase: " & TEXT(DEGREES(IMARGUMENT(COMPLEX(A1, B1))), "0.0") & "°"
// Displays in polar coordinates

// Engineering notation
=COMPLEX(A1, B1) & " Ω"
// Adds impedance units
```

## Commonly Used With Functions Examples

### AC Circuit Impedance Calculator
```spreadsheets
// Complete impedance analysis
="Z = " & COMPLEX(A1, B1) & " Ω | |Z| = " & 
 ROUND(IMABS(COMPLEX(A1, B1)), 2) & " Ω | ∠Z = " & 
 ROUND(DEGREES(IMARGUMENT(COMPLEX(A1, B1))), 1) & "°"
// Shows impedance in rectangular and polar forms
```

### Signal Processing Frequency Response
```spreadsheets
// Transfer function evaluation
=LET(H, IMDIV(COMPLEX(1, 0), COMPLEX(1, 2*PI()*C1*R1)), 
     "H(jω) = " & H & " | |H| = " & ROUND(IMABS(H), 3) & 
     " | ∠H = " & ROUND(DEGREES(IMARGUMENT(H)), 1) & "°")
// RC filter response with magnitude and phase
```

### Complex Power Analysis
```spreadsheets
// Three-phase power calculation
=LET(S, IMPRODUCT(COMPLEX(A1, B1), IMCONJUGATE(COMPLEX(C1, D1))),
     "S = " & S & " VA | P = " & ROUND(IMREAL(S), 1) & " W | Q = " & 
     ROUND(IMAGINARY(S), 1) & " VAr | PF = " & ROUND(IMREAL(S)/IMABS(S), 3))
// Complete power analysis with power factor
```

### Control System Pole-Zero Analysis
```spreadsheets
// Stability analysis
=IF(IMREAL(COMPLEX(A1, B1))<0, "Stable pole at " & COMPLEX(A1, B1), 
    "Unstable pole at " & COMPLEX(A1, B1) & " - SYSTEM UNSTABLE")
// Pole location stability check
```

### Fourier Transform Coefficient Display
```spreadsheets
// DFT coefficient formatting
="X[" & A1 & "] = " & COMPLEX(B1, C1) & 
 " | Magnitude: " & ROUND(IMABS(COMPLEX(B1, C1)), 3) & 
 " | Phase: " & ROUND(DEGREES(IMARGUMENT(COMPLEX(B1, C1))), 1) & "°" &
 IF(IMABS(COMPLEX(B1, C1))<0.001, " (negligible)", "")
// Comprehensive frequency domain coefficient display
```
