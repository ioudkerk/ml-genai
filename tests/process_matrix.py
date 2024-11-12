import unittest
from app.utils import process_dna_matrix

class TestDNAMatrixProcessor(unittest.TestCase):

    def test_valid_input(self):
        dna_matrix = [
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"
        ]
        result = process_dna_matrix(dna_matrix)
        self.assertEqual(result['dimensions'], (6, 6))
        self.assertEqual(result['matrix'], dna_matrix)
        self.assertIsInstance(result['sequences'], list)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            process_dna_matrix([])

    def test_uneven_rows(self):
        dna_matrix = [
            "ATGCGA",
            "CAGTG",
            "TTATGT",
        ]
        with self.assertRaises(ValueError):
            process_dna_matrix(dna_matrix)

    def test_horizontal_sequence(self):
        dna_matrix = [
            "AAAA",
            "ACTG",
            "CGTA",
        ]
        result = process_dna_matrix(dna_matrix)
        self.assertEqual(len(result['sequences']), 1)
        self.assertEqual(result['sequences'][0]['direction'], 'horizontal')
        self.assertEqual(result['sequences'][0]['char'], 'A')
        self.assertEqual(result['sequences'][0]['positions'], [(0, 0), (0, 1), (0, 2), (0, 3)])

    def test_vertical_sequence(self):
        dna_matrix = [
            "ACTG",
            "ACTG",
            "ACTG",
            "ACTG",
        ]
        result = process_dna_matrix(dna_matrix)
        self.assertEqual(len(result['sequences']), 4)
        self.assertTrue(any(seq['direction'] == 'vertical' for seq in result['sequences']))

    def test_diagonal_sequence(self):
        dna_matrix = [
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"
        ]
        result = process_dna_matrix(dna_matrix)
        self.assertTrue(any(seq['direction'] == 'diagonal' for seq in result['sequences']))

    def test_no_sequences(self):
        dna_matrix = [
            "ATCG",
            "CGTA",
            "GTAC",
            "TACG"
        ]
        result = process_dna_matrix(dna_matrix)
        self.assertEqual(len(result['sequences']), 0)

    def test_multiple_sequences(self):
        dna_matrix = [
            "AAAATGCGA",
            "CAGTGCAAA",
            "TTATGTTAT",
            "AGAAGGCCC",
            "CCCCTATGC",
            "TCACTGTTT"
        ]
        result = process_dna_matrix(dna_matrix)
        self.assertGreater(len(result['sequences']), 1)

    def test_boundary_sequences(self):
        dna_matrix = [
            "AAAA",
            "ACTG",
            "CGTA",
            "GTAC"
        ]
        result = process_dna_matrix(dna_matrix)
        self.assertEqual(len(result['sequences']), 1)
        self.assertEqual(result['sequences'][0]['positions'], [(0, 0), (0, 1), (0, 2), (0, 3)])

if __name__ == '__main__':
    unittest.main()
