
from fastapi import FastAPI
from routers import distances

#instance la app
app = FastAPI()

#Create the router for scalability purposes 
app.include_router(distances.router)






