import pandas as pd
import ta

class MACD:

    def calculate(self, df):

        df['ema_26'] = ta.trend.ema_indicator(df['close'], window=26, fillna=True).round(3)
        df['ema_12'] = ta.trend.ema_indicator(df['close'], window=12, fillna=True).round(3)

        df['macd'] = (df['ema_12'] - df['ema_26']).round(3)
        df['macd_signal'] = ta.trend.ema_indicator(df['macd'], window=9, fillna=True).round(3)
        df['macd_diff'] = (df['macd'] - df['macd_signal']).round(3)
        
        df.drop(columns=['ema_26', 'ema_12', 'macd', 'macd_signal'], inplace=True, errors='ignore')
        
        return df
