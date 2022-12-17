import pygame
import math
import sys

class Planet:
    def __init__(self, x, y, vx, vy, radius, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.mass = mass

    def update(self, ax, ay):
        self.vx += ax
        self.vy += ay
        self.x += self.vx
        self.y += self.vy


# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create planets
sun = Planet(WIDTH / 2, HEIGHT / 2, 0, 0, 50, 1000)
earth = Planet(sun.x + 150, sun.y, 0, -2, 25, 1)
mars = Planet(sun.x + 200, sun.y, 0, -1.5, 20, 0.5)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate forces
    dx = sun.x - earth.x
    dy = sun.y - earth.y
    dist = math.sqrt(dx**2 + dy**2)
    force = (sun.mass * earth.mass) / dist**2
    earth_ax = force * dx / dist
    earth_ay = force * dy / dist

    dx = sun.x - mars.x
    dy = sun.y - mars.y
    dist = math.sqrt(dx**2 + dy**2)
    force = (sun.mass * mars.mass) / dist**2
    mars_ax = force * dx / dist
    mars_ay = force * dy / dist

    # Update positions
    earth.update(earth_ax, earth_ay)
    mars.update(mars_ax, mars_ay)

    # Draw objects
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (int(sun.x), int(sun.y)), sun.radius)
    pygame.draw.circle(screen, WHITE, (int(earth.x), int(earth.y)), earth.radius)
    pygame.draw.circle(screen, WHITE, (int(mars.x), int(mars.y)), mars.radius)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)
