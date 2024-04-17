import os
from dotenv import load_dotenv
from fastapi import FastAPI
from routers import distances

#cargamos las variables de ambiente 
load_dotenv()
API_URL = os.environ["API_URL"]
#print(API_URL)

#instanciarmos la app
app = FastAPI()

#creamos el router para escalabilidad
app.include_router(distances.router)






