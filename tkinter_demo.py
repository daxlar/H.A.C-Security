from tkinter import *


HIGH = 3
MEDIUM = 2
LOW = 1

door_priority = 0
sound_priority = 0
temperature_hi_priority = 0
temperature_low_priority = 0


def crib_callback():
    global door_priority, sound_priority, temperature_hi_priority, temperature_low_priority
    door_priority = HIGH
    sound_priority = MEDIUM
    temperature_hi_priority = HIGH
    temperature_low_priority = HIGH
    root.destroy()


def pet_callback():
    global door_priority, sound_priority, temperature_hi_priority, temperature_low_priority
    door_priority = HIGH
    sound_priority = LOW
    temperature_hi_priority = HIGH
    temperature_low_priority = HIGH
    root.destroy()


def home_callback():
    global door_priority, sound_priority, temperature_hi_priority, temperature_low_priority
    door_priority = HIGH
    sound_priority = HIGH
    temperature_hi_priority = LOW
    temperature_low_priority = LOW
    root.destroy()


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
print(temperature_low_priority)


