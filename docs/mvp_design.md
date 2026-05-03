# MVP Design

## Portfolio Concept

A Japanese-language travel recommendation system that predicts which destinations or tours should be promoted.

## MVP

The MVP predicts whether Japanese travel demand to Thailand will increase or decrease next month.

## Why This Scope?

Destination-level data such as “how many Japanese travelers visited Bangkok, Phuket, Chiang Mai, Pattaya, or Khao Kheow Open Zoo” is not reliably available in public datasets.

Therefore, the first MVP uses country-level monthly Japanese visitors to Thailand.

## Target Variables

```text
target_yoy_up = 1 if next month’s visitors > same month last year
target_mom_up = 1 if next month’s visitors > current month
```

## Why Direction Classification?

Travel platforms often need to decide whether to increase, maintain, or reduce campaign exposure. A direction forecast is easier to use for campaign decisions than an exact visitor-count forecast.

## Shock Handling

Shock periods such as COVID-19 are marked with a shock flag. The project can compare models with shock months included, excluded, or down-weighted.
