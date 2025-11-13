from __future__ import annotations

import threading
from typing import Any, Dict

from dao.config import (
    MONGODB_DATABASE,
    MONGODB_HOST,
    MONGODB_PASSWORD,
    MONGODB_PORT,
    MONGODB_URI,
    MONGODB_USERNAME,
)
from pymongo import MongoClient


_CLIENT_LOCK = threading.Lock()
_CLIENT: MongoClient | None = None


def _build_client_kwargs() -> Dict[str, Any]:
    """Construit les paramètres de connexion en fonction de la configuration."""

    if MONGODB_URI:
        return {"host": MONGODB_URI}

    kwargs: Dict[str, Any] = {
        "host": MONGODB_HOST,
        "port": MONGODB_PORT,
    }

    if MONGODB_USERNAME:
        kwargs["username"] = MONGODB_USERNAME
    if MONGODB_PASSWORD:
        kwargs["password"] = MONGODB_PASSWORD

    return kwargs


def _get_client() -> MongoClient:
    """Retourne un client MongoDB partagé pour l'ensemble du processus."""

    global _CLIENT
    if _CLIENT is None:
        with _CLIENT_LOCK:
            if _CLIENT is None:
                _CLIENT = MongoClient(**_build_client_kwargs())
    return _CLIENT


def reset_client() -> None:
    """Ferme et réinitialise le client MongoDB mis en cache."""

    global _CLIENT
    with _CLIENT_LOCK:
        if _CLIENT is not None:
            _CLIENT.close()
            _CLIENT = None


class Connect:
    """
    Cette classe initialise une connexion à une base de données MongoDB.

    Attributes:
        MONGODB_HOST (str): L'hôte MongoDB.
        MONGODB_PORT (int): Le port MongoDB.
        MONGODB_USERNAME (str): Le nom d'utilisateur MongoDB.
        MONGODB_PASSWORD (str): Le mot de passe MongoDB.
        MONGODB_DATABASE (str): La base de données MongoDB.

    Methods:
        __init__(): Initialise la connexion à la base de données MongoDB en utilisant les paramètres spécifiés.
        close(): Ferme la connexion à la base de données MongoDB.
    """
    def __init__(self):
        """
        Initialise la connexion à la base de données MongoDB en utilisant les paramètres spécifiés.
        """
        self.MONGODB_HOST = MONGODB_HOST
        self.MONGODB_PORT = MONGODB_PORT
        self.MONGODB_USERNAME = MONGODB_USERNAME
        self.MONGODB_PASSWORD = MONGODB_PASSWORD
        self.MONGODB_DATABASE = MONGODB_DATABASE

        self.client = _get_client()
        self.db = self.client[self.MONGODB_DATABASE]

    def close(self):
        """
        Ferme la connexion à la base de données MongoDB.
        """
        reset_client()
