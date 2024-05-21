import tkinter as tk
from PIL import ImageTk, Image
import os
import subprocess
from random import randint


''' Прочтение настроек '''
Language = open('options/Language.txt')
Lang = Language.read()
Language.close()
Dificulty = open('options/Dificulty.txt')
Dif = Dificulty.read()
Dificulty.close()


''' Создание функций и путей к картинкам '''
p = os.path.abspath('BallGameEasy.exe')
p1 = os.path.abspath('BallGameNormal.exe')
p2 = os.path.abspath('BallGameHard.exe')
def Start_Normal():
    if Dif == "Easy":
        window.destroy()
        subprocess.run(["python", "BallGameEasy.py"])
    elif Dif == "Normal":
        window.destroy()
        subprocess.run(["python", "BallGameNormal.py"])
    elif Dif == "Hard":
        window.destroy()
        subprocess.run(["python", "BallGameHard.py"])
    else:
        window.destroy()
        subprocess.run(["python", "BallGameNormal.py"])

z = os.path.abspath('Tutorial.py')
def Tutorial():
    window.destroy()
    subprocess.run(["python", "Tutorial.py"])

q = os.path.abspath('Options.py')
def Options():
    window.destroy()
    subprocess.run(["python", "Options.py"])


path = "assets/Bigger_assets/Background.png"


''' Создание окна '''
window = tk.Tk()

window.iconbitmap('icon.ico')
window.title("Ball Game Menu")
window.geometry("512x512")
window.resizable(False, False)
canvas = tk.Canvas(window, width=512, height=512)
canvas.pack()

image = tk.PhotoImage(file=path)
canvas.create_image(0, 0, image=image, anchor="nw")


''' Текст и кнопки '''
if Lang == "RU":
    button = tk.Button(window, text='Играть', command=Start_Normal)
    canvas.create_window((205, 155), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='Обучение', command=Tutorial)
    canvas.create_window((205, 255), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='Выход', command=window.quit)
    canvas.create_window((205, 355), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='Настройки', command=Options)
    canvas.create_window((405, 455), anchor="nw", window=button, width=100, height=50)

elif Lang == "ENG":
    button = tk.Button(window, text='Play', command=Start_Normal)
    canvas.create_window((205, 155), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='Tutorial', command=Tutorial)
    canvas.create_window((205, 255), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='Quit', command=window.quit)
    canvas.create_window((205, 355), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='Options', command=Options)
    canvas.create_window((405, 455), anchor="nw", window=button, width=100, height=50)

elif Lang == "kitay":
    button = tk.Button(window, text='游戏', command=Start_Normal)
    canvas.create_window((205, 155), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='教程', command=Tutorial)
    canvas.create_window((205, 255), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='退出', command=window.quit)
    canvas.create_window((205, 355), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='选项', command=Options)
    canvas.create_window((405, 455), anchor="nw", window=button, width=100, height=50)

else:
    button = tk.Button(window, text='Play', command=Start_Normal)
    canvas.create_window((205, 155), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='Tutorial', command=Tutorial)
    canvas.create_window((205, 255), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='Quit', command=window.quit)
    canvas.create_window((205, 355), anchor="nw", window=button, width=100, height=50)

    button = tk.Button(window, text='Options', command=Options)
    canvas.create_window((405, 455), anchor="nw", window=button, width=100, height=50)

canvas.create_text(255, 100, text="Ball Game", fill="Red", font="Verdana 30")


window.mainloop()
