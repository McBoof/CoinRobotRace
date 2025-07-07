import pygame
import os

# Initialize pygame
pygame.init()

# Create a simple robot icon (24x24 pixels to match tile size)
def create_robot_icon(filename):
    # Create a surface
    surface = pygame.Surface((24, 24), pygame.SRCALPHA)
    
    # Fill with transparent background
    surface.fill((0, 0, 0, 0))
    
    # Draw a simple robot shape
    # Body (rectangle)
    pygame.draw.rect(surface, (100, 100, 100), (6, 8, 12, 10))
    
    # Head (circle)
    pygame.draw.circle(surface, (150, 150, 150), (12, 6), 4)
    
    # Eyes (small circles)
    pygame.draw.circle(surface, (255, 255, 255), (10, 5), 1)
    pygame.draw.circle(surface, (255, 255, 255), (14, 5), 1)
    
    # Antenna (line)
    pygame.draw.line(surface, (200, 200, 200), (12, 2), (12, 4), 1)
    
    # Arms (rectangles)
    pygame.draw.rect(surface, (120, 120, 120), (2, 10, 4, 2))
    pygame.draw.rect(surface, (120, 120, 120), (18, 10, 4, 2))
    
    # Legs (rectangles)
    pygame.draw.rect(surface, (80, 80, 80), (8, 18, 2, 4))
    pygame.draw.rect(surface, (80, 80, 80), (14, 18, 2, 4))
    
    # Save the image
    pygame.image.save(surface, filename)

# Create robot icons for all robots
robot_names = ['noah', 'zac', 'nathan', 'eden', 'samuel', 'zak', 'william', 'sophia', 'willow', 'kate', 'katie', 'jon']

for name in robot_names:
    create_robot_icon(f"{name}.png")
    print(f"Created {name}.png")

print("All robot icons created!")