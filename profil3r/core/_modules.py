import json
import os

# Change the "report_elements" array in the config.json file
# input is an array, for exemple : ["facebook", "twitter"]
def modules_update(self, modules):
    new_config = self.config
    new_config["report_elements"] = modules

    try:
        with open(self.config["config_path"], 'w') as fp:
            json.dump(new_config, fp, indent=4)
    except Exception as e:
        print(e)

# Remove modules that do not exist
def get_report_modules(self):
    return list( set(self.config["report_elements"]) & set(list(self.config["plateform"].keys())) )