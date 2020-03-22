from fastapi import FastAPI

from covid19_commcare_api.routers import webhooks


app = FastAPI()
app.include_router(webhooks.router, prefix='/webhooks')


@app.get('/')
async def root():
    return 
  