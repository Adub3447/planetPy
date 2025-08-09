# main.py

import pygame
import random
from planetPy_UI import * # Import everything from planetPy_UI.py

# region ---Inits---
# initalize pygame
pygame.init()

# create screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GAME TITLE")

# init UI default values
quitButtonColor = unpressedButtonRED
generateButtonColor = unpressedButtonBLUE
# endregion ---inits---

# region ---Design Planets---
planetRadius = 25
planetColors = [metalColor, foodColor, goodsColor]
class Planet:
    def __init__(self, position, color, radius = planetRadius):
        self.position = position
        self.color = color
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)
        
def spawnPlanets(num_Planets, screen_width, screen_height, planet_Radius, planet_Colors):
    spawned_Planets = []
    for _ in range(num_Planets):
        rand_x = random.randint(planet_Radius, screen_width - planet_Radius - uiOffset)
        rand_y = random.randint(planet_Radius, screen_height - planet_Radius - uiOffset)
        position = (rand_x, rand_y)
        color = random.choice(planet_Colors)
        spawned_Planets.append(Planet(position, color, planet_Radius))

    return spawned_Planets

planets = []
# endregion ---Design Planets---

# --- Setup UI Elements ---
ui_elements = setup_ui_elements(SCREEN_WIDTH, SCREEN_HEIGHT)

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
            quitButtonColor = pressedButtonRED
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and ui_elements["quit_button_rect"].collidepoint(event.pos):
            gameRunning = False
        else:
            quitButtonColor = unpressedButtonRED

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ui_elements["generate_button_rect"].collidepoint(event.pos):
            generateButtonColor = pressedButtonBLUE
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and ui_elements["generate_button_rect"].collidepoint(event.pos):
            planets = spawnPlanets(num_Planets=5, screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH, planet_Radius=planetRadius, planet_Colors=planetColors)
        else:
            generateButtonColor = unpressedButtonBLUE
        # endregion ---UIButtons---
    # endregion ---Event Handling---
    
    screen.fill(BLACK) # Clear the screen each frame
    
    # region ---Draw Elements---
    draw_ui(screen, ui_elements, quitButtonColor, generateButtonColor) # Draw UI
    
    for planet in planets: # Draw Planets
        planet.draw(screen)
    # endregion ---Draw Elements---
    
    pygame.display.flip()