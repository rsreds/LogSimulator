import random
from .utils import read_config


class Template():
    """Template class"""
    # Constructors

    def __init__(self):
        ran = random.randint(3, 7)
        lista = []
        for i in range(ran):
            dp = random.randint(0, 1)
            if dp == 0:
                lista.append(f'descriptor{i}')
            else:
                lista.append(f'PARAM')
        self.template = lista

    # Methods
    def write_line(self):
        """Print line based on template"""
        string = ""
        for i, t in enumerate(self.template):
            if t == 'PARAM':
                string = string + f'PARAM{i}' + ' '
            else:
                string = string + t + ' '
        return string.rstrip()


def generate_templates(params):
    """Generate templates by on configuration file"""
    n = params['templates']
    templates = []
    for i in range(n):
        t = Template()
        templates.append(t)
    return templates


def select_template(template_list):
    """Select template to use for next line"""
    n = len(template_list)
    rnd = random.randint(0, n-1)
    return template_list[rnd]


def generate_log():
    """Generate Log Files"""
    config_filename = 'config.json'
    config_dict = read_config(config_filename)

    filename = config_dict['filename']
    lines = config_dict['lines']

    templates = generate_templates(config_dict)

    with open(filename, 'w') as f:
        for i in range(lines):
            t = select_template(templates)
            s = t.write_line()
            f.write(s + '\n')
