
Feature:  Create a test case using BDD that opens target.com, clicks on the cart
  icon and verifies that “Your cart is empty” message is shown

  Scenario: Verify that the Target shopping cart is empty
    Given I am on the Target homepage (https://www.target.com/)
    When I click on the cart icon
    Then I should see the message "Your cart is empty"

  Scenario: Logged out user navigates to Sign In form
    Given I am on the Target homepage (https://www.target.com/)
    When I click on a "Sign In" element
    Then I should see the Sign In form