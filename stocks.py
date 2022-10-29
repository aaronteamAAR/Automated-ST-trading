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

def watchTime():
    global prev1, prev2, toStr, aware, pastTime, pastTime2
    timezone = pytz.timezone('US/Eastern')
    print(type(timezone))
    aware = dt.datetime.now(timezone).time()
    print(aware)
    pastTime = dt.datetime(2022, 10, 28, 14, 23)# time of 5minutes ago
    pastTime2 = pastTime - dt.timedelta(minutes=5)
    print(pastTime)
    print(pastTime2)
        

 ######################################################################
 
 
 
#  Check price overtime       
def checkPriceAction():
        global toStr
        for x in ticks:
            toStr = str(x)
            syb = yf.Ticker(toStr)
            data = pd.DataFrame(syb.history(interval="1m",period='1d'))
            data2 = pd.DataFrame(syb.history(interval="1m",period='1d', end=pastTime, start=pastTime2))
            data1 = data['Open'].reset_index(drop=True)
            dataPrev = data2['Open'].reset_index(drop=True)
            prev1 = data1.tail()
            prev2 = dataPrev.tail()



# Trying to see if reset index could still select prices without index involved
            
            
def compare():
    print(checkPriceAction.prev1)  
    print(checkPriceAction.prev2)
    
         
    
      
                
if __name__ == "__main__":
    login(days=1)    
 
              
while open_market():
    watchTime()
    compare()
    main.BUY(toStr, 1)
     
    logout()
#Next buy with robinhood but first put the stocks in tick in your robinhood account you need to own them               

