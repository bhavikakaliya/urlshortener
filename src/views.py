from datetime import datetime
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from starlette.responses import RedirectResponse
import uuid
from .models import URLs
from .schema import URLvalidate

client = MongoClient()

db = client["shorturl"]
collection = db["shorturls"]

router = APIRouter()

@router.get("/{short_url}")
async def redirect(short_url: str):

    url = collection.find_one({"short_url": short_url})
    if url:
        return RedirectResponse(url = url["long_url"])
    else:
        raise HTTPException(status_code= 404, detail = "URL not found")
    
@router.post("/", response_model = dict)
async def shorturl(url: URLvalidate):

    url = dict(url)
    if (url["custom"]):
        if collection.find_one({"short_url": url["custom"]}):
            raise HTTPException(status_code = 400, detail = "custom url already in use")
        else:
            short_url = url["custom"]
    else:
        while True:
            short_url = uuid.ShortUUID().random(length = 5)
            if collection.find_one({"short_url": short_url}):
                continue
            else:
                break
    
    url = {"long_url" : url["long_url"], "short_url" : short_url, "created_at" : datetime.now()}
    add = collection.insert_one(url)
    return {"url" : "http://127.0.0.1:8000/" + short_url}
    

    
