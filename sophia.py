from robot_base import RobotBase
import random

class Sophia(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Sophia")
        self.exploration_mode = True
        self.home_x = x
        self.home_y = y
    
    def getMoveDirection(self):
        """Sophia moves randomly"""
        return random.randint(0, 3)
    

