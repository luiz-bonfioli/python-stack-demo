# from mangum import Mangum

from src.application.controller import app
from src.core.common.config import WEB_SERVER_HOST, WEB_SERVER_PORT
#
# api_handler = Mangum(app)

# To run locally
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)
