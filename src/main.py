from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from router import router
from logger import logger
import os
from dotenv import load_dotenv

load_dotenv()

limiter = Limiter(key_func=get_remote_address)
PORT = os.getenv("PORT")

app = FastAPI()
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], #add frontend origin, allows all origins as of now
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["X-API-KEY"],
)
app.include_router(router)

@app.get("/")
def health_check():
    logger.info("Server is running on port: "+ str(PORT))
    return {"status" : "FastAPI service is running", "port": PORT}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)