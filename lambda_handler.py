from api import router
from mangum import Mangum
import uvicorn
from config import Config

handler = Mangum(router)

if __name__ == "__main__":
    uvicorn.run(router, port=Config.PORT)