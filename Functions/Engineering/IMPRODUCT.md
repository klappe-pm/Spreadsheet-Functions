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

# IMPRODUCT

## IMPRODUCT Description

Multiplies two or more complex numbers together, returning the product as a complex number. Essential for electrical engineering calculations involving impedance multiplication, signal processing, and complex mathematical operations in engineering systems.

> [!f(x)] IMPRODUCT Syntax
>
> ```spreadsheets
> IMPRODUCT(complex_number1, [complex_number2], [complex_number3], ...)
> ```
>
> **Parameters:**
> - `complex_number1` (required): First complex number in the form "a+bi" or "a+bj"
> - `complex_number2, complex_number3, ...` (optional): Additional complex numbers to multiply (up to 255 arguments)

> [!f(x)] IMPRODUCT Examples
>
> ```spreadsheets
> // Basic two complex numbers multiplication
> IMPRODUCT("3+4i", "2-i") → "10+5i"
> 
> // Multiple complex numbers
> IMPRODUCT("1+i", "2+2i", "3") → "0+12i"
> 
> // Real and complex number multiplication
> IMPRODUCT("5", "3+4i") → "15+20i"
> 
> // Complex conjugate multiplication (yields real result)
> IMPRODUCT("3+4i", "3-4i") → "25"
> 
> // Zero multiplication
> IMPRODUCT("3+4i", "0") → "0"
> ```

## Use Cases

### [[AC circuit analysis]]
- **Impedance calculations**: Multiply series impedances to find total circuit impedance in AC electrical systems
- **Power factor correction**: Calculate complex power relationships between voltage, current, and impedance
- **Filter design**: Determine transfer functions by multiplying complex frequency responses of cascaded stages
- **Resonance analysis**: Compute impedance products to identify resonant frequencies in RLC circuits

### [[Signal processing]]
- **Frequency domain operations**: Multiply complex frequency spectra for convolution and filtering operations
- **Modulation schemes**: Combine carrier and modulating signals in complex envelope representations
- **Digital filter implementation**: Cascade filter stages by multiplying their complex transfer functions
- **Phase-locked loop analysis**: Calculate loop gain products in complex frequency domain control systems

### [[Mathematical modeling]]
- **Complex polynomial multiplication**: Expand products of complex polynomials for engineering system analysis
- **Matrix operations**: Perform complex matrix multiplications for multi-input multi-output system models
- **Fourier analysis**: Multiply complex Fourier coefficients for signal transformation and analysis
- **Control system design**: Calculate open-loop and closed-loop transfer function products

## Related

### Similar Functions

- [[IMSUM]] - Adds complex numbers together, complement operation to multiplication
- [[IMDIV]] - Divides complex numbers, inverse operation of multiplication
- [[IMPOWER]] - Raises complex numbers to powers, equivalent to repeated multiplication
- [[COMPLEX]] - Creates complex numbers from real and imaginary parts for use with IMPRODUCT
- [[IMABS]] - Returns the magnitude of complex numbers, useful for analyzing multiplication results

## Complex Number Creation

### [[COMPLEX]]
Creates complex numbers from separate real and imaginary components, essential for preparing inputs for IMPRODUCT in engineering calculations.

```spreadsheets
// Create and multiply impedances
=IMPRODUCT(COMPLEX(50, 30), COMPLEX(75, -25))
// Returns: "4500+1000i" (impedance product for circuit analysis)

// Build complex coefficients from separate components
=IMPRODUCT(COMPLEX(A1, B1), COMPLEX(A2, B2), COMPLEX(A3, B3))
// Multiplies three complex numbers built from cell references

// Convert polar to rectangular and multiply
=IMPRODUCT(COMPLEX(r1*COS(theta1), r1*SIN(theta1)), COMPLEX(r2*COS(theta2), r2*SIN(theta2)))
// Multiplies complex numbers in polar form converted to rectangular
```

### [[IMCONJUGATE]]
Combined with IMPRODUCT to calculate magnitudes and perform reflection operations essential in signal processing and circuit analysis.

```spreadsheets
// Calculate magnitude squared using conjugate
=IMPRODUCT("3+4i", IMCONJUGATE("3+4i"))
// Returns: "25" (|z|² = z × z*)

// Power calculation in AC circuits
=IMPRODUCT(voltage_complex, IMCONJUGATE(current_complex))
// Calculates complex power S = V × I* in electrical systems

// Signal reflection coefficient
=IMPRODUCT(reflection_coeff, IMCONJUGATE(incident_signal))
// Computes reflected signal strength in transmission line analysis
```

## Arithmetic Operations

### [[IMSUM]]
Often paired with IMPRODUCT in complex polynomial operations and system analysis where both addition and multiplication are needed.

```spreadsheets
// Complex polynomial evaluation: (a+bi)*(c+di) + (e+fi)
=IMSUM(IMPRODUCT("2+3i", "4+5i"), "1-2i")
// Returns: "-8+23i" (polynomial term calculation)

// Impedance network analysis
=IMSUM(IMPRODUCT(Z1, Z2)/(IMSUM(Z1, Z2)), Z3)
// Calculates parallel impedance Z1||Z2 in series with Z3

// Fourier series coefficient calculation
=IMSUM(IMPRODUCT(a_n, COMPLEX(COS(n*x), SIN(n*x))))
// Builds Fourier series terms with complex coefficients
```

### [[IMDIV]]
Used with IMPRODUCT to perform complex fraction operations and calculate ratios essential in transfer function analysis.

```spreadsheets
// Complex transfer function H(s) = (s+1)/(s²+2s+5)
=IMDIV(IMSUM(s, "1"), IMPRODUCT(s, s) + IMPRODUCT("2", s) + "5")
// Calculates complex transfer function at frequency s

// Voltage divider with complex impedances
=IMDIV(IMPRODUCT(input_voltage, Z2), IMSUM(Z1, Z2))
// Calculates output voltage in complex impedance divider circuit

// Normalize complex product result
=IMDIV(IMPRODUCT("3+4i", "2-i"), IMABS(IMPRODUCT("3+4i", "2-i")))
// Creates unit complex number with same phase as product
```

## Analysis Functions

### [[IMABS]]
Combined with IMPRODUCT to analyze magnitude changes after multiplication operations, crucial for gain and attenuation calculations.

```spreadsheets
// Gain calculation in complex systems
=IMABS(IMPRODUCT(stage1_gain, stage2_gain, stage3_gain))
// Calculates total magnitude gain through cascaded stages

// Compare product magnitude to individual magnitudes
="Product: " & IMABS(IMPRODUCT("3+4i", "2-i")) & ", Individual: " & IMABS("3+4i")*IMABS("2-i")
// Verifies |z1 × z2| = |z1| × |z2| property

// Signal-to-noise ratio after multiplication
=20*LOG10(IMABS(IMPRODUCT(signal, gain))/IMABS(noise))
// Calculates SNR in dB after complex gain multiplication
```

### [[IMARGUMENT]]
Used with IMPRODUCT to analyze phase relationships after multiplication, essential for understanding phase shifts in engineering systems.

```spreadsheets
// Phase addition property verification
="Product phase: " & IMARGUMENT(IMPRODUCT("2+3i", "1+4i")) & ", Sum: " & (IMARGUMENT("2+3i")+IMARGUMENT("1+4i"))
// Verifies arg(z1 × z2) = arg(z1) + arg(z2)

// Total phase shift through cascaded systems
=IMARGUMENT(IMPRODUCT(transfer_func1, transfer_func2, transfer_func3))
// Calculates cumulative phase shift in degrees or radians

// Phase margin calculation in control systems
=180 + IMARGUMENT(IMPRODUCT(open_loop_gain, feedback_factor))*180/PI()
// Determines stability margin in feedback control systems
```

## Commonly Used With Functions Examples

### AC Circuit Analysis
```spreadsheets
// Series impedance calculation
=IMSUM(IMPRODUCT("50+30i", "0.8+0.6i"), IMPRODUCT("75-25i", "0.9+0.4i"))
// Calculates total impedance with current-dependent elements

// Three-phase power calculation
=IMPRODUCT(IMPRODUCT(line_voltage, IMCONJUGATE(line_current)), SQRT(3))
// Calculates three-phase complex power from line quantities

// Transformer equivalent circuit
=IMPRODUCT(primary_impedance, IMPOWER(turns_ratio, 2)) + secondary_impedance
// Refers secondary impedance to primary side for analysis
```

### Signal Processing Systems
```spreadsheets
// Cascaded filter response
=IMPRODUCT(IMDIV("1", IMSUM("1", IMPRODUCT(COMPLEX(0,1), frequency/cutoff1))), IMDIV("1", IMSUM("1", IMPRODUCT(COMPLEX(0,1), frequency/cutoff2))))
// Calculates frequency response of two cascaded low-pass filters

// Modulation and demodulation
=IMPRODUCT(IMPRODUCT(baseband_signal, carrier_complex), demod_carrier_complex)
// Performs complex envelope modulation and demodulation

// Digital filter coefficient multiplication
=IMPRODUCT(numerator_coeffs, IMPOWER(z_transform_var, -delay))
// Multiplies filter coefficients with z-transform delay terms
```
