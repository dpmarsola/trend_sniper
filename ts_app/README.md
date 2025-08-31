
To call the application from command line:
python -m app.trendsniper ITSA4 D1 2025-08-01 --adr --guppy 


To call the application as a backend service:
from app import trendsniper as ts

ticker_data = { "ticker": "ITSA4", "timeframe": "W1", "initial_period": "2025-01-01", "end_period": "2025-08-01"}
options_list = ["adr", "guppy", "atr", "macd", "show-raw-data"]

ts.parse_input_from_backend_request(ticker_data, options_list)

Example of the http request:
http://localhost:8000/trendsniper/?ticker=ITSA4&timeframe=D1&initial_period=2025-08-01&end_period=2025-08-30&options=adr&options=guppy&options=atr&options=macd&options=show-raw-data
