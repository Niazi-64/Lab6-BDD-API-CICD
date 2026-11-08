import os
import sys
import shutil
import argparse
from behave.__main__ import main as behave_main


def clean_and_create_folder(folder_path):
    """Deletes a folder if it exists and recreates it."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)

if __name__ == "__main__":
    allure_results_folder = "reports/allure-results"
    screenshot_folder = "screenshots"

    # 1. Pre-test setup
    print("Cleaning up old reports and screenshots...")
    clean_and_create_folder(allure_results_folder)
    clean_and_create_folder(screenshot_folder)

    # 2. Parse CLI arguments or Jenkins environment variable
    parser = argparse.ArgumentParser()
    parser.add_argument("--tags", help="Behave tags to filter scenarios", default="")
    args = parser.parse_args()

    tags_to_run = os.getenv("BEHAVE_TAGS", args.tags)

    # 3. Build Behave argument list
    behave_args = [
        "--format", "allure_behave.formatter:AllureFormatter",
        "--outfile", allure_results_folder
    ]
    if tags_to_run:
        behave_args.extend(["--tags", tags_to_run])

    behave_main(behave_args)
    print("Test execution finished. To view locally, run: allure serve reports/allure-results")
    sys.exit(exit_code)