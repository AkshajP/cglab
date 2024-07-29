import pygame
import random

# Initialize Pygame
pygame.init()
# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation Effects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


num_objects = 15
objects = []
for _ in range(num_objects):
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    radius = random.randint(20, 30)
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    speed_x = random.randint(-10, 10)
    speed_y = random.randint(-10, 10)
    objects.append({"x": x, "y": y, "radius": radius, "color": color, "speed_x": speed_x, "speed_y": speed_y})

running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    # Update and draw objects
    for obj in objects:
        # Move the object
        obj["x"] += obj["speed_x"]
        obj["y"] += obj["speed_y"]
    # Bounce off the edges
        if obj["x"] - obj["radius"] < 0 or obj["x"] + obj["radius"] > screen_width:
            obj["speed_x"] = -obj["speed_x"]
        if obj["y"] - obj["radius"] < 0 or obj["y"] + obj["radius"] > screen_height:
            obj["speed_y"] = -obj["speed_y"]
        # Draw the object
        pygame.draw.circle(screen, obj["color"], (obj["x"], obj["y"]), obj["radius"])
# Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS
# Quit Pygame
pygame.quit()
