import tkinter as tk
from PIL import ImageTk, Image
import os
import subprocess


''' Прочтение настроек '''
optionPP = open('options/PlayerP.txt')
OPP = optionPP.read()
optionPP.close()
Language = open('options/Language.txt')
Lang = Language.read()
Language.close()
optionEP = open('options/EnemyP.txt')
OEP = optionEP.read()
optionEP.close()
Bug = open('options/Bug.txt')
OB = Bug.read()
Bug.close()


''' Создание функций и путей к картинкам '''
p = os.path.abspath('main.py')
def Menu():
    window.destroy()
    subprocess.run(["python", "main.py"])

if OB == "False":
    path = "assets/Bigger_assets/Background.png"
elif OB == "True":
    path = "assets/Bigger_assets/BUGground.png"
else:
    path = "assets/Bigger_assets/Background.png"
if OPP == "False":
    path1 = "assets/Bigger_assets/Player.png"
    path2 = "assets/Bigger_assets/PlayerSuper.png"
if OPP == "True":
    path1 = "assets/Bigger_assets/PlayerP.png"
    path2 = "assets/Bigger_assets/PlayerSuperP.png"
else:
    path1 = "assets/Bigger_assets/Player.png"
    path2 = "assets/Bigger_assets/PlayerSuper.png"
if OEP == "False":
    path3 = "assets/Bigger_assets/Enemy.png"
    path4 = "assets/Bigger_assets/Enemy1.png"
    path5 = "assets/Bigger_assets/Enemy2.png"
    path6 = "assets/Bigger_assets/Enemy3.png"
    path7 = "assets/Bigger_assets/Enemy4.png"
    path8 = "assets/Bigger_assets/Enemy5.png"
elif OEP == "True":
    path3 = "assets/Bigger_assets/EnemyP.png"
    path4 = "assets/Bigger_assets/Enemy1P.png"
    path5 = "assets/Bigger_assets/Enemy2P.png"
    path6 = "assets/Bigger_assets/Enemy3P.png"
    path7 = "assets/Bigger_assets/Enemy4P.png"
    path8 = "assets/Bigger_assets/Enemy5P.png"
else:
    path3 = "assets/Bigger_assets/Enemy.png"
    path4 = "assets/Bigger_assets/Enemy1.png"
    path5 = "assets/Bigger_assets/Enemy2.png"
    path6 = "assets/Bigger_assets/Enemy3.png"
    path7 = "assets/Bigger_assets/Enemy4.png"
    path8 = "assets/Bigger_assets/Enemy5.png"


''' Создание окна '''
window = tk.Tk()

if OB == "False":
    window.iconbitmap('icon.ico')
    window.title("Ball Game Tutorial")
elif OB == "True":
    window.iconbitmap('assets/Bug.ico')
    window.title("Bug Game Tutorial")
else:
    window.iconbitmap('icon.ico')
    window.title("Ball Game Tutorial")
window.geometry("512x512")
window.resizable(False, False)
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
image7 = tk.PhotoImage(file=path7)
image8 = tk.PhotoImage(file=path8)

canvas.create_image(0, 0, image=image, anchor="nw")
canvas.create_image(64, 64, image=image1, anchor="nw")
canvas.create_image(64, 128, image=image2, anchor="nw")
canvas.create_image(64, 192, image=image3, anchor="nw")
canvas.create_image(128, 192, image=image4, anchor="nw")
canvas.create_image(64, 256, image=image5, anchor="nw")
canvas.create_image(128, 256, image=image6, anchor="nw")
canvas.create_image(0, 192, image=image7, anchor="nw")
canvas.create_image(0, 256, image=image8, anchor="nw")


''' Текст и кнопки '''
canvas.create_text(255, 35, text="Ball Game Tutorial", fill="Red", font="Verdana 30")

if Lang == "RU":
    canvas.create_text(256, 100, text="<-- Это вы\n управление: (WASD и стрелочки)", fill="Red", font="Verdana 10")
    canvas.create_text(256, 166, text="<-- Это тоже вы\n управление: (WASD и стрелочки)", fill="Red", font="Verdana 10")

    canvas.create_text(346, 226, text="<-- Это враги (еда)\n безобидные ничего не могут вам сделать", fill="Red", font="Verdana 10")
    canvas.create_text(296, 290, text="<-- Это враги (опасные)\n опасные могут вас съесть", fill="Red", font="Verdana 10")

elif Lang == "ENG":
    canvas.create_text(236, 100, text="<-- This is you\n control: (WASD and arrows)", fill="Red", font="Verdana 10")
    canvas.create_text(236, 166, text="<-- This is also you\n control: (WASD and arrows)", fill="Red", font="Verdana 10")

    canvas.create_text(346, 226, text="<-- These are enemies (food)\n Harmless people can't do anything to you", fill="Red", font="Verdana 10")
    canvas.create_text(326, 290, text="<-- These are enemies (dangerous)\n Dangerous ones can eat you", fill="Red", font="Verdana 10")

elif Lang == "kitay":
    canvas.create_text(236, 100, text="<--这是你的控制: (WASD 和箭头)", fill="Red", font="Verdana 10")
    canvas.create_text(236, 166, text="<--这也是你的控制: (WASD 和箭头)", fill="Red", font="Verdana 10")

    canvas.create_text(346, 226, text="<--这些都是敌人 (食物) 无害的人对你无能为力", fill="Red", font="Verdana 10")
    canvas.create_text(326, 290, text="<--这些都是敌人 (危险的) 危险的可以吃掉你", fill="Red", font="Verdana 10")

else:
    canvas.create_text(236, 100, text="<-- This is you\n control: (WASD and arrows)", fill="Red", font="Verdana 10")
    canvas.create_text(236, 166, text="<-- This is also you\n control: (WASD and arrows)", fill="Red", font="Verdana 10")

    canvas.create_text(346, 226, text="<-- These are enemies (food)\n Harmless people can't do anything to you", fill="Red",font="Verdana 10")
    canvas.create_text(326, 290, text="<-- These are enemies (dangerous)\n Dangerous ones can eat you", fill="Red",font="Verdana 10")

if Lang == "RU":
    canvas.create_text(280, 380, text="Правила:"
                                      "\nВы играете за зелёный круг ваша задача есть другие круги"
                                      "\nно фиолетовый, жёлтые и голубой круги могут съесть вас"
                                      "\nа так же если вы съедите 4 круга вы сможете"
                                      "\nсъесть 3 любых круга."
                                      "\nЗа фиолетовый, жёлтые и голубой круги вы получите"
                                      "\nв два раза больше чем за других", fill="Red", font="Verdana 10")

    button = tk.Button(window, text='Выход в меню', command=Menu)
    canvas.create_window((205, 455), anchor="nw", window=button, width=100, height=50)

elif Lang == "ENG":
    canvas.create_text(280, 380, text="Rules:"
                                      "\nYou play for the green circle, your task is to eat other circles"
                                      "\nBut purple, yellow and light blue circles can eat you"
                                      "\nAlso, if you eat 4 circles, you can"
                                      "\nEat any 3 circles."
                                      "\nFor purple, yellow and light blue circles you will get"
                                      "\ntwice as much as for the others", fill="Red", font="Verdana 10")

    button = tk.Button(window, text='Exit to the menu', command=Menu)
    canvas.create_window((205, 455), anchor="nw", window=button, width=100, height=50)

elif Lang == "kitay":
    canvas.create_text(280, 380, text="规则："
                                      "\n你为绿色圆圈玩，你的任务是吃掉其他圆圈"
                                      "\n但紫色，黄色和蓝色的圆圈可以吃掉你"
                                      "\n另外，如果你吃4个圆圈，你可以"
                                      "\n吃任何3个圆圈。"
                                      "\n对于紫色，黄色和蓝色的圆圈，你会得到"
                                      "\n是其他人的两倍", fill="Red", font="Verdana 10")

    button = tk.Button(window, text='退出到菜单', command=Menu)
    canvas.create_window((205, 455), anchor="nw", window=button, width=100, height=50)

else:
    canvas.create_text(280, 380, text="Rules:"
                                      "\nYou play for the green circle, your task is to eat other circles"
                                      "\nBut purple, yellow and light blue circles can eat you"
                                      "\nAlso, if you eat 4 circles, you can"
                                      "\nEat any 3 circles."
                                      "\nFor purple, yellow and light blue circles you will get"
                                      "\ntwice as much as for the others", fill="Red", font="Verdana 10")

    button = tk.Button(window, text='Exit to the menu', command=Menu)
    canvas.create_window((205, 455), anchor="nw", window=button, width=100, height=50)


window.mainloop()
