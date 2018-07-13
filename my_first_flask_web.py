from flask import Flask,render_template, request
from weather_api import WizzWeatherApi

app = Flask(__name__)

@app.route('/')
def index():
    location = "Cape Coast, gh"
    w = process_weather(location)
    wind = w['wind']
    temp = w['temp']

    humidity = w['humidity']
    
    return render_template('index.html', l = location, w = wind, t = temp, h = humidity)

@app.route('/process', methods = ['POST', 'GET'])
def process():
    if request.method == 'POST':
        result = request.form
        for key, value in result.items():
            loc = value
        w = process_weather(loc)
        wind = w['wind']
        temp = w['temp']
        humidity = w['humidity']
    
    return render_template('index.html', l = loc, w = wind, t = temp, h = humidity)


def process_weather(location):
    w = WizzWeatherApi(location)
    wind = w.wind()
    temp = w.temp()
    humidity = w.humidity()
    
    return {'wind': wind, 'temp':temp, 'humidity':humidity}
    
@app.route('/signin')
def signin():
    return "Please provide your email and password"

@app.route('/register')
def register_user():
    return "You have been successfully registered"

@app.route('/logout')
def loguout():
    return "Bye Bye"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
