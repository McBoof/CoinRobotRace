import random
import pygame
import os

class RobotBase:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.score = 0
        self.alive = True
        self.world_size = 30  # Store world size for boundary checking
        self.icon_image = self.loadIcon()
    
    def getMoveDirection(self):
        """
        Override this method to define robot movement behavior.
        Returns:
            int: 0 for north, 1 for east, 2 for south, 3 for west
        """
        return random.randint(0, 3)
    
    def speak(self):
        """
        Override this method to define what the robot says.
        Called every 10 seconds.
        Returns:
            str: Text to display in speech bubble
        """
        return f"{self.name} here"
    
    def celebrate(self):
        """
        Override this method to define celebration behavior.
        Called when robot picks up a coin.
        Returns:
            str: Text to display in speech bubble
        """
        return f"{self.name} got a coin!"
    
    def loadIcon(self):
        """
        Load the robot's PNG icon.
        Returns:
            pygame.Surface: The loaded icon image
        """
        icon_path = f"bots/{self.name.lower()}/{self.name.lower()}.png"
        if os.path.exists(icon_path):
            try:
                return pygame.image.load(icon_path)
            except:
                # If loading fails, create a default colored rectangle
                surface = pygame.Surface((24, 24))
                surface.fill((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
                return surface
        else:
            # If file doesn't exist, create a default colored rectangle
            surface = pygame.Surface((24, 24))
            surface.fill((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
            return surface
    
    def getIcon(self):
        """
        Get the robot's icon image.
        Returns:
            pygame.Surface: The icon image
        """
        return self.icon_image
    
    def movementAllowed(self, direction):
        """
        Check if movement in the given direction is allowed (not hitting walls).
        Args:
            direction (int): 0 for north, 1 for east, 2 for south, 3 for west
        Returns:
            bool: True if movement is allowed, False if it would hit a wall
        """
        if direction == 0:  # North
            return self.y > 0
        elif direction == 1:  # East
            return self.x < self.world_size - 1
        elif direction == 2:  # South
            return self.y < self.world_size - 1
        elif direction == 3:  # West
            return self.x > 0
        else:
            return False

    def bashDirection(self):
        """
        Override this method to define robot bash behavior.
        Called every 5 seconds.
        Returns:
            int: 0 for north, 1 for east, 2 for south, 3 for west
        """
        import random
        return random.randint(0, 3)

    def getBashedInsult(self):
        """
        Override this method to define what insult the robot uses when bashing.
        Returns:
            str: The insult word to use (default: "bashed")
        """
        return "bashed"
