Feature: Check that meteofrance is working

  Scenario: Should display a search text bar
    Given A web browser
    When I navigate to the meteofrance home page
    Then A search text bar is displayed
    When I fill the search text bar
    And I submit the form
    Then The search result contains Toulouse city
    When I click on Toulouse city
    Then Toulouse meteo is displayed