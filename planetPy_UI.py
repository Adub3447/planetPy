# planetPy_UI.py

import pygame

# region ---UI Variables---
# WHITE and BLACK are kept for text and screen background
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# uiOffset is still used for spacing
uiOffset = 10
# endregion ---UI Variables---

# region ---Design UI Elements---
def load_assets():
    """Loads and returns all necessary images and fonts."""
    try:
        # Load button images
        quit_unpressed_img = pygame.image.load("Artwork\Quit_Unpressed.png").convert_alpha()
        quit_pressed_img = pygame.image.load("Artwork\Quit_Pressed.png").convert_alpha()
        regenerate_unpressed_img = pygame.image.load("Artwork\Regenerate_Unpressed.png").convert_alpha()
        regenerate_pressed_img = pygame.image.load("Artwork\Regenerate_Pressed.png").convert_alpha()
        
        # Load legend images
        metal_legend_img = pygame.image.load("Artwork\MetalLegendImage.png").convert_alpha()
        food_legend_img = pygame.image.load("Artwork\FoodLegendImage.png").convert_alpha()
        goods_legend_img = pygame.image.load("Artwork\GoodsLegendImage.png").convert_alpha()
        

        
        # Define fonts
        font_button = pygame.font.SysFont('Arial', 18, bold=False)
        font_legend = pygame.font.SysFont('Arial', 12, bold=False)

        return {
            "quit_unpressed": quit_unpressed_img,
            "quit_pressed": quit_pressed_img,
            "regenerate_unpressed": regenerate_unpressed_img,
            "regenerate_pressed": regenerate_pressed_img,
            "metal_legend": metal_legend_img,
            "food_legend": food_legend_img,
            "goods_legend": goods_legend_img,
            "font_button": font_button,
            "font_legend": font_legend
        }
    except pygame.error as e:
        print(f"Error loading images: {e}")
        return None

def draw_ui(screen, ui_elements, assets, quit_pressed, generate_pressed):
    """Draws all UI elements on the screen."""
    
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
    text = assets["font_legend"].render("Metal", True, WHITE)
    text_rect = text.get_rect(center=ui_elements["legend_icon1_rect"].center)
    screen.blit(text, text_rect)
    
    screen.blit(assets["goods_legend"], ui_elements["legend_icon2_rect"])
    text = assets["font_legend"].render("Goods", True, WHITE)
    text_rect = text.get_rect(center=ui_elements["legend_icon2_rect"].center)
    screen.blit(text, text_rect)

    screen.blit(assets["food_legend"], ui_elements["legend_icon3_rect"])
    text = assets["font_legend"].render("Food", True, WHITE)
    text_rect = text.get_rect(center=ui_elements["legend_icon3_rect"].center)
    screen.blit(text, text_rect)

# endregion ---Design UI Elements---
