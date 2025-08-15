from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "f595e1162872637634cb238917f5faed"# Replace with your OpenWeatherMap key

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"].title(),
        }
    return None

@app.route("/", methods=["GET"])
def home():
    city = request.args.get("city")
    weather = None
    if city:
        weather = get_weather(city)
    return render_template("index.html", weather=weather, city=city)

if __name__ == "__main__":
    app.run(debug='false')
