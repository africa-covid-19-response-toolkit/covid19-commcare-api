from fastapi import APIRouter
from typing import List

from covid19_commcare_api.response_models import Community
from covid19_commcare_api.fetch import fetch_patient_registration

router = APIRouter()


@router.get('/GetAll', response_model=List[Community])
def get_all():
    return fetch_patient_registration()