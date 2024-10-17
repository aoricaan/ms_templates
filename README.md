## SM TEMPLATE


## Project Structure

```text
cookiecutter-template/
├── cookiecutter.json
├── {{ cookiecutter.proyecto }}/
│   ├── src/
│   │   ├── {{ cookiecutter.service }}/
│   │   │   ├── get/
│   │   │   │   └── lambda_handler.py
│   │   │   ├── post/
│   │   │   │   └── lambda_handler.py
│   │   │   ├── put/
│   │   │   │   └── lambda_handler.py
│   │   │   ├── delete/
│   │   │   │   └── lambda_handler.py
│   │   │   └── template.yaml
│   │   ├── layers/
│   │   │   └── utils/
│   │   │       └── python/
│   │   │           └── core/
│   │   │               └── utils.py
│   ├── templates/
│   │   ├── api.yaml
│   │   ├── apiDeployment.yaml
│   │   └── master_template.yaml

```
