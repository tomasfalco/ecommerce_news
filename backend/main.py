from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

NEWS_FILE = "news.json"

@app.get("/news")
def get_news():
    if not os.path.exists(NEWS_FILE):
        return {"news": []}
    with open(NEWS_FILE, "r") as f:
        news = json.load(f)
    return {"news": news} 