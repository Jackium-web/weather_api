from fastapi import FastAPI
import requests
import os

app = FastAPI()

# Your OpenWeatherMap API Key (you need to get one free)
API_KEY = os.getenv("API_KEY")

@app.get("/weather")
def get_weather(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        return {"error": "City not found or API error"}
    
    weather_info = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }
    
    return weather_info
