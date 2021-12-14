import json


def R_x(**kwargs):
    return round(kwargs.pop('Rm', '') * (kwargs.pop('l1', '') / kwargs.pop('l2', '')), 2)


def dR_x(rx, **kwargs):
    Rm = kwargs.pop('Rm', '')
    dRm = 0.01
    dL = 0.5
    l1, l2 = kwargs.pop('l1', ''), kwargs.pop('l2', '')
    return round(((dRm / Rm) + (dL / l1) + (dL / l2)) * rx, 2)


with open("Resistance2.json", "r") as file:
    data = json.load(file)
print(data)
with open("Resistance2_results.txt", "w+", encoding="utf-8-sig") as file:
    for key, values in data.items():
        file.write(f"{key}\n")
        file.write(" \tValues: %s" % dict(**values))
        Rx = R_x(**values)
        file.write(" \tRx: %s" % Rx)
        instumental_error = dR_x(Rx, **values)
        file.write(" \tInstrError: %s\n" % instumental_error)
    a = {
        1: {1: 1.18, 2: 1.43, 3: 1.16},
        2: {1: 2.1, 2: 2.12, 3: 2.11},
        3: {1: 3.2, 2: 3.24, 3: 3.24},
        4: {1: 0.78, 2: 0.78, 3: 0.72}
    }

    h = []
    for key, value in a.items():
        file.write("Промежуточные: %.2f\n" % (sum(value.values()) / 3))
        h.append(sum([abs(sum(value.values()) / 3 - i) for i in value.values()]))
    print(h)
    for key, value in zip(range(1, len(data.keys()) + 1), h):
        file.write("Относительная погрешность %d: %.2f\n" % (key, value))
