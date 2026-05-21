# Sports Analysis Agent

This is a Python project for my university assignment. It is an agent-based system that uses an external tool (TheSportsDB API) to fetch and display information about football teams.

# Programming Concepts Used
- OOP
- Type hinting
- Error Handling - Data Parsing

# How to run it
1. Run the main script:
   `python main.py`
2. Type the name of a team when prompted. (Note: Due to current API free-tier limits, only "Arsenal" will return full data).

# Running tests
I used `unittest` to verify that the API tool and the agent logic are working correctly. To run the tests, use this command:
`python -m unittest test_system.py`