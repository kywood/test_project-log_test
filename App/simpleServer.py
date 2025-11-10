import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="My FastAPI Server", version="1.0.0")




class RunID(BaseModel):
    run_id: str

@app.get("/runid", response_model= RunID , summary="Runid")
def getRunID():
    runid = RunID( run_id="run_2025-10-10T10:10:20:40" )

    return runid


def main():
    uvicorn.run("simpleServer:app", host="0.0.0.0", port=8000, reload=True)

    pass



if __name__ == '__main__':
    main()