import ta

class Guppy:

    def calculate(self, df, number_of_periods):
        # Fast ema periods for Guppy 
        fast_ema_1 = number_of_periods[0]
        fast_ema_2 = number_of_periods[1]
        fast_ema_3 = number_of_periods[2]
        fast_ema_4 = number_of_periods[3]
        fast_ema_5 = number_of_periods[4]
        fast_ema_6 = number_of_periods[5]

        # Slow ema periods for Guppy
        slow_ema_1 = number_of_periods[6]
        slow_ema_2 = number_of_periods[7]
        slow_ema_3 = number_of_periods[8]
        slow_ema_4 = number_of_periods[9]
        slow_ema_5 = number_of_periods[10]
        slow_ema_6 = number_of_periods[11]

        df['ema_f1'] = ta.trend.ema_indicator(df['close'], window=fast_ema_1, fillna=True).round(3)
        df['ema_f2'] = ta.trend.ema_indicator(df['close'], window=fast_ema_2, fillna=True).round(3)
        df['ema_f3'] = ta.trend.ema_indicator(df['close'], window=fast_ema_3, fillna=True).round(3)
        df['ema_f4'] = ta.trend.ema_indicator(df['close'], window=fast_ema_4, fillna=True).round(3)
        df['ema_f5'] = ta.trend.ema_indicator(df['close'], window=fast_ema_5, fillna=True).round(3)
        df['ema_f6'] = ta.trend.ema_indicator(df['close'], window=fast_ema_6, fillna=True).round(3)

        df['ema_s1'] = ta.trend.ema_indicator(df['close'], window=slow_ema_1, fillna=True).round(3)
        df['ema_s2'] = ta.trend.ema_indicator(df['close'], window=slow_ema_2, fillna=True).round(3)
        df['ema_s3'] = ta.trend.ema_indicator(df['close'], window=slow_ema_3, fillna=True).round(3)
        df['ema_s4'] = ta.trend.ema_indicator(df['close'], window=slow_ema_4, fillna=True).round(3)
        df['ema_s5'] = ta.trend.ema_indicator(df['close'], window=slow_ema_5, fillna=True).round(3)
        df['ema_s6'] = ta.trend.ema_indicator(df['close'], window=slow_ema_6, fillna=True).round(3)

        return df

