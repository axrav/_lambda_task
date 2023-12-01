from fastapi import FastAPI
from fastapi.responses import JSONResponse

router = FastAPI()

# get status of the api
@router.get("/status")
async def status():
    return JSONResponse(status_code=200, content={"status": "OK"})

# get all users
@router.get("/get-users")
async def get_users():
    return JSONResponse(status_code=200, content={"users": "users"})

# create a new user
@router.post("/create-user")
async def create_user():
    return JSONResponse(status_code=201, content={"status": "created"})

# update a specific user by user_id
@router.put("/update-user/{user_id}")
async def update_user(user_id: int):
    return JSONResponse(status_code=200, content={"user_id": user_id})

# delete a specific user by user_id
@router.delete("/delete-user/{user_id}")
async def delete_user(user_id: int):
    return JSONResponse(status_code=200, content={"user_id": user_id})

# get a specific user by user_id
@router.get("/get-user/{user_id}")
async def get_users(user_id: int):
    return JSONResponse(status_code=200, content={"user_id": user_id})


    