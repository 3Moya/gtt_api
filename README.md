# Chatbot para nuestro cliente gTt-VIH
Este proyecto consiste en un chatbot implementado con Python y Flask, que utiliza una base de datos en Firebase para almacenar las preguntas y respuestas de los usuarios, y una imagen Docker para facilitar su despliegue en AWS EC2, petición de la organización gTt que nos permitio involucrarnos de lleno en un proyecto social para dar voz y visbilidad a este colectivo.

Hemos creado una Base de Datos propia con los datos visuales de la misma pagina de ![gTt-Vih](http://gtt-vih.org/), esos datos nos han servido para hacer un end-to-end con el usuario, dando una respuesta a la pregunta realizada por el usuario y devolviendo articulos relacionados con la pregunta.

## Instalación

``` git clone https://github.com/gtt-data/gtt_api.git```

### Descarga la imagen desde DockerHub

Con el Docker desktop inicializado, ejecuta en la terminal:
1. Crear un archivo en el repositorio, con esta estructura:
``` OPENAI_KEY="API-KEY-personal" ```
2. docker pull 3moya/gtt
3. docker run -tp 5000:5000 --name gtt --env-file .env 3moya/gtt

###  Visualización Web server
Accede a nuestra aplicación web a traves de este link con esta estructura:

``` ec2-3-128-94-58.us-east-2.compute.amazonaws.com:5000 ```
# Uso
El chatbot responde a las preguntas que los usuarios envían en formato JSON a través de una petición POST a la ruta /chat del servidor Flask, que lo puede ejecutar tanto con POSTMAN o cualquier otro software alternativo.

El formato esperado de la petición es el siguiente:

{
    "question": "¿Cuál es la capital de España?",
    "user_id": "123456"
}

El chatbot responderá con un JSON que incluye la respuesta a la pregunta, una lista de recomendaciones de lectura relacionadas y una lista de formas de contacto para más información.

# Estructura del repositorio

``` 
├── Dockerfile
├── README.md
├── arbol_de_carpetas.txt
├── requirements.txt
└── src
    ├── app.py
    ├── data
    │   └── category_embedding_cache.pkl
    ├── schemas
    │   └── chat_request_schema.json
    └── utils
        ├── firebase.py
        └── openai.py
```

# Librerias necesarias para el proyecto
```
from flask import Flask, request, jsonify
import json
import jsonschema
from jsonschema import validate
from utils import openai, firebase
----------------------------------
import firebase_admin
from firebase_admin import credentials, firestore
------------------------------------------
import openai
import os
import pickle
import pandas as pd
from utils import firebase
from openai.embeddings_utils import (
    get_embedding,
    distances_from_embeddings,
    indices_of_nearest_neighbors_from_distances)
```