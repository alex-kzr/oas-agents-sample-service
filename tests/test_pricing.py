import unittest


class PricingTests(unittest.TestCase):
    def test_valid_order_total(self):
        from sample_service.pricing import calculate_total
        self.assertEqual(calculate_total([{'price':25,'quantity':4}]),100)

    @unittest.expectedFailure
    def test_known_discount_defect(self):
        from sample_service.pricing import calculate_total
        self.assertEqual(calculate_total([{'price':25,'quantity':4}],discount_percent=10),90)
