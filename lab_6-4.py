"""
Create a Python file named lab_6-4

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a list of 3 subjects that you have studied at Prep and store it as a variable.
Use a method to add a fourth subject you have studied to the end of the list.
Use a method to return the index of one of the subjects in your list.
Order the subjects alphabetically using a method.
Use a method to make a copy of this list and store it in a different variable.
Use a method to order this second list in reverse alphabetical order.
"""
#Author: Andrew Tkacs

#Initial List

subjects =["math", "English", "Science"]

#adding a variable

subjects.extend (["history"])

#return shallow copy of list

english_subjects = subjects.copy()

#sort the list (by default this functions sorts it alphabetically)

subjects.sort()

#new variable making a copy of the list

subjectscopy = subjects.copy()

#reverse order the second list

subjectscopy.reverse()