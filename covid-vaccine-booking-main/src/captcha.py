from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import PySimpleGUI as sg
import re

from captchasolve import solve
def captcha_builder(resp):
    print()
    print()
    print()
    print()
    a = solve(resp['captcha'])
    print()
    print()
    print()
    print()
    print()
    with open('captcha.svg', 'w') as f:
        f.write(re.sub('(<path d=)(.*?)(fill=\"none\"/>)', '', resp['captcha']))

    #drawing = svg2rlg('captcha.svg')
    #renderPM.drawToFile(drawing, "captcha.png", fmt="PNG")

    #layout = [[sg.Image('captcha.png')],
    #          [sg.Text("Enter Captcha Below")],
    #          [sg.Input(key='inp')],
    #          [sg.Button('Submit', bind_return_key=True)]]

    #window = sg.Window('Enter Captcha', layout, finalize=True)
    #window.TKroot.focus_force()         # focus on window
    #window.Element('inp').SetFocus()    # focus on field
    #event, values = window.read()
    #window.close()
    #print(values['inp'],"OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    return a

