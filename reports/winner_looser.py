import pandas as pd

# Import the DataFrame
<<<<<<< HEAD
sp500_data  = pd.read_pickle('/Users/lilygoncharov/Documents/Z/code/AI-Trading/data_pull/monthly_sp500_full_data.pkl')
=======
sp500_data  = pd.read_pickle('./pickle/weekly_sp500_data.pkl')
>>>>>>> dd1c1d937372bbf96b4da3050d55b6a8eee5c6b6

### Winner ###
# Calculate the percentage change for each stock over the week
percentage_change = (sp500_data.iloc[-1] - sp500_data.iloc[0]) / sp500_data.iloc[0] * 100

# Find the stock with the largest percentage change increase
max_increase_stock = percentage_change.idxmax()
max_increase_percentage = percentage_change[max_increase_stock]

print(f"The stock with the biggest % change increase during the period: {max_increase_stock}")
print(f"Percentage Change: {max_increase_percentage:.2f}%")

### Looser ###

# Calculate the percentage change for each stock over the week
percentage_change = (sp500_data.iloc[-1] - sp500_data.iloc[0]) / sp500_data.iloc[0] * 100

# Find the stock with the largest percentage change decrease (biggest loser)
min_decrease_stock = percentage_change.idxmin()
min_decrease_percentage = percentage_change[min_decrease_stock]

print(f"The stock with the biggest % change decrease during the week: {min_decrease_stock}")
print(f"Percentage Change: {min_decrease_percentage:.2f}%")