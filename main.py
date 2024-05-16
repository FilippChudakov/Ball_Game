import tkinter as tk
from PIL import ImageTk, Image
import os
import subprocess


''' Создание функций и путей к картинкам '''
p = os.path.abspath('BallGame.py')
def Start():
    window.destroy()
    subprocess.run(["python", "BallGame.py"])

p = os.path.abspath('Tutorial.py')
def Tutorial():
    window.destroy()
    subprocess.run(["python", "Tutorial.py"])

p = os.path.abspath('Options.py')
def Options():
    window.destroy()
    subprocess.run(["python", "Options.py"])

path = "assets/Bigger_assets/Background.png"


''' Создание окна '''
window = tk.Tk()

window.iconbitmap('icon.ico')
window.geometry("512x512")
window.resizable(False, False)
window.title("Ball Game Menu")
canvas = tk.Canvas(window, width=512, height=512)
canvas.pack()

image = tk.PhotoImage(file=path)
canvas.create_image(0, 0, image=image, anchor="nw")


''' Текст и кнопки '''
button = tk.Button(window, text='Играть', command=Start)
canvas.create_window((205, 155), anchor="nw", window=button, width=100, height=50)

button = tk.Button(window, text='Обучение', command=Tutorial)
canvas.create_window((205, 255), anchor="nw", window=button, width=100, height=50)

button = tk.Button(window, text='Выход', command=window.quit)
canvas.create_window((205, 355), anchor="nw", window=button, width=100, height=50)

button = tk.Button(window, text='Настройки', command=Options)
canvas.create_window((405, 455), anchor="nw", window=button, width=100, height=50)

canvas.create_text(255, 100, text="Ball Game", fill="Red", font="Verdana 30")


window.mainloop()
