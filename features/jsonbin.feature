Feature: JSONBin API CRUD Operations

  Background:
    Given the JSONBin base URL is "https://api.jsonbin.io/v3/b"
    And I set the JSONBin Master Key to "$2a$10$FhmsaLJQklqMh1VItuPEh.2NrSTiu6aCl2W9yTW1.QwDAnqaC059u"

  @create_multiple
  Scenario Outline: Create multiple JSON bins with different payloads
    When I send a POST request to create a bin named "<bin_name>" with key "<field>" and value "<value>"
    Then the response status code should be <status_code>
    And the response JSON metadata should contain a bin ID

    Examples:
      | bin_name     | field  | value   | status_code |
      | UserProfile  | role   | admin   | 200         |
      | AppConfig    | theme  | dark    | 200         |

  @create_read
  Scenario: Create and Read a JSON bin
    When I send a POST request to create a bin named "ReadTestBin" with key "status" and value "active"
    Then the response status code should be 200
    And the response JSON metadata should contain a bin ID
    When I send a GET request to read the created bin
    Then the response status code should be 200
    And the response JSON record should have key "status" with value "active"

  @create_delete
  Scenario: Create and Delete a JSON bin
    When I send a POST request to create a bin named "DeleteTestBin" with key "temp" and value "true"
    Then the response status code should be 200
    And the response JSON metadata should contain a bin ID
    When I send a DELETE request to remove the created bin
    Then the response status code should be 200
    And the response message should contain "Bin deleted successfully"