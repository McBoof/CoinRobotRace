from robot_base import RobotBase
import random

class Kate(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Kate")
    
    def getMoveDirection(self):
        """Kate moves randomly"""
        return random.randint(0, 3)
    
    def celebrate(self):
        """Kate got a coin"""
        return f"{self.name} got a coin!"

