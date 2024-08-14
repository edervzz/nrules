# gentera-nrule

DataDog


## 1. Crear environment
En caso de trabajar con un monorepo y VSCODE, será necesario hacer esta instalación abriendo la carpeta asignada al proyecto en Python, y luego cambiar a la carpeta del proyecto principal. Para confirmar que venv esta corriendo en la consola, abrir una terminar dentro de VSCODE y poner el mouse encima de la terminal seleccionada. 
```bash
$ python -m venv .venv
```
Luego de esto, presionar Ctrl+Shift+P y seleccionar el interprete de python, el cual sera el recien creado en nuestra carpeta _.venv_


## 2. Instalación del paquete Flask
```bash
$ pip install flask  
```

## 2.1 Requirements
```bash
pip freeze > requirements.txt
```

## 2.2 Requirements
```bash
pip install -r .\requirements.txt
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r .\requirements.txt
```

## 2.3 Otros paquetes
- python-decouple (https://pypi.org/project/python-decouple/)

## 2.4 Testing
```bash
python -m unittest -v 
```

## 2.5 selft signed
```bash
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package-name>
```

Este paquete permite usar variables de entorno en el siguiente orden jerarquico: envars(machine), settings(file), default(code)

Ejemplo de settings.ini (se ubica en la carpeta root del proyecto)
```ini
[settings]
DB_SERVER=asdf
DB_USR=eder
DB_PWD=velazquez
#COMMENTED=42
```


## 3. Punto de entrada
Crear un archivo llamado _app.py_ donde colocaremos 
```python
from flask import Flask

app = Flask(__name__)  # el archivo debe llamarse app así como esta variable

stores = [ # ejemplo de response body
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]


@app.get("/store") # decorador para verbo GET
def get_store(): # endpoint
    """_summary_"""
    return {"store": stores}
```
