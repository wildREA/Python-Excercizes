import struct

dict = {"Søren": 30, "Niels": 31, "Anders": 32}

for i, v in enumerate(dict):
    ageVal = list(dict.values())[i]
    print(str(v) + " er " + str(ageVal) + " år gammel.")