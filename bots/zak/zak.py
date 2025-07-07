from robot_base import RobotBase
import random

class Zak(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Zak")
    
    def getMoveDirection(self):
        """Zak moves randomly, avoiding walls"""
        attempts = 0
        while attempts < 10:  # Prevent infinite loop
            direction = random.randint(0, 3)
            if self.movementAllowed(direction):
                return direction
            attempts += 1
        return 0  # Default fallback
    
    def celebrate(self):
        """Zak got a coin"""
        return f"{self.name} got a coin!"
