import yaml
import os

def get_config(name):
    f = open_config_file(name)
    config = yaml.safe_load(f)
    return config

# Open config file, check config local
def open_config_file(name):
    local_file = 'config/' + name + '.local.yml'
    concrete_file = 'config/' + name + '.yml'

    if os.path.isfile(local_file):
        return open(local_file)
    elif os.path.isfile(concrete_file):
        return open(concrete_file)
    return None # Take care if the file is not exists
