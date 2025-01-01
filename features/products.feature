Feature: Product Management
  As a user
  I want to manage products
  So that I can keep track of my inventory

  Background:
    Given the following products exist
      | id | name    | description   | price | available | category  |
      | 1  | Hat     | A red fedora  | 59.95 | True      | Cloths    |
      | 2  | Shoes   | Running shoes | 89.99 | True      | Footwear  |
      | 3  | Jacket  | Leather jacket| 129.99| False     | Outerwear |

  Scenario: Read a Product
    When I start on the "Home Page"
    And I set the "Name" to "Hat"
    And I click the "Search" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "Hat" in the "Name" field
    And I should see "A red fedora" in the "Description" field
    And I should see "True" in the "Available" dropdown
    And I should see "Cloths" in the "Category" dropdown
    And I should see "59.95" in the "Price" field

  Scenario: Update a Product
    When I start on the "Home Page"
    And I set the "Name" to "Shoes"
    And I click the "Search" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    When I set the "Price" to "99.99"
    And I click the "Update" button
    Then I should see the message "Success"
    And I should see "99.99" in the "Price" field

  Scenario: Delete a Product
    When I start on the "Home Page"
    And I set the "Name" to "Jacket"
    And I click the "Search" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Delete" button
    Then I should see the message "Success"
    And I should not see "Jacket" in the product list

  Scenario: List all Products
    When I start on the "Home Page"
    And I click the "List All" button
    Then I should see "3" products in the list

  Scenario: Search for Products by Category
    When I start on the "Home Page"
    And I set the "Category" to "Footwear"
    And I click the "Search" button
    Then I should see the message "Success"
    And I should see "Shoes" in the results

  Scenario: Search for Products by Availability
    When I start on the "Home Page"
    And I set the "Available" dropdown to "True"
    And I click the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    And I should see "Shoes" in the results

  Scenario: Search for Products by Name
    When I start on the "Home Page"
    And I set the "Name" to "Jacket"
    And I click the "Search" button
    Then I should see the message "Success"
    And I should see "Jacket" in the results
