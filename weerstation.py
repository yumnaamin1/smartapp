def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius

def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif gevoel < 10:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"

def vraag_getal(tekst):
    while True:
        invoer = input(tekst)
        if invoer == "":
            return None
        try:
            return float(invoer)
        except ValueError:
            print("Dat is geen geldig getal, probeer het opnieuw.")

def weerstation():
    temperaturen = []
    dag = 1

    for i in range(7):
        temp_c = vraag_getal("Wat is op dag " + str(dag) + " de temperatuur[C]: ")
        if temp_c is None:
            print("bye")
            break

        windsnelheid = vraag_getal("Wat is op dag " + str(dag) + " de windsnelheid[m/s]: ")
        if windsnelheid is None:
            print("bye")
            break

        vochtigheid = vraag_getal("Wat is op dag " + str(dag) + " de vochtigheid[%]: ")
        if vochtigheid is None:
            print("bye")
            break

        temp_f = Fahrenheit(temp_c)
        rapport = weerrapport(temp_c, windsnelheid, vochtigheid)

        temperaturen.append(temp_c)
        gemiddelde = sum(temperaturen) / len(temperaturen)

        print("Het is " + str(temp_c) + "C (" + str(temp_f) + "F)")
        print(rapport)
        print("Gem. temp tot nu toe is " + str(gemiddelde))
        print("======================================")

        dag += 1