import yfinance as yf
import pandas as pd
import schedule,time, pytz
import datetime as dt
import robin_stocks.robinhood as rh
from datetime import timedelta
import main, config




def login(days):
    time_logged_in = 60*60*24*days
    rh.authentication.login(username=config.USERNAME,
                            password=config.PASSWORD,
                            expiresIn=time_logged_in,
                            scope='internal',
                            by_sms=True,
                            store_session=True)


# This session handles the logout 
def logout():
    rh.authentication.logout()


ticks = ('TSLA', 'AAPL', 'AMZN', 'F', 'AMC', 'SNDL', 'MSFT', 'DIS', 'NIO', 
'META', 'NFLX', 'NVDA', 'LCID', 'TWTR', 'VOO', 'SNAP', 'SPY', 'PFE', 'GPRO', 'GOOGL', 'AAL', 'PLUG', 'CCL', 'BABA', 'HOOD', 'BAC', 'SBUX', 'RIVN', 'PLTR', 'DAL', 'AMD', 'NOK', 'GME', 'TLRY', 'KO', 'COIN', 'VTI', 'T', 'CGC', 'SPCE', 'PYPL', 'UBER', 'MRNA', 'BB', 'GM', 'FCEL', 'RBLX', 'GE', 'WMT', 'SQ', 'PSEC', 'NCLH', 'WKHS', 'BA', 'DKNG', 'ABNB', 'QQQ', 'CRON', 'UAL', 'SIRI', 'CHPT', 'NKLA', 'JNJ', 'NKE', 'XOM', 'LUV', 'SOFI', 'INTC', 'ARKK', 'RIOT', 'MRO', 'PTON', 'DWAC', 'GOOG', 'OCGN', 'SHOP', 'JBLU', 'COST', 'ET', 'BNGO', 'RCL', 'SONY', 'TSM', 'WISH', 'RYCEY', 'V', 'JPM', 'CPRX', 
'TGT', 'CLOV', 'ZM', 'FUBO', 'O', 'RITM', 'CRM', 'IVR', 'QS', 'SPHD', 'PENN')



def open_market():
    market = False
    timezone = pytz.timezone('US/Eastern')
    aware = dt.datetime.now(timezone).time()
    print(aware) 

    market_open = dt.time(10,00,0) # 9:30AM Open time of the market
    market_close = dt.time(12,00,0) # 3:59PM Closing time of the market

    if aware > market_open and aware < market_close:
         market = True
    else:
        # print('### market is closed')
        pass

    return(market)

def watchlist():
    timezone = pytz.timezone('US/Eastern')
    print(type(timezone))
    aware = dt.datetime.now(timezone).time()
    print(aware) 
    global pastTime
    pastTime = dt.datetime.now(timezone)# time of 5minutes ago
    pastTime2 = dt.datetime.now(timezone) - dt.timedelta(minutes=5)
    print(pastTime)
    print(pastTime2)
    for x in ticks:
        toStr = str(x)
        syb = yf.Ticker(toStr)
        data = pd.DataFrame(syb.history(interval="1m",period='1d'))
        data2 = pd.DataFrame(syb.history(interval="1m",period='1d', end=pastTime, start=pastTime2))
        data1 = data['Open'].reset_index(drop=True)
        dataPrev = data2['Open'].reset_index(drop=True)
        prev1 = data1.tail().iloc[0:297, 2]
        prev2 = dataPrev.tail().iloc[0:297, 2]
        print(prev2, prev1)
        if prev2 > prev1:
                      print(toStr, prev1, " : ", prev2 )
                      print(toStr, 'Watch stop')
        else:
            print(toStr, 'Proceed to buy with robinhood')
            main.BUY(toStr, 1)
                 
    print(toStr)      
if __name__ == "__main__":
    login(days=1)  
    
    
              
    while open_market():
     schedule.every(5).minutes.do(watchlist())
     schedule.run_pending()
     time.sleep(1)
     
    logout()
#Next buy with robinhood but first put the stocks in tick in your robinhood account you need to own them               

