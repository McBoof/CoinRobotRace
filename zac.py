from robot_base import RobotBase
import random

class Zac(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Zac")
    
    def getMoveDirection(self):
        """Zac moves randomly"""
        return random.randint(0, 3)
    

