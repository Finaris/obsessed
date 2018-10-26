# Introduction

The grade sheet is used as the primary form of communication between the system and one's classes. The grammar for Obsessed's language is defined below, as well as any keywords that are used in the language.

[//]: # (TODO: Add a table of contents)
# Language Syntax
## Creating Assignment Categories

New categories of assignments can be defined in the following format:

```
"Category Name": 1, 2, 3, ...
```

The above line of code creates a new category with the name Category Name (note the enclosing quotation marks in the code). A colon will separate the name of the category, and grades will be defined in a comma-separated list. This will assume default behavior for grades, where the maximum score for an individual assignment is 100 and the weight of the category is evenly distributed across all categories (for example, if there are 5 categories then each category will have a
weight of 20%).

##### Example

Below is a sample grade sheet, where we have a class which grades all assignments out of 100 and each category has the same weight (33%):

```
"Homework": 85, 67, 23
"Tests": 79, 93
"Attendance": 75
```

## Overriding Defaults

### Using Keywords
If the user wishes to override the default behavior of a particular category, then they will be allowed to specify using a list of mappings between keywords and values enclosed in parentheses. It follows the following format:

```
"Category Name"(keyword1=value1, keyword2=value2, ...): 1, 2, 3, ...
```

In the above line, we create a new category with the name Category Name and define a list of grades. Furthermore, an additional set of parameters is provided via a list of key-value pairs enclosed in parentheses. More can be learned about keywords in the Keywords section, where specific keywords are described in greater detail.

##### Example

In the below example, two categories of assignments are created, one which is called "Homework" that is weighted at 40% of the total grade (each assignment is out of 100 points by default). The second category is "Tests," which is weighted at 60% of the total grade and each individual assignments is graded out of 50 points.

```
"Homework"(weight=.4): 85, 67, 23
"Tests"(weight=.6, max=50): 45, 36
```

### Different Maximums for Assignments in Same Category
In the case a user has varying maximum points for assignments in the same category, we can implement an inline override for the default maximum of the category. For example:
```
"[Category Name]": n/m
```
The above line will create a new category with one grade with value `n` that is graded out of `m` points.

##### Example
If a user has 5 tests, all of which are graded out of 100 (except for one which is graded out of 50), they would write the following line:
```
"Tests": 78, 90, 65, 44/50, 89
```

# Keywords

Below are definitions and examples of various keywords in the language.

## `weight`
`weight` defines the relative weight a _category_ of assignments has. If a class makes a particular category of grades, such as tests, weigh a certain percent of the class' overall grade, then `weight` will likely be modified. Values for `weight` are decimals representing the percent weight of a category with respect to the class' overall grade.

##### Example
If the user wishes to create a category named "tests" where tests are weighted as 70% of the overall class grade, they would write the following line:
```
"Tests"(weight=.7): ...
```

## `max`
`max` defines the default maximum grade for an _assignment_ within a category. By default, `max` is equal to `100`. However, if the user has assignments which grade out of different point values, the default may want to be overridden. Inline scaling of `max` will always take precedence over category defaults.

##### Example
If the user wishes to state that all homework will be graded out of 10 points, then they would write the following line:
```
"Homework"(max=10): ...
```