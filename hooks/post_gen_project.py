import os
from pathlib import Path

project_name = '{{ cookiecutter.project }}'
service_name = '{{ cookiecutter.service }}'
service_name_low = '{{ cookiecutter.serviceLow }}'

path_template = Path(os.getcwd()).joinpath('src').joinpath(service_name).joinpath('template.yaml')
data_template = path_template.read_text()
result = data_template.replace('{ ' + service_name_low + 'Id }', '{' + service_name_low + 'Id}')
path_template.write_text(result)
