# 🌤️ Django Weather App

This is a Django-based weather application that shows real-time weather information for any city entered by the user. It also displays a dynamic city image using the Google Custom Search API.

---

## ✨ Features

- Get real-time weather data for any city
- Beautiful city background images (1920x1080)
- Fallback city and image in case of API failure
- Error handling with user-friendly messages
- Uses OpenWeatherMap and Google Custom Search APIs

---

## 🌐 Demo

[image_alt] (https://github.com/Pavithra8S/weather/blob/main/weatherproject/weatherapp/static/Screenshot%202025-07-21%20221049.png)
[image_alt] (https://github.com/Pavithra8S/weather/blob/main/weatherproject/weatherapp/static/Screenshot%202025-07-21%20221102.png)

---

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **APIs:**
  - [OpenWeatherMap](https://openweathermap.org/)
  - [Google Custom Search](https://programmablesearchengine.google.com/)
- **Frontend:** HTML5, CSS3, Bootstrap (optional)

---

## 🔧 How It Works

1. User submits a city name via a form
2. The app:
   - Sends a request to **OpenWeatherMap** for weather data
   - Sends a request to **Google Custom Search** for a relevant background image
3. Renders the data and image to `index.html`
4. On failure (invalid city or network issue), it shows default data for **Indore**

---

## ⚙️ Getting Started

### 1.Clone the repository

```bash
git clone https://github.com/yourusername/django-weather-app.git
cd django-weather-app
 ### 2.Set Up Virtual Environment (optional but recommended)
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
### 3. Install Dependencies
pip install -r requirements.txt

### 4.Configure API Keys
Open views.py and replace:
WEATHER_API_KEY = 'your_openweather_api_key'
GOOGLE_API_KEY = 'your_google_api_key'
SEARCH_ENGINE_ID = 'your_search_engine_id'

### 5.Run the Project
python manage.py runserver

