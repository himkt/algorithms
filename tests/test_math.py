"""Test for mathematical functionalities."""

from algorithms.math import information_content
from algorithms.math import entropy
from algorithms.math import expected_length
from algorithms.math import meet_kraft_inequity

import unittest


class TestMathematicalFunctionalities(unittest.TestCase):
    """Test for mathematical functionalities."""

    def test_information_content(self):
        """Test for information content."""
        probability = 1/2
        ground_truth = 1.0  # log2 1/(1/2) = log2 2 = 1
        self.assertAlmostEqual(
            ground_truth,
            information_content(probability),
            delta=0.001
        )

    def test_entropy(self):
        """Test for entropy."""
        probabilities = [1/2, 1/4, 1/8, 1/8]
        ground_truth = 7/4
        self.assertEqual(
            ground_truth,
            entropy(probabilities)
        )

    def test_expected_length(self):
        """Test for expected length."""
        probabilities = [1/2, 1/4, 1/8, 1/8]
        codelengths = [1, 2, 4, 4]
        ground_truth = 2
        self.assertEqual(
            ground_truth,
            expected_length(probabilities, codelengths)
        )

    def test_meet_creaft_inequity(self):
        """Test for kraft inequity."""
        codelengths1 = [1, 2, 4, 4]
        self.assertTrue(meet_kraft_inequity(codelengths1))
        codelengths2 = [1, 1, 4, 4]
        self.assertFalse(meet_kraft_inequity(codelengths2))
