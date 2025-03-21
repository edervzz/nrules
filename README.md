# gentera-nrule

https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/
https://overapi.com/python
https://overapi.com/regex

-   cockies
-   local storage
-   session storage
-   casos no cubiertos con IA

Tipo de Regla: Match | Tree

Parámetros de entrada:
monto_cuota
producto

Parámetros de salida:
tasa_min
tasa_max

Se eligió _Match_, se crea 1 caso vacío

Match
caso: monto_cuota > 1000, monto_cuota < 20000, product = 'CCR'
entonces => tasa_min: 15.4, tasa_max: 17.1

SWITCH
quotationAmount > 10000 AND product = 'CCR' AND minAmount > 5000  
 => "amount": 123,"rates": {"min":12.2, "max":14}
quotationAmount > 15000 | product = 'CGC' | minAmount > 10000
=> "amount": 123,"rates": {"min":11.2, "max":13}
quotationAmount > 25000 | product = 'CGC' | minAmount > 20000
=> "amount": 123,"rates": {"min":10.1, "max":11}
ELSE
=> "amount": 123,"rates": {"min":15.4, "max":17.1}

IFELSE
IF product IN ['CCR','CM']
IF minAmount > 10000
=> "amount": 123,"rates": {"min":12.2, "max":14}
IF minAmount > 15000
=> "amount": 123,"rates": {"min":11.2, "max":14}
ELSE
=> "amount": 123,"rates": {"min":15.2, "max":17.1}
IF product IN ['CGC']
IF minAmount > 10000
=> "amount": 123,"rates": {"min":12.2, "max":14}
IF minAmount > 15000
=> "amount": 123,"rates": {"min":11.2, "max":14}
ELSE
=> "amount": 123,"rates": {"min":15.2, "max":17.1}

ELSE
=> "amount": 123,"rates": {"min":19.4, "max":19.9}

-   Hello
-   Migrate Tenant, Core
-   Create Tenant
-   Create KV
-   Save KV Item
-   Create Workflow
-   Save Rules

## Matrix

Case( Condition Group ID, KVS ID )

| Case | Condition 1 | Condition 2 | Output |
| ---- | ----------- | ----------- | -----: |
| AH34 | X = 1       | Y = 0       |   1600 |
| BD21 | X = 2       | Y = 0       |     12 |
| Cf78 | x = 3       | Y = 0       |      1 |

## New Features

-   Dockerized
-   Swagger
-   OTEL
-   CQRS
-   Multitenancy

## palettes

https://www.color-hex.com/color-palette/29876
https://www.color-hex.com/color-palette/97449

## Runner

-   Load Workflow

    -   Load Variant
    -   Load Rules
    -   Is Node

-   Perfom Validation(Variant, Rules, Is Node, Payload)

    -   If Is Node: retrieve Rule Action
    -   Return: Success/Failure + (Rule Action)

-   Performe Action
    -   If Is node: execute Rule Action
    -   else:
        -   Load Workflow Action (from Validation Success/Failure)
            -   Execute Workflow Action

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

```

## 2.2 Requirements

```bash
pip install -r .\requirements.txt
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r .\requirements.txt
pip freeze > .\requirements.txt
```

## 2.3 Otros paquetes

-   python-decouple (https://pypi.org/project/python-decouple/)

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

## 4 Vite

```bash
npm create vite
```

Luego seguir los pasos de vite

## 5 States vs Props

| states                   | props                    |
| ------------------------ | ------------------------ |
| variables de función     | argumentos de función    |
| mutables                 | inmutables               |
| si cambian, => re-render | si cambian, => re-render |

## 6 Bootstrap

Agregar esta linea en el archivo main.tsx
import 'bootstrap/dist/css/bootstrap.min.css'
<<<<<<< HEAD

## 7 librerias

Bootstrap, Tailwind, Bulma CSS
react-bootstrap, daisy ui, react bulma
=======

> > > > > > > f5be7ecff993aa42a366ac44bdf1281a0fb3934e
