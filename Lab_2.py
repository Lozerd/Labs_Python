print("Quiz")

points = 0
max_points = 100
answer_value = 25

print("2 * 2 - 4 / (8 ^ 2)?")

data = float(input())
if data == 3.975:
    print("Correct!")
    points += answer_value
else:
    print("Wrong :(")

print("Как отчество у Билла Клинтона?\n"
      "1. Джеферсон\n"
      "2. Герберт\n"
      "3. Уокер\n"
      "4. Петрович")
data = input()
if str.lower(data) == "джеферсон" or data.strip() == "1":
    print("Correct!")
    points += answer_value
else:
    print("Wrong")

print("Что такое HTML?\n"
      "1. Язык програмирования\n"
      "2. Язык разметки\n"
      "3. Help me\n"
      "4. Язык веб-вёрстки")
data = input()
if str.lower(data) == "язык разметки" or data.strip() == "2":
    print("Correct!")
    points += answer_value
else:
    print("Wrong")

print(
    "Что такое инкапсуляция?\n"
    "1. Сокрытие\n"
    "2. Переопределение полей класса\n"
    "3. Обеспечение доступа к полям класса через методы\n"
    "4. Метод определения класса")
data = input()
if str.lower("Обеспечение доступа к полям класса через методы") or data.strip() == "3":
    print("Correct!")
    points += answer_value
else:
    print("Wrong")
print(f"Вы набрали {points}/100 баллов")