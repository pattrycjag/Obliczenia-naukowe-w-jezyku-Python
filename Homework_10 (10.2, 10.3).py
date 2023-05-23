import pandas as pd

print("Ex.10.2 \n")
days = ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04', '2023-05-05']
temperatures = [25.6, 27.8, 26.5, 24.9, 28.1]
exchange_rates = [1.23, 1.25, 1.21, 1.18, 1.19]

series_data = pd.Series(temperatures, index=days)
series_exchange_rates= pd.Series(exchange_rates, index=days)

print("Temperature:")
print(series_data)
print("\nExchange rates:")
print(series_exchange_rates)

print("Ex.10.3 \n")

pt = [("Hydrogen", "H", 1),
      ("Helium", "He", 4),
      ("Lithium", "Li", 7),
      ("Beryllium", "Be", 9),
      ("Boron", "B", 11),
      ("Carbon", "C", 12),
      ("Nitrogen", "N", 14),
      ("Oxygen", "O", 16),
      ("Fluorine", "F", 19),
      ("Neon", "Ne", 20)]

table_of_elements = pd.DataFrame(pt, columns=['Name', 'Symbol', 'Weight'], index=range(1, 11))

print(table_of_elements)
