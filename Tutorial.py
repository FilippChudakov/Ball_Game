import tkinter as tk
from PIL import ImageTk, Image
import os
import subprocess


''' Создание функций и путей к картинкам '''
p = os.path.abspath('main.py')
def Menu():
    window.destroy()
    subprocess.run(["python", "main.py"])

path = "assets/Background1.png"
path1 = "assets/Tutorial_assets/Player.png"
path2 = "assets/Tutorial_assets/PlayerSuper.png"
path3 = "assets/Tutorial_assets/Enemy.png"
path4 = "assets/Tutorial_assets/Enemy1.png"
path5 = "assets/Tutorial_assets/Enemy2.png"
path6 = "assets/Tutorial_assets/Enemy3.png"


''' Создание окна '''
window = tk.Tk()

window.iconbitmap('icon.ico')
window.geometry("512x512")
window.resizable(False, False)
window.title("Ball Game Tutorial")
canvas = tk.Canvas(window, width=512, height=512)
canvas.pack()


''' Загрузка изображений на окно '''
image = tk.PhotoImage(file=path)
image1 = tk.PhotoImage(file=path1)
image2 = tk.PhotoImage(file=path2)
image3 = tk.PhotoImage(file=path3)
image4 = tk.PhotoImage(file=path4)
image5 = tk.PhotoImage(file=path5)
image6 = tk.PhotoImage(file=path6)

canvas.create_image(0, 0, image=image, anchor="nw")
canvas.create_image(64, 64, image=image1, anchor="nw")
canvas.create_image(64, 128, image=image2, anchor="nw")
canvas.create_image(64, 192, image=image3, anchor="nw")
canvas.create_image(128, 192, image=image4, anchor="nw")
canvas.create_image(64, 256, image=image5, anchor="nw")
canvas.create_image(128, 256, image=image6, anchor="nw")


''' Текст и кнопки '''
canvas.create_text(255, 35, text="Ball Game Tutorial", fill="Red", font="Verdana 30")

canvas.create_text(256, 100, text="<-- Это вы\n управление: (WASD и стрелочки)", fill="Red", font="Verdana 10")
canvas.create_text(256, 166, text="<-- Это тоже вы\n управление: (WASD и стрелочки)", fill="Red", font="Verdana 10")

canvas.create_text(346, 226, text="<-- Это враги (еда)\n безобидные ничего не могут вам сделать", fill="Red", font="Verdana 10")
canvas.create_text(296, 290, text="<-- Это враги (опасные)\n опасные могут вас съесть", fill="Red", font="Verdana 10")

button = tk.Button(window, text='Выход в меню', command=Menu)
canvas.create_window((205, 455), anchor="nw", window=button, width=100, height=50)


window.mainloop()