from fastapi import FastAPI
from network.manage_admin import manage_admin

app = FastAPI()

prefix_v1 = "/api/v1"

app.include_router(router=manage_admin, prefix=prefix_v1, tags=['cognito'])

