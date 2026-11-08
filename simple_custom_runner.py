from behave.__main__ import main as behave_main
if __name__ == "__main__":
    # Define arguments programmatically
    behave_args = [
    "--tags", "@regression",
    # You can add more behave arguments here
    ]
behave_main(behave_args)