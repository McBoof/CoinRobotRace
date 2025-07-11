from robot_base import RobotBase
import random
import pygame


class Samuel(RobotBase):

    def __init__(self, x, y):
        super().__init__(x, y, "Samuel")
        self.icon_image = pygame.image.load("bots/samuel/images-12.jpeg")
        self.icon_image = pygame.transform.scale(self.icon_image, (25, 25))
        while self.alive == True:
            self.score = self.score + 1

    def getMoveDirection(self):
        """Samuel moves randomly, avoiding walls"""
        # Example: Check for coins in all directions (but don't use the information)
        north_distance = self.isCoinInDirection(0)  # Check north
        east_distance = self.isCoinInDirection(1)  # Check east
        south_distance = self.isCoinInDirection(2)  # Check south
        west_distance = self.isCoinInDirection(3)  # Check west
        # These values are available but we ignore them and move randomly
        

        attempts = 0
        while attempts < 10:  # Prevent infinite loop
            direction = random.randint(0, 3)
            if self.movementAllowed(direction):
                return direction
            attempts += 1
        return 0  # Default fallback

    def celebrate(self):
        """Letsa go!!!"""
        return "Letsa go!!!"

    def bashDirection(self):
        """Random nonsense go!"""
        return random.randint(0, 3)

    def getBashedInsult(self):
        """Excuse me, sir """
        return "bashed"
