import numpy as np
import MetaTrader5 as mt5

timeframes = {
    'M1': mt5.TIMEFRAME_M1,
    'M5': mt5.TIMEFRAME_M5,
    'H1': mt5.TIMEFRAME_H1,
    'H4': mt5.TIMEFRAME_H4,
    'D1': mt5.TIMEFRAME_D1,
    'W1': mt5.TIMEFRAME_W1,
    'MN1': mt5.TIMEFRAME_MN1
}

def get_number_of_bars(mt5_timeframe, initial_period, end_period):
    """
    Calculate the number of bars based on the timeframe
    and determine if the period is long enough to calculate the indicators
    """
    business_days_count = np.busday_count(initial_period.date(), end_period.date())

    if business_days_count < 1:
        business_days_count = 1


    if mt5_timeframe == mt5.TIMEFRAME_M1:
        number_of_bars = business_days_count * (60 * 24)
    elif mt5_timeframe == mt5.TIMEFRAME_M5:
        number_of_bars = business_days_count * ((60/5) * 24)
    elif mt5_timeframe == mt5.TIMEFRAME_H1:
        number_of_bars = business_days_count * 24
    elif mt5_timeframe == mt5.TIMEFRAME_H4:
        number_of_bars = business_days_count * (24 / 4)
    elif mt5_timeframe ==  mt5.TIMEFRAME_D1:
        number_of_bars = business_days_count
    elif mt5_timeframe == mt5.TIMEFRAME_W1:
        number_of_bars = business_days_count // 5
    elif mt5_timeframe == mt5.TIMEFRAME_MN1:
        number_of_bars = business_days_count // 22

    else:
        raise ValueError("Invalid timeframe. Valid options are: M1 (1 minute), M5 (5 minutes), H1 (1 hour), H4 (4 hours), D1 (1 day), W1 (1 week), MN1 (1 month)")
    
    return number_of_bars

def get_mt5_timeframes(timeframe):
    """
    Get the time frames for the given timeframe
    """
    mt5_timeframe = timeframes.get(timeframe)

    if mt5_timeframe is None:
        raise ValueError("Invalid timeframe. Valid options are: M1 (1 minute), M5 (5 minutes), H1 (1 hour), H4 (4 hours), D1 (1 day), W1 (1 week), MN1 (1 month)")
    
    return mt5_timeframe
