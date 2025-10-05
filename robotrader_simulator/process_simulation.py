import decision_maker as dm

dmaker = dm.Decision_Maker()
def process_cycle(simulation_id, period):
    
    status = dmaker.check_status_positioned(simulation_id)
    
    if status["positioned"] == True:
        print("is positioned")
        print(status)
        check_stay_or_get_out(status["position_type"], period)
    else:
        check_stay_or_get_in(period)
        

def check_stay_or_get_out(positioned_short_or_long, period):

    decision = dmaker.check_stay_or_get_out(period)
    
    if decision == "get_out":
        
        if positioned_short_or_long.lower() == "short":
            
            signal = "buy"
            perform_operation(signal)
    
        if positioned_short_or_long.lower() == "long":
            
            signal = "sell"
            perform_operation(signal)
    
        # perform accountability
    

def check_stay_or_get_in(period):

    decision = dmaker.check_stay_or_get_in(period)
    
    if decision == "get_in":
       
        how_to_position = dmaker.decide_to_position_short_or_long()
       
        print(how_to_position)
        
        if how_to_position.lower() == "short":
            
            signal = "sell"
            perform_operation(signal)
    
        if how_to_position.lower() == "long":
            
            signal = "buy"
            perform_operation(signal)


def perform_operation(signal):
    
    if signal == "buy":
        dmaker.operate(signal)
    
    if signal == "sell":
        dmaker.operate(signal)
    