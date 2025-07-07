from robot_base import RobotBase
import random

class Katie(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Katie")
    
    def getMoveDirection(self):
        """Katie moves randomly"""
        return random.randint(0, 3)
    
    def celebrate(self):
        """Katie got a coin"""
        return f"{self.name} got a coin!"