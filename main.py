
import robin_stocks.robinhood as rh
import config
import sys

''' 
 pip install pandas
 pip install datetime
 pip install matplotlib.pyplot
 pip install robin_stocks 
 
 Write the above lines of code one at a time in your integrated terminal on replit
 
 '''


# This session handles the login 

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


def BUY(ticker, amount):
    buy = rh.order_buy_market(ticker, amount)
    
    
    
def SELL(ticker, amount):
    buy = rh.order_sell_market()
    
   
if __name__ == "__main__":
    login(days=1)
    rh.get_top_100()

