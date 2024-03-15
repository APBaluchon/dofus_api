# Project
Project to create a NoSql database with the entire Dofus encyclopaedia, with the aim of creating an api.

# Quick Start
> :warning: You will need to have Docker installed and might need to run the docker commands with administrator privileges.

- Install poetry, with `pip install poetry`for instance.
- Install dependencies with `python -m poetry install`.
- Build the docker image for the database with `docker compose build`.
- Run the database with `docker compose up -d`.
- Run the app with `python src/app.py`.

When the app is running, you can find the API swagger on [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)

Once you're done using the app, you can run `docker compose down` to stop the docker container running the Mongo database. 

# How to use the app

Once you're on the swagger, you can get data from several categories of the Dofus game, which you can filter (all the filters available are listed in the swagger).

Let's say you're looking for a monster which drops some "Viande Goûtue", go on [http://0.0.0.0:8000/monstres/?drops=Viande%20Go%C3%BBtue](http://0.0.0.0:8000/monstres/?drops=Viande%20Go%C3%BBtue) to know what monster to farm to get your meat.

Now you're someone busy and you don't have time to go far away for your meat, you can also add a filter on the area to know where to find some tasteful meat in your area: [http://0.0.0.0:8000/monstres/?drops=Viande%20Go%C3%BBtue&zone=Temple%20de%20Kerubim](http://0.0.0.0:8000/monstres/?drops=Viande%20Go%C3%BBtue&zone=Temple%20de%20Kerubim)

# Run tests

You can run the project's tests with `python -m unittest discover src`.

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

# Interaction diagram

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