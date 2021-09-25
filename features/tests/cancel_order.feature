# Created by Archana at 9/25/2021
Feature: Test Scenario for Cancel order functionality

  Scenario: User search for cancel order help
    Given Open Amazon help page
    When Input Cancel Order in search field
    Then Verify Cancel order text is shown
