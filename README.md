# HatProbability_Simulator

## Overview
The **Hat Probability Simulator** is a Python program that models a probability experiment using a hat filled with colored balls. The program allows users to randomly draw balls from the hat and calculate the probability of drawing a specific combination of colors over multiple experiments.

## Features
- Define a hat containing balls of different colors and their counts.
- Draw a specified number of balls randomly from the hat.
- Run multiple experiments to estimate the probability of drawing an expected set of balls.
- Uses **random sampling** for an efficient and accurate probability simulation.

## How It Works
1. **Initialize the Hat**: The `Hat` class takes keyword arguments representing different colors and their counts.
   ```python
   hat = Hat(red=3, blue=2, green=5)
   ```
   This creates a hat with 3 red, 2 blue, and 5 green balls.

2. **Draw Balls Randomly**: Use the `draw` method to randomly remove a specified number of balls from the hat.
   ```python
   drawn_balls = hat.draw(4)  # Draw 4 random balls from the hat
   ```

3. **Run Probability Experiments**: The `experiment` function runs multiple experiments to estimate the likelihood of drawing a specific set of balls.
   ```python
   probability = experiment(hat, {"red": 2, "blue": 1}, num_balls_drawn=4, num_experiments=1000)
   ```
   This checks the probability of drawing at least 2 red and 1 blue ball in 4 draws, repeated 1000 times.

## Dependencies
- Python 3.x
- No external libraries required (uses built-in modules `random` and `copy`).

## Installation & Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/hat-probability-simulator.git
   cd hat-probability-simulator
   ```
2. Run the script in Python:
   ```sh
   python hat_simulator.py
   ```

## Applications
- **Statistics & Probability Education**: Helps understand probability concepts through simulation.
- **Monte Carlo Simulations**: Useful for modeling real-world probability scenarios.
- **Game Development**: Can be adapted for lottery-style games.

## License
This project is open-source under the MIT License.

---
Feel free to contribute and improve this project!

