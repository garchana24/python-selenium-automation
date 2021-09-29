# Created by Archana at 9/29/2021
Feature: Test scenario to check the links in Amazon Bestsellers page


  Scenario: User checks the number of links in Bestsellers page
    Given Open Amazon page
    When Open Amazon Bestsellers page
    Then Verify if there are 5 number of links