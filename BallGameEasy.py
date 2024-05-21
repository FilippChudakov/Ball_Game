from os import environ
import pygame
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import *
from random import randint
import os
import subprocess
from random import randint


p = os.path.abspath('main.py')
def Menu():
    subprocess.run(["python", "main.py"])


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


''' Окно игры '''
W = 512
H = 512

window = display.set_mode((W, H))
if OB == "False":
    display.set_caption('BallGame Easy')
    background = transform.scale(image.load("assets/Background.png"), (W, H))
    pygame_icon = image.load('icon.ico')
elif OB == "True":
    display.set_caption('BugGame YsaE')
    background = transform.scale(image.load("assets/BUGground.png"), (W, H))
    pygame_icon = image.load('assets/Bug.ico')
else:
    display.set_caption('BallGame Easy')
    background = transform.scale(image.load("assets/Background.png"), (W, H))
    pygame_icon = image.load('icon.ico')
display.set_icon(pygame_icon)


''' Текст '''
menu = False
GameOver = 0
game = None
countSuper = 0
count = 0
count1 = 0
count2 = 0
font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None, 45)
counter = font1.render(str(count), True, (0, 0, 0))
if OB == "False":
    if Lang == "RU":
        gameover = font1.render("Игра окончена!", True, (0, 0, 0))
        gameover1 = font2.render("C - закрыть", True, (0, 0, 0))
        gameover2 = font2.render("M - меню", True, (0, 0, 0))
    elif Lang == "ENG":
        gameover = font1.render("Game Over!", True, (0, 0, 0))
        gameover1 = font2.render("C - close", True, (0, 0, 0))
        gameover2 = font2.render("M - menu", True, (0, 0, 0))
    else:
        gameover = font1.render("Game Over!", True, (0, 0, 0))
        gameover1 = font2.render("C - close", True, (0, 0, 0))
        gameover2 = font2.render("M - menu", True, (0, 0, 0))
elif OB == "True":
    if Lang == "RU":
        gameover = font1.render("ГАрИ ЕноКАЧоН!", True, (0, 0, 0))
        gameover1 = font2.render("C - АзТьырк", True, (0, 0, 0))
        gameover2 = font2.render("M - неМю", True, (0, 0, 0))
    elif Lang == "ENG":
        gameover = font1.render("Emga EvrO!", True, (0, 0, 0))
        gameover1 = font2.render("C - Loces", True, (0, 0, 0))
        gameover2 = font2.render("M - neMu", True, (0, 0, 0))
    else:
        gameover = font1.render("Emga EvrO!", True, (0, 0, 0))
        gameover1 = font2.render("C - Loces", True, (0, 0, 0))
        gameover2 = font2.render("M - neMu", True, (0, 0, 0))
else:
    if Lang == "RU":
        gameover = font1.render("Игра окончена!", True, (0, 0, 0))
        gameover1 = font2.render("C - закрыть", True, (0, 0, 0))
        gameover2 = font2.render("M - меню", True, (0, 0, 0))
    elif Lang == "ENG":
        gameover = font1.render("Game Over!", True, (0, 0, 0))
        gameover1 = font2.render("C - close", True, (0, 0, 0))
        gameover2 = font2.render("M - menu", True, (0, 0, 0))
    else:
        gameover = font1.render("Game Over!", True, (0, 0, 0))
        gameover1 = font2.render("C - close", True, (0, 0, 0))
        gameover2 = font2.render("M - menu", True, (0, 0, 0))


''' Игровой таймер '''
clock = time.Clock()
FPS = 60


''' Класс GameSprite '''
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed, sprite_infected):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (65, 65))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.infected = sprite_infected

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if self.rect.x >= W and self.rect.y >= H:
            pass
        else:
            if keys[K_a] or keys[K_d] or keys[K_w] or keys[K_s]:
                if keys[K_a] and self.rect.x > 0:
                    self.rect.x -= self.speed
                if keys[K_d] and self.rect.x < W - 80:
                    self.rect.x += self.speed
                if keys[K_w] and self.rect.y > 0:
                    self.rect.y -= self.speed
                if keys[K_s] and self.rect.y < H - 80:
                    self.rect.y += self.speed
            elif keys[K_LEFT] or keys[K_RIGHT] or keys[K_UP] or keys[K_DOWN]:
                if keys[K_LEFT] and self.rect.x > 0:
                    self.rect.x -= self.speed
                if keys[K_RIGHT] and self.rect.x < W - 80:
                    self.rect.x += self.speed
                if keys[K_UP] and self.rect.y > 0:
                    self.rect.y -= self.speed
                if keys[K_DOWN] and self.rect.y < H - 80:
                    self.rect.y += self.speed
        if keys[K_r] and self.rect.x == 1000 and self.rect.y == 1000:
            self.rect.x = 224
            self.rect.y = 224
            global GameOver
            GameOver = 0
        if keys[K_c]:
            global game
            game = False
        elif keys[K_m]:
            global menu
            menu = True
            game = False

    def SwitchPl(self, plsup):
        global countSuper
        if countSuper == 4:
            plsup.rect.x = self.rect.x
            plsup.rect.y = self.rect.y
            self.rect.x = 1000
            self.rect.y = 1000
            countSuper = -4
        elif countSuper == -1:
            self.rect.x = plsup.rect.x
            self.rect.y = plsup.rect.y
            plsup.rect.x = 900
            plsup.rect.y = 900
            countSuper += 1

    def Eat(self, enemy):
        if enemy.rect.x == self.rect.x and enemy.rect.y == self.rect.y:
            global count
            global counter
            global count1
            global count2
            global countSuper
            if enemy.infected == True and self.infected == False:
                self.rect.x = 1000
                self.rect.y = 1000
                global GameOver
                GameOver = 1
            elif enemy.infected == False:
                enemy.rect.x = 1100
                enemy.rect.y = 1100
                count += 1
                count1 += 1
                counter = font1.render(str(count), True, (0, 0, 0))
                countSuper += 1
            if enemy.infected == True and self.infected == True:
                countSuper += 1
                enemy.rect.x = 1200
                enemy.rect.y = 1200
                count2 += 1
                count += 2
                counter = font1.render(str(count), True, (0, 0, 0))

class enemy(GameSprite):
    def update(self):
        if self.rect.x >= W and self.rect.y >= H:
            pass
        else:
            rand = randint(0, 3)
            if rand == 0:
                if self.rect.x > 0:
                    self.rect.x -= self.speed
            elif rand == 1:
                if self.rect.x < W - 80:
                    self.rect.x += self.speed
            elif rand == 2:
                if self.rect.y > 0:
                    self.rect.y -= self.speed
            elif rand == 3:
                if self.rect.y < H - 80:
                    self.rect.y += self.speed

    def Eat(self, enemy):
        if enemy.rect.x == self.rect.x and enemy.rect.y == self.rect.y:
            enemy.rect.x = 1100
            enemy.rect.y = 1100
            global count1
            count1 += 1

if OB == "False":
    if OPP == "False":
        Player = player("assets/Player.png", 224, 224, 32, False)
        PlayerSuper = player("assets/PlayerSuper.png", 900, 900, 32, True)
    if OPP == "True":
        Player = player("assets/PlayerP.png", 224, 224, 32, False)
        PlayerSuper = player("assets/PlayerSuperP.png", 900, 900, 32, True)
    else:
        Player = player("assets/Player.png", 224, 224, 32, False)
        PlayerSuper = player("assets/PlayerSuper.png", 900, 900, 32, True)
    if OEP == "False":
        Enemy = enemy("assets/Enemy.png", 128, 128, 32, False)
        Enemy1 = enemy("assets/Enemy1.png", 320, 320, 32, False)
        Enemy2 = enemy("assets/Enemy2.png", 320, 128, 32, True)
        Enemy3 = enemy("assets/Enemy3.png", 128, 320, 32, True)
        Enemy4 = enemy("assets/Enemy4.png", 0, 224, 32, False)
    elif OEP == "True":
        Enemy = enemy("assets/EnemyP.png", 128, 128, 32, False)
        Enemy1 = enemy("assets/Enemy1P.png", 320, 320, 32, False)
        Enemy2 = enemy("assets/Enemy2P.png", 320, 128, 32, True)
        Enemy3 = enemy("assets/Enemy3P.png", 128, 320, 32, True)
        Enemy4 = enemy("assets/Enemy4P.png", 0, 224, 32, False)
    else:
        Enemy = enemy("assets/Enemy.png", 128, 128, 32, False)
        Enemy1 = enemy("assets/Enemy1.png", 320, 320, 32, False)
        Enemy2 = enemy("assets/Enemy2.png", 320, 128, 32, True)
        Enemy3 = enemy("assets/Enemy3.png", 128, 320, 32, True)
        Enemy4 = enemy("assets/Enemy4.png", 0, 224, 32, False)
elif OB == "True":
    PlayerBUG = randint(1, 3)
    EnemyBUG = randint(1, 3)
    if PlayerBUG == 1:
        Player = player("assets/EnemyP.png", 224, 224, 32, False)
        PlayerSuper = player("assets/Enemy3.png", 900, 900, 32, True)
    elif PlayerBUG == 2:
        Player = player("assets/PlayerSuper.png", 224, 224, 32, False)
        PlayerSuper = player("assets/Enemy2P.png", 900, 900, 32, True)
    elif PlayerBUG == 3:
        Player = player("assets/Enemy1.png", 224, 224, 32, False)
        PlayerSuper = player("assets/Player.png", 900, 900, 32, True)
    if EnemyBUG == 1:
        Enemy = enemy("assets/Enemy3P.png", 128, 128, 32, False)
        Enemy1 = enemy("assets/PlayerP.png", 320, 320, 32, False)
        Enemy2 = enemy("assets/PlayerSuper.png", 320, 128, 32, True)
        Enemy3 = enemy("assets/Enemy1.png", 128, 320, 32, True)
        Enemy4 = enemy("assets/Enemy2.png", 0, 224, 32, False)
    elif EnemyBUG == 2:
        Enemy = enemy("assets/Enemy2.png", 128, 128, 32, False)
        Enemy1 = enemy("assets/Enemy1P.png", 320, 320, 32, False)
        Enemy2 = enemy("assets/Player.png", 320, 128, 32, True)
        Enemy3 = enemy("assets/Enemy3.png", 128, 320, 32, True)
        Enemy4 = enemy("assets/Enemy5P.png", 0, 224, 32, False)
    elif EnemyBUG == 3:
        Enemy = enemy("assets/PlayerSuperP.png", 128, 128, 32, False)
        Enemy1 = enemy("assets/Enemy2P.png", 320, 320, 32, False)
        Enemy2 = enemy("assets/EnemyP.png", 320, 128, 32, True)
        Enemy3 = enemy("assets/Enemy.png", 128, 320, 32, True)
        Enemy4 = enemy("assets/Enemy1.png", 0, 224, 32, False)
else:
    if OPP == "False":
        Player = player("assets/Player.png", 224, 224, 32, False)
        PlayerSuper = player("assets/PlayerSuper.png", 900, 900, 32, True)
    if OPP == "True":
        Player = player("assets/PlayerP.png", 224, 224, 32, False)
        PlayerSuper = player("assets/PlayerSuperP.png", 900, 900, 32, True)
    else:
        Player = player("assets/Player.png", 224, 224, 32, False)
        PlayerSuper = player("assets/PlayerSuper.png", 900, 900, 32, True)
    if OEP == "False":
        Enemy = enemy("assets/Enemy.png", 128, 128, 32, False)
        Enemy1 = enemy("assets/Enemy1.png", 320, 320, 32, False)
        Enemy2 = enemy("assets/Enemy2.png", 320, 128, 32, True)
        Enemy3 = enemy("assets/Enemy3.png", 128, 320, 32, True)
        Enemy4 = enemy("assets/Enemy4.png", 0, 224, 32, False)
    elif OEP == "True":
        Enemy = enemy("assets/EnemyP.png", 128, 128, 32, False)
        Enemy1 = enemy("assets/Enemy1P.png", 320, 320, 32, False)
        Enemy2 = enemy("assets/Enemy2P.png", 320, 128, 32, True)
        Enemy3 = enemy("assets/Enemy3P.png", 128, 320, 32, True)
        Enemy4 = enemy("assets/Enemy4P.png", 0, 224, 32, False)
    else:
        Enemy = enemy("assets/Enemy.png", 128, 128, 32, False)
        Enemy1 = enemy("assets/Enemy1.png", 320, 320, 32, False)
        Enemy2 = enemy("assets/Enemy2.png", 320, 128, 32, True)
        Enemy3 = enemy("assets/Enemy3.png", 128, 320, 32, True)
        Enemy4 = enemy("assets/Enemy4.png", 0, 224, 32, False)


''' Игровой цикл '''
sec = 0
sec1 = 0
sec2 = 0
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if game:
        window.blit(background, (0, 0))

        Enemy.reset()
        Enemy1.reset()
        Enemy4.reset()
        Player.reset()
        Enemy2.reset()
        Enemy3.reset()
        PlayerSuper.reset()

        if sec == 15:
            Enemy.update()
            Enemy1.update()
            Enemy2.update()
            Enemy3.update()
            Enemy4.update()
            Player.update()
            PlayerSuper.update()
            Player.Eat(Enemy)
            Player.Eat(Enemy1)
            Player.Eat(Enemy2)
            Player.Eat(Enemy3)
            Player.Eat(Enemy4)
            PlayerSuper.Eat(Enemy)
            PlayerSuper.Eat(Enemy1)
            PlayerSuper.Eat(Enemy2)
            PlayerSuper.Eat(Enemy3)
            PlayerSuper.Eat(Enemy4)
            Enemy2.Eat(Enemy)
            Enemy2.Eat(Enemy1)
            Enemy2.Eat(Enemy4)
            Enemy3.Eat(Enemy)
            Enemy3.Eat(Enemy1)
            Enemy3.Eat(Enemy4)
            Player.SwitchPl(PlayerSuper)
            sec = 0
        else:
            sec += 1

        if count1 == 3:
            if sec1 == 90:
                Enemy.rect.x = 128
                Enemy.rect.y = 128
                Enemy1.rect.x = 320
                Enemy1.rect.y = 320
                Enemy4.rect.x = 0
                Enemy4.rect.y = 224
                count1 = 0
                sec1 = 0
            else:
                sec1 += 1

        if count2 == 2:
            if sec2 == 240:
                Enemy2.rect.x = 320
                Enemy2.rect.y = 128
                Enemy3.rect.x = 128
                Enemy3.rect.y = 320
                count2 = 0
                sec2 = 0
            else:
                sec2 += 1

        window.blit(counter, (10, 10))
        if GameOver == 1:
            if Lang == "RU":
                window.blit(gameover, (100, 200))
            elif Lang == "ENG":
                window.blit(gameover, (125, 200))
            else:
                window.blit(gameover, (125, 200))
            window.blit(gameover1, (200, 250))
            window.blit(gameover2, (200, 280))

    display.update()
    clock.tick(FPS)

pygame.quit()
if menu == True:
    Menu()
