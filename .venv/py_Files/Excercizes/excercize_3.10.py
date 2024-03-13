import struct

monthLenght = {
    "January": 31,
    "Fedbruary": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

for i, v in enumerate(monthLenght):
    ageVal = list(monthLenght.values())[i]
    print(str(v) + " har " + str(ageVal) + " dage.")