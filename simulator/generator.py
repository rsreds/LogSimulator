from .utils import read_config


def generate_log():
    config_filename = 'config.json'
    config_dict = read_config(config_filename)
    lines = config_dict['lines']
    print(f"The line to generate are: {lines}")
