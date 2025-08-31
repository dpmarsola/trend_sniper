from ..lib.indicators.adr import ADR
from ..lib.indicators.cbl import CBL
from ..lib.indicators.guppy import Guppy
from ..lib.indicators.atr import ATR
from ..lib.indicators.macd import MACD
from ..lib.context import ContextHelper


class DataEnricher:

    def execute(self, context, df):

        print("Enriching data with additional indicators...")
        
        c_helper = ContextHelper()
        
        for opt in context.get("options_list"):
            if opt == "adr":
                self.adr_period = c_helper.get_context_specific_data(context, "adr", "indicator", "data.adr_period")
                self.adr_multiplier = c_helper.get_context_specific_data(context, "adr", "indicator", "data.adr_multiplier")
                if self.adr_period > len(df.index):
                    raise ValueError(f"ADR period: {self.adr_period} is greater than the size of the dataframe: {len(df.index)}")
                df = ADR().calculate(df, self.adr_multiplier)
            if opt == "atr":
                self.atr_period = c_helper.get_context_specific_data(context, "atr_smp", "indicator", "data.atr_period")
                self.atr_multiplier = c_helper.get_context_specific_data(context, "atr_smp", "indicator", "data.atr_multiplier")
                if self.atr_period > len(df.index):
                    raise ValueError(f"ATR period: {self.atr_period} is greater than the size of the dataframe: {len(df.index)}")
                df = ATR().calculate(df, self.atr_period, self.atr_multiplier)
            if opt == "guppy":
                self.guppy_periods = c_helper.get_context_specific_data(context, "guppy", "indicator", "data.guppy_periods")
                df = Guppy().calculate(df, self.guppy_periods)
            if opt == "cbl":
                df = CBL().calculate(df)
            if opt == "macd":
                df = MACD().calculate(df)
            if opt == "show-raw-data":
                print(df)

        # set the date column as the index
        df.set_index('datetime', inplace=True)


        return df