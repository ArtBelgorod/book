import unittest
from city_functions import get_city_country

class CityCountryTest(unittest.TestCase):
    def test1(self):
        formatted_city_country = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago,Chile')

    def test2(self):
        formatted_city_country = get_city_country('santiago', 'chile', population = '5000000')
        self.assertEqual(formatted_city_country, 'Santiago,Chile - population 5000000!')

if __name__ == '__main__':
    unittest.main()
