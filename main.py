import pygame as pg
import random
from pygame.locals import *
import auth_system as aut
from classes import *
from pygameCshot import *

def shooting(player):
    if sable1.check_hit(player.x, player.y, 1):
        player.score = sable1.action(player.score)
    if sable2.check_hit(player.x, player.y, 2):
        player.score = sable2.action(player.score)
    if sable3.check_hit(player.x, player.y, 3):
        player.score = sable3.action(player.score)
    if bomb1.check_hit(player.x, player.y, 4):
        player.score = bomb1.action(player.score)
    if speed.check_hit(player.x, player.y, 5):
        player.speed = speed.action(player.speed)
    if time1.check_hit(player.x, player.y, 6):
        player.time = time1.action(player.time)
    if bullet1.check_hit(player.x, player.y, 7):
        player.bullet = bullet1.action(player.bullet)
