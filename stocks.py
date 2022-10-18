import yfinance as yf
import pandas as pd
import datetime as dt
import time


ticks = ('TSLA', 'AAPL', 'AMZN', 'F', 'AMC', 'SNDL', 'MSFT', 'DIS', 'NIO',
         'META', 'NFLX', 'NVDA', 'LCID', 'TWTR', 'VOO', 'SNAP', 'SPY', 'PFE', 'GPRO', 'GOOGL', 'AAL', 'PLUG', 'CCL', 'BABA', 'HOOD', 'BAC', 'SBUX', 'RIVN', 'PLTR', 'DAL', 'AMD', 'NOK', 'GME', 'TLRY', 'KO', 'COIN', 'VTI', 'T', 'CGC', 'SPCE', 'PYPL', 'UBER', 'MRNA', 'BB', 'GM', 'FCEL', 'RBLX', 'GE', 'WMT', 'SQ', 'PSEC', 'NCLH', 'WKHS', 'BA', 'DKNG', 'ABNB', 'QQQ', 'CRON', 'UAL', 'SIRI', 'CHPT', 'NKLA', 'JNJ', 'NKE', 'XOM', 'LUV', 'SOFI', 'INTC', 'ARKK', 'RIOT', 'MRO', 'PTON', 'DWAC', 'GOOG', 'OCGN', 'SHOP', 'JBLU', 'COST', 'ET', 'BNGO', 'RCL', 'SONY', 'TSM', 'WISH', 'RYCEY', 'V', 'JPM', 'CPRX',
         'TGT', 'CLOV', 'ZM', 'FUBO', 'O', 'RITM', 'CRM', 'IVR', 'QS', 'SPHD', 'PENN')


def watchlist():
    for x in ticks:
        toStr = str(x)
        syb = yf.Ticker(toStr)
        data = pd.DataFrame(syb.history(interval="1m", period='1d',))
        data2 = pd.DataFrame(syb.history(interval="2m", period='1d',))
        if data['Open'].sum() < data2['Open'].sum():
            print(data['Open'].sum())
            print(data2['Open'].sum())
            print('Watch stock')
        else:
            print('Proceed to buy with robinhood')

        break


def open_market():
    market = False
    time_now = dt.datetime.now().time()

    market_open = dt.time(11, 00, 0)  # 9:30AM Open time of the market
    market_close = dt.time(12, 12, 0)  # 3:59PM Closing time of the market

    if time_now > market_open and time_now < market_close:
        market = True
    else:
        print('### market is closed')
        pass

    return (market)


if __name__ == "__main__":
        while open_market():
            watchlist()

    # Next buy with robinhood but first put the stocks in tick in your robinhood account you need to own them

    # print(datetime.datetime.now() - datetime.timedelta(minutes=5))
