---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - logical
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
# IF

## IF Description

Tests a condition and returns one value if the condition is true and another value if the condition is false. The cornerstone of conditional logic in spreadsheets, enabling dynamic decision-making and data processing based on specified criteria.

> [!f(x)] IF Syntax
>
> ```spreadsheets
> IF(logical_test, value_if_true, value_if_false)
> ```
>
> **Parameters:**
> - `logical_test` (required): Condition to evaluate (returns TRUE or FALSE)
> - `value_if_true` (required): Value returned when condition is TRUE
> - `value_if_false` (optional): Value returned when condition is FALSE (defaults to FALSE if omitted)

> [!f(x)] IF Examples
>
> ```spreadsheets
> // Basic pass/fail evaluation
> IF(A1>=60, "Pass", "Fail") → "Pass" if A1 is 60 or higher, "Fail" otherwise
> 
> // Sales bonus calculation
> IF(B2>10000, B2*0.1, 0) → 10% bonus if sales exceed $10,000, 0 otherwise
> 
> // Text comparison
> IF(C3="Manager", 50000, 35000) → $50K salary for managers, $35K for others
> 
> // Date-based logic
> IF(D4>TODAY(), "Future", "Past/Present") → categorizes dates relative to today
> 
> // Empty cell handling
> IF(E5="", "No data", E5) → displays "No data" for empty cells, cell value otherwise
> ```

## Use Cases

### [[Conditional formatting]]
- **Grade categorization**: Assign letter grades based on numerical scores to create clear performance indicators
- **Status indicators**: Display "Active", "Inactive", or "Pending" based on last activity dates for account management
- **Performance ratings**: Convert numerical metrics into descriptive ratings like "Excellent", "Good", "Needs Improvement"
- **Priority assignment**: Set task priorities as "High", "Medium", or "Low" based on deadline proximity and importance scores

### [[Data validation]]
- **Input verification**: Check if entered values meet specific criteria and display error messages for invalid data
- **Range validation**: Ensure numerical inputs fall within acceptable ranges for quality control and data integrity
- **Format checking**: Verify that text entries follow required patterns like email formats or ID number structures
- **Completeness validation**: Identify missing required fields and prompt users to complete all necessary information

### [[Decision logic]]
- **Approval workflows**: Automatically route requests for approval based on amount thresholds or department rules
- **Discount calculations**: Apply different discount rates based on customer type, order volume, or loyalty status
- **Inventory management**: Trigger reorder alerts when stock levels fall below minimum thresholds
- **Risk assessment**: Categorize loans or investments as high, medium, or low risk based on multiple criteria

### [[Business calculations]]
- **Commission structures**: Calculate sales commissions using tiered rates based on performance levels and quotas
- **Overtime calculations**: Apply different pay rates for regular hours, overtime, and holiday work periods
- **Tax computations**: Determine appropriate tax rates and deductions based on income brackets and filing status
- **Shipping cost determination**: Calculate shipping fees based on weight, distance, and delivery speed preferences

## Related

### Similar Functions

- [[IFS]] - Tests multiple conditions sequentially without nested IF statements
- [[IFERROR]] - Handles errors gracefully by providing alternative values when formulas fail
- [[IFNA]] - Specifically handles #N/A errors from lookup functions
- [[SWITCH]] - Compares one value against multiple options, cleaner than nested IFs
- [[CHOOSE]] - Returns values from a list based on index position, alternative to multiple IFs

## Conditional Logic Functions

### [[AND]]
Combined with IF to test multiple conditions simultaneously, requiring all conditions to be true. Essential for complex business rules and multi-criteria decision making.

```spreadsheets
// Employee bonus eligibility (sales AND tenure requirements)
=IF(AND(B2>50000, C2>=3), B2*0.05, 0)
// 5% bonus if sales exceed $50K AND 3+ years tenure

// Loan approval logic
=IF(AND(D3>=650, E3<0.3, F3>2), "Approved", "Denied")
// Approved if credit score ≥650 AND debt ratio <30% AND 2+ years employment

// Academic honors calculation
=IF(AND(G4>=3.5, H4>=90), "Dean's List", "Regular Standing")
// Dean's List if GPA ≥3.5 AND attendance ≥90%
```

### [[OR]]
Used with IF to test multiple conditions where any one condition being true triggers the result. Perfect for flexible criteria and exception handling.

```spreadsheets
// Expedited shipping qualification
=IF(OR(A5>1000, B5="Premium", C5="VIP"), "Free Express", "Standard")
// Free express if order >$1000 OR Premium member OR VIP status

// Alert system for critical values
=IF(OR(D6>100, D6<10), "ALERT: Review Required", "Normal")
// Alert if temperature above 100 or below 10

// Holiday pay calculation
=IF(OR(E7="Holiday", E7="Weekend", F7>8), G7*1.5, G7)
// Time and half for holidays, weekends, or overtime hours
```

### [[NOT]]
Reverses logical values with IF, useful for exclusion logic and negative conditions. Simplifies complex conditional statements by inverting boolean results.

```spreadsheets
// Access control - deny specific departments
=IF(NOT(H8="Restricted"), "Access Granted", "Access Denied")
// Grant access unless department is "Restricted"

// Inventory availability check
=IF(NOT(I9<=0), "Available", "Out of Stock")
// Available unless quantity is zero or negative

// Working day validation
=IF(NOT(WEEKDAY(J10,2)>5), "Workday", "Weekend")
// Workday unless Saturday (6) or Sunday (7)
```

## Error Handling Functions

### [[IFERROR]]
Protects IF statements from errors by providing fallback values when formulas fail. Essential for robust spreadsheet design and user experience.

```spreadsheets
// Safe division with IF condition
=IFERROR(IF(K11<>0, L11/K11, "Cannot divide by zero"), "Calculation error")
// Handles both division by zero and other potential errors

// Lookup with condition and error handling
=IFERROR(IF(VLOOKUP(M12,Table1,2,0)>50, "High", "Low"), "Not found")
// Categorizes lookup results with error protection

// Complex formula protection
=IFERROR(IF(N13>AVERAGE(N:N), "Above Average", "Below Average"), "Insufficient data")
// Compares to average with error handling for empty ranges
```

### [[IFNA]]
Specifically handles #N/A errors in IF statements, particularly useful with lookup functions that commonly return #N/A when no match is found.

```spreadsheets
// Customer lookup with status
=IF(IFNA(VLOOKUP(O14,CustomerTable,3,0),"")="Active", "Proceed", "Check Status")
// Checks customer status with N/A protection

// Product availability with lookup
=IFNA(IF(VLOOKUP(P15,Inventory,2,0)>0, "In Stock", "Backordered"), "Product not found")
// Stock status with specific N/A handling

// Price calculation with error handling
=IFNA(IF(VLOOKUP(Q16,PriceList,2,0)>100, "Premium", "Standard"), "No pricing data")
// Price tier determination with N/A protection
```

## Commonly Used With Functions Examples

### IF with Mathematical Operations
IF frequently combines with mathematical functions to perform conditional calculations based on numerical criteria and business rules.

```spreadsheets
// Progressive tax calculation
=IF(A1<=50000, A1*0.1, IF(A1<=100000, 5000+(A1-50000)*0.2, 15000+(A1-100000)*0.3))
// Tiered tax rates: 10% up to $50K, 20% up to $100K, 30% above

// Shipping cost with weight tiers
=IF(B2<=5, 10, IF(B2<=20, 15, 25))
// $10 for ≤5 lbs, $15 for ≤20 lbs, $25 for heavier items

// Sales commission with performance multipliers
=IF(C3>=120, D3*0.15*1.5, IF(C3>=100, D3*0.1*1.2, D3*0.05))
// Higher commission rates and multipliers for exceeding quotas
```

### IF with Text Functions
Combines with text manipulation functions for dynamic content generation, data formatting, and conditional text processing.

```spreadsheets
// Dynamic greeting generation
=IF(E4="", "Hello Guest", CONCATENATE("Welcome back, ", E4, "!"))
// Personalized greeting based on whether name is provided

// Status report formatting
=IF(F5>90, UPPER("excellent"), IF(F5>70, PROPER("good performance"), "needs improvement"))
// Formats status text based on score with appropriate capitalization

// Email domain validation
=IF(ISNUMBER(FIND("@", G6)), RIGHT(G6, LEN(G6)-FIND("@", G6)), "Invalid email")
// Extracts domain from email addresses with validation
```

### IF with Date Functions
Essential for time-based logic, deadline management, and temporal data analysis in business applications.

```spreadsheets
// Project status based on deadlines
=IF(H7<TODAY(), "Overdue", IF(H7-TODAY()<=7, "Due Soon", "On Track"))
// Categorizes projects by deadline proximity

// Age-based eligibility determination
=IF(DATEDIF(I8, TODAY(), "Y")>=18, "Eligible", "Not Eligible")
// Determines eligibility based on calculated age

// Warranty status calculation
=IF(J9+365*2>TODAY(), "Under Warranty", "Warranty Expired")
// Checks if 2-year warranty is still valid
```

### IF with Lookup Functions
Combines with VLOOKUP, INDEX/MATCH, and other lookup functions for sophisticated data retrieval and conditional processing.

```spreadsheets
// Dynamic price lookup with discount logic
=IF(K10="Premium", VLOOKUP(L10, PriceTable, 2, 0)*0.9, VLOOKUP(L10, PriceTable, 2, 0))
// Applies 10% discount for premium customers

// Conditional data retrieval
=IF(COUNTIF(CustomerList, M11)>0, INDEX(CustomerData, MATCH(M11, CustomerList, 0), 3), "New Customer")
// Returns existing customer data or identifies new customers

// Multi-table lookup with conditions
=IF(N12="Domestic", VLOOKUP(O12, DomesticRates, 2, 0), VLOOKUP(O12, InternationalRates, 2, 0))
// Uses different rate tables based on shipping type
```

### IF with Statistical Functions
Integrates with statistical functions for conditional analysis, performance metrics, and data-driven decision making.

```spreadsheets
// Performance ranking with percentiles
=IF(P13>PERCENTILE($P$2:$P$100, 0.9), "Top 10%", IF(P13>PERCENTILE($P$2:$P$100, 0.5), "Above Average", "Below Average"))
// Ranks performance relative to dataset distribution

// Quality control with standard deviations
=IF(ABS(Q14-AVERAGE($Q$2:$Q$50))>2*STDEV($Q$2:$Q$50), "Outlier", "Normal")
// Identifies statistical outliers beyond 2 standard deviations

// Conditional aggregation
=IF(R15="Yes", SUMIF($S$2:$S$100, "Completed", $T$2:$T$100), "No data")
// Sums completed items only when analysis is enabled
```
