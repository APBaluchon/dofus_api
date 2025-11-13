"""Configuration des paramètres de connexion MongoDB.

Ce module récupère les paramètres depuis les variables d'environnement afin
d'éviter d'exposer des secrets dans le dépôt. Chaque valeur dispose d'un
fallback raisonnable pour simplifier le développement local.
"""

from __future__ import annotations

import os
from typing import Optional


def _get_env(name: str, default: Optional[str] = None) -> Optional[str]:
    """Récupère la valeur d'une variable d'environnement."""

    value = os.getenv(name)
    return value if value is not None else default


def _get_int_env(name: str, default: int) -> int:
    """Récupère une variable d'environnement entière avec un fallback sûr."""

    value = _get_env(name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


MONGODB_HOST = _get_env("MONGODB_HOST", "localhost")
MONGODB_PORT = _get_int_env("MONGODB_PORT", 27017)
MONGODB_USERNAME = _get_env("MONGODB_USERNAME")
MONGODB_PASSWORD = _get_env("MONGODB_PASSWORD")
MONGODB_DATABASE = _get_env("MONGODB_DATABASE", "dofusdb")
