from ta.volatility import AverageTrueRange
import pandas as pd

class ADR:
    
    def calculate(self, df, multiplier):

        df['daily_range'] = df['high'] - df['low']
        aux_df = df.copy()
        df['displacement'] = df.apply(lambda x: self.__calculate_average_daily_range(aux_df, x.name - 3 + 1, x.name + 1), axis=1).round(2)
        df['displacement'] = df['displacement'] * multiplier
        df['avg_daily_range'] = (df['open'] + df['displacement'])

        df.drop(columns=['daily_range', 'displacement'], inplace=True)

        return df
    
    def __calculate_average_daily_range(self, df, iperiod, fperiod):

        # sum all the daily ranges and devide by the number of periods
        if iperiod == fperiod:
            # If the period is the same, it means is the period 0, and has only 1 value for the adr
            adr = df['daily_range'][0]
        else:
            sum = df['daily_range'][iperiod:fperiod].sum()
            adr = sum / (fperiod - iperiod)

        return adr
