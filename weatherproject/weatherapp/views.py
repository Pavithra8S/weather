from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
import logging

def home(request):
    city = request.POST.get('city', 'indore')

    # OpenWeatherMap API
    WEATHER_API_KEY = '605e57733cbc61f5710a556a72c74efb'
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    weather_params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }

    # Google Custom Search API
    GOOGLE_API_KEY = 'AIzaSyC46GvyWtTOBuanx83FULthwqRXIiJp98U'
    SEARCH_ENGINE_ID = 'c0b7b5a3e7ebe47d8'
    search_query = f'{city} 1920x1080'
    fallback_image_url = 'https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg'

    try:
        # WEATHER API
        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()

        if weather_response.status_code != 200 or 'weather' not in weather_data:
            raise ValueError("Invalid weather API response")

        description = weather_data['weather'][0].get('description', 'Clear Sky')
        icon = weather_data['weather'][0].get('icon', '01d')  # fallback icon
        temp = weather_data['main'].get('temp', 25)
        day = datetime.date.today()

        # GOOGLE IMAGE SEARCH
        google_url = 'https://www.googleapis.com/customsearch/v1'
        search_params = {
            'key': GOOGLE_API_KEY,
            'cx': SEARCH_ENGINE_ID,
            'q': search_query,
            'searchType': 'image',
            'imgSize': 'xlarge',
            'num': 2
        }

        google_response = requests.get(google_url, params=search_params).json()
        image_url = fallback_image_url

        # Choose best image result
        if 'items' in google_response and len(google_response['items']) >= 1:
            image_url = google_response['items'][0].get('link', fallback_image_url)

        return render(request, 'index.html', {
            'description': description.title(),
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city.title(),
            'exception_occurred': False,
            'image_url': image_url
        })

    except Exception as e:
        logging.error(f"[ERROR] Weather fetch failed for city '{city}': {e}")
        messages.error(request, f"City data could not be retrieved. Showing fallback: Indore")

        return render(request, 'index.html', {
            'description': 'Clear Sky',
            'icon': '01d',
            'temp': 25,
            'day': datetime.date.today(),
            'city': 'Indore',
            'exception_occurred': True,
            'image_url': fallback_image_url
        })
