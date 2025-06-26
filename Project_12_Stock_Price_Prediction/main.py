import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

stock_symbol="AAPL"
forecast_days =200

data=yf.download(stock_symbol,start="2015-01-01",end=None)
data=data[['Close']].dropna()

data.reset_index(inplace=True)
data['Days']=(data['Date']-data['Date'].min()).dt.days

X=data[['Days']]
y=data['Close']

model=LinearRegression()
model.fit(X,y)

last_day=data['Days'].max()
future_days = np.arange(last_day+1,last_day+forecast_days+1).reshape(-1,1)
future_preds = model.predict(future_days)

plt.figure(figsize=(12,6))
plt.plot(data['Date'],y,label='Historical Prices',color='blue')

future_dates =pd.date_range(start=data['Date'].max()+pd.Timedelta(days=1),periods=forecast_days)
plt.plot(future_dates,future_preds, label='Label', color='red', linestyle='--')



plt.title(f"{stock_symbol} Stock Price Prediction ({forecast_days} days ahead)")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
