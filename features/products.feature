Feature: Product Catalog
    As a user
    I want to manage products
    So that I can maintain the product catalog

    Background:
        Given the following products
            | name    | description       | price | available | category |
            | Hat     | Baseball hat      | 15.00 | true      | Clothing |
            | Shoes   | Running shoes     | 50.00 | true      | Clothing |
            | Big Mac | Burger            | 5.00  | true      | Food     |
            | Sheets  | Bed sheets        | 25.00 | false     | Home     |

    Scenario: Read a Product
        Given I am on the "Home Page"
        When I enter "Big Mac" in the name search field
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Big Mac" in the results
        When I copy the product Id
        And I press the "Clear" button
        And I paste the product Id
        And I press the "Retrieve" button
        Then I should see "Big Mac" in the Name field

    Scenario: Update a Product
        Given I am on the "Home Page"
        When I enter "Big Mac" in the name search field
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Big Mac" in the results
        When I copy the product Id
        And I enter "Updated Big Mac" in the Name field
        And I press the "Update" button
        Then I should see the message "Success"
        When I press the "Clear" button
        And I paste the product Id
        And I press the "Retrieve" button
        Then I should see "Updated Big Mac" in the Name field
        When I press the "Clear" button
        And I enter "Updated Big Mac" in the name search field
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Updated Big Mac" in the results

    Scenario: Delete a Product
        Given I am on the "Home Page"
        When I enter "Big Mac" in the name search field
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Big Mac" in the results
        When I copy the product Id
        And I press the "Clear" button
        And I paste the product Id
        And I press the "Delete" button
        Then I should see the message "Product has been Deleted!"
        When I press the "Clear" button
        And I enter "Big Mac" in the name search field
        And I press the "Search" button
        Then I should see the message "Success"
        And I should not see "Big Mac" in the results

    Scenario: List All Products
        Given I am on the "Home Page"
        When I press the "Clear" button
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Hat" in the results
        And I should see "Shoes" in the results
        And I should see "Big Mac" in the results
        And I should see "Sheets" in the results

    Scenario: Search Products by Category
        Given I am on the "Home Page"
        When I press the "Clear" button
        And I select "Food" in the Category field
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Big Mac" in the results
        And I should not see "Hat" in the results

    Scenario: Search Products by Availability
        Given I am on the "Home Page"
        When I press the "Clear" button
        And I select "True" in the Available field
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Hat" in the results
        And I should see "Shoes" in the results
        And I should not see "Sheets" in the results

    Scenario: Search Products by Name
        Given I am on the "Home Page"
        When I enter "Big Mac" in the name search field
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Big Mac" in the results
        And I should see "Burger" in the results
