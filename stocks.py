import yfinance as yf
import pandas as pd
import schedule,time, pytz
import datetime as dt
from datetime import timedelta

    

ticks = ('TSLA', 'AAPL', 'AMZN', 'F', 'AMC', 'SNDL', 'MSFT', 'DIS', 'NIO', 
'META', 'NFLX', 'NVDA', 'LCID', 'TWTR', 'VOO', 'SNAP', 'SPY', 'PFE', 'GPRO', 'GOOGL', 'AAL', 'PLUG', 'CCL', 'BABA', 'HOOD', 'BAC', 'SBUX', 'RIVN', 'PLTR', 'DAL', 'AMD', 'NOK', 'GME', 'TLRY', 'KO', 'COIN', 'VTI', 'T', 'CGC', 'SPCE', 'PYPL', 'UBER', 'MRNA', 'BB', 'GM', 'FCEL', 'RBLX', 'GE', 'WMT', 'SQ', 'PSEC', 'NCLH', 'WKHS', 'BA', 'DKNG', 'ABNB', 'QQQ', 'CRON', 'UAL', 'SIRI', 'CHPT', 'NKLA', 'JNJ', 'NKE', 'XOM', 'LUV', 'SOFI', 'INTC', 'ARKK', 'RIOT', 'MRO', 'PTON', 'DWAC', 'GOOG', 'OCGN', 'SHOP', 'JBLU', 'COST', 'ET', 'BNGO', 'RCL', 'SONY', 'TSM', 'WISH', 'RYCEY', 'V', 'JPM', 'CPRX', 
'TGT', 'CLOV', 'ZM', 'FUBO', 'O', 'RITM', 'CRM', 'IVR', 'QS', 'SPHD', 'PENN')

def open_market():
    market = True
    timezone = pytz.timezone('US/Eastern')
    print(type(timezone))
    aware = dt.datetime.now(timezone).time()
    print(aware) 
  
    pastTime = dt.datetime.now(timezone) - dt.timedelta(minutes=5)  # time of 5minutes ago
    print(pastTime)
    market_open = dt.time(10,00,0) # 9:30AM Open time of the market
    market_close = dt.time(12,00,0) # 3:59PM Closing time of the market

    if aware > market_open and aware < market_close:
         market = True
    else:
     print('### market is closed')
     pass

     return(market)

def watchlist():
    timezone = pytz.timezone('US/Eastern')
    print(type(timezone))
    aware = dt.datetime.now(timezone).time()
    print(aware) 
  
    pastTime = dt.datetime.now(timezone) - dt.timedelta(minutes=5)  # time of 5minutes ago
    for x in ticks:
        toStr = str(x)
        syb = yf.Ticker(toStr)
        dataPresent = pd.DataFrame(syb.history(interval="1m",period='1d',))
        dataPast = pd.DataFrame(syb.history(interval="1m",period='1d',start=pastTime, end=dt.datetime.now(timezone)))
        if dataPast['Open'].sum() < dataPresent['Open'].sum():
                     print(dataPast['Open'].sum())
                     print(dataPresent['Open'].sum())
                     print('Watch stock')
        else:
            print(toStr, 'Proceed to sell with robinhood')
            
        
# schedule.every(5).minutes.do(watchlist)
watchlist()
# while open_market():
#     schedule.run_pending()
#     time.sleep(1)
#Next buy with robinhood but first put the stocks in tick in your robinhood account you need to own them               

# Fixed past time 