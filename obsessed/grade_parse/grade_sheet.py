"""
This module contains all information relating to the structure of a GradeSheet, which encompasses all data in a
.gs file.
"""
from collections import namedtuple


class GradeSheet:
    """
    Overall container of all logic present in a .gs file. This object is interacted with outside of the module.
    """

    def __init__(self, header=None, categories=None):
        """
        Each GradeSheet object contains:
            - header: a Header object which contains metadata about the GradeSheet
            - categories: a set of Category objects that are relevant to a single class's grades
        """
        # TODO: add header stuff in here
        self.categories = set()

    def __eq__(self, other):
        # TODO
        pass

    def __hash__(self):
        # TODO
        pass

    def __repr__(self):
        # TODO
        pass

    def __str__(self):
        # TODO
        pass


class Header:
    # TODO: Fill this out
    """
    ...
    """

    def __init__(self):
        # TODO
        pass

    def __eq__(self, other):
        # TODO
        pass

    def __hash__(self):
        # TODO
        pass

    def __repr__(self):
        # TODO
        pass

    def __str__(self):
        # TODO
        pass


class Category:
    # TODO: Fill this out
    """
    ...
    """

    def __init__(self):
        # TODO
        pass

    def __eq__(self, other):
        # TODO
        pass

    def __hash__(self):
        # TODO
        pass

    def __repr__(self):
        # TODO
        pass

    def __str__(self):
        # TODO
        pass


# TODO: Add this in
# Grade = namedtuple()

