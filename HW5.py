import numpy as np
import pandas as pd
import pandas_datareader.data as web

all_data = {ticker: web.get_data_yahoo(ticker)
            for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG', 'TSLA']}
print('1- Google closing price in 2018: $%.2f' %
       all_data['GOOG'].Close['2018-12-31'])
print('2- Apple trading volume in Oct 2020: %d' %
       all_data['AAPL'].Volume['2020-10'].sum())
print('3- Number of days Microsoft stock price opened higher than $150:',
       (all_data['MSFT'].Open['2019'] > 150).sum())

price = pd.DataFrame({ticker: data['Adj Close']
                     for ticker, data in all_data.items()})
returns = price.pct_change()
print('4- Tesla has the highest correlation with:',
      returns.corr().loc['TSLA'].sort_values()[0:4].idxmax())
IBM = all_data['IBM']
IBM['Amount'] = IBM.Volume * IBM['Adj Close']
print('5- IBM\'s trading amount in Jan 2020: $%.2f' %
 IBM.Amount['2020-1'].sum())