import urllib.request
import json

def huidig_weer():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=52.0907&longitude=5.1214"
        "&current=temperature_2m,wind_speed_10m"
    )
    

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            gegevens = json.loads(response.read().decode('utf-8'))

        huidig = gegevens['current']
        temperatuur = huidig['temperature_2m']
        wind = huidig['wind_speed_10m']

        print('\n--- Huidig weer in Utrecht ---')
        print(f'Temperatuur: {temperatuur} C')
        print(f'Windsnelheid: {wind} km/u')
        
    except (OSError, ValueError, KeyError) as fout:
        print('Het weer kon niet worden opgehaald')
        print(f'Details: {fout}')