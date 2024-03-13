alder = int(input("Hvor gammel er du?\n"))

if alder < 17:
    print("Du har ikke stemmeret")
elif alder == 17:
    print("Du har stemmeret om ét år.")
elif alder > 17:
    print("Du har stemmeret.")