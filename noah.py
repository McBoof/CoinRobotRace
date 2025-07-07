from robot_base import RobotBase
import random

class Noah(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Noah")
    
    def getMoveDirection(self):
        """Noah moves randomly"""
        return random.randint(0, 3)
    
    def celebrate(self):
        """Noah got a coin"""
        return f"{self.name} got a coin!"