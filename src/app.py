"""Application FastAPI exposant les objets Dofus."""

from typing import Dict, Optional

from fastapi import FastAPI, HTTPException

from dao.object_dao import ObjectDao


app = FastAPI()


def _build_filters(**kwargs: Optional[str]) -> Dict[str, str]:
    """Nettoie les filtres en supprimant les valeurs nulles."""

    return {key: value for key, value in kwargs.items() if value is not None}


def _get_object_or_404(category: str, object_id: str):
    """Retourne un document unique ou lève une 404 s'il est absent."""

    document = ObjectDao(category).get_object_by_id(object_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Objet introuvable")
    return document


@app.get("/ressources/")
async def get_all_ressources(limit: int = 10000, type: Optional[str] = None, level: Optional[str] = None):
    filters = _build_filters(type=type, level=level)
    return ObjectDao("ressources").get_all_objects(limit=limit, **filters)


@app.get("/ressources/{id}")
async def get_ressource_by_id(id: str):
    return _get_object_or_404("ressources", id)


@app.get("/consommables/{id}")
async def get_consommable_by_id(id: str):
    return _get_object_or_404("consommables", id)


@app.get("/consommables/")
async def get_all_consommables(
    limit: int = 10000,
    type: Optional[str] = None,
    level: Optional[str] = None,
    effects: Optional[str] = None,
):
    filters = _build_filters(type=type, level=level, effects=effects)
    return ObjectDao("consommables").get_all_objects(limit=limit, **filters)


@app.get("/montures/{id}")
async def get_monture_by_id(id: str):
    return _get_object_or_404("montures", id)


@app.get("/montures/")
async def get_all_montures(limit: int = 10000, effects: Optional[str] = None):
    filters = _build_filters(effects_monture=effects)
    return ObjectDao("montures").get_all_objects(limit, **filters)


@app.get("/monstres/")
async def get_all_monstres(
    limit: int = 10000,
    zone: Optional[str] = None,
    race: Optional[str] = None,
    drops: Optional[str] = None,
):
    filters = _build_filters(zone=zone, race=race, drops=drops)
    return ObjectDao("monstres").get_all_objects(limit, **filters)


@app.get("/monstres/{id}")
async def get_minstre_by_id(id: str):
    return _get_object_or_404("monstres", id)


@app.get("/metiers/{id}")
async def get_metier_by_id(id: str):
    return _get_object_or_404("metiers", id)


@app.get("/metiers/")
async def get_all_metiers(limit: int = 10000, recette: Optional[str] = None, recolte: Optional[str] = None):
    filters = _build_filters(recette=recette, recolte=recolte)
    return ObjectDao("metiers").get_all_objects(limit, **filters)


@app.get("/equipements/{id}")
async def get_equipement_by_id(id: str):
    return _get_object_or_404("equipements", id)


@app.get("/equipements/")
async def get_all_equipements(
    limit: int = 10000,
    level: Optional[str] = None,
    type: Optional[str] = None,
    panoplie: Optional[str] = None,
    effect: Optional[str] = None,
    craft: Optional[str] = None,
):
    filters = _build_filters(level=level, type=type, panoplie=panoplie, effects=effect, crafts=craft)
    return ObjectDao("equipements").get_all_objects(limit, **filters)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
