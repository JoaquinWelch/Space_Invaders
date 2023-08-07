import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Player
player_width = 20
player_height = 20
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 20
player_speed = 1

# Bullet
bullet_width = 5
bullet_height = 20
bullet_x = 0
bullet_y = player_y
bullet_speed = 2
bullet_state = "ready"  # "ready" or "fire"

# Enemies 
num_enemies = 5
enemy_width = 17
enemy_height = 17
enemy_speed = .9

enemy_bullet_width = 4
enemy_bullet_height = 20
enemy_bullet_speed = 1
enemy_bullets = []


enemy_speeds = [enemy_speed, -enemy_speed, enemy_speed, -enemy_speed, enemy_speed]

enemies = []
for i in range(num_enemies):
    enemies.append([random.randint(0, screen_width - enemy_width), random.randint(0, 200), enemy_speeds[i]])

# Game loop
running = True
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

    # Update bullet
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"

    # Update enemies
    for enemy in enemies:
        enemy[0] += enemy[2]
        if enemy[0] <= 0 or enemy[0] >= screen_width - enemy_width:
            enemy[2] = -enemy[2]

    for bullet in enemy_bullets:
        bullet[1] += enemy_bullet_speed
        if bullet[1] >= screen_height:
            enemy_bullets.remove(bullet)

# Enemy shooting logic
    for enemy in enemies:
        if random.randint(0, 2500) < 1:  # Adjust the probability as needed
            enemy_bullets.append([enemy[0] + enemy_width // 2 - enemy_bullet_width // 2, enemy[1] + enemy_height])

    # Collision detection with enemies
    for enemy in enemies:
        if bullet_state == "fire" and bullet_x > enemy[0] and bullet_x < enemy[0] + enemy_width and bullet_y < enemy[1] + enemy_height:
            bullet_state = "ready"
            enemy[0] = random.randint(0, screen_width - enemy_width)
            enemy[1] = random.randint(0, 200)

    # Clear the screen
    screen.fill(black)

    font = pygame.font.Font(None, 50)

    title = font.render("SPACE INVADERS", True, white)
    text_rect = title.get_rect(center=(screen_width//2, 30))
    screen.blit(title, text_rect)

    # Draw player, enemies, and bullet
    pygame.draw.rect(screen, green, (player_x, player_y, player_width, player_height))
    for enemy in enemies:
        pygame.draw.rect(screen, white, (enemy[0], enemy[1], enemy_width, enemy_height))
    if bullet_state == "fire":
        pygame.draw.rect(screen, white, (bullet_x, bullet_y, bullet_width, bullet_height))
    for bullet in enemy_bullets:
        pygame.draw.rect(screen, white, (bullet[0], bullet[1], enemy_bullet_width, enemy_bullet_height))  # Fixed this line


    pygame.display.update()

# Quit Pygame
pygame.quit()