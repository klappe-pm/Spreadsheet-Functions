---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - database
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
# DPRODUCT

## DPRODUCT Description

Multiplies all values in a database that match specified criteria by evaluating records against multiple conditions. DPRODUCT works with structured data where the first row contains field headers and subsequent rows contain data records.

> [!f(x)] DPRODUCT Syntax
>
> ```spreadsheets
> DPRODUCT(database, field, criteria)
> ```
>
> **Parameters:**
> - `database` (required): The range of cells that makes up the database or list including headers
> - `field` (required): Column to multiply - can be column label (in quotes) or column number
> - `criteria` (required): Range containing conditions that specify which records to multiply

> [!f(x)] DPRODUCT Examples
>
> ```spreadsheets
> // Multiply growth rates where region is "West"
> DPRODUCT(A1:E20, "GrowthRate", G1:G2) → 1.728
> 
> // Multiply conversion factors where unit = "Imperial"
> DPRODUCT(A1:F100, "Factor", H1:I3) → 2.54
> 
> // Calculate compound interest for specific accounts
> DPRODUCT(Database, "InterestRate", AccountCriteria) → 1.1576
> 
> // Multiply probability values for risk assessment
> DPRODUCT(A1:D50, "Probability", F1:F2) → 0.125
> 
> // Calculate total scaling factor
> DPRODUCT(Scaling, "Factor", ProcessCriteria) → 8.0
> ```

## Use Cases

### [[Compound calculations]]
- **Growth rate analysis**: Calculate compound growth by multiplying individual period growth rates to determine total growth over time
- **Interest calculations**: Compute compound interest by multiplying interest factors for multiple periods or accounts
- **Probability analysis**: Calculate joint probabilities by multiplying individual event probabilities for risk assessment
- **Scaling operations**: Determine total scaling factors by multiplying individual transformation ratios
- **Rate conversions**: Calculate compound conversion rates by multiplying sequential conversion factors

### [[Risk assessment]]
- **Failure probability**: Calculate overall system failure probability by multiplying individual component reliability rates
- **Success likelihood**: Determine project success probability by multiplying individual milestone success rates
- **Security risk**: Calculate compound security risk by multiplying individual vulnerability probabilities
- **Quality assurance**: Determine overall quality probability by multiplying individual process quality rates
- **Performance reliability**: Calculate system reliability by multiplying individual component performance factors

### [[Financial modeling]]
- **Investment returns**: Calculate compound returns by multiplying individual period return rates for portfolio analysis
- **Currency conversion**: Perform multi-step currency conversions by multiplying sequential exchange rates
- **Discount factors**: Calculate present value factors by multiplying individual discount rates over multiple periods
- **Cost multipliers**: Determine total cost impact by multiplying individual cost adjustment factors
- **Pricing calculations**: Calculate final prices by multiplying base prices with various adjustment factors

## Related

### Similar Functions

- [[PRODUCT]] - Multiplies values in ranges without database criteria filtering
- [[DSUM]] - Sums values instead of multiplying for database records matching criteria
- [[DAVERAGE]] - Averages values instead of multiplying for database records matching criteria
- [[DCOUNT]] - Counts records instead of multiplying for database records matching criteria
- [[POWER]] - Raises numbers to specified powers for exponential calculations

## Mathematical Functions

### [[PRODUCT]]
Simpler alternative for multiplying values without database criteria. PRODUCT works with ranges while DPRODUCT provides database-style filtering capabilities.

```spreadsheets
// Compare database vs range multiplication
=DPRODUCT(A1:C100,"Factor",E1:E2) & " (filtered) vs " & PRODUCT(C1:C100) & " (all values)"
// Shows difference between filtered database product and range product

// Compound growth calculation with filtering
=DPRODUCT(GrowthData,"Rate",YearCriteria) & " compound growth for selected years"
// Calculates compound growth only for specified years using database filtering

// Risk probability with conditional multiplication
=DPRODUCT(RiskFactors,"Probability",HighRiskCriteria) & " combined high-risk probability"
// Multiplies only high-risk probabilities using database criteria
```

### [[POWER]]
Complementary function for exponential calculations when DPRODUCT results need to be raised to powers or when calculating compound effects.

```spreadsheets
// Compound interest with time periods
=POWER(DPRODUCT(Rates,"InterestRate",AccountCriteria), YearsPeriod) & " final compound factor"
// Uses DPRODUCT for base rate calculation, POWER for time compounding

// Growth projection with exponential scaling
=InitialValue * POWER(DPRODUCT(Factors,"GrowthFactor",Criteria), ProjectionYears)
// Combines DPRODUCT for factor calculation with POWER for projection

// Probability scaling with confidence levels
=POWER(DPRODUCT(Events,"Probability",Criteria), ConfidenceLevel) & " adjusted probability"
// Adjusts compound probability using exponential confidence scaling
```

## Commonly Used With Functions Examples

### Investment Portfolio Analysis
```spreadsheets
// Multi-period return calculation with compound growth
="Portfolio Return: " & ROUND((DPRODUCT(Returns,"MonthlyReturn",PortfolioCriteria)-1)*100,2) & "%" &
" | Annualized: " & ROUND((POWER(DPRODUCT(Returns,"MonthlyReturn",PortfolioCriteria),12)-1)*100,2) & "%" &
" | Risk Factor: " & DPRODUCT(Risk,"RiskMultiplier",RiskCriteria) &
" | Adjusted Return: " & ROUND(((DPRODUCT(Returns,"MonthlyReturn",PortfolioCriteria)/DPRODUCT(Risk,"RiskMultiplier",RiskCriteria))-1)*100,2) & "%"
// Comprehensive investment analysis with compound returns and risk adjustment
```

### Manufacturing Quality Control
```spreadsheets
// Process reliability calculation with multiple stages
="Process: " & ProcessName & " | Stage Reliability: " & ROUND(DPRODUCT(Stages,"ReliabilityRate",ProcessCriteria)*100,2) & "%" &
" | Daily Production: " & DailyUnits & " units" &
" | Expected Good Units: " & ROUND(DailyUnits*DPRODUCT(Stages,"ReliabilityRate",ProcessCriteria),0) &
" | Defect Rate: " & ROUND((1-DPRODUCT(Stages,"ReliabilityRate",ProcessCriteria))*100,2) & "%" &
" | Quality Status: " & IF(DPRODUCT(Stages,"ReliabilityRate",ProcessCriteria)>=TargetReliability,"On Target","Below Standard")
// Manufacturing quality analysis with compound reliability calculations
```

### Currency and Unit Conversions
```spreadsheets
// Multi-step currency conversion with transaction costs
="Original: " & OriginalAmount & " " & BaseCurrency &
" | Conversion Factor: " & DPRODUCT(Rates,"ExchangeRate",ConversionPath) &
" | Transaction Costs: " & DPRODUCT(Costs,"CostMultiplier",TransactionCriteria) &
" | Final Amount: " & ROUND(OriginalAmount*DPRODUCT(Rates,"ExchangeRate",ConversionPath)*DPRODUCT(Costs,"CostMultiplier",TransactionCriteria),2) & " " & TargetCurrency &
" | Total Cost: " & ROUND(OriginalAmount*(1-DPRODUCT(Rates,"ExchangeRate",ConversionPath)*DPRODUCT(Costs,"CostMultiplier",TransactionCriteria)),2) & " " & BaseCurrency
// Complex currency conversion with multiple factors and cost calculations
```

### Risk Assessment Matrix
```spreadsheets
// Compound risk probability with mitigation factors
="Risk Scenario: " & RiskName & " | Base Probability: " & ROUND(DPRODUCT(Factors,"Probability",ScenarioCriteria)*100,2) & "%" &
" | Mitigation Effect: " & ROUND(DPRODUCT(Mitigation,"EffectivnessFactor",MitigationCriteria)*100,2) & "%" &
" | Final Risk: " & ROUND(DPRODUCT(Factors,"Probability",ScenarioCriteria)*DPRODUCT(Mitigation,"EffectivnessFactor",MitigationCriteria)*100,2) & "%" &
" | Risk Level: " & IF(DPRODUCT(Factors,"Probability",ScenarioCriteria)*DPRODUCT(Mitigation,"EffectivnessFactor",MitigationCriteria)<0.01,"Low",IF(DPRODUCT(Factors,"Probability",ScenarioCriteria)*DPRODUCT(Mitigation,"EffectivnessFactor",MitigationCriteria)<0.05,"Medium","High"))
// Risk assessment with compound probability and mitigation factor calculations
```

### Pricing Strategy Analysis
```spreadsheets
// Multi-factor pricing with compound adjustments
="Base Price: $" & BasePrice & " | Market Factors: " & ROUND(DPRODUCT(Market,"PriceMultiplier",MarketCriteria),3) &
" | Cost Adjustments: " & ROUND(DPRODUCT(Costs,"CostFactor",CostCriteria),3) &
" | Competition Factor: " & ROUND(DPRODUCT(Competition,"CompetitiveIndex",CompCriteria),3) &
" | Final Price: $" & ROUND(BasePrice*DPRODUCT(Market,"PriceMultiplier",MarketCriteria)*DPRODUCT(Costs,"CostFactor",CostCriteria)*DPRODUCT(Competition,"CompetitiveIndex",CompCriteria),2) &
" | Margin: " & ROUND(((BasePrice*DPRODUCT(Market,"PriceMultiplier",MarketCriteria)*DPRODUCT(Costs,"CostFactor",CostCriteria)*DPRODUCT(Competition,"CompetitiveIndex",CompCriteria))-ProductCost)/ProductCost*100,1) & "%"
// Comprehensive pricing analysis with multiple compound adjustment factors
```
