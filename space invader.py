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


