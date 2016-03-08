# solver
Naive python implementation of the simplex algorithm for solving linear optimisation problems.

simplex() accepts problems in tableau form, with _**b**_ in the first column, _**c^T**_ in the first row and _**A**_ and associated slack variables in the remaining rows.

Examples can be found in /tests/test_solver.py

This has many unhandled edge cases, use at your own risk. It meets my current needs; in the future I might extend it to be more generally useful.

