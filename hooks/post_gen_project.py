import os
from pathlib import Path

project_name = '{{ cookiecutter.project }}'
service_name = '{{ cookiecutter.service }}'
service_name_low = '{{ cookiecutter.serviceLow }}'

path_template = Path(os.getcwd()).joinpath('src').joinpath(service_name).joinpath('template.yaml')
data_template = path_template.read_text()
result = data_template.replace('{ ' + service_name_low + 'Id }', '{' + service_name_low + 'Id}')
path_template.write_text(result)

print('Si tienes la CLI de aws puedes ejecutar los siguientes comandos para desplegar el proyecto')

print('\nRecuerda que debes contar con un bucket s3 para almacena el codigo empaquetado')

print(
    f'1. Empaquetar el proyecto:\naws cloudformation package --template-file {os.getcwd()}/templates/master_template.yaml '
    f'--output-template-file {os.getcwd()}/tempaltes/master_template_pacakge.yaml --s3-bucket bucket-name')

print(f'Despliegue del proyecto:\n'
      f'aws cloudformation deploy --template-file {os.getcwd()}/templates/master_template_pacakge.yaml '
      f'--stack-name {project_name.lower()}-{service_name.lower()}-services  '
      f'--capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND')
