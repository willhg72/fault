from fastapi import Query
from typing import List

# funncion para leer una lista como parametros en un HTTP Metod GET
def coordinates_dict(coordinates: List[float] = Query(...)):
    return coordinates