import PySimpleGUI as sg
import subprocess
import os
from . import connect4


def run_python_file(filepath):
    subprocess.run(['python', filepath])

layout = [
    [sg.Text('Willkommen zu KI-Viergewinnt!       ')],
    [sg.Text('für einwandfreie Funktion Hand öffnen Handfläche zur Webcam')],
    [sg.Text('zum Fallenlassen der Steine, einfach Hand zur Faust schliessen')],
    [sg.Text('Danach ist der Zug beendet und der nächster Spieler an der Reihe')],        
    [sg.Button('Start', key='Multiplayer')],
    [sg.Button('Schließen')]
]

window = sg.Window('Viel Spaß mit diesem kleinen Spiel', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Schließen'):
        break
    
    elif event == 'Multiplayer':
        filepath = os.path.join(os.path.dirname(__file__), 'connect4.py')
        run_python_file(filepath)

window.close()
