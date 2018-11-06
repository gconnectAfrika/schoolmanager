"""Unit Tests to ensure stability of GConnect."""
# import doctest
import os
import pep8
import unittest


class TestPEP8(unittest.TestCase):
    """Test adherence to PEP8 Style Guide.

    Exceptions can be added to setup.cfg file located in the project folder.
    Test is limited (for now) to *py files in project folder.
    For advanced examples see documentation http://pep8.readthedocs.io/en/release-1.7.x/advanced.html

    """

    def test_pep8(self):
        """Test for PEP8 compliance."""
        pep8style = pep8.StyleGuide(quiet=False, config_file='.flake8')
        files = [file for file in os.listdir() if file.endswith('.py')]

        result = pep8style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    # def test_doctest(self):
    #    """Test python code found in docstrings."""
    #    files = [fh for fh in os.listdir() if fh.endswith('.py')]
    #    for fh in files:
    #        result = doctest.testfile(os.path.abspath(fh))
    #        self.assertEqual(result.failed, 0, "Doctest failed.")


if __name__ == '__main__':
    unittest.main()
