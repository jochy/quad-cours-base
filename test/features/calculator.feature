Feature: The calculator handles well operations

  Scenario: The calculator can sum two numbers
    Given A number 1 and a number 2
    When The calculator adds them
    Then The result is 3

  Scenario Outline: The calculator can sum two numbers
    Given A number <a> and a number <b>
    When The calculator adds them
    Then The result is <result>
    Examples:
      | a | b | result |
      | 1 | 2 | 3      |
      | 2 | 2 | 4      |
      | 5 | 5 | 10     |