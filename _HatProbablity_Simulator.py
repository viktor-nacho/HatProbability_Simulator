import copy
import random

class Hat:
    def __init__(self, **color_counts):
        """
        Initializes the Hat object with a dictionary of colors and their counts.
        Example: Hat(red=3, blue=2) will create a hat with 3 red and 2 blue balls.
        """
        self.contents = []  # List to store all balls in the hat
        
        for color, count in color_counts.items():
            self.contents.extend([color] * count)  # Add 'count' number of each color
    
    def draw(self, num_balls_to_draw):
        """
        Draws a specified number of balls randomly from the hat.
        If the requested number exceeds available balls, returns all balls.
        """
        if num_balls_to_draw > len(self.contents):
            return self.contents  # Return all balls if drawing more than available
        
        drawn_balls = random.sample(self.contents, num_balls_to_draw)  # Randomly select without replacement
        for ball in drawn_balls:
            self.contents.remove(ball)  # Remove drawn balls from the hat
        
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Runs multiple experiments to determine the probability of drawing expected balls.
    
    :param hat: Hat object containing balls
    :param expected_balls: Dictionary of expected ball counts (e.g., {"red": 2, "blue": 1})
    :param num_balls_drawn: Number of balls to draw in each experiment
    :param num_experiments: Number of times to repeat the experiment
    :return: Probability of drawing at least the expected number of balls
    """
    successful_experiments = 0  # Count of experiments where expectation is met
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)  # Create a fresh copy of the hat for each experiment
        drawn_balls = hat_copy.draw(num_balls_drawn)  # Draw balls
        
        # Count occurrences of drawn colors
        drawn_count = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        
        # Check if drawn balls meet or exceed expected counts
        success = all(drawn_count.get(color, 0) >= count for color, count in expected_balls.items())
        if success:
            successful_experiments += 1
    
    return successful_experiments / num_experiments  # Probability calculation