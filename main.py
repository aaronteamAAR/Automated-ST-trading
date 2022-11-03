
from sqlite3 import Timestamp
import robin_stocks.tda as td
import config, tdameri
import sys
import pandas as pd

# ''' 
#  pip install pandas
#  pip install datetime
#  pip install matplotlib.pyplot
#  pip install robin_stocks 
 
#  Write the above lines of code one at a time in your integrated terminal on replit
 
#  '''


# # This session handles the login 





def login():
    td.authentication.login(tdameri.passcode)
    
    td.authentication.set_login_state



def BUY():
     td.orders.place_order()