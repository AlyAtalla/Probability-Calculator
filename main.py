import random

class Hat:
    def __init__(self, **kwargs):
        # Initialize the contents of the hat based on the arguments
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # If the number of balls to draw is greater than the available balls, return all balls
        if num_balls >= len(self.contents):
            return self.contents[:]
        
        # Randomly draw the specified number of balls
        drawn_balls = random.sample(self.contents, num_balls)
        
        # Remove the drawn balls from the contents
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls