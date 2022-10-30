Feature: CRUD via UI

  Scenario: Create a user
    Given Via https://www.aqa.science/
    When We create a User at https://www.aqa.science/
    Then User was created successfully


  Scenario: Read a user
    Given We created a User before
    When We tried to find a created User
    Then User was successfully found

  Scenario: Update a user
    Given We created a User before
    When We tried to update a created User
    Then User was successfully updated


  Scenario: Delete a user
    Given We created a User before
    When We tried to delete a created User
    Then User was successfully deleted