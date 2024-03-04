from GameEntity import GameEntity

class RessourceEntity(GameEntity):
    def __init__(self, url: str):
        super().__init__(url)

if __name__ == "__main__":
    url = "https://www.dofus.com/fr/mmorpg/encyclopedie/ressources/13917-cervelle-peunch"
    item = RessourceEntity(url)
    print(item.get_name())
    print(item.get_id())
    print(item.get_type())
    print(item.get_level())
    print(item.get_description())
    print(item.get_image())