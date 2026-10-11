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



def aantal_dagen(inputFile):
    try:
        with open(inputFile, "r") as file:
            regels = file.readlines()

        return max(0, len(regels) - 1)

    except FileNotFoundError:
        print(f"Fout: bestand '{inputFile}' bestaat niet.")
        return 0

    except OSError as fout:
        print(f"Het bestand kon niet worden gelezen: {fout}")
        return 0




def auto_bereken(inputFile, outputFile):
    try:
        with open(inputFile, "r") as file:
            regels = file.readlines()

        with open(outputFile, "w") as file:
            for regel in regels[1:]:
                gegevens = regel.split()

                if len(gegevens) < 5:
                    print("Regel overgeslagen:", regel.strip())
                    continue

                try:
                    datum = gegevens[0]
                    numPeople = int(gegevens[1])
                    tempSetpoint = float(gegevens[2])
                    tempOutside = float(gegevens[3])
                    precip = float(gegevens[4])
                except ValueError:
                    print("Ongeldige gegevens:", regel.strip())
                    continue

                temperatuurverschil = tempSetpoint - tempOutside

                if temperatuurverschil >= 20:
                    cv = 100
                elif temperatuurverschil >= 10:
                    cv = 50
                else:
                    cv = 0

                ventilatie = min(numPeople + 1, 4)
                bewatering = precip < 3

                file.write(
                    f"{datum};{cv};{ventilatie};{bewatering}\n"
                )

        print("Actuatoren zijn berekend en opgeslagen.")

    except FileNotFoundError:
        print(f"Bestand '{inputFile}' bestaat niet.")
    except OSError as fout:
        print(f"Bestandsfout: {fout}")



def overwrite_settings(outputFile):
    datum = input ('Welke datum wil je aanpassen?')
    try:
        systeem = int(input('Kies een systeem(1, 2 of 3):'))
    except ValueError:
        print('Ongeldige invoer. voer 1, 2, of 3 in.')
        return -3

    if systeem == 1:
        try:
          waarde = int(input('Welke waarde?'))
        except ValueError:
            print('Voer een geldig getal in.')
            return -3

        if waarde < 0 or waarde > 100:
            return -3

    elif systeem == 2:
        try:
          waarde = int(input('Welke waarde?'))
        except ValueError:
            print('Voer een geldig getal in.')
            return -3

        if waarde < 0 or waarde > 4:
            return -3

    elif systeem == 3:
        try:
          waarde = int(input('Welke waarde?'))
        except ValueError:
            print('Voer een geldig getal in.')
            return -3
        if waarde != 0 and waarde != 1:
            return -3

    else:
        return -3

    with open(outputFile, 'r') as file:
        regels = file.readlines()

    gevonden = False

    for regel in regels:
         gegevens = regel.strip().split(';')

         if gegevens [0] == datum:
             gevonden = True
             if systeem == 1:
                 gegevens[1] = str(waarde)
             elif systeem == 2:
                 gegevens[2] = str(waarde)
             elif systeem == 3:
                 if waarde == 0:
                      gegevens[3] = 'False'
                 else:
                     gegevens[3] = 'True'

             nieuwe_regel = ';'.join(gegevens) + '\n'
             regels[regels.index(regel)] = nieuwe_regel


    if not gevonden:
        return -1


    with open(outputFile, 'w') as file:
        file.writelines(regels)

    return 0

def smart_app_controller():
    inputFile = 'input.txt'
    outputFile = 'output.txt'

    while True:
        print()
        print('Smart App Controller')
        print('1. Hoeveel dagen zijn aanwezig?')
        print('2. Bereken alle actuatoren')
        print('3. Overschrijf een waarde')
        print('4. Stoppen')

        keuze = input('Maak een keuze: ')

        if keuze == '1':
            print(aantal_dagen(inputFile))

        elif keuze == '2':
            auto_bereken(inputFile, outputFile)
            print('Actuatoren zijn berekend en opgeslagen.')

        elif keuze == '3':
            resultaat = overwrite_settings(outputFile)

            if resultaat == 0:
                print('Waarde succesvol aangepast')
            elif resultaat == -1:
                print('Datum niet gevonden')
            elif resultaat == -3:
                print('Ongeldige invoer.')

        elif keuze == '4':
            print('Programma gestopt.')
            break

        else:
            print('Ongeldige keuze.')

