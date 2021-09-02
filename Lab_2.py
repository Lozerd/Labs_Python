print("Quiz")

points = 0
max_points = 100
right_answer_value = 25

print("2 * 2 - 4 / (8 ^ 2)?", end="")

if int(input()) == 3.975:
    print("Correct!")
    points += right_answer_value
else:
    print("Wrong :(")

print("Как зовут Билла Клинтона?")
data = input()
if str.lower(data) == "bill" or str.lower(data) == "билл":
    print("Correct")
