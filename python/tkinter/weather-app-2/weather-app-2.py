# Weather App

from tkinter import *
import urllib.request
import json

from pprint import pprint

with open("api-key.txt") as file:
    key = file.read()

BASE_URL = "https://api.openweathermap.org/data/2.5/"
UNITS = "imperial"  # options menu?

DEG = "°"

def get_weather(city):
    url = BASE_URL + "weather?q=" + city + "&units=" + UNITS + "&appid=" + key
    request = urllib.request.urlopen(url).read()
    data = json.loads(request)
    pprint(data)
    return data

def get_forecast(city):
    url = BASE_URL + "forecast?q=" + city + "&units=" + UNITS + "&appid=" + key
    request = urllib.request.urlopen(url).read()
    data = json.loads(request)
    pprint(data['list'][0])

font_name = "Verdana"


class CityPage(Frame):
    def __init__(self, parent, city):
        Frame.__init__(self, parent)
        self.city = city

        self.city_label = Label(self, text="---------", font=(font_name, 36))
        self.city_label.grid(row=1, column=1, columnspan=2)

        self.desc_label = Label(self, text="-----", font=(font_name, 16))
        self.desc_label.grid(row=2, column=1, columnspan=2, pady=(0, 20))

        self.temp_label = Label(self, text="--" + DEG, font=(font_name, 32))
        self.temp_label.grid(row=3, column=1)

        self.icon_label = Label(self, text="----")
        self.icon_label.grid(row=3, column=2)

        self.forecast_frame = Frame(self)
        self.forecast_frame.grid(row=4, column=1, columnspan=2)

        self.update_current()

        self.forecast_data = []

    def update_current(self):
        data = get_weather(self.city)
        temp = int(data["main"]["temp"])
        desc = data["weather"][0]["description"].title()
        icon = data["weather"][0]["icon"]
        
        self.city_label.config(text=self.city)
        self.desc_label.config(text=desc)
        self.temp_label.config(text=str(temp) + DEG)
        self.icon_label.config(text=icon)

    def update_forecast():
        print(self.forecast_data)

        


root = Tk()

city_page = CityPage(root, "Fremont")
city_page.pack()
