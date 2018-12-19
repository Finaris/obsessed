from os.path import abspath, join, dirname
import unittest

from .. import Category
from .. import Grade
from .. import GradeSheet
from .. import ParseGradeSheet


""" Utility functions which are used in the above tests and global definitions. """


def _relative_to_absolute_path(relative_path):
    """ Converts a path relative to this file's location into an absolute one (thus making paths agnostic to the
        script's execution location).

    :param relative_path: (str) name of a path relative to this file
    :return: (str) absolute path based on the where the script was called
    """
    return abspath(join(dirname(__file__), relative_path))


""" Global definitions which are used in individual tests. """

TEST_EMPTY_GRADE_SHEET = GradeSheet()
TEST_SIMPLE_GRADE_SHEET = GradeSheet(None, [Category("Homework", grades=[Grade(None, 80), Grade(None, 90)]),
                                            Category("Tests", grades=[Grade(None, 70), Grade(None, 60)])])

# Names of files which contain certain types of grade sheet data.
EMPTY_GRADE_SHEET_FILE_NAME = _relative_to_absolute_path("mock_grade_sheets/empty.gs")
SIMPLE_NO_HEADER_GRADE_SHEET_FILE_NAME = _relative_to_absolute_path("mock_grade_sheets/simple_no_header.gs")
MULTIPLE_HEADER_AND_BODY_GRADE_SHEET_FILE_NAME = _relative_to_absolute_path("mock_grade_sheets/"
                                                                            "multiple_header_and_body.gs")
HEADER_BODY_WITH_KEYWORDS_GRADE_SHEET_FILE_NAME = _relative_to_absolute_path("mock_grade_sheets/"
                                                                             "header_body_with_keywords.gs")


""" Tests """


class TestParseFromFile(unittest.TestCase):

    def test_empty_file(self):
        expected = TEST_EMPTY_GRADE_SHEET
        actual = ParseGradeSheet.from_file(EMPTY_GRADE_SHEET_FILE_NAME)
        self.assertEqual(expected, actual)

    def test_file_with_contents(self):
        expected = TEST_SIMPLE_GRADE_SHEET
        actual = ParseGradeSheet.from_file(SIMPLE_NO_HEADER_GRADE_SHEET_FILE_NAME)
        self.assertEqual(expected, actual)


class TestParseFromString(unittest.TestCase):

    def test_empty_string(self):
        expected = TEST_EMPTY_GRADE_SHEET
        actual = ParseGradeSheet.from_string("")
        self.assertEqual(expected, actual)

    def test_string_with_contents(self):
        expected = TEST_SIMPLE_GRADE_SHEET
        raw_input = "\"Homework\": 80, 90\n\"Tests\": 70, 60"
        actual = ParseGradeSheet.from_string(raw_input)
        self.assertEqual(expected, actual)


class TestParse(unittest.TestCase):

    def test_body_no_keywords_with_no_header(self):
        expected = GradeSheet(None, [Category("Quizzes", grades=[Grade(None, 50)])])
        raw_input = "\"Quizzes\": 50"
        actual = ParseGradeSheet.from_string(raw_input)
        self.assertEqual(expected, actual)

    def test_header_with_no_body(self):
        expected = GradeSheet({'name': "Sample Name"}, None)
        raw_input = "name=\"Sample Name\""
        actual = ParseGradeSheet.from_string(raw_input)
        self.assertEqual(expected, actual)

    def test_grade_sheet_with_multiple_header_and_body(self):
        expected = GradeSheet({'name': 'Sample Grade Sheet', 'author': 'An Author'},
                              [Category("Category 1", grades=[Grade(None, 10)]),
                               Category("Category 2", grades=[Grade(None, 20), Grade(None, 30), Grade(None, 40)])])
        actual = ParseGradeSheet.from_file(MULTIPLE_HEADER_AND_BODY_GRADE_SHEET_FILE_NAME)
        self.assertEqual(expected, actual)

    def test_empty_keywords(self):
        expected = GradeSheet(None, [Category("Tests", {}, [Grade(None, 40)])])
        raw_input = "\"Tests\"(): 40"
        actual = ParseGradeSheet.from_string(raw_input)
        self.assertEqual(expected, actual)

    def test_header_body_with_keywords(self):
        expected = GradeSheet({'author': 'Anonymous', 'name': '6.813 Grades'},
                              [Category("Homework", {'weight': .4},
                                        [Grade(None, 85), Grade(None, 67), Grade(None, 23)]),
                               Category("Tests", {'weight': .5, 'max': 50}, [Grade(None, 46), Grade(None, 39)]),
                               Category("Attendance", {'weight': .1}, [Grade(None, 75)])])
        actual = ParseGradeSheet.from_file(HEADER_BODY_WITH_KEYWORDS_GRADE_SHEET_FILE_NAME)
        self.assertEqual(expected, actual)
