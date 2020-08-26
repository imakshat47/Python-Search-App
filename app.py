import PySimpleGUI as sg
import wikipedia
import wolframalpha             # API Call for Query
# Object of API Wolfram Alpha
client = wolframalpha.Client("K9XH57-7LUQHPW2J3")

# text to speach "Python Text to Speach"
import pyttsx3
engine = pyttsx3.init()
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# Query input Modal
sg.theme('DarkPurple')  # Add a touch of color Eg: Amber
# All the stuff inside your window.
layout = [[sg.Text('Enter a command'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Imaj', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    try:
        try:
            res = client.query(values[0])
            # Eg: "temperature in Washington, DC on October 3, 2012"
            wolfram_res = next(res.results).text
            sg.PopupNonBlocking(wolfram_res, title="Result from Walfram Alpha")
            engine.say(wolfram_res)         #speaks
        except:
            wiki_res = wikipedia.summary(values[0], sentences=1)
            sg.PopupNonBlocking(wiki_res, title="Result from Wiki")    
            engine.say(wiki_res)              #speaks
    except NameError:     
        engine.say("No result Master. Something went wrong.")              #speaks

    engine.runAndWait()

window.close()
