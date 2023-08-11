import pygame
import random
import sys
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")



player_width = 20
player_height = 20
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 20
player_speed = 1


bullet_width = 5
bullet_height = 20
bullet_x = 0
bullet_y = player_y
bullet_speed = 2
bullet_state = "ready"  



num_enemies = 5
enemy_width = 17
enemy_height = 17
enemy_speed = .9

enemy_bullet_width = 4
enemy_bullet_height = 20
enemy_bullet_speed = 1
enemy_bullets = []

restart_button_img = pygame.image.load('restart.png')


enemy_speeds = [enemy_speed, -enemy_speed, enemy_speed, -enemy_speed, enemy_speed]


enemies = []
for i in range(num_enemies):
    enemies.append([random.randint(0, screen_width - enemy_width), random.randint(0, 200), enemy_speeds[i]])


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

restart_button_img = pygame.image.load('restart.png')
restart_button = Button((screen_width - restart_button_img.get_width()) // 2, screen_height // 2, restart_button_img)

score = 0

running = True
game_over = False






while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullet_state = "fire"



    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player_x = max(0, min(player_x, screen_width - player_width))



    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"



    for enemy in enemies:
        enemy[0] += enemy[2]
        if enemy[0] <= 0 or enemy[0] >= screen_width - enemy_width:
            enemy[2] = -enemy[2]



    for bullet in enemy_bullets:
        bullet[1] += enemy_bullet_speed
        if bullet[1] >= screen_height:
            enemy_bullets.remove(bullet)




    for enemy in enemies:
        if random.randint(0, 50) < 1: 
            enemy_bullets.append([enemy[0] + enemy_width // 2 - enemy_bullet_width // 2, enemy[1] + enemy_height])


    for enemy in enemies:
        if bullet_state == 'fire' and bullet_x > enemy[0] and bullet_x < enemy[0] + enemy_width and bullet_y > enemy[1] and bullet_y < enemy[1]+bullet_height:
            bullet_state = 'ready'
            enemy[0] = random.randint(0, screen_width - enemy_width)
            enemy[1] = random.randint(0, 200)
            score += 10

    for bullet in enemy_bullets:
        if (player_x < bullet[0] + enemy_bullet_width and player_x + player_width > bullet[0] and
                player_y < bullet[1] + enemy_bullet_height and player_y + player_height > bullet[1]):
            running = False      
            game_over = True



    if not game_over:


        screen.fill(black)

        font = pygame.font.Font(None, 50)

        title = font.render("SPACE INVADERS", True, green)
        text_rect = title.get_rect(center=(screen_width//2, 30))
        screen.blit(title, text_rect)

        score_font = pygame.font.Font(None, 33)
        score_count = score_font.render(f'Score: {score}', True, white)
        screen.blit(score_count, (1, 1))

        pygame.draw.rect(screen, green, (player_x, player_y, player_width, player_height))
        for enemy in enemies:
            pygame.draw.rect(screen, white, (enemy[0], enemy[1], enemy_width, enemy_height))
        if bullet_state == "fire":
            pygame.draw.rect(screen, white, (bullet_x, bullet_y, bullet_width, bullet_height))
        for bullet in enemy_bullets:
            pygame.draw.rect(screen, white, (bullet[0], bullet[1], enemy_bullet_width, enemy_bullet_height)) 
    else:
        while game_over:  
            screen.fill(black)
            game_over_font = pygame.font.Font(None, 70)
            game_over_text = game_over_font.render("Game Over", True, white)
            game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(game_over_text, game_over_rect)

            restart_button.draw(screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.rect.collidepoing(event.pos):
                        player_x = (screen_width-player_width)//2
                        player_y = screen_height - player_height - 20
                        bullet_state = "ready"
                        enemies = []
                        for i in range(num_enemies):
                            enemies.append([random.randint(0, screen_width - enemy_width), random.randint(0, 200), enemy_speeds[i]])
                        score = 0
                        game_over = False                       



    pygame.display.update()
    if game_over:
        player_x = (screen_width - player_width) // 2
        player_y = screen_height - player_height - 20
        bullet_state = "ready"
        enemies = []
        for i in range(num_enemies):
            enemies.append([random.randint(0, screen_width - enemy_width), random.randint(0, 200), enemy_speeds[i]])
        score = 0 
        game_over = False
        pygame.time.delay(5000)

pygame.quit()
