# Project
Project to create a NoSql database with the entire Dofus encyclopaedia, with the aim of creating an api.

# Quick Start

- Create a `.env` file, or rename the `.env.example` file to `.env`.
- Replace the MongoDb username and password with the credentials that have been provided to you.

# Roadmap

- [x] Ressources
- [x] Consommables
- [x] Montures
- [x] Métiers
- [ ] Familiers
- [ ] Panoplies
- [x] Equipements
- [ ] Armes
- [x] Bestiaire
- [ ] Classes
- [ ] Objets d'apparat
- [ ] Compagnon
- [ ] Havres-Sacs

# Database diagram

```mermaid
erDiagram
    RESSOURCES {
        string id
        string name
        string type
        string level
        string description
        string image
    }

    MONTURES {
        string id
        string name
        json effects
        json characteristics
    }

    CONSOMMABLES {
        string id
        string name
        string type
        string level
        string description
        string image
        json effects
        json conditions
    }

    METIERS {
        string id
        string name
        string image
        string description
        json recettes
        json recoltes
    }

    EQUIPEMENTS {
        string id
        string name
        string type
        string level
        string description
        string image
        string panoplie
        json effects
        json crafts
    }

    MONSTRES {
        string id
        string name
        string race
        string zone
        json drops
        json characteristics
        json resistances
    }
```
