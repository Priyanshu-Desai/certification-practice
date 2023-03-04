#importing modules
#import pdb; pdb.set_trace()
from random import choice
import json
from tkinter import *
from tkinter import ttk

#opening files
az900 = open("questions/az900.json", "r")

#creating python objects from json
az900 = json.load(az900)

#setting up Tk with a title
root = Tk()
root.title("cloud certification practice")

#defining function to clear Frame
def clear_frame():
    for child in root.winfo_children():
        child.destroy()
    waitstate.set(1)

#defining function to get the value of the celected certification radio button
def choose_certification():
    global chosenCertification
    chosenCertification = certifications.get()
    clear_frame()

# creating a 500 by 500 window
frame = ttk.Frame(root, width=500, height=500)
frame.pack()

#make program wait until button press
waitstate = IntVar()

#creating welcome screen, with text and button
welcometext = ttk.Label(root, text="Welcome!\nHere you can practice exam questions for a variety of certifications!\nClick next to get started\n")
welcometext.pack()
welcometext.place(relx=0.5, rely=0, anchor='n')
nextbutton = ttk.Button(root, text='Next -->', command=clear_frame)
nextbutton.pack()
nextbutton.place(relx=0.5, rely=0.5, anchor='center')
nextbutton.wait_variable(waitstate)

#give certification options afer empty frame
certifications = StringVar()
az900radio = ttk.Radiobutton(root, text="AZ-900", variable=certifications, value="az900")
az900radio.pack()
az900radio.place(relx=0.5, rely=0.5, anchor='center')
nextbutton = ttk.Button(root, text='Next -->', command=choose_certification)
nextbutton.pack()
nextbutton.place(relx=0.9, rely=0.9, anchor='center')
print(certifications)
#givequestions to user on certification
nextbutton.wait_variable(waitstate)
loop = True
# while loop == True:
#     if

#execute tkinter
root.mainloop()
