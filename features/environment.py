import allure
from allure_commons.types import AttachmentType
from mlflow import context
def after_scenario(context, scenario):
# Check if the scenario failed
    if scenario.status == "failed":
        try:
            # Capture screenshot
            screenshot_path = f"screenshots/{scenario.name.replace(' ', '_')}.png"
            context.page.screenshot(path=screenshot_path)
            # Attach screenshot to Allure report
            with open(screenshot_path, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name=scenario.name,
                    attachment_type=AttachmentType.PNG
                )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
    # Don't forget to close your browser page/context if you are using Playwright/Selenium
    if hasattr(context, 'page'):
        context.page.close()
