#Entry point of the program
#Orchestrates the execution of the program
#Handles CLA
import os
from file_scanner import FileScanner
from content_analyzer import ContentAnalyzer

def main():
    path = input("Enter the path to the directory to scan: ").strip()
    if not os.path.isdir(path):
        print(f"Error: '{path}' is not a valid directory.")
        return

    scanner = FileScanner()
    analyzer = ContentAnalyzer()
    results = []

    for root, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            content = scanner.read_file(file_path)
            if content:
                sensitivity = analyzer.analyze_file(content)
                results.append({
                    'file': file_path,
                    'sensitivity': sensitivity
                })

    print("\nScan Results:")
    for result in results:
        print(f"File: {result['file']} | Sensitivity: {result['sensitivity']}")

if __name__ == '__main__':
    main()