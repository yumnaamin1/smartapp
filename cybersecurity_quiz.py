

def vragen_stellen():
    vragen = [
        ["Wat is phishing?", "Een computer sneller maken", "Persoonlijke gegevens proberen te stelen", "Een programma installeren", "B"],
        ["Wat is een sterk wachtwoord?", "123456", "Welkom123", "Een lang en uniek wachtwoord", "C"],
        ["Wat doet een firewall?", "Netwerkverkeer controleren", "Bestanden verwijderen", "Internet sneller maken", "A"],
        ["Wat is malware?", "Een beveiligingsupdate", "Schadelijke software", "Een veilige website", "B"],
        ["Wat betekent 2FA?", "Twee computers gebruiken", "Twee wachtwoorden opslaan", "Inloggen met twee verificatiestappen", "C"],
        ["Wat is een VPN?", "Een beveiligde verbinding", "Een antivirusprogramma", "Een harde schijf", "A"],
        ["Wat is ransomware?", "Software die bestanden gijzelt", "Een veilige back-up", "Een browser", "A"],
        ["Waarom zijn updates belangrijk?", "Ze veranderen je wachtwoord", "Ze verhelpen beveiligingsproblemen", "Ze verwijderen internet", "B"],
        ["Wat betekent HTTPS?", "Een website zonder beveiliging", "Een soort virus", "Een versleutelde verbinding met een website", "C"],
        ["Wat is social engineering?", "Mensen misleiden om informatie te krijgen", "Een sociaal netwerk bouwen", "Een computer repareren", "A"]
    ]

    score = 0

    for vraag in vragen:
        print("\nVraag:", vraag[0])
        print("A.", vraag[1])
        print("B.", vraag[2])
        print("C.", vraag[3])

        antwoord = input("Jouw antwoord (A/B/C): ").upper()

        if antwoord == vraag[4]:
            print("Goed antwoord! +1 punt")
            score = score + 1
        else:
            print("Fout! Het juiste antwoord is:", vraag[4])

    return score

def score_tonen(score):
    print("\n===== QUIZ RESULTAAT =====")
    print("Je eindscore is:", score, "van de 10")

    if score >= 8:
        print("Uitstekend! Je weet veel over cybersecurity!")
    elif score >= 5:
        print("Goed gedaan! Je hebt al wat kennis.")
    else:
        print("Blijf oefenen! Je kunt nog veel leren.")

def score_opslaan(score):
    bestand = open("quiz_scores.txt", "a")

    bestand.write("Score: " + str(score) + " van de 10\n")

    bestand.close()
    print("Je score is opgeslagen!")

def cybersecurity_quiz():
    score = 0

    while True:
        print("\n===== CYBERSECURITY QUIZ =====")
        print("1. Quiz starten")
        print("2. Stoppen")

        keuze = input("Maak je keuze: ")

        if keuze == "1":
            score = 0
            print("Welkom bij de Cybersecurityquiz!")

            score = vragen_stellen()
            score_tonen(score)
            score_opslaan(score)

        elif keuze == "2":
            print("Terug naar het hoofdmenu!")
            break

        else:
            print("Ongeldige keuze!")


if __name__ == "__main__":
    cybersecurity_quiz()
