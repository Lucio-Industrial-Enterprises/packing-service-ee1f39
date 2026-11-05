import unittest

from warehouse.sku import normalize_sku


class SkuTests(unittest.TestCase):
    def test_canonical_sku(self):
        self.assertEqual(normalize_sku(" a-12 "), "A-12")

    def test_sku_normalization(self):
        for value in ("aB-12", "AB-12", "\t aB-12 \n"):
            with self.subTest(value=value):
                self.assertEqual(normalize_sku(value), "AB-12")

    def test_blank_sku(self):
        for value in ("", "  ", "\t\n"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalize_sku(value)
