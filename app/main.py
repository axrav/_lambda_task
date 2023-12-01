from api import router
import uvicorn
from config import Config

if __name__ == "__main__":
    uvicorn.run(router, port=Config.PORT)
