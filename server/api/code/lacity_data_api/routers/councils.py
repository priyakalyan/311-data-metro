from fastapi import APIRouter, HTTPException

from ..models import api_models as schemas
from ..models.council import Council

router = APIRouter()


@router.get("", response_model=schemas.CouncilList)
async def get_all_councils():
    result = await Council.all()
    return result


@router.get("/types/stats")
async def get_all_council_type_stats():
    result = await Council.get_all_type_stats()
    return result


@router.get("/{id}", response_model=schemas.Council)
async def get_council(id: int):
    result = await Council.one(id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return result


@router.get("/{id}/counts/open/types", response_model=schemas.TypeCountList)
async def get_council_open_requests(id: int):
    result = await Council.get_open_request_counts(id)
    return result


@router.get("/{id}/types/stats")
async def get_council_type_stats(id: int):
    result = await Council.get_type_stats(id)
    return result
