from fastapi import APIRouter, status, Depends
from repositories import distances
import schemas
from services import util_functions

router = APIRouter(
    prefix='/distances',
    tags=['Distances']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=schemas.Distance)
async def calculate_distances(coordenates: schemas.Coordenates = Depends(util_functions.coordenates_dict)):
    return await distances.calculate_distances(coordenates)