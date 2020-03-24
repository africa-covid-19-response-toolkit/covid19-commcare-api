from fastapi import APIRouter
from typing import List

from covid19_commcare_api.response_models import Travller
from covid19_commcare_api.fetch import fetch_border_registration

router = APIRouter()


@router.get('/GetAll', response_model=List[Travller])
def get_all():
    return fetch_border_registration()