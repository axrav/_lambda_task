from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models import User
from db import get_collection
from uuid import UUID
# router of fastapi
router = FastAPI()
# define collection
collection = get_collection()

# status endpoint
@router.get("/status")
async def status():
    try:
        return JSONResponse(status_code=200, content={"status": "OK"})
    except Exception as e:
        return handle_error(e)

# create user endpoint
@router.post("/create-user")
async def create_user(user: User):
    try:
        user_dict = user.model_dump()
        result = await collection.insert_one(user_dict)
        return JSONResponse(content={"message": "user created successfully", "user_id": str(user.user_id)}, status_code=201)
    except Exception as e:
        return handle_error(e)

# get all users endpoint
@router.get("/get-users")
async def get_users():
    try:
        users = []
        async for user in collection.find():
            user['_id'] = str(user['_id'])
            user['user_id'] = str(user['user_id'])
            users.append(user)
        return JSONResponse(status_code=200, content={"users": users})
    except Exception as e:
        return handle_error(e)

# update user endpoint
@router.put("/update-user/{user_id}")
async def update_user(user_id: str, user: User):
    try:
        user_exists = await collection.find_one({"user_id": UUID(user_id)})
        if not user_exists:
            raise HTTPException(status_code=400, detail="User does not exist")
        update_data = {key: value for key, value in dict(user).items() if key != "user_id"}
        await collection.update_one({"user_id": UUID(user_id)}, {"$set": update_data})
        return JSONResponse(status_code=200, content={"message": "User updated successfully"})
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"message": str(e.detail)})
    except Exception as e:
        return handle_error(e)

# delete user endpoint
@router.delete("/delete-user/{user_id}")
async def delete_user(user_id: str):
    try:
        user_exists = await collection.find_one({"user_id": UUID(user_id)})
        if not user_exists:
            raise HTTPException(status_code=400, detail="User does not exist")
        await collection.delete_one({"user_id": UUID(user_id)})
        return JSONResponse(status_code=200, content={"message": "User deleted successfully"})
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"message": str(e.detail)})
    except Exception as e:
        return handle_error(e)

# get user endpoint
@router.get("/get-user/{user_id}")
async def get_user(user_id: str):
    try:
        user = await collection.find_one({"user_id": UUID(user_id)})
        if not user:
            raise HTTPException(status_code=400, detail="User does not exist")
        user['_id'] = str(user['_id'])
        user['user_id'] = str(user['user_id'])
        return JSONResponse(status_code=200, content={"user": user})
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"message": str(e.detail)})
    except Exception as e:
        return handle_error(e)

# error handler for all endpoints
def handle_error(exception: Exception):
    return JSONResponse(status_code=500, content={"message": "Internal Server Error", "error": str(exception)})
