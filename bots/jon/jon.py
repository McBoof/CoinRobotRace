from robot_base import RobotBase
import random

class Jon(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Jon")
    
    def getMoveDirection(self):
        """Jon moves randomly, avoiding walls"""
        attempts = 0
        while attempts < 10:  # Prevent infinite loop
            direction = random.randint(0, 3)
            if self.movementAllowed(direction):
                return direction
            attempts += 1
        return 0  # Default fallback
    
    def celebrate(self):
        """Jon got a coin"""
        return f"{self.name} got a coin!"
