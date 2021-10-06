# Created by Archana at 10/6/2021
Feature: Test scenario to verify the Bestseller page header links
  # Enter feature description here

  Scenario: User to verify Bestseller header links open the respective pages
    Given Open Amazon page
    When Open Amazon Bestsellers page
    Then Verify page by clicking on the links in header