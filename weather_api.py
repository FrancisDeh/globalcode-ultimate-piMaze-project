import pyowm

class WizzWeatherApi:
    
    def __init__(self, location):
        self.wm = pyowm.OWM('0215eb4164df6ee58a770465f1825379')
        self.location = location
        self.observation = self.wm.weather_at_place(location)
        self.weather = self.observation.get_weather()
   
    def wind(self):
        return self.weather.get_wind()['deg']

    def humidity(self):
        return self.weather.get_humidity()

    def temp(self):
        return self.weather.get_temperature('celsius')['temp']

#w = WizzWeatherApi("Location")
#w.wind()
#w.temp()
#w.humidity()

