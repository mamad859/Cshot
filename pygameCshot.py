import pygame as pg
from pygame.locals import *

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
cyan = (0, 255, 255)
purple = (150, 0, 150)
black = (0, 0, 0)

image = pg.image.load("target.png")
image = pg.transform.scale(image, (45, 45))
bomb = pg.image.load("bomb1.png")
bomb = pg.transform.scale(bomb, (80, 100))
rocket = pg.image.load("rocket.png")
rocket = pg.transform.scale(rocket, (60, 60))
timer = pg.image.load("clock.png")
timer = pg.transform.scale(timer, (60, 60))
bullet = pg.image.load("bullet.png")
bullet = pg.transform.scale(bullet, (60, 60))

def display_time(screen, time_left, x, y, color):
    font = pg.font.SysFont('calibri', 25)
    text = font.render(f"Time : {int(time_left)}s", True, color)
    screen.blit(text, (x, y))

def display_score(screen, player, x, y):
    font = pg.font.SysFont('calibri' , 20)
    text = font.render(f"{player.name} scores : {player.score}", True, blue)
    text2 = font.render(f"remaining bullets : {player.bullet}", True, red)
    screen.blit(text, (x, y))
    screen.blit(text2, (x, y + 20))

def display_result(screen, player1, player2):
    font = pg.font.SysFont('calibri', 35)
    if player1.score > player2.score:
        result_text = font.render(f"Congrats, {player1.name} is the winner!", True, blue)
    elif player2.score > player1.score:
        result_text = font.render(f"Congrats, {player2.name} is the winner!", True, blue)
    else:
        result_text = font.render("...Draw...", True, red)
    screen.blit(result_text , (250 , 270))
