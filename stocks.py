import yfinance as yf
import pandas as pd
import config
import schedule
import time
import trader
import robin_stocks.robinhood as rh



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
        
        
def get_price(symbol):
    ticker = yf.Ticker(symbol)
    week_data = ticker.history(interval="1m",period='max')
    return(week_data)
            
            
            
def get_tag():
    market_tag = rh.markets.get_top_100(info=None)
    for x in range(len(market_tag)):
      syb = market_tag[x]["symbol"]
      print(syb)

    
if __name__ == "__main__":
    login(days=1)
    tops = get_tag(trader.stocks)
    print(tops)