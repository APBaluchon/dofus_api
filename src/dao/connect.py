from dao.config import MONGODB_HOST, MONGODB_PORT, MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_DATABASE
from pymongo import MongoClient


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

        client_kwargs = {
            "host": self.MONGODB_HOST,
            "port": self.MONGODB_PORT,
        }

        if self.MONGODB_USERNAME:
            client_kwargs["username"] = self.MONGODB_USERNAME
        if self.MONGODB_PASSWORD:
            client_kwargs["password"] = self.MONGODB_PASSWORD

        self.client = MongoClient(**client_kwargs)
        self.db = self.client[self.MONGODB_DATABASE]

    def close(self):
        """
        Ferme la connexion à la base de données MongoDB.
        """
        self.client.close()
