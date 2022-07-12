Feature: Products API


@products-api
Scenario: create a product
    Given there is products lambda exists
    And there is products dynamo table exists
    When I call products post api
    Then I should see the sucess response