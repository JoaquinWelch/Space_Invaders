import pygame
import sys

pygame.init()
# game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

#while True:
#    for event in pygame.event.get():
 #       if event.type == pygame.QUIT:
  #          pygame.quit()
   #         sys.exit()

    #pygame.display.flip()
    
# player attributes
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

player_width, player_height = (50, 50)
player_speed = 5
player = pygame.Rect(screen_width // 2 - player_width // 2, screen_height - player_height - 10, player_width, player_height)

# enemy attributes
enemy_width, enemy_height = (30, 30)
enemy_speed = 2
num_enemies = 15
enemies = []
for i in range(num_enemies):
    enemy = pygame.Rect(50 + i * (enemy_width + 50), 50, enemy_width, enemy_height)
    enemies.append(enemy)


bullet_width, bullet_height = (5, 10)
bullet_speed = 10
bullets = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < screen_width:
        player.x += player_speed

    screen.fill(black)
    pygame.display.flip()