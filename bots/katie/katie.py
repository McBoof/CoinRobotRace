from robot_base import RobotBase
import random

class Katie(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Katie")
    
    def getMoveDirection(self):
        """Katie moves randomly, avoiding walls"""
        attempts = 0
        while attempts < 10:  # Prevent infinite loop
            direction = random.randint(0, 3)
            if self.movementAllowed(direction):
                return direction
            attempts += 1
        return 0  # Default fallback
    
    def celebrate(self):
        """Katie got a coin"""
        return f"{self.name} got a coin!"