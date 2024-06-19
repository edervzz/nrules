# gentera-nrule

## KVS - Almacenamientos de datos tipo Llave-Valor
Almacenamiento de datos para usarlo dentro de las expresiones con _wildcards_. Permiten que las reglas no tengan _hardcoded values_. 
- Diccionario de datos

## Data Business - Almacenamiento de Valores relevante para el negocio
Resultado de las reglas de negocio siendo valores relevantes para los procesos de negocio.
- Modo protegido
- Funciones: Insertar/Agregar, Primero Borrar
- Cache

## Operators - Operadores
Operadores usados dentro de Conjunto de reglas
- Full: AND
- Partial: OR
- Just One: XOR

## Business Rule - Regla de Negocio
Unidades minima de validación de negocio. Requieren una expresión y un KVS opcional. Además del resultado, pueden regresar Data Busines en modo protegido y su función de tratamiento.
- Expresión
- Resultado (IsTrue)
- [ ]KVS
### Resultado
- [ ]Data Businesss

## Set Of Business Rule - Conjunto de reglas de negocio
Conjunto de reglas de validacion de negocio enumeradas. Combinan 2 o más reglas y requiere de un Operador global o interno. Adicionalmente usa un colector de Data Business para las reglas así como su propio Data Business.
- Enumaradores
- [ ]Rule
- [ ]KVS
- Operator | Inner Operators
- Data Business Collector
### Resultado
- Data Business Collector + [ ]Data Business

## Workflow - Flujos para reglas de negocio
El workflow siempre derivara en la primer regla/set que se cumpla.
- [ ] Set BR | Rule
- [ ]KVS
- Data Business Collector
### Resultado
- Data Business Collector + [ ]Data Business

## Workflow Container - Contenedor de Flujos para reglas de negocio
Contenedor de Workflows. Luego de terminar con un workflow pasa al siguiente.
- [ ] WF
- Data Business Collector
### Resultado
- Data Business Collector

## 1. Crear enviroment
En caso de trabajar con un monorepo y VSCODE, será necesario hacer esta instalación abriendo la carpeta asignada al proyecto en Python, y luego cambiar a la carpeta del proyecto principal. Para confirmar que venv esta corriendo en la consola, abrir una terminar dentro de VSCODE y poner el mouse encima de la terminal seleccionada. 
```bash
$ python -m venv .venv
```
Luego de esto, presionar Ctrl+Shift+P y seleccionar el interprete de python, el cual sera el recien creado en nuestra carpeta _.venv_


## 2. Instalación del paquete Flask
```bash
$ pip install flask  
```

## 2.1 Otros paquetes
- python-decouple (https://pypi.org/project/python-decouple/)

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
