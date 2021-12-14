n = int(input("Введите значение стороны квадрата: "))
side = "0" * n * 2
print(side)
for i in range(n - 2):
    print(side[0], side.replace("0", " ")[2:-2], side[-1])
print(side)

print("\n\n\n")

side = [1 + i * 2 for i in range(n)]
spaces = " " * (len(str(max(side))) + 1)
print(len(spaces))
for i in range(len(side)):
    for j in side[i:]:
        print(j, end=spaces[1:])
    if len(side[i:]) < len(side) and i < 7:
        print(spaces * i * 2, end="")
    # else:
    #     print("   " * i * 2, end="")
    for k in reversed(side[i:]):
        print(k, end=spaces[1:])
    if i != len(side) - 1:
        print()

side = list(reversed(side))
for h in range(len(side) + 1):
    for a in reversed(side[:h]):
        print(a, end=" ")
    if len(side[:h]) < len(side) + 1 and h < 5:
        print(spaces * (len(side) + 1 - h) * 2, end="")
    # else:
    #     print("  " * (len(side) - h) * 2, end="")

    for b in side[:h]:
        print(b, end=" ")

    print()
