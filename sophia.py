from robot_base import RobotBase
import random

class Sophia(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Sophia")
        self.exploration_mode = True
        self.home_x = x
        self.home_y = y
    
    def getMoveDirection(self):
        """Sophia explores and then returns home"""
        if self.exploration_mode:
            # Explore randomly
            if random.random() < 0.1:  # 10% chance to start going home
                self.exploration_mode = False
            return random.randint(0, 3)
        else:
            # Go home
            if self.x == self.home_x and self.y == self.home_y:
                self.exploration_mode = True
                return random.randint(0, 3)
            
            # Move toward home
            if self.x < self.home_x:
                return 1  # East
            elif self.x > self.home_x:
                return 3  # West
            elif self.y < self.home_y:
                return 2  # South
            else:
                return 0  # North
    
    def speak(self):
        return "Exploring the world!"
    
    def celebrate(self):
        return "Sophia's adventure pays off!"
    
    def setIcon(self):
        return (200, 100, 255)  # Purple
