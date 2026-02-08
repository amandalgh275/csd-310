# test_cities.py - Final version
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Test cases for city_country function."""
    
    def test_city_country(self):
        """Test city_country with just city and country."""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Test city_country with optional population parameter."""
        formatted_name = city_country('santiago', 'chile', '5000000')
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')
    
    def test_city_country_population_language(self):
        """Test city_country with optional population and language parameters."""
        formatted_name = city_country('santiago', 'chile', '5000000', 'spanish')
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000, Spanish')

if __name__ == '__main__':
    unittest.main()