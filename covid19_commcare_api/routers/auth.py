from fastapi import APIRouter

from covid19_commcare_api.response_models import (
    AuthenticateVm, 
    CovidAuthenticateResult)

router = APIRouter()


@router.post('', response_model=CovidAuthenticateResult)
def root(auth: AuthenticateVm):
    pass