from ta.volatility import AverageTrueRange
import pandas as pd

class ADR:
    
    def calculate(self, df, number_of_periods, multiplier):

        df['daily_range'] = df['high'] - df['low']

        counter = 0
        sum_of_daily_range = 0.0
        adr = 0.0
        list_of_adr = []

        for idx, row in df.iterrows():

            if counter < (number_of_periods - 1):
                sum_of_daily_range += row['daily_range']
            else:
                if counter == (number_of_periods - 1):
                    adr = sum_of_daily_range / number_of_periods
                else:
                    adr = ((adr * (number_of_periods - 1) ) + row['daily_range']) / number_of_periods

            list_of_adr.append(round(adr, 2))
            counter += 1

        df['displacement'] = list_of_adr
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
