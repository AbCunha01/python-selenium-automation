# Created by Ari Cunha at 12/14/2024

 Feature: Verify Empty Cart Message

Scenario: Empty Cart Message
  Given I am on the Target homepage
  When I click the cart icon
  Then Verify the 'Your cart is empty' message


  Scenario: Navigate to Sign In
  Given I am on the Target homepage
  When  I click Sign In from the navigation menu
  Then Verify that the Sign In form opened