from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from controller.users_controllers import UsersController

manage_admin = APIRouter(prefix='/admin')

@manage_admin.get('/list-users')
async def list_users():
    users = UsersController.list_users()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(users))
