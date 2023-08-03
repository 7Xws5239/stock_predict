import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
from talib import RSI, SMA  # Technical Analysis Library

ts.set_token('6b8c79c89a4ca893322ae0288304304d31a82041fdb23260ff78fef0')

stock_code = "600629.SH"

data = ts.pro_bar(ts_code=stock_code, adj='qfq', start_date='20080101', end_date='20230101')

# Convert 'trade_date' to datetime
data['trade_date'] = pd.to_datetime(data['trade_date'])

# Calculate technical indicators
data['MA'] = SMA(data['close'], timeperiod=20)  # 20-day Moving average
data['RSI'] = RSI(data['close'], timeperiod=14)  # 14-day Relative Strength Index

# Plotting
fig, ax1 = plt.subplots()

# Plot closing price and moving average
ax1.plot(data['trade_date'], data['close'], label='Close')
ax1.plot(data['trade_date'], data['MA'], label='MA')
ax1.set_ylabel('Price')
ax1.set_title(f"{stock_code} Stock Price and Indicators")
ax1.grid(True)

# Plot RSI
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(data['trade_date'], data['RSI'], label='RSI', color='tab:orange')
ax2.set_ylabel('RSI')

# Show the legend
fig.legend(loc="upper left")

plt.show()
