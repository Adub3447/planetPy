# planetPy_UI.py
# creates all visual elements

import pygame
import os

#region ---Primary Settings---

# create screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GAME TITLE")

#endregion primary settings

# region ---UI Variables---
## Generic Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)

## Standardized Constants
uiOffset = .02
orbitOffset = .02
ui_scale_factor = .2
planet_scale_factor = .15
station_scale_factor = .05

#% versions
#uiOffset = SCREEN_HEIGHT*.3
#orbitOffset = SCREEN_HEIGHT*.1
#ui_scale_factor = SCREEN_HEIGHT*.3
#planet_scale_factor = SCREEN_HEIGHT*.3
#station_scale_factor = SCREEN_HEIGHT*.3
# endregion ---UI Variables---

# region ---Design UI Elements---
def load_assets():

    script_dir = os.path.dirname(__file__)     # Get the absolute path of the directory where this script is located
    try:    # load and scale assets
        # Load button images
        quit_unpressed_img = pygame.image.load(os.path.join(script_dir, "Artwork", "Quit_Unpressed.png")).convert_alpha()
        quit_pressed_img = pygame.image.load(os.path.join(script_dir, "Artwork", "Quit_Pressed.png")).convert_alpha()
        regenerate_unpressed_img = pygame.image.load(os.path.join(script_dir, "Artwork", "Regenerate_Unpressed.png")).convert_alpha()
        regenerate_pressed_img = pygame.image.load(os.path.join(script_dir, "Artwork", "Regenerate_Pressed.png")).convert_alpha()
        
        # Load legend images
        metal_legend_img = pygame.image.load(os.path.join(script_dir, "Artwork", "MetalLegendImage.png")).convert_alpha()
        food_legend_img = pygame.image.load(os.path.join(script_dir, "Artwork", "FoodLegendImage.png")).convert_alpha()
        goods_legend_img = pygame.image.load(os.path.join(script_dir, "Artwork", "GoodsLegendImage.png")).convert_alpha()
        
        # Load planet images
        metal_planet_img = pygame.image.load(os.path.join(script_dir, "Artwork", "MetalPlanetImage.png")).convert_alpha()
        food_planet_img = pygame.image.load(os.path.join(script_dir, "Artwork", "FoodPlanetImage.png")).convert_alpha()
        goods_planet_img = pygame.image.load(os.path.join(script_dir, "Artwork", "GoodsPlanetImage.png")).convert_alpha()

        # Load station images
        station_built_img = pygame.image.load(os.path.join(script_dir, "Artwork", "StationBuilt.png")).convert_alpha()
        station_unbuilt_img = pygame.image.load(os.path.join(script_dir, "Artwork", "StationUnbuilt.png")).convert_alpha()

        # Load ship images
        metal_ship_img = pygame.image.load(os.path.join(script_dir, "Artwork", "MetalShipImage.png")).convert_alpha()
        food_ship_img = pygame.image.load(os.path.join(script_dir, "Artwork", "FoodShipImage.png")).convert_alpha()
        goods_ship_img = pygame.image.load(os.path.join(script_dir, "Artwork", "GoodsShipImage.png")).convert_alpha()
        cop_ship_img = pygame.image.load(os.path.join(script_dir, "Artwork", "CopShipImage.png")).convert_alpha()
        pirate_ship_img = pygame.image.load(os.path.join(script_dir, "Artwork", "PirateShipImage.png")).convert_alpha()

        ## Link to hardware settings to fit any screen
        # Scale all UI images by the UI scale factor
        quit_unpressed_img = pygame.transform.scale(quit_unpressed_img, (int(quit_unpressed_img.get_width() * ui_scale_factor), int(quit_unpressed_img.get_height() * ui_scale_factor)))
        quit_pressed_img = pygame.transform.scale(quit_pressed_img, (int(quit_pressed_img.get_width() * ui_scale_factor), int(quit_pressed_img.get_height() * ui_scale_factor)))
        regenerate_unpressed_img = pygame.transform.scale(regenerate_unpressed_img, (int(regenerate_unpressed_img.get_width() * ui_scale_factor), int(regenerate_unpressed_img.get_height() * ui_scale_factor)))
        regenerate_pressed_img = pygame.transform.scale(regenerate_pressed_img, (int(regenerate_pressed_img.get_width() * ui_scale_factor), int(regenerate_pressed_img.get_height() * ui_scale_factor)))
        metal_legend_img = pygame.transform.scale(metal_legend_img, (int(metal_legend_img.get_width() * ui_scale_factor), int(metal_legend_img.get_height() * ui_scale_factor)))
        food_legend_img = pygame.transform.scale(food_legend_img, (int(food_legend_img.get_width() * ui_scale_factor), int(food_legend_img.get_height() * ui_scale_factor)))
        goods_legend_img = pygame.transform.scale(goods_legend_img, (int(goods_legend_img.get_width() * ui_scale_factor), int(goods_legend_img.get_height() * ui_scale_factor)))
        
        # Scale all planet images by the planet scale factor
        food_planet_img = pygame.transform.scale(food_planet_img, (int(food_planet_img.get_width() * planet_scale_factor), int(food_planet_img.get_height() * planet_scale_factor)))
        metal_planet_img = pygame.transform.scale(metal_planet_img, (int(metal_planet_img.get_width() * planet_scale_factor), int(metal_planet_img.get_height() * planet_scale_factor)))
        goods_planet_img = pygame.transform.scale(goods_planet_img, (int(goods_planet_img.get_width() * planet_scale_factor), int(goods_planet_img.get_height() * planet_scale_factor)))
        
        # Scale all station images by the station scale factor
        station_built_img = pygame.transform.scale(station_built_img, (int(station_built_img.get_width() * station_scale_factor), int(station_built_img.get_height() * station_scale_factor)))
        station_unbuilt_img = pygame.transform.scale(station_unbuilt_img, (int(station_unbuilt_img.get_width() * station_scale_factor), int(station_unbuilt_img.get_height() * station_scale_factor)))
        
        return { #delivers images to wherever called
            "quit_unpressed": quit_unpressed_img,
            "quit_pressed": quit_pressed_img,
            "regenerate_unpressed": regenerate_unpressed_img,
            "regenerate_pressed": regenerate_pressed_img,
            "metal_legend": metal_legend_img,
            "food_legend": food_legend_img,
            "goods_legend": goods_legend_img,
            "metal_planet": metal_planet_img,
            "food_planet": food_planet_img,
            "goods_planet": goods_planet_img,
            "station_built": station_built_img,
            "station_unbuilt": station_unbuilt_img,
            

        }
    except pygame.error as e:
        print(f"Error loading images: {e}")
        return None
# endregion ---Design UI Elements---

#region ----Draw UI----
def draw_ui(screen, ui_elements, assets, quit_pressed, generate_pressed):
    
    """.blit()
    The return rectangle is the area of the affected pixels, excluding any pixels outside the destination Surface, or outside the clipping area.
    """
    # Draw Quit Button
    if quit_pressed: 
        screen.blit(assets["quit_pressed"], ui_elements["quit_button_rect"])
    else:
        screen.blit(assets["quit_unpressed"], ui_elements["quit_button_rect"])

    # Draw Generate Button
    if generate_pressed:
        screen.blit(assets["regenerate_pressed"], ui_elements["generate_button_rect"])
    else:
        screen.blit(assets["regenerate_unpressed"], ui_elements["generate_button_rect"])

    # Draw Legend Icons
    screen.blit(assets["metal_legend"], ui_elements["legend_icon1_rect"])
    screen.blit(assets["goods_legend"], ui_elements["legend_icon2_rect"])
    screen.blit(assets["food_legend"], ui_elements["legend_icon3_rect"])

# endregion draw UI
