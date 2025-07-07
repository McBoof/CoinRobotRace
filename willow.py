from robot_base import RobotBase
import random

class Willow(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Willow")
    
    def getMoveDirection(self):
        """Willow moves randomly"""
        return random.randint(0, 3)
    
    def celebrate(self):
        """Willow got a coin"""
        return f"{self.name} got a coin!"

