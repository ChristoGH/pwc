import pandas as pd
import re

def clean_percentage(value):
    """Clean percentage values and convert to decimal"""
    # Extract the first number with decimal point if present
    match = re.search(r'(\d+\.?\d*)', str(value))
    if match:
        # Convert percentage to decimal
        return float(match.group(1)) / 100
    return None

# Create the data as a list of lists
data = [
    ['Indicator', 'Jan 2023', 'Jan 2024', 'Jan 2025'],
    ['Repo Rate', '7.25%', '8.25%', '7.50%'],
    ['Inflation (CPI)', '6.9%', '5.3%', '3.2%'],
    ['Unemployment', '32.7% (Q4 2022)', '32.1% (Q4 2023)', '31.9% (Q4 2024)'],
    ['GDP Growth (prev. year)', '2.0% (2022)', '0.7% (2023)', '0.6% (2024)']
]

# Create DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# First, melt to clean the values
melted_df = df.melt(
    id_vars=['Indicator'],
    var_name='date',
    value_name='value'
)

# Clean the values
melted_df['value'] = melted_df['value'].apply(clean_percentage)

# Pivot back to wide format with dates as columns
result_df = melted_df.pivot(
    index='Indicator',
    columns='date',
    values='value'
)

# Sort the columns chronologically
result_df = result_df.reindex(sorted(result_df.columns, key=lambda x: pd.to_datetime(x, format='%b %Y')), axis=1)

# Save to CSV
result_df.to_csv('economic_indicators.csv')

# Display the transformed data
print("\nTransformed Data:")
print(result_df)
