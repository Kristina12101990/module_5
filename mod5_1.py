class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        self.new_floor = new_floor
        n=0
        for i in range(new_floor):
            n += 1
            print(n)
        if new_floor > self.number_of_floors or new_floor < 1:
                print("Такого этажа нет")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

