# PWC Bank Impairments Analysis Application

## Overview
This Streamlit application analyzes bank credit impairments data alongside economic indicators to provide insights into the banking sector's credit risk patterns. The application offers interactive visualizations, statistical analysis, and regression modeling to understand the relationships between economic factors and bank impairments.
Find the repository at git@github.com:ChristoGH/pwc.git

## Features

### 1. Data Processing
- Processes bank impairment data from CSV files in the `pwc_data` directory
- Handles economic indicators data with support for multiple time periods
- Performs data cleaning and currency formatting
- Calculates percentage changes for both impairments and economic indicators

### 2. Interactive Visualizations
- **Time Series Analysis**
  - Line and bar plot options for viewing impairments over time
  - Secondary y-axis for total banking sector values
  - Interactive legends and hover information

- **Normalized Analysis**
  - Base 100 normalization for comparing relative changes
  - Customizable visualization options
  - Reference line at 100 for easy comparison

### 3. Statistical Analysis
- **Summary Statistics**
  - Mean, minimum, maximum, and total values by bank
  - Formatted currency display with proper notation

- **Changes Analysis**
  - Percentage changes in impairments by bank
  - Economic indicator trends
  - Correlation matrix with heatmap visualization

### 4. Regression Analysis
- **Individual Bank Analysis**
  - OLS regression for each bank with sufficient data points (≥3)
  - Variance Inflation Factor (VIF) analysis
  - Actual vs. Predicted plots
  - Residual analysis
  - Key metrics (R-squared, Adjusted R-squared, F-statistic)
  - Significant coefficients identification (p < 0.05)

- **Total Banking Sector Analysis**
  - Aggregate sector regression analysis
  - VIF analysis for sector-wide indicators
  - Comprehensive regression diagnostics

## Requirements
- Python 3.x
- Required packages:
  ```
  streamlit
  pandas
  plotly
  statsmodels
  numpy
  ```

## Data Requirements

### Bank Impairments Data
- CSV files in `pwc_data` directory
- Required format:
  - Date in first row, second column
  - Bank name in second row, second column
  - Item Number 194 for credit impairments
  - Values in thousands (automatically adjusted)

### Economic Indicators Data
- CSV file named `economic_indicators.csv`
- Required columns:
  - Indicator (including GDP Growth, Inflation, Repo Rate, Unemployment)
  - Date columns in format YYYY/MM/DD
  - Numeric values for each indicator

## Usage

1. **Data Preparation**
   - Place bank data files in `pwc_data` directory
   - Ensure `economic_indicators.csv` is present

2. **Running the Application**
   ```bash
   streamlit run pwc_app.py
   ```

3. **Using the Interface**
   - Click "Process new data..." to refresh data from files
   - Click "Retrieve data..." to load previously processed data
   - Use expanders to view different analyses
   - Switch between visualization types using the dropdown

## Data Flow
1. Data Loading and Processing
2. Time Series Visualization
3. Normalized Analysis
4. Statistical Summary
5. Changes Analysis
6. Regression Modeling

## Output Sections
1. Raw Data View
2. Economic Data View
3. Changes Analysis
4. Correlation Analysis
5. Time Series Visualizations
6. Normalized Analysis
7. Summary Statistics
8. Regression Analysis by Bank
9. Total Sector Analysis

## Notes
- Minimum 3 valid data points required for bank-specific regression analysis
- Automatic handling of missing values and infinities
- Currency values displayed in ZAR with proper formatting
- Interactive plots support zooming and hover information

## Error Handling
- Validates data point sufficiency
- Handles missing values in impairments data
- Manages infinite values in percentage calculations
- Provides warning messages for excluded banks
- Graceful error handling in regression analysis

## Best Practices
- Use consistent date formats
- Ensure economic indicators align with impairment dates
- Regular data updates for meaningful trend analysis
- Review warnings and error messages for data quality issues

## Limitations
- Maximum display of 50 correlation pairs
- Requires minimum 3 data points for regression
- Date alignment between economic and bank data is critical
- Memory usage increases with data volume

## Contributing
For modifications or improvements:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with detailed changes

