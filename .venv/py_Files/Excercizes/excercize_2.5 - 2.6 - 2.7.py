MYNDIG = 18 # const var
alder = int(input("Angiv alder.\n"))


# method #1
if alder != MYNDIG:
    print("Alder er ikke 18 år.")
else:
    print("Alder er 18 år.")

# method #2
if alder == 18: # if statements require double equality signs (error given otherwise)
    print("Alder er 18 år.")
else:
    print("Alder er ikke 18 år.")