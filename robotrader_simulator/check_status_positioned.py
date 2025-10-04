import data.simulation as sim
import data.account_position as acc

def check_status_positioned(simulation_id):

    _,_,position,_ = acc.select_account_position_data_by_simulation_id(simulation_id)    
    
    if position == 0:
        return "not_positioned"
    else:
        return "positioned"
        