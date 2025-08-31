from ta.volatility import AverageTrueRange

class ATR:

    def calculate(self, df, number_of_periods, multiplier):
        
        df['prev_close'] = df['close'].shift(1)
        df['true_range'] = AverageTrueRange(high=df["high"], low=df["low"], close=df["close"], window=number_of_periods)._true_range(high=df["high"], low=df["low"], prev_close=df["prev_close"])
        
        aux_df = df.copy()
        df['displacement'] = df.apply(lambda x: self.__calculate_average_true_range_simple_method(aux_df, x.name - number_of_periods + 1, x.name + 1), axis=1).round(2)
        df['displacement'] = df['displacement'] * multiplier
        df['avg_true_range'] = (df['open'] - df['displacement'])

        df['avg_true_range'] = self.calculate_pivot(df)
        df.drop(columns=['prev_close', 'true_range', 'displacement'], inplace=True)        
        return df

    def __calculate_average_true_range_simple_method(self, df, iperiod, fperiod):

        """
        Calculate the average true range using a simple method.
        The formula is sum of the true ranges divided by the number of periods.
        """
        # sum all the true ranges and devide by the number of periods
        if iperiod == fperiod:
            # If the period is the same, it means is the period 0, and has only 1 value for the atr
            atr = df['true_range'][0]
        else:
            sum = df['true_range'][iperiod:fperiod].sum()
            atr = sum / (fperiod - iperiod)

        return atr

    def calculate_pivot(self, df):

        df["pivot"] = float(0)

        for i in range(len(df)):
            if i == 0:
                df.at[df.iloc[i].name, 'avg_true_range'] = df.iloc[i].high + df.iloc[i].displacement
                df.at[df.iloc[i].name, 'pivot'] = df.index[i]
            else:
                if df.iloc[i-1].avg_true_range > df.iloc[ df.index == df.iloc[i-1].pivot]['low'].item():
                    if df.iloc[i].close > df.iloc[i-1].avg_true_range:
                        df.at[df.iloc[i].name, 'avg_true_range'] = df.iloc[i].low - df.iloc[i].displacement
                        df.at[df.iloc[i].name, 'pivot'] = df.index[i]
                    else:
                        if df.iloc[i].low <  df.iloc[ df.index == df.iloc[i-1].pivot]['low'].item():
                            df.at[df.iloc[i].name, 'avg_true_range'] = df.iloc[i].high + df.iloc[i].displacement
                            df.at[df.iloc[i].name, 'pivot'] = df.index[i]
                        else:
                            df.at[df.iloc[i].name, 'avg_true_range'] = df.iloc[i-1].avg_true_range
                            df.at[df.iloc[i].name, 'pivot'] = df.iloc[i-1].pivot
                else:
                    if df.iloc[i].close <  df.iloc[ df.index == df.iloc[i-1].pivot]['avg_true_range'].item():
                        df.at[df.iloc[i].name, 'avg_true_range'] = df.iloc[i].high + df.iloc[i].displacement
                        df.at[df.iloc[i].name, 'pivot'] = df.index[i]
                    else:
                        if df.iloc[i].high > df.iloc[ df.index == df.iloc[i-1].pivot]['high'].item():
                            df.at[df.iloc[i].name, 'avg_true_range'] = df.iloc[i].low - df.iloc[i].displacement
                            df.at[df.iloc[i].name, 'pivot'] = df.index[i]
                        else:
                            df.at[df.iloc[i].name, 'avg_true_range'] = df.iloc[i-1].avg_true_range
                            df.at[df.iloc[i].name, 'pivot'] = df.iloc[i-1].pivot
        
        # get rid of the pivot column
        df.drop(columns=['pivot'], inplace=True)
        return df['avg_true_range']
