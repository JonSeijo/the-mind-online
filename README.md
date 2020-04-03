# Server

## INSTALLING:

Pararse en the-mind-online
Creamos un entorno virtual donde vamos a instalar las librerias de python:

```python3.7 -m venv the-mind-venv```


Activamos el entorno virutal:
```source the-mind-venv/bin/activate```

Para saber si esta andando, deberia aparecer "(the-mind-venv)" a la izquierda del prompt.


Instalamos las librerias necesarias (importante, el venv tiene que estar activado!)
```pip install -r requirements.txt```


## RUNNIG

Cada vez que querramos usar el server tenemos que activar el entorno virtual
```source the-mind-venv/bin/activate```


Correr los tests:
```./test.sh```

Correr el type checking:
```./test.sh all```

Arrancar el server:
```./serve.sh```

El _server_ arranca en localhost:5000, se puede acceder desde el navegador


-----------------------------

# Cliente

## INSTALLING

- Instalar yarn
( https://classic.yarnpkg.com/en/docs/install/#debian-stable )

Es posible que necesites instalar "nodejs", no estoy seguro si se instala solo con yarn.

Parados en "the-mind-react", queremos instalar las dependencias especificadas en el package.json:

``` yarn install```


## RUNNIG

Parados en "the-mind-react":
``` yarn start```

Ahora podemos acceder al cliente desde localhost:3000