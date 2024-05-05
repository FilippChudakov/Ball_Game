import tkinter as tk
from PIL import ImageTk, Image
import os
import subprocess


p = os.path.abspath('BallGame.py')
def Start():
    window.destroy()
    subprocess.run(["python", "BallGame.py"])

path = "assets/Background1.png"

window = tk.Tk()

window.geometry("512x512")
canvas = tk.Canvas(window, width=512, height=512)
canvas.pack()
image = tk.PhotoImage(file=path)
canvas.create_image(0, 0, image=image, anchor="nw")

button = tk.Button(window, text='Выход', command=window.quit)
canvas.create_window((205, 355), anchor="nw", window=button, width=100, height=50)

button = tk.Button(window, text='Играть', command=Start)
canvas.create_window((205, 155), anchor="nw", window=button, width=100, height=50)

button = tk.Button(window, text='Обучение', command=window.quit)
canvas.create_window((205, 255), anchor="nw", window=button, width=100, height=50)

canvas.create_text(255, 100, text="Ball Game", fill="Red", font="Verdana 30")

window.mainloop()
