# Data Exploration Notes – Day 1

## Dataset Overview
- Dataset: Individual Household Electric Power Consumption
- Time granularity: 1 minute
- Total rows: ~2.07 million
- Data span: Multiple years

## Target Variable
- Primary target for forecasting: `Global_active_power`
- Unit: kilowatts (kW)
- Represents total household active power consumption

## Time Index
- Date and Time are provided as separate columns
- Will be combined into a single datetime index during preprocessing
- Datetime column will be used as the primary index for resampling and modeling

## Missing Values
Missing values are present and represented as '?' in the raw dataset.

| Column | Missing Count |
|------|--------------|
| Global_active_power | 25,979 |
| Global_reactive_power | 25,979 |
| Voltage | 25,979 |
| Global_intensity | 25,979 |
| Sub_metering_1 | 25,979 |
| Sub_metering_2 | 25,979 |
| Sub_metering_3 | 25,979 |

- Missing values are consistent across all measurement columns
- Strategy for handling missing values will be decided after resampling (likely forward fill or interpolation)

## Initial Observations
- Power consumption is expected to show daily and weekly seasonality
- Occasional spikes are likely due to high-load appliances (e.g., heating, cooking)
- No obvious data corruption observed at this stage (to be confirmed via visualization)

## Next Steps
- Combine Date and Time into a datetime index
- Resample data to hourly granularity
- Visualize trends and spikes
- Engineer time-based features