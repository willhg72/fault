from fastapi import Query
from typing import List

# funncion para leer una lista como parametros en un HTTP Metod GET
def coordenates_dict(coordenates: List[float] = Query(...)):
    return coordenates