
def inkomsten_toevoegen(inkomsten):
    try:
        bedrag = float(input("Hoeveel geld heb je ontvangen? €"))

        if bedrag > 0:
            inkomsten.append(bedrag)
            print("Inkomsten toegevoegd: €", bedrag)
        else:
            print("Het bedrag moet groter zijn dan 0.")

    except ValueError:
        print("Ongeldig bedrag! Vul een getal in.")


def uitgaven_toevoegen(uitgaven):
    try:
        bedrag = float(input("Hoeveel geld heb je uitgegeven? €"))

        if bedrag > 0:
            uitgaven.append(bedrag)
            print("Uitgave toegevoegd: €", bedrag)
        else:
            print("Het bedrag moet groter zijn dan 0.")

    except ValueError:
        print("Ongeldig bedrag! Vul een getal in.")


def saldo_berekenen(inkomsten, uitgaven):
    totaal_inkomsten = sum(inkomsten)
    totaal_uitgaven = sum(uitgaven)

    saldo = totaal_inkomsten - totaal_uitgaven

    print("Totale inkomsten: €", totaal_inkomsten)
    print("Totale uitgaven: €", totaal_uitgaven)
    print("Je saldo is: €", saldo)

def spaardoel_instellen():
    try:
        bedrag = float(input("Wat is je spaardoel? €"))

        if bedrag > 0:
            print("Je spaardoel is ingesteld op €", bedrag)
            return bedrag
        else:
            print("Het spaardoel moet groter zijn dan 0.")

    except ValueError:
        print("Ongeldig bedrag! Vul een getal in.")

    return None

def overzicht_tonen(inkomsten, uitgaven, spaardoel):
    totaal_inkomsten = sum(inkomsten)
    totaal_uitgaven = sum(uitgaven)
    saldo = totaal_inkomsten - totaal_uitgaven

    print("\n===== FINANCIEEL OVERZICHT =====")
    print("Totale inkomsten: €", totaal_inkomsten)
    print("Totale uitgaven: €", totaal_uitgaven)
    print("Huidig saldo: €", saldo)

    if spaardoel > 0:
        print("Je spaardoel: €", spaardoel)

        nog_sparen = spaardoel - saldo

        if nog_sparen > 0:
            print("Je moet nog €", nog_sparen, "sparen.")
        else:
            print("Gefeliciteerd! Je hebt je spaardoel bereikt!")
    else:
        print("Je hebt nog geen spaardoel ingesteld.")

def gegevens_opslaan(inkomsten, uitgaven, spaardoel):
    bestand = open("budget_data.txt", "w")

    bestand.write("spaardoel;" + str(spaardoel) + "\n")

    for bedrag in inkomsten:
        bestand.write("inkomsten;" + str(bedrag) + "\n")

    for bedrag in uitgaven:
        bestand.write("uitgaven;" + str(bedrag) + "\n")

    bestand.close()
    print("Je gegevens zijn opgeslagen!")

def gegevens_laden():
    inkomsten = []
    uitgaven = []
    spaardoel = 0

    try:
        bestand = open("budget_data.txt", "r")

        for regel in bestand:
            delen = regel.strip().split(";")

            if delen[0] == "spaardoel":
                spaardoel = float(delen[1])
            elif delen[0] == "inkomsten":
                inkomsten.append(float(delen[1]))
            elif delen[0] == "uitgaven":
                uitgaven.append(float(delen[1]))

        bestand.close()
        print("Je opgeslagen gegevens zijn geladen!")

    except FileNotFoundError:
        print("Nog geen opgeslagen gegevens gevonden.")

    return inkomsten, uitgaven, spaardoel


def budgetplanner():
    inkomsten, uitgaven, spaardoel = gegevens_laden()

    while True:
        print("\n===== BUDGETPLANNER =====")
        print("1. Inkomsten toevoegen")
        print("2. Uitgaven toevoegen")
        print("3. Saldo bekijken")
        print("4. Spaardoel instellen")
        print("5. Financieel overzicht")
        print("6. Stoppen")

        keuze = input("Maak je keuze: ")

        if keuze == "1":
            inkomsten_toevoegen(inkomsten)
        elif keuze == "2":
            uitgaven_toevoegen(uitgaven)
        elif keuze == "3":
            saldo_berekenen(inkomsten, uitgaven)

        elif keuze == "4":
            nieuw_spaardoel = spaardoel_instellen()

            if nieuw_spaardoel is not None:
                spaardoel = nieuw_spaardoel

        elif keuze == "5":
            overzicht_tonen(inkomsten, uitgaven, spaardoel)


        elif keuze == "6":

            gegevens_opslaan(inkomsten, uitgaven, spaardoel)

            print("Terug naar het hoofdmenu!")

            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    budgetplanner()