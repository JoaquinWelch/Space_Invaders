import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Player =
player_width, player_height = 30, 30
player_speed = 1
player_x, player_y = screen_width // 2 - player_width // 2, screen_height - player_height - 10

# enemies
enemy_width, enemy_height = 20, 20
enemy_speed = .75
num_enemies = 10
enemies = []
for i in range(num_enemies):
    enemy_x, enemy_y = 50 + i * (enemy_width + 50), 50
    enemies.append((enemy_x, enemy_y))

enemy_x_change = 2
enemy_y_change = 40

bullet_width, bullet_height = 5, 10
bullet_speed = 8
bullets = []



game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_width < screen_width:
        player_x += player_speed

    # bullet shooting
    if keys[pygame.K_SPACE]:
        bullet_x, bullet_y = player_x + player_width // 2 - bullet_width // 2, player_y
        bullets.append((bullet_x, bullet_y))

    # Enemy movements
    for i in range(num_enemies):
        enemy_x, enemy_y = enemies[i]
        enemy_x += enemy_x_change

        if enemy_x + enemy_width >= screen_width or enemy_x <= 0:  
            enemy_x_change *= -1
            enemy_y += enemy_y_change

        enemies[i] = (enemy_x, enemy_y)



   
    # Move bullets and remove off-screen bullets
    bullets = [(bullet_x, bullet_y - bullet_speed) for bullet_x, bullet_y in bullets if bullet_y > 0]

    # Collision detection
    for bullet in bullets.copy():
        for i, (enemy_x, enemy_y) in enumerate(enemies):
            if enemy_x <= bullet[0] <= enemy_x + enemy_width and enemy_y <= bullet[1] <= enemy_y + enemy_height:
                bullets.remove(bullet)
                del enemies[i]
                num_enemies -= 1

    # Clear screen
    screen.fill(BLACK)



  # Draw everything on the screen
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    for enemy_x, enemy_y in enemies:
        pygame.draw.rect(screen, GREEN, (enemy_x, enemy_y, enemy_width, enemy_height))
    for bullet_x, bullet_y in bullets:
        pygame.draw.rect(screen, WHITE, (bullet_x, bullet_y, bullet_width, bullet_height))

    # Update the display
    pygame.display.flip()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()

    score = 0

    for bullet in bullet.copy():
        for i, (enemy_x, enemy_y) in enumerate(enemies):
            if enemy_x <= bullet[0] <= enemy_x + enemy_width and enemy_y <= bullet[1] <= enemy_y + enemy_height:

                score += 10


    game_over = (player_x < enemy_x + enemy_width and
                player_x + player_width > enemy_x and
                player_y < enemy_y + enemy_height and
                player_y + player_height > enemy_y)
    
    if game_over:
        game_over_f = pygame.font.Font(None, 50)
        game_over_text = game_over_f.render("Game Over Loser", True, WHITE)
        screen.blit(game_over_text, (screen_width))