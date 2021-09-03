import random as rd

difficulty_choices = {
    "0": "Простой",
    "1": "Лёгкий",
    "2": "Нормальный",
    "3": "Сложный",
    "4": "Вам не выжить!",
}

person_to_travel = {
    0: 9,
    1: 8,
    2: 7,
    3: 6,
    4: 5,
}

native_to_travel = {
    0: rd.randint(6, 13),
    1: rd.randint(7, 14),
    2: rd.randint(8, 15),
    3: rd.randint(10, 18),
    4: rd.randint(12, 22),
}


class Person:
    def __init__(self, person_difficulty=0):
        self.alive = True
        self.distance = 0
        self.canteen_drinks = 3
        self._thirst = 0
        self._camel_alive = True
        self._camel_tiredness = 0
        self.camel_speed = 3
        self.difficulty = person_to_travel[person_difficulty]

    def go_forward(self, speed=0):
        if self._camel_alive:
            if not speed:
                miles_travelled = rd.randint(2 + self.camel_speed, 6 + (self.camel_speed * 2) + self.difficulty)
                self.distance += miles_travelled
                self._thirst += 1
                self._camel_tiredness += 1
            miles_travelled = rd.randint(7 + self.camel_speed,
                                         10 + (self.camel_speed * self.camel_speed) + 1 + self.difficulty)
            self.distance += miles_travelled
            self._thirst += 1
            self._camel_tiredness += rd.randint(1, 3)
        else:
            if not speed:
                miles_travelled = rd.randint(2, 6)
                self.distance += miles_travelled
                self._thirst += 1
                self._camel_tiredness += 1
            miles_travelled = rd.randint(7, 10)
            self.distance += miles_travelled
            self._thirst += 1
            self._camel_tiredness += rd.randint(1, 3)
        print("You traveled %i miles" % miles_travelled)

    def drink(self):
        if self.canteen_drinks > 0:
            self.canteen_drinks -= 1
            self._thirst = 0
            return print("Вы сделали 1 глоток из фляги")
        print("У вас не осталось воды во фляге")

    def sleep(self):
        print("Вы решили переночевать, ваш верблюд этому очень рад!")
        self._camel_tiredness = 0

    def check_status(self):
        if not self.distance >= 200:
            if not (goal - native.distance) <= (goal - self.distance):
                if self._thirst > 4:
                    print("Вы очень хотите пить!")
                elif self._thirst > 6:
                    print("Вы умерли от жажды!")
                    self.alive = False
                if self.alive and self._camel_alive:
                    if 5 <= self._camel_tiredness < 8:
                        print("Ваш верблюд устал")
                    elif self._camel_tiredness >= 8:
                        print("Ваш верблюд умер!")
                        self._camel_alive = False
                return self.alive
            elif (person.distance - native.distance) == 15:
                print("Коренные жители вас нагоняют!")
                return self.alive
            self.alive = False
            print("Вы проиграли, вас поймали!")
            return 0
        print("Вы пересекли великую пустыню Моби!")
        return 0

    def reset_status(self):
        self.canteen_drinks = 3
        self._thirst = 0
        self._camel_tiredness = 0

    def info(self):
        print("Дистанции пройдено:", self.distance)
        print("Осталось глотков во фляге:", self.canteen_drinks)
        print(f"Коренные жители в {person.distance - native.distance} км от вас {native.distance}")


class Native:
    def __init__(self, native_difficulty=0):
        self.distance = -20 if native_difficulty <= 2 else -8
        self.difficulty = native_difficulty

    def go_forward(self):
        self.distance += native_to_travel[self.difficulty]


person_choices = {
    "A": "Попить из фляги",
    "B": "Идти вперед с обычной скоростью",
    "C": "Идти вперед с максимальной скоростью",
    "D": "Остановиться на ночлег",
    "E": "Проверить статус",
    "Q": "Выйти."
}

goal = 200

print("Добро пожаловать в Camel!\n"
      "Вы украли верблюда, чтобы пересечь великую пустыню Моби.\n"
      "Коренные жители хотят вернуть своего верблюда и преследуют вас!\n"
      "Выживайте в походе по пустыне и убегайте от жителей.\n")

active = True

print("Выберите сложность: ")
for key, value in difficulty_choices.items():
    """ Вывод возможных вариантов сложности """
    print(f"{key}: {value}")
print("Выберите номер сложности")

difficulty = int(input())

person = Person(difficulty=difficulty)
native = Native(difficulty=difficulty)

while person.alive:
    print()
    for key, value in person_choices.items():
        """ Вывод возможных вариантов """
        print(f"{key}: {value}")
    player_input = input("Ваш выбор? ").lower()
    print()
    if player_input == "q" or player_input == "выйти":
        active = False

    oasis = rd.randint(1, 20)

    if player_input == "a":
        person.drink()
    elif player_input == "d":
        person.sleep()
        native.go_forward()
    elif player_input == "e":
        person.info()
    elif player_input == "c":
        person.go_forward(speed=1)
        native.go_forward()
        if oasis == 1:
            print("Вы нашли оазис! (Восстановление всех характеристик)")
            person.reset_status()
    elif player_input == "b":
        person.go_forward()
        native.go_forward()
        if oasis == 1:
            print("Вы нашли оазис! (Восстановление всех характеристик)")
            person.reset_status()
    else:
        print("Такого варианта нет!")
    if person.check_status() == 0:
        break
