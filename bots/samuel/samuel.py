from robot_base import RobotBase
import random

class Samuel(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Samuel")
    
    def getMoveDirection(self):
        """Samuel moves randomly, avoiding walls"""
        attempts = 0
        while attempts < 10:  # Prevent infinite loop
            direction = random.randint(0, 3)
            if self.movementAllowed(direction):
                return direction
            attempts += 1
        return 0  # Default fallback
    
    def celebrate(self):
        """Samuel got a coin"""
        return f"{self.name} got a coin!"
    
    def getBashedInsult(self):
        """Samuel's bash insult"""
        return "slammed"
