# Data Dictionary

| Column | Description |
|---|---|
| month | Month in YYYY-MM format |
| japanese_visitors_to_thailand | Monthly Japanese visitors to Thailand. Synthetic in sample data. Replace with official data. |
| jpy_thb_exchange_rate_proxy | Sample exchange-rate proxy. Replace with real JPY/THB data. |
| public_holiday_count_japan | Number of Japanese public holidays in the month |
| is_golden_week_month | 1 if the month includes Golden Week travel demand |
| is_obon_month | 1 if the month includes Obon travel demand |
| is_new_year_travel_month | 1 if the month is related to New Year travel demand |
| shock_flag | 1 if the month is treated as an external shock period |
| large_drop_flag | 1 if large YoY or MoM drop is detected |
| target_yoy_up | 1 if next month is higher than same month last year |
| target_mom_up | 1 if next month is higher than current month |
