from fastapi import FastAPI

from covid19_commcare_api.routers import (
    auth, community_inspections, community, 
    traveller)


app = FastAPI()
app.include_router(auth.router, prefix='/api/Auth')
app.include_router(community_inspections.router,
                   prefix='/api/CommunityInspections')
app.include_router(community.router, prefix='/api/Community')
app.include_router(traveller.router, prefix='/api/Travllers')