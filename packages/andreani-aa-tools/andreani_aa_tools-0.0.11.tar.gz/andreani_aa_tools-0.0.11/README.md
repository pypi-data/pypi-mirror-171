# Andreani Advanced Analytics tools

## Instalar usando pip

```

pip install andreani-aa-tools

```

## Importanción

```

import aa_tools

```

## Ejemplo de uso

```

from aa_tools import logger, haversine

if __name__ == "__main__":

    log = logger("test.py", "main")

    result = haversine(-58.490160, -34.566116, -58.485096, -34.572123)

    log.log_console(f"Haversine distance: {result}", "INFO")

    log.close()

```

### Listado de funciones agregadas:

* Haversine: Distancia euclidia entre dos puntos.

* Logger: Maneja el log según los lineamientos de Andreani.

* Datalake: Interfaz de conexión al datalake para descargar y cargar archivos csv y/o parquet.


### Listado de funciones a agregar:

* División de un dataframe en una lista de dataframes para procesamiento en hilos.

* Distancia de ruta entre dos puntos.

* Model training
