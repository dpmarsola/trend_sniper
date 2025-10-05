import data.simulation as sim
import data.account_position as acc
from datetime import datetime


class Decision_Maker():
    
    flag = True

    def check_status_positioned(self, simulation_id):

        _,_,position,_ = acc.select_account_position_data_by_simulation_id(simulation_id)    
        
        if position == 0:
            return "not_positioned"
        else:
            return "positioned"

    def check_stay_or_get_in(self, period):
        
        if int(period.strftime("%d")) % 2 == 0:
            return "get_in"
        else:
            return "stay"
        
    def decide_to_position_short_or_long(self):
        
        if self.flag == True:
            self.flag = False
            return "short"
        else:
            self.flag = True
            return "long"

    def operate(self, operation):
        
        if operation == "buy":
            print("bought")
        else:
            print("sold")
    