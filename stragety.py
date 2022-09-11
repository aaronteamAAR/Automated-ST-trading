import pandas as pd

import robin_stocks.helper as helper
import robin_stocks.urls as urls


class trader():
 def __init__(self, stocks):
        self.stocks = stocks
        
        self.sma_hour = {stocks[i]: 0 for i in range(0, len(stocks))}
        self.run_time = 0 
        
        #self.buffer = 0.005 
        
        self.price_sma_hour = {stocks[i]: 0 for i in range(0, len(stocks))}
        
       # print('price sma hour', self.price_sma_hour)
       
 def get_historical_price(self, stock, span):
     span_interval = {'day': ' 5min', 'week': '10min', 'month': 'hrs', 'year': 'day', '5yrs': 'week'}
     interval = span_interval[span]
     
     symbols = helper.inputs_to_set(stock)
     url = urls.historicals()
     payload = {'symbols' : ','.join(symbols),
                'interval' : interval,
                'span' : span,
                'bounds' : 'regular'}
     
     data = helper.request_get(url, 'results', payload)
     
     
     historical_data = []
     for item in data:
         for subitem in item['historicals']:
             historical_data.append(subitem)
     
     print('data: \n', data)