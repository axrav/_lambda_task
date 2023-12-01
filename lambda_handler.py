import uvicorn
from mangum import Mangum

from api import router
from config import Config

handler = Mangum(router)

if __name__ == "__main__":
    uvicorn.run(router, port=Config.PORT)
