from robot_base import RobotBase
import random

class Eden(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Eden")
    
    def getMoveDirection(self):
        """Eden moves randomly"""
        return random.randint(0, 3)
    
    def celebrate(self):
        """Eden got a coin"""
        return f"{self.name} got a coin!"
