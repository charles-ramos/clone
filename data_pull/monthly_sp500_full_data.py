# Import Packages
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Define a mapping dictionary to handle discrepancies
symbol_mapping = {
    'BRK.B': 'BRK-B',
    'BF.B': 'BF-B',
}

# Import the DataFrame from sp500_symbols pickle file
sp500_symbols = pd.read_pickle('./pickle/sp500_symbols.pkl')

# Calculate the start and end dates for the last month
end_date = datetime.now()  # Current date
start_date = end_date - timedelta(days=30)  # Subtract 30 days to get the start date for last week

# Format the dates as strings in 'YYYY-MM-DD' format
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

# Create an empty DataFrame to store the historical data
monthly_sp500_data = pd.DataFrame()

# Loop through each symbol in the S&P 500 list and fetch historical data
for symbol in sp500_symbols:
    # Check if the symbol needs to be converted using the mapping dictionary
    if symbol in symbol_mapping:
        symbol_to_fetch = symbol_mapping[symbol]
    else:
        symbol_to_fetch = symbol

    try:
        stock_data = yf.download(symbol_to_fetch, start=start_date_str, end=end_date_str)
        if not stock_data.empty:
            stock_data = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].rename(
                columns={'Open': f'{symbol}_Open', 'High': f'{symbol}_High', 'Low': f'{symbol}_Low',
                         'Close': f'{symbol}_Close', 'Volume': f'{symbol}_Volume'})
            monthly_sp500_data = pd.concat([monthly_sp500_data, stock_data], axis=1)
    except Exception as e:
        print(f"Error fetching data for {symbol_to_fetch}: {e}")

# Pickle the DataFrame
monthly_sp500_data.to_pickle('./pickle/monthly_sp500_full_data.pkl')

# Save DataFrame to a CSV file with proper headers for each stock
file_name = f"sp500_monthly_data_{start_date_str}_{end_date_str}.csv"

# Define the directory path where you want to save the file

directory = './data'

# Specify the file path within the directory
file_name = os.path.join(directory, f"sp500_monthly_full_data_{start_date_str}_{end_date_str}.csv")

# Save DataFrame to a CSV file with proper headers for each stock
with open(file_name, 'w') as file:
    file.write(f"Monthly data from {start_date_str} to {end_date_str}\n")
    monthly_sp500_data.to_csv(file, header=True)