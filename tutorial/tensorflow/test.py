import pygame

# Initialize Pygame
pygame.init()

# Set the window size
size = width, height = 640, 480

# Create the Pygame window
screen = pygame.display.set_mode(size)

# Set the background color
background_color = (255, 255, 255)

# Fill the screen with the background color
screen.fill(background_color)

# Draw a red circle in the center of the screen
circle_color = (255, 0, 0)
circle_center = (width/2, height/2)
circle_radius = 50
pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

# Update the display
pygame.display.flip()

# Wait for the user to close the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
