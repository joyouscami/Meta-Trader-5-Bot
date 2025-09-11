import MetaTrader5 as mt5
from datetime import datetime, timedelta

# Replace with your actual login credentials
login =2000986368       # Your account number
password = 'Ricmwas2015!'
server = 'JustMarkets-Demo'  # e.g., 'MetaQuotes-Demo'

# Initialize MT5 connection
if not mt5.initialize(login=login, password=password, server=server):
    print("Failed to initialize MT5:", mt5.last_error())
    quit()
else:
    print("MT5 initialized successfully")
