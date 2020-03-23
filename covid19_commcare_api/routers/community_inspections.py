from fastapi import APIRouter


router = APIRouter()

@router.get('/id')
def get_id(id: int):
    return 1

@app.get('/GetAll')
def get_all():
    return 1

@app.get('/')
def get_record(LastRecord: int, PageSize: int):
    return 1


@app.get('/RRT')
def get_rrt(Source: str, LastRecord: int, PageSize: int):
    return 1