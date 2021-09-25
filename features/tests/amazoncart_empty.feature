# Created by Archana at 9/25/2021
Feature: Test Scenario for Amazon cart check

  Scenario: User check for cart empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify cart empty text is shown


  Scenario: User adds item to cart and checks for cart
    Given Open Amazon page
    When Enter bag into search field
    When Select a bag item
    When Add the item to cart
    Then Verify count in cart icon