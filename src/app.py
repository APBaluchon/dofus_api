from fastapi import FastAPI, HTTPException
from DAO.ressources_dao import RessourcesDao

app = FastAPI()

@app.get("/ressources/")
async def get_all_ressources(limit: int = 10000):
    return RessourcesDao().get_all_ressources(limit)

@app.get("/ressources/{id}")
async def get_ressource_by_id(id: int):
    return RessourcesDao().get_ressource_by_id(id)[0]

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)