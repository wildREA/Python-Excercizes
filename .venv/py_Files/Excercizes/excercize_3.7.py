values = "Peter", "Niels", "Mikkel", "Flemming", "Hans", "Nikolaj"

# names
# -----------------
nameList = []

while nameList == []:
    nameList.extend(values)
print(str(nameList) + "\n")

print("Sorting...\n")

sortedList = sorted(nameList)
print("Alphabetical\n" + str(sortedList))