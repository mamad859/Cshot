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

def display_time(screen, remaining_time, pos_x, pos_y, color):
    time_font = pg.font.SysFont('Bauhaus 93', 30)
    # time_font = pg.font.SysFont('Arial Black', 28)
    
    time_text = time_font.render(f"TIME: {int(remaining_time)}s", True, color)
    screen.blit(time_text, (pos_x, pos_y))

def display_score(screen, player, pos_x, pos_y):
    score_font = pg.font.SysFont('Orbitron', 22)
    # score_font = pg.font.SysFont('Verdana', 20)
    
    score_text = score_font.render(f"{player.name.upper()}: {player.score} PTS", True, blue)
    
    bullets_text = score_font.render(f"AMMO: {player.bullet}", True, red)
    
    screen.blit(score_text, (pos_x, pos_y))
    screen.blit(bullets_text, (pos_x, pos_y + 25))

def display_result(screen, player1, player2):
    title_font = pg.font.SysFont('Arial', 40, bold=True)
    score_font = pg.font.SysFont('Calibri', 35)
    winner_color = (50, 150, 255)
    draw_color = (255, 70, 70)
    text_shadow = (20, 20, 20)
    
    if player1.score > player2.score:
        winner_text = f"Winner: {player1.name}!"
        result_text = f"Congratulation!"
    elif player2.score > player1.score:
        winner_text = f"Winner: {player2.name}!"
        result_text = f"Congratulation!"
    else:
        winner_text = "Tie!"
        result_text = "It was a good game!"
    
    title_surface = title_font.render(winner_text, True, winner_color if winner_text != "Tie!" else draw_color)
    subtitle_surface = score_font.render(result_text, True, (240, 240, 240))  # سفید روشن
    
    title_shadow = title_font.render(winner_text, True, text_shadow)
    subtitle_shadow = score_font.render(result_text, True, text_shadow)
    
    title_rect = title_surface.get_rect(center=(screen.get_width()//2, 250))
    subtitle_rect = subtitle_surface.get_rect(center=(screen.get_width()//2, 300))
    
    screen.blit(title_shadow, (title_rect.x+2, title_rect.y+2))
    screen.blit(subtitle_shadow, (subtitle_rect.x+2, subtitle_rect.y+2))
    
    screen.blit(title_surface, title_rect)
    screen.blit(subtitle_surface, subtitle_rect)
    
    score_text = f"{player1.score} - {player2.score}"
    score_surface = title_font.render(score_text, True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(screen.get_width()//2, 200))
    screen.blit(score_surface, score_rect)

