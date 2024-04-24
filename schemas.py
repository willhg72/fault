from pydantic import BaseModel



class coordinates(BaseModel):
    latitude: float
    longitude: float
    