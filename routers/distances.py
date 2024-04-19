from fastapi import APIRouter, status, Depends
from repositories import distances
import schemas
from services import util_functions
from typing import List

router = APIRouter(
    prefix='/distances',
    tags=['Distances']
)

@router.get('/', status_code=status.HTTP_200_OK)
async def calculate_distances(coordenates_lat: float,  coordenates_long: float):
    coordenates: List[float] = [coordenates_lat, coordenates_long]
    return distances.calculate_distances(coordenates)