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
RED = (200, 0, 0) # color for the quit button
WHITE = (255, 255, 255) # color for text and stars

#endregion ---inits---

#region Design the Quit Button

# Define button dimensions
button_width = 80
button_height = 30
# Position the button in the top-right corner with some padding
button_x = SCREEN_WIDTH - button_width - 10 # 10 pixels from the right edge
button_y = 10 # 10 pixels from the top edge
quit_button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
#endregion design quit button


# game loop to keep the window displayed and functional until the game is quit
gameRunning = True
while gameRunning:

	# Event Handling
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # If left mouse button is pressed
			gameRunning = False
            
	# Draw the menu
	# Draw the quit button
	pygame.draw.rect(screen, RED, quit_button_rect) 
	font = pygame.font.Font(None, 24) # Choose a font and size
	text = font.render("Quit", True, WHITE) # Render the text "Quit" in white
	text_rect = text.get_rect(center=quit_button_rect.center) # Center text on button
	screen.blit(text, text_rect) # Draw the text
    
	
	# Refresh screen to display elements each loop
	pygame.display.flip()
	

