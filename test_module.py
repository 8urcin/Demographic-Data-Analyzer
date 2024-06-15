import unittest
from demographic_data_analyzer import demographic_data_analyzer

class TestDemographicDataAnalyzer(unittest.TestCase):
    def test_race_count(self):
        result = demographic_data_analyzer()
        self.assertEqual(result['race_count']['White'], 27816)
        self.assertEqual(result['race_count']['Black'], 3124)
        

    def test_average_age_men(self):
        result = demographic_data_analyzer()
        self.assertAlmostEqual(result['average_age_men'], 39.4, places=1)

    def test_percentage_bachelors(self):
        result = demographic_data_analyzer()
        self.assertAlmostEqual(result['percentage_bachelors'], 16.4, places=1)

  

if __name__ == "__main__":
    unittest.main()
