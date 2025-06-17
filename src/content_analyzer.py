import json
import os

# Content analysis logic
# Handles sensitivity scoring and rules
class ContentAnalyzer:
    """
    Class to analyze the content of files and determine their sensitivity score using rules from a JSON file.
    """
    def __init__(self, rules_path=None):
        if rules_path is None:
            rules_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'rules.json')
        with open(rules_path, 'r', encoding='utf-8') as f:
            self.rules = json.load(f)

    def analyze_file(self, file_content):
        return self.determine_sensitivity(file_content)

    def determine_sensitivity(self, content):
        content_lower = content.lower()
        for level, keywords in self.rules.items():
            for keyword in keywords:
                if keyword in content_lower:
                    return level
        return "unknown"