# Created by affim at 1/7/2025
Feature: Target Website Testing

  Scenario: Search for a Product
    Given user is on the Target homepage
    When user searches for "iPhone 14"
    Then search results should contain "iPhone 14"

  Scenario: Verify Target Circle Benefits
    Given user is on the Target Circle page
    When user verifies benefit cells
    Then there should be at least 10 benefit cells

  Scenario: Verify user can add a Product to Cart
    Given Open Target main page
    When Search for <iPhone Case>
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Open Cart page
    Then Verify cart has <iPhone Case>
    And Verify "iPhone Case" is in search result url
    Examples:
    |product		|
    |iPhone 		|
    |iPhone Case	|
    |iPhone Cord	|


