import pygame
import random
import winsound

win = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Kick Ass")
pygame.mixer.init()

#image of characters
player = pygame.image.load('player.png')
player=pygame.transform.scale(player,(150,200))
enemy = pygame.image.load('sanjit.png')
enemy=pygame.transform.scale(enemy,(150,200))
weapon_id = 'weapon' + str(random.randint(1,4)) + '.png'
weapon = pygame.image.load(weapon_id)
weapon = pygame.transform.scale(weapon, (90, 90))
boom = pygame.image.load('boom.png')
boom=pygame.transform.scale(boom,(100,150))
bg=pygame.image.load('bg.jpg')
bg=pygame.transform.scale(bg,(1080,720))
#game values
enemyVelocity=25
enemyX=480
enemyY=30
playerVelocity=45
playerX=480
playerY=520
fireballVelocity=30
fireballTrack={'0':[-1,-1],'1':[-1,-1],'2':[-1,-1],'3':[-1,-1],'4':[-1,-1]}
fireballLimit=-1
collision=False
fireballStartIndex=0
enterFireball=0
gameActive = True
while gameActive:

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameActive=False

    #center positioins
    #win.blit(player,(480,520))
    #win.blit(enemy,(480,30))
    #win.blit(fireball,(510,300))

    #stuff on screen going on here
    win.blit(bg, (0, 0))
    win.blit(enemy, (enemyX, enemyY))
    win.blit(player,(playerX,playerY))

    for i in fireballTrack.keys():
        tempX, tempY = tuple(fireballTrack[i])
        if tempY >= -10:
            win.blit(weapon, (tempX, tempY))
            tempY -= fireballVelocity
            fireballTrack[i] = [tempX, tempY]
        if tempY < -10:
            print('terminated')
            fireballLimit -=1
        if abs(tempX - enemyX)<80 and abs(tempY - enemyY)<80:
            win.blit(boom, (tempX,tempY))
            fireballLimit -=1
            play_id = 's' + str(random.randint(1, 8)) + '.wav'
            winsound.PlaySound(play_id,winsound.SND_ASYNC)



    pygame.display.update()

    if(enemyX >= 1075) or (enemyX <= 10):
        enemyX=random.randint(0,1074)
        enemyY=random.randint(0,350)
        enemy_mov = random.randint(1, 2)
        if enemy_mov == 1:
            enemyVelocity *= -1
    else:
        enemyX+=enemyVelocity


    keys=pygame.key.get_pressed()

    #player movement
    if keys[pygame.K_LEFT]:
        playerX-=playerVelocity
    if keys[pygame.K_RIGHT]:
        playerX+=playerVelocity

    if playerX>=880:
        playerX=200
    if playerX<200:
        playerX=880


    if keys[pygame.K_SPACE]:
        if fireballLimit<4:
            fireballLimit+=1
            fireballTrack[str(enterFireball)]=[playerX,playerY+20]
            print(fireballTrack)
            enterFireball+=1
            enterFireball%=5
            print(fireballLimit, enterFireball)
            play_id='g'+str(random.randint(1,8))+'.wav'
            winsound.PlaySound(play_id, winsound.SND_ASYNC)


pygame.quit()
