from robot_base import RobotBase
import random

class Kate(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Kate")
    
    def getMoveDirection(self):
        """Kate moves randomly, avoiding walls"""
        # Example: Check for coins in all directions (but don't use the information)
        north_distance = self.isCoinInDirection(0)  # Check north
        east_distance = self.isCoinInDirection(1)   # Check east
        south_distance = self.isCoinInDirection(2)  # Check south
        west_distance = self.isCoinInDirection(3)   # Check west
        # These values are available but we ignore them and move randomly
        
        attempts = 0
        while attempts < 10:  # Prevent infinite loop
            direction = random.randint(0, 3)
            if self.movementAllowed(direction):
                return direction
            attempts += 1
        return 0  # Default fallback
    
    def celebrate(self):
        """Kate got a coin"""
        return f"{self.name} got a coin!"
    
    def bashDirection(self):
        """Kate picks a random direction to bash"""
        return random.randint(0, 3)
    
    def getBashedInsult(self):
        """Kate's bash insult"""
        return "kicked"

