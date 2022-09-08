import config
import robin_stocks as rh

import datetime as dt
import time

def login(days):
    time_logged_in  = 60*60*24*days
    rh.authentication.login(username = config.USERNAME,
                            password = config.PASSWORD,
                            expiresIn = time_logged_in,
                            scope = 'internal',
                            by_sms = True,
                            store_session = True)

def logout():
    rh.authentication.logout()


def get_stocks():
    stocks = list()
    stocks.append('CNET')
    stocks.append('NKE')
    return(stocks)

def open_market():
    market = False
    time_now = dt.datetime.now().time()

    market_open = dt.time(9, 30, 0) #market open time
    market_close = dt.time(15, 59, 0) #market close time

    if time_now > market_open and time_now < market_close:
        market = True
    else:
        print("Market is closed")

    return (market)

open_market()
