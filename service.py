import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os,json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
 
@app.get('/config')
def getConfig():
    data_path = os.getcwd()+"/data/data.json"
    tmp_json = {}
    with open(data_path, 'r') as f:
        tmp_json = json.load(f)
        f.close()
    return tmp_json

@app.get("/")
async def main():
    return {"message": "Hello!"}
 
if __name__ == '__main__':
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8001,
                workers=1)