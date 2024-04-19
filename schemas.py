from pydantic import BaseModel



class Coordenates(BaseModel):
    latitude: float
    longitude: float
    