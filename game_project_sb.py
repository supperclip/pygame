import pygame, sys
from pygame.locals import QUIT
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Keyboard')
clock = pygame.time.Clock()

background_surface = pygame.Surface((800, 500))
background_surface.fill("black")


#get sentry picture
sentry_picture = pygame.image.load("x/sentry_loc.png").convert_alpha() #credit to helldivers1 for the basic picture and https://giventofly.github.io/pixelit/#tryit for the pixerart generator

chainsaw_1 = pygame.image.load("x/chain_enemy1.png").convert_alpha()
chainsaw_1 = pygame.transform.rotate(chainsaw_1 , 270)
chainsaw_1 = pygame.transform.scale(chainsaw_1 , (60,60))

chainsaw_2 = pygame.image.load("x/chain_enemy2.png").convert_alpha()
chainsaw_2 = pygame.transform.rotate(chainsaw_2 , 270)
chainsaw_2 = pygame.transform.scale(chainsaw_2 , (60,60))

turret_1 = pygame.image.load("x/turret_frame_1.png").convert_alpha()
turret_1 = pygame.transform.scale(turret_1 , (100,100))

rocket = pygame.image.load("x/rocket_1.png").convert_alpha()
rocket = pygame.transform.scale(rocket, (30,30))
turret_1 = pygame.transform.rotate(turret_1 , 270)


chainsaw_animation_list = [chainsaw_1 , chainsaw_2]

current_frame = 0
frame_offset = 0
enemy_Xlist = []
enemy_Ylist = []

turret_location = [801, 501]

enemy_speed = 1 #pixels per frame?

while True:
  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                turret_location = [127.5,425]
            if event.key == pygame.K_2:
                turret_location = [327.5,425]
            if event.key == pygame.K_3:
                turret_location = [477.5,425]
            if event.key == pygame.K_4:
                turret_location = [677.5,425]
          

    # Mouse logic
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #background
    screen.blit(background_surface, (0, 0))

    #turret logic
    screen.blit(sentry_picture, (100,400))
    screen.blit(sentry_picture, (300,400))
    screen.blit(sentry_picture, (450,400))
    screen.blit(sentry_picture, (650,400))

    #screen.blit(turret_1 , (turret_location))

    #rotate turret to mouse
    TrotX = mouse_x - turret_location[0]
    TrotY = mouse_y - turret_location[1]
    Tdist = math.hypot(TrotX, TrotY)
    Tdist += 0.000001 #fixes the crash, hopefuly?
    TdirX = TrotX / Tdist
    TdirY = TrotY / Tdist
    Tangle_radians = math.atan2(TrotY, TrotX) 
    Tangle_degrees = math.degrees(Tangle_radians)
    rotated_turret = pygame.transform.rotate(turret_1, -Tangle_degrees)
    turret_rect = rotated_turret.get_rect(center=(turret_location[0], turret_location[1]))

    screen.blit(rotated_turret , (turret_rect.topleft))



    
    #enemy logic
    current_frame += 1
    if current_frame % 15 == 0:  
        if len(enemy_Xlist) <= 100:
            enemy_x = random.randint(0, 800)
            enemy_Xlist.append(enemy_x)
            enemy_Ylist.append(0)

    #vodoo
    for x in range(len(enemy_Xlist)):
        enemy_coords = [enemy_Xlist[x], enemy_Ylist[x]]
        
        # Calculate the rotation angle
        rotX = mouse_x - enemy_coords[0]
        rotY = mouse_y - enemy_coords[1]
        #this works, sadly
        dist = math.hypot(rotX, rotY)
        dist += 0.000001 #fixes the crash, hopefuly?
        dirX = rotX / dist
        dirY = rotY / dist
        enemy_Xlist[x] += dirX * enemy_speed
        enemy_Ylist[x] += dirY * enemy_speed
        angle_radians = math.atan2(rotY, rotX) 
        angle_degrees = math.degrees(angle_radians)

        if current_frame % 10 == 0:
            frame_offset = random.randint(0,1)

        #distance mouse to enemy with math vodoo shit
        
        #idk how this works but it works 
        rotated_enemy = pygame.transform.rotate(chainsaw_animation_list[frame_offset], -angle_degrees)
        
        #get new surface with more vodoo
        rotated_rect = rotated_enemy.get_rect(center=(enemy_coords[0], enemy_coords[1]))

        screen.blit(rotated_enemy, rotated_rect.topleft)


    pygame.display.update()
    clock.tick(60)

    #known issues: game can crash because distance can be 0 and it is used to devide another number (fixed?)