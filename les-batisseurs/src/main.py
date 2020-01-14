import random
from dataclasses import dataclass


class Worker(object):
    def __init__(self, id, stone, wood, architecture, decoration):
        self.id = id
        self.stone = stone
        self.wood = wood
        self.architecture = architecture
        self.decoration = decoration
        self.building_working_on = None

    @property
    def cost(self):
        return self.stone + self.wood + self.architecture + self.decoration

    @property
    def name(self):
        if self.cost == 2:
            return "Apprentice"
        elif self.cost == 3:
            return "Manoeuvre"
        elif self.cost == 4:
            return "Compagnon"
        elif self.cost == 5:
            return "Maitre"

    def __repr__(self):
        return "{}:{{S:{} W:{} A:{} D:{} M:{}}}".format(self.name, self.stone, self.wood, self.architecture, self.decoration, self.cost)


@dataclass(frozen=True)
class Building:
    identifier: int
    stone: int
    wood: int
    architecture: int
    decoration: int
    victory_point: int
    money: int
    name: str = "Undefined"

    # def __repr__(self):
    #     return "{}:{{S:{} W:{} A:{} D:{} VP:{} M:{}}}".format(self.name, self.stone, self.wood, self.architecture, self.decoration, self.victory_point, self.money)


class Player(object):
    def __init__(self, name="Undefined"):
        self.name = name
        self.money = 10
        self.victory_point = 0
        self.buildings = set()
        self.workers = set()

    def __repr__(self):
        return "{}\nMoney: {} Victory point: {}\nBuildings: {}\nWorkers: {}".format(self.name, self.money, self.victory_point, self.buildings, self.workers)

    def take_building(self, table, building_to_be_taken):
        self.buildings.add(table.building_to_be_taken.remove(building_to_be_taken))
        table.building_to_be_taken.append(table.building_deck.pop(0))

    def take_worker(self, table, worker_to_be_taken_index):
        self.workers.add(table.worker_to_be_taken.pop(worker_to_be_taken_index))
        table.worker_to_be_taken.append(table.worker_deck.pop(0))

   # def make_worker_working_on_building(self, worker_index, building_index):


class Table(object):
    NUMBER_OF_BUILDING_SHOWN = 5
    NUMBER_OF_WORKER_SHOWN = 5

    def __init__(self):
        self.building_deck = {Building(1, 2, 1, 0, 1, 8, 4, "Le port"),
                              Building(2, 0, 2, 2, 2, 10, 3, "Le temple"),
                              Building(3, 2, 0, 2, 2, 10, 3, "L'hôtel de ville"),
                              Building(4, 2, 1, 3, 2, 12, 3, "Le forum"),
                              Building(5, 1, 0, 1, 0, 6, 1, "La chamellerie"),
                              Building(6, 3, 2, 2, 1, 12, 4, "La forteresse"),
                              Building(7, 0, 1, 0, 1, 6, 1, "L'échoppe")}
        self.worker_deck = [Worker(1, 0, 0, 1, 1), Worker(2, 0, 1, 0, 1), Worker(3, 1, 1, 0, 0), Worker(4, 1, 0, 0, 1),
                            Worker(5, 0, 2, 1, 0), Worker(6, 0, 0, 3, 2), Worker(7, 0, 3, 2, 0)]
        self.building_to_be_taken = set()
        self.worker_to_be_taken = []
        self.prepare()

    def __repr__(self):
        str_to_return = "Building shown: "
        building_name_string = ""
        for building in self.building_to_be_taken:
            str_to_return += str(building) + " | "

        str_to_return += "\nWorker shown: "
        for worker in self.worker_to_be_taken:
            str_to_return += str(worker) + " | "
        return str_to_return

    def prepare(self):
        #random.shuffle(self.building_deck)
        #random.shuffle(self.worker_deck)
        for i in range(self.NUMBER_OF_BUILDING_SHOWN):
            self.building_to_be_taken.add(self.building_deck.pop())
        self.worker_to_be_taken.extend(self.worker_deck[:self.NUMBER_OF_WORKER_SHOWN])
        del self.worker_deck[:self.NUMBER_OF_WORKER_SHOWN]


def start():
    print("Starting the program")

    player1 = Player("Ludovic")
    player2 = Player("Sandrine")
    table = Table()
    foo = Building(1, 2, 1, 0, 1, 8, 4, name="Le port")
    foo2 = Building(2, 2, 1, 0, 1, 8, 4, name="Le port")
    print(foo == foo2)
    print(table)
    print(player1)
    player1.take_building(table, )
    player1.take_worker(table, 0)
    print(player1)


if __name__ == '__main__':
    start()
