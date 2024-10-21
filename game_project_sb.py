import pygame
import sys
from pygame.locals import QUIT
import random
import math
from player_class import player
from player_class import Directions

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Keyboard')
clock = pygame.time.Clock()

background_surface = pygame.Surface((800, 500))
background_surface.fill("black")

# Load images
sentry_picture = pygame.image.load("x/sentry_loc.png").convert_alpha()
chainsaw_1 = pygame.image.load("x/chain_enemy1.png").convert_alpha()
chainsaw_1 = pygame.transform.rotate(chainsaw_1, 270)
chainsaw_1 = pygame.transform.scale(chainsaw_1, (60, 60))

chainsaw_2 = pygame.image.load("x/chain_enemy2.png").convert_alpha()
chainsaw_2 = pygame.transform.rotate(chainsaw_2, 270)
chainsaw_2 = pygame.transform.scale(chainsaw_2, (60, 60))

turret_1 = pygame.image.load("x/turret_frame_1.png").convert_alpha()
turret_1 = pygame.transform.scale(turret_1, (100, 100))
turret_1 = pygame.transform.rotate(turret_1, (0))

rocket = pygame.image.load("x/rocket_1.png").convert_alpha()
rocket = pygame.transform.scale(rocket, (30, 30))

player_surface = pygame.Surface((40, 40))
player_surface.fill("red")
player_rect = player_surface.get_rect()
player_rect.x = 400
player_rect.y = 250

chainsaw_animation_list = [chainsaw_1, chainsaw_2]
current_frame = 0
frame_offset = 0
enemy_Xlist = []
enemy_Ylist = []


Current_Direction = Directions.InValid
p1 = player(Current_Direction)
MoveSpeed = 1

enemy_speed = 0.6  # pixels per frame?

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and keys[pygame.K_w]:
        Current_Direction = Directions.UpAndLeft
    elif keys[pygame.K_d] and keys[pygame.K_w]:
        Current_Direction = Directions.UpAndRight
    elif keys[pygame.K_d] and keys[pygame.K_s]:
        Current_Direction = Directions.DownAndRight
    elif keys[pygame.K_a] and keys[pygame.K_s]:
        Current_Direction = Directions.DownAndLeft
    elif keys[pygame.K_a]:
        Current_Direction = Directions.Left
    elif keys[pygame.K_w]:
        Current_Direction = Directions.Up
    elif keys[pygame.K_d]:
        Current_Direction = Directions.Right
    elif keys[pygame.K_s]:
        Current_Direction = Directions.Down
    else:
        Current_Direction = Directions.InValid

    # Background
    screen.blit(background_surface, (0, 0))

    # Player logic
    playerList = p1.MovePlayer(Current_Direction)
    playerMoveX = (playerList[0] * MoveSpeed)
    playerMoveY = (playerList[1] * MoveSpeed)

    # Update player position
    player_rect.x += playerMoveX
    player_rect.y += playerMoveY

    # Draw player
    screen.blit(player_surface, player_rect)

    # Mouse logic
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Turret logic
    screen.blit(sentry_picture, (100, 400))
    screen.blit(sentry_picture, (300, 400))
    screen.blit(sentry_picture, (450, 400))
    screen.blit(sentry_picture, (650, 400))
    screen.blit(turret_1, (82.5, 385.5))
    screen.blit(turret_1, (282.5, 385.5))
    screen.blit(turret_1, ((82.5 + 350), 385.5))
    screen.blit(turret_1, ((82.5 + 550), 385.5))

    # Enemy logic
    current_frame += 1
    if current_frame % 15 == 0:
        if len(enemy_Xlist) <= 100:
            enemy_x = random.randint(0, 800)
            enemy_Xlist.append(enemy_x)
            enemy_Ylist.append(0)

    # Voodoo (enemy following mouse)
    for x in range(len(enemy_Xlist)):
        enemy_coords = [enemy_Xlist[x], enemy_Ylist[x]]
        
        # Calculate the rotation angle
        rotX = mouse_x - enemy_coords[0]
        rotY = mouse_y - enemy_coords[1]
        dist = math.hypot(rotX, rotY) or 0.000001  # Prevent division by zero
        dirX = rotX / dist
        dirY = rotY / dist
        enemy_Xlist[x] += dirX * enemy_speed
        enemy_Ylist[x] += dirY * enemy_speed
        angle_radians = math.atan2(rotY, rotX) 
        angle_degrees = math.degrees(angle_radians)

        if current_frame % 10 == 0:
            frame_offset = random.randint(0, 1)

        rotated_enemy = pygame.transform.rotate(chainsaw_animation_list[frame_offset], -angle_degrees)
        rotated_rect = rotated_enemy.get_rect(center=(enemy_coords[0], enemy_coords[1]))
        screen.blit(rotated_enemy, rotated_rect.topleft)

    pygame.display.update()
    clock.tick(60)
