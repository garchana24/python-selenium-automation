# Created by Archana at 10/11/2021
Feature: Test Scenario for logged out user sees Sign in page when clicking Orders


  Scenario:Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Return&Orders link
    Then Verify if amazon sign in page opens