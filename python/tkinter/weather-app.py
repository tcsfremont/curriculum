# Created by Andrew DeLapo

import urllib.request
import json
import pprint
import time

from tkinter import *

from PIL import Image

key = "API KEY GOES HERE!" # Get your own! https://openweathermap.org/

#Resize Snowman and SandCastle
snowman_img = Image.open("snowman.png")
snowman_img = snowman_img.resize((418, 500))
snowman_img.save("snowman.png", "png")

sandcastle_img = Image.open("sandcastle.png")
sandcaslte_img = sandcastle_img.resize((500, 500))
sandcastle_img.save("sandcastle.png", "png")

# Start App
root = Tk()
root.wm_title("Kyle's Weather App!")

# Create Entry Widget, where user can type city name.
city_entry = Entry(root)
city_entry.insert(END, "Fremont") # Default city is Fremont. You can change this!
city_entry.pack()

city = city_entry.get()

go_button = Button(root, text="Get Weather", height = 1, width = 15, bg = "black", fg = "white")
go_button.pack()

# Create URL
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=" + key

# Load Data
json_string = urllib.request.urlopen(url).read()
json_string = json_string.decode("utf-8") # Decode if necessary. Use if needed.
json_data = json.loads(json_string)

# Get current weather data
current_temp = json_data["main"]["temp"]
current_description = json_data["weather"][0]["description"]
icon_url = "http://openweathermap.org/img/w/" + json_data["weather"][0]["icon"] + ".png"
icon_data = urllib.request.urlretrieve(icon_url, filename="icon.png")

# Resizing Weather Icon
image = Image.open("icon.png")
image = image.resize((200, 200))
image.save("icon.png", "png")
image.close()

mainframe = Frame(root)
mainframe.pack()

lframe = Frame(mainframe)
lframe.grid(row = 1, column = 1)

rframe = Frame(mainframe)
rframe.grid(row = 1, column = 2)

snowman = PhotoImage(file="snowman.png")
sandcastle = PhotoImage(file="sandcastle.png")
weather_icon = PhotoImage(file="icon.png")

# Choose snowman or sandcastle based on current temp
if current_temp < 50:
    character_image = snowman
else:
    character_image = sandcastle

char_label = Label(lframe, image=character_image)
char_label.pack()

talk = "It's " + str(current_temp) + " degrees outside. " + current_description.title() + "!"

talk_frame = Frame(rframe)
talk_frame.pack()

talk_label = Label(talk_frame, text=talk, font = (20))
talk_label.pack()

lower_frame = Frame(rframe)
lower_frame.pack()

icon_label = Label(lower_frame, image=weather_icon)
icon_label.grid(row = 1, column = 1)

forecast_button = Button(lower_frame, text="Get Forecast", height = 1, width = 15, bg = "black", fg = "white")
forecast_button.grid(row = 1, column = 2)

def get_new_weather():
    city = city_entry.get()

    # Create URL
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=" + key

    # Load Data
    json_string = urllib.request.urlopen(url).read()
    json_string = json_string.decode("utf-8") # Decode if necessary. Use if needed.
    json_data = json.loads(json_string)

    #pprint.pprint(json_data)

    # Get current weather data
    current_temp = json_data["main"]["temp"]
    current_description = json_data["weather"][0]["description"]
    icon_url = "http://openweathermap.org/img/w/" + json_data["weather"][0]["icon"] + ".png"
    icon_data = urllib.request.urlretrieve(icon_url, filename="icon.png")

    # Resizing Weather Icon
    image = Image.open("icon.png")
    image = image.resize((200, 200))
    image.save("icon.png", "png")
    image.close()

    weather_icon = PhotoImage(file="icon.png")

    icon_label.config(image=weather_icon)
    icon_label.image = weather_icon

    if current_temp < 50:
        character_image = snowman
    else:
        character_image = sandcastle

    char_label.config(image=character_image)
    char_label.image = character_image

    talk = "It's " + str(current_temp) + " degrees outside. " + current_description.title() + "!"
    talk_label.config(text=talk)

go_button.config(command = get_new_weather)

# Get Forecast

def get_forecast():
    fc_window = Tk()
    fc_window.wm_title("Forecast")
    city = city_entry.get()
    url = "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&units=imperial&appid=" + key

    # Load Data
    json_string = urllib.request.urlopen(url).read()
    json_string = json_string.decode("utf-8") # Decode if necessary. Use if needed.
    json_data = json.loads(json_string)

    forecast = json_data["list"][::8]

    #print(forecast)

    count = 0

    for interval in forecast:
        day_frame = Frame(fc_window, relief=GROOVE, borderwidth=5)
                
        epoch = interval["dt"]
        t = interval["main"]["temp"]
        icon = interval["weather"][0]["icon"]
        icon_url = "http://openweathermap.org/img/w/" + icon + ".png"
        icon_data = urllib.request.urlretrieve(icon_url, filename="icon" + str(count) + ".png")

        date_label = Label(day_frame, text = time.strftime("%A, %B %d, %Y", time.localtime(int(epoch))))
        date_label.grid(row = 0, column = 0)

        weather_icon = PhotoImage(master=day_frame, file="icon" + str(count) + ".png")        
        icon_label = Label(day_frame, image = weather_icon)
        icon_label.image = weather_icon
        icon_label.grid(row = 1, column = 0)

        temp_label = Label(day_frame, text=str(t))
        temp_label.grid(row = 2, column = 0)

        day_frame.grid(row = 0, column = count, padx = 10, pady = 10)

        count = count + 1

        
#get_forecast()
forecast_button.config(command = get_forecast)

root.mainloop()


