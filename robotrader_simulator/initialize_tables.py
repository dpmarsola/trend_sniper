from datetime import datetime
import data.simulation as sim
import data.account_position as acc

def initialize_tables(start_date, end_date, frequency, asset, initial_balance):

    # Create a new simulation ID and initilize the simulation
    curr_date = datetime.now()
    formmatted_date = curr_date.strftime("%Y%m%d_%H%M")
    simulation_id = f'sim_{formmatted_date}'
    result = sim.select_simulation_data_by_id(simulation_id)
 
    if result == None:
        sim.insert_simulation_data((simulation_id, start_date, end_date, frequency, asset, initial_balance, initial_balance))
        account_id = simulation_id.replace("sim", "acc")
        account_name = asset
        acc.insert_account_position_data((account_id, account_name, "NA", 0, simulation_id))
        
    return simulation_id