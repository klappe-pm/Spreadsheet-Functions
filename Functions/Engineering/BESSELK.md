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
# BESSELK

## BESSELK Description

Returns the modified Bessel function of the second kind Kn(x), also known as the MacDonald function. Provides exponentially decaying solutions to modified Bessel differential equations in cylindrical coordinates. Essential for modeling heat diffusion, electromagnetic wave attenuation, and boundary value problems where solutions must decay at infinity.

> [!f(x)] BESSELK Syntax
>
> ```spreadsheets
> BESSELK(x, n)
> ```
>
> **Parameters:**
> - `x` (required): The value at which to evaluate the function (positive real number)
> - `n` (required): The order of the Bessel function (non-negative integer)

> [!f(x)] BESSELK Examples
>
> ```spreadsheets
> // Basic modified Bessel function of second kind
> BESSELK(1, 0) → 0.421
> 
> // First order evaluation
> BESSELK(1, 1) → 0.602
> 
> // Higher order functions
> BESSELK(2, 2) → 0.254
> 
> // Small argument behavior (singular)
> BESSELK(0.1, 0) → 2.427
> 
> // Large argument asymptotic behavior
> BESSELK(5, 0) → 0.0037
> 
> // Heat conduction applications
> BESSELK(0.5, 0) → 0.924
> 
> // Electromagnetic attenuation
> BESSELK(3, 1) → 0.040
> ```

## Use Cases

### [[Heat conduction and diffusion]]
- **External heat transfer**: Model temperature decay in infinite cylindrical domains with surface cooling
- **Thermal insulation analysis**: Calculate heat loss and temperature profiles in cylindrical insulation systems
- **Ground heat exchangers**: Analyze thermal response of buried pipes and geothermal heat pump systems
- **Heat sink design**: Optimize fin geometry and thermal performance for cylindrical heat dissipation systems

### [[Electromagnetic wave attenuation]]
- **Lossy waveguide analysis**: Calculate field attenuation and propagation in dissipative cylindrical waveguides
- **Skin effect modeling**: Analyze current distribution and losses in cylindrical conductors at high frequency
- **Antenna near-field analysis**: Model electromagnetic field decay in the reactive near-field region
- **Shielding effectiveness**: Calculate field penetration and attenuation in cylindrical electromagnetic shields

### [[Fluid mechanics and porous media]]
- **Groundwater flow**: Model radial flow patterns around wells and infiltration galleries in aquifers
- **Permeability testing**: Analyze pressure decay and flow characteristics in cylindrical core samples
- **Heat exchanger design**: Calculate thermal boundary layer development and heat transfer in tube banks
- **Mass transfer processes**: Model concentration profiles and diffusion in cylindrical reaction vessels

## Related

### Similar Functions

- [[BESSELI]] - Modified Bessel function of the first kind for exponential growth solutions
- [[BESSELJ]] - Bessel function of the first kind for oscillatory solutions in cylindrical coordinates
- [[BESSELY]] - Bessel function of the second kind for boundary value problems
- [[EXP]] - Exponential function often combined with BESSELK for complete decay solutions

## Mathematical Analysis Functions

### [[BESSELI]]
Complements BESSELK to form complete solutions for modified Bessel differential equations. BESSELI provides growing solutions while BESSELK provides decaying solutions.

```spreadsheets
// General modified Bessel equation solution
=BESSELI(A1, B1)*C1 + BESSELK(A1, B1)*D1
// Complete solution with arbitrary constants

// Boundary condition matching for finite domains
=IF(A1<1, BESSELI(A1, B1), BESSELK(A1, B1))
// Select appropriate function based on boundary conditions

// Heat conduction in cylindrical annulus
=BESSELI(SQRT(A1), 0)*B1 + BESSELK(SQRT(A1), 0)*C1
// Temperature profile between cylindrical surfaces
```

### [[EXP]]
Combined with BESSELK for modeling complete exponential decay with geometric effects. EXP provides time decay while BESSELK adds spatial variation.

```spreadsheets
// Heat diffusion with time decay
=EXP(-A1*T1)*BESSELK(B1*R1, 0)
// Temperature decay with radial variation

// Electromagnetic wave attenuation
=EXP(-γ*Z1)*BESSELK(A1*R1, 1)
// Field decay with propagation distance and radial variation

// Concentration decay in cylindrical reactor
=EXP(-k*T1)*BESSELK(SQRT(k/D)*R1, 0)
// Reactant concentration with reaction and diffusion
```

## Engineering Calculation Functions

### [[LOG]]
Works with BESSELK for logarithmic analysis and asymptotic behavior evaluation. LOG enables proper scaling and large-argument approximations.

```spreadsheets
// Asymptotic approximation validation
=LOG(BESSELK(A1, B1)) + A1 - LOG(SQRT(PI()/(2*A1)))
// Checks large argument asymptotic behavior

// Heat transfer coefficient calculation
=LOG(BESSELK(A1, 0)/BESSELK(B1, 0))/(A1-B1)
// Logarithmic heat transfer rate analysis

// Attenuation constant determination
=-LOG(BESSELK(A1, B1)/BESSELK(C1, B1))/(A1-C1)
// Calculates decay constant from function values
```

### [[SQRT]]
Combined with BESSELK for proper dimensional scaling in physical applications. SQRT provides argument scaling for diffusion and wave equations.

```spreadsheets
// Heat equation scaling
=BESSELK(SQRT(A1*B1), 0)
// Proper dimensional argument for thermal diffusion

// Electromagnetic skin depth
=BESSELK(SQRT(2)*R1/δ1, 0)
// Scaled penetration depth analysis

// Mass diffusion scaling
=BESSELK(R1*SQRT(k/D), 0)
// Scaled argument for reaction-diffusion problems
```

## Validation and Analysis Functions

### [[IF]]
Combined with BESSELK for conditional evaluation and singularity handling. IF enables proper function evaluation and boundary condition implementation.

```spreadsheets
// Singularity avoidance
=IF(A1>0, BESSELK(A1, B1), "Invalid argument")
// Ensures positive arguments for convergence

// Solution selection based on boundary conditions
=IF(C1="decaying", BESSELK(A1, B1), BESSELI(A1, B1))
// Selects decaying vs growing solution

// Asymptotic approximation switching
=IF(A1>10, SQRT(PI()/(2*A1))*EXP(-A1), BESSELK(A1, B1))
// Uses approximation for large arguments
```

### [[ABS]]
Works with BESSELK for magnitude analysis and error calculation. ABS ensures positive results and enables proper function evaluation.

```spreadsheets
// Magnitude calculation for decaying fields
=ABS(BESSELK(A1, B1))
// Ensures positive physical quantities

// Error analysis between approximations
=ABS(BESSELK(A1, B1) - SQRT(PI()/(2*A1))*EXP(-A1))
// Compares exact vs asymptotic solutions

// Relative error calculation
=ABS((BESSELK(A1, B1) - BESSELK(C1, B1))/BESSELK(A1, B1))
// Calculates relative differences
```

## Physical Modeling Functions

### [[PI]]
Combined with BESSELK for proper geometric scaling and normalization. PI provides scaling factors for cylindrical coordinate systems.

```spreadsheets
// Geometric scaling in cylindrical coordinates
=BESSELK(2*PI()*R1/L1, 0)
// Normalized radial coordinate scaling

// Heat flux calculation
=2*PI()*k*L*BESSELK(A1, 1)/BESSELK(A1, 0)
// Cylindrical heat flux with geometric factors

// Electromagnetic power loss
=PI()*R1^2*σ*BESSELK(SQRT(2)*R1/δ, 0)
// Power loss in cylindrical conductor
```

### [[COS]]
Works with BESSELK for time-harmonic solutions and angular variations. COS provides temporal or angular dependence combined with radial decay.

```spreadsheets
// Time-harmonic heat conduction
=BESSELK(A1*R1, 0)*COS(ω*T1)
// Oscillatory temperature with radial decay

// Electromagnetic field with angular variation
=BESSELK(A1*R1, n)*COS(n*θ1)*COS(ω*T1)
// Complete field solution with angular dependence

// Vibration damping analysis
=BESSELK(A1*R1, 0)*COS(ω*T1)*EXP(-δ*T1)
// Damped oscillation with spatial decay
```

## Commonly Used With Functions Examples

### Heat Transfer in Cylindrical Insulation
```spreadsheets
// Temperature profile and heat loss calculation
=LET(T_profile, T_inner*BESSELK(r/L_char, 0)/BESSELK(r_inner/L_char, 0),
     heat_loss, 2*PI()*k*L*BESSELK(r_inner/L_char, 1)/BESSELK(r_inner/L_char, 0),
     "T(r) = " & ROUND(T_profile, 2) & "°C | Heat loss: " & ROUND(heat_loss, 1) & " W/m")
// Complete thermal analysis with temperature and heat flux
```

### Electromagnetic Field Attenuation
```spreadsheets
// Field strength and penetration depth analysis
="Field: " & ROUND(E0*BESSELK(SQRT(2)*r/δ, 0), 2) & " V/m" &
 " | Penetration: " & ROUND(δ*LN(E0/0.37), 2) & " mm" &
 " | Loss: " & ROUND(-20*LOG10(BESSELK(SQRT(2)*r/δ, 0)), 1) & " dB"
// Complete electromagnetic attenuation analysis
```

### Groundwater Flow Around Well
```spreadsheets
// Pressure drawdown and flow rate calculation
=LET(s, s0*BESSELK(r/B, 0)/BESSELK(r_well/B, 0),
     Q, 2*PI()*T*s0*BESSELK(r_well/B, 1)/BESSELK(r_well/B, 0),
     "Drawdown: " & ROUND(s, 3) & " m | Flow rate: " & ROUND(Q, 2) & " m³/day")
// Complete well hydraulics analysis
```

### Thermal Stress in Pressure Vessel
```spreadsheets
// Stress distribution with thermal loading
=LET(σ_thermal, α*E*ΔT*BESSELK(r/a, 0)/(1-ν),
     σ_max, α*E*ΔT/(1-ν),
     factor, BESSELK(r/a, 0),
     "Thermal stress: " & ROUND(σ_thermal/1e6, 1) & " MPa" &
     " | Stress factor: " & ROUND(factor, 3) & " | Safety: " & ROUND(σ_allow/σ_thermal, 2))
// Complete thermal stress analysis with safety factor
```

### Heat Exchanger Performance Analysis
```spreadsheets
// Effectiveness and heat transfer calculation
="Effectiveness: " & ROUND(1-BESSELK(NTU*Cr, 0), 3) &
 " | Heat transfer: " & ROUND(ε*C_min*(T_hot-T_cold), 1) & " W" &
 " | LMTD: " & ROUND((T_hot-T_cold)/LN((T_hot-T_cold_out)/(T_hot_out-T_cold)), 2) & "°C"
// Complete heat exchanger performance with thermal analysis
```
