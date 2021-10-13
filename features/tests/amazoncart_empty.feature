# Created by Archana at 9/25/2021
Feature: Test Scenario for Amazon cart check

  Scenario: User check for cart empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify cart empty text is shown


  Scenario: User adds item to cart and checks for cart
    Given Open Amazon page
    When Enter bag into search field
    And Click on amazon search icon
    And Select a bag item
    And Add the item to cart
    Then Verify count is 1 in cart icon
    Then Verify if added product is same in cart