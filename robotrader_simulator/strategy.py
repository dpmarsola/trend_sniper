import constants

class Strategy():
    
    def sginal_in(self, period):
        
        if int(period.strftime("%d")) % 2 != 0:
            position_type = constants.SHORT
            decision = constants.GET_IN
        else:
            position_type = constants.LONG
            decision = constants.STAY
        
        return decision, position_type

    def sginal_out(self, period):
        
        if int(period.strftime("%d")) % 2 == 0:
            decision = constants.GET_OUT
        else:
            decision = constants.STAY
            
        return decision