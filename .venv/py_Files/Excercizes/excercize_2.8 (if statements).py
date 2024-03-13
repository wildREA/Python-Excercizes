import random

numeralis = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI"}
key = random.randint(1,6)

if key == 0 in numeralis:
    print(numeralis[0])
elif key == 1 in numeralis:
    print(numeralis[1])
elif key == 2 in numeralis:
    print(numeralis[2])
elif key == 3 in numeralis:
    print(numeralis[3])
elif key == 4 in numeralis:
    print(numeralis[4])
elif key == 5 in numeralis:
    print(numeralis[5])

print("Random integer: {0}".format(str(key)))