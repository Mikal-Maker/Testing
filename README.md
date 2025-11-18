# Homework
- Name: Michael Hoshen
## Question 1) Define the following unit, integration, regression tests and when you would use each?
- Unit test: Tests a unit of code by itself. It is used to test a function or class since you can check if they are workingas intended.
- Integration test: Tests if multiple parts of code work together. It is used to test multiple modules of an application together.
- Regression test: Tests features that were already working after changes are made. This is used to make sure old code doesn't break with new updates.
## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.
- Pytest discovery: Uses the name of files to run. Looks for .py files beginning with "test_" or ending with "_test", functions beginnning with "test_" are run.
- Fixture: A ficture is a function with the @pytest.fixture decorator. It allows for data to be given for tests like arguments, making tests easier to duplicate without extra code.