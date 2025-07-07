from robot_base import RobotBase
import random

class Sophia(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Sophia")
    
    def getMoveDirection(self):
        """Sophia moves randomly"""
        return random.randint(0, 3)
    
    def celebrate(self):
        """Sophia got a coin"""
        return f"{self.name} got a coin!"

