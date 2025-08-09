# main.py
# runs game loop, draws Ui elements, and handles events

import pygame
import random
from planetPy_UI import *
from planetPy_Spawns import *

# region ---Inits---
pygame.init()   # initalize pygame
quit_button_pressed = False # default button states
generate_button_pressed = False
# endregion ---inits---

#region ---Load Assets---
assets = load_assets()  # Load all game assets once at the start, must happen before img can be assigned

###optimize this section
quit_unpressed_img = assets["quit_unpressed"]
regenerate_unpressed_img = assets["regenerate_unpressed"]
legend_img = assets["metal_legend"]

# Quit Button
quit_button_x = SCREEN_WIDTH - quit_unpressed_img.get_width() - uiOffset
quit_button_y = uiOffset 
quit_button_rect = quit_unpressed_img.get_rect(topleft=(quit_button_x, quit_button_y))

# Regenerate Button
generate_button_x = SCREEN_WIDTH - regenerate_unpressed_img.get_width() - uiOffset
generate_button_y = quit_unpressed_img.get_height() + uiOffset * 2
generate_button_rect = regenerate_unpressed_img.get_rect(topleft=(generate_button_x, generate_button_y))

# Legend Window         ##make appendable
home_x = uiOffset
home_y = uiOffset
legend_button_height = legend_img.get_height() 
legend_list = [0, 1, 2]
legend_list [0] = legend_icon1_rect = legend_img.get_rect(topleft=(home_x, home_y))
legend_list [1] = legend_icon2_rect = legend_img.get_rect(topleft=(home_x, home_y + legend_button_height + uiOffset))
legend_list [2] = legend_icon3_rect = legend_img.get_rect(topleft=(home_x, home_y + 2 * (legend_button_height + uiOffset)))

ui_elements = {
    "quit_button_rect": quit_button_rect,
    "generate_button_rect": generate_button_rect,
    "legend_icon1_rect": legend_icon1_rect,
    "legend_icon2_rect": legend_icon2_rect,
    "legend_icon3_rect": legend_icon3_rect,
}
#endregion ui elements

#region ---Game Loop---
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
            print("How many planets?")
            num_Planets = int(input())
            planets = spawnPlanets(num_Planets, screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH, assets=assets)

            '''#debug'''
            planet_x = 400
            planet_y = 400
            stations = spawnStation(planet_x, planet_y, assets)
        else:
            generate_button_pressed = False
        # endregion ---UIButtons---
    # endregion ---Event Handling---
    
    screen.fill(BLACK) # Clear the screen each frame
    
    # region ---Draw Elements---
    draw_ui(screen, ui_elements, assets, quit_button_pressed, generate_button_pressed)
    
    for planet in planets:      #Draw Planets
        planet.draw(screen)

    for station in stations:    #Draw Stations
            station.draw(screen)

    print(planets)
    # endregion ---Draw Elements---
    
    pygame.display.flip()

    #endregion game loop
