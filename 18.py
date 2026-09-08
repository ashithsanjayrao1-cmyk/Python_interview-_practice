from fastapi import FastAPI, Depends,HTTPException,Header

app = FastAPI()

def verify_api_key(api_key: str = Header(None)):
    if api_key != "super-secret":
        raise HTTPException(status_code = 403, detail = "Forbidden: Invalid API Key")

    return api_key

@app.get("/secure-data")
async def get_secure_data(key: str = Depends(verify_api_key)):
    return{"message":"Access granted!","used_key": key}

