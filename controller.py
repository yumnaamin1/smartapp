def aantal_dagen(inputFile):
    try:
        bestand = open(inputFile)
    except FileNotFoundError:
        print("Het bestand", inputFile, "bestaat niet!")
        return 0

    regels = bestand.readlines()
    bestand.close()
    return len(regels) - 1


def auto_bereken(inputFile, outputFile):
    try:
        bestand = open(inputFile)
    except FileNotFoundError:
        print("Het bestand", inputFile, "bestaat niet!")
        return

    regels = bestand.readlines()
    bestand.close()

    uitvoer = open(outputFile, "w")

    for regel in regels[1:]:
        regel = regel.strip()
        delen = regel.split()

        datum = delen[0]
        aantal_personen = int(delen[1])
        setpoint = float(delen[2])
        buiten = float(delen[3])
        neerslag = float(delen[4])

        verschil = setpoint - buiten
        if verschil >= 20:
            cv_ketel = 100
        elif verschil >= 10:
            cv_ketel = 50
        else:
            cv_ketel = 0

        ventilatie = aantal_personen + 1
        if ventilatie > 4:
            ventilatie = 4

        if neerslag < 3:
            bewatering = True
        else:
            bewatering = False

        uitvoer.write(datum + ";" + str(cv_ketel) + ";" + str(ventilatie) + ";" + str(bewatering) + "\n")

    uitvoer.close()


def overwrite_settings(outputFile):
    try:
        bestand = open(outputFile)
    except FileNotFoundError:
        print("Het bestand", outputFile, "bestaat nog niet. Kies eerst optie 2.")
        return -1

    regels = bestand.readlines()
    bestand.close()

    datum = input("Welke datum wil je aanpassen? ")

    gevonden = False
    index = 0
    for i in range(len(regels)):
        delen = regels[i].strip().split(";")
        if delen[0] == datum:
            gevonden = True
            index = i

    if not gevonden:
        return -1

    print("1: CV-ketel")
    print("2: Ventilatie")
    print("3: Bewatering")
    systeem = input("Welk systeem? ")
    waarde = input("Nieuwe waarde? ")

    delen = regels[index].strip().split(";")

    if systeem == "1":
        if waarde.isdigit() and 0 <= int(waarde) <= 100:
            delen[1] = waarde
        else:
            return -3
    elif systeem == "2":
        if waarde.isdigit() and 0 <= int(waarde) <= 4:
            delen[2] = waarde
        else:
            return -3
    elif systeem == "3":
        if waarde == "0":
            delen[3] = "False"
        elif waarde == "1":
            delen[3] = "True"
        else:
            return -3
    else:
        return -3

    regels[index] = delen[0] + ";" + delen[1] + ";" + delen[2] + ";" + delen[3] + "\n"

    uitvoer = open(outputFile, "w")
    uitvoer.writelines(regels)
    uitvoer.close()

    return 0


def smart_app_controller():
    inputFile = "smart_data_in.txt"
    outputFile = "smart_data_out.txt"

    stoppen = False
    while not stoppen:
        print("1: Aantal dagen weergeven")
        print("2: Actuatoren berekenen")
        print("3: Waarde overschrijven")
        print("4: Stoppen")
        keuze = input("Keuze: ")

        if keuze == "1":
            print("Aantal dagen:", aantal_dagen(inputFile))
        elif keuze == "2":
            auto_bereken(inputFile, outputFile)
            print("Klaar! Opgeslagen in", outputFile)
        elif keuze == "3":
            resultaat = overwrite_settings(outputFile)
            if resultaat == 0:
                print("Waarde aangepast!")
            elif resultaat == -1:
                print("Datum niet gevonden!")
            elif resultaat == -3:
                print("Ongeldig systeem of ongeldige waarde!")
        elif keuze == "4":
            stoppen = True
            print("Tot ziens!")
        else:
            print("Ongeldige keuze, probeer opnieuw.")