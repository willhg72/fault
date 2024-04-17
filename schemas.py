from pydantic import BaseModel



class Coordenates(BaseModel):
    latitude: float
    longitude: float
    
    
class Distance(BaseModel):
    distance: float
    name: str
    
    class config:
        from_attributes = True
        #arbitrary_types_allowed = True
        #allow_population_by_field_name = True