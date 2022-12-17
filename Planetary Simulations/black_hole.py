import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Black Hole Simulation")

# Set the background color to black
screen.fill((0, 0, 0))

# Set the center of the screen as the location of the black hole
black_hole_x, black_hole_y = window_size[0] // 2, window_size[1] // 2

# Set the radius of the black hole
black_hole_radius = 100

# Set the mass of the black hole
black_hole_mass = 1000

# Set the acceleration due to gravity (G)
G = 6.67408e-11

# Set the initial velocity of an object falling into the black hole
initial_velocity = 100

# Set the time step for the simulation (dt)
dt = 0.1

# Set the initial position of the object
x, y = 0, window_size[1]

# Set the initial velocity of the object
vx, vy = initial_velocity, 0

# Set the initial acceleration of the object
ax, ay = 0, 0

# Set the mass of the object
mass = 1

# Set the color of the object
color = (255, 255, 255)

# Set the radius of the object
radius = 10

# Set the elapsed time to 0
elapsed_time = 0

# Run the simulation until the object falls into the black hole
while y > black_hole_y:
    # Calculate the acceleration of the object due to the black hole's gravity
    distance = ((black_hole_x - x)**2 + (black_hole_y - y)**2)**0.5
    ax = -G * black_hole_mass * (x - black_hole_x) / distance**3
    ay = -G * black_hole_mass * (y - black_hole_y) / distance**3

    # Update the velocity of the object using the acceleration
    vx += ax * dt
    vy += ay * dt

    # Update the position of the object using the velocity
    x += vx * dt
    y += vy * dt

    # Draw the black hole
    pygame.draw.circle(screen, (255, 255, 255), (black_hole_x, black_hole_y), black_hole_radius)

    # Draw the object
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)

    # Update the display
    pygame.display.flip()

    # Increment the elapsed time
    elapsed_time += dt

# Print the elapsed time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
