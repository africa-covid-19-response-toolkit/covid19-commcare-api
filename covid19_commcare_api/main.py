from fastapi import FastAPI

from covid19_commcare_api.routers import (
    auth, community_inspections, community, 
    traveller, webhooks)


app = FastAPI()
app.include_router(webhooks.router, prefix='/api/Auth')
app.include_router(webhooks.router, prefix='/webhooks')
app.include_router(webhooks.router, prefix='/api/CommunityInspection')
app.include_router(webhooks.router, prefix='/api/Community')
app.include_router(webhooks.router, prefix='/api/Traveller')


@app.get('/')
async def root():
    return 
  