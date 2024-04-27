
from fastapi import FastAPI
from routers import distances
from mangum import Mangum

#instance la app
app = FastAPI()

#Create the router for scalability purposes 
app.include_router(distances.router)

@app.get('/')
async def testing_ep():
    return {"message": "Hello World"}




