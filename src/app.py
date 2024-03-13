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

@app.get("/monstres/")
async def get_all_monstres(limit: int = 10000, zone: str = None, race:str = None, drops: str = None):
    filters = {}

    if zone:
        filters["zone"] = zone
    if race:
        filters["race"] = race
    if drops:
        filters["drops"] = [drops]
    result = ObjectDao("monstres").get_all_objects(limit, **filters)
    return result
    
@app.get("/monstres/{id}")
async def get_minstre_by_id(id: int):
    return ObjectDao("monstres").get_object_by_id(id)[0]

@app.get("/metiers/{id}")
async def get_metier_by_id(id: int):
    return ObjectDao("metiers").get_object_by_id(id)[0]

@app.get("/metiers/")
async def get_all_metiers(limit: int = 10000, recette: str = None, recolte: str = None):
    filters = {}

    if recette:
        filters["recette"] = [recette]
    if recolte:
        filters["recolte"] = [recolte]
    return ObjectDao("metiers").get_all_objects(limit, **filters)

@app.get("/equipements/{id}")
async def get_metier_by_id(id: int):
    return ObjectDao("equipements").get_object_by_id(id)[0]

@app.get("/equipements/")
async def get_all_metiers(limit: int = 10000, level: str = None, panoplie: str = None, effect: str = None, craft: str = None):
    filters = {}

    if level:
        filters["level"] = level
    if panoplie:
        filters["panoplie"] = panoplie
    if effect:
        filters["effects"] = [effect]
    if craft:
        filters["crafts"] = [craft]
    return ObjectDao("equipements").get_all_objects(limit, **filters)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)