import time
import tkinter as tk
import datetime
import requests

def Weather(box):
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=45e0057ee1a4a9f43a6b875247e73f4a"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    info=condition + "\n"+ str(temp)+ "C"
    datas="\n"+ "Max Temp : " +str(max_temp)+"\n" + "Min Temp : " +str(min_temp) +"\n"+ "Pressure : " +str(pressure) + "\n" + "Humidity : " + str(humidity)+ "\n"+ "Wind : " +str(wind)+ "\n"+ "Sunset : " +sunset +"\n" + "Sunrise : " +sunrise
    lbl1.config(text=info)
    lbl2.config(text=datas)

box=tk.Tk()
box.geometry("400x400")
box.title("Weather")
box.configure(bg='pink')

Font=("Courier", 15, "bold")
text=("Courier", 25, "bold")

textfield=tk.Entry(box, font=Font)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',Weather)

lbl1=tk.Label(box, font=Font)
lbl1.pack()

lbl2=tk.Label(box,font=Font)
lbl2.pack()

box.mainloop()