import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd  # Import pandas

ts.set_token('6b8c79c89a4ca893322ae0288304304d31a82041fdb23260ff78fef0')

stock_code = "600629.SH"

data = ts.pro_bar(ts_code=stock_code, adj='qfq', start_date='20230701', end_date='20230803')

# Convert 'trade_date' to datetime
data['trade_date'] = pd.to_datetime(data['trade_date'])

plt.plot(data['trade_date'], data['close'])
plt.title(f"{stock_code} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show()
