import socket
from tkinter import *
import requests

HIGH = 3
MEDIUM = 2
LOW = 1

microphone = 1
reed = 10
temperature = 100

number_samples = 0
greatest_number = 0

door_priority = 0
sound_priority = 0
temperature_hi_priority = 0


high_risk = "go home now"
medium_risk = "pay attention to alerts"
low_risk = "all iz well"

phrase_1 = low_risk
phrase_2 = low_risk
phrase_3 = low_risk

def crib_callback():
    global door_priority, sound_priority, temperature_hi_priority, temperature_low_priority
    door_priority = HIGH
    sound_priority = MEDIUM
    temperature_hi_priority = HIGH
    root.destroy()


def pet_callback():
    global door_priority, sound_priority, temperature_hi_priority, temperature_low_priority
    door_priority = HIGH
    sound_priority = LOW
    temperature_hi_priority = HIGH
    root.destroy()


def home_callback():
    global door_priority, sound_priority, temperature_hi_priority, temperature_low_priority
    door_priority = HIGH
    sound_priority = HIGH
    temperature_hi_priority = LOW
    root.destroy()


def email_alert(first, second, third):
    report = {"Value1" : 0, "Value2": 0, "Value3": 0}
    report["Value1"] = first
    report["Value2"] = second
    report["Value3"] = third
    requests.post("https://maker.ifttt.com/trigger/something_is_WRONG/with/key/dCOToeQZzXJRGlzaWT6c5O?value1={}&value2={}&value3={}".format(first, second, third))


root = Tk()

ourMessage ='Remember to lock the door!'
messageVar = Message(root, text=ourMessage)
messageVar.config(bg='lightblue')
messageVar.pack(fill=BOTH, expand=True)

crib = Button(root, text="crib monitor", command=crib_callback)
crib.pack(fill=BOTH, expand=True)

pet = Button(root, text="pet monitor", command=pet_callback)
pet.pack(fill=BOTH, expand=True)

home = Button(root, text="home monitor", command=home_callback)
home.pack(fill=BOTH, expand=True)


root.mainloop()
print(door_priority)
print(sound_priority)
print(temperature_hi_priority)


UDP_PORT_NO = 6789
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("im about to start the infinite loop")
hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)
print(hostIP)
serverSock.bind((hostIP, UDP_PORT_NO))

while True:
    data, addr = serverSock.recvfrom(2048)
    current_value = int.from_bytes(data, byteorder='big')

    if current_value > greatest_number :
        greatest_number = current_value

    number_samples += 1

    if number_samples == 10000:

        if(greatest_number & 100) == 100:
            if temperature_hi_priority == HIGH:
                phrase_1 = high_risk
            if temperature_hi_priority == MEDIUM:
                phrase_1 = medium_risk
            if temperature_hi_priority == LOW:
                phrase_1 = low_risk

        if(greatest_number & 10) == 10:
            if door_priority == HIGH:
                phrase_2 = high_risk
            if door_priority == MEDIUM:
                phrase_2 = medium_risk
            if door_priority == LOW :
                phrase_2 = low_risk

        if(greatest_number & 1) == 1:
            if sound_priority == HIGH:
                phrase_3 = high_risk
            if sound_priority == MEDIUM:
                phrase_3 = medium_risk
            if sound_priority == LOW:
                phrase_3 = low_risk

        email_alert(phrase_2, phrase_1, phrase_3)
        greatest_number = 0
        number_samples = 0







