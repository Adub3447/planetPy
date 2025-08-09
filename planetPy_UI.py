# ui.py

import pygame

# region ---UI Variables---
##Button States
unpressedButtonRED = (200, 20, 20)
pressedButtonRED = (80, 20, 20)
unpressedButtonBLUE = (0, 150, 200)
pressedButtonBLUE = (0, 125, 150)

##Misc
WHITE = (255, 255, 255)
BLACK = (0,0,0)

##Themes
metalColor = (150, 80, 200)
foodColor = (100, 150, 45)
goodsColor = (200, 100, 20)

button_text_color = WHITE
legend_text_color = BLACK

uiOffset = 10
# endregion ---UI Variables---

# region ---Design UI Elements---
def setup_ui_elements(screen_width, screen_height):
    """Sets up and returns all UI rectangles and fonts."""
    
    font_button = pygame.font.SysFont('Arial', 18, bold=False)
    font_legend = pygame.font.SysFont('Arial', 12, bold=False)

    # Quit Button
    rectButton_Width = 80
    rectButton_Height = 30
    button_x = screen_width - rectButton_Width - uiOffset
    button_y = uiOffset 
    quit_button_rect = pygame.Rect(button_x, button_y, rectButton_Width, rectButton_Height)

    # Generate Button
    button_y = rectButton_Height * 2 + uiOffset
    generate_button_rect = pygame.Rect(button_x, button_y, rectButton_Width, rectButton_Height)

    # Legend Window
    legButton_Width = 40
    legButton_Height = 15
    legend_x = uiOffset
    legend_y = uiOffset 
    legend_icon1_rect = pygame.Rect(legend_x, legend_y, legButton_Width, legButton_Height)
    legend_icon2_rect = pygame.Rect(legend_x, legend_y + legButton_Height + uiOffset, legButton_Width, legButton_Height)
    legend_icon3_rect = pygame.Rect(legend_x, legend_y + 2 * legButton_Height + 2 * uiOffset, legButton_Width, legButton_Height)
    
    return {
        "quit_button_rect": quit_button_rect,
        "generate_button_rect": generate_button_rect,
        "legend_icon1_rect": legend_icon1_rect,
        "legend_icon2_rect": legend_icon2_rect,
        "legend_icon3_rect": legend_icon3_rect,
        "font_button": font_button,
        "font_legend": font_legend
    }

def draw_ui(screen, ui_elements, quit_button_color, generate_button_color):
    """Draws all UI elements on the screen."""
    
    # Draw Quit Button
    pygame.draw.rect(screen, quit_button_color, ui_elements["quit_button_rect"]) 
    text = ui_elements["font_button"].render("Quit", True, button_text_color)
    text_rect = text.get_rect(center=ui_elements["quit_button_rect"].center)
    screen.blit(text, text_rect)

    # Draw Generate Button
    pygame.draw.rect(screen, generate_button_color, ui_elements["generate_button_rect"]) 
    text = ui_elements["font_button"].render("Generate", True, button_text_color)
    text_rect = text.get_rect(center=ui_elements["generate_button_rect"].center)
    screen.blit(text, text_rect)

    # Draw Legend
    pygame.draw.rect(screen, metalColor, ui_elements["legend_icon1_rect"])
    text = ui_elements["font_legend"].render("Metal", True, legend_text_color)
    text_rect = text.get_rect(center=ui_elements["legend_icon1_rect"].center)
    screen.blit(text, text_rect)
    
    pygame.draw.rect(screen, goodsColor, ui_elements["legend_icon2_rect"])
    text = ui_elements["font_legend"].render("Goods", True, legend_text_color)
    text_rect = text.get_rect(center=ui_elements["legend_icon2_rect"].center)
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, foodColor, ui_elements["legend_icon3_rect"])
    text = ui_elements["font_legend"].render("Food", True, legend_text_color)
    text_rect = text.get_rect(center=ui_elements["legend_icon3_rect"].center)
    screen.blit(text, text_rect)
# endregion ---Design UI Elements---