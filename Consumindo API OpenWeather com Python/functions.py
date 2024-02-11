import requests

def get_weather_from_api(api_key, city):
    '''
        Acessar diretamente a API OpenWeather
        :param api_key: 
        :param city: 
        :return:
    '''
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f'{base_url}appid={api_key}&={city}'
    response = requests.get(complete_url)

    return response.json()

def get_weather(city_name):
    '''
        Filtrar os dados climáticos de uma cidade
        :param city_name:
        :return:
    '''
    api_key = ''
    weather_data = get_weather_from_api(api_key, city_name)
    if weather_data['cod'] == 401:
        print('Problema durante a requisição!\n'
              f'Mensagem: {weather_data['message']}')
    elif weather_data['cod'] != 404:
        main_weather = weather_data['weather'][0]['main']
        temperature = weather_data['main']['temp']

        print(f'Clima em {city_name}: {main_weather}')
        print(f'Temperatura: {temperature - 273.15:.2f}°C')
    else:
        print('Cidade não encontrada!')