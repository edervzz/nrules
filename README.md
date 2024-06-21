# gentera-nrule

## Variant Catalog - Catalogo de variante
Diccionario de datos para alimentar a las expresiones usando __wildcards__ evitando valores fijos.

## KVS - Valores de negocio
Diccionario de datos con infomación relevante para el negocio. Estos son usandos dentro de __contenedores__.

## Operators - Operadores
Operadores usados dentro de __conjunto de reglas__ o __contenedores__.
- Full: AND
- Partial: OR

## Rule - Regla de Negocio
Unidad minima de validación, se componene de una __expression__ y un resultado  __pass=true__.
+ Variant*
- Expression => Pass

## Rule Set - Conjunto de Reglas de Negocio
Conjunto de __reglas__ relacionadas por __operadores__ que devuelven un resultado __pass=true__ cuando se cumplen todas.
+ Variant*
- Rule + Operator + Rule ...  => Pass

## Nodo - Contenedor de Reglas
Un nodo reune __reglas__ y __conjuntos__ relacionados por __operadores__ que devuelve un __KVS__ cuando el resultado es satisfactorio __pass=true__. Se puede adjuntar una __variante__ que realizará la sustitución de las variantes que existan.
+ Variant*
- Rule + Operator + RuleSet + Operator + RuleSet ... => (Pass, KVS)

## WorkItem - Elemento de Reglas de Negocio
Un elemento de trabajo se compone de __contenedores__, __conjuntos__ y/o __reglas__ que siempre deben cumplirse el en orden configurado
Los KVS resultantes pueden combinarse, sustituirse, acumularse (en caso de números) o usarse como una __variante__ para el siguiente elemento.
Los KVS que se usen como __variante__ se suben al __colector de variante__ y se usa durante toda la ejecución del __nodo__.
El __colector de variante__ puede sustituir las __variantes__ de los componentes.
- Variant Collector
- KVS Collector
- [ ] Containers => (Pass, KVS, KVSFunc) ---> [ ] Set => Pass ---> [ ] Reglas => Pass

## Workflow - Flujo de Reglas de Negocio.
Un flujo de trabajo ejecuta __elementos de trabajo__, y resuelve el resultado de __KVS__ en conjunto de sus __KVSFunc__.
Por defecto, el workflow siempre aplicará la función de __sustitución__ sobre el __KVS__ según el orden de los __workitems__.


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
$ pip freeze > requirements.txt
```

## 2.2 Requirements
```bash
$ pip install -r .\requirements.txt
```

## 2.3 Otros paquetes
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
