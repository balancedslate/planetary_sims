import pygame
import math

# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Planetary parameters
MASS_STAR = 1000  # Mass of the central star (in units of solar masses)
MASS_PLANET1 = 0.001  # Mass of the first planet (in units of solar masses)
MASS_PLANET2 = 0.002  # Mass of the second planet (in units of solar masses)
POSITION_STAR = (WIDTH / 2, HEIGHT / 2)  # Initial position of the central star
POSITION_PLANET1 = (WIDTH / 2 + 200, HEIGHT / 2)  # Initial position of the first planet
POSITION_PLANET2 = (WIDTH / 2 - 200, HEIGHT / 2)  # Initial position of the second planet
VELOCITY_PLANET1 = (0, -10)  # Initial velocity of the first planet
VELOCITY_PLANET2 = (0, 10)  # Initial velocity of the second planet
GRAVITATIONAL_CONSTANT = 0.1  # Gravitational constant
TIMESTEP = 0.01  # Timestep for the simulation (in units of years)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the planets and star
star = pygame.draw.circle(screen, WHITE, POSITION_STAR, 10)
planet1 = pygame.draw.circle(screen, WHITE, POSITION_PLANET1, 5)
planet2 = pygame.draw.circle(screen, WHITE, POSITION_PLANET2, 5)

# Main loop
running = True
while running:
    # Calculate the gravitational force on each planet
    r1 = math.sqrt((POSITION_PLANET1[0] - POSITION_STAR[0])**2 + (POSITION_PLANET1[1] - POSITION_STAR[1])**2)
    r2 = math.sqrt((POSITION_PLANET2[0] - POSITION_STAR[0])**2 + (POSITION_PLANET2[1] - POSITION_STAR[1])**2)
    force1 = GRAVITATIONAL_CONSTANT * MASS_PLANET1 * MASS_STAR / r1**2
    force2 = GRAVITATIONAL_CONSTANT * MASS_PLANET2 * MASS_STAR / r2**2
    # Calculate the acceleration of each planet
    acceleration1 = force1 / MASS_PLANET1
    acceleration2 = force2 / MASS_PLANET2
    # Update the velocity of each planet
    VELOCITY_PLANET1 = (VELOCITY_PLANET1[0] + acceleration1 * TIMESTEP, VELOCITY_PLANET1[1] + acceleration1 * TIMESTEP)
    VELOCITY_PLANET2 = (VELOCITY_PLANET2[0] + acceleration2 * TIMESTEP, VELOCITY_PLANET2[1] + acceleration2 * TIMESTEP)
    # Update the position of each planet
    POSITION_PLANET1 = (POSITION_PLANET1[0] + VELOCITY_PLANET1[0] * TIMESTEP, POSITION_PLANET1[1] + VELOCITY_PLANET1[1] * TIMESTEP)
    POSITION_PLANET2 = (POSITION_PLANET2[0] + VELOCITY_PLANET2[0] * TIMESTEP, POSITION_PLANET2[1] + VELOCITY_PLANET2[1] * TIMESTEP)
    # Render the planets and star
    screen.fill(BLACK)
    star = pygame.draw.circle(screen, WHITE, POSITION_STAR, 10)
    planet1 = pygame.draw.circle(screen, WHITE, POSITION_PLANET1, 5)
    planet2 = pygame.draw.circle(screen, WHITE, POSITION_PLANET2, 5)
    pygame.display.flip()
    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

