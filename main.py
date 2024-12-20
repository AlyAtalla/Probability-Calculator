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
            all_balls = self.contents[:]
            self.contents.clear()  # Optionally clear the contents if all balls are drawn
            return all_balls
        
        # Randomly draw the specified number of balls
        drawn_balls = random.sample(self.contents, num_balls)
        
        # Remove the drawn balls from the contents
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        # Create a copy of the hat to ensure each experiment is independent
        hat_copy = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        
        # Draw balls from the hat
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the drawn balls
        drawn_count = {}
        for ball in drawn_balls:
            if ball in drawn_count:
                drawn_count[ball] += 1
            else:
                drawn_count[ball] = 1
        
        # Check if the drawn balls meet the expected criteria
        success = True
        for color, count in expected_balls.items():
            if drawn_count.get(color, 0) < count:
                success = False
                break
        
        if success:
            successful_experiments += 1

    # Calculate the probability
    probability = successful_experiments / num_experiments
    return probability

# Example usage
if __name__ == "__main__":
    hat = Hat(blue=5, red=4, green=2)
    probability = experiment(
        hat=hat,
        expected_balls={'red': 1, 'green': 2},
        num_balls_drawn=4,
        num_experiments=2000
    )

    print(probability)