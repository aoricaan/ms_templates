# {{ cookiecutter.project }} - {{ cookiecutter.service }}

Este proyecto fue generado con el template ms_templates, el cual es una forma simple de crear los siguientes recursos

## Api Gateway

[api.yaml](templates/api.yaml)

1. AWS::ApiGateway::RestApi
2. AWS::IAM::Role

[apiDeployment.yaml](templates/apiDeployment.yaml)

1. AWS::ApiGateway::Deployment
2. AWS::ApiGateway::Stage
3. AWS::ApiGateway::UsagePlan
4. AWS::ApiGateway::ApiKey
5. AWS::ApiGateway::UsagePlanKey

[layers.yaml](templates/layers.yaml)
1. AWS::Lambda::LayerVersion

[template.yaml](src/%7B%7B%20cookiecutter.service%20%7D%7D/template.yaml)
1. AWS::IAM::Role
2. AWS::Serverless::Function (x4)
3. AWS::ApiGateway::Resource (x2)
4. AWS::ApiGateway::Method (x5)


Estructura del proyecto
```text
{{ cookiecutter.project }}/
├── src/
│   ├── {{ cookiecutter.service }}/
│   │   ├── get/
│   │   │   ├──__init__.py
│   │   │   └── lambda_handler.py
│   │   ├── post/
│   │   │   ├──__init__.py
│   │   │   └── lambda_handler.py
│   │   ├── put/
│   │   │   ├──__init__.py
│   │   │   └── lambda_handler.py
│   │   ├── delete/
│   │   │   ├──__init__.py
│   │   │   └── lambda_handler.py
│   │   └── template.yaml
│   ├── layers/
│   │   └── utils/
│   │       └── python/
│   │           └── core/
│   │               ├──__init__.py
│   │               └── utils.py
├── templates/
│   ├── api.yaml
│   ├── apiDeployment.yaml
│   ├── layers.yaml
│   └── master_template.yaml
├── README.md

```