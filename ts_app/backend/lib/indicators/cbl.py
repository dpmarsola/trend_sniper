class CBL:
    
    def calculate(self, df):

        df['cbl'] = float(0)
        df['pivot'] = float(0)

        for i in range(len(df)):
            if i == 0:
                df.at[df.iloc[i].name, 'cbl'] = df.iloc[i].high
                df.at[df.iloc[i].name, 'pivot'] = df.index[i]
            else:
                if df.iloc[i-1].cbl > df.iloc[ df.index == df.iloc[i-1].pivot]['low'].item():
                    if df.iloc[i].close > df.iloc[i-1].cbl:
                        df.at[df.iloc[i].name, 'cbl'] = self.__cbl_change_low(df.iloc[i], df)
                        df.at[df.iloc[i].name, 'pivot'] = df.index[i]
                    else:
                        if df.iloc[i].low <  df.iloc[ df.index == df.iloc[i-1].pivot]['low'].item():
                            df.at[df.iloc[i].name, 'cbl'] = self.__cbl_change_high(df.iloc[i], df)
                            df.at[df.iloc[i].name, 'pivot'] = df.index[i]
                        else:
                            df.at[df.iloc[i].name, 'cbl'] = df.iloc[i-1].cbl
                            df.at[df.iloc[i].name, 'pivot'] = df.iloc[i-1].pivot
                else:
                    if df.iloc[i].close <  df.iloc[ df.index == df.iloc[i-1].pivot]['cbl'].item():
                        df.at[df.iloc[i].name, 'cbl'] = self.__cbl_change_high(df.iloc[i], df)
                        df.at[df.iloc[i].name, 'pivot'] = df.index[i]
                    else:
                        if df.iloc[i].high > df.iloc[ df.index == df.iloc[i-1].pivot]['high'].item():
                            df.at[df.iloc[i].name, 'cbl'] = self.__cbl_change_low(df.iloc[i], df)
                            df.at[df.iloc[i].name, 'pivot'] = df.index[i]
                        else:
                            df.at[df.iloc[i].name, 'cbl'] = df.iloc[i-1].cbl
                            df.at[df.iloc[i].name, 'pivot'] = df.iloc[i-1].pivot
        
        # get rid of the pivot column
        df.drop(columns=['pivot'], inplace=True)
        return df

    def __cbl_change_low(self, row, df):
        result = self.__find_3_significant_bars(row, df, "low")
        return result
    
    def __cbl_change_high(self, row, df):
        result = self.__find_3_significant_bars(row, df, "high")
        return result

    def __find_3_significant_bars(self, row, df, high_low):
        """
        Find the 3 significant bars before the current bar.
        A significant bar is a bar that has a higher high or lower low than the previous bar.
        """

        sig_bars = []

        if high_low == "low":
            sig_bars.append(row.low)
            reference = row.low
        else:
            sig_bars.append(row.high)
            reference = row.high

        sub_df = df[df.datetime < row.datetime].copy()

        for i in range(len(sub_df)-1, 0, -1):
            if high_low == "low":
                if sub_df.iloc[i].low < sub_df.iloc[ sub_df.index == sub_df.iloc[i].pivot]['low'].item():
                    break

                if sub_df.iloc[i].low < reference:
                    sig_bars.append(sub_df.iloc[i].low)
                    reference = sub_df.iloc[i].low
            else:
                if sub_df.iloc[i].high > sub_df.iloc[ sub_df.index == sub_df.iloc[i].pivot]['high'].item():
                    break

                if sub_df.iloc[i].high > reference:
                    sig_bars.append(sub_df.iloc[i].high)
                    reference = sub_df.iloc[i].high
            
            if len(sig_bars) == 2:
                if high_low == "low":
                    if sub_df.iloc[i].low < reference:
                        sig_bars.append(sub_df.iloc[i].low)
                else:
                    if sub_df.iloc[i].high > reference:
                        sig_bars.append(sub_df.iloc[i].high)                       

            if len(sig_bars) == 3:
                break

        if len(sig_bars) == 3:
            return sig_bars[2]
        elif len(sig_bars) == 2:
            return sig_bars[1]
        elif len(sig_bars) == 1:
            return sig_bars[0]