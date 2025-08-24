---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- logical
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- logical
- excel
- sheets
---
# OR

## OR Description

Tests multiple conditions and returns TRUE if ANY of the conditions evaluate to true. Returns FALSE only when ALL conditions are false. Perfect for flexible criteria where meeting any single requirement is sufficient.

> [!f(x)] OR Syntax
>
> ```spreadsheets
> OR(logical1, logical2, [logical3], ...)
> ```
>
> **Parameters:**
> - `logical1` (required): First condition to evaluate
> - `logical2` (required): Second condition to evaluate  
> - `logical3, ...` (optional): Additional conditions (up to 255 total arguments)

> [!f(x)] OR Examples
>
> ```spreadsheets
> // Basic flexible condition test
> OR(A1>100, B1="Premium") → TRUE if sales >$100 OR customer is Premium
> 
> // Multiple qualification paths
> OR(C2="Manager", D2>=10, E2="MBA") → TRUE if Manager OR 10+ years experience OR has MBA
> 
> // Alert condition checking
> OR(F3<10, G3>90, H3="Critical") → TRUE if stock <10 OR temp >90 OR critical status
> 
> // Weekend or holiday detection
> OR(WEEKDAY(I4,2)>5, J4="Holiday") → TRUE if weekend OR designated holiday
> 
> // Error or empty condition
> OR(ISERROR(K5), ISBLANK(L5)) → TRUE if calculation error OR cell is empty
> ```

## Use Cases

### [[Flexible criteria]]
- **Customer service escalation**: Route to supervisor if VIP customer, large order value, or complaint severity is high
- **Shipping qualification**: Offer expedited shipping for premium members, large orders, or urgent requests
- **Employee benefits eligibility**: Qualify for benefits if full-time, union member, or management level
- **Product discount eligibility**: Apply discount for bulk orders, loyalty members, or promotional periods

### [[Exception handling]]
- **System alerts**: Notify administrators if server downtime, high memory usage, or error rate exceeds threshold
- **Quality control flags**: Mark items for review if dimensions out of spec, weight unusual, or visual defects present
- **Payment processing**: Accept orders with credit card, PayPal, or corporate account payment methods
- **Access permissions**: Grant entry if employee badge, visitor pass, or emergency override is used

### [[Alternative pathways]]
- **Application approval**: Approve loans if excellent credit, sufficient collateral, or cosigner available
- **Academic admission**: Accept students with high GPA, exceptional test scores, or outstanding extracurriculars
- **Vendor qualification**: Work with suppliers offering lowest cost, fastest delivery, or highest quality ratings
- **Investment decisions**: Consider opportunities with high ROI, low risk profile, or strategic importance

### [[Data validation]]
- **Input acceptance**: Accept dates in multiple formats, various currency symbols, or different text encodings
- **File processing**: Handle CSV, Excel, or JSON data formats from different source systems
- **User authentication**: Allow login with username, email address, or employee ID credentials
- **Address validation**: Accept if ZIP code valid, state abbreviation correct, or city name matches database

## Related

### Similar Functions

- [[AND]] - Returns TRUE only when all conditions are true, opposite logic to OR
- [[XOR]] - Returns TRUE when exactly one condition is true, exclusive OR logic
- [[NOT]] - Reverses logical values, often combined with OR for complex exclusion logic
- [[IF]] - Uses OR results for conditional decisions and flexible branching logic
- [[IFS]] - Tests multiple OR conditions in sequence for cascading logic

## Conditional Logic Functions

### [[IF]]
OR creates flexible conditional logic in IF statements, allowing multiple acceptable paths to trigger the same result.

```spreadsheets
// Flexible bonus qualification
=IF(OR(A2>150000, B2="Excellent", C2>=10), A2*0.12, IF(OR(A2>75000, B2="Good"), A2*0.08, A2*0.03))
// 12% bonus if high sales OR excellent rating OR 10+ years, 8% if moderate sales OR good rating

// Multi-path shipping calculation
=IF(OR(D3="Express", E3="VIP", F3>1000), 0, IF(OR(G3="Standard", H3<50), 10, 25))
// Free shipping for express/VIP/large orders, $10 for standard/small items, $25 otherwise

// Flexible approval workflow
=IF(OR(I4="CEO", J4="VP", K4>100000), "Auto-Approve", "Requires Review")
// Auto-approve for executives or high-value requests
```

### [[AND]]
Combines with OR to create sophisticated logical structures mixing inclusive and exclusive criteria.

```spreadsheets
// Complex qualification matrix
=AND(OR(L5="Premium", M5>5000), N5>=18, O5="Active")
// Must be (Premium member OR large order) AND adult AND active account

// Multi-tier alert system
=OR(AND(P6>95, Q6="Production"), AND(R6<5, S6="Inventory"), T6="Critical")
// Alert if (>95% capacity AND production) OR (<5 units AND inventory item) OR critical flag

// Flexible access control
=AND(U7="Authorized", OR(V7="Employee", W7="Contractor", X7="Visitor"))
// Requires authorized status AND (employee OR contractor OR visitor)
```

### [[NOT]]
Combines with OR for exclusion logic and handling negative conditions across multiple criteria.

```spreadsheets
// Access denial conditions
=OR(NOT(Y8="Active"), Z8="Suspended", AA8<TODAY()-365)
// Deny if NOT active OR suspended OR account older than 1 year

// Quality exclusion criteria
=NOT(OR(BB9="Defective", CC9="Recalled", DD9="Expired"))
// Item acceptable if NOT (defective OR recalled OR expired)

// Working time validation
=OR(NOT(EE10>=9), NOT(FF10<=17), WEEKDAY(GG10,2)>5)
// Invalid if before 9 AM OR after 5 PM OR weekend
```

## Data Analysis Functions

### [[SUMIF]] and [[SUMIFS]]
OR logic can be simulated using multiple SUMIF functions to aggregate data meeting any of several criteria.

```spreadsheets
// Multi-criteria sales summation (OR logic simulation)
=SUMIF(HH:HH,"North",II:II)+SUMIF(HH:HH,"South",II:II)+SUMIF(HH:HH,"East",II:II)
// Sum sales from North OR South OR East regions

// Flexible product category totals
=SUMIF(JJ:JJ,"Electronics",KK:KK)+SUMIF(JJ:JJ,"Computers",KK:KK)+SUMIF(JJ:JJ,"Mobile",KK:KK)
// Total sales for Electronics OR Computers OR Mobile categories

// Multi-status order summation
=SUMIF(LL:LL,"Pending",MM:MM)+SUMIF(LL:LL,"Processing",MM:MM)+SUMIF(LL:LL,"Shipped",MM:MM)
// Sum orders that are Pending OR Processing OR Shipped
```

### [[COUNTIF]] and [[COUNTIFS]]
Similar OR logic simulation by adding multiple COUNTIF results to count items meeting any of several conditions.

```spreadsheets
// Multi-criteria customer counting
=COUNTIF(NN:NN,"Premium")+COUNTIF(NN:NN,"VIP")+COUNTIF(NN:NN,"Corporate")
// Count customers who are Premium OR VIP OR Corporate

// Flexible performance counting
=COUNTIF(OO:OO,">90")+COUNTIF(PP:PP,"Excellent")+COUNTIF(QQ:QQ,"A+")
// Count high performers by score >90 OR excellent rating OR A+ grade

// Multi-department employee count
=COUNTIF(RR:RR,"Sales")+COUNTIF(RR:RR,"Marketing")+COUNTIF(RR:RR,"Support")
// Count employees in Sales OR Marketing OR Support departments
```

### [[FILTER]]
Modern function that can implement OR logic using array formulas for dynamic data filtering.

```spreadsheets
// Multi-condition customer filtering
=FILTER(CustomerData, (SS:SS="Premium")+(TT:TT>5000)+(UU:UU="VIP"))
// Returns customers who are Premium OR have orders >$5000 OR VIP status

// Flexible date range filtering
=FILTER(ProjectData, (VV:VV>=TODAY())+(WW:WW="Critical")+(XX:XX="Overdue"))
// Shows projects due today+ OR critical priority OR overdue status

// Multi-category inventory filter
=FILTER(Inventory, (YY:YY="Electronics")+(ZZ:ZZ="Computers")+(AAA:AAA<10))
// Returns Electronics OR Computers OR items with stock <10
```

## Commonly Used With Functions Examples

### OR with Date Functions
OR provides flexible date-based logic for business rules, scheduling, and time-sensitive operations.

```spreadsheets
// Flexible scheduling validation
=IF(OR(WEEKDAY(BBB12,2)<6, CCC12="Holiday Override", DDD12="Emergency"), "Schedule", "Weekend/Holiday")
// Schedule if weekday OR holiday override OR emergency

// Multi-date milestone checking
=OR(EEE13<=TODAY(), FFF13="Complete", GGG13="Waived")
// Milestone met if due date passed OR marked complete OR waived

// Time-sensitive promotion eligibility
=IF(OR(HHH14>=DATE(2024,11,1), III14="Black Friday", JJJ14="Cyber Monday"), "Promo Price", "Regular Price")
// Special pricing for holiday season OR specific promotional days
```

### OR with Text Functions
Enables flexible text matching, format validation, and string processing with multiple acceptable patterns.

```spreadsheets
// Flexible email domain validation
=IF(OR(RIGHT(KKK15,4)=".com", RIGHT(KKK15,4)=".org", RIGHT(KKK15,4)=".edu"), "Valid Domain", "Check Format")
// Accept common email domains

// Multi-format phone number acceptance
=OR(LEN(MMM16)=10, LEN(MMM16)=12, LEN(MMM16)=14)
// Accept various phone number formats (with/without formatting)

// Flexible name validation
=OR(ISNUMBER(FIND(" ", NNN17)), LEN(NNN17)>2, OOO17="Mononym")
// Valid if contains space OR length >2 OR designated as single name
```

### OR with Lookup Functions
Creates flexible lookup logic with multiple table options and fallback strategies.

```spreadsheets
// Multi-table product lookup
=IF(OR(PPP18="A", PPP18="B"), VLOOKUP(QQQ18, TableA, 2, 0), VLOOKUP(QQQ18, TableB, 2, 0))
// Use different lookup tables based on product category

// Flexible customer data retrieval
=IF(OR(NOT(ISERROR(VLOOKUP(RRR19, ActiveCustomers, 1, 0))), NOT(ISERROR(VLOOKUP(RRR19, InactiveCustomers, 1, 0)))), "Found", "New")
// Check multiple customer databases

// Multi-criteria pricing lookup
=IF(OR(SSS20="Retail", TTT20>100, UUU20="Member"), VLOOKUP(VVV20, RetailPricing, 2, 0), VLOOKUP(VVV20, WholesalePricing, 2, 0))
// Use retail pricing for retail customers OR large orders OR members
```

### OR with Mathematical Functions
Provides flexible numerical criteria for calculations, validations, and business rule implementation.

```spreadsheets
// Flexible discount qualification
=IF(OR(WWW21>1000, XXX21>=5, YYY21="Loyalty"), WWW21*0.1, 0)
// 10% discount if order >$1000 OR quantity ≥5 OR loyalty member

// Multi-threshold performance bonus
=IF(OR(ZZZ22>PERCENTILE($ZZZ$2:$ZZZ$100,0.95), AAAA22="Outstanding"), BBBB22*0.15, IF(OR(ZZZ22>PERCENTILE($ZZZ$2:$ZZZ$100,0.8), AAAA22="Exceeds"), BBBB22*0.1, 0))
// Bonus for top 5% performance OR outstanding rating, secondary bonus for top 20% OR exceeds expectations

// Flexible credit approval
=OR(CCCC23/DDDD23>1.5, EEEE23>700, FFFF23="Excellent")
// Approve if debt-to-income <1.5 OR credit score >700 OR excellent reference
```

### OR with Error Handling Functions
Creates comprehensive error checking with multiple validation paths and fallback options.

```spreadsheets
// Comprehensive data validation
=IF(OR(ISERROR(GGGG24), ISBLANK(HHHH24), IIII24<=0), "Invalid Data", "Valid")
// Flag as invalid if calculation error OR blank OR non-positive value

// Multi-format date validation
=OR(NOT(ISERROR(DATE(JJJJ25,1,1))), NOT(ISERROR(DATEVALUE(KKKK25))), LLLL25="TBD")
// Valid if year format works OR text date works OR marked as TBD

// Flexible reference checking
=IF(OR(NOT(ISNA(VLOOKUP(MMMM26, RefTable1, 1, 0))), NOT(ISNA(VLOOKUP(MMMM26, RefTable2, 1, 0))), NNNN26="Override"), "Authorized", "Check Reference")
// Authorized if found in either reference table OR has override flag
```
