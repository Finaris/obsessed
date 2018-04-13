# Introduction

The grade sheet is used as the primary form of communication between the system and one's classes.

# Language Syntax
## Defining New Assignment Categories

New categories of assignments can be defined in the following format:

```
"[Category Name]": 1, 2, 3, ... , n
```

The above line of code creates a new category with the name [Category Name] (note the enclosing quotation marks).
A colon will separate the name of the category, and grades will be defined in a comma-separated list.

# Examples

Below is a sample grade sheet, where we have a class which grades all assignments out of 100
and breaks down weights into tests (50%), homework (40%) and attendance (10%):

```
"Homework": 85, 67, 23
"Tests": 85, 78
"Attendance": 75
```

Afterwards, we can perform whatever calculations we wish with the data set.
