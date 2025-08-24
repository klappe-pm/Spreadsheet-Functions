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
# CONVERT

## CONVERT Description

Converts a number from one measurement unit to another. Supports conversions between weight, distance, time, pressure, force, energy, power, magnetism, temperature, volume, and area units. Essential for engineering calculations requiring unit standardization and international measurement system conversions.

> [!f(x)] CONVERT Syntax
>
> ```spreadsheets
> CONVERT(number, from_unit, to_unit)
> ```
>
> **Parameters:**
> - `number` (required): The value to convert
> - `from_unit` (required): The unit to convert from (text string)
> - `to_unit` (required): The unit to convert to (text string)

> [!f(x)] CONVERT Examples
>
> ```spreadsheets
> // Length conversions
> CONVERT(100, "m", "ft") → 328.084
> 
> // Weight conversions
> CONVERT(2.5, "kg", "lbm") → 5.51156
> 
> // Temperature conversions
> CONVERT(32, "F", "C") → 0
> 
> // Energy conversions
> CONVERT(1, "kWh", "J") → 3600000
> 
> // Pressure conversions
> CONVERT(14.7, "psi", "Pa") → 101353
> 
> // Volume conversions
> CONVERT(1, "gal", "l") → 3.78541
> 
> // Time conversions
> CONVERT(3600, "sec", "hr") → 1
> ```

## Use Cases

### [[Unit standardization]]
- **Engineering drawings**: Convert mixed imperial and metric dimensions to single unit system for manufacturing consistency
- **International project coordination**: Standardize measurements across global teams using different measurement systems
- **Scientific data analysis**: Convert field measurements to standard SI units for research publication and peer review
- **Material specifications**: Ensure material properties are expressed in units matching design software and manufacturing equipment

### [[Engineering calculations]]
- **Structural analysis**: Convert loads between different force units (kN, lbf, N) for stress and deflection calculations  
- **Fluid dynamics**: Transform pressure, flow rate, and viscosity units for hydraulic system design and pump sizing
- **Electrical engineering**: Convert power measurements between watts, horsepower, and BTU/hr for motor selection and energy analysis
- **Thermal analysis**: Convert heat transfer coefficients and thermal conductivity between metric and imperial systems

### [[Data processing]]
- **Sensor data normalization**: Convert raw sensor readings from various manufacturers into consistent units for analysis
- **Manufacturing quality control**: Standardize measurement units across production lines for statistical process control
- **Environmental monitoring**: Convert weather station data, emissions measurements, and pollution levels to regulatory units
- **Supply chain management**: Convert package weights, dimensions, and volumes between supplier units and shipping requirements

## Related

### Similar Functions

- [[DEC2BIN]] - Converts decimal numbers to binary representation for digital system analysis
- [[BIN2DEC]] - Converts binary numbers to decimal for data processing and calculations
- [[HEX2DEC]] - Converts hexadecimal to decimal for programming and memory address calculations  
- [[DEC2HEX]] - Converts decimal to hexadecimal for color codes and memory addressing
- [[COMPLEX]] - Creates complex numbers for electrical engineering and signal processing calculations

## Measurement System Functions

### [[ROUND]]
Used with CONVERT to control precision of converted values and handle engineering tolerance requirements. ROUND ensures converted measurements align with manufacturing capabilities and measurement instrument precision.

```spreadsheets
// Precision control for machining tolerances
=ROUND(CONVERT(2.54, "in", "mm"), 2)
// Returns: 64.52 (rounded to 0.01mm precision)

// Engineering dimension with appropriate precision
=ROUND(CONVERT(A1, "ft", "m"), 3) & " m"
// Converts feet to meters with 3 decimal places

// Material quantity with commercial rounding
=ROUND(CONVERT(B2, "lbm", "kg")*1.1, 1)
// Adds 10% safety factor and rounds to 0.1kg precision
```

### [[IF]]  
Combined with CONVERT for conditional unit conversions and validation of measurement ranges. IF enables automatic unit selection based on magnitude and provides error handling for invalid conversions.

```spreadsheets
// Automatic unit selection based on magnitude
=IF(A1<1000, CONVERT(A1, "g", "oz") & " oz", CONVERT(A1, "g", "lbm") & " lbs")
// Uses ounces for small masses, pounds for large masses

// Validation of engineering limits
=IF(CONVERT(B1, "psi", "Pa")>200000, "Exceeds material limit", "Safe pressure")
// Checks if pressure exceeds 200kPa safety threshold

// Temperature range validation
=IF(AND(CONVERT(C1,"F","C")>=0, CONVERT(C1,"F","C")<=100), "Water liquid", "Phase change")
// Determines water phase based on temperature range
```

## Engineering Calculation Functions

### [[SUM]]
Works with CONVERT to aggregate measurements in consistent units and calculate total loads, volumes, or quantities. SUM ensures accurate engineering totals when combining measurements from different sources.

```spreadsheets
// Total structural load calculation
=SUM(CONVERT(D2:D10, "kips", "N"))
// Converts all loads to Newtons before summing

// Material volume calculation
=SUM(CONVERT(E2:E20, "ft^3", "m^3"))
// Aggregates volumes in cubic meters

// Energy consumption analysis
=SUM(CONVERT(F1:F12, "BTU", "kWh"))
// Converts monthly energy data to kWh for billing
```

### [[AVERAGE]]
Combined with CONVERT to calculate mean values in standardized units for performance analysis and quality control. AVERAGE with CONVERT enables consistent statistical analysis across mixed measurement systems.

```spreadsheets
// Average material density across suppliers
=AVERAGE(CONVERT(G2:G15, "lb/ft^3", "kg/m^3"))
// Standardizes density measurements for comparison

// Mean environmental temperature
=AVERAGE(CONVERT(H1:H24, "F", "C"))
// Converts hourly temperatures to Celsius for analysis  

// Average flow rate performance
=AVERAGE(CONVERT(I2:I100, "gpm", "L/s"))
// Converts pump test data to metric units
```

### [[MAX]]
Used with CONVERT to find maximum values in consistent units for safety analysis and design limits. MAX with CONVERT ensures proper identification of peak loads, pressures, or temperatures regardless of original measurement units.

```spreadsheets
// Maximum allowable stress check
=MAX(CONVERT(J2:J50, "ksi", "MPa"))
// Finds peak stress in standard engineering units

// Peak temperature identification
=MAX(CONVERT(K1:K1000, "F", "C"))
// Identifies maximum operating temperature

// Highest flow rate recorded
=MAX(CONVERT(L2:L365, "ft^3/min", "m^3/s"))
// Finds peak volumetric flow rate
```

## Commonly Used With Functions Examples

### Engineering Design Validation
```spreadsheets
// Complete structural load analysis with safety factors
=IF(MAX(CONVERT(A2:A10,"kips","N"))*1.5 > 50000, 
    "Design exceeds capacity", 
    "Safe design - Max load: " & ROUND(MAX(CONVERT(A2:A10,"kips","N")),0) & " N")
// Converts loads to Newtons, applies 1.5x safety factor, validates against 50kN limit
```

### Multi-Unit Material Calculations  
```spreadsheets
// Total material cost with mixed units
=SUM(CONVERT(B2:B5,"lbm","kg")*C2:C5) & " kg total at $" & 
 ROUND(SUMPRODUCT(CONVERT(B2:B5,"lbm","kg"),C2:C5*D2:D5),2)
// Converts weights to kg, calculates total mass and cost
```

### Environmental Monitoring Dashboard
```spreadsheets
// Temperature range analysis with alerts
=IF(OR(CONVERT(E1,"F","C")<0, CONVERT(E1,"F","C")>40), 
    "ALERT: " & ROUND(CONVERT(E1,"F","C"),1) & "°C outside range", 
    "Normal: " & ROUND(CONVERT(E1,"F","C"),1) & "°C")
// Converts temperature and provides range-based status
```

### Process Control Optimization
```spreadsheets
// Pressure system efficiency calculation
=ROUND((CONVERT(F2,"psi","kPa")/CONVERT(F1,"psi","kPa"))*100,1) & "% efficiency at " & 
 ROUND(CONVERT(G2,"gpm","L/min"),0) & " L/min flow"
// Calculates pressure ratio efficiency with flow rate context
```

### Quality Control Statistics
```spreadsheets
// Dimensional tolerance analysis
=IF(ABS(CONVERT(H2,"in","mm")-25.4)<0.1, "Within tolerance", 
    "Out of spec by " & ROUND(ABS(CONVERT(H2,"in","mm")-25.4),3) & " mm")
// Converts measurements to mm and checks against 25.4±0.1mm specification
```
