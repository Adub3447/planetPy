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
##Button States
unpressedButtonRED = (200, 20, 20)
pressedButtonRED = (80, 20, 20)
unpressedButtonBLUE = (0, 150, 200)
pressedButtonBLUE = (0, 125, 150)

##Themes
metalColor = (150, 80, 200)         # color for metal theme
foodColor = (125, 200, 75)          # color for food theme
goodsColor = (250, 150, 50)         # color for goods theme

##Misc
WHITE = (255, 255, 255) # color for text and 

# init UI default values
uiOffset = 10
quitButtonColor = unpressedButtonRED
generateButtonColor = unpressedButtonBLUE

#endregion ---inits---

#region Design UI elements

#region Design Buttons

##Quit Button 
# Dimensions
rectButton_Width = 80
rectButton_Height = 30
# Top Right Corner
button_x = SCREEN_WIDTH - rectButton_Width - uiOffset
button_y = uiOffset 
quit_button_rect = pygame.Rect(button_x, button_y, rectButton_Width, rectButton_Height)

##Generate Button
# Dimensions
rectButton_Width = 80
rectButton_Height = 30
# Under Quit button
button_x = SCREEN_WIDTH - rectButton_Width - uiOffset # 10 pixels from the right edge
button_y = rectButton_Height*2 + uiOffset # 10 pixels from the top edge
generate_button_rect = pygame.Rect(button_x, button_y, rectButton_Width, rectButton_Height)

#endregion design quit button

#region Design planets
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
        #random coordinates
        rand_x = random.randint(planet_Radius, screen_width-planet_Radius -uiOffset)
        rand_y = random.randint(planet_Radius, screen_height - planet_Radius - uiOffset)
        position = (rand_x, rand_y)

        #random color
        color = random.choice(planet_Colors)

        #Add to spawned planet list
        spawned_Planets.append(Planet(position, color, planet_Radius))

    return spawned_Planets
planets = []
#endregion design planets

#endregion design ui elements

# game loop to keep the window displayed and functional until the game is quit
gameRunning = True
while gameRunning:

    #region Event Handling
    for event in pygame.event.get():
        ##Close Window
        if event.type == pygame.QUIT: 
            gameRunning = False
    
        #region UIButtons
        ##QuitButton function
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and quit_button_rect.collidepoint(event.pos): # If left mouse button is pressed and in bounds of the Quit Button
            quitButtonColor = pressedButtonRED
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and quit_button_rect.collidepoint(event.pos): # If left mouse button is pressed and in bounds of the Quit Button
            gameRunning = False
        else:
            quitButtonColor = unpressedButtonRED

        ##GenerateButton function
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and generate_button_rect.collidepoint(event.pos): # If left mouse button is pressed and in bounds of the Quit Button
            generateButtonColor = pressedButtonBLUE
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and generate_button_rect.collidepoint(event.pos): # If left mouse button is pressed and in bounds of the Quit Button
            planets = spawnPlanets(num_Planets=5, screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH, planet_Radius=planetRadius, planet_Colors=planetColors)
        else:
            generateButtonColor = unpressedButtonBLUE

        #endregion uibuttons


        #region next set of event handling
        #endregion next set
    #endregion event handling


    #region Draw the UI
    ##Draw Quit Botton
    pygame.draw.rect(screen, quitButtonColor, quit_button_rect) 
    font = pygame.font.Font(None, 24) # Choose a font and size
    text = font.render("Quit", True, WHITE) # Render the text "Quit" in white
    text_rect = text.get_rect(center=quit_button_rect.center) # Center text on button
    screen.blit(text, text_rect) # Draw the text

    ##Draw Generate Button
    pygame.draw.rect(screen, generateButtonColor, generate_button_rect) 
    font = pygame.font.Font(None, 24) # Choose a font and size
    text = font.render("Generate", True, WHITE) # Render the text "Quit" in white
    text_rect = text.get_rect(center=generate_button_rect.center) # Center text on button
    screen.blit(text, text_rect) # Draw the text

    for planet in planets:
        planet.draw(screen)

    #endregion draw UI

	
	# Refresh screen to display elements each loop
    pygame.display.flip()


