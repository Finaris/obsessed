"""
This module contains all information relating to the structure of a GradeSheet, which encompasses all data in a
.gs file.
"""
import collections


class GradeSheetGeneric:
    """
    Defines a set of behaviors common to all GradeSheet objects, such as equality, hashing, string printing,
    representations, and more.
    """

    # Used to separate different fields in the string representation of a grade_sheet object.
    _STRING_FIELD_SEPARATOR = "\n-----\n"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and vars(self) == vars(other)

    def __hash__(self):
        return sum(hash(value) if isinstance(value, collections.Hashable) else hash(str(value))
                   for value in vars(self).values())

    def __str__(self):
        return self._STRING_FIELD_SEPARATOR.join("{0}: {1}".format(field.capitalize(), value)
                                                 for field, value in sorted(vars(self).items()))


class GradeSheet(GradeSheetGeneric):
    """
    Overall container of all logic present in a .gs file, such as metadata and grade categories.
    """

    def __init__(self, header=None, categories=None):
        """
        Each GradeSheet contains:
            - header: (dict) contains metadata about the GradeSheet
            - categories: (list) a list of Category objects that are relevant to a single class's grades
        """
        self.header = header
        self.categories = categories

    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__, self.header, repr(self.categories))


class Category(GradeSheetGeneric):
    """
    Contains information pertaining to a single set of class grades, including keyword modifiers and the actual grades.
    """

    def __init__(self, name, grades=None, keywords=None):
        """
        Each Category contains:
            - name: (str) the name of the specified Category
            - grades: (list) an ordered list of Grade objects pertaining to ap articular Category
            - keywords: (dict) a mapping of specified keywords to their associated values
        """
        self.name = name
        self.grades = grades
        self.keywords = keywords

    def __repr__(self):
        return "{0}({1}, {2}, {3})".format(self.__class__.__name__, self.name, repr(self.grades), self.keywords)


class Grade(GradeSheetGeneric):
    """
    Stores data relating to an individual grade in a Category.
    """

    def __init__(self, name, value, maximum=100):
        """
        Each Grade contains:
            - name: (str) the name of this Grade
            - value: (float) the score provided for this particular Grade
            - maximum: (float) the maximum amount of points possible on this assignment; default value is 100
        """
        self.name = name
        self.value = value
        self.maximum = maximum

    def __repr__(self):
        return "{0}({1}, {2}, {3})".format(self.__class__.__name__, self.name, self.value, self.maximum)
