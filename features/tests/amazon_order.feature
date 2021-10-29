# Created by Archana at 10/11/2021
Feature: Test Scenario for logged out user sees Sign in page when clicking Orders


  Scenario:Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Return&Orders link
    Then Verify if amazon sign in page opens

  Scenario:User can search a product by selecting a department
    Given Open Amazon page
    When Select department by alias electronics
    And Enter camera into search field
    And Click on amazon search icon
    Then Verify if electronics department is selected

  Scenario:User can see the New Arrivals deals
    Given Open Amazon product B081YS2F7N page
    When Hover over the new arrivals deals
    Then Verify the user sees the New Arrivals deals