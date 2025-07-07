from robot_base import RobotBase
import random
import pygame

class Zak(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.score = 9999999999999999999999984757384674748373636377238847474738282848848382

    

    def getMoveDirection(self):
        """Zak moves randomly, avoiding walls"""
        # Example: Check for coins in all directions (but don't use the information)
        north_distance = self.isCoinInDirection(0)  # Check north
        east_distance = self.isCoinInDirection(1)   # Check east
        south_distance = self.isCoinInDirection(2)  # Check south
        west_distance = self.isCoinInDirection(3)   # Check west
        # These values are available but we ignore them and move randomly
        
        attempts = 0
        while attempts <999999:  # Prevent infinite loop
            direction = random.randint(0, 3)
            if self.movementAllowed(direction):
                return direction
            attempts += 1
        return 0  # Default fallback
    
    def celebrate(self):
        """Zak got a coin"""
        return f"SIUUUUUU"
    
    def bashDirection(self):
        """Zak picks a random direction to bash"""
        return random.randint(0, 3)
    
    def getBashedInsult(self):
        """Zak's bash insult"""
        return insult()
        
    def insult():
        insults = ['gg','zAnked','zAnked. Sincerely.','I have made a severe and continuous lapse in my judgment.',"I'm calling the police.",'what']
        return random.choice(insults)