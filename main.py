import math
# data = int(input('Enter temperature in Fahrenheit: '))
# print("Temperature in Celsius: {:2}".format(((data * 9) / 5) + 32))

expr = [int(item) for item in input("Enter data with space: \"height\" \"bottom base\" \"top base\": ").split(" ")]
print(f"The area is: {0.5 * (expr[1] + expr[2]) * expr[0]}")

radius1 = int(input("Enter radius1: "))
print(f"Aree of a circle: {math.pi * pow(radius1, 2)}")

radius2 = int(input("Enter radius2: "))
print(f"Area of an eclipse: {math.pi * radius1 * radius2}")

height = int(input("Enter height: "))
print(f"Area of an equilateral triangle: {(pow(height, 2) * math.sqrt(3)) / 3}")

print(f"Volume of a cone: {(math.pi * pow(radius1, 2) * height) / 3}")
print(f"Volume of a sphere: {(4 * math.pi * pow(radius1, 3)) / 3}")

variables = [int(item) for item in input("Enter variables with space: \"a\" \"b\" \"C\" ").split(' ')]
print(f"Area of an arbitrary triangle: {0.5 * variables[0] * variables[1] * math.sin(variables[2])}")
# math.sin()
