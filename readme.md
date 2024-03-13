# Project
Project to create a NoSql database with the entire Dofus encyclopaedia, with the aim of creating an api.

# Quick Start
- Install poetry, with `pip install poetry`for instance.
- Install dependencies with `python -m poetry install`.
- Build the docker image with `docker compose build`.
- Run the app with `docker compose up`.

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

# Interaction diagram

```mermaid
sequenceDiagram
    actor U as User
    participant S as API
    participant DB as Database
    U->>DB: Read-only MongoDb credentials
    U->>S: Item request
    S->>DB: NoSql request
    DB-->>S: NoSql result
    S-->>U: Result as json
    note over U, S: Possibility to add filters
```

# Class diagram (not done yet)

```mermaid
---
title: Class diagram
---
classDiagram
    class DAO{
        +get_all_objects(**filters)
        +get_object_by_id(id: int)
    }
    class Object{
        +string name
        +int id
        +string type
        +int level
        +string description
        +string image
        +string url
        +use_scraper()
        +to_json()
    }
    class Scraper{
        +get_name()
        +get_id()
        +get_type()
        +get_level()
        +get_description()
        +get_image()
        +has_effects()
        +has_conditions()
        +has_characteristics()
    }
    class Utils{
        +get_content_page(url: string)
        +get_number_pages(category: string)
        +get_all_links_from_page(category: string, page: int)
        +get_all_links(category: string, filepath: string, starting_page: int, nb_page: int)
        +page_contains_category(category: string, soup: BeautifulSoup)
        +page_contains_tab(category: string, soup: BeautifulSoup)
        +get_category_content(category: string, soup: BeautifulSoup)
        +convert_effects_to_dict(effects: list)
        +convert_characteristics_to_dict(characteristics: list)
        +get_nth_number(text: string, number: int)
        +contains_number(text: string)
        +find_good_stat(text: string)
        +find_good_characteristics(text: string)
        +add_spaces(text: string)
    }

```