import requests
from bs4 import BeautifulSoup

def obter_previsao_tempo(cidade='São Paulo'):
    url = f'https://weather.com/pt-BR/clima/hoje/l/24ad1305205b675a4165b13e3638cf90b620c87a7e234c1a7365d6b67aaadb12'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        elemento_temperatura = soup.find(class_='TodayDetailsCard--feelsLikeContainer--2bePz')
        if elemento_temperatura:
            temperatura = elemento_temperatura.get_text()
            return temperatura
        else: 
            return "não foi possivel obter a temperatura, tente novamente mais tarde"
    else:
        return 'não foi possivel obter a temperatura, tente novamente mais tarde'

previsao_sao_paulo = obter_previsao_tempo()

print(f'a previsao para São Paulo é de {previsao_sao_paulo}')