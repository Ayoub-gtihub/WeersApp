def Fahrenheit(temp_celcius):
    fahrenheit = 32 + 1.8 * temp_celcius
    return fahrenheit

def gevoelstemperatuur(windsnelheid, temp_celcius, luchtvochtigheid):
    gevoel = temp_celcius - (luchtvochtigheid/ 100 * windsnelheid)
    return gevoel

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(windsnelheid, temp_celcius, luchtvochtigheid)
    if gevoel < 0 and windsnelheid > 10:
        return'Het is heel koud en het stormt! Verwarming helemaal aan!'
    elif gevoel < 0 and windsnelheid <= 10:
        return 'Het is behoorlijk koud! Verwarming aan op de benedenverdieping!'
    elif gevoel >= 0 and gevoel < 10 and windsnelheid > 12:
        return 'Het is best koud en het waait; verwarming aan en roosters dicht!'
    elif gevoel >= 0 and gevoel < 10 and windsnelheid <= 12:
        return'het is een beetje koud, elektrische kachel op de benedenverdieping aan!'
    elif gevoel >= 10 and gevoel < 22:
        return 'heerlijk weer, niet te koud of te warm'
    else:
        return 'Warm! Airco aan!'

def weerstation():
    temperaturen = []

    for dag in range (1, 8):
        invoer = input(f'Wat is op de {dag} de temperatuur[C]:')

        if invoer == "":
            break

        try:
            temp_celcius = float(invoer)
        except ValueError:
            print('voer een geldig getal in')
            continue

        temperaturen.append(temp_celcius)

        invoer_wind = input(f'Wat is op dag {dag} de windsnelheid[m/s]:')

        if invoer_wind == "":
            break

        try:
            windsnelheid = float(invoer_wind)
        except ValueError:
            print('Voer een geldig getal in')
            continue

        invoer_lucht = input(f'Wat is op die dag {dag} de vochtigheid[%]')

        if invoer_lucht == "":
            break

        try:
            luchtvochtigheid = float(invoer_lucht)
        except ValueError:
            print('Voer een geldig getal in')
            continue


        fahrenheit_waarde = Fahrenheit(temp_celcius)
        print(f'het is {temp_celcius}C ({fahrenheit_waarde}F)')

        rapport = weerrapport (temp_celcius, windsnelheid, luchtvochtigheid)
        print(rapport)

        gemiddelde = sum(temperaturen) / len(temperaturen)
        print(f'Gem. temp tot nu toe is {gemiddelde}')
        print('================================')

