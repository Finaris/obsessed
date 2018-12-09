import unittest
from .. import Category
from .. import Grade
from .. import GradeSheet
from .. import GradeSheetGeneric


""" Global definitions which are used in various unit tests. """

# Class definitions which inherit from GradeSheetGeneric and have varying degrees of arguments.


class GenericSubclassNoFieldsA(GradeSheetGeneric):
    pass


class GenericSubclassNoFieldsB(GradeSheetGeneric):
    pass


class GenericSubclassThreeFieldsA(GradeSheetGeneric):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GenericSubclassThreeFieldsB(GradeSheetGeneric):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# General dummy values and objects used for behavioral testing.
TEST_NAME_ONE = "Test Name One"
TEST_NAME_TWO = "Test Name Two"

TEST_VALUE_ONE = 60
TEST_VALUE_TWO = 70
TEST_VALUE_THREE = 80
DEFAULT_GRADE_MAXIMUM = 100

TEST_HEADER = {'author': 'joseph', 'name': '6.813'}
TEST_KEYWORDS = {'max': 80}

TEST_GENERIC_NO_FIELDS_A = GenericSubclassNoFieldsA()
TEST_GENERIC_NO_FIELDS_A_DUPE = GenericSubclassNoFieldsA()
TEST_GENERIC_NO_FIELDS_B = GenericSubclassNoFieldsB()
TEST_GENERIC_THREE_FIELDS_A_ONE = GenericSubclassThreeFieldsA(TEST_VALUE_ONE, TEST_VALUE_TWO)
TEST_GENERIC_THREE_FIELDS_A_ONE_DUPE = GenericSubclassThreeFieldsA(TEST_VALUE_ONE, TEST_VALUE_TWO)
TEST_GENERIC_THREE_FIELDS_A_TWO = GenericSubclassThreeFieldsA(TEST_VALUE_ONE, TEST_VALUE_THREE)
TEST_GENERIC_THREE_FIELDS_B = GenericSubclassThreeFieldsB(TEST_VALUE_ONE, TEST_VALUE_TWO)

TEST_GRADE_HOMEWORK_ONE = Grade(TEST_NAME_ONE, TEST_VALUE_ONE)
TEST_GRADE_HOMEWORK_ONE_DUPE = Grade(TEST_NAME_ONE, TEST_VALUE_ONE)
TEST_GRADE_HOMEWORK_TWO = Grade(TEST_NAME_TWO, TEST_VALUE_TWO, TEST_VALUE_THREE)

TEST_CATEGORY_ONE = Category(TEST_NAME_ONE, [TEST_GRADE_HOMEWORK_ONE, TEST_GRADE_HOMEWORK_TWO], {})
TEST_CATEGORY_ONE_DUPE = Category(TEST_NAME_ONE, [TEST_GRADE_HOMEWORK_ONE, TEST_GRADE_HOMEWORK_TWO], {})
TEST_CATEGORY_TWO = Category(TEST_NAME_TWO, [TEST_GRADE_HOMEWORK_ONE], TEST_KEYWORDS)

TEST_GRADESHEET_ONE = GradeSheet(TEST_HEADER, [TEST_CATEGORY_ONE, TEST_CATEGORY_TWO])
TEST_GRADESHEET_ONE_DUPE = GradeSheet(TEST_HEADER, [TEST_CATEGORY_ONE, TEST_CATEGORY_TWO])
TEST_GRADESHEET_TWO = GradeSheet({}, [TEST_CATEGORY_TWO])

""" Tests """


class TestGradeSheetGeneric(unittest.TestCase):
    """ Tests the various utility methods provided by GradeSheetGeneric. """

    """ Test(s) for __eq__ """
    def test_eq_dif_object_no_fields(self):
        self.assertNotEqual(TEST_GENERIC_NO_FIELDS_A, TEST_GENERIC_NO_FIELDS_B)

    def test_eq_same_object_no_fields(self):
        self.assertEqual(TEST_GENERIC_NO_FIELDS_A, TEST_GENERIC_NO_FIELDS_A_DUPE)

    def test_eq_dif_object_same_fields(self):
        self.assertNotEqual(TEST_GENERIC_THREE_FIELDS_A_ONE, TEST_GENERIC_THREE_FIELDS_B)

    def test_eq_same_object_dif_fields(self):
        self.assertNotEqual(TEST_GENERIC_THREE_FIELDS_A_ONE, TEST_GENERIC_THREE_FIELDS_A_TWO)

    def test_eq_same_object_same_fields(self):
        self.assertEqual(TEST_GENERIC_THREE_FIELDS_A_ONE, TEST_GENERIC_THREE_FIELDS_A_ONE_DUPE)

    """ Test(s) for __repr__ """
    def test_repr(self):
        expected = "{0}({1}, {2})".format(GenericSubclassThreeFieldsA.__name__, TEST_VALUE_ONE, TEST_VALUE_TWO)
        actual = repr(TEST_GENERIC_THREE_FIELDS_A_ONE)
        self.assertEqual(expected, actual)

    """ Test(s) for __str__ """
    def test_str(self):
        expected = "X: {0}{1}Y: {2}".format(TEST_VALUE_ONE, GradeSheetGeneric._STRING_FIELD_SEPARATOR, TEST_VALUE_TWO)
        actual = str(TEST_GENERIC_THREE_FIELDS_A_ONE)
        self.assertEqual(expected, actual)


class TestGradeSheet(unittest.TestCase):
    """ Test regarding the container GradeSheet object and the logic contained within it. """

    """ Test(s) for __eq__ """
    def test_eq_is_equal(self):
        self.assertEqual(TEST_GRADESHEET_ONE, TEST_GRADESHEET_ONE_DUPE)

    def test_eq_is_not_equal(self):
        self.assertNotEqual(TEST_GRADESHEET_ONE, TEST_GRADESHEET_TWO)

    """ Test(s) for __repr__ """
    def test_repr(self):
        expected = "GradeSheet({0}, {1})".format(TEST_HEADER, repr([TEST_CATEGORY_ONE, TEST_CATEGORY_TWO]))
        actual = repr(TEST_GRADESHEET_ONE)
        self.assertEqual(expected, actual)

    """ Test(s) for __str__ """
    def test_str(self):
        expected = "Header: {0}{1}Categories: {2}".format(TEST_HEADER, GradeSheetGeneric._STRING_FIELD_SEPARATOR,
                                                          str([TEST_CATEGORY_ONE, TEST_CATEGORY_TWO]))
        actual = str(TEST_GRADESHEET_ONE)
        self.assertEqual(expected, actual)


class TestCategory(unittest.TestCase):
    """ Tests regarding a Category and the logic contained within it. """

    """ Test(s) for __eq__ """
    def test_eq_is_equal(self):
        self.assertEqual(TEST_CATEGORY_ONE, TEST_CATEGORY_ONE_DUPE)

    def test_eq_is_not_equal(self):
        self.assertNotEqual(TEST_CATEGORY_ONE, TEST_CATEGORY_TWO)

    """ Test(s) for __repr__ """
    def test_repr(self):
        expected = "Category({0}, {1}, {2})".format(repr(TEST_NAME_ONE),
                                                    repr([TEST_GRADE_HOMEWORK_ONE, TEST_GRADE_HOMEWORK_TWO]), {})
        actual = repr(TEST_CATEGORY_ONE)
        self.assertEqual(expected, actual)

    """ Test(s) for __str__ """
    def test_str(self):
        expected = "Name: {0}{1}Grades: {2}{3}Keywords: {4}".format(TEST_NAME_ONE,
                                                                    GradeSheetGeneric._STRING_FIELD_SEPARATOR,
                                                                    str([TEST_GRADE_HOMEWORK_ONE,
                                                                         TEST_GRADE_HOMEWORK_TWO]),
                                                                    GradeSheetGeneric._STRING_FIELD_SEPARATOR, {})
        actual = str(TEST_CATEGORY_ONE)
        self.assertEqual(expected, actual)


class TestGrade(unittest.TestCase):
    """ Tests regarding a Grade and the logic contained within it. """

    """ Test(s) for __eq__ """
    def test_eq_is_equal(self):
        self.assertEqual(TEST_GRADE_HOMEWORK_ONE, TEST_GRADE_HOMEWORK_ONE_DUPE)

    def test_eq_is_not_equal(self):
        self.assertNotEqual(TEST_GRADE_HOMEWORK_ONE, TEST_GRADE_HOMEWORK_TWO)

    """ Test(s) for __repr__ """
    def test_repr(self):
        expected = "Grade({0}, {1}, {2})".format(repr(TEST_NAME_ONE), TEST_VALUE_ONE, DEFAULT_GRADE_MAXIMUM)
        actual = repr(TEST_GRADE_HOMEWORK_ONE)
        self.assertEqual(expected, actual)

    """ Test(s) for __str__ """
    def test_str(self):
        expected = str(TEST_GRADE_HOMEWORK_ONE)
        actual = "Name: {0}{1}Value: {2}{3}Maximum: {4}".format(TEST_NAME_ONE,
                                                                GradeSheetGeneric._STRING_FIELD_SEPARATOR,
                                                                TEST_VALUE_ONE,
                                                                GradeSheetGeneric._STRING_FIELD_SEPARATOR,
                                                                DEFAULT_GRADE_MAXIMUM)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
