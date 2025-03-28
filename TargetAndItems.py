import random

def randpos():
    x = random.randint(80, 720)
    y = random.randint(80, 520)
    return (x, y)

targets = [randpos() for _ in range(7)]

class Target:
    def __init__(self, type, radius):
        self.x = targets[type][0]
        self.y = targets[type][1]
        self.radius = radius
    def check_hit(self, x_pos, y_pos, tar_num):
        if (self.radius + 5)**2 >= (x_pos - self.x - self.radius)**2 + (y_pos - self.y - self.radius)**2:
            global targets
            targets[tar_num] = randpos()
            return True
        
class Sable(Target):
    def apply_effect(self, score):
        return score + 1
    
class Speed(Target):
    def apply_effect(self, speed):
        return speed + 5

class Bomb(Target):
    def apply_effect(self, score):
        return score - 3
    
class Bullet(Target):
    def apply_effect(self, bullet):
        return bullet + 5
    
class Time(Target):
    def apply_effect(self, time):
        return time + 10
    
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullet = 12
        self.score = 0
        self.time = 75
        self.speed = 20
