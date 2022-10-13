import yfinance as yf
import pandas as pd
import schedule
import time


        
def get_price(symbol):
    ticker = yf.Ticker(symbol)
    week_data = ticker.history(interval="1m",period='max')
    return(week_data)


            
def get_priceNow():
    tag = get_price('AAPL')
    print(tag) 
    
    
            
if __name__ == "__main__":
    schedule.every(5).seconds.do(get_priceNow)
  
while True:
    schedule.run_pending()
    time.sleep(1)
    