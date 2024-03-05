from fastapi import FastAPI, HTTPException
from DAO.object_dao import ObjectDao

app = FastAPI()

@app.get("/ressources/")
async def get_all_ressources(limit: int = 10000):
    return ObjectDao().get_all_objects(limit)

@app.get("/ressources/{id}")
async def get_ressource_by_id(id: int):
    return ObjectDao().get_object_by_id(id)[0]

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)