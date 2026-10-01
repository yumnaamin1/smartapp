temperatuur = float(input("Wat is op dag 1 de temperatuur[C]: "))
windsnelheid = float(input("Wat is op dag 1 de windsnelheid[m/s]:"))
vochtigheid = float(input("Wat is op dag 1 de vochtigheid[%]: "))

temp_f = 32 + 1.8 * temperatuur
gevoelstemperatuur = temperatuur - vochtigheid / 100 * windsnelheid

if gevoelstemperatuur < 0 and windsnelheid > 10:
    rapport = "Het is heel koud en het stormt! Verwarming helemaal aan!"
elif gevoelstemperatuur < 0:
    rapport = "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
elif gevoelstemperatuur < 10 and windsnelheid > 12:
    rapport = "Het is best koud en het waait; verwarming aan en roosters dicht!"
elif gevoelstemperatuur < 10:
    rapport = "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
elif gevoelstemperatuur < 22:
    rapport = "Heerlijk weer, niet te koud of te warm."
else:
    rapport = "Warm! Airco aan!"

print("het is", temperatuur, "C en", temp_f)
print("windsnelheid:", windsnelheid)
print("vochtigheid:", vochtigheid)
print("gevoelstemperatuur is:", gevoelstemperatuur)
print(rapport)