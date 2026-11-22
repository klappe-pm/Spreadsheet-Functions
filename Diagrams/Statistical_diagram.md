---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Statistical
purpose:
  - Function Relationships
use-case:
  - Choosing a Statistical Function
  - Comparing Averages and Spread
related:
  - AVEDEV
  - AVERAGE
  - AVERAGEA
  - AVERAGEIF
  - AVERAGEIFS
  - BETA.DIST
  - BETA.INV
  - BINOM.DIST
  - BINOM.DIST.RANGE
  - BINOM.INV
  - CHISQ.DIST
  - CHISQ.DIST.RT
  - CHISQ.INV
  - CHISQ.INV.RT
  - CHISQ.TEST
  - COMBIN
  - COMBINA
  - CONFIDENCE.NORM
  - CONFIDENCE.T
  - CORREL
  - COUNT
  - COUNTA
  - COUNTBLANK
  - COUNTIF
  - COUNTIFS
  - COUNTUNIQUE
  - COUNTUNIQUEIFS
  - COVAR
  - COVARIANCE.P
  - COVARIANCE.S
  - DEVSQ
  - EXPON.DIST
  - F.DIST
  - F.DIST.RT
  - LARGE
  - MAX
  - MEDIAN
  - MIN
  - MODE
  - SMALL
level: 3
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - statistical
  - distribution
  - regression
---

# Statistical Functions Relationship Diagram

This diagram shows the relationships between functions in the Statistical category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Statistical fill:#FF6B6B,stroke:#333,stroke-width:2px,color:#000
    COVARIANCE_S["COVARIANCE.S<br/>Returns the sample covariance of two data sets"]
    MEDIAN["MEDIAN<br/>Returns the median of the given numbers"]
    T_DIST_RT["T.DIST.RT<br/>Returns the right-tailed Student's t-distribution"]
    MODE_MULT["MODE.MULT<br/>Returns a vertical array of the most frequently occurring values"]
    SMALL["SMALL<br/>Returns the k-th smallest value in a data set"]
    T_DIST_2T["T.DIST.2T<br/>Returns the two-tailed Student's t-distribution"]
    NORM_INV["NORM.INV<br/>Returns the inverse of the normal cumulative distribution"]
    WEIBULL_DIST["WEIBULL.DIST<br/>Returns the Weibull distribution"]
    GEOMEAN["GEOMEAN<br/>Returns the geometric mean"]
    LINEST["LINEST<br/>Returns the parameters of a linear trend"]
    LARGE["LARGE<br/>Returns the k-th largest value in a data set"]
    F_DIST["F.DIST<br/>Returns the left-tailed F probability distribution"]
    STEYX["STEYX<br/>Returns the standard error of the predicted y-value for each x"]
    TRIMMEAN["TRIMMEAN<br/>Returns the mean of the interior of a data set"]
    T_TEST["T.TEST<br/>Returns the probability associated with a Student's t-test"]
    COUNTA["COUNTA<br/>Counts how many values are in the list of arguments"]
    MAXIFS["MAXIFS<br/>Returns the maximum value among cells that meet multiple criteria"]
    CONFIDENCE_T["CONFIDENCE.T<br/>Returns a confidence interval for a mean (Student's t)"]
    RANK_EQ["RANK.EQ<br/>Returns the rank of a number in a list of numbers"]
    VAR["VAR<br/>Estimates variance based on a sample"]
    MIN["MIN<br/>Returns the minimum value in a list of arguments"]
    CONFIDENCE_NORM["CONFIDENCE.NORM<br/>Returns a confidence interval for a population mean"]
    MODE["MODE<br/>Returns the most common value in a data set"]
    STANDARDIZE["STANDARDIZE<br/>Returns a normalized value"]
    FORECAST_LINEAR["FORECAST.LINEAR<br/>Returns a future value along a linear trend"]
    FORECAST_ETS["FORECAST.ETS<br/>Returns a future value using exponential smoothing (ETS)"]
    CHISQ_INV["CHISQ.INV<br/>Returns the inverse of the left-tailed chi-squared distribution"]
    VARPA["VARPA<br/>Calculates population variance, including text and logical values"]
    NORM_S_INV["NORM.S.INV<br/>Returns the inverse of the standard normal cumulative distribution"]
    COUNTIF["COUNTIF<br/>Counts cells within a range that meet a given criterion"]
    GAMMALN_PRECISE["GAMMALN.PRECISE<br/>Returns the natural logarithm of the gamma function"]
    FORECAST_ETS_STAT["FORECAST.ETS.STAT<br/>Returns a statistic for a time series forecast"]
    BINOM_DIST["BINOM.DIST<br/>Returns the binomial distribution probability"]
    COUNTUNIQUEIFS["COUNTUNIQUEIFS<br/>Counts unique values with conditions (Google Sheets only)"]
    MAXA["MAXA<br/>Returns the maximum value, including text and logical values"]
    F_INV_RT["F.INV.RT<br/>Returns the inverse of the right-tailed F distribution"]
    KURT["KURT<br/>Returns the kurtosis of a data set"]
    SKEW_P["SKEW.P<br/>Returns the skewness of a distribution based on a population"]
    CORREL["CORREL<br/>Returns the correlation coefficient of two data sets"]
    DEVSQ["DEVSQ<br/>Returns the sum of squared deviations from the mean"]
    VARP["VARP<br/>Calculates variance based on the entire population"]
    FORECAST_ETS_SEASONALITY["FORECAST.ETS.SEASONALITY<br/>Returns the length of the repeating pattern in a time series"]
    COUNTBLANK["COUNTBLANK<br/>Counts the number of blank cells within a range"]
    CHISQ_TEST["CHISQ.TEST<br/>Returns the chi-squared test for independence"]
    QUARTILE_INC["QUARTILE.INC<br/>Returns the quartile of a data set, using inclusive percentiles"]
    RANK["RANK<br/>Returns the rank of a number in a list of numbers"]
    PERCENTILE["PERCENTILE<br/>Returns the k-th percentile of values in a range"]
    PHI["PHI<br/>Returns the density of a standard normal distribution"]
    STDEVP["STDEVP<br/>Calculates standard deviation based on the entire population"]
    T_INV_2T["T.INV.2T<br/>Returns the inverse of the two-tailed Student's t-distribution"]
    QUARTILE_EXC["QUARTILE.EXC<br/>Returns the quartile of a data set, using exclusive percentiles"]
    GAMMA["GAMMA<br/>Returns the Gamma function value"]
    COUNT["COUNT<br/>Counts how many numbers are in the list of arguments"]
    VAR_P["VAR.P<br/>Calculates variance based on the entire population"]
    PERCENTRANK_EXC["PERCENTRANK.EXC<br/>Returns the percentage rank of a value, exclusive of endpoints"]
    AVERAGEIF["AVERAGEIF<br/>Returns the average of cells that meet a single criterion"]
    FISHERINV["FISHERINV<br/>Returns the inverse of the Fisher transformation"]
    NORM_S_DIST["NORM.S.DIST<br/>Returns the standard normal cumulative distribution"]
    RSQ["RSQ<br/>Returns the square of the Pearson correlation coefficient"]
    MODE_SNGL["MODE.SNGL<br/>Returns the most common value in a data set"]
    STDEV_S["STDEV.S<br/>Estimates standard deviation based on a sample"]
    AVEDEV["AVEDEV<br/>Returns the average of the absolute deviations from the mean"]
    CHISQ_INV_RT["CHISQ.INV.RT<br/>Returns the inverse of the right-tailed chi-squared distribution"]
    AVERAGE["AVERAGE<br/>Returns the average of its arguments"]
    PERCENTRANK_INC["PERCENTRANK.INC<br/>Returns the percentage rank of a value, inclusive of endpoints"]
    PERCENTRANK["PERCENTRANK<br/>Returns the percentage rank of a value in a data set"]
    AVERAGEA["AVERAGEA<br/>Returns the average of its arguments, including text and logicals"]
    COUNTUNIQUE["COUNTUNIQUE<br/>Counts unique values in a range (Google Sheets only)"]
    PERMUTATIONA["PERMUTATIONA<br/>Returns permutations with repetitions"]
    T_DIST["T.DIST<br/>Returns the left-tailed Student's t-distribution"]
    GAMMALN["GAMMALN<br/>Returns the natural logarithm of the gamma function"]
    STDEV_P["STDEV.P<br/>Calculates standard deviation based on the entire population"]
    F_TEST["F.TEST<br/>Returns the result of an F-test"]
    FORECAST["FORECAST<br/>Returns a value along a linear trend (legacy, see FORECAST.LINEAR)"]
    COVAR["COVAR<br/>Returns covariance, the average of paired deviation products"]
    PEARSON["PEARSON<br/>Returns the Pearson product moment correlation coefficient"]
    FISHER["FISHER<br/>Returns the Fisher transformation"]
    COMBINA["COMBINA<br/>Returns combinations with repetitions"]
    INTERCEPT["INTERCEPT<br/>Returns the intercept of the linear regression line"]
    LOGNORM_INV["LOGNORM.INV<br/>Returns the inverse of the lognormal cumulative distribution"]
    SKEW["SKEW<br/>Returns the skewness of a distribution"]
    Z_TEST["Z.TEST<br/>Returns the one-tailed probability of a z-test"]
    STDEV["STDEV<br/>Estimates standard deviation based on a sample"]
    PROB["PROB<br/>Returns the probability that values fall between two limits"]
    FREQUENCY["FREQUENCY<br/>Returns a frequency distribution as a vertical array"]
    PERCENTILE_EXC["PERCENTILE.EXC<br/>Returns the k-th percentile of values, using exclusive bounds"]
    COUNTIFS["COUNTIFS<br/>Counts cells that meet multiple criteria"]
    HYPGEOM_DIST["HYPGEOM.DIST<br/>Returns the hypergeometric distribution"]
    F_INV["F.INV<br/>Returns the inverse of the left-tailed F distribution"]
    NORM_DIST["NORM.DIST<br/>Returns the normal cumulative distribution"]
    PERCENTILE_INC["PERCENTILE.INC<br/>Returns the k-th percentile of values, using inclusive bounds"]
    AVERAGEIFS["AVERAGEIFS<br/>Returns the average of cells that meet multiple criteria"]
    F_DIST_RT["F.DIST.RT<br/>Returns the right-tailed F probability distribution"]
    GAMMA_DIST["GAMMA.DIST<br/>Returns the gamma distribution"]
    BINOM_DIST_RANGE["BINOM.DIST.RANGE<br/>Returns a binomial probability for a range of trial results"]
    CHISQ_DIST_RT["CHISQ.DIST.RT<br/>Returns the right-tailed chi-squared distribution"]
    MINA["MINA<br/>Returns the minimum value, including text and logical values"]
    MAX["MAX<br/>Returns the maximum value in a list of arguments"]
    VAR_S["VAR.S<br/>Estimates variance based on a sample"]
    GROWTH["GROWTH<br/>Returns values along an exponential trend"]
    BINOM_INV["BINOM.INV<br/>Returns the smallest value meeting a cumulative binomial criterion"]
    CHISQ_DIST["CHISQ.DIST<br/>Returns the chi-squared distribution"]
    LOGNORM_DIST["LOGNORM.DIST<br/>Returns the cumulative lognormal distribution"]
    GAMMA_INV["GAMMA.INV<br/>Returns the inverse of the gamma cumulative distribution"]
    PERMUT["PERMUT<br/>Returns the number of permutations for a given number of objects"]
    LOGEST["LOGEST<br/>Returns the parameters of an exponential trend"]
    MINIFS["MINIFS<br/>Returns the minimum value among cells that meet multiple criteria"]
    POISSON_DIST["POISSON.DIST<br/>Returns the Poisson distribution"]
    BETA_INV["BETA.INV<br/>Returns the inverse of the cumulative beta distribution"]
    COVARIANCE_P["COVARIANCE.P<br/>Returns the population covariance of two data sets"]
    HARMEAN["HARMEAN<br/>Returns the harmonic mean"]
    STDEVPA["STDEVPA<br/>Calculates population standard deviation, including text and logicals"]
    TREND["TREND<br/>Returns values along a linear trend"]
    VARA["VARA<br/>Estimates variance based on a sample, including text and logicals"]
    BETA_DIST["BETA.DIST<br/>Returns the cumulative beta distribution function"]
    GAUSS["GAUSS<br/>Returns 0.5 less than the standard normal cumulative distribution"]
    SLOPE["SLOPE<br/>Returns the slope of the linear regression line"]
    COMBIN["COMBIN<br/>Returns the number of combinations for a given number of objects"]
    NEGBINOM_DIST["NEGBINOM.DIST<br/>Returns the negative binomial distribution"]
    EXPON_DIST["EXPON.DIST<br/>Returns the exponential distribution"]
    FORECAST_ETS_CONFINT["FORECAST.ETS.CONFINT<br/>Returns a confidence interval for a forecast value"]
    RANK_AVG["RANK.AVG<br/>Returns the average rank of a number in a list of numbers"]
    STDEVA["STDEVA<br/>Estimates standard deviation of a sample, with text and logicals"]
    T_INV["T.INV<br/>Returns the inverse of the left-tailed Student's t-distribution"]
    QUARTILE["QUARTILE<br/>Returns the quartile of a data set"]
    IF["IF<br/>External Function"]
    COVARIANCE_S --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COVARIANCE_S --> SUM
    class SUM external
    COVARIANCE_S --> AVERAGE
    IF["IF<br/>Related Function"]
    COVARIANCE_S -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COVARIANCE_S -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MEDIAN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MEDIAN --> SUM
    class SUM external
    MEDIAN --> AVERAGE
    IF["IF<br/>Related Function"]
    MEDIAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MEDIAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    T_DIST_RT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    T_DIST_RT --> SUM
    class SUM external
    T_DIST_RT --> AVERAGE
    IF["IF<br/>Related Function"]
    T_DIST_RT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    T_DIST_RT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MODE_MULT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MODE_MULT --> SUM
    class SUM external
    MODE_MULT --> AVERAGE
    IF["IF<br/>Related Function"]
    MODE_MULT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MODE_MULT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SMALL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SMALL --> SUM
    class SUM external
    SMALL --> AVERAGE
    IF["IF<br/>Related Function"]
    SMALL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SMALL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    T_DIST_2T --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    T_DIST_2T --> SUM
    class SUM external
    T_DIST_2T --> AVERAGE
    IF["IF<br/>Related Function"]
    T_DIST_2T -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    T_DIST_2T -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    NORM_INV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    NORM_INV --> SUM
    class SUM external
    NORM_INV --> AVERAGE
    IF["IF<br/>Related Function"]
    NORM_INV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    NORM_INV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    WEIBULL_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    WEIBULL_DIST --> SUM
    class SUM external
    WEIBULL_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    WEIBULL_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    WEIBULL_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GEOMEAN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GEOMEAN --> SUM
    class SUM external
    GEOMEAN --> AVERAGE
    IF["IF<br/>Related Function"]
    GEOMEAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GEOMEAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LINEST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    LINEST --> SUM
    class SUM external
    LINEST --> AVERAGE
    IF["IF<br/>Related Function"]
    LINEST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LINEST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LARGE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    LARGE --> SUM
    class SUM external
    LARGE --> AVERAGE
    IF["IF<br/>Related Function"]
    LARGE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LARGE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    F_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    F_DIST --> SUM
    class SUM external
    F_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    F_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    F_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    STEYX --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    STEYX --> SUM
    class SUM external
    STEYX --> AVERAGE
    IF["IF<br/>Related Function"]
    STEYX -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    STEYX -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TRIMMEAN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TRIMMEAN --> SUM
    class SUM external
    TRIMMEAN --> AVERAGE
    IF["IF<br/>Related Function"]
    TRIMMEAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TRIMMEAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    T_TEST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    T_TEST --> SUM
    class SUM external
    T_TEST --> AVERAGE
    IF["IF<br/>Related Function"]
    T_TEST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    T_TEST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUNTA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUNTA --> SUM
    class SUM external
    COUNTA --> AVERAGE
    IF["IF<br/>Related Function"]
    COUNTA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COUNTA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MAXIFS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MAXIFS --> SUM
    class SUM external
    MAXIFS --> COUNT
    IF["IF<br/>Related Function"]
    MAXIFS -.-> IF
    class IF external
    SUMIF["SUMIF<br/>Related Function"]
    MAXIFS -.-> SUMIF
    class SUMIF external
    IF["IF<br/>External Function"]
    CONFIDENCE_T --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CONFIDENCE_T --> SUM
    class SUM external
    CONFIDENCE_T --> AVERAGE
    IF["IF<br/>Related Function"]
    CONFIDENCE_T -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CONFIDENCE_T -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RANK_EQ --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    RANK_EQ --> SUM
    class SUM external
    RANK_EQ --> AVERAGE
    IF["IF<br/>Related Function"]
    RANK_EQ -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    RANK_EQ -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    VAR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VAR --> SUM
    class SUM external
    VAR --> AVERAGE
    IF["IF<br/>Related Function"]
    VAR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    VAR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MIN --> IF
    class IF external
    INDEX["INDEX<br/>External Function"]
    MIN --> INDEX
    class INDEX external
    MATCH["MATCH<br/>External Function"]
    MIN --> MATCH
    class MATCH external
    MIN -.-> MAX
    MIN -.-> SMALL
    IF["IF<br/>External Function"]
    CONFIDENCE_NORM --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CONFIDENCE_NORM --> SUM
    class SUM external
    CONFIDENCE_NORM --> AVERAGE
    IF["IF<br/>Related Function"]
    CONFIDENCE_NORM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CONFIDENCE_NORM -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MODE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MODE --> SUM
    class SUM external
    MODE --> AVERAGE
    IF["IF<br/>Related Function"]
    MODE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MODE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    STANDARDIZE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    STANDARDIZE --> SUM
    class SUM external
    STANDARDIZE --> AVERAGE
    IF["IF<br/>Related Function"]
    STANDARDIZE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    STANDARDIZE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FORECAST_LINEAR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FORECAST_LINEAR --> SUM
    class SUM external
    FORECAST_LINEAR --> AVERAGE
    IF["IF<br/>Related Function"]
    FORECAST_LINEAR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FORECAST_LINEAR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FORECAST_ETS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FORECAST_ETS --> SUM
    class SUM external
    FORECAST_ETS --> AVERAGE
    IF["IF<br/>Related Function"]
    FORECAST_ETS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FORECAST_ETS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CHISQ_INV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHISQ_INV --> SUM
    class SUM external
    CHISQ_INV --> AVERAGE
    IF["IF<br/>Related Function"]
    CHISQ_INV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CHISQ_INV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    VARPA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VARPA --> SUM
    class SUM external
    VARPA --> AVERAGE
    IF["IF<br/>Related Function"]
    VARPA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    VARPA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    NORM_S_INV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    NORM_S_INV --> SUM
    class SUM external
    NORM_S_INV --> AVERAGE
    IF["IF<br/>Related Function"]
    NORM_S_INV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    NORM_S_INV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUNTIF --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUNTIF --> SUM
    class SUM external
    COUNTIF --> COUNT
    IF["IF<br/>Related Function"]
    COUNTIF -.-> IF
    class IF external
    SUMIF["SUMIF<br/>Related Function"]
    COUNTIF -.-> SUMIF
    class SUMIF external
    IF["IF<br/>External Function"]
    GAMMALN_PRECISE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GAMMALN_PRECISE --> SUM
    class SUM external
    GAMMALN_PRECISE --> AVERAGE
    IF["IF<br/>Related Function"]
    GAMMALN_PRECISE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GAMMALN_PRECISE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FORECAST_ETS_STAT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FORECAST_ETS_STAT --> SUM
    class SUM external
    FORECAST_ETS_STAT --> AVERAGE
    IF["IF<br/>Related Function"]
    FORECAST_ETS_STAT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FORECAST_ETS_STAT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BINOM_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BINOM_DIST --> SUM
    class SUM external
    BINOM_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    BINOM_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BINOM_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUNTUNIQUEIFS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUNTUNIQUEIFS --> SUM
    class SUM external
    COUNTUNIQUEIFS --> COUNT
    IF["IF<br/>Related Function"]
    COUNTUNIQUEIFS -.-> IF
    class IF external
    SUMIF["SUMIF<br/>Related Function"]
    COUNTUNIQUEIFS -.-> SUMIF
    class SUMIF external
    IF["IF<br/>External Function"]
    MAXA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MAXA --> SUM
    class SUM external
    MAXA --> AVERAGE
    IF["IF<br/>Related Function"]
    MAXA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MAXA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    F_INV_RT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    F_INV_RT --> SUM
    class SUM external
    F_INV_RT --> AVERAGE
    IF["IF<br/>Related Function"]
    F_INV_RT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    F_INV_RT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    KURT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    KURT --> SUM
    class SUM external
    KURT --> AVERAGE
    IF["IF<br/>Related Function"]
    KURT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    KURT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SKEW_P --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SKEW_P --> SUM
    class SUM external
    SKEW_P --> AVERAGE
    IF["IF<br/>Related Function"]
    SKEW_P -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SKEW_P -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CORREL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CORREL --> SUM
    class SUM external
    CORREL --> AVERAGE
    IF["IF<br/>Related Function"]
    CORREL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CORREL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DEVSQ --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DEVSQ --> SUM
    class SUM external
    DEVSQ --> AVERAGE
    IF["IF<br/>Related Function"]
    DEVSQ -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DEVSQ -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    VARP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VARP --> SUM
    class SUM external
    VARP --> AVERAGE
    IF["IF<br/>Related Function"]
    VARP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    VARP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FORECAST_ETS_SEASONALITY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FORECAST_ETS_SEASONALITY --> SUM
    class SUM external
    FORECAST_ETS_SEASONALITY --> AVERAGE
    IF["IF<br/>Related Function"]
    FORECAST_ETS_SEASONALITY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FORECAST_ETS_SEASONALITY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUNTBLANK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUNTBLANK --> SUM
    class SUM external
    COUNTBLANK --> AVERAGE
    IF["IF<br/>Related Function"]
    COUNTBLANK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COUNTBLANK -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CHISQ_TEST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHISQ_TEST --> SUM
    class SUM external
    CHISQ_TEST --> AVERAGE
    IF["IF<br/>Related Function"]
    CHISQ_TEST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CHISQ_TEST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    QUARTILE_INC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    QUARTILE_INC --> SUM
    class SUM external
    QUARTILE_INC --> AVERAGE
    IF["IF<br/>Related Function"]
    QUARTILE_INC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    QUARTILE_INC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RANK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    RANK --> SUM
    class SUM external
    RANK --> AVERAGE
    IF["IF<br/>Related Function"]
    RANK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    RANK -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PERCENTILE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PERCENTILE --> SUM
    class SUM external
    PERCENTILE --> AVERAGE
    IF["IF<br/>Related Function"]
    PERCENTILE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PERCENTILE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PHI --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PHI --> SUM
    class SUM external
    PHI --> AVERAGE
    IF["IF<br/>Related Function"]
    PHI -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PHI -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    STDEVP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    STDEVP --> SUM
    class SUM external
    STDEVP --> AVERAGE
    IF["IF<br/>Related Function"]
    STDEVP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    STDEVP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    T_INV_2T --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    T_INV_2T --> SUM
    class SUM external
    T_INV_2T --> AVERAGE
    IF["IF<br/>Related Function"]
    T_INV_2T -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    T_INV_2T -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    QUARTILE_EXC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    QUARTILE_EXC --> SUM
    class SUM external
    QUARTILE_EXC --> AVERAGE
    IF["IF<br/>Related Function"]
    QUARTILE_EXC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    QUARTILE_EXC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GAMMA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GAMMA --> SUM
    class SUM external
    GAMMA --> AVERAGE
    IF["IF<br/>Related Function"]
    GAMMA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GAMMA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUNT --> IF
    class IF external
    COUNT --> AVERAGE
    SUM["SUM<br/>External Function"]
    COUNT --> SUM
    class SUM external
    COUNT -.-> COUNTA
    COUNT -.-> COUNTIF
    IF["IF<br/>External Function"]
    VAR_P --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VAR_P --> SUM
    class SUM external
    VAR_P --> AVERAGE
    IF["IF<br/>Related Function"]
    VAR_P -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    VAR_P -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PERCENTRANK_EXC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PERCENTRANK_EXC --> SUM
    class SUM external
    PERCENTRANK_EXC --> AVERAGE
    IF["IF<br/>Related Function"]
    PERCENTRANK_EXC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PERCENTRANK_EXC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    AVERAGEIF --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    AVERAGEIF --> SUM
    class SUM external
    AVERAGEIF --> COUNT
    IF["IF<br/>Related Function"]
    AVERAGEIF -.-> IF
    class IF external
    SUMIF["SUMIF<br/>Related Function"]
    AVERAGEIF -.-> SUMIF
    class SUMIF external
    IF["IF<br/>External Function"]
    FISHERINV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FISHERINV --> SUM
    class SUM external
    FISHERINV --> AVERAGE
    IF["IF<br/>Related Function"]
    FISHERINV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FISHERINV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    NORM_S_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    NORM_S_DIST --> SUM
    class SUM external
    NORM_S_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    NORM_S_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    NORM_S_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RSQ --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    RSQ --> SUM
    class SUM external
    RSQ --> AVERAGE
    IF["IF<br/>Related Function"]
    RSQ -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    RSQ -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MODE_SNGL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MODE_SNGL --> SUM
    class SUM external
    MODE_SNGL --> AVERAGE
    IF["IF<br/>Related Function"]
    MODE_SNGL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MODE_SNGL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    STDEV_S --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    STDEV_S --> SUM
    class SUM external
    STDEV_S --> AVERAGE
    IF["IF<br/>Related Function"]
    STDEV_S -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    STDEV_S -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    AVEDEV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    AVEDEV --> SUM
    class SUM external
    AVEDEV --> AVERAGE
    IF["IF<br/>Related Function"]
    AVEDEV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    AVEDEV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CHISQ_INV_RT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHISQ_INV_RT --> SUM
    class SUM external
    CHISQ_INV_RT --> AVERAGE
    IF["IF<br/>Related Function"]
    CHISQ_INV_RT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CHISQ_INV_RT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    AVERAGE --> IF
    class IF external
    AVERAGE --> COUNT
    SUM["SUM<br/>External Function"]
    AVERAGE --> SUM
    class SUM external
    AVERAGE -.-> MEDIAN
    AVERAGE -.-> MODE
    IF["IF<br/>External Function"]
    PERCENTRANK_INC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PERCENTRANK_INC --> SUM
    class SUM external
    PERCENTRANK_INC --> AVERAGE
    IF["IF<br/>Related Function"]
    PERCENTRANK_INC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PERCENTRANK_INC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PERCENTRANK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PERCENTRANK --> SUM
    class SUM external
    PERCENTRANK --> AVERAGE
    IF["IF<br/>Related Function"]
    PERCENTRANK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PERCENTRANK -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    AVERAGEA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    AVERAGEA --> SUM
    class SUM external
    AVERAGEA --> AVERAGE
    IF["IF<br/>Related Function"]
    AVERAGEA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    AVERAGEA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUNTUNIQUE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUNTUNIQUE --> SUM
    class SUM external
    COUNTUNIQUE --> AVERAGE
    IF["IF<br/>Related Function"]
    COUNTUNIQUE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COUNTUNIQUE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PERMUTATIONA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PERMUTATIONA --> SUM
    class SUM external
    PERMUTATIONA --> AVERAGE
    IF["IF<br/>Related Function"]
    PERMUTATIONA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PERMUTATIONA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    T_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    T_DIST --> SUM
    class SUM external
    T_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    T_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    T_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GAMMALN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GAMMALN --> SUM
    class SUM external
    GAMMALN --> AVERAGE
    IF["IF<br/>Related Function"]
    GAMMALN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GAMMALN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    STDEV_P --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    STDEV_P --> SUM
    class SUM external
    STDEV_P --> AVERAGE
    IF["IF<br/>Related Function"]
    STDEV_P -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    STDEV_P -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    F_TEST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    F_TEST --> SUM
    class SUM external
    F_TEST --> AVERAGE
    IF["IF<br/>Related Function"]
    F_TEST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    F_TEST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FORECAST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FORECAST --> SUM
    class SUM external
    FORECAST --> AVERAGE
    IF["IF<br/>Related Function"]
    FORECAST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FORECAST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COVAR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COVAR --> SUM
    class SUM external
    COVAR --> AVERAGE
    IF["IF<br/>Related Function"]
    COVAR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COVAR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PEARSON --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PEARSON --> SUM
    class SUM external
    PEARSON --> AVERAGE
    IF["IF<br/>Related Function"]
    PEARSON -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PEARSON -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FISHER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FISHER --> SUM
    class SUM external
    FISHER --> AVERAGE
    IF["IF<br/>Related Function"]
    FISHER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FISHER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COMBINA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COMBINA --> SUM
    class SUM external
    COMBINA --> AVERAGE
    IF["IF<br/>Related Function"]
    COMBINA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COMBINA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    INTERCEPT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    INTERCEPT --> SUM
    class SUM external
    INTERCEPT --> AVERAGE
    IF["IF<br/>Related Function"]
    INTERCEPT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    INTERCEPT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LOGNORM_INV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    LOGNORM_INV --> SUM
    class SUM external
    LOGNORM_INV --> AVERAGE
    IF["IF<br/>Related Function"]
    LOGNORM_INV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LOGNORM_INV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SKEW --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SKEW --> SUM
    class SUM external
    SKEW --> AVERAGE
    IF["IF<br/>Related Function"]
    SKEW -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SKEW -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    Z_TEST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    Z_TEST --> SUM
    class SUM external
    Z_TEST --> AVERAGE
    IF["IF<br/>Related Function"]
    Z_TEST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    Z_TEST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    STDEV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    STDEV --> SUM
    class SUM external
    STDEV --> AVERAGE
    IF["IF<br/>Related Function"]
    STDEV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    STDEV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PROB --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PROB --> SUM
    class SUM external
    PROB --> AVERAGE
    IF["IF<br/>Related Function"]
    PROB -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PROB -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FREQUENCY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FREQUENCY --> SUM
    class SUM external
    FREQUENCY --> AVERAGE
    IF["IF<br/>Related Function"]
    FREQUENCY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FREQUENCY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PERCENTILE_EXC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PERCENTILE_EXC --> SUM
    class SUM external
    PERCENTILE_EXC --> AVERAGE
    IF["IF<br/>Related Function"]
    PERCENTILE_EXC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PERCENTILE_EXC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COUNTIFS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COUNTIFS --> SUM
    class SUM external
    COUNTIFS --> COUNT
    IF["IF<br/>Related Function"]
    COUNTIFS -.-> IF
    class IF external
    SUMIF["SUMIF<br/>Related Function"]
    COUNTIFS -.-> SUMIF
    class SUMIF external
    IF["IF<br/>External Function"]
    HYPGEOM_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HYPGEOM_DIST --> SUM
    class SUM external
    HYPGEOM_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    HYPGEOM_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    HYPGEOM_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    F_INV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    F_INV --> SUM
    class SUM external
    F_INV --> AVERAGE
    IF["IF<br/>Related Function"]
    F_INV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    F_INV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    NORM_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    NORM_DIST --> SUM
    class SUM external
    NORM_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    NORM_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    NORM_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PERCENTILE_INC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PERCENTILE_INC --> SUM
    class SUM external
    PERCENTILE_INC --> AVERAGE
    IF["IF<br/>Related Function"]
    PERCENTILE_INC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PERCENTILE_INC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    AVERAGEIFS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    AVERAGEIFS --> SUM
    class SUM external
    AVERAGEIFS --> COUNT
    IF["IF<br/>Related Function"]
    AVERAGEIFS -.-> IF
    class IF external
    SUMIF["SUMIF<br/>Related Function"]
    AVERAGEIFS -.-> SUMIF
    class SUMIF external
    IF["IF<br/>External Function"]
    F_DIST_RT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    F_DIST_RT --> SUM
    class SUM external
    F_DIST_RT --> AVERAGE
    IF["IF<br/>Related Function"]
    F_DIST_RT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    F_DIST_RT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GAMMA_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GAMMA_DIST --> SUM
    class SUM external
    GAMMA_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    GAMMA_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GAMMA_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BINOM_DIST_RANGE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BINOM_DIST_RANGE --> SUM
    class SUM external
    BINOM_DIST_RANGE --> AVERAGE
    IF["IF<br/>Related Function"]
    BINOM_DIST_RANGE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BINOM_DIST_RANGE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CHISQ_DIST_RT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHISQ_DIST_RT --> SUM
    class SUM external
    CHISQ_DIST_RT --> AVERAGE
    IF["IF<br/>Related Function"]
    CHISQ_DIST_RT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CHISQ_DIST_RT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MINA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MINA --> SUM
    class SUM external
    MINA --> AVERAGE
    IF["IF<br/>Related Function"]
    MINA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    MINA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MAX --> IF
    class IF external
    INDEX["INDEX<br/>External Function"]
    MAX --> INDEX
    class INDEX external
    MATCH["MATCH<br/>External Function"]
    MAX --> MATCH
    class MATCH external
    MAX -.-> MIN
    MAX -.-> LARGE
    IF["IF<br/>External Function"]
    VAR_S --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VAR_S --> SUM
    class SUM external
    VAR_S --> AVERAGE
    IF["IF<br/>Related Function"]
    VAR_S -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    VAR_S -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GROWTH --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GROWTH --> SUM
    class SUM external
    GROWTH --> AVERAGE
    IF["IF<br/>Related Function"]
    GROWTH -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GROWTH -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BINOM_INV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BINOM_INV --> SUM
    class SUM external
    BINOM_INV --> AVERAGE
    IF["IF<br/>Related Function"]
    BINOM_INV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BINOM_INV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CHISQ_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHISQ_DIST --> SUM
    class SUM external
    CHISQ_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    CHISQ_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CHISQ_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LOGNORM_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    LOGNORM_DIST --> SUM
    class SUM external
    LOGNORM_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    LOGNORM_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LOGNORM_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GAMMA_INV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GAMMA_INV --> SUM
    class SUM external
    GAMMA_INV --> AVERAGE
    IF["IF<br/>Related Function"]
    GAMMA_INV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GAMMA_INV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PERMUT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PERMUT --> SUM
    class SUM external
    PERMUT --> AVERAGE
    IF["IF<br/>Related Function"]
    PERMUT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    PERMUT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LOGEST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    LOGEST --> SUM
    class SUM external
    LOGEST --> AVERAGE
    IF["IF<br/>Related Function"]
    LOGEST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    LOGEST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MINIFS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MINIFS --> SUM
    class SUM external
    MINIFS --> COUNT
    IF["IF<br/>Related Function"]
    MINIFS -.-> IF
    class IF external
    SUMIF["SUMIF<br/>Related Function"]
    MINIFS -.-> SUMIF
    class SUMIF external
    IF["IF<br/>External Function"]
    POISSON_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    POISSON_DIST --> SUM
    class SUM external
    POISSON_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    POISSON_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    POISSON_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BETA_INV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BETA_INV --> SUM
    class SUM external
    BETA_INV --> AVERAGE
    IF["IF<br/>Related Function"]
    BETA_INV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BETA_INV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COVARIANCE_P --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COVARIANCE_P --> SUM
    class SUM external
    COVARIANCE_P --> AVERAGE
    IF["IF<br/>Related Function"]
    COVARIANCE_P -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COVARIANCE_P -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HARMEAN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HARMEAN --> SUM
    class SUM external
    HARMEAN --> AVERAGE
    IF["IF<br/>Related Function"]
    HARMEAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    HARMEAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    STDEVPA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    STDEVPA --> SUM
    class SUM external
    STDEVPA --> AVERAGE
    IF["IF<br/>Related Function"]
    STDEVPA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    STDEVPA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TREND --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TREND --> SUM
    class SUM external
    TREND --> AVERAGE
    IF["IF<br/>Related Function"]
    TREND -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TREND -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    VARA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VARA --> SUM
    class SUM external
    VARA --> AVERAGE
    IF["IF<br/>Related Function"]
    VARA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    VARA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BETA_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BETA_DIST --> SUM
    class SUM external
    BETA_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    BETA_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    BETA_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GAUSS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GAUSS --> SUM
    class SUM external
    GAUSS --> AVERAGE
    IF["IF<br/>Related Function"]
    GAUSS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GAUSS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SLOPE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SLOPE --> SUM
    class SUM external
    SLOPE --> AVERAGE
    IF["IF<br/>Related Function"]
    SLOPE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SLOPE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    COMBIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    COMBIN --> SUM
    class SUM external
    COMBIN --> AVERAGE
    IF["IF<br/>Related Function"]
    COMBIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    COMBIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    NEGBINOM_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    NEGBINOM_DIST --> SUM
    class SUM external
    NEGBINOM_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    NEGBINOM_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    NEGBINOM_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    EXPON_DIST --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    EXPON_DIST --> SUM
    class SUM external
    EXPON_DIST --> AVERAGE
    IF["IF<br/>Related Function"]
    EXPON_DIST -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    EXPON_DIST -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FORECAST_ETS_CONFINT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FORECAST_ETS_CONFINT --> SUM
    class SUM external
    FORECAST_ETS_CONFINT --> AVERAGE
    IF["IF<br/>Related Function"]
    FORECAST_ETS_CONFINT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FORECAST_ETS_CONFINT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RANK_AVG --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    RANK_AVG --> SUM
    class SUM external
    RANK_AVG --> AVERAGE
    IF["IF<br/>Related Function"]
    RANK_AVG -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    RANK_AVG -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    STDEVA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    STDEVA --> SUM
    class SUM external
    STDEVA --> AVERAGE
    IF["IF<br/>Related Function"]
    STDEVA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    STDEVA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    T_INV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    T_INV --> SUM
    class SUM external
    T_INV --> AVERAGE
    IF["IF<br/>Related Function"]
    T_INV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    T_INV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    QUARTILE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    QUARTILE --> SUM
    class SUM external
    QUARTILE --> AVERAGE
    IF["IF<br/>Related Function"]
    QUARTILE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    QUARTILE -.-> IFERROR
    class IFERROR external
    class COVARIANCE_S Statistical
    class MEDIAN Statistical
    class T_DIST_RT Statistical
    class MODE_MULT Statistical
    class SMALL Statistical
    class T_DIST_2T Statistical
    class NORM_INV Statistical
    class WEIBULL_DIST Statistical
    class GEOMEAN Statistical
    class LINEST Statistical
    class LARGE Statistical
    class F_DIST Statistical
    class STEYX Statistical
    class TRIMMEAN Statistical
    class T_TEST Statistical
    class COUNTA Statistical
    class MAXIFS Statistical
    class CONFIDENCE_T Statistical
    class RANK_EQ Statistical
    class VAR Statistical
    class MIN Statistical
    class CONFIDENCE_NORM Statistical
    class MODE Statistical
    class STANDARDIZE Statistical
    class FORECAST_LINEAR Statistical
    class FORECAST_ETS Statistical
    class CHISQ_INV Statistical
    class VARPA Statistical
    class NORM_S_INV Statistical
    class COUNTIF Statistical
    class GAMMALN_PRECISE Statistical
    class FORECAST_ETS_STAT Statistical
    class BINOM_DIST Statistical
    class COUNTUNIQUEIFS Statistical
    class MAXA Statistical
    class F_INV_RT Statistical
    class KURT Statistical
    class SKEW_P Statistical
    class CORREL Statistical
    class DEVSQ Statistical
    class VARP Statistical
    class FORECAST_ETS_SEASONALITY Statistical
    class COUNTBLANK Statistical
    class CHISQ_TEST Statistical
    class QUARTILE_INC Statistical
    class RANK Statistical
    class PERCENTILE Statistical
    class PHI Statistical
    class STDEVP Statistical
    class T_INV_2T Statistical
    class QUARTILE_EXC Statistical
    class GAMMA Statistical
    class COUNT Statistical
    class VAR_P Statistical
    class PERCENTRANK_EXC Statistical
    class AVERAGEIF Statistical
    class FISHERINV Statistical
    class NORM_S_DIST Statistical
    class RSQ Statistical
    class MODE_SNGL Statistical
    class STDEV_S Statistical
    class AVEDEV Statistical
    class CHISQ_INV_RT Statistical
    class AVERAGE Statistical
    class PERCENTRANK_INC Statistical
    class PERCENTRANK Statistical
    class AVERAGEA Statistical
    class COUNTUNIQUE Statistical
    class PERMUTATIONA Statistical
    class T_DIST Statistical
    class GAMMALN Statistical
    class STDEV_P Statistical
    class F_TEST Statistical
    class FORECAST Statistical
    class COVAR Statistical
    class PEARSON Statistical
    class FISHER Statistical
    class COMBINA Statistical
    class INTERCEPT Statistical
    class LOGNORM_INV Statistical
    class SKEW Statistical
    class Z_TEST Statistical
    class STDEV Statistical
    class PROB Statistical
    class FREQUENCY Statistical
    class PERCENTILE_EXC Statistical
    class COUNTIFS Statistical
    class HYPGEOM_DIST Statistical
    class F_INV Statistical
    class NORM_DIST Statistical
    class PERCENTILE_INC Statistical
    class AVERAGEIFS Statistical
    class F_DIST_RT Statistical
    class GAMMA_DIST Statistical
    class BINOM_DIST_RANGE Statistical
    class CHISQ_DIST_RT Statistical
    class MINA Statistical
    class MAX Statistical
    class VAR_S Statistical
    class GROWTH Statistical
    class BINOM_INV Statistical
    class CHISQ_DIST Statistical
    class LOGNORM_DIST Statistical
    class GAMMA_INV Statistical
    class PERMUT Statistical
    class LOGEST Statistical
    class MINIFS Statistical
    class POISSON_DIST Statistical
    class BETA_INV Statistical
    class COVARIANCE_P Statistical
    class HARMEAN Statistical
    class STDEVPA Statistical
    class TREND Statistical
    class VARA Statistical
    class BETA_DIST Statistical
    class GAUSS Statistical
    class SLOPE Statistical
    class COMBIN Statistical
    class NEGBINOM_DIST Statistical
    class EXPON_DIST Statistical
    class FORECAST_ETS_CONFINT Statistical
    class RANK_AVG Statistical
    class STDEVA Statistical
    class T_INV Statistical
    class QUARTILE Statistical
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```

## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions In This Category: 151
