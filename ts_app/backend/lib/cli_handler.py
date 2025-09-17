import json
from datetime import datetime, timedelta
import pytz
from lib import timeframes
from lib.context import ContextHelper

class CLIHandler:
    
    ticker_data = {
        "ticker": "",
        "timeframe": "",
        "initial_period": "",
        "end_period": ""
    }

    options_list = []
    flags_data = {
        "flag_adr": False,
        "flag_atr": False,
        "flag_guppy": False,
        "flag_cbl": False,
        "flag_save_to_file": False,
        "flag_show_chart": False,
        "flag_show_raw_data" : False
    }
    
    def _parse_options(self, arg, context):

        if "adr" in arg.lower():
            self.options_list.append("adr")
        elif "atr" in arg.lower():
            self.options_list.append("atr")
        elif "guppy" in arg.lower():
            self.options_list.append("guppy")
        elif "cbl" in arg.lower():
            self.options_list.append("cbl")
        elif "macd" in arg.lower():
            self.options_list.append("macd")
        elif "show-raw-data" in arg.lower():
            self.options_list.append("show-raw-data")

    def _valid_parse_ticker_data(self, sys, context):

        pgm_name = sys.argv[0]

        if len(sys.argv) < 4:
            print(f"ERROR: Wrong syntax. Need at least 3 parameter for TICKER, TIMEFRAME and INITIAL PERIOD. \nSyntax: python {pgm_name} <ticker> <timeframe: D1, H1, M5> <initial_period: YYYY-MM-DD> [end_period: YYYY-MM-DD] [--options]")
            sys.exit(1)

        try:
            self.ticker_data["ticker"] = sys.argv[1].upper()
            self.ticker_data["timeframe"] = sys.argv[2].upper()

            #check if period is in YYYY-MM-DD format
            try:
                self.ticker_data["initial_period"] = sys.argv[3]
                datetime.strptime(self.ticker_data["initial_period"], "%Y-%m-%d")
            except ValueError:
                print(f"ERROR: An invalid date for Initial Period was provided: [{sys.argv[3]}]. Expected format: YYYY-MM-DD")
                sys.exit(1)
            

        except IndexError:
            print(f"ERROR: Wrong syntax.\nSyntax: python {pgm_name} <ticker> <timeframe: D1, H1, M5> <initial_period: YYYY-MM-DD> [end_period: YYYY-MM-DD]")
            sys.exit(1)

        try:
            if not sys.argv[4].startswith("--"):
                self.ticker_data["end_period"] = sys.argv[4]
                datetime.strptime(self.ticker_data["end_period"], "%Y-%m-%d")
            else:
                tomorrow = datetime.now() + timedelta(days=1)
                self.ticker_data["end_period"] = tomorrow.strftime("%Y-%m-%d")
        except IndexError:
            #calculate tomorrow's date
            tomorrow = datetime.now() + timedelta(days=1)
            self.ticker_data["end_period"] = tomorrow.strftime("%Y-%m-%d")
        except ValueError:
            print(f"ERROR: An invalid date for End Period was provided: [{sys.argv[4]}]. Expected format: YYYY-MM-DD")
            sys.exit(1)


        # Calculate the number of bars based on the timeframe
        # and determine if the period is long enough to calculate the indicators
        timezone = pytz.timezone('America/Sao_Paulo')
        initial_period = datetime.strptime(self.ticker_data["initial_period"], "%Y-%m-%d").replace(tzinfo=timezone)
        end_period = datetime.strptime(self.ticker_data["end_period"], "%Y-%m-%d").replace(tzinfo=timezone)

        mt5_timeframe = timeframes.get_mt5_timeframes(self.ticker_data["timeframe"])
        number_of_bars = timeframes.get_number_of_bars(mt5_timeframe, initial_period, end_period)

        ctxHelper = ContextHelper()
        atr_param = ctxHelper.get_context_specific_data(context, "atr_smp", "indicator", "data.atr_period")
        adr_param = ctxHelper.get_context_specific_data(context, "adr", "indicator", "data.adr_period")
        
        if (number_of_bars < atr_param or 
            number_of_bars < adr_param):
            print(f"ERROR: The interval between {self.ticker_data['initial_period']} and {self.ticker_data['end_period']} is too short to calculate ADR ({adr_param}) and ATR ({atr_param}) for a timeframe of {self.ticker_data['timeframe']}.")
            sys.exit(1)

    def get_context_from_cmd_line(self, sys, context):

        self._valid_parse_ticker_data(sys, context)

        #add ticker data to context
        context["ticker_data"] = self.ticker_data

        # parse the optional command line arguments
        for arg in sys.argv:
            if arg.startswith("--"):
                self._parse_options(arg, context)
        
        context["options_list"] = self.options_list
        
        return context
