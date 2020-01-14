import random


class Worker(object):
    def __init__(self, id, stone, wood, architecture, decoration):
        self.id = id
        self.stone = stone
        self.wood = wood
        self.architecture = architecture
        self.decoration = decoration
        self.building_working_on = None

    @property
    def level(self):
        return self.stone + self.wood + self.architecture + self.decoration   \
    @property
    def name(self):
        if self.level == 2:
            return "Apprentice"
        elif self.level == 3:
            return "Manoeuvre"
        elif self.level == 4:
            return "Compagnon"
        elif self.level == 5:
            return "Maitre"
        return self.stone + self.wood + self.architecture + self.decoration


class Building(object):
    def __init__(self, id, stone, wood, architecture, decoration, money, victory_point, name="Undefined"):
        self.id = id
        self.name = name
        self.stone = stone
        self.wood = wood
        self.architecture = architecture
        self.decoration = decoration
        self.victory_point = victory_point
        self.money = money


class Player(object):
    def __init__(self):
        self.money = 10
        self.victory_point = 0
        self.buildings = []
        self.workers = []


class Table(object):
    def __init__(self):
        self.building_deck = [Building(1, "Le port", 2, 1, 0, 1, 8, 4), Building(2, "Le temple", 0, 2, 2, 2, 10, 3),
                              Building(3, "L'hôtel de ville'", 2, 0, 2, 2, 10, 3), Building(4, "Le forum", 2, 1, 3, 2, 12, 3),
                              Building(5, "Le temple", 0, 2, 2, 2, 10, 3), Building(6, "La forteresse", 3, 2, 2, 1, 12, 4), Building(7, "L'echoppe", 0, 1, 0, 1, 6, 1)]
        self.worker_deck = [Worker(1, 0, 0, 1, 1), Worker(2, 0, 1, 0, 1), Worker(3, 1, 1, 0, 0), Worker(4, 1, 0, 0, 1),
                            Worker(5, 0, 2, 1, 0), Worker(6, 0, 0, 3, 2), Worker(7, 0, 3, 2, 0)]
        self.building_to_be_taken = []
        self.worker_to_be_taken = []

    def take_building(self, player, building_to_be_taken_index):
        player.buildings.append(self.building_to_be_taken.pop(building_to_be_taken_index))
        self.building_to_be_taken.append(self.building_deck.pop(0))

    def take_worker(self, player, worker_to_be_taken_index):
        player.workers.append(self.worker_to_be_taken.pop(worker_to_be_taken_index))
        self.worker_to_be_taken.append(self.worker_deck.pop(0))

    def prepare(self):
        random.shuffle(self.building_deck)
        random.shuffle(self.worker_deck)
        self.building_to_be_taken.append(self.building_deck[])


def start():
    print("Starting the program")

    player1 = Player()
    player2 = Player()
    table = Table()
    print(table.building_deck)
    print(table.building_to_be_taken)
    print(player1.buildings)
    table.take_building(player1, 1)
    print(table.building_deck)
    print(table.building_to_be_taken)
    print(player1.buildings)


if __name__ == '__main__':
    start()
