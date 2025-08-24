---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- engineering
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- engineering
- excel
- sheets
---
# IMSUB

## IMSUB Description

Subtracts one complex number from another (complex1 - complex2). Essential for impedance difference calculations, voltage drop analysis, error signal generation, and complex mathematical operations requiring subtraction in engineering applications.

> [!f(x)] IMSUB Syntax
>
> ```spreadsheets
> IMSUB(complex_number1, complex_number2)
> ```
>
> **Parameters:**
> - `complex_number1` (required): Complex number (minuend) in the form "a+bi" or "a+bj"
> - `complex_number2` (required): Complex number (subtrahend) to subtract from the first

> [!f(x)] IMSUB Examples
>
> ```spreadsheets
> // Basic complex subtraction
> IMSUB("5+3i", "2+i") → "3+2i"
> 
> // Real number subtraction
> IMSUB("7", "3") → "4"
> 
> // Subtract imaginary from real
> IMSUB("5", "2i") → "5-2i"
> 
> // Complex conjugate subtraction
> IMSUB("4+3i", "4-3i") → "6i"
> 
> // Zero subtraction (identity)
> IMSUB("3+4i", "0") → "3+4i"
> ```

## Use Cases

### [[Circuit analysis]]
- **Voltage difference calculations**: Calculate voltage drops across circuit components
- **Impedance network analysis**: Determine impedance differences in parallel and series combinations
- **Error signal generation**: Generate error signals for feedback control systems
- **Phase difference analysis**: Calculate phase and magnitude differences between signals

### [[Signal processing]]
- **Signal difference analysis**: Calculate differences between complex signals for comparison
- **Noise reduction**: Subtract noise estimates from received signals
- **Interference cancellation**: Remove interference by subtracting known interference patterns
- **Frequency offset correction**: Correct frequency offsets by subtracting carrier deviations

### [[Control systems]]
- **Feedback error calculation**: Generate error signals by subtracting feedback from reference
- **Stability analysis**: Calculate loop gain margins and phase margins
- **Compensation network design**: Design lead-lag compensators using complex subtraction
- **State estimation**: Calculate estimation errors in Kalman filter applications

## Related

### Similar Functions

- [[IMSUM]] - Adds complex numbers, opposite operation to subtraction
- [[IMDIV]] - Divides complex numbers, related arithmetic operation
- [[IMPRODUCT]] - Multiplies complex numbers, related arithmetic operation
- [[IMABS]] - Returns magnitude of complex difference for distance calculations
- [[IMCONJUGATE]] - Creates conjugates for complex conjugate subtraction operations

## Arithmetic Operations

### [[IMSUM]]
Complementary operation to IMSUB, often used together for complex arithmetic expressions and signal processing calculations.

```spreadsheets
// Verify subtraction using addition: (a-b) + b = a
=IMSUM(IMSUB("5+3i", "2+i"), "2+i")
// Returns: "5+3i" (verifies subtraction correctness)

// Calculate impedance differences and sums
=IMSUB(total_impedance, IMSUM(known_impedance1, known_impedance2))
// Finds unknown impedance in impedance network

// Signal processing: remove DC offset and add calibration
=IMSUM(IMSUB(signal_with_dc, dc_offset), calibration_factor)
// Processes signal by removing DC and adding calibration
```

### [[IMABS]]
Combined with IMSUB to calculate distances and magnitudes of complex differences, essential for error analysis.

```spreadsheets
// Calculate error magnitude between signals
=IMABS(IMSUB(reference_signal, measured_signal))
// Returns magnitude of error between reference and measurement

// Distance between complex impedances
=IMABS(IMSUB(impedance1, impedance2))
// Calculates distance between two impedance points in complex plane

// Control system error magnitude
=IMABS(IMSUB(setpoint, feedback_signal))
// Calculates magnitude of control error for stability analysis
```

## Commonly Used With Functions Examples

### Control System Applications
```spreadsheets
// PID controller error calculation
=IMSUB(setpoint_complex, process_output_complex)
// Generates complex error signal for advanced PID control

// Loop gain calculation with feedback subtraction
=IMDIV(IMSUB(forward_gain, feedback_gain), IMSUM("1", loop_gain))
// Calculates closed-loop gain using complex subtraction

// Phase margin calculation
=IMARGUMENT(IMSUB("1", loop_transfer_function)) * 180/PI()
// Calculates phase margin by subtracting loop gain from unity
```

### AC Circuit Analysis
```spreadsheets
// Voltage divider with complex impedances
=IMDIV(IMPRODUCT(input_voltage, load_impedance), IMSUM(source_impedance, load_impedance))
// But first calculate impedance difference for analysis:
=IMSUB(total_impedance, source_impedance)

// Three-phase voltage differences
=IMSUB(line_voltage_AB, line_voltage_BC)
// Calculates voltage difference between phases

// Power factor correction analysis
=IMSUB(COMPLEX(real_power, uncorrected_reactive_power), COMPLEX(real_power, corrected_reactive_power))
// Shows reactive power reduction from power factor correction
```
