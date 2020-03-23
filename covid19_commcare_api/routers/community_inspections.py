from fastapi import APIRouter


router = APIRouter()

@router.get('/id')
def get_id(id: int):
    pass

@app.get('/GetAll')
def get_all():
    pass

@app.get('/')
def get_record(LastRecord: int, PageSize: int):
    pass


@app.get('/RRT')
def get_rrt(Source: str, LastRecord: int, PageSize: int):
    pass