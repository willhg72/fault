from fastapi import APIRouter, status, Depends
from repositories import distances
from services import util_functions
from typing import List

router = APIRouter(
    prefix='/distances',
    tags=['Distances']
)

@router.get('/', status_code=status.HTTP_200_OK)
async def calculate_distances(latitude: float,  longitude: float):
    coordinates: List[float] = [latitude, longitude]
    return distances.calculate_distances(coordinates)