import tkinter as tk
from tkinter.ttk import Checkbutton
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import os
import subprocess


''' Создание функций и путей к картинкам '''
p = os.path.abspath('main.py')
def Menu():
    window.destroy()
    subprocess.run(["python", "main.py"])


''' Прочтение настроек '''
optionPP = open('options/PlayerP.txt')
OPP = optionPP.read()
optionPP.close()
Language = open('options/Language.txt')
Lang = Language.read()
Language.close()
Dificulty = open('options/Dificulty.txt')
Dif = Dificulty.read()
Dificulty.close()
optionEP = open('options/EnemyP.txt')
OEP = optionEP.read()
optionEP.close()

def checkOPP_changed(OPP):
    if OPP.get() == True:
        file = open('options/PlayerP.txt', 'w')
        file.write('True')
        file.close()
    elif OPP.get() == False:
        file = open('options/PlayerP.txt', 'w')
        file.write('False')
        file.close()

def checkOEP_changed(OEP):
    if OEP.get() == True:
        file = open('options/EnemyP.txt', 'w')
        file.write('True')
        file.close()
    elif OEP.get() == False:
        file = open('options/EnemyP.txt', 'w')
        file.write('False')
        file.close()

def on_change_Language(event):
    if cb.get() == "РУССКИЙ":
        file = open('options/Language.txt', 'w')
        file.write('RU')
        file.close()
    elif cb.get() == "ENGLISH":
        file = open('options/Language.txt', 'w')
        file.write('ENG')
        file.close()
    elif cb.get() == "中文":
        file = open('options/Language.txt', 'w')
        file.write('kitay')
        file.close()

def on_change_Dificulty(event):
    if cb1.get() == "EASY":
        file = open('options/Dificulty.txt', 'w')
        file.write('Easy')
        file.close()
    elif cb1.get() == "NORMAL":
        file = open('options/Dificulty.txt', 'w')
        file.write('Normal')
        file.close()
    elif cb1.get() == "HARD":
        file = open('options/Dificulty.txt', 'w')
        file.write('Hard')
        file.close()

path = "assets/Bigger_assets/Background.png"


''' Создание окна '''
window = tk.Tk()

window.iconbitmap('icon.ico')
window.title("Ball Game Options")
window.geometry("512x512")
window.resizable(False, False)
canvas = tk.Canvas(window, width=512, height=512)
canvas.pack()

image = tk.PhotoImage(file=path)
canvas.create_image(0, 0, image=image, anchor="nw")
stateOPP = tk.BooleanVar()
stateOEP = tk.BooleanVar()


''' Текст и кнопки '''
if Lang == "RU":
    button = tk.Button(window, text='Выход в меню', command=Menu)
    canvas.create_window((205, 455), anchor="nw", window=button, width=100, height=50)
elif Lang == "ENG":
    button = tk.Button(window, text='Exit to the menu', command=Menu)
    canvas.create_window((205, 455), anchor="nw", window=button, width=100, height=50)
elif Lang == "kitay":
    button = tk.Button(window, text='退出到菜单', command=Menu)
    canvas.create_window((205, 455), anchor="nw", window=button, width=100, height=50)
else:
    button = tk.Button(window, text='Exit to the menu', command=Menu)
    canvas.create_window((205, 455), anchor="nw", window=button, width=100, height=50)

if OPP == "True":
    stateOPP.set(True)
elif OPP == "False":
    stateOPP.set(False)
else:
    file = open('options/PlayerP.txt', 'w')
    file.write('False')
    file.close()
    stateOPP.set(False)

if OEP == "True":
    stateOEP.set(True)
elif OEP == "False":
    stateOEP.set(False)
else:
    file = open('options/EnemyP.txt', 'w')
    file.write('False')
    file.close()
    stateOEP.set(False)

if Lang == "RU":
    chk = Checkbutton(window, text='Пометить\nигрока', variable=stateOPP, command=lambda: checkOPP_changed(stateOPP))
    canvas.create_window((20, 20), anchor="nw", window=chk, width=88, height=40)

    chk1 = Checkbutton(window, text='Пометить\nврагов', variable=stateOEP, command=lambda: checkOEP_changed(stateOEP))
    canvas.create_window((20, 70), anchor="nw", window=chk1, width=88, height=40)

    canvas.create_text(160, 20, text="Язык", font="Verdana 10")
    canvas.create_text(260, 20, text="Сложность", font="Verdana 10")

elif Lang == "ENG":
    chk = Checkbutton(window, text='Tag\na player', variable=stateOPP, command=lambda: checkOPP_changed(stateOPP))
    canvas.create_window((20, 20), anchor="nw", window=chk, width=88, height=40)

    chk1 = Checkbutton(window, text='Tag\nthe enemies', variable=stateOEP, command=lambda: checkOEP_changed(stateOEP))
    canvas.create_window((20, 70), anchor="nw", window=chk1, width=88, height=40)

    canvas.create_text(160, 20, text="Language", font="Verdana 10")
    canvas.create_text(260, 20, text="Dificulty", font="Verdana 10")
elif Lang == "kitay":
    chk = Checkbutton(window, text='标记玩家', variable=stateOPP, command=lambda: checkOPP_changed(stateOPP))
    canvas.create_window((20, 20), anchor="nw", window=chk, width=88, height=40)

    chk1 = Checkbutton(window, text='标记敌人', variable=stateOEP, command=lambda: checkOEP_changed(stateOEP))
    canvas.create_window((20, 70), anchor="nw", window=chk1, width=88, height=40)

    canvas.create_text(160, 20, text="语言", font="Verdana 10")
    canvas.create_text(260, 20, text="复杂性", font="Verdana 10")
else:
    chk = Checkbutton(window, text='Tag\na player', variable=stateOPP, command=lambda: checkOPP_changed(stateOPP))
    canvas.create_window((20, 20), anchor="nw", window=chk, width=88, height=40)

    chk1 = Checkbutton(window, text='Tag\nthe enemies', variable=stateOEP, command=lambda: checkOEP_changed(stateOEP))
    canvas.create_window((20, 70), anchor="nw", window=chk1, width=88, height=40)

    canvas.create_text(160, 20, text="Language", font="Verdana 10")
    canvas.create_text(260, 20, text="Dificulty", font="Verdana 10")

cb = Combobox(window, state="readonly", values=("ENGLISH", "РУССКИЙ", "中文"))
canvas.create_window((120, 30), anchor="nw", window=cb, width=80, height=30)

if Lang == "kitay":
    cb.current(2)
elif Lang == "RU":
    cb.current(1)
elif Lang == "ENG":
    cb.current(0)
else:
    file = open('options/Language.txt', 'w')
    file.write('ENG')
    file.close()
    cb.current(0)

cb.bind("<<ComboboxSelected>>", on_change_Language)

cb1 = Combobox(window, state="readonly", values=("EASY", "NORMAL", "HARD"))
canvas.create_window((220, 30), anchor="nw", window=cb1, width=80, height=30)

if Dif == "Easy":
    cb1.current(0)
elif Dif == "Normal":
    cb1.current(1)
elif Dif == "Hard":
    cb1.current(2)
else:
    file = open('options/Dificulty.txt', 'w')
    file.write('Normal')
    file.close()
    cb.current(1)

cb1.bind("<<ComboboxSelected>>", on_change_Dificulty)


window.mainloop()
