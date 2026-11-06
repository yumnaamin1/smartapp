
def taak_toevoegen(taken):
    taak = input("Welke taak wil je toevoegen? ")

    if taak != "":
        taken.append(taak)
        print("Taak toegevoegd:", taak)
    else:
        print("Je moet een taak invullen.")


def taken_bekijken(taken):
    if len(taken) == 0:
        print("Je hebt nog geen taken.")
    else:
        print("\n===== JOUW TAKEN =====")

        for i in range(len(taken)):
            print(i + 1, ".", taken[i])

def taak_voltooien(taken):
    if len(taken) == 0:
        print("Je hebt nog geen taken.")
        return

    taken_bekijken(taken)

    try:
        nummer = int(input("Welke taak heb je voltooid? "))

        if nummer >= 1 and nummer <= len(taken):
            taken[nummer - 1] = "[Klaar] " + taken[nummer - 1]
            print("Taak voltooid!")
        else:
            print("Dit taaknummer bestaat niet.")

    except ValueError:
        print("Vul een geldig nummer in.")

def taak_verwijderen(taken):
    if len(taken) == 0:
        print("Je hebt nog geen taken.")
        return

    taken_bekijken(taken)

    try:
        nummer = int(input("Welke taak wil je verwijderen? "))

        if nummer >= 1 and nummer <= len(taken):
            verwijderde_taak = taken.pop(nummer - 1)
            print("Taak verwijderd:", verwijderde_taak)
        else:
            print("Dit taaknummer bestaat niet.")

    except ValueError:
        print("Vul een geldig nummer in.")

def taken_opslaan(taken):
    bestand = open("taken.txt", "w")

    for taak in taken:
        bestand.write(taak + "\n")

    bestand.close()
    print("Je taken zijn opgeslagen!")

def taken_laden():
    taken = []

    try:
        bestand = open("taken.txt", "r")

        for regel in bestand:
            taak = regel.strip()
            taken.append(taak)

        bestand.close()
        print("Je opgeslagen taken zijn geladen!")

    except FileNotFoundError:
        print("Nog geen opgeslagen taken gevonden.")

    return taken

def todo_app():
    taken = taken_laden()

    while True:
        print("\n===== TODO APP =====")
        print("1. Taak toevoegen")
        print("2. Taken bekijken")
        print("3. Taak voltooien")
        print("4. Taak verwijderen")
        print("5. Stoppen")

        keuze = input("Maak je keuze: ")

        if keuze == "1":
            taak_toevoegen(taken)
        elif keuze == "2":
            taken_bekijken(taken)
        elif keuze == "3":
            taak_voltooien(taken)
        elif keuze == "4":
            taak_verwijderen(taken)
        elif keuze == "5":
            taken_opslaan(taken)
            print("Terug naar het hoofdmenu!")
            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")


if __name__ == "__main__":
    todo_app()
