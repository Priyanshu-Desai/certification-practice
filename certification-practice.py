#emergency debugger
# import pdb; pdb.set_trace()
#importing modules
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

#defining function to get the value of selected checkbuttons in question
def submit_question():
    global chosenAnswers
    chosenAnswers = ''
    if optionAVar.get() == True:
        chosenAnswers += 'A'
    if optionBVar.get() == True:
        chosenAnswers += 'B'
    if optionCVar.get() == True:
        chosenAnswers += 'C'
    if optionDVar.get() == True:
        chosenAnswers += 'D'

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

#give questions to user on certification
nextbutton.wait_variable(waitstate)
#while loop for infinite questions
loop = True
while loop == True:
    #checking which certification the user has chosen
    if chosenCertification == 'az900':
        #randomly selecting a question
        selectedQuestion = choice(az900)

    #reading question details and saving them to a variable
    questionText = selectedQuestion['question']
    optionAText = selectedQuestion['options']['A']
    optionBText = selectedQuestion['options']['B']
    optionCText = selectedQuestion['options']['C']
    optionDText = selectedQuestion['options']['D']
    answer = selectedQuestion['answer']

    #setting control variables to capture state of checkbox
    optionAVar = BooleanVar()
    optionBVar = BooleanVar()
    optionCVar = BooleanVar()
    optionDVar = BooleanVar()

    #creating taxt label
    question = ttk.Label(root, text=questionText)
    question.pack()
    question.place(relx=0.5, rely=0.1, anchor='n')

    #creating checkboxes if the value of the option is not None
    if optionAText != None:
        optionA = ttk.Checkbutton(root, text=optionAText, variable=optionAVar)
        optionA.pack()
        optionA.place(relx='0.5', rely='0.3', anchor='center')
    if optionBText != None:
        optionB = ttk.Checkbutton(root, text=optionBText, variable=optionBVar)
        optionB.pack()
        optionB.place(relx='0.5', rely='0.4', anchor='center')
    if optionCText != None:
        optionC = ttk.Checkbutton(root, text=optionCText, variable=optionCVar)
        optionC.pack()
        optionC.place(relx='0.5', rely='0.5', anchor='center')
    if optionDText != None:
        optionD = ttk.Checkbutton(root, text=optionDText, variable=optionDVar)
        optionD.pack()
        optionD.place(relx='0.5', rely='0.6', anchor='center')

    #creating submit Button
    submitButton = ttk.Button(root, text='Submit', command=submit_question)
    submitButton.pack()
    submitButton.place(relx=0.9, rely=0.9, anchor='center')
    submitButton.wait_variable(waitstate)

    if chosenAnswers == answer:
        print('correct')
    else:
        print('incorrect')

    #exiting loop
    loop = False

#execute tkinter
root.mainloop()
