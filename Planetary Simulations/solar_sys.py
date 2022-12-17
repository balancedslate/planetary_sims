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
        self.vx *= 0.99  # Reduce velocity by a small factor to simulate inertia
        self.vy *= 0.99  # Reduce velocity by a small factor to simulate inertia
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
sun = Planet(WIDTH / 2, HEIGHT / 2, 0, 0, 50, 500)
earth = Planet(sun.x + 150, sun.y, 0, -2, 25, 1)
mars = Planet(sun.x + 200, sun.y, 0, -1.5, 20, 0.5)
jupiter = Planet(sun.x + 300, sun.y, 0, -0.5, 40, 3)  # New planet

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def calculate_forces(planet1, planet2, ax, ay):
    """Calculates the forces acting on planet1 from planet2"""
    dx = planet1.x - planet2.x
    dy = planet1.y - planet2.y
    dist = math.sqrt(dx**2 + dy**2)
    if dist < planet1.radius + planet2.radius:
        dist = planet1.radius + planet2.radius
    force = (planet2.mass * planet1.mass) / dist**2
    ax += force * dx / dist
    ay += force * dy / dist
    return ax, ay

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate forces
    earth_ax = 0
    earth_ay = 0
    mars_ax = 0
    mars_ay = 0
    jupiter_ax = 0  # New variable for new planet's acceleration
    jupiter_ay = 0  # New variable for new planet's acceleration
    for planet in (sun, earth, mars, jupiter):  # Add new planet to list
        earth_ax, earth_ay = calculate_forces(earth, planet, earth_ax, earth_ay)
        mars_ax, mars_ay = calculate_forces(mars, planet, mars_ax, mars_ay)
        jupiter_ax, jupiter_ay = calculate_forces(jupiter, planet, jupiter_ax, jupiter_ay)  # Calculate force on new planet

    # Update positions
    earth.update(earth_ax, earth_ay)
    mars.update(mars_ax, mars_ay)
    jupiter.update(jupiter_ax, jupiter_ay)  # Update new planet's position

    # Draw objects
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (int(sun.x), int(sun.y)), sun.radius)
    pygame.draw.circle(screen, WHITE, (int(earth.x), int(earth.y)), earth.radius)
    pygame.draw.circle(screen, WHITE, (int(mars.x), int(mars.y)), mars.radius)
    pygame.draw.circle(screen, WHITE, (int(jupiter.x), int(jupiter.y)), jupiter.radius)  # Draw new planet

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

