import unittest
from app.utils import validate_dna_matrix

class TestValidateDNAMatrix(unittest.TestCase):

    def test_valid_matrix(self):
        """Test a valid DNA matrix"""
        valid_matrix = ["ATCG", "GCTA", "CGAT"]
        self.assertIsNone(validate_dna_matrix(valid_matrix))

    def test_empty_matrix(self):
        """Test an empty matrix"""
        with self.assertRaises(ValueError) as context:
            validate_dna_matrix([])
        self.assertEqual(str(context.exception), "Input matrix cannot be empty")

    def test_unequal_row_lengths(self):
        """Test a matrix with unequal row lengths"""
        invalid_matrix = ["ATCG", "GCT", "CGAT"]
        with self.assertRaises(ValueError) as context:
            validate_dna_matrix(invalid_matrix)
        self.assertEqual(str(context.exception), "Row 1 has length 3, expected 4. All rows must have the same length")

    def test_invalid_characters(self):
        """Test a matrix with invalid characters"""
        invalid_matrix = ["ATCG", "GCTA", "CGAX"]
        with self.assertRaises(ValueError) as context:
            validate_dna_matrix(invalid_matrix)
        self.assertEqual(str(context.exception), "Invalid characters {'X'} found in row 2. Only A, T, C, G are allowed")

    def test_single_row_matrix(self):
        """Test a matrix with a single row"""
        single_row_matrix = ["ATCG"]
        self.assertIsNone(validate_dna_matrix(single_row_matrix))

    def test_large_valid_matrix(self):
        """Test a large valid matrix"""
        large_matrix = ["ATCG" * 25] * 100  # 100x100 matrix
        self.assertIsNone(validate_dna_matrix(large_matrix))

    def test_lowercase_characters(self):
        """Test a matrix with lowercase characters"""
        lowercase_matrix = ["atcg", "GCTA", "CGAT"]
        with self.assertRaises(ValueError) as context:
            validate_dna_matrix(lowercase_matrix)
        error_message = str(context.exception)
        self.assertIn("Invalid characters", error_message)
        self.assertIn("found in row 0", error_message)
        self.assertIn("Only A, T, C, G are allowed", error_message)
        for char in 'acgt':
            self.assertIn(char, error_message)


    def test_empty_row(self):
        """Test a matrix with an empty row"""
        empty_row_matrix = ["ATCG", "", "CGAT"]
        with self.assertRaises(ValueError) as context:
            validate_dna_matrix(empty_row_matrix)
        self.assertEqual(str(context.exception), "Row 1 has length 0, expected 4. All rows must have the same length")

if __name__ == '__main__':
    unittest.main()
