import tkinter as tk
from tkinter.ttk import Checkbutton
from PIL import ImageTk, Image
import os
import subprocess


''' Создание функций и путей к картинкам '''
p = os.path.abspath('main.py')
def Menu():
    window.destroy()
    subprocess.run(["python", "main.py"])

def checkOPP_changed(OPP):
    if OPP.get() == True:
        file = open('options/PlayerP.txt', 'w')
        file.write('True')
        file.close()
    elif OPP.get() == False:
        file = open('options/PlayerP.txt', 'w')
        file.write('False')
        file.close()

path = "assets/Bigger_assets/Background.png"


''' Создание окна '''
window = tk.Tk()

window.iconbitmap('icon.ico')
window.geometry("512x512")
window.resizable(False, False)
window.title("Ball Game Options")
canvas = tk.Canvas(window, width=512, height=512)
canvas.pack()

image = tk.PhotoImage(file=path)
canvas.create_image(0, 0, image=image, anchor="nw")


''' Текст и кнопки '''
button = tk.Button(window, text='Выход в меню', command=Menu)
canvas.create_window((205, 455), anchor="nw", window=button, width=100, height=50)


''' Прочтение настроек '''
optionPP = open('options/PlayerP.txt')
OPP = optionPP.read()
optionPP.close()
stateOPP = tk.BooleanVar()

if OPP == "True":
    stateOPP.set(True)
elif OPP == "False":
    stateOPP.set(False)
else:
    file = open('options/PlayerP.txt', 'w')
    file.write('False')
    file.close()
    stateOPP.set(False)

chk = Checkbutton(window, text='Пометить\nигрока', variable=stateOPP, command=lambda: checkOPP_changed(stateOPP))
canvas.create_window((20, 20), anchor="nw", window=chk, width=80, height=40)


window.mainloop()
