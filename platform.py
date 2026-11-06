import requests
from weerstation import weerstation
from controller import smart_app_controller
from budgetplanner import budgetplanner
from todo_app import todo_app
from cybersecurity_quiz import cybersecurity_quiz

def huidige_temperatuur():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.09&longitude=5.12&current_weather=true"

    try:
        response = requests.get(url)
        data = response.json()
        temperatuur = data["current_weather"]["temperature"]
        print("De huidige temperatuur in Utrecht is", temperatuur, "graden Celsius.")
    except:
        print("Kon de temperatuur niet ophalen, controleer je internetverbinding.")


def platform():
    stoppen = False
    while not stoppen:
        print("1: Weerstation")
        print("2: Smart App Controller")
        print("3: Huidige temperatuur Utrecht")
        print("4: Budgetplanner")
        print("5: TODO-app")
        print("6: Cybersecurityquiz")
        print("7: Stoppen")
        keuze = input("Keuze: ")

        if keuze == "1":
            weerstation()
        elif keuze == "2":
            smart_app_controller()
        elif keuze == "3":
            huidige_temperatuur()
        elif keuze == "4":
            budgetplanner()
        elif keuze == "5":
            todo_app()


        elif keuze == "6":

            cybersecurity_quiz()


        elif keuze == "7":

            stoppen = True

            print("Tot ziens!")
        else:
            print("Ongeldige keuze, probeer opnieuw.")


platform()