import pandas as pd

days = ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04', '2023-05-05']
temperatures = [25.6, 27.8, 26.5, 24.9, 28.1]
exchange_rates = [1.23, 1.25, 1.21, 1.18, 1.19]

series_data = pd.Series(temperatures, index=days)
series_exchange_rates= pd.Series(exchange_rates, index=days)

print("Temperature:")
print(series_data)
print("\nExchange rates:")
print(series_exchange_rates)
