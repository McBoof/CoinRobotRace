from robot_base import RobotBase
import random

class Katie(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Katie")
        self.aggressive = True
        self.last_move = 0
    
    def getMoveDirection(self):
        """Katie moves randomly"""
        return random.randint(0, 3)
    

    

