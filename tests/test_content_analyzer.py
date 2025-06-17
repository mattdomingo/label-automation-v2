# Add src directory to sys.path so we can import ContentAnalyzer
import sys  # Import sys to manipulate the Python path
import os  # Import os for file and path operations
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))  # Add src to sys.path
from content_analyzer import ContentAnalyzer  # Import the ContentAnalyzer class from the src directory

import unittest  # Import unittest framework for testing
import json  # Import json to create a temporary rules file

class TestContentAnalyzer(unittest.TestCase):  # Define a test case class for ContentAnalyzer
    def setUp(self):  # Setup runs before each test
        # Create a temporary rules file for testing
        self.rules_path = os.path.join(os.path.dirname(__file__), 'test_rules.json')  # Path for the test rules file
        self.rules_data = {
            "confidential": ["confidential", "internal use only"],
            "pii": ["ssn", "social security number", "credit card"],
            "public": ["public", "for everyone"]
        }  # Define sample rules
        with open(self.rules_path, 'w', encoding='utf-8') as f:  # Open the rules file for writing
            json.dump(self.rules_data, f)  # Write the rules data to the file
        self.analyzer = ContentAnalyzer(self.rules_path)  # Create an instance of ContentAnalyzer with the test rules

    def tearDown(self):  # Teardown runs after each test
        if os.path.exists(self.rules_path):  # Check if the test rules file exists
            os.remove(self.rules_path)  # Remove the test rules file

    def test_confidential_detection(self):  # Test detection of confidential content
        content = "This document is confidential and should not be shared."  # Sample content
        result = self.analyzer.analyze_file(content)  # Analyze the content
        self.assertEqual(result, "confidential")  # Assert the result is 'confidential'

    def test_pii_detection(self):  # Test detection of PII content
        content = "The SSN is 123-45-6789."  # Sample content
        result = self.analyzer.analyze_file(content)  # Analyze the content
        self.assertEqual(result, "pii")  # Assert the result is 'pii'

    def test_public_detection(self):  # Test detection of public content
        content = "This information is public and for everyone."  # Sample content
        result = self.analyzer.analyze_file(content)  # Analyze the content
        self.assertEqual(result, "public")  # Assert the result is 'public'

    def test_unknown_detection(self):  # Test detection of unknown content
        content = "This is a generic document with no sensitive keywords."  # Sample content
        result = self.analyzer.analyze_file(content)  # Analyze the content
        self.assertEqual(result, "unknown")  # Assert the result is 'unknown'

if __name__ == '__main__':  # Run the tests if this file is executed directly
    unittest.main()  # Start the unittest test runner
