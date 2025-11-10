from ta.volatility import AverageTrueRange
import pandas as pd

class RSI:
    
    def calculate(self, df: pd.DataFrame, number_of_periods):

        df['aux_col'] = df['close'] - df['close'].shift(1)
        df['gains'] = 0
        df['losses'] = 0
        df['avg_gain'] = 0
        df['avg_loss'] = 0

        for idx, row in df.iterrows():
            if row['aux_col'] > 0:
                df.at[idx, 'gains'] = row['aux_col']
            if row['aux_col'] < 0:
                df.at[idx, 'losses'] = (row['aux_col'] * -1)

        counter = 0

        for idx, row in df.iterrows():
            if counter == (number_of_periods - 1):
                df.at[idx, 'avg_gain'] = df['gains'].iloc[0:idx].sum()
                df.at[idx, 'avg_loss'] = df['losses'].iloc[0:idx].sum()
            else:
                if counter > (number_of_periods - 1):
                    df.at[idx, 'avg_gain'] = ((df['avg_gain'].iloc[idx-1] * (number_of_periods - 1)) + row['gains']) / number_of_periods
                    df.at[idx, 'avg_loss'] = ((df['avg_loss'].iloc[idx-1] * (number_of_periods - 1)) + row['losses']) / number_of_periods

            counter += 1

        df['relative_strength'] = df['avg_gain']/df['avg_loss']

        df['rsi'] = 100 - (100 / (1 + df['relative_strength']))


        df = df.drop(['aux_col', 'gains', 'losses', 'avg_gain', 'avg_loss', 'relative_strength'], axis=1)
        print(df)


