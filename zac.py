from robot_base import RobotBase
import random

class Zac(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Zac")
    
    def getMoveDirection(self):
        """Zac moves completely randomly"""
        return random.randint(0, 3)
    
    def speak(self):
        return "Chaos is fun!"
    
    def celebrate(self):
        return "Lucky me!"
    
    def setIcon(self):
        return (100, 255, 100)  # Green
