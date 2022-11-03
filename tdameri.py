from asyncore import close_all
import robin_stocks.tda as td
import config, stocks
from datetime import timedelta
import datetime as dt
import schedule,time, pytz




passcode = td.authentication.generate_encryption_passcode()


def logging_first(passcode,client_id, authToken, reToken):
    td.login_first_time(passcode)
    



def login():
    td.authentication.login(passcode)
    
    td.authentication.set_login_state
  

def open_market():
    market = False
    timezone = pytz.timezone('US/Eastern')
    aware = dt.datetime.now(timezone).time()
    print(aware) 

    market_open = dt.time(10,00,0) # 9:30AM Open time of the market
    market_close = dt.time(12,00,0) # 3:59PM Closing time of the market
    close_all = dt.time(3, 00, 0)

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
    pastTime = dt.datetime.mow(timezone)# time of 5minutes ago
    pastTime2 = pastTime - dt.timedelta(minutes=5)
    print(pastTime)
    print(pastTime2)

  
def get_market_options():
    td.stocks.get_quotes(stocks.ticks, jsonify=True)
    
    
def get_PriceAction():
    current = td.stocks.get_price_history(stocks.ticks, period=1, period_type='day', frequency=5)
    previous =  td.stocks.get_price_history(stocks.ticks, period=1, period_type='day', frequency=5, start_date=pastTime2, end_date=pastTime) 
    
    



def SELL_ALL():
    if close_all:
        # sell all stocks traded during market hour
        
    
    

while open_market():
    
    
    
    
