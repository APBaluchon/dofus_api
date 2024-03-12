from fastapi import FastAPI, HTTPException
from DAO.ObjectDAO import ObjectDao


app = FastAPI()

@app.get("/ressources/")
async def get_all_ressources(limit: int = 10000, type: str = None, level: str = None):
    filters = {}
    if type:
        filters["type"] = type
    if level:
        filters["level"] = level

    result = ObjectDao("ressources").get_all_objects(limit=limit, **filters)
    return result

@app.get("/ressources/{id}")
async def get_ressource_by_id(id: int):
    return ObjectDao("ressources").get_object_by_id(id)[0]

@app.get("/consommables/{id}")
async def get_consommable_by_id(id: int):
    return ObjectDao("consommables").get_object_by_id(id)[0]

@app.get("/consommables/")
async def get_all_consommables(limit: int = 10000, type: str = None, level: str = None, effects: str = None):
    filters = {}
    if type:
        filters["type"] = type
    if level:
        filters["level"] = level
    if effects:
        filters["effects"] = [effects]

    result = ObjectDao("consommables").get_all_objects(limit=limit, **filters)
    return result


@app.get("/montures/{id}")
async def get_monture_by_id(id: int):
    return ObjectDao("montures").get_object_by_id(id)[0]

@app.get("/montures/")
async def get_all_montures(limit: int = 10000, effects: str = None):
    filters = {}

    if effects:
        filters["effects_monture"] = effects
    
    result = ObjectDao("montures").get_all_objects(limit, **filters)
    return result

# @app.get("/metiers/{id}")
# async def get_metier_by_id(id: int):
#     return ObjectDao("metiers").get_object_by_id(id)[0]
# 
# @app.get("/metiers/")
# async def get_all_metiers(limit: int = 10000):
#     return ObjectDao("metiers").get_all_objects(limit)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)