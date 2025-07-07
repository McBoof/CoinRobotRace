from robot_base import RobotBase
import random

class Eden(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Eden")
        self.spiral_step = 0
        self.spiral_direction = 0
        self.steps_in_direction = 0
        self.max_steps = 1
    
    def getMoveDirection(self):
        """Eden moves in a spiral pattern"""
        if self.steps_in_direction >= self.max_steps:
            self.spiral_direction = (self.spiral_direction + 1) % 4
            self.steps_in_direction = 0
            if self.spiral_direction % 2 == 0:  # Every other turn, increase max steps
                self.max_steps += 1
        
        self.steps_in_direction += 1
        return self.spiral_direction
    
    def speak(self):
        return "Spiraling outward!"
    
    def celebrate(self):
        return "Eden's spiral wins!"
    
    def setIcon(self):
        return (255, 255, 100)  # Yellow
