import pygame
import os

def create_robot_icon(filename, color):
    """Create a simple robot icon with the given color"""
    # Initialize pygame
    pygame.init()
    
    # Create a 24x24 surface
    surface = pygame.Surface((24, 24))
    surface.fill((255, 255, 255))  # White background
    
    # Draw robot shape
    # Head (circle)
    pygame.draw.circle(surface, color, (12, 8), 6)
    
    # Body (rectangle)
    pygame.draw.rect(surface, color, (8, 12, 8, 8))
    
    # Arms (small rectangles)
    pygame.draw.rect(surface, color, (4, 14, 3, 4))
    pygame.draw.rect(surface, color, (17, 14, 3, 4))
    
    # Eyes (black dots)
    pygame.draw.circle(surface, (0, 0, 0), (10, 7), 1)
    pygame.draw.circle(surface, (0, 0, 0), (14, 7), 1)
    
    # Save the image
    pygame.image.save(surface, filename)
    print(f"Created {filename}")

# Create unique colored icons for each robot
robots = {
    'noah': (255, 100, 100),    # Red
    'zac': (100, 255, 100),     # Green
    'nathan': (100, 100, 255),  # Blue
    'eden': (255, 255, 100),    # Yellow
    'samuel': (255, 100, 255),  # Magenta
    'zak': (100, 255, 255),     # Cyan
    'william': (255, 165, 0),   # Orange
    'sophia': (128, 0, 128),    # Purple
    'willow': (255, 192, 203),  # Pink
    'kate': (165, 42, 42),      # Brown
    'katie': (0, 128, 128),     # Teal
    'jon': (128, 128, 128)      # Gray
}

for robot_name, color in robots.items():
    filename = f"bots/{robot_name}/{robot_name}.png"
    create_robot_icon(filename, color)

print("All robot icons created successfully!")