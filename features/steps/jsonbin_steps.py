from behave import given, when, then
import requests

@given('the JSONBin base URL is "{base_url}"')
def step_set_base_url(context, base_url):
    context.base_url = base_url

@given('I set the JSONBin Master Key to "{api_key}"')
def step_set_api_key(context, api_key):
    context.headers = {
        "Content-Type": "application/json",
        "X-Master-Key": api_key
    }

@when('I send a POST request to create a bin named "{bin_name}" with key "{key}" and value "{value}"')
def step_create_bin(context, bin_name, key, value):
    headers = context.headers.copy()
    headers["X-Bin-Name"] = bin_name
    payload = {key: value}
    context.response = requests.post(context.base_url, json=payload, headers=headers)
    if context.response.status_code == 200:
        context.bin_id = context.response.json().get("metadata", {}).get("id")

@when('I send a GET request to read the created bin')
def step_read_bin(context):
    url = f"{context.base_url}/{context.bin_id}"
    context.response = requests.get(url, headers=context.headers)

@when('I send a DELETE request to remove the created bin')
def step_delete_bin(context):
    url = f"{context.base_url}/{context.bin_id}"
    context.response = requests.delete(url, headers=context.headers)

@then('the response status code should be {status_code:d}')
def step_verify_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, but got {context.response.status_code}. Body: {context.response.text}"

@then('the response JSON metadata should contain a bin ID')
def step_verify_bin_id(context):
    data = context.response.json()
    bin_id = data.get("metadata", {}).get("id")
    assert bin_id is not None, f"Bin ID missing in response: {data}"

@then('the response JSON record should have key "{key}" with value "{expected_value}"')
def step_verify_record_content(context, key, expected_value):
    data = context.response.json()
    actual_value = data.get("record", {}).get(key)
    assert actual_value == expected_value, \
        f"Expected '{expected_value}' for key '{key}', got '{actual_value}'"

@then('the response message should contain "{expected_text}"')
def step_verify_message_text(context, expected_text):
    assert expected_text in context.response.text, \
        f"Expected '{expected_text}' in response, got '{context.response.text}'"