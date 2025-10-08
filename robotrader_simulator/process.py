import decision_maker as dm
import operate as op
import constants

dmaker = dm.Decision_Maker()
operate = op.Operate()
def process_cycle(simulation_id, period, asset):
    
    status = dmaker.check_status_positioned(simulation_id)
    
    if status["positioned"] == True:
        check_stay_or_get_out(status["position_type"], period, simulation_id, asset)
    else:
        check_stay_or_get_in(simulation_id, period, asset)

def check_stay_or_get_out(positioned_short_or_long, period, simulation_id, asset):

    decision = dmaker.DUMMY_stay_or_get_out(period)
    
    if decision == constants.GET_OUT:
        
        operate.close_position(simulation_id, period, asset)

def check_stay_or_get_in(simulation_id, period, asset):

    decision, position_type = dmaker.DUMMY_stay_or_get_in(period)
    
    if decision == constants.GET_IN:
        
        operate.open_position(simulation_id, period, asset, position_type)
    
    
