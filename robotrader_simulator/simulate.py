
import process as ps
import pandas as pd
import initialize_tables as initab
import strategy as st

start_date = '2025-08-01'
end_date = '2025-08-11'
frequency = 'D'
asset = "ITSA4"
initial_balance = 10000.00

def simulate(start_date: str, end_date: str, frequency: str, asset: str, initial_balance: int, strategy: object):

    # populate the tables with initial values
    simulation_id = initab.initialize_tables(start_date, end_date, frequency, asset, initial_balance)

    # process periods
    periods_range = pd.date_range(start=start_date, end=end_date, freq=frequency)

    for period in periods_range:
        ps.process_cycle(simulation_id, period, asset, strategy)


simulate(start_date, end_date, frequency, asset, initial_balance, st.Strategy())