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

enemy_test = pygame.Surface((25, 25), pygame.SRCALPHA)
pygame.draw.rect(enemy_test, (0, 255, 0), (0, 0, 25, 25))

#get sentry picture
sentry_picture = pygame.image.load("x/sentry_loc.png").convert_alpha() #credit to helldivers1 for the basic picture and https://giventofly.github.io/pixelit/#tryit for the pixerart generator
sentry_locX = [600,400]
sentry_locY = [400,100]

current_frame = 0
enemy_Xlist = []
enemy_Ylist = []

enemy_speed = 1 #pixels per frame?

while True:
  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
          

    # Mouse logic
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #background
    screen.blit(background_surface, (0, 0))

    #blit static images
    screen.blit(sentry_picture, (400,400))
    screen.blit(sentry_picture, (600,400))
    screen.blit(sentry_picture, (400,100))
    screen.blit(sentry_picture, (600,100))
    
    #enemy logic
    current_frame += 1
    if current_frame % 15 == 0:  
        enemy_x = random.randint(0, 800)
        enemy_Xlist.append(enemy_x)
        enemy_Ylist.append(0)  

    #vodoo
    for x in range(len(enemy_Xlist)):
        enemy_coords = [enemy_Xlist[x], enemy_Ylist[x]]
        
        # Calculate the rotation angle
        rotX = mouse_x - enemy_coords[0]
        rotY = mouse_y - enemy_coords[1]

        dist = math.hypot(rotX, rotY)

        dirX = rotX / dist
        dirY = rotY / dist

        enemy_Xlist[x] += dirX * enemy_speed
        enemy_Ylist[x] += dirY * enemy_speed

        angle_radians = math.atan2(rotY, rotX) 
        angle_degrees = math.degrees(angle_radians)

        #distance mouse to enemy with math vodoo shit
        
        #idk how this works but it works 
        rotated_enemy = pygame.transform.rotate(enemy_test, -angle_degrees)
        
        #get new surface with more vodoo
        rotated_rect = rotated_enemy.get_rect(center=(enemy_coords[0], enemy_coords[1]))

        screen.blit(rotated_enemy, rotated_rect.topleft)


    pygame.display.update()
    clock.tick(60)
