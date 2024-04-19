import os
from dotenv import load_dotenv
from fastapi import FastAPI
from routers import distances

#cargamos las variables de ambiente 
load_dotenv()
#print(API_URL)

#instance la app
app = FastAPI()

#creamos el router para escalabilidad
app.include_router(distances.router)






