import pygame
import random

#region ---Inits---
# initalize pygame
pygame.init()

# create screen dimensions
# using display.set_mode
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GAME TITLE")

# initialize color scheme for reference later
unpressedButtonRED = (200, 20, 20)  # color for red buttons unpressed
pressedButtonRED = (80, 20, 20)     # color for red buttons pressed
metalColor = (150, 80, 200)         # color for metal theme
foodColor = (125, 200, 75)          # color for food theme
goodsColor = (250, 150, 50)         # color for goods theme
WHITE = (255, 255, 255) # color for text and 

# init UI default colors
quitButtonColor = unpressedButtonRED

#endregion ---inits---

#region Design UI elements

#region Design Quit Button
# Define button dimensions
button_width = 80
button_height = 30
# Position the button in the top-right corner with some padding
button_x = SCREEN_WIDTH - button_width - 10 # 10 pixels from the right edge
button_y = 10 # 10 pixels from the top edge
quit_button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
#endregion design quit button

#region Design planets
planetColors = [metalColor, foodColor, goodsColor]
planetRadius = 25

#endregion design planets

#endregion design ui elements

# game loop to keep the window displayed and functional until the game is quit
gameRunning = True
while gameRunning:

    #region Event Handling
    for event in pygame.event.get():
        #region quit options
        if event.type == pygame.QUIT: # Allows quitting by clicking the window's 'X' 
            gameRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and quit_button_rect.collidepoint(event.pos): # If left mouse button is pressed and in bounds of the Quit Button
            quitButtonColor = pressedButtonRED
            pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and quit_button_rect.collidepoint(event.pos): # If left mouse button is pressed and in bounds of the Quit Button
            gameRunning = False
        else:
            quitButtonColor = unpressedButtonRED
        #endregion quit options
        
        #region next set of event handling
        #endregion next set
    #endregion event handling


    #region Draw the UI
    #Draw Quit Botton
    pygame.draw.rect(screen, quitButtonColor, quit_button_rect) 
    font = pygame.font.Font(None, 24) # Choose a font and size
    text = font.render("Quit", True, WHITE) # Render the text "Quit" in white
    text_rect = text.get_rect(center=quit_button_rect.center) # Center text on button
    screen.blit(text, text_rect) # Draw the text
    #endregion draw UI
	
	# Refresh screen to display elements each loop
    pygame.display.flip()


