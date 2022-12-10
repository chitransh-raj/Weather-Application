from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f714b76b0e66609998f5781e6f33b427").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pr_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather App")
win.config(bg= "Sky blue")
win.geometry("500x600")

name_label = Label(win, text="Weather Application",
                   font=("Hack",32, "bold"))
name_label.place(x=25, y=50, height=60, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text="Weather Application", values = list_name,
                   font=("Hack",25, "bold"), textvariable=city_name)
com.place(x=25, y=150, height=60, width=450)


w_label = Label(win, text="Weather Climate",
                   font=("Hack",18, ))
w_label.place(x=25, y=350, height=40, width=210)
w_label1 = Label(win, text="",
                   font=("Hack",18, ))
w_label1.place(x=265, y=350, height=40, width=210)


wb_label = Label(win, text="Weather Discription",
                   font=("Hack",16, ))
wb_label.place(x=25, y=410, height=40, width=210)
wb_label1 = Label(win, text="",
                   font=("Hack",16, ))
wb_label1.place(x=265, y=410, height=40, width=210)


temp_label = Label(win, text="Temperature",
                   font=("Hack",16, ))
temp_label.place(x=25, y=470, height=40, width=210)
temp_label1 = Label(win, text="",
                   font=("Hack",16, ))
temp_label1.place(x=265, y=470, height=40, width=210)

pr_label = Label(win, text="Pressure",
                   font=("Hack",16, ))
pr_label.place(x=25, y=530, height=40, width=210)
pr_label1 = Label(win, text="",
                   font=("Hack",16, ))
pr_label1.place(x=265, y=530, height=40, width=210)


submit_button = Button(win, text="Done",
                   font=("Hack",20, "bold"), command=data_get)
submit_button.place(x=200, y=250, height=40, width=100)


win.mainloop()