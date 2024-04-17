
#from geopy.distance import geodesic
from fastapi import HTTPException, status
from schemas import Coordenates as CoordenatesSchema

async def calculate_distances(coordenates):
    try:
        res =  CoordenatesSchema(latitude=7.918843016917235, longitude=-72.49822232488799)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error en calculate_distances")
        res = None
    return dict({'distance': 100.1,
                 'name': 'San Andres'})