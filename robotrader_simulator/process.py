import information as info
import operate as op
import constants

information = info.Information()
operate = op.Operate()

def process_cycle(simulation_id, period, asset, strategy):
    
    status = information.check_status_positioned(simulation_id)
    
    if status["positioned"] == True:
        decision = strategy.sginal_out(period)
        if decision == constants.GET_OUT:
            operate.close_position(simulation_id, period, asset)
    else:
        decision, position_type = strategy.sginal_in(period)
        if decision == constants.GET_IN:
            operate.open_position(simulation_id, period, asset, position_type)

    
    
