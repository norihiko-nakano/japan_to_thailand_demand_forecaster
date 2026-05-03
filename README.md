# Japan-to-Thailand Travel Demand Direction Forecaster

**Inspired by Moo Deng 🦛**

This portfolio is an MVP for a Japanese-language travel recommendation system.  
The broader idea is to help a travel platform decide which destinations or tours should be promoted to Japanese users.

For the MVP, the scope is intentionally small:

> Predict whether Japanese travel demand to Thailand will increase or decrease next month.

Public data does not reliably show where Japanese travelers go inside Thailand by city or attraction.  
So this MVP starts with country-level demand. If internal search, click, booking, or destination-level data were available, the same framework could be extended to predict demand for Bangkok, Phuket, Chiang Mai, Pattaya, Chonburi, Khao Kheow Open Zoo, and other destinations.

---

## 1. Motivation

Moo Deng, the baby pygmy hippo at Khao Kheow Open Zoo, showed how quickly travel-related attention can turn into real-world tourism demand.

This project explores the first step toward a system that could detect demand signals and recommend what to promote on Japanese-language travel pages.

Example future use case:

> If Moo Deng becomes popular among Japanese users, the system could detect rising demand signals and recommend promoting Khao Kheow Open Zoo tours, Chonburi hotels, Pattaya day trips, and transport options from Bangkok.

---

## 2. Business Problem

Japanese travelers are affected by seasonal patterns such as:

- Golden Week
- Obon
- New Year holidays
- Three-day weekends
- Exchange-rate movements
- Recovery or disruption after external shocks

A travel platform can use demand forecasts to decide:

- whether to promote Thailand next month
- when to increase visibility on Japanese-language pages
- when to prepare Thailand campaign pages
- when to recommend Bangkok, Phuket, Chiang Mai, Pattaya, or future destination-level tours

---

## 3. MVP Scope

### Target

Two binary classification targets are proposed:

```text
target_yoy_up = 1 if next month's visitors > same month last year
target_mom_up = 1 if next month's visitors > current month's visitors
```

### Main MVP Question

```text
Will Japanese travel demand to Thailand increase next month?
```

This is more useful than predicting the exact number because travel platforms often need a decision:

```text
Promote Thailand more / Keep current exposure / Reduce exposure
```

---

## 4. Data

### MVP Data

This repository contains a small synthetic sample dataset:

```text
data/sample_jttd_monthly.csv
```

It is only for demonstrating the pipeline.

For the real project, replace it with official monthly data such as:

- Japanese visitors to Thailand by month
- Japanese outbound travel statistics
- Thailand inbound tourism statistics
- exchange-rate data
- Japanese public holiday calendar

### Why Synthetic Data Is Included

The sample data lets the code run immediately.  
It should not be used as evidence about real travel demand.

---

## 5. Features

The MVP uses features such as:

```text
visitors_lag_1
visitors_lag_2
visitors_lag_3
visitors_lag_12
rolling_mean_3m
rolling_mean_6m
mom_growth_lag_1
yoy_growth_lag_1
month_number
public_holiday_count_japan
is_golden_week_month
is_obon_month
is_new_year_travel_month
jpy_thb_exchange_rate_proxy
shock_flag
```

---

## 6. Shock Handling

External shocks such as COVID-19 can distort normal travel demand.

This project does not blindly delete unusual data.  
Instead, it marks shock periods and allows two modeling approaches:

1. **Include shock_flag as a feature**
2. **Exclude or down-weight shock months when modeling normal demand**

This makes the model more transparent and easier to explain.

---

## 7. Model Plan

### Baseline

- Last year same month direction
- Moving-average direction

### MVP Models

- Logistic Regression
- Random Forest Classifier

### Metrics

- Accuracy
- Precision
- Recall
- F1 score
- Direction accuracy
- Confusion matrix

For business use, direction accuracy is especially important:

```text
Can the system correctly detect whether demand is rising or falling?
```

---

## 8. Travel Platform Recommendation Logic

Example output:

```text
Prediction: Japanese demand to Thailand is likely to increase next month.
Confidence: 72%

Recommended action:
- Increase Thailand exposure on Japanese-language travel pages
- Promote Bangkok and Phuket packages
- Prepare content for Golden Week / Obon / New Year travel intent
- Monitor destination-level demand signals for future campaign refinement
```

---

## 9. Future Work

The MVP intentionally excludes TV, X, and news data to avoid data-collection complexity.

Future expansion:

- Add Japanese news buzz features
- Add X/social buzz signals
- Add TV exposure metadata
- Add Google Trends
- Add Agoda internal search / click / booking data
- Extend from country-level Thailand demand to destination-level demand
- Predict tours or attractions such as Khao Kheow Open Zoo, Pattaya day trips, Phuket island tours, or Chiang Mai seasonal trips

---

## 10. Portfolio Positioning

This is not just a machine-learning exercise.

It demonstrates:

- business problem framing
- Japanese market understanding
- tourism demand analysis
- practical handling of public data limitations
- shock-period treatment
- MVP design for future internal-data expansion

---

## 11. How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the modeling script:

```bash
python src/model.py
```

---

## 12. Suggested CV Description

> Built a Japan-to-Thailand travel demand forecasting MVP inspired by Moo Deng’s viral impact on tourism. The model predicts whether next-month Japanese travel demand to Thailand will increase or decrease using lag features, seasonality, Japanese holiday indicators, exchange-rate proxy features, and shock-period handling. The project is positioned as a foundation for Japanese-language travel page recommendations.
