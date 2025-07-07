import random

class RobotBase:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.score = 0
        self.alive = True
        self.icon_color = self.setIcon()
    
    def getMoveDirection(self):
        """
        Override this method to define robot movement behavior.
        Returns:
            int: 0 for north, 1 for east, 2 for south, 3 for west
        """
        return random.randint(0, 3)
    
    def speak(self):
        """
        Override this method to define what the robot says.
        Called every 10 seconds.
        Returns:
            str: Text to display in speech bubble
        """
        return self.name
    
    def celebrate(self):
        """
        Override this method to define celebration behavior.
        Called when robot picks up a coin.
        Returns:
            str: Text to display in speech bubble
        """
        return f"{self.name} got a coin!"
    
    def setIcon(self):
        """
        Override this method to set robot icon.
        Since we can't use image files, return a color tuple.
        Returns:
            tuple: RGB color tuple (r, g, b)
        """
        # Default random color
        return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    
    def getIcon(self):
        """
        Get the robot's icon color.
        Returns:
            tuple: RGB color tuple
        """
        return self.icon_color
