import PySimpleGUI as sg
from pygame import mixer
mixer.init()

def login_window():
    sg.theme('GreenMono')
    layout_login = [
        [sg.Text('User'),sg.InputText(key='user')],
        [sg.Text('Password'),sg.Input(key='password',password_char='*')],
        [sg.Button('Login')]
    ]
    return sg.Window('Welcome', layout_login, finalize=True)

def player_window():
    sg.theme('GreenMono')
    layout_player = [
        [sg.Text('----------------')],
        [sg.Button('Play Music')]
    ]
    return sg.Window('Play Music', layout_player, finalize=True)

def play_music():
    mixer.music.load('music1.mp3')
    mixer.music.play()

def stop_music():
    mixer.music.stop()

def pause_music():
    mixer.music.pause()

window1, window2= login_window(), None

while True:
    window, event, values = sg.read_all_windows()

    if window == window1 and event == sg.WINDOW_CLOSED:
        break

    if window == window1 and event == 'Login':
        window2 = player_window()
        window1.hide()

    if window == window2 and event == 'Play Music':
        play_music()

    if window == window2 and event == sg.WINDOW_CLOSED:
        break