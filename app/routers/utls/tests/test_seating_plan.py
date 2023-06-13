import unittest

import sys
sys.path.append("..")  # Add parent folder to sys.path
from seating_plan import generate_seating_plan


# from seating_plan import generate_seating_plan

class TestSeatingPlanGenerator(unittest.TestCase):
    theater_seating = {'A': 18, 'B': 20, 'C': 20, 'D': 20, 'E': 20, 'F': 20, 'G': 20, 'H': 20, 'I': 20, 'J': 20,
                       'K': 18, 'L': 18, 'M': 9}  # Example theater seating configuration

    def test_no_booked_seats_even_row(self):
        booked_seats = []  # No seats are booked
        headcount = 4
        selected_row = 'A'

        expected_seating_plan = [7, 8, 9, 10]  # Example expected seating plan

        seating_plan = generate_seating_plan(self.theater_seating, booked_seats, headcount, selected_row)

        self.assertEqual(seating_plan, expected_seating_plan)

    def test_no_booked_seats_odd_row(self):
        booked_seats = []  # No seats are booked
        headcount = 5
        selected_row = 'M'

        expected_seating_plan = [2, 3, 4, 5, 6]  # Example expected seating plan

        seating_plan = generate_seating_plan(self.theater_seating, booked_seats, headcount, selected_row)

        self.assertEqual(seating_plan, expected_seating_plan)


if __name__ == '__main__':
    unittest.main()
