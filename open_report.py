#!/usr/bin/env python
"""Script to serve and open the Allure report"""
import subprocess
import webbrowser
import time
import os

def serve_allure_report():
    """Serve the Allure report and open it in browser"""
    report_dir = os.path.join(os.path.dirname(__file__), 'allure-report')
    
    print("=" * 60)
    print("Allure Report Server")
    print("=" * 60)
    print(f"\nReport location: {report_dir}")
    print("\nStarting Allure report server...")
    print("The report will open in your default browser.")
    print("Press Ctrl+C to stop the server.\n")
    
    try:
        # Start the Allure server
        result = subprocess.run(
            ['allure', 'open', report_dir],
            capture_output=False
        )
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
    except Exception as e:
        print(f"Error: {e}")
        print("\nTrying alternative method...")
        # Fallback: open the index.html file directly
        index_path = os.path.join(report_dir, 'index.html')
        if os.path.exists(index_path):
            webbrowser.open(f'file:///{index_path}')
            print(f"Opened report at: {index_path}")

if __name__ == "__main__":
    serve_allure_report()
