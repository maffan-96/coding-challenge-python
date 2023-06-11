import unittest
from unittest.mock import patch
from challenge.PropertyManager import PropertyManager

class TestPropertyManager(unittest.TestCase):
    @classmethod
    
    def setUpClass(cls):
        print("\nsetUpClass method: Runs before all tests...")
    def setUp(self):
        print("\nRunning setUp method...")
        self.property_manager = PropertyManager("Alexendro", 1324)
    def tearDown(self):
        print("Running tearDown method...")
    
    @patch("builtins.input", return_value = 435)
    def test_get_valid_num(self, input): # Test with valid int
        print("Running 'get_valid_num function' to check if it returns valid int...")
        self.assertTrue(type(self.property_manager.get_valid_num("display msg"))== int, "get_valid_num class doesn' return int")

    @patch("builtins.input", return_value = "Affan")
    def test_get_valid_str(self, input): # Test with valid str
        print("Running 'get_valid_str' function to check if it returns valid str...")
        self.assertTrue(self.property_manager.get_valid_str("display msg") == "Affan", "get_valid_str class method doesn't return str")
    
    @patch("builtins.input", side_effect = ["Affan",  123])
    def test_create_applicant(self, inputs): # Test with valid str
        print("Running 'create_applicant' function to check if it adds valid applicant profile...")
        self.property_manager.create_applicant()
        self.assertTrue(self.property_manager.applicant_list[0]["name"] == "Affan", "create_applicant class method didn't add applicant name correctly")
        self.assertTrue(self.property_manager.applicant_list[0]["income"] == 123, "create_applicant class method didn't add applicant income correctly")

    @patch("builtins.input", side_effect = ["Carniceros",  450])
    def test_create_property(self, input): # Test with valid str
        print("Running 'create_property' function to check if it returns valid property...")
        self.property_manager.create_property()
        self.assertTrue(self.property_manager.property_list[0]["address"] == "Carniceros", "'create_property' class method didn't add property address correctly")
        self.assertTrue(self.property_manager.property_list[0]["rent"] == 450, "'create_applicant' class method didn't add property rent correctly")

    @patch("builtins.input", return_value = 1)
    def test_prefered_activity(self, input): # Test with valid str
        print("Running 'prefered_activity' function to check if it returns valid option...")
        self.assertTrue(self.property_manager.prefered_activity("display msg") == 1, "'prefered_activity' class method doesn't return chosen option correctly")

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass method: Runs after all tests...")
        
if __name__=='__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)