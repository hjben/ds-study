from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import JSONResponse

import uvicorn

import os, gc
import json
import warnings

app = FastAPI()
warnings.filterwarnings("ignore")

def garbage_collection():
    gc.collect()

@app.post("/post")
async def post(info: Request, background_tasks: BackgroundTasks):
    req_info = await info.json()
    result = dict()
    
    # place custom variables and function
    #
    #

    background_tasks.add_task(garbage_collection)
    return JSONResponse(content=result)

@app.get('/get')
async def get():
    result = dict()
    
    # place custom variables and function
    #
    #
    
    background_tasks.add_task(garbage_collection)
    return JSONResponse(content=result)

# Run api (main)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)