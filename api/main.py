from fastapi import FastAPI
from typing import Optional
from disruptAI import base
import res

app = FastAPI(
    title=res.title,
    description=res.description,
    version=res.version,
    openapi_url=None
)

@app.get("/")
async def index():
    return {"Error": "No routing provided"}

@app.get("/{apiKey}/{model}/{usageType}")
async def request(apiKey: str, model: str, usageType: str, query: Optional[str] = None, options: Optional[str] = None):
    return {"API": apiKey, "Model Name": model, "useCase": usageType, "options": options, "query": query}