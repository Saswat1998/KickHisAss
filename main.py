import pygame
import random
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Kick His Ass')
clock = pygame.time.Clock()
my_avatar = pygame.image.load('destroyer.png')
fireball = pygame.image.load('fireball.jpg')
enemy = pygame.image.load('sanjit.jpg')
boom = pygame.image.load('boom.jpg')

def myAvatar(x,y):
    gameDisplay.blit(my_avatar, (x,y))

def myFireball(x,y):
    gameDisplay.blit(fireball, (x,y))
    
def myEnemy(x,y):
    gameDisplay.blit(enemy, (x,y))
    
def Boom(x,y):
    gameDisplay.blit(boom, (x,y))

def gameLoop():
    x = display_width * 0.45
    y = display_height * 0.8
    
    x_fireball = x + 20
    y_fireball = y + 15
    
    x_enemy = random.randrange(0, display_width)
    y_enemy = random.randrange(0, display_height*0.4)
    
    
    
    x_change = 0
    y_fireball_change = 0
    flag = False
    hit = False
    
    crashed = False
    while not crashed:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    
                if event.key == pygame.K_SPACE:
                    #myFireball(x_fireball, y_fireball)
                    #pygame.display.update()
                    y_fireball_change = 4
                    flag = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                    x_change = 0
                
                    
                    
                    
        
        x += x_change 
        #y_fireball -= y_fireball_change
        #time.sleep(0.5)
        gameDisplay.fill(green)
        myEnemy(x_enemy, y_enemy)
        myAvatar(x,y)
        if y_fireball < 0:
            x_fireball = x + 20
            y_fireball = y + 15
            flag = False
        
        if flag == True:
            y_fireball -= y_fireball_change
            myFireball(x_fireball, y_fireball)
            
        if x_fireball >= x_enemy and x_fireball <= x_enemy+56 and y_fireball >= y_enemy and y_fireball <= y_enemy+65:
            #time.sleep(0.5)
            Boom(x_enemy, y_enemy)
            #time.sleep(0.5)
            x_fireball = x + 20
            y_fireball = y + 15
            flag = False
            hit = True
            x_enemy = random.randrange(0, display_width)
            y_enemy = random.randrange(0, display_height*0.4)
            #time.sleep(0.5)
            
        
        
            
        pygame.display.update()
        #time.sleep(0.5)
        if hit == True:
            #Boom(x_enemy, y_enemy)
            time.sleep(0.5)
            hit = False
    
        clock.tick(60)
gameLoop()
    
pygame.quit()
#quit()        
            