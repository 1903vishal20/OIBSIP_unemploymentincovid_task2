# Unemployment Rate Analysis During COVID-19

## Overview
This project analyzes the unemployment rate during the COVID-19 pandemic using time series analysis. The objective is to explore trends, perform statistical analysis, and forecast future unemployment rates based on historical data.

## Dataset
The dataset used for this analysis contains the following columns:
- **Region**: The geographical area for which the data is reported.
- **Date**: The date of the recorded unemployment data (format: dd-mm-yyyy).
- **Frequency**: The frequency of the recorded data (e.g., Monthly).
- **Estimated Unemployment Rate (%)**: The estimated unemployment rate as a percentage.
- **Estimated Employed**: The estimated number of employed individuals.
- **Estimated Labour Participation Rate (%)**: The estimated labor participation rate as a percentage.
- **Area**: Indicates whether the area is urban or rural.

## Requirements
- Python 3.7 or higher
- Pandas
- Matplotlib
- Statsmodels
- SciPy
- Seaborn

## Installation
You can install the required libraries using pip:
```bash
pip install pandas matplotlib statsmodels scipy seaborn
```

## Usage
1. Clone the repository or download the script file.
2. Place your dataset in the same directory as the script or adjust the path in the script accordingly.
3. Run the script using Python:
```bash
python covid.py
```

## Outputs
- A time series plot of the unemployment rate over time.
- Average unemployment rates before and during COVID-19.
- Correlation analysis with COVID-19 cases (if applicable).
- T-test for comparing average unemployment rates.
- Forecast of the unemployment rate for the next 12 months using ARIMA.
- Heatmap for regional unemployment rates.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
