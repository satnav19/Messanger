import PySimpleGUI as sg
import socket
import requests
sg.theme('Python')


def get_ip():
    url = "https://api.ipify.org/"
    answer = requests.get(url)
    return answer.text


layout = [[sg.Text("Your ip is: "), sg.Text(f"{get_ip()}")],
          [sg.Text("Enter recipient ip: "), sg.InputText()],
          [sg.Button("Start conversation"), sg.Button("Quit")]]
window = sg.Window("messanger", layout)
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Quit"):
        break
    sg.popup(f"target is: {values[0]}")
window.close()
