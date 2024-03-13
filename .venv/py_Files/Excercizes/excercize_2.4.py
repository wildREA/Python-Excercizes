alder = int(input("Hvor gammel er du?\n"))

if alder < 0 or alder > 130:
    print("Error 400 (Bad request) - alder.Exception cannot process due to an invalid value.")
elif alder < 18:
    print("Du får ungdomsrabat.")
elif int(alder) in range(18, 65):
    print("Du får ingen rabat.")
else:
    print("Du får pensionistrabat.")