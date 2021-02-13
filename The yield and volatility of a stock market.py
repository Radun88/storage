import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

assets = []
print('Программа запущена,\n если выдаёт ошибку ,проверьте тикер бумаги на YAHOO finance.')
print()
print('Введите количество тикеров которые будете выводить:')
ticker = int(input())
print('Введите тикер акций,несколько тикеров вводится через Enter:')
for i in range(0,ticker):
    assets.append(str(input()))
    
pf_data = pd.DataFrame()
print('Введите дату учёта ценной бумаги от даты , в формате: 2012-01-01')
data_start =str(input()) #2012-1-1

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source='yahoo', start=data_start)['Adj Close']

log_returns = np.log(pf_data / pf_data.shift(1))


#средняя доходность бумаги
for a in assets:
    income = log_returns[a].mean() * 250
    print('|{: <7} | {: >7.2%} |'.format(a, income),'Cредняя доходность бумаги')


#средняя волатильность бумаги
for a in assets:
    volatility = log_returns[a].std() * 250**0.5
    print('|{: <7} | {: >7.2%}|'.format(a, volatility),'Cредняя волатильность бумаги')


# Plot all the close prices
((pf_data.pct_change()+1).cumprod()).plot(figsize=(7, 5))

# Show the legend
plt.legend()

# Define the label for the title of the figure
plt.title("Adjusted Close Price", fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()
