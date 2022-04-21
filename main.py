from ast import operator
from tkinter import *
from numpy import place
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from timezonefinder import TimezoneFinder
from phonenumbers import timezone
from geopy.geocoders import Nominatim

import time
import zoneinfo
import config
import pytz


root = Tk()
root.geometry("365x584+400+100")
root.resizable(False,False)

def track():
    enter_number = entry.get()
    number = phonenumbers.parse(enter_number)
    #Country
    locate = geocoder.description_for_number(number, "en") 
    l = Label(root,text=locate, bg="black",fg="white",font=("arial",10,"bold")).place(x=10,y=400)
    
    #operator
    operator = carrier.name_for_number(number, "en")
    o = Label(root,text=operator, bg="black",fg="white",font=("arial",10,"bold")).place(x=200,y=400)
    
    #phone timezone
    time = timezone.time_zones_for_number(number)
    t = Label(root,text=time, bg="black",fg="white",font=("arial",10,"bold")).place(x=10,y=450)
    
    #geolocater
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(locate)
    lng = location.longitude
    lat = location.latitude
    n = Label(root,text=lng, bg="black",fg="white",font=("arial",10,"bold")).place(x=10,y=500)

    a = Label(root,text=lat, bg="black",fg="white",font=("arial",10,"bold")).place(x=200,y=500)
    
   
    
    


heading = Label(root,text="TRACK NUMBER", font=("arial", 15,"bold")).place(x=100,y=110)

entry = StringVar()
enter_number = Entry(root,textvariable=entry,width=17,bd=0,font=("arial",20),justify="center").place(x=50,y=220)

country = Label(root,text="Country: ", bg="black",fg="white",font=("arial",10,"bold")).place(x=10,y=400)

sim = Label(root,text="SIM: ", bg="black",fg="white",font=("arial",10,"bold")).place(x=200,y=400)

zone = Label(root,text="TimeZone:", bg="black",fg="white",font=("arial",10,"bold")).place(x=10,y=450)

clock = Label(root,text="PhoneTime:", bg="black",fg="white",font=("arial",10,"bold")).place(x=200,y=450)

longitude = Label(root,text="Longitude:", bg="black",fg="white",font=("arial",10,"bold")).place(x=10,y=500)

latitude = Label(root,text="Latitude:", bg="black",fg="white",font=("arial",10,"bold")).place(x=200,y=500)



button = Button(root,text="Search",cursor="hand2",bd=0,font=("arial",16,"bold"),command=track).place(x=135,y=300)

root.mainloop()