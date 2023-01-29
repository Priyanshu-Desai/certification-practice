#importing modules
from random import choice
from tkinter import *
from tkinter import ttk

#opening files
az900 = open("questions/AZ-900.json", "r")

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
welcomebutton = ttk.Button(root, text='Next -->', command=clear_frame)
welcomebutton.pack()
welcomebutton.place(relx=0.5, rely=0.5, anchor='center')

#give certification options afer empty frame
welcomebutton.wait_variable(waitstate)
certifications = StringVar()
az900 = ttk.Radiobutton(root, text="AZ-900", variable=certifications, value="az900")
az900.pack()
az900.place(relx=0.5, rely=0.5, anchor='center')
certButton = ttk.Button(root, text='Next -->', command=choose_certification)
certButton.pack()
certButton.place(relx=0.9, rely=0.9, anchor='center')
welcomebutton.wait_variable(waitstate)
print(chosenCertification)

#execute tkinter
root.mainloop()
