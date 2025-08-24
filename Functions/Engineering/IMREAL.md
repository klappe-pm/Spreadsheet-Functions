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
# IMREAL

## IMREAL Description

Extracts the real part (real component) of a complex number, returning it as a real number. Essential for separating the resistive component from complex impedances, analyzing in-phase signals, and extracting real coefficients from complex mathematical expressions in engineering applications.

> [!f(x)] IMREAL Syntax
>
> ```spreadsheets
> IMREAL(complex_number)
> ```
>
> **Parameters:**
> - `complex_number` (required): Complex number in the form "a+bi" or "a+bj" from which to extract the real part

> [!f(x)] IMREAL Examples
>
> ```spreadsheets
> // Extract real part from complex number
> IMREAL("3+4i") → 3
> 
> // Real number returns itself
> IMREAL("7") → 7
> 
> // Negative real part
> IMREAL("-2+5i") → -2
> 
> // Pure imaginary number returns 0
> IMREAL("6i") → 0
> 
> // Complex result from calculation
> IMREAL(IMSUM("2+3i", "4-i")) → 6
> ```

## Use Cases

### [[AC circuit analysis]]
- **Resistance extraction**: Extract the resistive component from complex impedance measurements for power loss calculations
- **In-phase current analysis**: Determine the real power component by extracting real parts of current phasors
- **Power factor calculations**: Use real power components to calculate power factor and efficiency metrics
- **Harmonic analysis**: Extract fundamental frequency components from complex harmonic representations

### [[Signal processing]]
- **I/Q demodulation**: Extract in-phase (I) components from complex envelope representations in communication systems
- **FFT analysis**: Separate real frequency components from complex Fourier transform results for spectral analysis
- **Filter design**: Extract real coefficients from complex transfer functions for implementation in digital systems
- **Phase detection**: Analyze real components to determine phase relationships in coherent detection systems

### [[Mathematical analysis]]
- **Complex equation solving**: Extract real solutions from complex polynomial roots and eigenvalue calculations
- **Statistical analysis**: Process real components of complex random variables and probability distributions
- **Optimization problems**: Separate real constraints from complex optimization variables in engineering design
- **Matrix operations**: Extract real parts from complex matrix eigenvalues and eigenvectors for stability analysis

## Related

### Similar Functions

- [[IMAGINARY]] - Extracts the imaginary part of a complex number, complementary to IMREAL
- [[IMABS]] - Returns the magnitude (absolute value) of a complex number
- [[IMARGUMENT]] - Returns the phase angle (argument) of a complex number
- [[IMCONJUGATE]] - Returns the complex conjugate, used with IMREAL for calculations
- [[COMPLEX]] - Creates complex numbers from real and imaginary parts, inverse operation

## Complex Number Extraction

### [[IMAGINARY]]
Paired with IMREAL to completely decompose complex numbers into their real and imaginary components for analysis and reconstruction.

```spreadsheets
// Complete complex number decomposition
=IMREAL("5+3i") & " + " & IMAGINARY("5+3i") & "i"
// Returns: "5 + 3i" (reconstructs original from components)

// Build polar form from rectangular components
=SQRT(IMREAL(z)^2 + IMAGINARY(z)^2) & " ∠" & ATAN2(IMAGINARY(z), IMREAL(z))*180/PI() & "°"
// Converts complex number to magnitude and phase representation

// Separate AC circuit components
="Resistance: " & IMREAL(impedance) & " Ω, Reactance: " & IMAGINARY(impedance) & " Ω"
// Displays impedance components for circuit analysis
```

### [[COMPLEX]]
Used with IMREAL to verify complex number integrity and reconstruct numbers from extracted components in engineering calculations.

```spreadsheets
// Verify real part extraction accuracy
=IMREAL(COMPLEX(real_part, imag_part)) = real_part
// Returns TRUE if extraction is correct

// Process real parts in arrays of complex numbers
=COMPLEX(IMREAL(A1:A10), 0)
// Creates array of real parts as complex numbers with zero imaginary part

// Filter and reconstruct based on real part criteria
=IF(IMREAL(complex_impedance)>50, COMPLEX(IMREAL(complex_impedance), 0), complex_impedance)
// Keeps only real part if resistance exceeds threshold
```

## Analysis Functions

### [[IMABS]]
Combined with IMREAL to analyze the relationship between magnitude and real components, essential for power and efficiency calculations.

```spreadsheets
// Power factor calculation using real and magnitude components
=IMREAL(complex_power)/IMABS(complex_power)
// Calculates power factor from complex power measurements

// Real component percentage of total magnitude
=IMREAL("4+3i")/IMABS("4+3i")*100 & "%"
// Returns: "80%" (real part contribution to magnitude)

// Efficiency analysis in power systems
="Real Power: " & IMREAL(apparent_power) & " W, Efficiency: " & (IMREAL(apparent_power)/IMABS(apparent_power)*100) & "%"
// Calculates electrical efficiency from complex power measurements
```

### [[IMARGUMENT]]
Used with IMREAL to analyze phase relationships and convert between rectangular and polar representations of complex numbers.

```spreadsheets
// Verify rectangular to polar conversion
=IMREAL("5+12i") & " = " & IMABS("5+12i")*COS(IMARGUMENT("5+12i"))
// Confirms real part equals magnitude × cos(angle)

// Phase analysis for power factor correction
=IF(IMARGUMENT(complex_impedance)*180/PI()>30, "Needs PF correction", "Acceptable PF")
// Analyzes phase angle based on real component relationships

// Signal quadrant identification
=IF(IMREAL(signal)>0, IF(IMAGINARY(signal)>0, "Q1", "Q4"), IF(IMAGINARY(signal)>0, "Q2", "Q3"))
// Identifies signal quadrant based on real and imaginary signs
```

## Mathematical Operations

### [[IMSUM]]
Often combined with IMREAL to perform operations on real components of multiple complex numbers in engineering calculations.

```spreadsheets
// Sum of real parts from multiple impedances
=IMREAL(IMSUM(Z1, Z2, Z3))
// Calculates total real impedance from sum of complex impedances

// Real power calculation from multiple sources
="Total Real Power: " & IMREAL(IMSUM(P1_complex, P2_complex, P3_complex)) & " W"
// Sums real power components from multiple complex power measurements

// Average real component analysis
=IMREAL(IMSUM(A1:A10))/COUNT(A1:A10)
// Calculates average of real components from array of complex numbers
```

### [[IMPRODUCT]]
Used with IMREAL to extract real results from complex multiplication operations, important for power calculations and system analysis.

```spreadsheets
// Real power from voltage and current product
=IMREAL(IMPRODUCT(voltage_phasor, IMCONJUGATE(current_phasor)))/2
// Calculates average real power from AC phasor multiplication

// Real coefficient extraction from polynomial multiplication
=IMREAL(IMPRODUCT(COMPLEX(a1, b1), COMPLEX(a2, b2)))
// Extracts real coefficient from complex polynomial term multiplication

// Transfer function real part at specific frequency
=IMREAL(IMPRODUCT(numerator_complex, IMDIV("1", denominator_complex)))
// Calculates real part of transfer function for frequency response analysis
```

## Commonly Used With Functions Examples

### Power System Analysis
```spreadsheets
// Three-phase real power calculation
=IMREAL(IMPRODUCT(IMPRODUCT(line_voltage, IMCONJUGATE(line_current)), SQRT(3)))
// Calculates total real power in three-phase system

// Load resistance calculation from complex impedance
=IMREAL(IMDIV(IMPOWER(voltage_rms, 2), IMCONJUGATE(complex_current)))
// Determines resistive load component from voltage and current measurements

// Power factor improvement analysis
="Before PF correction: " & IMREAL(original_power)/IMABS(original_power) & ", After: " & IMREAL(corrected_power)/IMABS(corrected_power)
// Compares power factors before and after capacitor bank installation
```

### Signal Processing Applications
```spreadsheets
// I/Q demodulation - extract in-phase component
=IMREAL(IMPRODUCT(received_signal, COMPLEX(COS(carrier_phase), -SIN(carrier_phase))))
// Extracts in-phase data from modulated carrier signal

// Real part of frequency response at specific frequency
=IMREAL(IMDIV(numerator_polynomial, denominator_polynomial))
// Evaluates real frequency response for filter design

// Correlation analysis - real correlation coefficient
=IMREAL(IMSUM(IMPRODUCT(signal1_complex, IMCONJUGATE(signal2_complex))))/SQRT(IMSUM(IMABS(signal1_complex)^2)*IMSUM(IMABS(signal2_complex)^2))
// Calculates real correlation between two complex signals
```
