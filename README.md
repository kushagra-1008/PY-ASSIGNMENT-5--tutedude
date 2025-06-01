Task 1: Create a Dictionary of Student Marks
-
Problem Statement: Write a Python program that:
1. Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student’s name is not found, display an appropriate message.

MY SOLUTION.
I have defined a dictionary with student names as keys and their marks as values.
Then, I have used the input() function to take the student's name from the user.
To retrieve the marks, I used the dictionary's `.get()` function.
If the name is not found in the dictionary, it prints "Student not found", else it prints the marks of that student.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 2: Demonstrate List Slicing
-
Problem Statement: Write a Python program that:
1. Creates a list of numbers from 1 to 10.
2. Extracts the first five elements from the list.
3. Reverses these extracted elements.
4. Prints both the extracted list and the reversed list.

MY SOLUTION.
I have created an empty list and used a for loop to append numbers from 1 to 10.
Then, I sliced the first five elements using `l[0:5]` and stored them in a variable.
After that, I reversed the sliced portion using slicing with a step of -1 (`l[4::-1]`).
Finally, I printed the original list, the first five elements, and their reversed version.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
