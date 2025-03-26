import pygame as pg
import random
from pygame.locals import *
import auth_system as aut
from classes import *
from pygameCshot import *

def shooting(player):
    if sable1.check_hit(player.x, player.y, 1):
        player.score = sable1.apply_effect(player.score)
    if sable2.check_hit(player.x, player.y, 2):
        player.score = sable2.apply_effect(player.score)
    if sable3.check_hit(player.x, player.y, 3):
        player.score = sable3.apply_effect(player.score)
    if bomb1.check_hit(player.x, player.y, 4):
        player.score = bomb1.apply_effect(player.score)
    if speed.check_hit(player.x, player.y, 5):
        player.speed = speed.apply_effect(player.speed)
    if time1.check_hit(player.x, player.y, 6):
        player.time = time1.apply_effect(player.time)
    if bullet1.check_hit(player.x, player.y, 7):
        player.bullet = bullet1.apply_effect(player.bullet)
        
def main_game(player1_name, player2_name):
    pg.init()
    pg.mixer.init()
    pg.mixer.music.load("Cshot.mp3")
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(-1)
    
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Cshot")
    running = True
    while running:
        player1.time -= 1/60
        player2.time -= 1/60
        if (player1.time < 0 and player2.time < 0) or (player1.bullet == 0 and player2.bullet == 0):
            running = False
        for event in pg.event.get():
            if event.type == QUIT:
                running = False
                break
            elif event.type == KEYDOWN:
                if player1.time > 0:
                    if event.key == K_a and player1.x > 0:
                        player1.x -= player1.speed
                    elif event.key == K_w and player1.y > 0:
                        player1.y -= player1.speed
                    elif event.key == K_s and player1.y < 600:
                        player1.y += player1.speed
                    elif event.key == K_d and player1.x < 800:
                        player1.x += player1.speed
                    elif event.key == K_SPACE and player1.bullet > 0:
                        shooting(player1)
                        points.append([player1.x, player1.y, 1])
                        player1.bullet -= 1
                if player2.time > 0:
                    if event.key == K_DOWN and player2.y < 600:
                        player2.y += player2.speed
                    elif event.key == K_UP and player2.y > 0:
                        player2.y -= player2.speed
                    elif event.key == K_RIGHT and player2.x < 800:
                        player2.x += player2.speed
                    elif event.key == K_LEFT and player2.x > 0:
                        player2.x -= player2.speed
                    elif event.key == K_RETURN and player2.bullet > 0:
                        shooting(player2)
                        points.append([player2.x, player2.y, 2])
                        player2.bullet -= 1
                elif event.key == K_ESCAPE:
                    running = False
                    pg.quit()

        screen.fill(cyan)

        display_time(screen, player1.time, 5, 60, purple)
        display_time(screen, player2.time, 630, 60, purple)

        for point in points:
            if point[2] == 1:
                pg.draw.circle(screen, red, (point[0], point[1]), 5)
            elif point[2] == 2:
                pg.draw.circle(screen, blue, (point[0], point[1]), 5)
        for target in range(3):
            screen.blit(image , (targets[target][0] , targets[target][1]))

        screen.blit(bomb, (targets[3][0], targets[3][1]))
        screen.blit(rocket, (targets[4][0], targets[4][1]))
        screen.blit(timer, (targets[5][0], targets[5][1]))
        screen.blit(bullet, (targets[6][0], targets[6][1]))

        display_score(screen, player1, 5, 10)
        display_score(screen, player2, 630, 10)

        sable1 = Sable(1, 25)
        sable2 = Sable(2, 25)
        sable3 = Sable(3, 25)
        bomb1 = Bomb(4, 50)
        speed = Speed(5, 30)
        time1 = Time(6, 30)
        bullet1 = Bullet(7, 30)
        pg.display.update()
        clock.tick(60)

    display_result(screen, player1, player2)

    pg.display.flip()
    pg.time.wait(4000)
    pg.quit()
    
if __name__ == "__main__" :
    sable1 = Sable(1, 25)
    sable2 = Sable(2, 25)
    sable3 = Sable(3, 25)
    bomb1 = Bomb(4, 50)
    speed = Speed(5, 25)
    time1 = Time(6, 25)
    bullet1 = Bullet(7, 30)

    player1 = Player(random.randint(10, 790), random.randint(10, 590))
    player2 = Player(random.randint(10, 790), random.randint(10, 590))
    player1_name, player2_name = "", ""
    player1.name = player1_name ; player2.name = player2_name
    points = []
    clock = pg.time.Clock()

    player1_name,player2_name = aut.start_game()
    main_game(player1_name, player2_name)
