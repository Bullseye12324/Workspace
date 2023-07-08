# Workspace
Floyd's Algorithm Recursion Implementation

This repository contains the recursive implementation of Floyd's algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. The objective of this project is to explore an alternative approach to the original imperative version, as well as evaluate its performance and compare it with the iterative implementation.

Contents
Introduction and Hypothesis
This is contained in the assigment submission, however line 4 contains a brief summary
Directory Structure
├── FloydA.py Contains the implementation of Floyd's algorithm using recursion
├── TestfloydA.py Includes the unittests for the recursive and imperative approaches
├── performancetest.py Includes the performance test
├── testexamples.py Includes the test examples used
├── requirements.txt Conatins the dependecies to run the code
└── README.md

Installation
Clone this repository: https://github.com/Bullseye12324/Workspace.git
(https://github.com/Bullseye12324/Workspace/assets/138522173/70f903e3-475c-4f8a-8893-39dcddf9359e)

Setup your environment:python -m venv myvenv
navigate to main directory
pip install - r requirements.txt

Usage
To use the recursive implementation of Floyd's algorithm importnt the 'FloydA' module into your code

Tests
This project includes comprehensive unit tests to ensure the correctness of the recursive implementation. To run the tests, execute the following command 
python -m unitest disover TestfloydA

Performance Evaluation
To evaluate the performance of the recursive implementation, we conducted a comparative analysis with the original imperative version provided in the PDF. The performance tests focused on measuring the execution time and memory usage of both implementations using various graph sizes and structures.
See testexamples.py for an overview of these.


Results and Analysis
The performance evaluation revealed differences between the recursive and imperative versions of Floyd's algorithm. The recursive implementation exhibited longer execution times and higher memory consumption, particularly for larger graph sizes. These results align with our initial hypothesis, suggesting that the recursive approach introduces additional function call overhead and deeper call stacks, impacting performance.

Despite the performance disparities, the recursive implementation offers advantages in terms of code simplicity and clarity. Furthermore, further optimisations could potentially mitigate some of the performance differences.

Conclusion
This project explored the recursive implementation of Floyd's algorithm, providing insights into the trade-offs between the recursive and imperative approaches. The comparative performance analysis demonstrated the impact of algorithmic design choices on execution time and memory usage. The recursive implementation showcases the potential for simplicity and clarity, although it comes at the cost of performance in certain scenarios.

For more information, refer to the code documentation and the report included in this repository.
