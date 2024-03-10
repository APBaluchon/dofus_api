from fastapi import FastAPI, HTTPException
from DAO.ObjectDAO import ObjectDao

app = FastAPI()

@app.get("/ressources/")
async def get_all_ressources(limit: int = 10000, type: str = None, level: str = None):
    if type and level:
        result = ObjectDao("ressources").get_all_objects(limit = limit, type = type, level = level)
    elif type:
        result = ObjectDao("ressources").get_all_objects(limit = limit, type = type)
    elif level:
        result = ObjectDao("ressources").get_all_objects(limit = limit, level = level)
    else:
        result = ObjectDao("ressources").get_all_objects(limit = limit)
    return result

@app.get("/ressources/{id}")
async def get_ressource_by_id(id: int, type: str = None, level: int = None):
    return ObjectDao("ressources").get_object_by_id(id)[0]

@app.get("/consommables/{id}")
async def get_consommable_by_id(id: int):
    return ObjectDao("consommables").get_object_by_id(id)[0]

@app.get("/consommables/")
async def get_all_consommables(limit: int = 10000, type: str = None, level: str = None):
    if type and level:
        result = ObjectDao("consommables").get_all_objects(limit = limit, type = type, level = level)
    elif type:
        result = ObjectDao("consommables").get_all_objects(limit = limit, type = type)
    elif level:
        result = ObjectDao("consommables").get_all_objects(limit = limit, level = level)
    else:
        result = ObjectDao("consommables").get_all_objects(limit = limit)
    return result


@app.get("/montures/{id}")
async def get_monture_by_id(id: int):
    return ObjectDao("montures").get_object_by_id(id)[0]

@app.get("/montures/")
async def get_all_montures(limit: int = 10000):
    return ObjectDao("montures").get_all_objects(limit)

# @app.get("/metiers/{id}")
# async def get_metier_by_id(id: int):
#     return ObjectDao("metiers").get_object_by_id(id)[0]
# 
# @app.get("/metiers/")
# async def get_all_metiers(limit: int = 10000):
#     return ObjectDao("metiers").get_all_objects(limit)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)