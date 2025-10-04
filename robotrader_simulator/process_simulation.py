import check_status_positioned as chk_status

def process_cycle(simulation_id):
    
    status = chk_status.check_status_positioned(simulation_id)
    
    if status == "positioned":
        print("hello positioned")
        # positioned_short_or_long = logic_to_check_how_positioned_short_or_long
        # check_stay_or_get_out(positioned_short_or_long)
        
    if status == "not_positioned":
        print("world not positioned")
        # check_stay_or_get_in
        

def check_stay_or_get_out(positioned_short_or_long):

    decision = logic_to_check_stay_or_get_out
    
    if decision == "get_out":
        
        if positioned_short_or_long == "short":
            
            signal = "buy"
            perform_operation(signal)
    
        if positioned_short_or_long == "long":
            
            signal = "sell"
            perform_operation(signal)
    
        # perform accountability
    

def check_stay_or_get_in():

    decision = logic_to_check_stay_or_get_in
    
    if decision == "get_int":
        
        how_to_position = logic_to_decide_how_to_position_short_or_long
        
        if positioned_short_or_long == "short":
            
            signal = "sell"
            perform_operation(signal)
    
        if positioned_short_or_long == "long":
            
            signal = "buy"
            perform_operation(signal)


def perform_operation(signal):
    
    if signal == "buy":
        buy_logic
    
    if signal == "sell":
        sell_logic
    