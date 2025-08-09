# main.py

import pygame
import random
from planetPy_UI import *

# region ---Inits---
# initalize pygame
pygame.init()

# create screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GAME TITLE")

# Load all game assets once at the start
assets = load_assets()

# Initialize button state flags
quit_button_pressed = False
generate_button_pressed = False
# endregion ---inits---

# region ---Design Planets---
# The Planet class now takes an image instead of a color or radius
class Planet:
    def __init__(self, position, image):
        self.position = position
        self.image = image
        self.rect = self.image.get_rect(center=position)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
def spawnPlanets(num_Planets, screen_width, screen_height, assets):
    """Spawns a given number of planets with random positions and images."""
    spawned_Planets = []
    planet_images = [assets["metal_planet"], assets["food_planet"], assets["goods_planet"]]
    
    for _ in range(num_Planets):
        planet_image = random.choice(planet_images)
        # Use the image dimensions to calculate valid spawn coordinates
        rand_x = random.randint(planet_image.get_width(), screen_width - planet_image.get_width() - uiOffset)
        rand_y = random.randint(planet_image.get_height(), screen_height - planet_image.get_height() - uiOffset)
        position = (rand_x, rand_y)
        spawned_Planets.append(Planet(position, planet_image))

    return spawned_Planets

planets = []
# endregion ---Design Planets---

# --- Setup UI Elements ---
# Define the UI element rectangles here after loading the assets
# The new, smaller image sizes are automatically used here
quit_unpressed_img = assets["quit_unpressed"]
regenerate_unpressed_img = assets["regenerate_unpressed"]
metal_legend_img = assets["metal_legend"]

# Quit Button
button_x = SCREEN_WIDTH - quit_unpressed_img.get_width() - uiOffset
button_y = uiOffset 
quit_button_rect = quit_unpressed_img.get_rect(topleft=(button_x, button_y))

# Regenerate Button
button_y = quit_unpressed_img.get_height() + uiOffset * 2
generate_button_rect = regenerate_unpressed_img.get_rect(topleft=(button_x, button_y))

# Legend Window
legend_x = uiOffset
legend_y = uiOffset 
legend_icon1_rect = metal_legend_img.get_rect(topleft=(legend_x, legend_y))
legend_icon2_rect = metal_legend_img.get_rect(topleft=(legend_x, legend_y + metal_legend_img.get_height()))
legend_icon3_rect = metal_legend_img.get_rect(topleft=(legend_x, legend_y + 2 * metal_legend_img.get_height()))

ui_elements = {
    "quit_button_rect": quit_button_rect,
    "generate_button_rect": generate_button_rect,
    "legend_icon1_rect": legend_icon1_rect,
    "legend_icon2_rect": legend_icon2_rect,
    "legend_icon3_rect": legend_icon3_rect,
}

# game loop
gameRunning = True
while gameRunning:
    # region ---Event Handling---
    for event in pygame.event.get():
        ##Close Window
        if event.type == pygame.QUIT: 
            gameRunning = False
    
        # region ---UIButtons---
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ui_elements["quit_button_rect"].collidepoint(event.pos):
            quit_button_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and ui_elements["quit_button_rect"].collidepoint(event.pos):
            gameRunning = False
        else:
            quit_button_pressed = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ui_elements["generate_button_rect"].collidepoint(event.pos):
            generate_button_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and ui_elements["generate_button_rect"].collidepoint(event.pos):
            planets = spawnPlanets(num_Planets=5, screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH, assets=assets)
        else:
            generate_button_pressed = False
        # endregion ---UIButtons---
    # endregion ---Event Handling---
    
    screen.fill(BLACK) # Clear the screen each frame
    
    # region ---Draw Elements---
    draw_ui(screen, ui_elements, assets, quit_button_pressed, generate_button_pressed)
    
    for planet in planets: # Draw Planets
        planet.draw(screen)
    # endregion ---Draw Elements---
    
    pygame.display.flip()
