Feature: CRUD via API

  Scenario: Create a user
    Given Via https://www.aqa.science/
    When We create a User via API
    Then We should check that user created successfully

  @check_user
  Scenario: Read a user
    Given We created a User before via API
    When We tried to find a created User via API
    Then We should check that user successfully found

  Scenario: Update a user
    Given We created a User before via API
    When We tried to update a created User via API
    Then We should check that user was successfully updated


  Scenario: Delete a user
    Given We created a User before via API
    When We tried to delete a created User via API
    Then We should check that user was successfully deleted