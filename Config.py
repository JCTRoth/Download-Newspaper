import json

# TODO ADD FUNCTION: WRITE TO JSON FILE TO UPDATE COUNTER



class config:

    config = ""  # Config Storage

    def __init__(self):
        return

    def read_config_file(self, config_path):
        # Loads Project Config into Class Obj.
        confFile = open(config_path, "r")
        self.config = json.loads(confFile.read())
