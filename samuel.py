from robot_base import RobotBase
import random

class Samuel(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Samuel")
        self.bounce_direction = random.randint(0, 3)
    
    def getMoveDirection(self):
        """Samuel bounces around like a ball"""
        # Check if we're at world boundaries and need to bounce
        if self.x == 0 and self.bounce_direction == 3:  # Hit left wall
            self.bounce_direction = 1  # Go east
        elif self.x == 99 and self.bounce_direction == 1:  # Hit right wall
            self.bounce_direction = 3  # Go west
        elif self.y == 0 and self.bounce_direction == 0:  # Hit top wall
            self.bounce_direction = 2  # Go south
        elif self.y == 99 and self.bounce_direction == 2:  # Hit bottom wall
            self.bounce_direction = 0  # Go north
        
        return self.bounce_direction
    
    def speak(self):
        return "Bouncing around!"
    
    def celebrate(self):
        return "Samuel bounced to victory!"
    
    def setIcon(self):
        return (255, 100, 255)  # Magenta
