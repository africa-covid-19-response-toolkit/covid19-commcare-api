from fastapi import APIRouter
from typing import List

from covid19_commcare_api.response_models import CommunityInspection
from covid19_commcare_api.fetch import fetch_door_to_door

router = APIRouter()


@router.get('/id', response_model=CommunityInspection)
def get_id(id: int):
    pass


@router.get('', response_model=List[CommunityInspection])
def get_record(LastRecord: int = 0, PageSize: int = 100):
    return fetch_door_to_door(limit=PageSize, LastRecord=offset)


@router.get('/RRT', response_model=List[CommunityInspection])
def get_rrt(Source: str, LastRecord: int, PageSize: int):
    pass
