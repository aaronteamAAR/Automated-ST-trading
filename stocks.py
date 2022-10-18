import yfinance as yf
import pandas as pd
import schedule
import time
import datetime
import trader
        
def get_price(symbol):
    ticker = yf.Ticker(symbol).get
    week_data = ticker.history(interval="1m",period='max')
    return(week_data)
    

ticks = ('TSLA', 'AAPL', 'AMZN', 'F', 'AMC', 'SNDL', 'MSFT', 'DIS', 'NIO', 
'META', 'NFLX', 'NVDA', 'LCID', 'TWTR', 'VOO', 'SNAP', 'SPY', 'PFE', 'GPRO', 'GOOGL', 'AAL', 'PLUG', 'CCL', 'BABA', 'HOOD', 'BAC', 'SBUX', 'RIVN', 'PLTR', 'DAL', 'AMD', 'NOK', 'GME', 'TLRY', 'KO', 'COIN', 'VTI', 'T', 'CGC', 'SPCE', 'PYPL', 'UBER', 'MRNA', 'BB', 'GM', 'FCEL', 'RBLX', 'GE', 'WMT', 'SQ', 'PSEC', 'NCLH', 'WKHS', 'BA', 'DKNG', 'ABNB', 'QQQ', 'CRON', 'UAL', 'SIRI', 'CHPT', 'NKLA', 'JNJ', 'NKE', 'XOM', 'LUV', 'SOFI', 'INTC', 'ARKK', 'RIOT', 'MRO', 'PTON', 'DWAC', 'GOOG', 'OCGN', 'SHOP', 'JBLU', 'COST', 'ET', 'BNGO', 'RCL', 'SONY', 'TSM', 'WISH', 'RYCEY', 'V', 'JPM', 'CPRX', 
'TGT', 'CLOV', 'ZM', 'FUBO', 'O', 'RITM', 'CRM', 'IVR', 'QS', 'SPHD', 'PENN')

for x in ticks:
      toStr = str(x)
      syb = yf.Ticker(toStr)
      data = pd.DataFrame(syb.history(interval="1m",period='1d',))
      print(data['Open'].sum())



//create a function to check the current price every 5 minutes