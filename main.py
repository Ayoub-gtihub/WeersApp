from api_weer import huidig_weer
from controller import smart_app_controller

def menu():
    while True:
        print('\n==========================')
        print('                WeersApp')
        print('Regen of zon? WeersApp weet het')
        print('1. Eigen weerstation')
        print('2. Smart App Controller')
        print('3. Huidig weer in Utrecht')
        print('4. Afsluiten')


        keuze = input('Maak een keuze: ')

        if keuze == '1':
            weerstation()

        elif keuze == '2':
            smart_app_controller()


        elif keuze == '3':
            huidig_weer()


        elif keuze == '4':
            print('Bedankt voor het gebruiken van WeersApp')
            break

        else:
            print('Ongeldige keuze. Kies 1, 2, 3 of 4.')

if __name__ == '__main__':
    menu()


 