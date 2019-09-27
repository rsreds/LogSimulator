from .utils import read_config


class Template():
    def __init__(self):
        self.template = ['descriptor', 'descriptor', 'PARAM', ]


def generate_log():
    """Generate Log Files based on configuration"""
    config_filename = 'config.json'
    config_dict = read_config(config_filename)
    filename = config_dict['filename']
    lines = config_dict['lines']
    log_line = Template()
    with open(filename, 'w') as f:
        for i in range(lines):
            line = ""
            for element in log_line.template:
                if element == 'PARAM':
                    line = line + f'PARAM{i} '
                else:
                    line = line + element + ' '
            f.write(line + '\n')
