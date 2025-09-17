import json
import sys

class ContextLoader():

    context = {}

    def load_context(self):
        try:
            for p in sys.path:
                if p.endswith('backend'):
                    with open(f"{p}/config.json", "r") as config_file:
                        context_s = config_file.read()
                        self.context = json.loads(context_s)
                    break
        except (FileNotFoundError, json.JSONDecodeError):
            print("ERROR: File config.json does not exist or there is an Invalid JSON format in config.json.")

    def add_to_context(self, key, data):
        
        if (len(self.context) == 0):
            self.load_context()

        self.context[key] = data
        return self.context
    
class ContextHelper():
    
    def get_config_by_type(self, type):
        """
        Returns a list of parameters filtered by type.
        """
        stored_params = []
        
        data = json.loads(self.params)

        for param_obj in data["params"]:
            if param_obj.get('param_type') == type:
                stored_params.append(param_obj)

        return type, stored_params            

    def get_config_by_name_and_type(self, obj, name, type):
        """
        Returns a list of parameters filtered by name and type.
        """
        stored_params = []

        data = obj

        for param_obj in data["params"]:
            if param_obj.get('param_name') == name:
                if param_obj.get('param_type') == type:
                    stored_params.append(param_obj)
                    break
    
        return stored_params  
       
    def get_config_by_key(self, key):
        """
        Returns a list of parameters filtered by a specific key.
        """
        data = json.loads(self.params)

        return data.get(key)           
    
    def set_config_by_name_and_type(self, name, type, param_key, param_value):
        """
        Sets a specific parameter value by name and type.
        """
        data = json.loads(self.params)

        idx = 0
        for param_obj in data["params"]:
            if param_obj.get('param_name') == name and param_obj.get('param_type') == type:
                data["params"][idx][param_key] = param_value
                break
            idx += 1

        self.params = json.dumps(data, indent=2)

        return self
    
    def get_context_specific_data(self, obj, pname, ptype, *pqualifier):
        """
        Returns the specific data of a parameter filtered by name and type.
        """
        stored_params = []

        for param_obj in obj["params"]:
            if param_obj.get('param_name') == pname and param_obj.get('param_type') == ptype:
                if pqualifier:
                    qualifier_props = pqualifier[0].split('.')
                    param = param_obj.get('param_specific')
                    for prop in qualifier_props:
                        param = param.get(prop)
                    stored_params.append(param)
                break

        return stored_params[0]
