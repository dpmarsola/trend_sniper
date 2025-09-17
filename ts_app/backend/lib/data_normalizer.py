import MetaTrader5 as mt5
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from datetime import datetime
import pytz
from lib import timeframes
import json

register_matplotlib_converters()

class DataNormalizer:

    def _get_rates_from_metatrader(self, ticker, timeframe, initial_period, end_period):

        timezone = pytz.timezone("America/Sao_Paulo")
        initial_period = datetime.strptime(initial_period, "%Y-%m-%d").replace(tzinfo=timezone)
        end_period = datetime.strptime(end_period, "%Y-%m-%d").replace(tzinfo=timezone)
      
        mt5_timeframe = timeframes.get_mt5_timeframes(timeframe)
        number_of_bars = int(timeframes.get_number_of_bars(mt5_timeframe, initial_period, end_period))

        # connect to MetaTrader 5
        if not mt5.initialize():
            print("initialize() failed")
            mt5.shutdown()
            return None
        
        # get the rates for the given ticker and timeframe
        self.mt5_rates = mt5.copy_rates_from(ticker, mt5_timeframe, end_period, number_of_bars)
        
        if self.mt5_rates is None:
            mt5.shutdown()
            return None

        # shut down connection to MetaTrader 5
        mt5.shutdown()

        return self.mt5_rates

    def execute(self, context):
        
        ticker_data = context["ticker_data"]
        self.ticker = ticker_data["ticker"]
        self.timeframe = ticker_data["timeframe"]
        self.initial_period = ticker_data["initial_period"]
        self.end_period = ticker_data["end_period"]
        self.mt5_rates = None
        self.rates_dataframe = None

        print(f"Fetching data from MetaTrader 5 for {self.ticker} in {self.timeframe} timeframe from {self.initial_period} to {self.end_period}...")

        # Convert rates data to pandas DataFrame
        rates_dataframe = pd.DataFrame(self._get_rates_from_metatrader(self.ticker, self.timeframe, self.initial_period, self.end_period))
        
        if rates_dataframe.empty:
            raise ValueError(f"Data for {self.ticker} in {self.timeframe} timeframe from {self.initial_period} to {self.end_period} is empty.")
        else:
            # convert time in seconds into the datetime format
            rates_dataframe['datetime'] = pd.to_datetime(rates_dataframe['time'], unit='s', utc=True)

        # filter the dataframe to provide only row with the date greater than the initial_period
        rates_dataframe = rates_dataframe[ rates_dataframe['datetime'] >= self.initial_period ]

        return rates_dataframe

