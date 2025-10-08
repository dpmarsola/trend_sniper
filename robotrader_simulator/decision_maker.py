import data.simulation as sim
import data.account_position as acc
from datetime import datetime
import parms
import constants


class Decision_Maker():
    
    flag = True
    position_type = ""
    position_amount = 0
    position_quantity = 0

    def check_status_positioned(self, simulation_id):
        
        result = {"positioned" : False,
                  "position_amount" : 0,
                  "position_type" : constants.NA}

        _,_,self.position_type,self.position_amount,self.position_quantity,_ = acc.select_account_position_data_by_simulation_id(simulation_id)    
        
        if self.position_type != constants.NA:
            result["position_amount"] = self.position_amount
            result["position_type"] = self.position_type
            result["position_quantity"] = self.position_quantity
            result["positioned"] = True

        return result 
    
    def DUMMY_stay_or_get_in(self, period):
        
        if int(period.strftime("%d")) % 2 != 0:
            position_type = constants.SHORT
            decision = constants.GET_IN
        else:
            position_type = constants.LONG
            decision = constants.STAY
        
        return decision, position_type

    def DUMMY_stay_or_get_out(self, period):
        
        if int(period.strftime("%d")) % 2 == 0:
            decision = constants.GET_OUT
        else:
            decision = constants.STAY
            
        return decision

    def determine_amount_to_expose(self, simulation_id):
        
        _,_,_,_,_,_,current_balance = sim.select_simulation_data_by_id(simulation_id)
        
        exposable_amount = current_balance * (int(parms.EXPOSABLE_PERCENTAGE)) // 100
        
        return exposable_amount
    
    def get_position_information(self, simulation_id):
        
        _,_,position_type,exposed_amount,position_quantity,_ = acc.select_account_position_data_by_simulation_id(simulation_id)
        
        return (position_type, exposed_amount, position_quantity)
    
    def DUMMY_get_asset_current_market_price(self, asset):
        
        return 1.49