import urllib2, json
from random import randint

def getDailyWeatherConditions():
    response = urllib2.urlopen("https://raw.githubusercontent.com/arocho/generative-art/master/data/bayamon_weather021917").read()
    bayamonWeather = json.loads(response)
    dailyConditions = bayamonWeather['daily']
    return dailyConditions['data']

def getColor(weather):
    color_dict = {'rain': '#6699cc', 'partly-cloudy-day': '#99cccc', 'partly-cloudy-night': '#336666', 'clear-day': '#66cccc'}
    
    return color_dict[weather]
    
def setup():
    size(800, 800)
    noLoop()
    alpha(100)
    noFill()

def draw():
    background(0)
    forecast = getDailyWeatherConditions()
    
    for i, val in enumerate(forecast):
        x = randint(100,700)
        y = randint(100,700)
        eWidth = randint(500,700)
        eHeight= randint(500,700)
        ellipse(x, y, eWidth, eHeight)
        print forecast[i]['icon']
        stroke(getColor(forecast[i]['icon']))
        
        