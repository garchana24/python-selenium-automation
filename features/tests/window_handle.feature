# Created by Archana at 10/5/2021
Feature: Test scenario for window handling
  # Create a window handling test case from the class and verify that user can open amazon applications from Terms of Conditions

  Scenario: User can open and close Amazon Privacy Notice
  Given Open Amazon T&C page
  When Store original windows
  And Click on Amazon Privacy Notice link
  And Switch to the newly opened window
  Then Verify Amazon Privacy Notice page is opened
  And User can close new window
  And Switch back to original