import data.simulation as sim
import data.account_position as acc
from datetime import datetime


class Decision_Maker():
    
    flag = True
    position_type = ""
    position_amount = 0

    def check_status_positioned(self, simulation_id):
        
        result = {"positioned" : False,
                  "position_amount" : 0,
                  "position_type" : "NA"}

        _,_,self.position_type,self.position_amount,_ = acc.select_account_position_data_by_simulation_id(simulation_id)    
        
        if self.position_type != "NA":
            result["position_amount"] = self.position_amount
            result["position_type"] = self.position_type
            result["positioned"] = True

        return result 
    
    def check_stay_or_get_in(self, period):
        
        if int(period.strftime("%d")) % 2 == 0:
            return "get_in"
        else:
            return "stay"

    def check_stay_or_get_out(self, period):
        
        if int(period.strftime("%d")) % 2 != 0:
            return "get_out"
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
    