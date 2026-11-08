import os
import shutil
from behave.__main__ import main as behave_main
def clean_and_create_folder(folder_path):
    """Deletes a folder if it exists and recreates it."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)

if __name__ == "__main__":
    # Define paths
    allure_results_folder = "reports/allure-results"
    screenshot_folder = "screenshots"
    # 1. Perform pre-test setup
    print("Cleaning up old reports and screenshots...")
    clean_and_create_folder(allure_results_folder)
    clean_and_create_folder(screenshot_folder)
    # 2. Define Behave arguments and run tests
    behave_args = [
    "--tags", "@regression or @api",
    "--format", "allure_behave.formatter:AllureFormatter",
    "--outfile", "reports/allure-results"
    ]
    behave_main(behave_args)
    # 3. Perform post-test actions (e.g., generate report)
    print("Test execution finished. To see the report, run: allure serve reports/allure-results")
