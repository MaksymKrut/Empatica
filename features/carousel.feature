@home @carousel
Feature: Test Empatica Home page links consistency and functionality
  In order to check all existing links on Empatica Home page
  As test automation engineer
  I need to create script checking availability of links

  @final @javascript @insulated
  Scenario: User can operate with home pahe carousel
    Given I am on the home page
    When I click "first carousel page" element
    Then I should see "test"
    When I click "second carousel page" element
    Then I should see "test"
    When I click "third carousel page" element
    Then I should see "test"