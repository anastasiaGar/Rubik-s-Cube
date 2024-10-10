# Rubik's Cube Solver with A* Algorithm

Overview
This project implements a Rubik's Cube solver using the A search algorithm* combined with two heuristic functions: Manhattan Distance and Corner-Edge Sum Max. The system simulates the cube’s movements and provides both the scrambled and solved states. It also prints intermediate steps during the solution process.

Features
Cube Representation: The Rubik's Cube is modeled as a 3D cube using a 2D character array where each color is represented by a letter (e.g., R for Red, G for Green, etc.).
12 Cube Rotations: Functions to rotate any face of the cube either Clockwise (CW) or Anti-Clockwise (ACW).
A Algorithm*: Solves the Rubik’s Cube by searching for the most efficient sequence of moves.
Heuristic Functions: Combines two heuristic functions—Manhattan Distance and Corner-Edge Sum Max—to guide the A* algorithm efficiently.
Random Scramble: Ability to scramble the cube randomly and attempt to solve it.
Output of Steps: Displays the intermediate cube states throughout the solution process.
Code Structure
1. Cube Representation (Cube and Cube_random)
Cube: Represents a Rubik's Cube in its solved state using a 2D character array, where each character stands for a color.
Cube_random: Inherits from Cube but scrambles the cube using random moves.
Cube Functions:
The cube can perform 12 different movements:

FrontCW / FrontACW: Rotates the front face clockwise/anti-clockwise.
UpCW / UpACW: Rotates the top face clockwise/anti-clockwise.
DownCW / DownACW: Rotates the bottom face clockwise/anti-clockwise.
LeftCW / LeftACW: Rotates the left face clockwise/anti-clockwise.
RightCW / RightACW: Rotates the right face clockwise/anti-clockwise.
BackCW / BackACW: Rotates the back face clockwise/anti-clockwise.
printCube(): Prints the current state of the cube.

make_move(int move): Decides which rotation to perform based on the input integer (1 to 12), mapping to one of the 12 rotation functions.

Random Scramble: make_move() is used in the Cube_random version to perform a series of random moves, scrambling the cube.

2. A Solver (Astar)*
A Algorithm*: This file contains the implementation of the A* algorithm used to solve the cube.
Key Functions:
goal_reached(state): Checks if the cube is solved.
astar(): Implements the A* search algorithm with a priority queue, checking intermediate cube states and printing progress.
PriorityEntry: A class to handle priority queue entries, which includes the state of the cube and its cost. This avoids issues with tuple comparison when states have the same cost.
corner_edge_sum_max(state): Heuristic function that combines the maximum sum of the cube’s corner and edge tiles' distances, using the Manhattan Distance for calculation.
3. Final State Examples (final_state)
Contains sample input and output, demonstrating both the scrambled and solved cube states. Intermediate steps are also shown during the A* search process.
