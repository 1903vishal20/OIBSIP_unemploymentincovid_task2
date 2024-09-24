import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from scipy import stats
import seaborn as sns

# Load dataset
data = pd.read_csv('unemployment_data.csv')

# Display the first few rows and column names of the dataset
print("First few rows of the dataset:")
print(data.head())
print("\nColumn names:")
print(data.columns)

# Strip whitespace from column names
data.columns = data.columns.str.strip()

# Check the column names after stripping
print("\nColumn names after stripping whitespace:")
print(data.columns)

# Convert the date column to datetime format; check the exact name first
date_column_name = 'Date'  # Ensure this matches your dataset

# Verify if the date column exists
if date_column_name not in data.columns:
    print(f"Column '{date_column_name}' not found. Available columns: {data.columns.tolist()}")
else:
    # Convert the date column to datetime with dayfirst=True
    data[date_column_name] = pd.to_datetime(data[date_column_name], dayfirst=True)

    # Set the date as the index
    data.set_index(date_column_name, inplace=True)

    # EDA: Plotting the unemployment rate over time
    plt.figure(figsize=(12, 6))
    plt.plot(data['Estimated Unemployment Rate (%)'], label='Unemployment Rate', color='blue')  # Adjust for actual column name
    plt.title('Unemployment Rate Over Time')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.legend()
    plt.grid()
    plt.show()

    # Comparative Analysis: Average unemployment rates pre-COVID vs during COVID
    pre_covid = data[data.index < '2020-03-01']
    covid_period = data[data.index >= '2020-03-01']

    avg_pre_covid = pre_covid['Estimated Unemployment Rate (%)'].mean()
    avg_covid = covid_period['Estimated Unemployment Rate (%)'].mean()

    print(f'Average Unemployment Rate Pre-COVID: {avg_pre_covid:.2f}%')
    print(f'Average Unemployment Rate During COVID: {avg_covid:.2f}%')

    # Correlation Analysis with COVID cases (if applicable)
    if 'COVID_Cases' in data.columns:
        correlation = data[['Estimated Unemployment Rate (%)', 'COVID_Cases']].corr()
        print('Correlation between Unemployment Rate and COVID Cases:')
        print(correlation)

    # Hypothesis Testing: T-test for average unemployment rates
    t_stat, p_value = stats.ttest_ind(pre_covid['Estimated Unemployment Rate (%)'], covid_period['Estimated Unemployment Rate (%)'])
    print(f'T-test statistic: {t_stat}, P-value: {p_value}')

    # Time Series Forecasting: ARIMA model
    model = ARIMA(data['Estimated Unemployment Rate (%)'], order=(1, 1, 1))
    model_fit = model.fit()

    # Forecasting the next 12 months
    forecast = model_fit.forecast(steps=12)
    plt.figure(figsize=(12, 6))
    plt.plot(data['Estimated Unemployment Rate (%)'], label='Historical Unemployment Rate', color='blue')
    plt.plot(forecast.index, forecast, label='Forecast', color='orange')
    plt.title('Unemployment Rate Forecast')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.legend()
    plt.grid()
    plt.show()

    # Heatmap for regional analysis if applicable
    if 'Region' in data.columns:
        heatmap_data = data.pivot_table(values='Estimated Unemployment Rate (%)', index='Region', columns=data.index.month)
        plt.figure(figsize=(12, 8))
        sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt=".2f")
        plt.title('Unemployment Rate by Region Over Time')
        plt.xlabel('Month')
        plt.ylabel('Region')
        plt.show()
