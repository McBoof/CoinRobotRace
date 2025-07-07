from robot_base import RobotBase
import random

class Nathan(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Nathan")
        self.target_x = random.randint(0, 29)
        self.target_y = random.randint(0, 29)
    
    def getMoveDirection(self):
        """Nathan tries to reach random target points"""
        if self.x == self.target_x and self.y == self.target_y:
            # Reached target, pick a new one
            self.target_x = random.randint(0, 29)
            self.target_y = random.randint(0, 29)
        
        # Move toward target
        if self.x < self.target_x:
            return 1  # East
        elif self.x > self.target_x:
            return 3  # West
        elif self.y < self.target_y:
            return 2  # South
        else:
            return 0  # North
    
    def speak(self):
        return "Going places!"
    
    def celebrate(self):
        return "Nathan strikes!"
    
    def setIcon(self):
        return (100, 100, 255)  # Blue
