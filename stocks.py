from tradingview_ta import *
import datetime as dt
import pandas as pd
import tabulate as tb
import schedule,time, pytz
from datetime import timedelta


ticks = ('TSLA', 'AAPL', 'AMZN', 'F', 'AMC', 'SNDL', 'MSFT', 'DIS', 'NIO', )

tostring = str(ticks)


tesla = TA_Handler(
    symbol=["NASDAQ:TSLA", "NASDAQ:APPL"],
    screener="america",
    exchange="all",
    interval='1m'
)
indicator = tesla.get_indicators()
print(indicator["open"])

# 1. Get prices for 50 stocks from the initial 100 stocks
# 2. Get the past price of the stocks[5mins ago]
# 3. Compare the present price with the past price
# 4. Check the prices once every 5mins three times
# 5. if value increase then BUY
# 6. Check the prices once every 5mins three times, if price decrease then SELL
# 7. if bought stock from step 5 increase in price then SELL
# 8. is time {} then sell all