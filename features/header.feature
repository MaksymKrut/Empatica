@home @header
Feature: Test Empatica Home page links consistency and functionality
  In order to check all existing links on Empatica Home page
  As test automation engineer
  I need to create script checking availability of links

  @final @javascript @insulated
  Scenario: User can operate with header Store menu and sub-menus
    Given I am on the home page
    When I click on Store link element
    And I click on Order Embrace watch link element
    Then I should see A gorgeous watch designed to save lives text
    Given I am on the home page
    When I click on Store link element
    And I click on Order E4 wristband link element
    Then I should see The most comfortable and accurate wristband text

#  @final @javascript @insulated
#  Scenario: User can operate with header Embrace Watch menu and sub-menus
#    Given I am on the home page
#    When I click "Embrace Watch" element
#    Then I should see "test"
#    And I should see "test"
#
#  @final @javascript @insulated
#  Scenario: User can operate with header E4 Wristband link
#    Given I am on the home page
#    When I click "E4 wristband" element
#    Then the url should contain ""
#
#  @final @javascript @insulated
#  Scenario: User can operate with header Science header link
#    Given I am on the home page
#    When I click "Science" element
#    Then the url should contain ""
#
#  @final @javascript @insulated
#  Scenario: User can operate with header Blog header link
#    Given I am on the home page
#    When I click "Blog" element
#    Then the url should contain ""
#
#  @final @javascript @insulated
#  Scenario: User can operate with header Support header link
#    Given I am on the home page
#    When I click "Support" element
#    Then the url should contain ""