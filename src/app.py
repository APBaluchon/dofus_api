from fastapi import FastAPI, HTTPException
from DAO.ressources_dao

app = FastAPI()

@app.get("/ressources/")
async def get_all_ressources(limit: int = 10000):
    return